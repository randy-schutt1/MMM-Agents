# V15 — SCREENSHOT INDEX

**37 frames**, curated from a **623-frame** 10× sweep (`SWF_CAPTURE_RECIPE.md` §10).
Every frame is the full **1024 × 786** stage **including the player control bar**, so each one
**carries its own burned-in timecode and proves its own timestamp** — the property the quarantined
`VISUAL_INDEX.md` files lack (`Q-016`).

**Capture provenance.** Source SHA-256 `5308c350…82b49` verified against `SOURCE_MANIFEST.md`
before **and after** the frame-rate patch, proving the original was not modified. Declared rate
read from **this file's own header** — `3.0 fps`, patched to `30.0` for 10×; header also gives
`frameCount = 9,379` → `3126.33 s`, agreeing with measured audio `3125.45 s` and the manifest's
`3125 s`. Stage `1024 × 786`, play coordinate `(512, 300)`, and **the pre-click/post-click guard
confirmed the click fired** (`sweep.log`: *"play click confirmed: stage changed"*). Port `8915`
verified free, then verified as this session's PID, then the served bytes SHA-256-matched against
the local copy (`GOTCHA 4`).

---

## ⭐ §0 — THE +15-SECOND SWEEP OFFSET: MEASURED, AND ITS CAUSE NAMED (open item 174)

`V14_REVIEW_R1.md` found that **all 29 V14 frames ran exactly +16 s against their own burned-in
timecode**, that V12's and V13's ran at 0–1 s, and required the next session to *measure the
offset; if it recurs, name the cause*. **It recurred, at +15 s, and the cause is in the recipe.**

**Measured, not assumed** — the burned-in timecode was read off eight frames spanning the file:

| Sweep label | Burned-in timecode | Offset |
|---|---|---|
| `0` | `00:16` | +16 |
| `100` | `01:55` | +15 |
| `500` | `08:35` | +15 |
| `1000` | `16:55` | +15 |
| `1500` | `25:15` | +15 |
| `2000` | `33:35` | +15 |
| `2500` | `41:55` | +15 |
| `3000` | `50:15` | +15 |

**Constant +15 s, zero drift across 52 minutes.** The `+16` at label `0` is the OSD's own
1-second lazy granularity (`GOTCHA 2`), not a different offset.

### THE CAUSE

`SWF_CAPTURE_RECIPE.md` §10's `sweep.mjs` clicks play, then waits **1500 ms** to compare the
pre-click and post-click screenshots (the `GOTCHA 5` guard), and **only then** starts the clock
(`const t0 = Date.now()`). At `SPEED = 10`, **that 1500 ms of wall clock is 15 presentation
seconds of playback.** The offset is therefore not a defect and not drift:

> **`offset_seconds = guard_ms / 1000 × SPEED`**

**This predicts V14's +16 s** (same 1500 ms guard, same 10×, plus the same 1-second OSD
granularity) **and it predicts V12's and V13's 0–1 s**: a sweep that sets `t0` before the click,
or waits a fraction of that, cannot accumulate it. **It is deterministic, computable in advance,
and it scales with `SPEED`** — at 40× the same guard would put every frame 60 s out.

### WHAT THIS SESSION DID ABOUT IT

**Every filename in §1 is the TRUE presentation time — `sweep_label + 15.0` — and every one of
them was checked against its own burned-in timecode before it was named.** No frame in this
directory is named from the raw sweep label. A reader can verify any row by reading the
bottom-right corner of the PNG it points at.

⚠ **Recommended for `SWF_CAPTURE_RECIPE.md` §10, which is a POLICY document and therefore is
NOT edited on this branch (`D-038a`):** set `t0` immediately before `p.mouse.click(...)` and
take the guard screenshot afterwards, or subtract `guard_ms/1000 × SPEED`. Raised as
`REVIEW_INDEX.md` item 189.

---

## §1 — THE FRAMES

**Every frame below was opened and looked at before it was named** (`FILE_NAMING_STANDARD.md` §3
— descriptors say what is shown, not what it means). `[PRINTED]` marks text read off the frame.

| `[ts]` | File | What is shown |
|---|---|---|
| 00:00:15 | `title-slide-week-seven` | ⭐ Title slide: `Market Makers Boot Camp` and, below it, **`Week 7`** `[PRINTED]`. **The printed corroboration of the twice-spoken *"week seven"*** at `[00:00:02]` and `[00:00:23]` |
| 00:00:30 | `welcome-back-tradestrong` | `Market Maker Boot Camp` / `Welcome Back` / **`TRADESTRONG`** `[PRINTED]` |
| 00:01:10 | `managing-your-expectations-list` | `Managing Your Expectations` — a seven-item bulleted list beginning *"I expect you to:"* (*follow along free from distraction*, *give me 2 hrs a week*, *make an honest effort at completing all assignments on time*, *execute in demo the concepts as illustrated*, *refrain from negativity in your own mind*, …). Rendered small; the list is legible, the sub-clauses are at the edge of legibility and are **not** transcribed here |
| 00:04:30 | `chat-box-still-ignoring-ya` | `Chat box……` / `Still Love ya!` / `Still ignoring ya!  ( during my teaching time!!)` / `This will not change!!` `[PRINTED]` |
| 00:04:40 | `announcements-live-class-stevens-institute` | ⭐⭐ `Live Class` / `New Jersey @ Steven's Institute` / `June 23-27 @ 6PM 'till 11pm` / `Visit the " NJ or Bust" section on the forum for details` / `Hotel information, please visit: tinyurl.com/mmfxlodging` / **`This Class will NOT be recorded or streamed!!!!!!!`** `[PRINTED]`. **See §3 — corpus-gap evidence** |
| 00:05:55 | `announcements-web-class-june-2-6` | ⭐⭐ `Web Class` / `June 2nd - June 6th` / **`6pm-10pm with Sat as the Indicator chart setup day.`** / `These recordings will be left up all during the Live event` `[PRINTED]`. **See §3 — this names, by scheduled date, the session that would answer `A-084`, and it is not in this corpus** |
| 00:07:15 | `where-are-you-by-now-you-should-list` | ⭐ `Where are you?` / `By now you should…..` → `Have a set of Flash cards` · `Have 4hr Markups` · `Have Taken TDI only Trades` · `Worked the Big Board` · `Moving AVG Only trades` `[PRINTED]`. **The printed roll-call of the drills V13/V14 set** |
| 00:07:50 | `take-a-ways-flash-card-4hr-big-board` | ⭐ `Take – a- ways:` / `Can spot a clean set-up pattern (Flash Card)` / `Understand the big picture (4hr)` / `Have a deeper understanding as to how the dealer extends the Hi/Lo holds a level and comes above/below the same level for stop triggers and trap moves etc. (Big Board)` `[PRINTED]` |
| 00:10:20 | `tdi-take-a-ways-slide` | ⭐ `Understand how to really use the TDI and how to manage your trades with it.` / `Can confirm a trade signal when combined with dealer price action, Timing and larger cycle` / `If you are not seeing this, go back and do the drills…..it is never too late!!!` `[PRINTED]`. **NO periods, NO smoothing, NO band values, NO input names — see §4** |
| 00:13:50 | `moving-average-take-a-ways-slide` | `Can see how to read the moving AVG` / `For trade management` / `For confirmed entry or exit` `[PRINTED]` |
| 00:14:20 | `forum-post-gilbert-ellis-big-board-trades` | ⭐⭐ A **screenshot of the course forum**: `Gilbert Ellis - Glendale, AZ` · `Student` · `Posts: 13`; thread **`Big Board Trades U/CHF & U/CAD`**, **`on: April 30, 2012, 03:12:23 AM`**; four attachments `USDCAD HiLo HW.gif` / `USDCHF HiLo HW.PNG` (×2 each, view counts 88/52/37/26) `[PRINTED]`. **A dated student submission of the V14 high/low-board drill, posted INSIDE the missing-week window — see §3** |
| 00:14:35 | `gilbert-ellis-annotated-chart-times-written` | The same student's chart blown up: candles with a grey information panel, a cyan-highlighted box, and **hand-written clock times against the high and low** — the practice `[00:14:41]` calls *"He wrote in what the times were for the high and low"* |
| 00:15:15 | `gilbert-ellis-second-annotated-chart` | The second of the same student's charts, same treatment |
| 00:16:00 | `forum-post-peter-brown-tdi-topic` | ⭐ Forum screenshot: `Peter Brown - Sydney, NSW` · `Student` · `Posts: 7`; thread **`TDI (Read 61 times)`**, **`on: April 28, 2012, 07:57:45 PM`**; attachments `audchftdi.gif`, `audusd tdi.gif` `[PRINTED]`. **A dated TDI-only-trades submission, also inside the missing-week window** |
| 00:16:15 | `peter-brown-tdi-only-trade-chart` | That student's chart: price pane over an oscillator sub-pane, moving averages in yellow/red/cyan |
| 00:17:15 | `ron-vara-chart-pins-pullback-news-spike` | A third student's chart (`Ron Vara`, `[00:17:05]`): tall red/green candles, a cyan box, the setup `[00:17:13]` narrates as *"pins, pull back … pins, again"* around a news spike |
| 00:17:20 | `stray-window-pc-tools-registry-mechanic` | ⚠ **NOT an MT4 panel.** A `PC Tools \| Registry Mechanic` window has opened over the instructor's desktop — `1-Click Optimization`, `35% Completed`, `Scanning Registry HKEY_CLASSES_ROOT\ExtendedControls.CM12TimeEditorCtrl.1`, `Registry issues found: 0`. Indexed because V14's two stray Windows dialogs are indexed, and because **a stray window is the commonest false positive for the properties dialog `A-084` needs** |
| 00:17:55 | `what-i-am-trying-to-accomplish-slide` | `What I am trying to accomplish with these sessions:` / `I am breaking down the chart template and covering each element of the setups.` / `If you can master each segment individually, when all the elements are placed back on the chart you will be strong and confident with your trading decisions.` / `Hence, you will have mastered the business!!` / `You Are doing a dis-service to yourself by not participating in these drills.` `[PRINTED]` |
| 00:18:35 | `this-weeks-break-down-slide` | `This Weeks Break Down` `[PRINTED]` — the section divider between the housekeeping half and the lesson |
| 00:18:50 | `pound-four-hour-annotated-psychological-sr` | ⭐⭐ **A 2012 instructor's-own MT4 chart, annotated.** Header `GBPUSD,H4  1.61508 1.61610 1.61438 1.61450`; sub-window legend **`TDI_MMM 56.5199 43.8625 47.9931`**; overlays in **yellow, red, cyan** plus a horizontal **yellow** level; hand annotations `HOW`, `Dealer Breaks High..ends with a Pin..Sell`, `Psychological S&R Levels` (two white horizontals), pushes numbered **`1 2 3`** on both the price pane and the TDI pane, `NEWS / NO Trade`, `Trend has Been Up Big!`, `Dealer Must Correct!!` `[PRINTED]`. **See §4** |
| 00:21:55 | `euro-annotated-chart-m-formation` | The Euro chart of `[00:20:39]`–`[00:21:12]`: same template, sub-window legend `TDI_MMM 45.6793 37.0056 42.0139`, black hand-drawn trend strokes |
| 00:23:10 | `euro-four-hour-bigger-m-annotated` | The four-hour Euro view `[00:21:55]` calls *"a bigger, bigger thing going on"*, with a red hand-drawn circle at the level `[00:22:08]` describes as *"the deal or just misses the previous high"* |
| 00:26:25 | `if-you-still-cant-see-this-slide` | `If you still can't see this` / `Go back and work some more charts!!` / `The answers are here!!!` `[PRINTED]`. ⚠ The slide's own title reads **`Marker Makers Boot Camp`** — a typo in the instructor's deck, recorded because it is a distinguishing feature of the source, not of the capture |
| 00:27:05 | `adr-high-and-low-oscillator-slide` | ⭐ `ADR High and LOW` / `Always Plotted As An Oscillator` / `Offers Traders Little To No Value In This Format` `[PRINTED]`. **The lesson's title slide** |
| 00:28:20 | `adr-values-converted-to-hard-targets-slide` | ⭐ `ADR` / `We Took The Values As Plotted On The Sub-graph And Converted Them To Hard Targets On The Chart.` / `Now When These Values Are Hit We Can Make Solid Trade Decisions` `[PRINTED]`. **The method statement for the whole lesson** |
| 00:30:05 | `adr-slide-annotated-c-u-m-w` | The same slide with the instructor drawing over it in yellow: an oscillator trace, and letter shapes he calls out as the `C`/`U` and `M`/`W` forms |
| 00:32:00 | `adr-high-low-four-bullets-slide` | ⭐ `ADR High/Low` / `Acts As Intraday Support/Resistance` / `May Line Up With A Pivot Point` / `Lets You Know Where You Are In The Move And What Type Of Trade May Be Warranted` / `Acts As A Target Once The Trade Is On` `[PRINTED]` |
| 00:32:50 | `gotomeeting-hide-desktop-overlay` | ⚠ The broadcast platform's own banner, **`GoToMeeting: Hide Desktop`**, over a plain blue field covering the top ~60% of the stage for ~5 s `[PRINTED]`. **The first frame in this corpus to name the delivery platform.** Indexed because an unexplained blue field is exactly the artifact a later session would mis-read as a lost slide |
| 00:36:35 | `adr-high-low-annotated-weekly-pattern` | The four-bullet slide with the instructor's hand-drawn weekly pattern over it — a rising staircase with `M`/`W` letters and a `T`, drawn while narrating `[00:35:34]`–`[00:36:26]` (*Sunday psychological S&R → Monday false move → Tuesday high of the week → Wed/Thu/Fri*) |
| 00:40:35 | `adr-marker-grid-chart-dotted-lines` | ⭐ A near-empty chart pane showing **the grid itself**: cyan dotted, red dotted and grey dash-dot horizontal lines with no candles in view — the *"floating grid"* and *"fixed grid"* of `[00:32:16]` isolated |
| 00:41:30 | `confluence-slide-yesterday-high-low-pivot-adr` | ⭐⭐⭐ **THE LESSON'S RULE, PRINTED:** `ADR High/Low` / `Yesterday's High And Low, A Pivot Point And The ADR Marker Will Create Strong Intra-day Reversal Zones` / `Especially If These Points Also Coincide With A Longer Period Moving AVG  50 Or 200` `[PRINTED]` |
| 00:44:15 | `adr-slide-annotated-m-and-w-hand-drawn` | The four-bullet slide with hand-drawn `M` and `W` shapes over it |
| 00:44:50 | `daily-chart-annotated-ellipses-yellow` | ⭐⭐ **The confluence diagram.** Cyan dotted line labelled **`DayLo`**, a grey label **`S1`**, a white dash-dot line labelled **`M1`**, two red dotted lines, and the instructor's yellow hand-drawn **W** inside a hand-drawn ellipse spanning the band `[PRINTED]`. **`S1` and `M1` are MT4 pivot labels — see §4** |
| 00:45:00 | `chart-adr-zone-red-box-annotated` | Price chart with a solid red block at the left edge, dash-dot levels, the yellow and red moving averages, and hand annotation |
| 00:46:00 | `chart-adr-high-0-89822-red-box` | ⭐ Chart with a red band labelled **`ADR High: 0.89622`**, pivot labels **`M4`** and **`R1`**, and yellow/red moving averages where **the yellow line turns first and the red follows** `[PRINTED]` |
| 00:51:00 | `chart-adr-low-1-07128-annotated-spikes` | ⭐ Chart with a red band labelled **`ADR Low: 1.07128`**, pivot labels **`S1`** and **`M1`**, and the instructor's yellow `V` drawn on the spike-and-reverse `[00:51:00]` calls *"He went right down past the ADR. He spiked it to the M1. And then he reversed away quickly"* |
| 00:52:00 | `end-of-lesson-replay-control` | The final frame — the player's replay control, timecode `52:0x` |

---

## §2 — WHAT THE SWEEP DOES **NOT** CONTAIN

Stated as a negative because a negative is only useful if it is stated with its scope.

- **NO MT4 properties dialog, NO Navigator pane, NO indicator inputs tab, in any of the 623
  frames.** Two windows do open over the desktop — `17:20` (`PC Tools \| Registry Mechanic`) and
  `32:50` (`GoToMeeting: Hide Desktop`) — and **neither is an MT4 panel.** With V12's, V13's and
  V14's sweeps this makes **2,670 frames across four lessons containing no such dialog.**
- **NO parameter tuple in any indicator legend.** Both TDI legends in this file read
  `TDI_MMM <v1> <v2> <v3>` — short name and three current values — exactly the `A-087` behaviour.
  Consistent with V13's finding and with `REVIEW_INDEX.md` item 154's correction that this is a
  fact about **this build**, `TDI_MMM`, and not about legends in general.
- **NO printed RSI period, smoothing period, smoothing type, or band width anywhere.** The one
  TDI slide, `10:20`, is prose.

---

## §3 — THE CORPUS-GAP FRAMES

Four frames bear on the missing Week 6 and the missing Orlando recording (`A-092`), and they do
it from the print rather than from the speech:

1. **`00:00:15` `Week 7`** — printed. The lesson says what week it is.
2. **`00:07:15` the drill roll-call** — printed. The drills it asks about are the ones V13 and
   V14 set, so nothing was assigned in between that this corpus does not hold; **the gap is a gap
   in RECORDINGS, not in the syllabus.**
3. **`00:14:20` and `00:16:00` the two dated forum posts** — `April 30, 2012, 03:12:23 AM` and
   `April 28, 2012, 07:57:45 PM`. **Both fall between V14 (2012-04-15) and V15 (2012-05-06)**,
   i.e. inside the window where a Week 6 recording would sit. The course was **running** in that
   window; students were submitting homework into it. That is independent, timestamped,
   Tier-1 evidence that the absence is an absence of *recordings*.
4. **`00:04:40` `This Class will NOT be recorded or streamed!!!!!!!`** — printed, about the June
   live class, and `[00:05:21]` gives the reason in the speaker's own voice: *"The same shit that
   happened in **Orlando** where **I didn't get a recording out of there** is exactly why I'm not
   streaming this class."* **The missing Orlando recording is not a collection failure. It was
   never made, and the instructor says so.**

---

## §4 — WHAT THE CHARTS SHOW ABOUT THE INDICATORS, AND WHAT THEY DO NOT

**`D-043` gets a third independent Tier-1 corroboration, by ordering.** On `18:50` and `46:00`
the price pane carries **yellow, red, cyan** (and, on `18:50`, a flat horizontal yellow level)
moving averages, and at every turn **the yellow line changes direction first and the red follows
it**. A faster EMA turns before a slower one, so **yellow is the shorter period and red the
longer** — which is `D-043`'s `5 = mustard = yellow`, `13 = ketchup = red`, and **not** `D-041`/
`D-042`'s reversed pairing. The audio agrees without naming a number: `[00:12:12]` *"The moving
averages have painted an M with the mustard. It crossed back over the ketchup."*

**The printed confluence slide names `50` and `200`** — `Especially If These Points Also Coincide
With A Longer Period Moving AVG  50 Or 200` — and `[00:41:39]` reads the same pair aloud as
*"Maybe the 50. **Mayonnaise** or the water\[s\] laying near the blueberries"*. Under `D-043`
that is `water = 50` and `mayo = 200`. **The slide does not attach either nickname to either
number**, so this is corroboration of the *periods being the taught pair*, not of the mapping.

**`S1`, `R1`, `M1`, `M3`, `M4` are MT4 PIVOT LABELS, not "M formations".** `44:50` and `51:00`
print `S1` and `M1` on horizontal grid lines; `46:00` prints `M4` and `R1`. This is decisive for
reading the audio, where `[00:45:47]` *"This is an M1 M3 day"* and `[00:44:53]` *"There's your
mayonnaise, your M3"* would otherwise read as M-formations. **`M1`–`M4` are the mid-levels
between the pivot's S/R levels.** Logged as `A-096`.

**And what they do not show.** Two TDI legends, `TDI_MMM 56.5199 43.8625 47.9931` (`18:50`,
GBPUSD H4) and `TDI_MMM 45.6793 37.0056 42.0139` (`21:55`, Euro), are **new readouts of an
already-recorded object** (V03, V05, V08, V09, V13 all print `TDI_MMM` with three values).
They are consistent with the buffer order `MarketBase Line · RSI Price Line · Trade Signal Line`
recorded from `MM4XSF_TDI.ex4` — in both readouts the middle value is the extreme one and the
third sits between it and the first, which is what a fast SMA, a slower SMA and a long base line
do on a directional move. **That is a consistency check, not an identification: infinitely many
(fast, slow) pairs produce the same ordering, and the 2012 bars needed to test a specific pair
are outside this project's corpus, which starts 2013-01-01 (`D-036a`, `D-044`).**
**`A-084`, `A-085` and `A-086` are NOT advanced by these frames and are NOT closed.**
