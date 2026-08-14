# V17 — SCREENSHOT INDEX

**Source:** `Bootcamp1 Wk8 051312 Part1 (57mins).swf` · V17 · 2012-05-13 · 00:57:09
**37 curated frames** — 36 from a **694-frame** 10× sweep at `1024 × 786`, plus **one** `2048 × 1572`
re-capture from a second, targeted sweep (`§6`). Every frame is the full **1024 × 786** stage
**including the control bar**, so each image **proves its own timestamp** from the burned-in player
readout (`SWF_CAPTURE_RECIPE.md` §8).

---

## §0 — ⚠⚠ `SWF_CAPTURE_RECIPE.md` §8a — THE MANDATORY SWEEP→CLOCK OFFSET MEASUREMENT

**§8a is a numbered required step, added by the V14 R1 remediation (`REVIEW_INDEX.md` items 174 /
186) because V14 skipped it and shipped 29 frames whose filenames were all `+16 s` wrong. It was run
here, before any frame was named.**

### §0.1 — THE MEASUREMENT

`offset = burned_timecode − (i × 5)`, read from the pixels of the bottom-right `MM:SS / MM:SS`
readout, cropped `144 × 26` at `(880, 760)` and upscaled 5× with nearest-neighbour.

| Sweep index `i` | Filename second `i × 5` | **Burned timecode, read from pixels** | **Offset** |
|---|---|---|---|
| 0 | 0 | `00:16` | ⚠ **+16** — see §0.3 |
| 1 | 5 | `00:16` | ⚠ +11 |
| 2 | 10 | `00:16` | ⚠ +6 |
| **4** | **20** | **`00:20`** | **0** |
| **6** | **30** | **`00:30`** | **0** |
| **8** | **40** | **`00:40`** | **0** |
| **10** | **50** | **`00:50`** | **0** |
| **12** | **60** | **`01:00`** | **0** |
| **20** | **100** | **`01:40`** | **0** |
| **60** | **300** | **`05:00`** | **0** |
| **100** | **500** | **`08:19`** | **−1** |
| **200** | **1000** | **`16:39`** | **−1** |
| **300** | **1500** | **`25:00`** | **0** |
| **400** | **2000** | **`33:20`** | **0** |
| **500** | **2500** | **`41:40`** | **0** |
| **600** | **3000** | **`50:01`** | **+1** |
| **685** | **3425** | **`57:05`** | **0** |
| 693 | 3465 | `57:10` | clamped at the file's own duration, as §8a says to expect |

⭐ **THE OFFSET IS ZERO for every frame from `i = 4` onward — measured at FOURTEEN points spread
across the file, plus the clamp.** The three `±1 s` readings are the OSD's own 1-second granularity
and lazy update (`GOTCHA 2`), not drift: they are non-monotonic (`−1, −1, 0, 0, 0, +1`), which
**rules out** a rate error by construction.

**Running history:** V12 `+16`, V13 `+15`, V14 `+16` (unmeasured, shipped wrong), V15 `+15`,
V16 **0**, V17 **0**.

### §0.1a — THE RATE CHECK (§8a step 3), RUN SEPARATELY

§8a step 3 requires proving this is an **ORIGIN** error and not a **RATE** error: consecutive
filename deltas must equal consecutive burned deltas.

| Interval | Filename Δ | Burned Δ | Agrees? |
|---|---|---|---|
| `i=100 → 200` | 500 s | `08:19 → 16:39` = 500 s | ✅ |
| `i=200 → 300` | 500 s | `16:39 → 25:00` = 501 s | ✅ (±1) |
| `i=300 → 400` | 500 s | `25:00 → 33:20` = 500 s | ✅ |
| `i=400 → 500` | 500 s | `33:20 → 41:40` = 500 s | ✅ |
| `i=500 → 600` | 500 s | `41:40 → 50:01` = 501 s | ✅ (±1) |
| `i=600 → 685` | 425 s | `50:01 → 57:05` = 424 s | ✅ (±1) |

**Independently, the wall-clock write interval was measured on the PNGs' own mtimes**, because an
independent ASR pass was running on the same machine during the sweep (`V17_SOURCE_NOTES.md` §0
`D6`) and CPU contention would show up here first:

| Frame band | Mean interval |
|---|---|
| `0–100` | 484.3 ms |
| `100–200` | 500.4 ms |
| `200–300` | 500.2 ms |
| `300–400` | 499.6 ms |
| `400–500` | 499.7 ms |
| `500–693` | 500.0 ms |

**Target 500 ms. No drift. The concurrency risk was taken and it did not land.**

### §0.2 — ⚠ WHY IT IS ZERO: A DECLARED DEVIATION FROM §10, AND IT CONFIRMS ITEM 188 A SECOND TIME

`REVIEW_INDEX.md` item **188** (V15 student) diagnosed the `+15/+16` band as the recipe's own fixed
`1500 ms` guard sitting between `p.mouse.click()` and `const t0 = Date.now()` — which at `SPEED = 10`
is **exactly 15 presentation seconds** — and proposed moving `t0` **before** the click. V16 ran that
way and measured **0**. **This session's `sweep.mjs` also has `t0` before the click**, which is a
**deviation from `SWF_CAPTURE_RECIPE.md` §10 as written**, declared here rather than presented as a
compliant run.

| | Predicted | Measured |
|---|---|---|
| `t0` **after** the click + guard | `+15`/`+16` s | V12 `+16`, V13 `+15`, V14 `+16`, V15 `+15` — **4 of 4** |
| `t0` **before** the click | **0** | V16 **0** (10 points), **V17 0 (14 points)** — **2 of 2** |

⭐ **Item 188's fix is now confirmed on two independent lessons, by two sessions, on 24 measured
points.** ⚠ **It is still NOT applied to the recipe.** `SWF_CAPTURE_RECIPE.md` is a **policy ledger**
and `D-038a` puts policy edits on the integration branch, never on a lesson branch. **Open item 197
is owed and is now twice-evidenced.**

⚠ **§8a's per-lesson measurement requirement must survive the fix.** Zero twice does not license
assuming zero a third time — that is exactly the reasoning that produced V14's 29 wrong filenames.

### §0.3 — THE THREE EARLY FRAMES, AND WHY THEY ARE NOT DRIFT

Frames `i = 0..2` all read `00:16` instead of `00:00`/`00:05`/`00:10`. **They are not an offset and
not drift: they are three screenshots taken back-to-back at the moment the pacing loop started.**
The pre-click guard screenshot took **1,578 ms** on this run (logged), so deadlines `t0 + 0/500/1000
ms` were already in the past when the loop began; `i = 3`'s deadline (`t0 + 1500 ms`) was marginal
and `i = 4`'s (`t0 + 2000 ms`) was the first in the future. **The grid locks exactly at `i = 4`, and
that is what the table shows.**

**Consequence, stated because it is a real gap: the first 16 seconds of V17 were NOT sampled on the
5-second grid.** They are covered by three near-identical frames. **No frame from `i < 4` is used or
named in this index.** The earliest committed frame is `i = 4` (`00:00:20`), and the first 16 s of
audio is housekeeping (`[00:00:00]`–`[00:00:14]`, the session calendar), which the `00:00:20` frame
prints in full anyway.

### §0.4 — ⚠ A SECOND SAMPLING LIMIT, DECLARED (`V17_SOURCE_NOTES.md` §0 `D5`)

The §7 screen detector runs on the 5-second grid, so **a screen displayed for less than 5 seconds
can be missed entirely.** It nearly happened here: *"trade two"* of the first pop quiz
(`GBPJPY,M15`) was on screen for **≈7 seconds** — `[00:20:23]` to `[00:20:30]` — and is caught by
**exactly one** frame, `i = 245`. Its diff score against `i = 244` was `17.6`, **below the `§7`
threshold of the initial pass**, and it was recovered only by a targeted second scan of the
`236–250` window driven by the transcript.

**Nothing in this index is known to be missing. That is not the same as knowing nothing is
missing**, and the difference is why this section exists. Open item **207**.

---

## §1 — HOW THE 36 WERE CHOSEN

*(The 37th, `V17_00-21-09_hidpi-recapture-…`, comes from the separate hi-DPI run in `§6` and is
not part of this selection.)*

1. Pairwise diff of all 694 sweep frames (grayscale, control bar excluded, downsampled `256 × 186`),
   keeping `mean > 6.0`, runs collapsed within 10 s → **31 screen states**.
2. A second pass at `mean > 1.6` → **32** (one addition, `i = 316`).
3. A targeted third pass driven by the transcript over four windows the first two under-sampled
   (`236–250`, `500–570`, `440–500`, `600–694`) → **5 further frames**, including `§0.4`'s `i = 245`
   and the Day-2 cycle slide.
4. **Contact sheets were built and looked at before anything was named.**

⚠⚠ **AND THAT LAST STEP IS NOT A FORMALITY.** `V16_MASTERY_REPORT.md` `S1` records that **eleven of
V16's thirty-four frame names were fabricated from the transcript** and described nothing in their
own images. **Every name below was written while looking at a rendering of that specific frame**,
and the four highest-value ones were additionally re-rendered at 2–3× and read character by character
(`§3`). **The failure mode is known and it was actively defended against; this session does not claim
to be immune to it.**

---

## §2 — THE FRAMES

| # | `i` | Burned | Filename | What is visible |
|---|---|---|---|---|
| 1 | 4 | `00:00:20` | `…_boot-camp-schedule-slide-may-13-to-july-1.png` | Printed schedule, seven dated rows, `May 13th` → `July 1st` |
| 2 | 32 | `00:02:40` | `…_market-maker-boot-camp-welcome-back-title-slide.png` | Diagonal title card, `WELCOME BACK!` / `TRADE STRONG` |
| 3 | 35 | `00:02:55` | `…_managing-your-expectations-slide.png` | `Managing Your Expectations` — six bullets, last one highlighted |
| 4 | 47 | `00:03:55` | `…_announcements-title-slide.png` | Diagonal section card, `ANNOUNCEMENTS` |
| 5 | 56 | `00:04:40` | `…_web-class-june-2-to-june-6-slide.png` | `Web Class / June 2nd – June 6th / 6pm-10pm with Sat as the Indicator chart setup day` |
| 6 | 73 | `00:06:05` | `…_where-are-you-by-now-you-should-checklist-slide.png` | Seven-item student progress checklist |
| 7 | 135 | `00:11:15` | `…_take-a-ways-flash-card-4hr-big-board-slide.png` | `Take – a- ways:` — four bullets |
| 8 | 152 | `00:12:40` | `…_take-a-ways-tdi-and-adr-slide.png` | Four further take-away bullets, TDI and ADR |
| 9 | 164 | `00:13:40` | `…_andrew-closed-transactions-account-statement.png` | ⭐⭐ A broker statement — `Account: 7131248  Name: Andrew  Currency: USD`, a `Closed Transactions:` table with `Ticket / Open Time / Type / Size / Item / Price / S/L / T/P / Close Time` columns and an `Open Trades` table below. **Rows are legible**, dated `2012.03.25`–`2012.03.26`, and **carry real `S/L` values** — see `V17_SOURCE_NOTES.md` §13a |
| 10 | 171 | `00:14:15` | `…_student-flash-card-the-pattern-short-and-long-trade.png` | ⭐⭐ Annotated chart + `The Pattern The Pattern The Pattern!!!` with 5-point `Short Trade` and 6-point `Long Trade` lists |
| 11 | 176 | `00:14:40` | `…_level-3-week-after-a-correction-chart.png` | Candle chart, printed `Level 3 week after a correction / Confuse traders`, `HOW` / `LOW` labels, red down-arrows |
| 12 | 204 | `00:17:00` | `…_chart-annotated-its-a-trap-baby-and-straight-away.png` | Chart with hand text `It's a Trap Baby!!`, `HOW`, `Straight away!!`, `Pins to 50 outta London!`; on-chart pivot labels `R1` and `M3` legible at the right edge |
| 13 | 235 | `00:19:35` | `…_pop-quiz-what-are-these-trades-called-slide.png` | `Pop Quiz:` — three questions |
| 14 | 241 | `00:20:05` | `…_pop-quiz-trade-one-gbpusd-m15-chart.png` | ⭐ Chart header reads `GBPUSD,M15 1.61657 1.61677 1.61624 1.61659`; on-chart pivot labels `R1`, `M3`, `M2`, `Pivot` |
| 15 | 245 | `00:20:25` | `…_pop-quiz-trade-two-gbpjpy-m15-chart.png` | ⭐ Header reads `GBPJPY,M15 128.848 128.876 128.760 128.813`; red and pale-blue boxes, `R = 35.6`, `Pivot`, `M2` |
| 16 | 246 | `00:20:30` | `…_pop-quiz-answers-gj-ketchup-and-mustard-slide.png` | ⭐⭐ `Answers: Safety Trades / Better selection: G/J … a close above the ketchup and mustard …` |
| 17 | 254 | `00:21:10` | `…_gbpjpy-m15-chart-red-and-blue-boxes-r-equals-35-6.png` | The `GBPJPY,M15` chart again, mouse pointer on the white MA |
| 18 | 264 | `00:22:00` | `…_gbpusd-m15-chart-with-pivot-labels.png` | The `GBPUSD,M15` chart again |
| 19 | 279 | `00:23:15` | `…_registry-mechanic-window-over-the-slide.png` | ⚠ A `PC Tools │ Registry Mechanic` application window, `1-Click Optimization`, over the slideshow |
| 20 | 284 | `00:23:40` | `…_pop-quiz-answers-slide-shown-again.png` | The answers slide, second showing |
| 21 | 294 | `00:24:30` | `…_gbpjpy-m15-chart-numbered-one-to-seven.png` | ⭐ `GBPJPY,M15` chart with hand-drawn digits `1`–`7` placed on it |
| 22 | 297 | `00:24:45` | `…_seven-point-answer-key-safety-trade-slide.png` | ⭐⭐ `Answer Key` + printed `Safety Trade` list, points 1–7 |
| 23 | 340 | `00:28:20` | `…_answer-key-slide-with-hand-drawn-annotations.png` | The same slide under heavy black hand annotation |
| 24 | 362 | `00:30:10` | `…_trend-title-slide.png` | Diagonal section card, `TREND` |
| 25 | 420 | `00:35:00` | `…_level-3-week-chart-heavily-circled.png` | Frame 11's chart, now circled and marked in black |
| 26 | 447 | `00:37:15` | `…_pop-quiz-answers-slide-shown-a-third-time.png` | The answers slide, third showing |
| 27 | 460 | `00:38:20` | `…_how-do-we-identify-the-trend-slide.png` | ⭐ `How Do We Identify The Trend?` — `MM Trend (Real Trend)` / `Technical Trend (Rest of the world)` + three bullets |
| 28 | 473 | `00:39:25` | `…_trend-is-set-by-the-market-maker-slide.png` | Three bullets on trend ownership and trading both ways |
| 29 | 506 | `00:42:10` | `…_three-day-cycle-day-1-slide-news-is-use-typo.png` | ⭐ `Trend Is Generally Setup As A 3 Day Cycle.` / `Day 1: …` — bottom line reads `News Is Use To Perpetuate False Trend` |
| 30 | 541 | `00:45:05` | `…_powerpoint-editor-open-news-is-used-caret.png` | ⭐⭐ The PowerPoint **editor**, same slide, bottom line now `News Is Used To Perpetuate False Trend` **with the text caret immediately after `Used`** |
| 31 | 543 | `00:45:15` | `…_three-day-cycle-day-2-fifty-two-hundred-crossover-slide.png` | ⭐⭐ `Day 2: Moving Avgs On Higher Time Frames Will Signal. / 50/200 Cross Over Etc. / … Zero Line MACD Crossover CCI Zero line Cross / Retail Traders Will Wait For Confirmations To Enter` |
| 32 | 565 | `00:47:05` | `…_three-day-cycle-day-3-acceleration-slide.png` | `Day 3: … Market Makers Show Acceleration & Separation From MAs A Certain Trap / News Is Used To Further The Cause / MM Apply The Brakes …` |
| 33 | 595 | `00:49:35` | `…_reversal-books-profit-broker-other-side-slide.png` | `The Reversal Is Used For Market Makers To Book A Profit.` + the *"some dude in China"* bullets |
| 34 | 612 | `00:51:00` | `…_trend-reset-mayo-blue-berry-slide.png` | ⭐⭐ `A Trend Reset … Not Reverse Directions. / This will usually appear on a chart landmark (Mayo ,Blue Berry) / … 3 More Days Can Be Expected. / … 4 Or 5 Levels Might Be Identified…….That Is Why We Use A Stop Loss!!!!!` |
| 35 | 648 | `00:54:00` | `…_peak-identified-trend-bias-three-days-slide.png` | `Once The Peak Is Identified The Trend Bias Will Be In Line With The Peak For 3 Days / It Is Safe To Trade V Bottoms And V Tops … / This will keep you out of false W's or M's` |
| 36 | 686 | `00:57:10` | `…_end-of-file-replay-overlay.png` | The final slide dimmed under the player's `replay` overlay — end of file |

All 36 filenames carry the prefix `V17_HH-MM-SS_`.

---

## §3 — THE FOUR FRAMES READ CHARACTER BY CHARACTER

These four carry claims that other V17 artifacts depend on, so each was re-rendered enlarged and
transcribed rather than summarised. **Full verbatim text is in `V17_SOURCE_NOTES.md`** at the
sections named.

| Frame | Rendered at | Where the verbatim text lives |
|---|---|---|
| `00:14:15` student flash card | `3×`, text block cropped to `(640,30)–(940,560)` | `V17_SOURCE_NOTES.md` §6 |
| `00:24:45` seven-point answer key | `3×`, cropped to `(690,40)–(1024,760)` | `V17_SOURCE_NOTES.md` §8 |
| `00:51:00` trend reset | `2×`, full slide | `V17_SOURCE_NOTES.md` §12 |
| `00:45:05` PowerPoint editor | `3×`, bottom line cropped to `(280,540)–(940,640)` | `V17_SOURCE_NOTES.md` §14 |

---

## §4 — ⚠ WHERE THE FRAMES ACT ON THE TRANSCRIPT — **AND ONE ROW HERE WAS WRONG**

**Three places — and after the independent ASR pass returned, only ONE of the three is a
correction.** Row 1 is **retracted** and re-filed as a **speaker** contradiction; row 2 is a
disambiguation; row 3 stands. **This section's original framing overstated what the frames did and
is corrected in place rather than quietly softened** (`REMEDIATION_PROTOCOL.md` §2,
`V17_TRANSCRIPT.md` §5a).

| # | Committed ASR | What the frame shows | Consequence |
|---|---|---|---|
| 1 | `[00:21:10]` *"this is **G U** safety trade"* | `00:21:10` header reads **`GBPJPY,M15`**, and the `00:20:30` slide credits **`G/J`** | ⚠⚠ **THIS ROW IS CORRECTED.** It read *"~~The better trade is GBP/JPY. Naming it `G/U` would have inverted the lesson's answer~~"* on the premise that the ASR was wrong. **The independent ASR pass renders `GU` too** — the transcript is faithful and **the speaker misnamed his own chart**, calling it *"pound yen"* forty seconds later at `[00:21:50]`. **Filed as `C-027`.** The frames corrected my reading of the **speaker**, not of the ASR. ⭐ The answer — **GBP/JPY** — is unchanged, on three supports |
| 2 | `[00:45:16]`, `[00:45:52]` *"a **5200** crossover"* | `00:45:15` prints **`50/200 Cross Over Etc.`** | ⚠ **DISAMBIGUATES rather than corrects** — both engines hear *"5,200"*, because that is how `50/200` is read aloud. The pair is the **50 and 200 EMAs**; `5200` is not a period |
| 3 | `[00:44:56]` *"I got a correct… the news is used"* — unclear what is being corrected | `00:42:10` prints `News Is **Use** To`; `00:45:05` shows the **editor** with the caret after `News Is **Used**` | He is correcting **his own slide, live**, and the deck is therefore mutable mid-session (`A-124`) |

---

## §5 — PROVENANCE OF THE CAPTURE

| Check | Result |
|---|---|
| Source SHA-256 vs `SOURCE_MANIFEST.md` | `2281fa8b…c5d407f767` ✅ verified **before** the patch |
| Source SHA-256 re-verified **after** the frame-rate patch | ✅ **unchanged** — the original was never written to (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Stage size, read from the header | `1024 × 786` → play coordinate `(512, 300)` (`GOTCHA 5`) |
| Declared frame rate, read from **this file's** header | `3.0` fps → patched to `30.0` (`10×`). `frameCount 10290` |
| Play-click guard (`GOTCHA 5`) | ✅ `play click CONFIRMED, stage changed` — **not** assumed |
| Port (`GOTCHA 4`) | `8961`, chosen after `8931`/`8947`/`8953` were found **BUSY** by other sessions. `lsof` checked before and after |
| Served bytes (`GOTCHA 4`) | ✅ `curl … │ shasum` **matched** the on-disk patched copy. Unique filename `v17_x10.swf` — no cache reuse |
| Content-vs-transcript check (`GOTCHA 4`) | ✅ at `i = 4`: seven spoken dates, seven printed dates, same order (`V17_TRANSCRIPT.md` §3) |
| §8a offset | ✅ **MEASURED**, 14 points, **zero** |
| §8a rate check | ✅ **RUN SEPARATELY**, 6 intervals + PNG mtimes |
| Frames named from | **the images**, at `1024 × 786` and, for four of them, enlarged (`§3`) |

---

## §6 — ⭐⭐ A HIGH-DPI RE-CAPTURE WAS RUN, AND IT RETURNS A NEGATIVE RESULT THAT MATTERS FOR OPEN ITEM 198

**`REVIEW_INDEX.md` item 198** (V16 student) proposed that *"`A-101`'s cheapest close is a
higher-resolution re-capture of two named frames whose price axis is illegible at `1024 × 786`"*,
and `COURSE_PROGRESS.md`'s V17 GATE carry-forward `(a)` repeated it: *"A re-capture at higher
`deviceScaleFactor` would settle it in one frame."*

**V17 gave a cheap opportunity to test that proposal on its own material.** Three V17 frames show
the pivot indicator's `R1` / `M3` / `M2` / `Pivot` labels **on live MT4 charts** rather than on V16's
schematic — the first time in the corpus. So the same experiment was run here.

### §6.1 — WHAT WAS RUN

A second sweep, **same patched `v17_x10.swf`, same port, same play coordinate, same
`t0`-before-click**, with `deviceScaleFactor: 2` → a **`2048 × 1572`** stage, capturing six indices
around the pop-quiz charts.

### §6.2 — ⚠⚠ AND §8a HAD TO BE RE-RUN, AND IT CAME BACK **DIFFERENT**

| Run | Offset, measured from the burned timecode | Points |
|---|---|---|
| main sweep (`1024 × 786`) | **0** | 14 |
| **hi-DPI sweep (`2048 × 1572`)** | ⚠ **−1** | **6, uniform** |

Burned readings: `16:59`, `20:04`, `20:24`, `21:09`, `21:59`, `24:29` against nominal `17:00`,
`20:05`, `20:25`, `21:10`, `22:00`, `24:30` — **exactly `−1 s` at every point, over 7.5 minutes of
presentation time**, so the rate is right and the origin moved. The pre-click guard screenshot took
**1,651 ms** on this run against **1,578 ms** on the main sweep.

⭐ **This is `SWF_CAPTURE_RECIPE.md` §8a's own warning demonstrated: *"IT IS LATENCY, SO IT VARIES
PER RUN. DO NOT HARDCODE IT."* Two runs of the same script, on the same machine, forty minutes
apart, gave `0` and `−1`.** **The hi-DPI frame is named from its burned timecode, `00-21-09`, not
from `i × 5`.**

### §6.3 — ⛔ THE RESULT: IT DOES NOT WORK, AND THE REASON GENERALISES

`V17_00-21-09_hidpi-recapture-gbpjpy-m15-chart.png` is a genuine `2048 × 1572` capture. **It
recovers no price axis and no additional level label.**

**The reason is structural, not a capture setting: the chart is a BITMAP EMBEDDED IN A POWERPOINT
SLIDE.** The limiting resolution is the picture the author pasted into the deck, which was cropped
before pasting — **the price scale is not in the source image at all.** Doubling
`deviceScaleFactor` doubles the sampling of the *player*, and the player is faithfully rendering an
already-low-resolution bitmap. **A 2× capture of a 1× source is a 2× upscale and nothing more.**

### §6.4 — WHAT THIS DOES AND DOES NOT SAY ABOUT ITEM 198

**Does:** for any frame whose chart is a **slide-embedded picture**, item 198's proposed remedy
**cannot work**, and this is now measured rather than argued. **The check is cheap and should be run
first: does the frame show the MT4 window chrome (title bar, price axis, `F10` board), or does it
show a cropped picture sitting inside a slide?** V17's quiz charts show an MT4 **symbol header**
(`GBPJPY,M15 128.848 …`) but **no axis and no window frame** — they are pictures.

⚠ **Does NOT:** settle item 198 for **V16's** two named frames (`V16_00-16-50_…`,
`V16_00-17-30_…`), which are V16's material on V16's branch and were **not** re-captured here
(`D-038`). If either of those is a full-screen MT4 capture rather than a slide picture, a hi-DPI
pass could still pay there. **This section narrows item 198 from "do it" to "check what kind of
image it is first, because on one lesson's frames it provably does not help."**

### §6.5 — AND `A-101` IS UNCHANGED

No tenth level appears on any V17 chart. The visible labels across
`V17_00-17-00_…`, `V17_00-20-05_…`, `V17_00-20-25_…`, `V17_00-21-10_…` and `V17_00-21-09_hidpi…`
are **`R1`, `M3`, `M2`, `Pivot`** — a subset of V16's printed nine-level grid, with **no `M5`**
(V17 GATE carry-forward `(c)`). ⚠ **That is not evidence against `M5`**: only part of the grid is in
view on any of these charts, and absence from a cropped picture is not absence from the indicator.
