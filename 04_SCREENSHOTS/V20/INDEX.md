# V20 — SCREENSHOT INDEX

**Lesson:** `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` — Week 9, Part 2, 2012-05-20
**22 frames**, captured by the `SWF_CAPTURE_RECIPE.md` §10 fast sweep at **10×**.
**Every frame retains the full 1024×786 stage including the control bar, so each one proves its own
timestamp from its own burned timecode.**

---

## §0 — ⚠️ REQUIRED §8a VERIFICATION — THE SWEEP→CLOCK OFFSET

**Capture parameters, read from THIS file's header rather than carried forward:**

| Field | Value | Source |
|---|---|---|
| Stage | **1024 × 786** | header RECT — so the play click is `(512, 300)` per `GOTCHA 5` |
| Declared `frameRate` | **3.0** | header |
| Patched rate | **30.0** (= 3.0 × 10) | ⭐ derived from **this** file's declared rate, never typed as a literal |
| `frameCount` | 8248 | header ⇒ implied duration **2749.333 s** |
| Sweep step | 5 presentation-seconds (500 ms wall) | 558 frames captured |
| Play-click guard | ⭐ **before/after screenshots differed — the click took effect** | `GOTCHA 5` |
| Port | verified free, then verified serving **my** bytes by SHA-256 | `GOTCHA 4` — ⚠️ **the first port picked was BUSY with another session's server and the check caught it** |

### The measurement — ⭐ A FIFTH SHAPE, AND IT CORROBORATES ITEM 296

`offset = burned − (i × 5)`, read from the pixels:

| frame `i` | expected `i × 5` | **burned timecode** | offset |
|---|---|---|---|
| 0 | 00:00 | **00:17** | **+17 s** |
| 1 | 00:05 | **00:18** | **+13 s** |
| 2 | 00:10 | **00:19** | **+9 s** |
| 24 | 02:00 | **02:00** | ⭐ **0 s** |
| 120 | 10:00 | **10:00** | **0 s** |
| 240 | 20:00 | **20:00** | **0 s** |
| 480 | 40:00 | **40:00** | **0 s** |
| 549 | 45:45 | **45:45** | **0 s** |

⭐⭐ **THE OFFSET IS A DECAYING TRANSIENT, NOT A CONSTANT: `+17 s` at the first frame, fully absorbed
by `i = 24` (two minutes in), and EXACTLY ZERO for the remaining 525 frames.**

⭐ **This is a second independent observation of the mechanism V19 offered as a hypothesis**
(`REVIEW_INDEX.md` item **296**). V19 measured `+16 s` / `+11 s` at `i = 0,1` and then flat; V20
measures `+17 / +13 / +9` and then flat. **Both sweeps schedule against an ABSOLUTE deadline
(`t0 + i × STEP_MS`) rather than an incremental sleep, so the play-click latency is absorbed instead
of accumulated.** ⚠️ **Item 296 is corroborated, not proven** — it predicts that an incremental-sleep
sweep would show a CONSTANT `+16 s`, and this session did not run one.

**Rate check (§8a step 3) — ORIGIN, NOT RATE.** Consecutive filename deltas equal consecutive burned
deltas exactly at `24 → 120 → 240 → 480 → 549`: every interval is an exact multiple of 5 s. **The
fps patch is correct.**

⭐ **CONSEQUENCE FOR NAMING: because the body offset is 0, `i × 5` and the burned timecode are the
same number, and every filename below carries the BURNED value.** ⚠️ **No frame was taken from the
transient region** — the earliest kept frame is `i = 5` (`00:25`), past the point where the offset
had decayed to under 1 s.

---

## §1 — THE FRAMES

| # | Frame | Burned | What is on screen |
|---|---|---|---|
| 1 | `V20_00-00-25_outside-structure-definition-five-clauses.png` | `00:25` | ⭐⭐ **THE DEFINITION SLIDE.** `MARKET MAKER TRAP MOVES` / *"Outside Structure:"* — five printed clauses (§2 below) |
| 2 | `V20_00-02-00_outside-structure-high-chart-circled.png` | `02:00` | Chart, red/yellow/cyan MAs + blue level; an aggressive drop hand-circled in red |
| 3 | `V20_00-04-35_classic-outside-structure-gbpchf-m15-annotated.png` | `04:35` | ⭐⭐ **`Classic Outside Structure`** — chart header reads **`GBPCHF,M15`**; printed annotation panel (§3) |
| 4 | `V20_00-11-20_intra-day-outside-structure-chart.png` | `11:20` | `Intra-Day Outside` titled chart; red/blue shaded boxes, `R = 24` / `R = 88` labels |
| 5 | `V20_00-18-20_multiday-outside-structure-gbpusd-m15.png` | `18:20` | ⭐ `Multiday Outside Structure`; chart header reads **`GBPUSD,M15`**; `R = 31.7` / `R = 16.1` |
| 6 | `V20_00-20-00_the-spike-title-railroad-spikes-photo.png` | `20:00` | `MARKET MAKERS BOOT CAMP` / `THE SPIKE`, photo of two railroad spikes in a hand |
| 7 | `V20_00-20-30_spike-definition-four-clauses.png` | `20:30` | ⭐⭐ **THE SPIKE DEFINITION**, four printed clauses (§4) |
| 8 | `V20_00-22-15_spike-single-candle-chart.png` | `22:15` | Chart, one dominant candle, green dashed levels top and bottom |
| 9 | `V20_00-25-50_rail-road-tracks-title-track-photo.png` | `25:50` | `MARKET MAKERS BOOT CAMP` / **`RAIL ROAD TRACKS`** (printed as two words), photo of a railway |
| 10 | `V20_00-26-15_rail-road-tracks-definition-30-minute.png` | `26:15` | ⭐⭐⭐ **THE DEFINITION SLIDE** (§5) |
| 11 | `V20_00-27-30_railroad-tracks-chart-circled-high.png` | `27:30` | Chart, the high hand-circled in magenta, red/blue level lines — the `30 minutes or less` example |
| 12 | `V20_00-29-00_entry-chart-green-arrow-quick-test-label.png` | `29:00` | Chart with a green up-arrow marking the entry; a `Quick Test and R & D` object is already on the canvas |
| 13 | `V20_00-30-15_mona-lisa-railroad-chart-wt-labels.png` | `30:15` | ⭐ The *"Mona Lisa"* chart — `wt = 53.2`, `wt = 85.0`, ADR high/low text, price scale legible |
| 14 | `V20_00-31-35_prevailing-theory-market-myths-slide.png` | `31:35` | ⭐ `MARKET MAKER MOVES` — the *"market myths"* slide (§6) |
| 15 | `V20_00-32-45_ab-equals-oh-crap-lightning-bolt.png` | `32:45` | Chart with `A`–`B`–`C`–`D` drawn as the lightning bolt and *"AB= OH CRAP!!!!"* typed on it |
| 16 | `V20_00-33-15_fib-retracement-not-usdchf-m15.png` | `33:15` | ⭐ **`USDCHF,M15`** with Fib levels `100.0 / 61.8 / 50.0 / 38.2` drawn and *"FIB Retracement…………NOT!!!!"*; a live MT4 panel shows `Spread 38.0`, `Hi to Low 964` |
| 17 | `V20_00-34-55_quick-test-and-r-and-d-slide.png` | `34:55` | ⭐⭐ **`QUICK TEST AND R & D`** — the assignment, printed (§7) |
| 18 | `V20_00-38-15_answers-nine-patterns.png` | `38:15` | ⭐⭐⭐ **`ANSWERS`** — the nine-item key, printed (§8) |
| 19 | `V20_00-39-05_sentiment-act-against-it.png` | `39:05` | *"Market Makers Create Sentiment And Act Against It / They Use News And Rumors To Take Your Money"* |
| 20 | `V20_00-39-45_remember-summary-nine-bullets.png` | `39:45` | ⭐⭐⭐ **`REMEMBER`** — the nine-bullet summary (§9) |
| 21 | `V20_00-43-40_remember-validate-technicals-lint.png` | `43:40` | `REMEMBER` — *"…I Hope He Comes Up With **Lint**! / You Now Know Better!!"* |
| 22 | `V20_00-44-00_closing-slide-good-night.png` | `44:00` | Closing slide (§10 — ⚠️ **and it contradicts the audio**) |

---

## §2 — FRAME 1, TRANSCRIBED FROM THE PIXELS — AND IT SETTLES TWO ASR DEFECTS

> **Outside Structure:**
> The Vector portion of The Half-A- Batman
> Used to set the **HOD /LOD** as a single leg only
> Used to Form the **HOW or LOW**
> Where as the stop hunt will come at a higher or lower level

⭐⭐ **`[00:00:48]`'s *"The high and the weak in the low of the week"* is `HOW or LOW`** — High Of
Week / Low Of Week. **The audio is unreadable and the slide is unambiguous.**

⚠️⚠️ **AND THE SLIDE IS NARROWER THAN THE SPEECH.** The printed clause names **only the
Half-A-Batman**; `[00:00:28]`'s *"The vector portion of **M or W formation**"* is **spoken and not
printed**. **Any claim that the outside structure is the vector of an M/W rests on the AUDIO
alone.**

---

## §3 — FRAME 3, THE ANNOTATION PANEL

> High is established / **RR Tracks** / MM comes near the **HOW** but does not break it / The Spread
> is widened at the test candles / Avg start to flatten / **Mustard makes an M** / Stops are hit 1 bar
> Short!!!!!!!!! / **+50**

⭐⭐ **THE CHART HEADER READS `GBPCHF,M15`.** See §11.

---

## §4 — FRAME 7, THE SPIKE DEFINITION

> **The Spike:**
> An aggressive change in price usually following a news announcement
> Used to Trigger stops or **move the trading zone.**
> Direction is based solely upon **dealer open volume (net short or net longs)**
> Nothing to do with the retail traders trend

---

## §5 — FRAME 10, THE RAILROAD-TRACK DEFINITION — ⭐⭐⭐ THE MOST VALUABLE FRAME IN THE SET

> **Rail Road Tracks:**
> A **30 minute** structure where the Market Makers trigger the stops, **Shift the zone** and Set the
> **HOD or LOD** on one move.

⭐⭐ **THIS SETTLES THE LESSON'S MOST FREQUENT SYSTEMATIC ASR DEFECT.** *"Shift his own"* — which
occurs five times in the committed transcript and sits **inside this definition** — is **`Shift the
zone`**. **The transcript cannot say it and the slide says it plainly.**

---

## §6 — FRAME 14

> Understand The Prevailing Theory Out There Gets You To Chase The Stop Hunt, Perhaps Run Fib
> Extensions Or **AB=CD** Projection. Maybe Take A **BO** or Two.
> These Are Market Myths And Will Always Lead To Failure !
> They Will Slowly Erode Your Equity, But Because You May Get Some Right, You Refill Your Account
> With Your Hard Earned Money!

⭐ Settles `[00:32:48]`'s *"the AV equals"* → **`AB=CD`**, and `BO` = breakout.

---

## §7 — FRAME 17, THE ASSIGNMENT, PRINTED

> **QUICK TEST AND R & D**
> Test: Make A List Of The Patterns That Were Covered.
> **R&D: Develop Flash Cards Of These Exact Sets.**

---

## §8 — FRAME 18, THE ANSWER KEY, PRINTED — NINE ITEMS

> **ANSWERS**
> 1. Half –A-Batman
> 2. Upside Down Half-A-Batman
> 3. Evening/Morning Star
> 4. Spike To The Low (vector)
> 5. Spike To The High (vector)
> 6. **RR Tracks**
> 7. **2 Pins High/Low M or W**
> 8. Extended Consolidation After A Pattern
> 9. ⭐ **Outside Structure**

⚠️ **Item 7 is ONE line, not two** — the audio at `[00:38:20]` (*"two pins high, low, and M and W"*)
reads as though it might be two. **The slide settles it.** ⭐ **And item 9 is the concept V20 added
tonight**; the audio trails off before naming it and **the slide carries it.**

---

## §9 — FRAME 20, THE SUMMARY, PRINTED — NINE BULLETS

> **REMEMBER**
> Fast Move Is False Move
> Never Chase Rising Or Falling Currency
> Market Makers Drop To Buy
> Market Makers Pump To Dump.
> **LOY and HOY Are Major Trap Moves Do Not Trade These As BO's**
> Market Makers Will Extend The High/Low In 3 Moves
> ⭐ **The Trend Move Is Slow And Steady**
> MMs Need To Book Profit Also So The Trend Move Will Contain **20 To 25 Pip Pullbacks And 3 Levels
> Of Move With Corresponding Levels Of Consolidation**
> A Powerful Or Extended Move Is Always Followed By Consolidation To Bring Traders Back Into The
> Fray, **Level 3**

⭐ ***"The Trend Move Is Slow And Steady"* is printed and NEVER SPOKEN** — it does not appear in the
marker grid in any form. **A rule recoverable only from the pixels.**

---

## §10 — ⚠️ FRAME 22 CONTRADICTS THE AUDIO, AND THE EXPLANATION IS BORING

The closing slide prints:

> **See You Next Sunday…..** / Keep the drills and home works going / NEVER TOO LATE TO ROLL UP YOUR
> SLEEVES AND TAKE RESPONSIBILITY FOR YOU TRADING!! / Good Night!

⛔ **The audio says the opposite**, `[00:43:55]`: *"We'll **not** see you next Sunday. **We're off.**
We're off. We're off."*

⭐ **NO CONTRADICTION RECORD IS OPENED, and the reason is stated so a reviewer can disagree.** This
is a **stock closing slide** carried between lessons — the same wording is plausible on every deck —
and **V19's own printed schedule settles the fact independently**: `May 27th — Memorial day weekend
- enjoy ( no session)`. **The speech and V19's schedule agree; the closing slide is stale
boilerplate, not a competing claim about method.** ⚠️ **It is recorded here rather than passed over,
and a reviewer who thinks a printed/spoken divergence must always get a `C-xxx` should charge it.**

---

## §11 — ⭐⭐⭐ THE FINDING THIS FRAME SET EXISTS FOR: **`M15` IS PRINTED ON THE CHARTS**

**Three separate charts carry an MT4 symbol header naming the timeframe:**

| Frame | Burned | Header |
|---|---|---|
| 3 | `04:35` | **`GBPCHF,M15`** |
| 5 | `18:20` | **`GBPUSD,M15`** |
| 16 | `33:15` | **`USDCHF,M15`** |

⭐⭐ **THE COURSE'S WORKING TIMEFRAME IS 15-MINUTE, AND HERE IT IS IN PRINT.** Until now the corpus
has carried this as a **derivation**: V19 `[00:41:32]`'s *"eight candles or greater … which is by
the way two hours"* gives `120 ÷ 8 = 15`, and `V19_INTERPRETATION.md` §2.3 graded it **HIGH and
DERIVED** because *"the lesson never says M15 — the string does not occur."*

⚠️⚠️ **THIS IS EVIDENCE ABOUT THE CHARTS THE INSTRUCTOR IS SHOWING, NOT A SPOKEN RULE.** V20 does
not **say** *"use the 15-minute chart"* either — **the string `M15` is spoken zero times in V20 as
well.** What changed is that the timeframe is now **directly attested in print on three charts
across three instruments**, instead of being computed from a bar count. ⭐ **`REVIEW_INDEX.md` item
245's remediation — which corrects `A-010` to *"On a 15-minute chart, eight"* — should see these
three frames.**
