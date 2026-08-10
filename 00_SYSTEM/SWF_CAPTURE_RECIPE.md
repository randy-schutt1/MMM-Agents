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

## 11. UNTESTED IDEA THAT WOULD REMOVE THE 1-HOUR COST

The SWF header declares its frame rate, and it is patchable in a **working copy**:

```text
V01: frameRate=3.0, frameCount=9853, stored as a 16.16 fixed value at body offset 17
     (after the 8-byte file header and the RECT; decompress CWS bodies with zlib first)
```

Raising 3 fps to, say, 120 fps should make Ruffle advance the root timeline ~40× faster
— a full sweep in ~1.5 min instead of 55. The presentation **is** the root timeline
(9853 `SHOWFRAME` tags exactly matches `frameCount`), so this has a good chance of
working.

Two unknowns: the Camtasia player may drive slides from an internal timer or audio
position rather than the root timeline, in which case nothing speeds up; and Ruffle
ticks on `requestAnimationFrame`, which headless Chrome typically caps at 60 fps, so the
practical ceiling may be ~20× rather than 40×.

**Audio would be unusable at that rate**, so this is a screenshots-only path. If you
also want the archival mp4, you still need one real-time pass.

Worth 15 minutes on V02 before committing to 20 more hours of real-time capture. If it
works, the recommendation becomes: fast sweep for screenshots by default, real-time only
when the mp4 is specifically wanted.
