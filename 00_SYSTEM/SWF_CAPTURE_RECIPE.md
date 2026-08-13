# SWF CAPTURE RECIPE — HOW TO PROCESS ONE LESSON VIDEO

Written for a **fresh agent session with zero prior context**. Follow it top to bottom
for V02, then V03, and so on. One video per session.

Established on V01, 2026-08-10. Fast-sweep method added on V02, same day.

---

## 0. WHAT YOU ARE DEALING WITH — READ THIS FIRST

The source files are Flash `.swf` screen recordings from 2012. **They contain no video
stream.** The screen is composited from hundreds of small bitmap tiles placed onto a
display list over time (Camtasia). Consequences:

- `ffmpeg` **cannot** extract frames. It dies after ~2 minutes with
  `pixel format change unsupported`. This is structural, not a flag you are missing.
- Parsing the SWF tags directly gives you **one** full keyframe and hundreds of 30×50px
  delta tiles. Not frames.
- Producing viewable frames requires a **Flash renderer**. Ruffle's WebAssembly build is
  one, and it works.

**`ffmpeg -vn -c copy` DOES extract the audio perfectly**, full length. It prints the
same pixel-format errors while doing it — those refer to the video stream you are
discarding. Ignore them.

### Do not waste time on these — all tested and ruled out

| Route | Why not |
|---|---|
| Building `ruffle_exporter` from source | **FORBIDDEN.** A long cargo build hung an entire session. Do not attempt. |
| Ruffle desktop release binary | GUI player only. No headless exporter asset ships in the release. |
| Ruffle JS seek API | Does not exist. `goto_frame`, `seek`, `current_frame`, `set_framerate` appear **0 times** in `ruffle.js` / `core.ruffle.*.js`. They are internal Rust symbols only. |
| `ExternalInterface` into the SWF | The SWF registers no callbacks — `addCallback` appears 0 times in its AS2 string pool. Ruffle's `callExternalInterface` has nothing to call. |
| Dragging the Camtasia scrubber to seek | It works, but lands imprecisely and non-linearly. Only viable closed-loop, which needs OCR. Not worth it. |
| CloudConvert / paid conversion services | Unnecessary. Also uploads proprietary course material to a third party. |

---

## 1. PREREQUISITES

```bash
node -v && npm -v && which ffmpeg ffprobe && python3 -c "import PIL; print('pillow ok')"
```

Playwright: install the npm package, but **do not** download its bundled Chromium — the
cached version is usually mismatched. Use the system Chrome instead via
`channel: 'chrome'`.

```bash
cd <scratchpad>/ruffle-test && npm init -y && npm install playwright
```

Ruffle self-hosted web build (this is the only download you need):

```bash
curl -sL -o ruffle-selfhosted.zip \
  "https://github.com/ruffle-rs/ruffle/releases/download/v0.5.0/ruffle-0.5.0-web-selfhosted.zip"
unzip -o -q ruffle-selfhosted.zip -d ruffle-web
```

---

## 2. SERVE THE PLAYER — `file://` WILL NOT WORK

WASM needs a real HTTP origin.

```bash
mkdir -p serve
cp ruffle-web/*.wasm ruffle-web/*.js serve/
cp "01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/<THE VIDEO>.swf" serve/vNN.swf   # a COPY

# PICK A FRESH PORT AND PROVE IT IS YOURS -- see GOTCHA 4. Do not reuse 8899.
PORT=89NN
lsof -nP -iTCP:$PORT -sTCP:LISTEN && { echo "BUSY - pick another"; exit 1; }
cd serve && python3 -m http.server $PORT & sleep 2
lsof -nP -iTCP:$PORT -sTCP:LISTEN            # must be THIS session's python PID
diff <(curl -s http://127.0.0.1:$PORT/vNN.swf | shasum -a 256 | cut -d' ' -f1) \
     <(shasum -a 256 serve/vNN.swf           | cut -d' ' -f1) || exit 1
```

> **A `200` from `curl -sI` proves nothing.** Another session's server will answer it
> happily and then serve you its own lesson. Run the two checks above. **GOTCHA 4.**

**Never modify the original `.swf`.** Work on a copy in the scratchpad
(`SOURCE_INGESTION_PROTOCOL.md` §2).

`serve/index.html`:

```html
<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;padding:0;background:#000;overflow:hidden}
</style></head><body>
<script src="ruffle.js"></script>
<script>
window.__ready = false;
const SCALE = Number(new URLSearchParams(location.search).get('scale') || 1);
window.RufflePlayer = window.RufflePlayer || {};
window.RufflePlayer.config = { autoplay: "on", unmuteOverlay: "hidden",
  warnOnUnsupportedContent: false, logLevel: "error", contextMenu: false, splashScreen: false };
window.addEventListener("load", async () => {
  const player = window.RufflePlayer.newest().createPlayer();
  window.__player = player;
  player.style.width  = (1024*SCALE) + "px";
  player.style.height = (786*SCALE) + "px";
  player.style.position = "absolute"; player.style.left = "0"; player.style.top = "0";
  document.body.appendChild(player);
  await player.load({ url: "vNN.swf" });
  window.__ready = true;
});
</script></body></html>
```

> ### GOTCHA 1 — do not clobber Ruffle's own object
> `window.RufflePlayer = { config: {...} }` **destroys** `newest()` and the page hangs
> on `__ready` forever. It must be
> `window.RufflePlayer = window.RufflePlayer || {}` then set `.config`.
> This cost a debugging cycle on V01.

---

## 3. RECORD THE PLAYTHROUGH — REAL TIME, ~1 HOUR

> **Not the default any more.** For screenshots use the 10× fast sweep in **§10**, which
> does a 60-minute lesson in ~6 minutes. Use this real-time path only when you want the
> synced audio+video mp4 as an archival asset. §§4–6 (offset, mux, sync verify) apply
> only to this path.

Run it in the background. Check the duration in `SOURCE_MANIFEST.md` and add ~40 s of
margin.

```js
// record_full.mjs
import { chromium } from 'playwright';
const RUN_MS = <duration_seconds + 40> * 1000;
const b = await chromium.launch({ channel: 'chrome',
  args: ['--autoplay-policy=no-user-gesture-required','--mute-audio'] });
const ctx = await b.newContext({
  viewport: { width: 1024, height: 786 }, deviceScaleFactor: 1,
  recordVideo: { dir: 'vidfull', size: { width: 1024, height: 786 } },
});
const p = await ctx.newPage();
await p.goto('http://127.0.0.1:8899/index.html?scale=1', { waitUntil: 'load' });
await p.waitForFunction('window.__ready === true', { timeout: 60000 });
await p.waitForTimeout(3000);
const t0 = Date.now();
await p.mouse.click(PLAY_X, PLAY_Y);      // <-- starts the Camtasia player. NOT a constant:
                                          //     read it from the stage size, GOTCHA 5
while (Date.now() - t0 < RUN_MS) { await p.waitForTimeout(60000);
  console.log('elapsed_min', ((Date.now()-t0)/60000).toFixed(1)); }
await ctx.close(); await b.close();       // ctx.close() finalises the .webm
```

- The SWF does **not** autoplay: the Camtasia player shows a play button, and a click on it is
  what starts playback. **Without it you record an hour of a static splash screen — and nothing
  downstream looks wrong when that happens.** ⚠ **The click coordinate is NOT a constant.** It
  depends on the file's declared stage size, and this library holds two. **Read `GOTCHA 5` before
  you use any number here**, and set `PLAY_X` / `PLAY_Y` from it:

  ```text
  1024 x 786 stage  ->  (512, 300)     eighteen of the twenty-one files
  1280 x 738 stage  ->  (512, 325)     V08, V09, V21
  ```
- `ctx.close()` must be called or the `.webm` is never finalised.
- Console output is extremely noisy (AVM1 warnings). Filter with `grep -v "^\[console\]"`.

**Check sync 15 minutes in rather than discovering a problem at 55.** The partial
`.webm` is readable while being written:

```bash
cp vidfull/*.webm /tmp/partial.webm
ffmpeg -v error -y -ss 904 -i /tmp/partial.webm -frames:v 1 \
  -vf "crop=90:20:934:766,scale=360:80" check.png     # read the burned-in timecode
```

---

## 4. FIND THE OFFSET — THE STEP MOST LIKELY TO GO WRONG

Recording starts *before* playback does. The gap varies per run (**4.00 s** on one V01
run, **3.40 s** on another) — **measure it, never assume it.**

```bash
mkdir -p align
ffmpeg -v error -y -t 8.0 -i vidfull/*.webm \
  -vf "fps=25,crop=700:500:160:120,scale=175:125" align/a_%04d.png
```

```python
from PIL import Image, ImageChops
import glob
prev=None
for i,f in enumerate(sorted(glob.glob('align/a_*.png'))):
    im=Image.open(f).convert('L')
    if prev:
        h=ImageChops.difference(im,prev).histogram(); n=sum(h)
        m=sum(k*v for k,v in enumerate(h))/n
        if m>0.4: print(f'{i/25:5.2f}  {m:7.2f}')
    prev=im
```

**The largest diff (~75) is playback start.** That is your offset.

> ### GOTCHA 2 — do not derive the offset from the on-screen timecode
> The Camtasia OSD updates lazily and has 1-second granularity. Deriving the offset from
> its `00:00`→`00:01` transition gave 3.3 s when the true value was 4.0 s. Use the
> frame-diff. Use the OSD only to *verify* afterwards.

---

## 5. EXTRACT AUDIO AND MUX

```bash
ffmpeg -v error -y -i "<original>.swf" -vn -c:a copy audio.mp3     # errors are expected
ffprobe -v error -show_entries format=duration -of csv=p=0 audio.mp3   # must match manifest

ffmpeg -v error -y -ss <OFFSET> -accurate_seek -i vidfull/*.webm \
  -i audio.mp3 -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p \
  -c:a aac -b:a 96k -movflags +faststart -shortest VNN.mp4
```

> ### GOTCHA 3 — `-ss` placement
> `-ss` **before `-i <video>`** trims the video. Putting it before `-i <audio>` trims the
> *audio* instead and silently shifts sync by the offset amount. Symptom: every burned
> timecode reads exactly `offset` seconds low. Check the flag order before re-recording
> anything.

Expect ~2 MB/min (≈100–130 MB per lesson) and ~45× real-time encode (≈60–90 s).

## 6. VERIFY SYNC — MANDATORY, DO NOT SKIP

The player burns its own timecode into the bottom-right of every frame. In a correctly
synced mp4, **mp4 position == burned timecode** at every point.

```bash
for t in 5 300 600 900 1200 1500 1800 2100 2400 2700 3000 3240; do
  ffmpeg -v error -y -ss $t -i VNN.mp4 -frames:v 1 \
    -vf "crop=90:20:934:766,scale=360:80:flags=lanczos" "sync/q_$t.png"
done
```

Stack them into a strip and read them. **All must match.** V01: 12/12 exact, zero drift.
If they are all off by the same constant, your offset is wrong — re-mux, do not
re-record. If the error *grows*, the recording dropped frames — re-record under lower
system load.

## 7. FIND THE DISTINCT SCREENS

`ffmpeg` scene detection under-detects on a slide deck with a uniform background (it
found 11 changes in V01 at threshold 0.30, missing most). Sample and diff instead:

```bash
ffmpeg -v error -y -i VNN.mp4 -vf "fps=1/5,crop=1024:768:0:0,scale=256:192" -q:v 4 thumbs/t_%04d.jpg
```

Then pairwise-diff consecutive thumbnails, keep `mean > 6.0`, and collapse runs within
10 s. V01: 657 thumbnails → 20 distinct screen states.

Combine those with the timestamps the transcript flags as visually important. Extract
candidates, **build contact sheets, and look at them before naming anything.**

## 8. EXTRACT AND NAME

```bash
ffmpeg -v error -y -ss <seconds> -i VNN.mp4 -frames:v 1 "VNN_HH-MM-SS_descriptor.png"
```

- **Keep the full 1024×786 frame including the control bar.** The burned-in timecode
  makes each screenshot prove its own timestamp — valuable in a project that quarantined
  72 files for claiming timestamps that did not match content.
- Descriptors: lowercase, hyphenated, 2–5 words, **what is shown, not what it means**
  (`FILE_NAMING_STANDARD.md` §3).
- **Look at each frame before naming it.** Naming from the transcript alone reproduces
  the exact failure that produced the quarantined `VISUAL_INDEX.md`.

Target ~20–25 images per lesson (V01: 22, ~11 MB). The full mp4 is retained outside the
repo, so anything not curated can be pulled later in about a second.

## 9. THEN DO THE STUDY WORK

Order matters — it is what keeps interpretation honest:

1. **Transcript first.** Verify it before trusting it (`SETUP_ISSUES.md` I-008 — 20 of
   21 transcripts are still unverified). Check: final timestamp vs measured duration;
   monotonic timestamps; does it preserve its own ASR errors and crosstalk? A fabricated
   transcript does not invent its own mishearings.
2. **`VNN_SOURCE_NOTES.md` from the transcript alone**, before looking at screenshots.
3. **`VNN_INTERPRETATION.md`**, still transcript-only, with honest confidence grades.
4. **Then** the screenshots, added as a **new section** — never by rewriting §§1–9.

> ### Why step 4 comes last, and why it is the whole point
> On V01 the visuals **corrected an over-generalisation** I had made from audio (I had
> widened a closed list of six trap-move boundaries into "every session boundary"), and
> **resolved a word I had refused to guess** ("pendings", printed on a slide, never
> spoken). Had the screenshots been available while writing the notes, neither the error
> nor the refusal would be visible in the record. Keeping the two passes separate is
> what lets a reviewer see which conclusions survive on audio alone.

Then: ambiguities (`A-NNN`), contradictions (`C-NNN`), `VNN_MASTERY_REPORT.md`,
`COURSE_PROGRESS.md`, `LOG.md`, `scripts/validate_project.py`, commit.

**Stop before the review.** `VNN_REVIEW_R1.md` is written by a *separate* session
(`REVIEW_PROTOCOL.md`); the student cannot audit itself.

---

## 10. THE FRAME-RATE SPEEDUP — TESTED, IT WORKS, 40×

**Status: CONFIRMED WORKING, 2026-08-10 on V02. This is now the default method for
screenshots.** Real-time capture (§3) is only needed when you specifically want a synced
audio+video mp4.

### The patch

The SWF header declares its frame rate, and it is patchable in a **working copy**.

> ### ⚠ THE DECLARED RATE VARIES ACROSS THIS LIBRARY. READ IT; DO NOT ASSUME IT.
> **Corrected 2026-08-13 by `18_REVIEW/V10/V10_REVIEW_R1.md`, on open item 87 raised by the
> V10 student session.** Until this correction §10 quoted `3.0` from V01/V02 as though it were
> the library's constant, and instructed *"Patch 3.0 → 30.0 fps"*. **V10 declares 2.0.** A
> session following the old prose on V10 would have patched 2.0 → 30.0 and swept at **15×, not
> 10×** — and it **fails silently**, producing a complete, well-formed, correctly-timecoded
> frame set at **7.5 presentation-seconds** apart instead of 5, under-sampling the screen-state
> detector by a third. **Same family as `GOTCHA 4` and `GOTCHA 5`: a header field that varies
> across the library, quoted as a constant, with no loud failure when it is wrong.**
>
> **THE RULE: read `frameRate` from the header of the file you are about to capture, and patch
> it to `rate × SPEED`. Never type a literal.** `GOTCHA 5`'s stage-size probe already parses
> the header immediately before this field, so the value is already in hand.

**Measured examples — data points, NOT the library's constant:**

```text
V01: frameRate=3.0, frameCount=9853,  at body offset 17
V02: frameRate=3.0, frameCount=10861, at body offset 17
V10: frameRate=2.0, frameCount=11553, at body offset 17
     (after the 8-byte file header and the RECT; decompress CWS bodies with zlib first)
```

**V10 is the cross-check proving this field must be read:** 11,553 frames ÷ 2.0 fps = 5776.5 s,
against measured audio of 5776.222 s and a `SOURCE_MANIFEST.md` duration of 5776 s — three
independent figures agreeing, and none of them consistent with 3.0.

Parser/patcher: read `sig`/`version`/`fileLength` from the first 8 bytes; zlib-decompress
the body for `CWS`; skip the RECT (5-bit `nbits`, then 4 × `nbits` bits, rounded up to a
byte boundary — 17 bytes for a 1024×786 stage); `frameRate` is a `UI16` there (8.8 fixed,
`raw / 256`), followed by `frameCount` as a `UI16`. Write back as `FWS` with
`fileLength = 8 + len(body)` so you never have to recompress.

**Always patch a copy.** Verify the originals by SHA-256 against `SOURCE_MANIFEST.md`
afterwards.

### Measured speedup

| Wall clock | 120 fps patched | 3 fps control (V02's declared rate) |
|---|---|---|
| 20 s | 13:20 | 00:20 |
| 40 s | 26:40 | 00:40 |
| 60 s | 40:00 | 01:00 |

**Exactly 40×, linear.** Both unknowns from the original proposal resolved favourably:
the Camtasia player *does* follow the root timeline, and Ruffle's `requestAnimationFrame`
tick is *not* a ceiling — it advances as many timeline frames per tick as the declared
rate demands. The burned-in timecode advances correctly at speed, so every screenshot
still proves its own timestamp.

### Use 10×, not 40×

**Patch `declared_rate × 10`** — 3.0 → **30.0** on V01/V02, 2.0 → **20.0** on V10. A 60-minute
lesson then sweeps in ~6 minutes, and a screenshot every 0.5 s of wall clock gives exactly the
5-second sampling grid §7 wants — **but only if the multiplier really is 10, which is only true
if the patched rate was derived from this file's own declared rate.**

> *Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this sentence read:*
> *"~~Patch 3.0 → **30.0 fps**.~~"* — corrected 2026-08-13, open item 87.

40× works, but it compresses screenshot cadence until Playwright's own capture latency
dominates and leaves less margin for correct delta-tile compositing. Speed is no longer the
bottleneck.

```js
// sweep.mjs — 10x, screenshot every 5 presentation-seconds
// DECLARED_FPS comes from THIS file's header (see the warning above).
// Do NOT hardcode 3.0: V01/V02 declare 3.0, V10 declares 2.0.
const SPEED=10, DECLARED_FPS=<read_from_header>;
const PATCH_FPS=DECLARED_FPS*SPEED;               // 30.0 on V01/V02, 20.0 on V10
const PRES_S=<duration_s>, STEP_PRES=5;
const STEP_MS=STEP_PRES*1000/SPEED;               // 500 ms wall
const N=Math.ceil(PRES_S/STEP_PRES)+8;
await p.goto(`http://127.0.0.1:${PORT}/index.html?scale=1&swf=v02_x10.swf`,{waitUntil:'load'});
await p.waitForFunction('window.__ready === true',{timeout:60000});
await p.waitForTimeout(2500);
const t0=Date.now();

// PLAY_X/PLAY_Y come from the stage size -- see GOTCHA 5. Do NOT hardcode (512,300).
const before = await p.screenshot();
await p.mouse.click(PLAY_X, PLAY_Y);
await p.waitForTimeout(1500);
const after = await p.screenshot();
if (Buffer.compare(before, after) === 0) {
  console.error('PLAY CLICK MISSED -- the stage did not change in 1.5 s. Aborting.');
  await ctx.close(); await b.close();
  process.exit(1);                       // <-- non-zero. Do not sweep a splash screen.
}

for(let i=0;i<N;i++){
  const w=t0+i*STEP_MS-Date.now(); if(w>0) await p.waitForTimeout(w);
  await p.screenshot({path:`sweep/s_${String(i).padStart(4,'0')}.png`});
}
```

**The before/after guard is not optional and it is not belt-and-braces.** It is the only check
that has ever caught this failure at the time it happened rather than an hour later. See
`GOTCHA 5`.

Audio is unusable at any speedup, so this is a screenshots-only path. For the archival
mp4 you still need one real-time pass (§3) — decide per lesson whether that is wanted.

---

> ### GOTCHA 4 — VERIFY THE PORT AND THE BYTES, OR YOU WILL CAPTURE THE WRONG FILM
>
> **This cost an entire 61-minute capture, a wrong decision record (D-020), and two
> confident-but-false findings about the source library.** Read it before you serve
> anything.
>
> `python3 -m http.server 8899` **fails silently if the port is busy** — it prints an
> "Address already in use" line and exits, leaving whatever was already there to answer.
> Multiple agent sessions share this machine and this repo, and a previous lesson's
> server is very likely still running on the port the recipe told you to use. That
> server's `index.html` loads **its own** SWF and ignores your `?swf=` parameter.
>
> The trap is that everything downstream looks healthy: the page loads, Ruffle
> initialises, `__ready` goes true, playback starts, the timecode burns in, a valid
> hour-long `.webm` is produced. It is simply the wrong lesson.
>
> `curl -sI ... | head -3` returning `200` **does not confirm your server is running.**
> It confirms *a* server is running. That is the check that failed here.
>
> ```bash
> PORT=8917   # pick a fresh one per session; do not reuse 8899 by reflex
> lsof -nP -iTCP:$PORT -sTCP:LISTEN && { echo "BUSY - pick another"; exit 1; }
> cd serve && python3 -m http.server $PORT & sleep 2
> lsof -nP -iTCP:$PORT -sTCP:LISTEN          # must show THIS session's python PID
> diff <(curl -s http://127.0.0.1:$PORT/vNN.swf | shasum -a 256 | cut -d' ' -f1) \
>      <(shasum -a 256 serve/vNN.swf          | cut -d' ' -f1) || exit 1
> ```
>
> **Also give every served file a unique name.** Reusing `probe_tmp.swf` across files
> lets browser/HTTP caching hand back a stale body — that produced a second false result
> here, a survey of all 21 lessons that appeared to show every file declaring an
> identical 54:44 duration. It was one file, twenty-one times.
>
> **And sanity-check content against the transcript early.** The port collision was
> finally caught because the slides did not match what the instructor was saying. One
> screenshot at a known timestamp, compared against the transcript, would have caught it
> in the first two minutes instead of after an hour. Do that before any long capture.

---

> ### GOTCHA 5 — THE PLAY-BUTTON COORDINATE IS PER-STAGE-SIZE, NOT A CONSTANT — AND IT HAS ALREADY COST TWO CAPTURES
>
> **Added 2026-08-13 by the V09 R1 reviewer**, from `18_REVIEW/V09/V09_REVIEW_R1.md` §16. This is a
> `D-038a` policy-ledger edit: the V08 and V09 sessions both hit this, both diagnosed it correctly,
> and neither could fix it here from a task branch.
>
> **The failure, twice, in the same shape.** V08's first sweep produced **529 identical frames** of
> the Camtasia splash. V09's first sweep produced **638**. In both cases the recipe's
> `mouse.click(512, 300)` **missed the play button**, which sits at approximately **`(512, 325)`**
> on those files. **Nothing downstream looked wrong either time**: the port was verified, the bytes
> matched, `__ready` went true, and hundreds of valid PNGs were written. Both were caught only by
> **opening a frame and looking at it**.
>
> **The cause, measured rather than reasoned about.** The stage rectangle is a declared field in the
> SWF header, and this library holds **two** sizes:
>
> ```text
> 1280 x 738   Bootcamp1 Wk2 032612 Part3 (43mins).swf     <- V08
> 1280 x 738   Bootcamp1 Wk2 032612 Part4 (53mins).swf     <- V09
> 1280 x 738   Bootcamp1 Wk10 061712 (75mins).swf          <- V21
> 1024 x 786   ...the other eighteen files
> ```
>
> The Playwright viewport in §3 and §10 is `1024 x 786`. Ruffle fits a `1280 x 738` stage into it at
> scale **0.8**, letterboxed vertically — visible in the committed frames as uniform dark bands at
> roughly rows `0-160` and `685-785`, which V06/V07 frames do not have. **So every viewport
> coordinate calibrated on a 1024x786 file is displaced on a 1280x738 one.** It is not a per-file
> oddity, it is a property of a header field, and it is checkable in seconds.
>
> **Read the stage size FIRST. It costs one command:**
>
> ```bash
> python3 - "$SWF" <<'EOF'
> import sys, zlib
> d = open(sys.argv[1], 'rb').read(8192)
> body = zlib.decompressobj().decompress(d[8:]) if d[:3] == b'CWS' else d[8:]
> bits = ''.join(f'{b:08b}' for b in body[:24]); nb = int(bits[:5], 2); p = 5; v = []
> for _ in range(4):
>     x = int(bits[p:p+nb], 2) - ((1 << nb) if bits[p] == '1' else 0); v.append(x); p += nb
> print('stage', (v[1]-v[0])//20, 'x', (v[3]-v[2])//20)
> EOF
> ```
>
> | Stage | Play coordinate |
> |---|---|
> | `1024 x 786` | `(512, 300)` |
> | `1280 x 738` | `(512, 325)` |
>
> **Do not trust the table alone.** A third stage size may exist in material this project has not
> opened, and the burned-in player chrome is not guaranteed to sit in the same place forever.
> **Confirm the target from a pre-click screenshot**, or use the general fix below, which needs no
> table at all.
>
> ### THE GENERAL FIX — SCREENSHOT BEFORE AND AFTER THE CLICK, AND ABORT IF THEY ARE IDENTICAL
>
> This is V08's own remedy, adopted here as the standard rather than left in one lesson's index.
> It is in the §10 script above. It does not care what the stage size is, it costs 1.5 seconds, and
> it converts a silent hour-long failure into a non-zero exit **at the moment it happens**.
>
> **The lesson generalises past this coordinate**, and it is the same one `D-020`'s retraction and
> `GOTCHA 4` record in different costumes: **verify the input reached the system under test before
> you trust any output.** A pipeline that produces well-formed artifacts is not evidence that it
> produced the right ones.

---

## 11. REALISTIC TIMINGS (V01 real-time; V02 fast-sweep)

| Phase | Wall clock | Attention |
|---|---|---|
| Setup (npm, Ruffle download, serve, **port verification**) | ~4 min | active, first session only |
| **Fast screenshot sweep @10×** | **~6 min per 60-min lesson** | background |
| *(optional)* real-time pass for the archival mp4 | ~1× video length | background |
| Screen detection + extraction | ~3 min | active |
| Reviewing and naming frames | ~10 min | active |
| Transcript verification (incl. Whisper spot-checks) | ~12 min | mostly unattended |
| Source notes | ~30 min | active |
| Interpretation | ~30 min | active |
| Ambiguities / contradictions | ~20 min | active |
| Mastery report + bookkeeping + commit | ~20 min | active |

**~2.5 h of active work per lesson.** The hour of unattended recording is no longer
mandatory — it is now a per-lesson choice about whether the archival mp4 is wanted.
