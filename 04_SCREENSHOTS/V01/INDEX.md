# V01 — SCREENSHOT INDEX

| Field | Value |
|---|---|
| Video ID | V01 |
| Captured | **None** — extraction blocked, see below |
| Count | 0 |

---

## INDEX

| Screenshot | Timestamp | Concept | What to notice | Rule supported | Classification | Related homework |
|---|---|---|---|---|---|---|
| _(none captured)_ | | | | | | |

---

## WHY THERE ARE NO SCREENSHOTS

`SETUP_ISSUES.md` I-006. The source files are Flash `.swf` screen recordings from
2012, and every automated route tried in this session failed for a reason that is now
understood rather than merely observed:

**1. `ffmpeg` cannot decode these files past roughly two minutes.** It aborts with
`pixel format change unsupported`.

**2. The reason is structural, not a bug to work around.** Parsing the SWF tag
stream directly shows what the container actually holds for V01:

```text
SHOWFRAME tags .................. 9,853   (3.0 fps × 3,284 s = the full 54:44)
DefineBitsJPEG2 (JPEG images) ...   389
DefineBitsLossless (bitmaps) ....   603
DefineShape3 ....................   658
PlaceObject2 ....................   537
DefineSprite ....................   503
```

There is no video stream. The screen is composited from hundreds of small bitmap
tiles placed onto a display list over time — the standard Camtasia-style
screen-recording layout. Extracting the image tags directly yields **one** full
1024×768 keyframe (at `00:00:00`) and 388 delta tiles of 26×38 to 72×56 pixels:
cursor sprites and changed screen regions, not frames.

Reconstructing viewable frames therefore requires evaluating the display list —
i.e. a Flash renderer. No amount of `ffmpeg` invocation will produce them.

**3. Ruffle was checked and ruled out within the time box.** The current release
(v0.5.0) ships `ruffle-0.5.0-macos-universal.tar.gz` — a GUI desktop player. There is
no headless `exporter` asset in the release. Frame export exists only in the
`ruffle_exporter` crate, which means a from-source Rust build; that is explicitly
out of bounds after it hung a previous session. **No download was made.**

**4. What remains open.** CloudConvert, when the project owner is back at his own
machine (currently expected Thursday), converting the `.swf` files to a real video
container that `ffmpeg` can then sample normally. That is the live route.

## PLACEHOLDERS — WHAT WOULD BE CAPTURED

If extraction becomes available, these are the moments to capture, in priority order.
Sourced from `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md` § SCREENSHOT-WORTHY MOMENTS.

| Priority | Timestamp | What is shown | What it would resolve |
|---|---|---|---|
| 1 | `[00:38:57]`–`[00:40:23]` | The weekly-cycle diagram — "tracer" lines for Sunday/Monday, the rise, the pullback holding the level, the stop hunt, the drop away from the peak, the crossover, the anchor point | A-001 (anchor point), A-008 (tracer), A-015 (what the dealer shows). The single highest-value capture in the lesson. |
| 2 | `[00:51:42]`–`[00:51:56]` | "Stop hunt high drop", "straight drop with a little pin" being pointed at | A-009. Fourteen seconds of audio names four formations and describes none. |
| 3 | `[00:43:53]`–`[00:44:33]` | Chart with the "blue box"; the trade shown sits outside it | A-006. Would establish whether the box is a session range or a price zone — two mutually exclusive readings. |
| 4 | `[00:45:55]`–`[00:46:35]` | The "red box" with US-session times marked | N9–N11 in the source notes — the session times are garbled beyond recovery in audio; the slide is the only route. |
| 5 | `[00:34:47]`–`[00:35:15]` | Whatever is on screen while the anchor point is introduced | A-001, A-010, and I7 — whether anchor point and peak formation are the same object. |
| 6 | `[00:16:02]`–`[00:22:07]` | Slide listing survey questions 1–18 | The instructor's numbering collapses at `[00:20:43]`; the slide is the only reliable copy. Curriculum evidence rather than trading evidence. |
| 7 | `[00:44:36]`–`[00:45:02]` | End-of-week: short, outside spike to the low, chop | A-016. |
| 8 | `[00:52:03]` | GBP chart from "when the pound was a dollar fifty" | CL3 — the instructor's own claim that the cycle is era-invariant. |
| 9 | `[00:48:41]` | The "big entry candle" | A-017. |
| 10 | `[00:09:42]`–`[00:11:53]` | Forum layout slide | Administrative only. Lowest value. |

## FALLBACK — TRADINGVIEW RECREATIONS

The project owner has approved recreating the referenced chart moments in TradingView
where a real screenshot cannot be obtained.

**Not started.** That is a separate, later step and was deliberately not begun in this
session.

When it is done, it must go to `09_CHART_EXAMPLES/`, **never** to `04_SCREENSHOTS/`,
and each image needs a sidecar stating that it is a recreation, not a course
screenshot. `SETUP_ISSUES.md` I-006 is unambiguous: *"Do not substitute generated,
illustrative, or reconstructed images for real course screenshots under any
circumstances."* A recreation is evidence of what a described setup looks like on a
chart; it is never evidence of what the instructor showed.

The only recreation candidate with a real anchor is `[00:40:26]` — USDCHF and EURUSD,
week ending Friday 2012-03-16, the only instruments and date named in the lesson.
Everything else in V01 is described without an instrument or a date, so a recreation
would be illustrating the agent's reading rather than the instructor's example.

## THE ONE EXISTING IMAGE

`01_SOURCE_VIDEOS/.../01_Bootcamp1_Wk1_031812_Part1_55mins/SCREENSHOTS/VIDEO_01_SCREENSHOT_001_00-02-00.jpg`
(manifest X26) survives from an earlier extraction attempt. Its filename asserts
`00:02:00`; that claim is unverified. It has **not** been copied here and is **not**
cited as evidence in any V01 artifact.

The quarantined `VISUAL_INDEX.md` for this video described 78 screenshots in detail.
One image exists, and its filename matches none of the descriptions. See
`00_SYSTEM/QUARANTINE_REGISTER.md` Q-001.

---

## COVERAGE CHECK

| Category | Captured? | Notes |
|---|---|---|
| Definitions / diagrams | ❌ | The weekly-cycle diagram at `[00:38:57]` is the lesson's central visual |
| Annotated charts | ❌ | Six distinct charts referenced, none captured |
| Setup formation | ❌ | |
| Setup completion | ❌ | |
| Pre-entry context | ❌ | |
| Entry | ❌ | `[00:48:41]` "big entry candle" |
| Stop location | — | No stop-placement rule is given anywhere in V01 |
| Target location | — | No target is given anywhere in V01 |

**Assessment.** Roughly the last 21 minutes of this lesson is narration over prepared
slides — `[00:38:13]` "I'm not drawing. I just have a slide up. I'm going to show
pictures." The instructor speaks deictically throughout: "this", "right here", "these
two lines", "where I've drawn it". About half of what was taught is in the visual
channel and none of it was recovered.

Every artifact derived from V01 carries this limitation. It is the main reason no
item in `V01_INTERPRETATION.md` is classified `VISUAL`.
