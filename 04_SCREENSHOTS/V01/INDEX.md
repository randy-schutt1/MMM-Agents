# V01 — SCREENSHOT INDEX

| Field | Value |
|---|---|
| Video ID | V01 |
| Captured | 2026-08-10 — Ruffle (WASM) in headless Chrome via Playwright, recorded full-length, muxed with the SWF's own audio, frames extracted with `ffmpeg -ss` |
| Count | 22 |
| Derivative used | `V01.mp4` (1024×786, H.264, 3284.96 s) — a derivative held outside `01_SOURCE_VIDEOS/`, per `SOURCE_INGESTION_PROTOCOL.md` §2 |
| Source SHA-256 | `c7e660f4b187e0ef81c05d38cc031cb523b56ec22c0c96db4b4dd41303d84030` |

**Every image includes the player's own burned-in timecode in the bottom-right
corner.** That is deliberate: each screenshot independently proves the timestamp its
filename claims. Given this project quarantined 72 files for asserting timestamps
that did not match their content (`QUARANTINE_REGISTER.md` Q-001), self-verifying
evidence was judged worth 18 pixels of player chrome.

---

## SYNC VERIFICATION

The mp4's own position was checked against the burned-in timecode at twelve points
spanning the full runtime. **All twelve matched exactly; zero drift.**

| mp4 position | 00:05 | 05:00 | 10:00 | 15:00 | 20:00 | 25:00 | 30:00 | 35:00 | 40:00 | 45:00 | 50:00 | 54:00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burned timecode | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## INDEX

`Classification`: `SOURCE` = instructor is stating it; `VISUAL` = demonstrated on
screen; `INFERRED` = the agent's reading of the image.

| Screenshot | Timestamp | Concept | What to notice | Rule supported | Classification |
|---|---|---|---|---|---|
| `V01_00-00-35_boot-camp-intro-slide.png` | `[00:00:35]` | Course framing | Slide text matches the transcript opening almost word for word | §1 overview | SOURCE |
| `V01_00-02-35_managing-expectations-slide.png` | `[00:02:35]` | Student conduct | Five bullets: follow free from distraction; honest effort on assignments; execute in demo; refrain from negativity; take your time | S1–S7 | SOURCE |
| `V01_00-06-15_contact-email-slide.png` | `[00:06:15]` | Admin | Contact address slide | — | SOURCE |
| `V01_00-09-50_forum-layout-screenshot.png` | `[00:09:50]` | Admin | Screen capture of the reorganised forum; sections visible | H1 submission location | VISUAL |
| `V01_00-14-10_student-folder-slide.png` | `[00:14:10]` | Admin | Template / student folder instructions | S9 | SOURCE |
| `V01_00-16-55_survey-questions-1-to-9.png` | `[00:16:55]` | Curriculum | Titled **"STUDENT RATING SELF EVALUATION"**. Questions 1–9 legible | H1 | SOURCE |
| `V01_00-19-20_survey-questions-10-to-18.png` | `[00:19:20]` | Curriculum | Questions 10–18 legible, including *"10. Do you know how to read the EMA's in real time?"* | H1, A-013 | SOURCE |
| `V01_00-24-10_survey-target-and-baggage-questions.png` | `[00:24:10]` | Curriculum | IDEAL % gain target per month / per week; London vs NY; other analysis "baggage" | H2, H3 | SOURCE |
| `V01_00-27-50_teaching-26-to-90-slide.png` | `[00:27:50]` | Admin | Reads "Teaching 26 to 90 day 1" | — | SOURCE |
| `V01_00-30-35_trap-moves-are-made-list.png` | `[00:30:35]` | **Trap-move timing** | Slide **"How To Beat The Market Maker — The Trap Moves Are Made:"** listing six boundaries | **S28–S33** | **VISUAL** |
| `V01_00-38-50_beginning-of-week-chart.png` | `[00:38:50]` | Weekly cycle | Slide titled **"Beginning Of Week"**. Candles, four MA lines (yellow/red/cyan/white), a blue shaded box and a red shaded box, red and green arrows | S34, S35 | **VISUAL** |
| `V01_00-39-10_week-beginning-trap-high-label.png` | `[00:39:10]` | Weekly cycle | Same chart carrying the printed label **"Week Beginning Trap High"** | S34, W1 | **VISUAL** |
| `V01_00-39-40_beginning-of-week-drawn-on.png` | `[00:39:40]` | Weekly cycle | Instructor's live green freehand annotation added over the same chart | Steps 1–12, §5 | **VISUAL** |
| `V01_00-40-25_beginning-of-session-chart.png` | `[00:40:25]` | **Session traps** | Slide **"Beginning Of Session"**. Printed labels **"Trigger The Pendings"**, **"Trigger The Stops"**, **"Beginning Of Sessions"**. Blue box over the low flat range; red box over the post-run high | **S29–S31, A-003** | **VISUAL** |
| `V01_00-43-58_beginning-of-session-drawn-on.png` | `[00:43:58]` | Session traps | Same chart with live green annotation | S39–S41 | **VISUAL** |
| `V01_00-44-40_end-of-week-chart.png` | `[00:44:40]` | End-of-week trap | Slide **"End Of Week"**. Red box mid-chart, blue box at lower right, printed label "End Of Week" | S55–S57 | **VISUAL** |
| `V01_00-46-05_end-of-week-drawn-on.png` | `[00:46:05]` | End-of-week trap | Same chart, live annotation added | S55–S59 | **VISUAL** |
| `V01_00-48-35_trap-higher-level-long-holders.png` | `[00:48:35]` | Trap anatomy | Printed title **"Trap Here..Higher Level Long Holders"**. Boxes carry numeric labels **`R = 70.5`**, **`R = 51…`**, **`= 43.1`** | S45, S46, **A-018** | **VISUAL** |
| `V01_00-50-55_typical-week-gbpusd-m15.png` | `[00:50:55]` | **Weekly cycle** | Slide **"Typical Week"**. Chart header reads **`GBPUSD,M15`** with `Previous Days Range= 146.4`, `Current Days Range= 110.6`. Vertical day separators labelled Sunday / Monday / Tues / Wed / Friday. Printed annotations: *"Stops Are Triggered on The Weak long Holders"*, *"Lower Level Short Holders Are Now trapped"*, *"A uni-directional Swing The Rest Of The Week"*, *"Higher Level Longs Are Now Trapped"*, *"Level Not Crossed Until Late Friday"* | **S20–S26, S49–S51** | **VISUAL** |
| `V01_00-51-45_typical-week-drawn-on.png` | `[00:51:45]` | Weekly cycle | Same chart with live green annotation over the drop | S53, A-009 | **VISUAL** |
| `V01_00-52-10_typical-week-more-drawing.png` | `[00:52:10]` | Weekly cycle | Further annotation | S54–S56 | **VISUAL** |
| `V01_00-54-30_typical-week-final-state.png` | `[00:54:30]` | Weekly cycle | Final state of the annotated chart at lesson end | S60 | **VISUAL** |

---

## HOW THESE WERE PRODUCED

Full method and gotchas: `00_SYSTEM/SWF_CAPTURE_RECIPE.md`.

Summary: `ffmpeg` cannot decode these SWFs — they contain **no video stream**, only a
composited bitmap display list. Ruffle's WASM build renders them correctly in a
headless browser. The lesson was played through at 1× while Playwright recorded the
page, then the recording was trimmed to the measured playback-start offset and muxed
with the audio extracted straight from the SWF (`ffmpeg -vn -c copy`).

The source `.swf` was never modified.

## COVERAGE CHECK

| Category | Captured? | Notes |
|---|---|---|
| Definitions / diagrams | ✅ | Trap-move list `[00:30:35]`; four titled chart slides |
| Annotated charts | ✅ | Six, four of them with the instructor's live freehand drawing |
| Setup formation | ⚠️ | Shown on the instructor's prepared examples only; no live formation walk-through |
| Setup completion | ⚠️ | As above |
| Pre-entry context | ✅ | `[00:40:25]` blue box → break → red box sequence |
| Entry | ⚠️ | `[00:48:35]` is the closest; V01 states no entry trigger |
| Stop location | — | **No stop-placement rule is stated anywhere in V01** |
| Target location | — | **No target is stated anywhere in V01** |

The two `—` rows are lesson content gaps, not capture gaps. The two `⚠️` rows reflect
that V01 teaches from prepared slides rather than working a setup live.

## SELECTION METHOD, AND WHAT WAS NOT KEPT

Frames were sampled every 5 s across the full 54:44 (657 thumbnails) and compared
pairwise; 20 distinct screen states emerged. Those, plus specific moments named in
the transcript, produced 24 candidates, reviewed as contact sheets. Two were dropped
as duplicates of an adjacent state.

**The full 54:44 mp4 is retained outside the repository.** Any timestamp not indexed
here can be extracted later with `ffmpeg -ss` in about a second. Nothing was lost by
curating; this index is a selection, not the limit of what is available.
