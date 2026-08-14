# V11 — SCREENSHOT INDEX

## HOW THESE WERE CAPTURED

| Field | Value |
|---|---|
| Method | `SWF_CAPTURE_RECIPE.md` §10 — 10× frame-rate sweep, Playwright + Ruffle 0.5.0, system Chrome |
| Source | `Bootcamp1 Wk4 040812 Part1 (51mins).swf`, SHA-256 `606cc5a8…4d2101`, **a working copy** — the original was re-hashed afterwards and is unmodified |
| Header, read from **this file** | `frameRate` **3.0**, `frameCount` **9,171**, stage **1024 × 786** |
| Patch | 3.0 → **30.0** fps, i.e. **×10** — derived from this file's own declared rate, per §10's corrected rule (open item 87). **Not a literal** |
| Port | **8953**, verified free before binding and verified as this session's PID afterwards; served bytes SHA-256-matched against disk (`GOTCHA 4`, `D-022`). **Port 8931 was tried first and was BUSY — another session held it.** The check did its job |
| Play click | `(512, 300)` for the 1024 × 786 stage (`GOTCHA 5`). The **pre-click / post-click screenshot guard fired and passed** — `sweep.log`: *"play click confirmed: stage changed"* |
| Sweep | 620 frames at 500 ms wall = **5 presentation-seconds** apart; 585 distinct file sizes, first 20 frames all distinct — **not a splash-screen capture** |
| Frame → time | `t = index × 5 + 15` seconds. **The +15 s is measured, not assumed**: frame `0021` carries the burned-in timecode `02:00`, and `21 × 5 + 15 = 120`. It is the 1.5 s wall-clock guard wait between the play click and `t0`, multiplied by 10 |
| Screen-state detection | §7 pairwise grayscale diff over the sweep frames, threshold `mean > 6.0`, runs collapsed within 2 frames → **28 distinct screen states** |
| Selection | 27 frames. Every one was **opened and looked at** before it was named (§8) |

**Every frame retains the full 1024 × 786 stage including the player control bar, so each image
carries its own burned-in timecode and proves its own timestamp.**

## CONTENT SANITY CHECK — RUN EARLY, PER `GOTCHA 4`

Frame `0021` (burned timecode `02:00`) prints a slide reading *"Chat Box / I am ignoring you!! /
On purpose!! / Chat box will be ignored until the end of the segments… / Please post all research
work in the forum for review / Grade your work against my posts or slides…"*.

The transcript at `[00:01:37]`–`[00:01:54]` reads *"All right chat box. I'm ignoring you on
purpose… Listen the chat box is gonna be ignored till the end of the segment… Please post all
research work in the forum for review. Raise [Grade] your work against my post or slides."*

**Slide and audio match, at the same timestamp, on a file whose identity was in question until
this check.** That is the two-minute check `GOTCHA 4` asks for, and it passed.

---

## THE FRAMES

| # | File | Presentation time | What is shown |
|---|---|---|---|
| 1 | `V11_00-00-40_title-card-and-managing-expectations.png` | 00:40 | Banner `MARKET MAKERS BOOT CAMP`; *"Managing Your Expectations"* list — *"Give me 2 Hrs a week!"*, *"Execute in demo the concepts as illustrated"*, *"Refrain from negativity in your own mind"* |
| 2 | `V11_00-01-40_chat-box-and-forum-policy-slide.png` | 01:40 | The chat-box / forum-posting policy slide (the sanity-check frame above) |
| 3 | `V11_00-03-00_student-email-marked-up-eurjpy-gbpjpy.png` | 03:00 | **A student's own marked-up EUR/JPY and GBP/JPY charts**, pasted with his email text. Red boxes, pip annotations, *"Re-enter here"*, *"Thanks Buddy"*. This is the artifact the first 25 minutes argue against |
| 4 | `V11_00-07-45_hand-drawn-box-25-50-lod-w-formation.png` | 07:45 | **Hand-drawn on a blank MS Paint canvas**: a box, a drop out of it, a W, and the hand-written labels **`25` / `50`** and **`LOD`**. The lesson's central geometry, in his own hand |
| 5 | `V11_00-09-00_hand-drawn-box-with-w-inside-circled.png` | 09:00 | The same drawing extended — a **W circled inside the box** (the case he calls not a trade) and an M drawn above |
| 6 | `V11_00-11-15_hand-drawn-aggressive-m-and-w-formations.png` | 11:15 | Two large hand-drawn formations — the *"aggressive and big"* M and W of `[00:11:00]` |
| 7 | `V11_00-11-30_student-chart-second-leg-w-in-shadow-box.png` | 11:30 | Back to the student's charts, for the *"this W right here perfect the second leg forms in the shadow box"* passage `[00:12:07]` |
| 8 | `V11_00-13-20_problems-occurring-as-a-group-slide.png` | 13:20 | **PRINTED LIST — `Problems that are occurring as a group`**: *"You are entering on the vector candles / Leg 1 With No Confirmations / Before LOD /HOD have locked in / Inside the Blue Box / With no reason other than the dealer has made a move / Not taking the timing into consideration / Afraid you will miss something and causing your own demise"* |
| 9 | `V11_00-15-55_new-protocol-for-all-of-us-slide.png` | 15:55 | *"These items are the only reason you are failing to generate winning trades! It must stop immediately… **Here is a new protocol for All of us!**"* |
| 10 | `V11_00-20-20_trade-strong-mantra-slide.png` | 20:20 | **PRINTED — the `Trade Strong` mantra, five commitments.** See § THE PRINT-VS-SPEECH DIVERGENCE below |
| 11 | `V11_00-21-00_bracelets-limit-order-green-slide.png` | 21:00 | *"This will be our new group Mantra! I have ordered Bracelets… they will be the color of `LIMIT ORDER GREEN!!!` … If you Push your Limit…You will hit your Limit!"* |
| 12 | `V11_00-24-25_one-trade-philosophy-slide.png` | 24:25 | **PRINTED — `One Trade Philosophy`**, ten completions of *"One trade should not………."* |
| 13 | `V11_00-26-45_indicators-and-oscillators-slide.png` | 26:45 | **PRINTED — `INDICATORS AND OSCILLATORS`**: *"All Indicators Measure The Same Thing / All Plot Above Or Below A Base Or Zero Line / If You Use Several – Which One Wins? / Why Not Master The Use Of One?"* |
| 14 | `V11_00-27-35_can-you-decide-cluttered-subgraph-chart.png` | 27:35 | **`CAN YOU DECIDE??`** — a chart with **six** stacked sub-graph indicator panes. The negative example of `[00:27:42]` |
| 15 | `V11_00-28-30_rsi-relative-strength-index-slide.png` | 28:30 | **PRINTED — `RSI RELATIVE STRENGTH INDEX`**: *"RSI Based on Close (won't fall for spikes) / Excellent for Confirming Shifts in Momentum / Excellent for Spotting Divergence / **Levels Can Be Counted Inside The Indicator** / In Order To Use TDI You Must Understand RSI"* |
| 16 | `V11_00-30-10_rsi-uses-list-slide.png` | 30:10 | **PRINTED — `RSI`**: *"Above/Below Market base line **(50)** / Base Line Break/Cross Shift In Momentum / OB / OS / **M Formation** / **W Formation** / Trend Line break"* |
| 17 | `V11_00-31-25_range-analysis-with-rsi-parameters-slide.png` | 31:25 | ⭐ **PRINTED — `RANGE ANALYSIS WITH RSI` — the lesson's parameter table.** See § THE PRINTED RSI PARAMETERS below |
| 18 | `V11_00-34-30_rsi-scale-overbought-oversold-diagram.png` | 34:30 | **PRINTED DIAGRAM** — a 10–90 scale with dashed bands: `Extreme Overbought` (~85), `Initial Overbought` (80), `POSITIVE` (above 50), `NEGATIVE` (below 50), `Initial Oversold` (~25), `Extreme Oversold` (~15) |
| 19 | `V11_00-37-30_range-rules-bull-8040-bear-6020-slide.png` | 37:30 | **PRINTED — `RANGE RULES`: `1. Bull Range: 80 / 40` · `2. Bear Range: 60 / 20`** |
| 20 | `V11_00-39-15_rsi-range-switch-8040-to-6020-diagram.png` | 39:15 | **PRINTED DIAGRAM — the range switch.** `80 / 40 → 60 / 20`, drawn as band pair **A** (80/40) on the left and band pair **B** (60/20) on the right |
| 21 | `V11_00-42-40_positive-trend-three-stages-diagram.png` | 42:40 | **PRINTED — `POSITIVE TREND`**, an S-curve with points 1/2/3 at ~40 / 50 / 60+: *"1. Short Term Trend Turning Up · 2. Intermediate Trend Turning Up · 3. Intermediate/Long Term Up (Begins Upside Acceleration)"* |
| 22 | `V11_00-44-15_negative-trend-three-stages-diagram.png` | 44:15 | **PRINTED — `NEGATIVE TREND`**, the mirror image, with a green hand-drawn annotation at point 1 |
| 23 | `V11_00-44-40_divergences-bear-and-bull-diagram.png` | 44:40 | **PRINTED — `DIVERGENCES`**, four labelled panels: `BEAR DIVERGENCE` (**A** RSI VALUE, **B** CLOSE PRICE) and `BULL DIVERGENCE` (**C** RSI VALUE, **D** CLOSE PRICE) |
| 24 | `V11_00-46-05_top-side-divergence-chart.png` | 46:05 | **`TOP SIDE DIVERGENCE`** — a live chart, price making an M while the sub-graph line stays flat, with a hand-drawn white trendline on each |
| 25 | `V11_00-46-45_mayonnaise-and-the-50-downtrend-chart.png` | 46:45 | ⭐ **The frame at the `"there's the mayonnaise. There's the 50"` sentence.** See § THE FRAME THAT DOES NOT SETTLE `C-018` below |
| 26 | `V11_00-47-35_dealer-hits-same-level-three-times-chart.png` | 47:35 | The three-touch example of `[00:47:31]`–`[00:49:52]`, with a red box over the touches and a hand-drawn white horizontal at the level |
| 27 | `V11_00-50-40_divergence-final-chart.png` | 50:40 | **`DIVERGENCE`** — the closing chart, price topping while the sub-graph rolls over. The lesson ends here, mid-sentence |

---

## ⭐ WHAT THE VISUALS ADDED — WRITTEN AFTER THE TRANSCRIPT PASS, PER §9

`SWF_CAPTURE_RECIPE.md` §9 puts the screenshot pass **last**, so that what the visuals change is
visible in the record rather than absorbed silently. Four things changed.

### 1. THE PRINTED RSI PARAMETERS — the lesson's one printed parameter table

Frame 17 (`31:25`) prints, verbatim:

```text
RANGE ANALYSIS WITH RSI

Parameters of RSI:  1. Value of RSI:  0 - 100
                    2. Normal Range:  70/30
                    3. Bull Range:    80/40
                    4. Bear Range:    60/20
                    5. Overbought/Oversold  80/20
                    6. Mid Point or Basis Level of 50
```

Every one of the six is also **spoken** at `[00:31:28]`–`[00:32:04]`, and the two agree exactly.
**Print and speech corroborate; nothing is added by either.**

> ### ⚠ AND THE THING THAT IS **NOT** ON THIS SLIDE IS THE ONE A BACKTEST NEEDS
>
> The slide is headed ***"Parameters of RSI"*** and it does **not state the RSI period.** Neither
> does any other frame in the lesson, and neither does the audio: `rsi` occurs **33** times and a
> lookback length is never attached to it. The word *"Parameters"* makes this a **near-miss of
> exactly the kind `D-030` exists for** — a session skimming for a parameter block would find one,
> and it does not contain the parameter.
>
> **`A-080` is opened on this**, and every RSI-dependent claim in V11 stays `DO NOT CODE`. The
> Tier 2 seminar notes were searched (`D-040` step 2) and **do not supply a period either**
> (`EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` describes the TDI's four components without
> a lookback). **Tier 1 silent, Tier 2 silent — the negative is recorded, and no number is
> invented.**

### 2. THE PRINT-VS-SPEECH DIVERGENCE ON THE `Trade Strong` MANTRA

Frame 10 (`20:20`) prints five commitments. The speaker reads them at `[00:20:18]`–`[00:20:52]`.
**Four match verbatim. One does not.**

| # | PRINTED (frame 10) | SPOKEN `[00:20:32]` |
|---|---|---|
| 1 | *"I will only take Second leg setups"* | same |
| 2 | *"I will only take M or W outside the box"* | same (+ *"dammit"*) |
| 3 | ***"I will not overleverage my account"*** | ***"I will not over leverage my account. I will not take a 25 risk on one trade"*** |
| 4 | *"I will execute with clarity free of distraction"* | same |
| 5 | *"I will never lift my stops"* | same |

**The spoken version carries a NUMBER the slide does not: *"a 25 risk on one trade"*.** It is
almost certainly *25 %* — no unit is spoken, and none is printed. **This is recorded as `A-081`
and is NOT resolved here**; the print does not disambiguate it, and inferring *"percent"* because
it is the only sensible unit is the `D-030` error in miniature. Note the direction of the gap:
**speech is the superset**, which is the opposite of the usual case and is why the divergence
would have been invisible to a screenshot-only pass.

### 3. THE HAND-DRAWN GEOMETRY IS BETTER EVIDENCE THAN THE AUDIO FOR THE `25 / 50`

Frame 4 (`07:45`) shows him writing **`25`** over **`50`** beside a drop out of a box, with
**`LOD`** written under the low. The audio at `[00:07:34]`–`[00:07:36]` is *"The distance is what?
25 to 50 pits [pips]"* — a bare number with no anchor stated in that sentence. **The drawing
supplies the anchor visually: the 25/50 is measured from the box down to the LOD region.** This
corroborates the reading already carried in `A-005`/`A-078` and adds nothing new to it; it is
recorded because it is the clearest single image of that geometry in the corpus so far.

### 4. THE FRAME THAT DOES **NOT** SETTLE `C-018` — and the honest report of a negative

Frame 25 (`46:45`) is the frame at the sentence *"Look where the averages are. There's the
mayonnaise. There's the 50"* — the sentence on which `C-018` is opened against `A-020`'s
`Mayo = 200`.

**It does not settle it, and this section exists to say so plainly rather than to squeeze a
reading out of a picture.**

What the frame actually shows:

- **At least four moving averages**, distinguishable by colour: **cyan** (highest and flattest —
  the slowest of the four), **red**, **yellow**, and a **white** line. Price trades **below** the
  cyan and red on the right-hand side, consistent with *"we're in a downtrend"*.
- A literal **blue rectangle** on the chart — the *"blue box"* is blue.
- The OHLC legend (`1.21739 1.21636 1.21708`) and an ADR panel reading
  **`Previous Days Range= 160.8`** and **`Current Days Range= 284`**.
- A sub-graph with a yellow line and a green line.
- **NO indicator legend, NO period label on any average, and no MT4 "Indicators List" window.**
  The chart is scrolled such that the upper-left of the price pane sits behind the drawing-tools
  toolbar.

**So the image confirms that several averages are on screen and confirms the downtrend; it cannot
say which line he is pointing at, and it cannot count the full set** (a fifth average could be off
the visible price range). `A-020`'s own *Required Research* — *"a screenshot showing the chart's
indicator list or a labelled average"* — is **still not satisfied**, four lessons after it was
written.

**Recorded as a negative result rather than omitted.** A frame that fails to resolve the question
it was extracted for is evidence about the question's difficulty, and leaving it out would let a
later session assume the check was never run.

---

## WHAT IS NOT HERE

- **No archival mp4 was produced.** `D-021` makes the real-time pass optional and this lesson gave
  no reason to want one; the 620-frame sweep is retained in the session scratchpad and the `.swf`
  is unmodified, so any timestamp can be re-rendered.
- **The pre-ingestion `SCREENSHOTS/` folder is NOT the source of anything here.** It holds one
  image, it is the lesson's title card, and `VISUAL_INDEX.md` describes it as an Asian-box chart
  with five EMAs. See `QUARANTINE_REGISTER.md` **Q-012** §3a.
