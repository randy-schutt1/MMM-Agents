# MMM TradingView Indicator — chart-marking aid for manual backtesting

> **Branch:** `feature/tradingview-mmm-indicator` · **Created:** 2026-08-13 · **Status:** `TOOL — NOT SPEC`
>
> Two Pine Script **v6** indicators (never strategies) that draw EMAs, session boxes and a TDI
> panel, so that manual chart study under `06_MANUAL_BACKTEST/` does not have to be done by eye.
>
> **This tool encodes no setup, fires no signal, and is evidence of nothing.**

---

## ⚠ READ FIRST — THE THREE THINGS THIS TOOL IS NOT

**1. It is not a Phase-5 Observer component, and it is not in `14_PINE/`.**
`DECISIONS.md` **D-006** defers Pine Script until the Master Specification (Phase 3) and Machine
Specification (Phase 4) exist. They do not. `14_PINE/README.md` says so on its own front page:
*"STATUS: EMPTY — DO NOT WRITE CODE YET."* That gate is intact and this tool does not breach it —
it lives under `06_MANUAL_BACKTEST/tools/`, which is where the manual-backtest helper scripts
already live (`run_pt033.py`, `sensitivity_pt033.py`, `crosscheck_pt034_vs_pt033.py`, …), and it
is a *drawing aid for a human*, not a machine translation of a rule. **If you find yourself
adding an entry condition to it, stop — that work belongs in `14_PINE/` after Phase 4.**

**2. Nothing it renders is evidence.**
Per `14_PINE/README.md`: *"Compilation is not validation."* A beautiful chart demonstrates
nothing. The TDI panel's settings now come from the owner's actual MT4 tooling rather than from
internet defaults (see A-039 below) — but *matching a rendering* still is not *validating a
method*, and the band's std-dev multiple remains unrecovered.

**3. It contains parameters that are outright guesses, and they are labelled as such.**
Every input in both files carries one of three tags — `[TIER 1]`, `[TIER 2]`, `[DEFAULT]` — in
the code comments and in the TradingView tooltips. The table below is the same information.

---

## What is implemented

| Component | File | Pane |
|---|---|---|
| Five EMAs — 5, 13, 50, 200, 800; each independently toggleable, each with its own colour and period input | `MMM_Indicator.txt` | overlay |
| Session boxes — Asian, London, London "prime", New York, NY "prime"; each independently toggleable | `MMM_Indicator.txt` | overlay |
| TDI — RSI line, Fast MA, Slow MA / Trade Signal, Market Base Line, Volatility Bands | `MMM_TDI.txt` | separate |

### Why two files rather than one

TDI is a 0–100 oscillator and belongs in its own pane; the EMAs and boxes belong on the price
chart, so they live in two scripts. Add both to the chart.

> **⚠ This rationale changed at the v5 → v6 port, and the earlier version of this README was
> wrong about it going forward.** It argued the split was *forced*: "a Pine v5 script occupies
> exactly one pane… two scripts is the only correct implementation — not a stylistic choice."
> That was true of **v5**. It is **not** true of v6, which adds `force_overlay` — a single v6
> script can declare `overlay = false` for the TDI panel and push the EMAs and boxes onto the
> price pane with `force_overlay = true`.
>
> So the split is now a **choice**, and the honest reason is a different one: two scripts means
> two settings dialogs, so the panel and the overlay can be toggled, restyled or removed
> independently — which is what chart-marking work actually wants. **Merging them into one v6
> script is fully supported** if you would rather have a single indicator; say the word.

---

## Source-verified vs. default — the whole picture

Sourcing tiers are `00_SYSTEM/SOURCING_HIERARCHY.md` (`D-040`): **Tier 1** = the course
recordings and their transcripts/slides (authoritative); **Tier 2** = the Mauro seminar-notes
PDF, cited `MMM-NOTES p.N` (`D-039`, normative but outranked by Tier 1); **Tier 3** = generic
internet material (**never** normative).

**No parameter in this tool comes from any lesson's `RULES.md` or `NOTES.md`.** Those are
quarantined fabricated content (`QUARANTINE_REGISTER.md` **Q-001**–**Q-011**) and were excluded
by instruction. This matters concretely: `Q-001`'s own evidence section shows that the
fabricated `RULES.md` sourced the EMA periods 5/13/50/200/800 to timestamp `[00:04:00]`, where
the actual V01 audio is the instructor telling students not to rush their homework. The periods
below rest on entirely different evidence.

### ✅ Source-verified

| Parameter | Value | Tier | Citation |
|---|---|---|---|
| EMA periods 5, 13, 50, 200 | 5 / 13 / 50 / 200 | **2** | `MMM-NOTES` **p.38**: *"The specific EMA's used in Mauro's charts are the 5, 13, 50 and 200 bar EMA's."* Roles on the same page: 5 & 13 *"are the signal lines"*, 50 *"is the balance line and shows the intraday trend"*, 200 *"is the home base defining the longer term trend."* |
| EMA period 800 | 800 | **1** | V09 `[00:41:43]`–`[00:41:48]`, quoted in `03_LESSON_NOTES/V09_SOURCE_NOTES.md` §9: *"This is the blueberry. **The blueberry is the 800 on the 15 minute time frame.**"* Explicit and unhedged; **the 15-minute timeframe is part of the definition.** |
| Asian session | 8:30pm – 3:00am | **1** | V02 slide *"ForEx Trading Times"* `[00:45:55]`, transcribed at `03_LESSON_NOTES/V02_SOURCE_NOTES.md` §4b. Corroborated Tier 2 by `MMM-NOTES` p.8 (`00:30–07:00 GMT`). |
| London session | 3:30am – 9:00am | **1** | Same slide. Corroborated by `MMM-NOTES` p.8 (`07:30–13:00 GMT`). |
| New York session | 9:30am – 5:00pm | **1** | Same slide. ⚠ Tier 2 p.8 gives the US close as `20:30 GMT` = **16:30 ET**, a genuine half-hour divergence from the Tier-1 slide's 5pm. Tier 1 wins; the divergence is noted, not hidden. |
| The session-box concept, and that the Asian box is one of them | — | **2** | `MMM-NOTES` **p.40**, *"Colour-Coded Sessions"*: *"Two boxes can be drawn. The 1st is drawn around the Asian session and simply denotes the area of consolidation that is expected during this period… It is just a guide."* |
| NY "prime" box **window** (NY open + ~3h → 09:30–12:30) | 3 hours | **2** | `MMM-NOTES` **p.40**: the second box *"starts at the beginning of the NY open and runs for about 3 hours"*, flagged as the **New York Reversal** window. |
| TDI's four lines and their roles (structure only) | — | **2** | `MMM-NOTES` **p.45–47**, recorded at `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2a. |

### 🔧 Recovered from tooling — a new evidence class, tagged `[TOOLING]`

Owner-supplied MT4 artifacts in `~/Desktop/Trading/Indicators/`. **This is neither Tier 1 nor
Tier 2** — see the A-039 section for why that distinction is being kept rather than quietly
collapsed.

| Parameter | Value | Source |
|---|---|---|
| TDI RSI period | **21** | `Ultimate Blue.tpl`, block `name=!SM_TDI`: `RSI_Period=21` |
| TDI RSI price | `close` | `RSI_Price=0` (MT4 `PRICE_CLOSE`) |
| TDI fast MA (RSI Price Line) | 2, SMA | `RSI_Price_Line=2`, `RSI_Price_Type=0` (MT4 `MODE_SMA`) |
| TDI slow MA (Trade Signal Line) | 7, SMA | `Trade_Signal_Line=7`, `Trade_Signal_Type=0` |
| TDI band / base-line period | 34 | `Volatility_Band=34` |
| Shark-fin levels | **63 / 37** | `SharkFin_Upper_Level=63`, `SharkFin_Lower_Level=37`, plus dedicated "Upper/Lower Shark Fin" buffers in the `.ex4` |
| Panel levels | 68 / 63 / 50 / 37 / 32 | the template's `level_0`…`level_4` |
| TDI line colours | DodgerBlue / LightSteelBlue / MidnightBlue / FireBrick | template `color_1`…`color_5` as MT4 BGR integers; they decode to exact MT4 web colours. **Buffer→line mapping is inferred**, not proven — buffers 1 and 3 share a colour and weight so they are read as the two bands. |

### ⚠ Defaults — NOT source-verified

| Parameter | Default | Why it is a default |
|---|---|---|
| **All five EMA colours** | cyan / orange / blue / pink / purple | **No colour for any moving average is stated anywhere** — not in the corpus, not in `MMM-NOTES`. `03_LESSON_NOTES/V05_SOURCE_NOTES.md` §8 records the negative result outright: *"No colours, no nicknames, no periods assigned."* Chosen only to be distinguishable. |
| EMA source | `close` | Not specified by any source. |
| **Session timezone** | Arm A, `UTC-5` | **This is the big one — see the next section.** |
| Day mask | `1234567` | The corpus states no day mask for the intraday table. |
| **London "prime" box (whole object)** | `03:30–07:30`, **OFF by default** | **No source defines any London sub-box.** See below. |
| The name *"prime"* on the NY box | — | The source calls it the **NY Reversal** box. The *window* is Tier 2; only the *name* is invented. |
| **TDI volatility-band std-dev multiple** | 1.6185 | **Still a guess.** The MT4 indicator exposes no input for it, so it is compiled into the `.ex4` and the template cannot reveal it. Remains the Tier-3 public value. See the A-039 section. |
| Box styling, label text, right-extension | — | Cosmetic. |

---

## The three caveats that actually matter

### 1. "Prime box" is not a term from this course

The string **`prime` occurs zero times in `03_LESSON_NOTES/` (V01–V10) and zero times in the
`MMM-NOTES` text extract.** It is not in the glossary, the ambiguity register, or the
contradictions register. It arrived with the build request, not from the source material. The
two boxes named "prime" here are therefore in **completely different evidentiary positions**,
and collapsing them would be a mistake:

- **NY prime box — the name is invented, the object is real.** It maps onto `MMM-NOTES` p.40's
  second box: NY open + ~3 hours, the New York Reversal window. It nests inside the NY session
  box by construction (09:30–12:30 ⊂ 09:30–17:00), both in time and — because its high/low is
  computed only from its own bars — in price. **Defaulted ON.**
- **London prime box — the whole object is invented.** No source describes a London sub-box at
  all. Note also that `MMM-NOTES` p.40 says *"**Two** boxes can be drawn"*, and a London box is
  not one of them. Its `03:30–07:30` default is constructed from the nearest documented
  statement, `MMM-NOTES` **p.51**: *"Trading hours should be from the end of the Asian session
  and into the London open for 4 hours."* That is a **screen-time recommendation, not a box**,
  and p.51 is itself ambiguous about whether the four hours run from the Asian close (03:00) or
  the London open (03:30). **Defaulted OFF**, and it should stay off unless you have a reason of
  your own. It carries no evidentiary weight.

### 2. The session timezone is an open question, not a setting — A-019 / D-031

The V02 slide prints a complete session table and **prints no timezone on it.** That is ambiguity
record **`A-019`**, still **OPEN**, still `DO NOT CODE`. The instructor declines to specify
(`[00:49:52]` *"Listen, don't analyse it… These are the times"*) and says the man who taught him
has died (`[00:49:22]`).

**`DECISIONS.md` D-031** converts this into a **tested variable with two pre-registered arms**:

| Arm | Setting | Meaning |
|---|---|---|
| **A** (default) | `UTC-5` fixed, year-round | The table is fixed clock numbers that never move |
| **B** | `America/New_York` | The table tracks the market's wall clock, shifting with DST |

> **The binding rule: run both arms and report both results, every time.** Divergence between
> them is a **finding**, never a selection criterion. Reporting only the arm that looks better is
> error class **E09** (cherry-picking) and **E24** — it is exactly how a timezone convention gets
> "validated" by noise. The timezone dropdown exists so both arms can actually be run. It is not
> a preference.

One cross-source observation, recorded because it is genuinely informative and **explicitly not
treated as closing A-019**: `MMM-NOTES` p.8 gives the sessions in GMT with an ET gloss — *"Gap
time between 07:00 and 07:30 GMT / 03:00 and 03:30 ET"*. `07:00 GMT` equals `03:00 ET` only at
`UTC-4`, so that document's own arithmetic is DST-tracking (Arm B), and under Arm B the Tier-2
GMT table and the Tier-1 slide agree on Asian and London **to the minute**. That is corroboration
worth knowing. It is one document's internal arithmetic, and `A-019` asks what **the course**
meant — so the record stays open and both arms stay.

### 3. The TDI panel's numbers now come from tooling, not guesswork — but A-039 is still open

**`A-039`** is `DO NOT CODE` / `DO NOT SUBSTITUTE`, still open. It records that TDI is treated as
a load-bearing entry criterion and is **never taught**:

- **V04** — named 6× as an entry condition, never defined.
- **V05** — frame `V05_00-36-54` prints the sub-panel header `TDI_MMM 54.6718 55.0688 53.6150`,
  the corpus's first displayed *name*; a slide is *titled* *"Mark up the TDI as well…"*. Still no
  inputs, periods, bands, line names or decision rule. **A name is not a definition.**
- **V07** — demoted in passing to *"an extra confirmation"*; *"shoulder verges"* (shoulder
  divergences) introduced and not defined.
- **V08** — the `TDI_MMM` panel is on screen for the entire 43-minute lesson and is **never
  mentioned aloud.**

Tier 2 has a dedicated TDI chapter (`MMM-NOTES` p.45–47) and it supplies **structure only**.
From `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2a:

> *"Zero numeric parameters. Anywhere. No RSI period, no signal-line period or type, no market
> baseline period, no volatility-band period or standard-deviation multiple, no price source, no
> timeframe. Searched across all 84 pages."*

**UPDATED 2026-08-13 — the numbers are no longer guesses, but the record is still open.**

This section previously said every TDI number here was a Tier-3 internet default. The owner has
since supplied the actual MT4 tooling in `~/Desktop/Trading/Indicators/`:

- **`Ultimate Blue.tpl`** — an MT4 chart template whose saved indicator block is literally
  `name=!SM_TDI`, carrying the inputs the chart was running (md5 `ea22c8cf…`).
- **`MM4XSF_TDI.ex4`** — the compiled indicator (md5 `42e97991…`), whose embedded strings read
  *"Copyright 2011, CompassFX"*, internal name **`mm4x-tdi`**, with buffers named *MarketBase
  Line*, *RSI Price Line*, *Trade Signal Line*, *Upper/Lower Shark Fin*, *Upper/Lower VB Break*,
  *MBL Slope* — and a parameter-name list **identical** to the template block, so it is the same
  indicator under a different filename.

`!SM_TDI` / `MM4X` read as Steve Mauro / Market Maker 4X, and the buffer names line up
one-for-one with the four lines `MMM-NOTES` p.45 describes. The recovered values are in the
`[TOOLING]` table above and are now the script's defaults.

> **The headline: `RSI_Period=21`, not 13.** The Tier-3 default this file previously shipped was
> **wrong**, and wrong on the single most consequential number in the indicator — everything
> drawn with RSI 13 was a different oscillator. That is exactly the failure mode A-039's
> `DO NOT SUBSTITUTE` exists to prevent, and it is now a demonstrated one rather than a
> hypothetical.

**Still not recovered: the standard-deviation multiple.** The MT4 indicator exposes no input for
it, so it is compiled into the `.ex4` and the template cannot reveal it. `bandMult` is still
1.6185 and still a guess. Four of the five numbers that shape this oscillator are now traceable
to an artifact; this one is not.

**This does NOT close `A-039`, and the distinction is deliberate.** `SOURCING_HIERARCHY.md` ranks
the recordings (Tier 1) and the Mauro PDF (Tier 2). An MT4 template on the owner's disk is
**neither** — it is a new evidence class with no tier and no admitting decision, and the Mauro
PDF itself needed **`D-039`**, an explicit owner attestation, before it could close anything.
Provenance is also weaker than it first looks: the files are dated **2016** and **2019**, the
bootcamp was recorded in **2012**, and nothing in the template proves the settings are the
instructor's rather than a later user's. So the tag is `[TOOLING]`, kept visibly distinct from
`[TIER 1]` / `[TIER 2]`, and `A-039` stays **OPEN** and `DO NOT CODE` pending a register entry
and an owner ruling.

**`A-032` is materially advanced and should be written up separately.** The indicator carries
first-class `SharkFin_Upper_Level` / `SharkFin_Lower_Level` inputs (**63 / 37**) and dedicated
*Upper/Lower Shark Fin* buffers. That record has carried the phrase since V03 with no definition
and exactly one located instance (frame `V07_00-18-25`). Thresholds are not a definition of the
pattern — but this is the first time the corpus has had numbers attached to the term at all.
Writing that up belongs in the ambiguity register, as a deliberate act; this tool does not do it.

**Therefore:** this panel may **not** be used to close `A-039`, `A-031` (*"blood in the water"*,
narrowed to the market-baseline cross, blocked downstream by A-039) or `A-032` (*"shark fin"*).
And no
backtest result depending on these numbers may be reported as a test of the method — it would be
a test of this file's guesses. The script carries a permanent, non-removable on-panel warning
label to that effect.

---

## Installation

> **Why `.txt` and not `.pine`:** both scripts are stored with a `.txt` extension so they open in
> any plain-text editor and can be selected and copied without fuss. The contents are ordinary
> Pine Script v6 and are unchanged by the extension — TradingView never reads the file, only what
> you paste into the Pine Editor, so the extension is irrelevant to it.

1. Open a GBP/USD chart (`D-007` — the project's primary research instrument) on an **intraday**
   timeframe. The 15-minute chart is the natural default, because the 800 EMA's Tier-1 definition
   is *"the 800 on the 15 minute time frame"*.
2. **Pine Editor** (bottom panel of TradingView) → **Open** → **New blank indicator**.
3. Paste the entire contents of `MMM_Indicator.txt`, replacing the template → **Save** → give it
   a name → **Add to chart**.
4. Repeat steps 2–3 for `MMM_TDI.txt`. It will attach in its own pane below price.
5. Open each script's settings (⚙) and set the **timezone arm** — and read the tooltip on that
   input before you choose.

Both scripts compile as-is with no external dependencies.

---

## Known limitations

**Pine / platform**

- **Pine v6 required** (`//@version=6` on line 1 of both files). They will not compile as v5 —
  `array.new<box>()` and the v6 `bool` semantics are assumed.
- **A `nz()` bug was fixed at the v6 port.** The first release tracked the previous bar's session
  state with `nz(inAsia[1], false)`, which does not compile: *"Cannot call `nz` with argument
  `source`=… (series bool). An argument of `series bool` type was used but a `simple int` is
  expected. (CE10123)"* — `nz()` has overloads for the numeric and colour types but **not** for
  `series bool`. The previous state is now carried in an explicit `var bool` and never read from
  history, which sidesteps the overload entirely and does not depend on whether `bool` may hold
  `na` (v5) or may not (v6).
- **Intraday only.** On daily-and-higher charts one bar spans every session, so no honest box
  could be drawn. Box drawing is *suppressed* rather than approximated, and a one-line on-chart
  notice appears so that "no boxes" is never misread as "no sessions found".
- **Box cap.** Pine hard-caps a script at 500 boxes; `max_boxes_count` is set to 500 and the
  *Sessions to keep* input (default 20 per box type, 5 types) prunes the oldest. Raise it and you
  will hit the ceiling.
- **Session boundaries need bars.** A box opens on the first bar whose timestamp falls inside the
  window. Over illiquid periods, holidays or broker feed gaps the box's edges follow the *data*,
  not the clock. Different brokers' GBP/USD feeds will therefore draw slightly different boxes
  from identical settings.
- **Boxes are live-updating within a session.** While a session is open its high/low extends with
  each new bar. This is intended, but it means a screenshot taken mid-session is not the final box.
- **800 EMA needs 800 bars of history.** It plots `na` until then. On short intraday histories it
  may not appear at all — that is missing data, not a bug.
- **One pane per script**, hence the two files (see above).
- Boxes are drawing objects, so they are not accessible to alerts and do not appear in the Data
  Window.

**Methodological**

- The **5pm high/low reset**, the **5pm–8pm dead gap**, and the two **changeover gaps**
  (3:00–3:30a, 9:00–9:30a) are all printed on the same Tier-1 V02 slide and are **not drawn** by
  this tool. That is a scope decision, not a sourcing gap — they are documented and available to
  a future version.
- **`C-010` is unresolved.** The corpus uses an 800 that `MMM-NOTES` does not contain anywhere in
  84 pages, while `MMM-NOTES` enumerates the set as *"the 5, 13, 50 and 200"*. Tier 1 outranks
  Tier 2 so the 800 stands and is defaulted ON — but the two sources genuinely disagree about the
  size of the set. Toggle the 800 off to see the Tier-2 set alone.
- **The "800-on-15m ≡ 200-on-1h" identity is not acted on.** It is spoken in V09 and recorded
  **NOTED, NOT ADOPTED** (`V09_SOURCE_NOTES.md` §9b). Every EMA here is computed on the chart's
  own timeframe; nothing is resampled and no timeframe is forced.
- **No EMA is labelled "Mayo".** `A-020` / `C-010` leave the *period* behind that nickname open —
  `V10_SOURCE_NOTES.md` records V10 using `blueberry` and `Mayo` as line names with **no period
  attached**. Labelling the 200 "Mayo" would invent the mapping the corpus withholds. Only
  *blueberry = 800 on the 15m* is safe, and it appears as a comment.

---

## Two adjacent finds in the same folder — recorded, NOT acted on

Found while extracting the TDI parameters. Neither changes this tool; both are logged so they
are not lost, and both need proper register treatment rather than a quiet adoption here.

**1. `!sm_WorkTime_v1.5b` corroborates the 800 EMA (bears on `C-010`).** The same
`Ultimate Blue.tpl` carries an `sm`-prefixed session tool whose inputs include `Alert50EMA`,
`Alert200EMA` and — decisively — **`Alert800EMA`** (with `Alert800Pips=30`). `C-010` is the
contradiction that the corpus uses an 800 which `MMM-NOTES` never mentions in 84 pages. Here is
a second artifact in the same lineage treating the 800 as a first-class object, which cuts the
same way Tier 1 does. It does **not** close `C-010`, which is about what the *sources* say.

The same indicator also has `draw_asian_box` / `draw_euro_box` / `draw_ny_box` /
`draw_mktopen_box` and a `DrawStopHuntBox` — i.e. the session-box concept, in the tooling.
**Its clock times are not usable as evidence**: the companion binary is named
`sm_WorkTime_no_autogmt`, meaning GMT auto-detection is off and the times are raw **broker
server time** with an unknown offset. They do not reconcile with the V02 slide under any single
consistent offset, so they are **not** imported into the session boxes and `A-019` is untouched.
Worth noting that `draw_mktopen_box=true` defines *two* one-hour windows (`10:00–11:00` and
`16:00–17:00`) — structurally the closest thing yet seen to a "prime box", still unnamed as such.

**2. `4X-2010-SEMA4X` does NOT carry the 5/13/50/200/800 set.** The template's EMA indicator has
`Period1=36`, `Period2=60`, `Period3=156`, `Period4=408` — four periods, none of them the
documented set, on an unrecorded timeframe. **Not adopted, and the EMA script is unchanged.**
Recorded because a future session will find this file and should know it was seen and rejected
rather than missed.

## Related records

`A-019` (session timezone) · `A-020` (moving-average nicknames) · `A-039` (TDI never taught) ·
`A-031` (blood in the water) · `A-032` (shark fin) · `A-005` (the trading zone) ·
`C-010` (the moving-average set) · `D-006` (Pine deferred) · `D-007` (GBP/USD) ·
`D-030` (no approximated definitions) · `D-031` (timezone is a tested variable) ·
`D-039` / `D-040` (the Mauro notes and the sourcing hierarchy) ·
`Q-001`–`Q-011` (quarantined fabricated notes — excluded from this tool entirely)
