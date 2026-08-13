# MMM TradingView Indicator — chart-marking aid for manual backtesting

> **Branch:** `feature/tradingview-mmm-indicator` · **Created:** 2026-08-13 · **Status:** `TOOL — NOT SPEC`
>
> Two Pine Script v5 **indicators** (never strategies) that draw EMAs, session boxes and a TDI
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
nothing. In particular, agreement between the TDI panel here and a TDI panel in the course
proves nothing, because **the course's own TDI settings are unknown** (see A-039 below).

**3. It contains parameters that are outright guesses, and they are labelled as such.**
Every input in both files carries one of three tags — `[TIER 1]`, `[TIER 2]`, `[DEFAULT]` — in
the code comments and in the TradingView tooltips. The table below is the same information.

---

## What is implemented

| Component | File | Pane |
|---|---|---|
| Five EMAs — 5, 13, 50, 200, 800; each independently toggleable, each with its own colour and period input | `MMM_Indicator.pine` | overlay |
| Session boxes — Asian, London, London "prime", New York, NY "prime"; each independently toggleable | `MMM_Indicator.pine` | overlay |
| TDI — RSI line, Fast MA, Slow MA / Trade Signal, Market Base Line, Volatility Bands | `MMM_TDI.pine` | separate |

### Why two files rather than one

TDI is a 0–100 oscillator and belongs in its own pane; the EMAs and boxes belong on the price
chart. **A Pine v5 script occupies exactly one pane.** The `force_overlay` argument that would
let a single script write to both was introduced in **Pine v6** and does not exist in v5. Since
the brief specifies v5 *and* a separate TDI pane, two scripts is the only correct
implementation — not a stylistic choice. Add both to the chart.

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

### ⚠ Defaults — NOT source-verified

| Parameter | Default | Why it is a default |
|---|---|---|
| **All five EMA colours** | cyan / orange / blue / pink / purple | **No colour for any moving average is stated anywhere** — not in the corpus, not in `MMM-NOTES`. `03_LESSON_NOTES/V05_SOURCE_NOTES.md` §8 records the negative result outright: *"No colours, no nicknames, no periods assigned."* Chosen only to be distinguishable. |
| EMA source | `close` | Not specified by any source. |
| **Session timezone** | Arm A, `UTC-5` | **This is the big one — see the next section.** |
| Day mask | `1234567` | The corpus states no day mask for the intraday table. |
| **London "prime" box (whole object)** | `03:30–07:30`, **OFF by default** | **No source defines any London sub-box.** See below. |
| The name *"prime"* on the NY box | — | The source calls it the **NY Reversal** box. The *window* is Tier 2; only the *name* is invented. |
| **Every numeric TDI parameter** | 13 / 2 / 7 / 34 / 1.6185 | **Tier 3 public defaults. See the A-039 section.** |
| TDI colours, MA type, 32/50/68 levels | — | Not stated by any source. |
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

### 3. Every number in the TDI panel is a guess — A-039

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

The defaults shipped here — RSI 13, fast 2, slow 7, bands 34 @ 1.6185 — are the publicly
circulating Dean Malone TDI defaults, i.e. **Tier 3**: *"EXTERNAL — NON-NORMATIVE, permanently.
Closes nothing, unblocks nothing, cited in no artifact."* They are present only so the panel
renders. Reconstructing settings from *"an improved version of the RSI"* is precisely the
approximation **`D-030`** forbids.

**Therefore:** this panel may **not** be used to close `A-039`, `A-031` (*"blood in the water"*,
narrowed to the market-baseline cross, blocked downstream by A-039) or `A-032` (*"shark fin"*,
located on frame `V07_00-18-25` as a red box drawn on a TDI sub-panel, still undefined). And no
backtest result depending on these numbers may be reported as a test of the method — it would be
a test of this file's guesses. The script carries a permanent, non-removable on-panel warning
label to that effect.

---

## Installation

1. Open a GBP/USD chart (`D-007` — the project's primary research instrument) on an **intraday**
   timeframe. The 15-minute chart is the natural default, because the 800 EMA's Tier-1 definition
   is *"the 800 on the 15 minute time frame"*.
2. **Pine Editor** (bottom panel of TradingView) → **Open** → **New blank indicator**.
3. Paste the entire contents of `MMM_Indicator.pine`, replacing the template → **Save** → give it
   a name → **Add to chart**.
4. Repeat steps 2–3 for `MMM_TDI.pine`. It will attach in its own pane below price.
5. Open each script's settings (⚙) and set the **timezone arm** — and read the tooltip on that
   input before you choose.

Both scripts compile as-is with no external dependencies.

---

## Known limitations

**Pine / platform**

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

## Related records

`A-019` (session timezone) · `A-020` (moving-average nicknames) · `A-039` (TDI never taught) ·
`A-031` (blood in the water) · `A-032` (shark fin) · `A-005` (the trading zone) ·
`C-010` (the moving-average set) · `D-006` (Pine deferred) · `D-007` (GBP/USD) ·
`D-030` (no approximated definitions) · `D-031` (timezone is a tested variable) ·
`D-039` / `D-040` (the Mauro notes and the sourcing hierarchy) ·
`Q-001`–`Q-011` (quarantined fabricated notes — excluded from this tool entirely)
