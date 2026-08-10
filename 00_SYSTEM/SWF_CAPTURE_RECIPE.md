# SWF CAPTURE RECIPE — HOW TO PROCESS ONE LESSON VIDEO

Written for a **fresh agent session with zero prior context**. Follow it top to bottom
for V02, then V03, and so on. One video per session.

Established and validated on V01, 2026-08-10.

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
cd serve && python3 -m http.server 8899 &
```

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
await p.mouse.click(512, 300);            // <-- starts the Camtasia player
while (Date.now() - t0 < RUN_MS) { await p.waitForTimeout(60000);
  console.log('elapsed_min', ((Date.now()-t0)/60000).toFixed(1)); }
await ctx.close(); await b.close();       // ctx.close() finalises the .webm
```

- The SWF does **not** autoplay: the Camtasia player shows a play button. The
  `mouse.click(512, 300)` is what starts it. Without it you record an hour of a static
  splash screen.
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

## 10. REALISTIC TIMINGS (measured on V01)

| Phase | Wall clock | Attention |
|---|---|---|
| Setup (npm, Ruffle download, serve) | ~3 min | active, first session only |
| **Record playthrough** | **~1× video length (55 min)** | background |
| Offset + mux + encode | ~3 min | active |
| Sync verification | ~2 min | active |
| Screen detection + extraction | ~3 min | active |
| Reviewing and naming frames | ~10 min | active |
| Transcript verification | ~10 min | active |
| Source notes | ~30 min | active |
| Interpretation | ~30 min | active |
| Ambiguities / contradictions | ~20 min | active |
| Mastery report + bookkeeping + commit | ~20 min | active |

**~2.5 h of active work per lesson, plus ~1 h of unattended recording** that overlaps
with reading the transcript. Across V02–V21 that is roughly 20 hours of recording — run
it in the background, one video per session.

---

## 11. THE FRAME-RATE SPEEDUP IDEA — TESTED ON V02, IT DOES NOT WORK

**Status: RULED OUT, 2026-08-10. Do not re-attempt. Budget the full real-time hour for
every remaining lesson.**

### The idea, as it stood before testing

The SWF header declares its frame rate, and it is patchable in a **working copy**:

```text
V01: frameRate=3.0, frameCount=9853,  at body offset 17
V02: frameRate=3.0, frameCount=10861, at body offset 17
     (after the 8-byte file header and the RECT; decompress CWS bodies with zlib first)
```

Raising 3 fps to 120 fps *should* have made Ruffle advance the root timeline ~40×
faster. The arithmetic that made this look promising is real and still checks out:
V02's 10861 frames ÷ 3 fps = 3620.3 s, against a measured audio length of 3619.8 s.
**The root timeline is exactly as long as the presentation.** That is why the idea was
worth testing.

### What was tested

Three runs, each loading a patched working copy from a local HTTP origin in headless
Chrome via Playwright, clicking play, and reading the Camtasia player's own burned-in
timecode against wall clock.

| Run | Declared fps | Wall clock 60 s | Player OSD read |
|---|---|---|---|
| 1 | **120.0** (40×) | 60 s | `01:00` |
| 2 | **1.0** (⅓×) | 60 s | `01:00` |
| 3 | 3.0 (unmodified control) | 60 s | `01:00` |

Screenshots at 0/10/20/30/45/60 s in run 1 advanced exactly 10, 20, 30, 45 and 60
seconds of presentation content. At 60 s of wall clock the patched 120 fps copy was
still displaying the opening title slide.

### Why the 1 fps run is the decisive one

A 120 fps run that shows no speedup is ambiguous — it could mean the header is honoured
but something downstream caps the rate (the `requestAnimationFrame` ceiling that was
listed as unknown #2). **Patching *down* to 1 fps removes that ambiguity.** No frame
rate cap can explain a threefold *slowdown* failing to appear. Playback ran at exactly
1× in all three runs, so the declared frame rate is not being used to drive the
presentation at all.

**Conclusion: unknown #1 was the real one.** The Camtasia player drives its slides from
an internal timer or from audio position, not from the root timeline. The root timeline
is the right length, but it is not the clock.

If you test a variant of this idea on some future file, use the same two-sided design —
patch up *and* down. A one-sided test cannot distinguish "ignored" from "capped".

### Reusable code

The header parser and patcher are ~20 lines each and are worth rewriting if ever needed:
read `sig`/`version`/`fileLength` from the first 8 bytes, zlib-decompress the body for
`CWS`, skip the RECT (5-bit `nbits`, then 4 × `nbits` bits, rounded up to a byte
boundary — 17 bytes for a 1024×786 stage), then `frameRate` is a `UI16` at that offset
(8.8 fixed: `raw / 256`) followed by `frameCount` as a `UI16`. Write back as `FWS` with
`fileLength = 8 + len(body)` to avoid recompressing.

**Always patch a copy.** The originals were verified untouched by SHA-256 against
`SOURCE_MANIFEST.md` after this session's work.

### What this means for V03–V21

There is no shortcut. Each remaining lesson costs one real-time playthrough of its own
length. That is ~18 hours across V03–V21, and it is unattended background time that
overlaps with reading the transcript — which is the right way to schedule it, and is
what §10's timings already assume.

Two things make the hour cheaper than it looks, and both should be exploited:

1. **Start the recording first, before anything else.** It is the long pole and needs no
   attention. On V02 the recording was launched ~7 minutes into the session and the
   transcript verification, quarantine audit, source notes, interpretation and register
   updates were all completed while it ran. The capture cost effectively nothing.
2. **The mp4 is a permanent asset.** Once made, any future timestamp is one
   `ffmpeg -ss` away. There is no reason to ever record the same lesson twice, which
   means the archival pass and the screenshot pass are the same pass. Do not treat them
   as a value/cost tradeoff to be re-litigated per lesson — record once, keep it.
