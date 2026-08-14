# V12 — SCREENSHOT INDEX

> **Lesson:** `Bootcamp1 Wk4 040812 Part2 (55mins).swf` — *Traders Dynamic Index*
> **Capture:** `SWF_CAPTURE_RECIPE.md` §10, 10× sweep (declared `3.0` fps read from **this file's**
> header and patched to `30.0` on a **copy**), stage `1024 × 786`, play coordinate `(512, 300)`,
> pre/post-click guard **fired** (`sweep.log`: *"play click confirmed: stage changed"*).
> **672 frames · 27 distinct screen states · 28 curated.**

---

## 0. HOW TO READ THE TIMESTAMPS — AND THE SYNC VERIFICATION

Every frame retains the **full 1024 × 786 stage including the Camtasia control bar**, so the
player's **burned-in timecode is legible in the bottom-right of every image** and each screenshot
proves its own timestamp (`SWF_CAPTURE_RECIPE.md` §8).

**The filename timestamp is the burned timecode, not the sweep index.** Sweep frame *i* is
captured at presentation second `i × 5`, and the burned timecode runs a **constant +16 s** ahead of
that (the interval between the sweep's `t0` and the play click taking effect).

**Verified, not assumed** — six frames spread across the file, timecode read from the pixels:

| Sweep frame | `i × 5 + 16` | Burned timecode | |
|---|---|---|---|
| 0 | 00:16 | `00:16 / 55:1` | ✅ |
| 102 | 08:46 | `08:46 / 55:1` | ✅ |
| 208 | 17:36 | `17:36 / 55:1` | ✅ |
| 445 | 37:21 | `37:21 / 55:1` | ✅ |
| 604 | 50:36 | `50:36 / 55:1` | ✅ |
| 661 | 55:21 → clamps | `55:18 / 55:1` | ✅ (end of file) |

**6/6 exact, zero drift.** And the mapping is confirmed a second way, on **content**: frame 311
prints `Shark Fin Hold The Mayo` at burned `26:11`, and the transcript's `[00:26:11]` reads
*"Shark fin hold the mail"* — **the same second, in both media**.

---

## 1. ⚠️ LEGENDS — RECORDED IN FULL, WHETHER OR NOT THEY SEEMED RELEVANT

**V11 R1 item 109 required this.** V11's `INDEX.md` recorded a frame's *pane count* and not its
*legend stack*, and the legend turned out to carry `RSI(21)`. **Every legend legible in any V12
frame is transcribed below, including the ones that carry no parameters** — the negative is the
point.

| Where | Verbatim | Carries a period? |
|---|---|---|
| **TDI sub-window**, every charted frame | `Traders Dynamic Index Visual 51.9428 44.5136 37.0844 52.6318 47.2979 46.5466` (values vary per frame) | ❌ **NO.** The indicator's **name and its six output buffers**. MT4 prints an indicator's inputs in parentheses after the name when they are set; **here there are none** |
| **Price pane**, `00-34-26` | `EURJPY,M15  108.054 108.140 108.047 108.093` / `High= 108.538  Previous Days Range= 180` / `Low= 106.798  Current Days Range= 85.4` / `Close= 107.629` | ❌ **NO.** Symbol, timeframe, OHLC and a custom daily-range readout. **No moving-average periods** |
| **Price pane**, `00-37-21` | `EURUSD.M15  1.22257 1.22363 1.22256 1.22317` / `High= 1.2303  Previous Days Range= 110.8` / `Low= 1.2193  Current Days Range= 39.9` / `Close= 1.221` | ❌ **NO** |
| **Price pane**, `00-22-11` and `00-40-36` | `…33629 1.33397 1.33816` / `…de No, Today's Range= 952, T's High= 1.3414…` / `…rget Low= 1.32972 / To ADR High= 544, To ADR…` | ❌ **NO.** A custom text overlay of range/ADR figures, **partly clipped at the left edge by the stage crop** — recorded as partial rather than reconstructed |
| **Hover tooltip**, `00-26-11` | `UPPERLINE  67.8351` | ❌ **NO.** An MT4 **buffer-name hover**, the closest thing in the lesson to an indicator dialog. It names an output, not an input |

> ### ⭐ THE MEASURED NEGATIVE — NO SETTINGS DIALOG EXISTS IN THIS LESSON
>
> `A-080`'s *Required Research* and `COURSE_PROGRESS.md` V12 GATE (b) asked for **an MT4
> indicator-properties dialog, a Navigator entry, or a sub-window legend with a period.**
>
> **All 672 frames were scanned** frame-to-frame at mean-difference threshold **2.0** — a third of
> the 6.0 used for screen-state detection, deliberately low so a modal window open for even one
> 5-second sample could not be missed. **30 changes: the 27 screen states plus three
> announcement-slide text edits. No modal window, no properties dialog, no Navigator panel, at any
> point in the file.**
>
> **`A-080` closes anyway — on the audio** (`V12_SOURCE_NOTES.md` §3). The instructor states the
> period four times and explains why he changed it. **The frames were the predicted route and they
> are not the route.**

---

## 2. THE FRAMES

### The four-step build (`V12_SOURCE_NOTES.md` §4, §10.1)

| # | File | Burned | What is visible |
|---|---|---|---|
| 1 | `V12_00-00-16_title-card-traders-dynamic-index.png` | `00:16` | **The lesson's title card**, black on white: **`Traders Dynamic Index`**, subtitled *"Thank You Dean & CompassFX"*. **Held for 8½ minutes — the longest static screen in the file.** No chart, no candles, no axis. *(This is the frame whose existence falsified the transcript-only claim that the lesson prints no title — `V12_SOURCE_NOTES.md` §10.0.)* |
| 2 | `V12_00-08-46_tdi-a-better-rsi-bullet-slide.png` | `08:46` | White-on-black bullets under a boxed `TDI` header: *"A Better RSI ??? · Gives Better Signals And Trade Confirmations · A Powerful Tool To Scale-in With When Used In Proper Context Of The Market · Will Help Build Confidence In Your Trade Calls · Will Identify Divergence Easily"* |
| 3 | `V12_00-09-41_dean-malone-hybrid-indicator-definition.png` | `09:41` | `Traders Dynamic Index` over *"A hybrid indicator developed to indicate market conditions related to **trend direction** (green), **momentum** (blue), and **market volatility** (red). An "all-in-one" indicator!"* — **Dean Malone's own definition, two-thirds of which the speaker repudiates aloud at `[00:09:51]`–`[00:10:03]`** |
| 4 | `V12_00-10-36_step-1-rsi-price-line-eurusd-daily.png` | `10:36` | `Step 1: RSI Price Line`. A `Traders Dynamic Index` sub-panel over **EURUSD, Daily**, 13 Jan 2005 – 17 May 2005, scale marked `32 / 50 / 68`. **One GREEN line only** |
| 5 | `V12_00-11-36_step-2-trade-signal-line-added.png` | `11:36` | `Step 2: Trade Signal Line`. Same panel, a **RED** line added |
| 6 | `V12_00-12-56_step-3-market-base-line-added.png` | `12:56` | `Step 3: Market Base Line`. Same panel, a **YELLOW** line added |
| 7 | `V12_00-14-31_market-base-line-forecasts-reversals.png` | `14:31` | *"**Market Base Line forecasts Market Reversals**"*. EURUSD Daily **price** panel above (blue/red price plot) and the TDI's **yellow baseline alone** below, with **four red circles** drawn at its turns |
| 8 | `V12_00-15-31_step-4-volatility-bands-added.png` | `15:31` | `Step 4: Volatility Bands`. Same panel, **two BLUE bands** added, enclosing the green and red lines |
| 9 | `V12_00-16-26_volatility-bands-bullet-slide.png` | `16:26` | `TDI` bullets: *"Volatility Bands Act As Support / Resistance Based On The Close (Much Stronger) · When The Bands Contain The RSI Line After A Break, It Is Divergent (Stop Hunt) · When Viewed In The Proper Context, They Can Identify Stop Hunts, Scale Ins And Exits"* |

**The four colours the deck prints — green / red / yellow / blue — are the four the speaker names
in audio.** 4/4 agreement (`V12_SOURCE_NOTES.md` §10.1).

### Worked charts and the signal slides (§6)

| # | File | Burned | What is visible |
|---|---|---|---|
| 10 | `V12_00-17-36_annotated-chart-out-and-in-arrows.png` | `17:36` | MT4 15-minute chart on grey. Light-blue Asian box; white, cyan, yellow and red lines in the price pane; `wt = 58.3` label. **`OUT` and `IN` captions with white block arrows** beneath the TDI sub-window |
| 11 | `V12_00-19-06_tdi-signals-shark-fin-bullet-slide.png` | `19:06` | `TDI SIGNALS`: *"Bands Are Tight · **RSI Line Breaks Out And Comes Right Back** · A Shark's Dorsal Fin Appears To Be Emerging From The Water · **Fin Goes Back Under The Waterline and Crosses The Signal (Red, Blood In The Water)**"*. ⭐ **The corpus's first printed definition of both terms** (`A-031`, `A-032`) |
| 12 | `V12_00-20-41_chart-31-2-pip-box-shark-fin-short.png` | `20:41` | 15-minute chart, light-blue box labelled `31.2`; pivot lines captioned `M3`, `Pivot`, `M2`, `S1`; red and green arrow markers; two white-boxed glyphs top and bottom. TDI sub-window below |
| 13 | `V12_00-22-11_chart-37-6-pip-box-railroad-tracks.png` | `22:11` | 15-minute chart, box labelled `37.6`; hand-drawn count **`1` `2` `3`** down to the low; white up-arrow marker. Custom overlay text at top (range / ADR figures, left-clipped) |
| 14 | `V12_00-23-26_tdi-signals-shark-fin-long-bullet-slide.png` | `23:26` | `TDI SIGNALS`: *"Shark Fin Long · **Same Criteria As Short (Inverted)** · The Setups Must Coincide With Other Indicators · Must Be In Right Part Of The Cycle"* |
| 15 | `V12_00-24-46_chart-21-0-pip-box-head-and-shoulders.png` | `24:46` | 15-minute chart, box labelled `wt = 21.0`; cluster of red and green arrow markers across the box; strong run up on the right. Custom overlay `Range= 130.5 / …ge= 168.7` |
| 16 | ⭐ `V12_00-26-11_shark-fin-hold-the-mayo-captioned-chart.png` | `26:11` | **Chart captioned in large white text: `Shark Fin  Hold The Mayo`.** Light-blue box `= 27.5`; a **red highlight box** at `wt = 73.1`; green up-arrows at the lows. **A WHITE line runs beneath price and the marked low sits on it.** Cyan, red and yellow lines also present. TDI sub-window below with an **`UPPERLINE 67.8351` hover tooltip**. ⭐ **The word `Mayo` is PRINTED here, at the same second the audio says *"hold the mail"* — this is what closes `A-064`** |
| 17 | `V12_00-28-51_scaling-with-tdi-title-card.png` | `28:51` | Section title card: **`SCALING WITH TDI`** |
| 18 | `V12_00-29-11_tdi-entry-and-scale-in-bullet-slide.png` | `29:11` | `TDI`: *"You Are In The Right Market Segment · Price Is In The Channel · RSI Line Breaks Outside The Bands As A Stop Hunt · Reversal Is Imminent Look For Signals / Setup · **Enter The Trade Stop Loss 23 Pips above the HOD** · **Add To The Trade At MB Break And VB Break** · **Exit All Units @ VB Return Crossover**"*. ⭐ **The lesson's whole trade management, printed** |
| 19 | ⭐⭐ `V12_00-31-31_tdi-vb-break-price-held-by-200-chart.png` | `31:31` | **Captioned: `TDI VB BREAK, PRICE HELD BY 200  FOLLOWED BY MB BREAK, LOWER VB BREAK EXIT`.** Dark-blue box `wt = 28.5` top left; **`400+ Pips`** printed mid-chart; red highlight box at `wt = 60.0`; hand-drawn `1` `2` `3` and `Exit` marks in the TDI sub-window. **A WHITE line descends across the top of the chart and price turns at it.** ⭐ **This frame's caption and the audio at `[00:31:22]`–`[00:31:27]` (*"held by the mayonnaise perfectly. Held by the 200"*) are the same moment — the evidence that moves `A-020`'s mayo row to `RESOLVED BY COURSE`** |
| 20 | `V12_00-33-41_scaling-with-tdi-bullet-slide.png` | `33:41` | `SCALING WITH TDI`: *"TDI Offers A Few Key Points To Scale In With · After Entry Is Made, Add To Your Trade On A MB Cross · Add Again On A VB Break · Exit All Units On VB Return"* |
| 21 | `V12_00-34-26_eurjpy-m15-chart-110-pips.png` | `34:26` | **EURJPY M15** (legend §1). Light-blue box; **`110 pips`** and **`60 pips`** printed measurements; red down-arrow; red highlight box `wt = 70.4`; `Exit` marked; a coloured signal-tile grid top right with `108.083` and `Pips to Open / At Hi Low 215 / Daily Hi 105` readouts |
| 22 | `V12_00-37-21_eurusd-m15-chart-white-line-support.png` | `37:21` | **EURUSD M15** (legend §1). Dark-blue box left; red highlight box `wt = 83.6`; magenta and green candles; **a WHITE line runs flat across the lower third and price bounces from it**; `Exit` and count marks `1 2 3` in the TDI sub-window |
| 23 | `V12_00-40-11_chart-blue-box-with-tdi-subgraph.png` | `40:11` | 15-minute chart with a **dark-blue box** lower left, magenta down-arrow, sharp run up; hand-drawn white trend strokes in both panes. TDI sub-window legend `52.6318 47.2979 46.5466` |
| 24 | `V12_00-40-36_mm-hit-the-stops-high-chart-plus-284.png` | `40:36` | **Captioned `MM Hit The Stops High`.** Light-blue box `wt = 30.7`; count `1 2 3` down the decline; a printed running total **`114 / 95 / 75` over `+284`**; red highlight box `wt = 34.5`; **`EXIT ALL TRADES`** captioned bottom right |
| 25 | `V12_00-41-41_tdi-checkpoints-bullet-slide.png` | `41:41` | `TDI`: *"If you are NOT scaling in / Use the same signals to stay the trade · We can call them **"Check points"** / They are confirmations to hold on or look for the exit"* |

### The assignment and the announcements (§8)

| # | File | Burned | What is visible |
|---|---|---|---|
| 26 | ⭐ `V12_00-42-06_this-weeks-r-and-d-assignment-slide.png` | `42:06` | **`THIS WEEKS R & D`** — *"Find And Identify The Trade Signals Using TDI · Use any pair you like. Black out price action and check your knowledge."* with a cartoon of a man examining a chart through a magnifying glass. ⭐ **This is the week-4 assignment V11 `[00:00:46]` promised and did not give** (`COURSE_PROGRESS.md` V12 GATE (c)). **The slide is the SHORT version — the spoken assignment at `[00:43:18]`–`[00:49:08]` adds the demo account, the five blind trades, the wristwatch and the two-pair restriction** |
| 27 | `V12_00-50-36_announcements-orlando-meetup.png` | `50:36` | `MARKET MAKERS BOOT CAMP` — *"Announcements / Kar is working on the Orlando Meetup / If he is able to get it lined up, I will attend. / We will possibly set it up as additional training and stream it live / recorded / Don't get excited yet..this is just wishful thinking on my part!! / **We are shooting for April 21st** / I will keep you posted if we can get it done!"*. ⭐ **A forward-dated reference: 2012-04-21 is a Saturday 13 days after the session date, independently corroborating `2012-04-08`** |
| 28 | `V12_00-55-18_announcements-new-jersey-venue.png` | `55:18` | `MARKET MAKERS BOOT CAMP` — *"Finally / I am working closely with the Venue in NJ to / Lock up some dates for June. / I will deliver a Web class / Review prior to my trip to New Jersey / I am looking at late May / Everyone is always welcomed!! / I will post the details as I lock down the availability"*, partly overlaid by the player's end-of-file **`replay`** button. **Final frame** |

---

## 3. WHAT IS **NOT** IN ANY FRAME — the negatives, stated so a later session does not re-search

| Looked for | Result |
|---|---|
| MT4 indicator-properties dialog | ❌ **None.** Measured across all 672 frames — §1 |
| Navigator / Indicators list | ❌ **None** |
| A legend carrying **any** indicator period | ❌ **None.** Five legends transcribed in §1; **not one has a parenthesised parameter.** This is now measured on **two consecutive lessons of the instructor's own charts** (V11 R1 established the same for V11's `46:45` and `47:35`) |
| A moving-average legend naming `5`, `13`, `50`, `200` or `800` | ❌ **None.** The `200` in this lesson is named **in a slide caption and in speech**, never in a legend |
| `ketchup`, `mustard`, `blueberry`, `raspberry` | ❌ **Zero occurrences**, printed or spoken. `D-042` §1's exhaustive negative is unaffected by V12 |
| The TDI's component periods (TSL, baseline, bands) | ❌ **None** — `A-039` stays open on these, `A-085`, `A-086` |
