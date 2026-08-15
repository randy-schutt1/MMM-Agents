# `06_MANUAL_BACKTEST/tools/` — chart-marking and chart-rendering aids

> **Status:** `TOOLS — NOT SPEC, NOT EVIDENCE`
> **Governing:** `D-006` (Pine gate) · `D-030` (never approximate a missing definition) ·
> `D-031` / `A-019` (the clock is a tested variable) · `D-043` (EMA mapping) ·
> `A-039` (TDI, still `OPEN`) · `COMMON_PROTOCOL.md` §2 `E06`

---

## WHAT LIVES HERE

| File | What it is | Where it runs |
|---|---|---|
| `mmm_chart_render.py` | **This branch.** Python renderer: candles + 5 EMAs + session boxes + TDI panel, batch-rendered to PNG from the derived M15/H1 CSVs. | Local, offline |
| `chart_renders/` | Its output. Gitignored bulk; two committed samples in `samples/`. | — |
| `MMM_Indicator.txt` | Pine v6 overlay — EMAs + session boxes | TradingView |
| `MMM_TDI.txt` | Pine v6 panel — TDI | TradingView |
| `MMM_Indicator_README.md` | The Pine tools' disclosure document | — |

> ### ⭐ UPDATED 2026-08-14 — **THE BRANCHES ARE MERGED, AND THE PAIR RULE IS NOW STANDING.**
>
> The note that stood here said the Pine files were *"not yet merged"* and that **if the two
> branches merged, the Pine files and this one must be reconciled as a pair.** **They merged
> at `b8b2c80`**, under `D-052` (the owner standardised on `MMM_TDI.txt`). That conditional
> is therefore spent, and `D-053` consequence 3 adopts its substance as a **standing rule**:
>
> ⛔ **A TDI or EMA parameter changed in `MMM_TDI.txt` / `MMM_Indicator.txt` MUST be changed
> in `mmm_chart_render.py` in the same commit, or the reason recorded.** A parameter changed
> in one and not the other is exactly the divergence this project keeps registers to prevent.
>
> **Reconciled 2026-08-14 at `D-053`:** all seven TDI numeric parameters and the band basis
> **agree** across the pair. The one divergence found was a **warrant tag, not a value** —
> both files called `RSI period 21` `[TOOLING]` when `A-080` had closed it
> `RESOLVED BY COURSE`. Corrected in both.
>
> ⭐ **`MMM_TDI.txt` is the PRIMARY TDI INSTRUMENT** (`D-053`). `mmm_chart_render.py` is its
> Python port; where they are ever found to disagree, **the Pine file is the reference and
> the disagreement is a defect to be recorded, not silently reconciled in either direction.**

---

## ⚠ THE THREE THINGS THESE TOOLS ARE NOT

**1. Not Phase-5 Observer components, and not in `14_PINE/`.**
`D-006` defers Pine Script and machine translation of rules until the Master Specification
(Phase 3) and Machine Specification (Phase 4) exist. They do not. `14_PINE/README.md` says
so on its own front page. These are **drawing aids for a human**, which is why they sit
here beside the manual-backtest scripts. **If you find yourself adding an entry condition,
stop — that work belongs in `14_PINE/` after Phase 4.**

**2. Nothing they render is evidence.**
*"Compilation is not validation."* A beautiful chart demonstrates nothing. This applies to
the PNG output with exactly the same force as to the Pine plots.

**3. They contain parameters that are outright guesses, and those are labelled.**
See the disclosure table below. Every value carries exactly one tag.

---

## HOW THE VISUAL METHOD DIFFERS FROM THE PT-SERIES — READ THIS BEFORE USING IT

This is the distinction most likely to be lost, so it is stated at length rather than in a
footnote.

### The PT-series is hypothesis testing

A `PT-xxx` test states a prediction **in advance**, pre-registers it in `PRE_REGISTERED/`,
fixes its window, runs once, and reports the number it gets — **including when the number
is unwelcome**. The pre-registration requirement is not bureaucracy: a hypothesis you can
revise after seeing the data is not a hypothesis, and `E09`/`E24` (cherry-picking) is the
failure it exists to prevent.

### This renderer is pattern-recognition practice

It draws a chart. **It states no prediction**, so there is nothing to pre-register and
**the pre-registration requirement does not apply to it.**

### The corollary, which is the part that gets forgotten

> **Because it makes no prediction, it also produces no evidence.**

Studying two hundred rendered windows and forming an impression is **not a finding**. It
does not close an `A-xxx` ambiguity, does not resolve a `C-xxx` contradiction, does not
support or undermine any rule, and **may not be cited in a mastery report as though it
did.** What it legitimately produces is a student who recognises a shape faster on a live
chart. That is worth having and it is not a result.

### The two are complements, not substitutes

| | PT-series | This renderer |
|---|---|---|
| Question | "Does X hold, measurably, over window W?" | "What does this actually look like?" |
| Pre-registration | **Required** | Not applicable — nothing is predicted |
| Output | A number, with `n`, and its exclusions | An image |
| Can it close an ambiguity? | Yes, within its stated scope | **No. Never.** |
| Can it be cited as evidence? | Yes | **No** |
| Governing failure mode | Cherry-picking (`E09`/`E24`) | Believing you have learned something measurable |

### And `E06` binds both

`COMMON_PROTOCOL.md` §2, restated by `D-036a`: **a chart may be LOOKED AT; nothing may be
MEASURED OFF one.** Every number reaching a result comes from a checksummed CSV via a
committed script. `mmm_chart_render.py` writes pixels and reads none — which is precisely
why it can exist without weakening anything. **If you catch yourself reading a level off one
of these PNGs, that is an `E06` breach**, and the fix is to query the CSV.

---

## DISCLOSURE TABLE — WHAT IS SOURCE-VERIFIED, WHAT IS NOT

Tags, in descending strength. This mirrors `MMM_Indicator_README.md`; the tags are copied,
not re-derived.

| Tag | Meaning |
|---|---|
| `[TIER 1]` | Stated in the course recordings/slides. Authoritative. |
| `[TIER 2]` | Stated in MMM-NOTES, the Mauro seminar PDF (`D-039`). Normative, outranked by Tier 1. |
| `[TOOLING]` | Recovered from the owner's MT4 artifacts. **Not a tier** — no admitting decision exists. Scoped to **parameters only**: it may say what number was in a settings box; it may never say what was taught. Artifacts are dated 2015–2019; the bootcamp was recorded 2012. |
| `[OWNER-ATTESTED]` | Stated directly by the project owner, cited to its `DECISIONS.md` entry. **Not a tier** — `D-041` put owner attestation outside the hierarchy as an adjudication warrant. Stronger than `[DEFAULT]` (testimony, not invention); weaker than `[TIER 1]` (no recording shows it). |
| `[DEFAULT]` | **Not source-verified. This tool's choice.** Change freely. |

**Never used at all:** any lesson `RULES.md` / `NOTES.md` — quarantined fabricated content,
`QUARANTINE_REGISTER.md` Q-001…Q-011. No parameter here comes from them.

### EMAs — periods

| Period | Tag | Warrant |
|---|---|---|
| 5, 13, 50, 200 | `[TIER 2]` | MMM-NOTES p.38: *"The specific EMA's used in Mauro's charts are the 5, 13, 50 and 200 bar EMA's."* Roles on the same page: 5/13 signal lines, 50 balance line, 200 home base. |
| 800 | `[TIER 1]` | V09 `[00:41:43]`: *"This is the blueberry. The blueberry is the 800 on the 15 minute time frame."* **The 15-minute timeframe is part of the definition.** |

> ⚠ **`C-010` is unresolved.** MMM-NOTES enumerates the set as 5/13/50/200 and contains
> **zero** occurrences of 800 across 84 pages. Tier 1 outranks Tier 2 so the 800 stands, but
> the two sources genuinely disagree about **the size of the set**.
>
> ⚠ **On H1 charts the 800 is drawn on a timeframe no source places it on.** V09 defines it
> *on the 15-minute*. The renderer prints this warning on every H1 image rather than drawing
> it silently. The "800-on-15m == 200-on-1h" identity is spoken in V09 but recorded
> **NOTED, NOT ADOPTED** (`V09_SOURCE_NOTES` §9b); this tool does not act on it and
> resamples nothing.

### EMAs — colours: ALL FIVE ARE `[OWNER-ATTESTED]` (`D-043`), NOT OBSERVED ON-SCREEN

| Period | Nickname | Colour | Tags |
|---|---|---|---|
| 5 | mustard | **YELLOW** `#FFFF00` | `[OWNER-ATTESTED]` **+ `[TIER 1]` on the colour** |
| 13 | ketchup | **RED** `#FF0000` | `[OWNER-ATTESTED]` **only** |
| 50 | water | **AQUA** `#00FFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` |
| 200 | mayonnaise | **WHITE** `#FFFFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` |
| 800 | blueberry | **BLUE** `#0000FF` | `[OWNER-ATTESTED]` + `[TOOLING]` |

Cite as **"OWNER-ATTESTED (`D-043`), not observed on-screen."** No frame in
`04_SCREENSHOTS/` carries a legend and no speaker in V01–V11 names a colour and a
**nickname** in the same sentence — `V05_SOURCE_NOTES` §8 records the negative result
explicitly.

- **The one exception** is the 5's **colour**: V07 `[00:25:34]` — *"this yellow one is a
  five moving average"* — the only place in V01–V11 a speaker joins a colour to a period in
  one sentence. That cell alone is additionally `[TIER 1]`.
- **It does not extend to the nickname.** *"mustard = 5"* still requires chaining V07's
  *yellow = 5* through the owner's *mustard = yellow*, and **no speaker makes that join**.
  Only **blueberry** is `RESOLVED BY COURSE` (V09).
- **`I-011` is CLOSED** (`D-043`). `D-043` **reversed** `D-041`'s nickname↔period *and*
  `D-042` §2's period↔colour; their composition — nickname↔colour — **did not change**. If
  you are reading a cached copy or the `D-042` wording: **5 is now YELLOW, 13 is now RED.**
- **Nicknames are deliberately not used as plot labels.** Labelling the 200 *"Mayo"* would
  invent the mapping `A-020` records as still open.

### TDI — `A-039` IS STILL `OPEN` AND STILL `DO NOT CODE`

> ⚠ **The commissioning brief for the renderer described these as "Tier 3 defaults only".
> That is out of date** and porting it forward would have understated what is known.
> `MMM_TDI.txt` was rewritten 2026-08-13: four of the five numbers are now `[TOOLING]`,
> recovered from the owner's MT4 artifacts (`!SM_TDI` in `Ultimate Blue.tpl`;
> `MM4XSF_TDI.ex4`, CompassFX 2011). **The headline was `RSI_Period` 13 → 21** — the Tier-3
> internet default previously shipped was wrong on the most consequential number in the
> indicator, and everything drawn with RSI 13 was a different oscillator.

| Parameter | Value | Tag |
|---|---|---|
| RSI period | **21** | ⭐ **`[TIER 1]`** — `A-080` **`CLOSED — RESOLVED BY COURSE`**, three independent Tier 1 instances (incl. V13 first-person *"we have it set to 21"*); V13 `[00:54:51]` makes it a lookback in **chart periods, scaling with timeframe**. `!SM_TDI RSI_Period=21` **corroborates** and is no longer the warrant — **tag corrected at `D-053`**, which found both tools understating this. **Not** the Tier-3 13 |
| RSI source | close | `[TOOLING]` — `RSI_Price=0` = MT4 `PRICE_CLOSE` |
| Fast MA (RSI Price Line) | **2**, SMA | `[TOOLING]` — `RSI_Price_Line=2`, `Type=0`. `A-084` **`PROVISIONALLY RESOLVED — TOOLING`** at `k = 2`, on the §3.4 re-check list |
| Slow MA (Trade Signal Line) | **7**, SMA | `[TOOLING]` — `Trade_Signal_Line=7`, `Type=0`. ⛔ **`A-085` — see the box below. This line does NOT poll the one-hour chart** |
| Volatility band / base-line period | **34** | ⛔ `[TOOLING]` — `Volatility_Band=34`. **THIS IS `A-086`'s MISSING QUANTITY.** `D-045`-**ELIGIBLE, NOT ADOPTED**; never stated in Tier 1 or Tier 2. **It is why the bands are unconstructible and why `A-031`/`A-032` are uncomputable** |
| **Band BASIS** — deviation of *what*? | **the RSI line** | ⚠ `[OWNER-RULED]` — **`D-052`, `OWNER EMPIRICAL PREFERENCE`.** `dev = mult × stdev(RSI)`, **not** of the base line. ⛔ **NOT course-verified:** Tier 1 V14 `[00:45:09]` and Tier 2 `MMM-NOTES` p.45 **both** say the market base, both stand unretracted, and the ruling **overrides** them. `C-021` closed on it |
| **Band std-dev multiple** | **1.6185** | ⛔ **`[DEFAULT]` — STILL A GUESS, AND STILL OWED.** The MT4 indicator exposes no input for it, so it is compiled into the `.ex4` and the template cannot reveal it. **Still the Tier-3 public value.** ⚠ **And V14 `[00:45:09]`'s unhedged *"two standard deviations"* has a Tier 1 warrant this number does not** — `D-052` consequence 6, reaffirmed at `D-053` consequence 5, **not resolved** |
| Levels 68 / 50 / 32 | | `[TOOLING]` — template level list |
| Shark-fin levels 63 / 37 | | `[TOOLING]` — `SharkFin_Upper/Lower_Level`, with dedicated buffers. **`A-032` remains OPEN** — these are the indicator's thresholds, not a definition of the pattern. |
| Line colours | | `[TOOLING]`, **but the buffer→line mapping is INFERRED** — the template does not name its buffers. Sensible, not proven. |

> ## ⛔⛔ `A-085` — THE TRADE SIGNAL LINE. **THIS TOOL DOES NOT DO WHAT THE LESSON SAYS THE TSL DOES.**
>
> **`D-053` §3(a).** V12 `[00:11:49]`, restated `[00:11:59]`: *"The TSL in essence is a **polling
> of the one-hour chart**, brought into your view on the 15 minute."* `[00:12:07]`: *"when you get
> a crossover right here, in essence **you now have a signal on the one-hour chart**."*
>
> **What the line actually is, in both tools:** a **7-period SMA of the RSI, on the chart's /
> render's own timeframe.** Nothing in it reads a higher timeframe, and nothing in the shipped TDI
> ever did. `A-085` records that the claim may describe an **effect** (a smoothed line lags like a
> slower timeframe) stated as though it were a **mechanism**, does **not** adjudicate which, and is
> ⛔ `DO NOT CODE`.
>
> ⛔ **A crossover of this line is a crossover of a 7-SMA of the RSI on the timeframe in front of
> you. It is NOT evidence that "a one-hour signal has fired" and may not be reported as one.**
>
> ⚠️ **Why this outranks the other open records in practical danger:** V12 `[00:12:18]` tells a
> student they *"not necessarily"* need to consult the one-hour chart given a shark fin and blood
> in the water. **A student is told they may stop looking at a timeframe on the strength of this
> claim** — and if the claim is an effect rather than a mechanism, that advice is unsafe. Neither
> tool can tell you which it is.
>
> ⛔ **Do not "fix" this** by wiring an H1 `request.security()` / resample into either tool. That is
> `D-030`'s forbidden act — inventing a construction the corpus never gave — and it would look
> authoritative on a chart or a rendered PNG. `A-085` closes on a lesson that states a
> construction, or it does not close.

**Why `A-039` does not close.** An MT4 template on the owner's disk is neither Tier 1 (the
recordings) nor Tier 2 (the Mauro PDF). It is an evidence class with no tier and no
admitting decision — the Mauro PDF itself needed `D-039` before it could close anything.
**Consequence:** this panel may not close `A-039`, `A-031` ("blood in the water") or
`A-032` ("shark fin"), and **no backtest depending on these numbers may be reported as a
test of the method.** What changed is only that the numbers trace to an artifact rather than
to a forum post. **Four of the five are sourced; the band multiple is not, and the bands on
every rendered image are drawn with a number nobody has verified.**

### Session boxes — times `[TIER 1]`, timezone `A-019` OPEN

The V02 slide `[00:45:55]`, verbatim (`V02_SOURCE_NOTES` §4b):

```text
5pm High / Low Reset (The MM Spread Is Set)
5pm to 8pm Dead Gap
Asian Session:    8:30pm - 3:00am    Gap 3-3:30a
London Session:   3:30am - 9:00am    Gap 9-9:30a
New York Session: 9:30-5pm
```

| Box | Window | Default | Tag |
|---|---|---|---|
| Dead gap + 5pm reset line | 17:00–20:00 | on | `[TIER 1]` — same slide |
| Asian range | 20:30–03:00 | on | `[TIER 1]` times; `[TIER 2]` corroborates the box concept (MMM-NOTES p.40) |
| London | 03:30–09:00 | on | `[TIER 1]` times |
| New York | 09:30–17:00 | on | `[TIER 1]` times |
| NY prime / reversal | 09:30–12:30 | on | **Window `[TIER 2]`** (p.40: *"starts at the beginning of the NY open and runs for about 3 hours"*); **the NAME "prime" is `[DEFAULT]`** |
| London prime | 03:30–07:30 | **OFF** | ⚠ **`[DEFAULT]` ENTIRELY — no source defines any London sub-box.** Enable with `--london-prime`. No evidentiary weight whatsoever. |

> ⚠ **"PRIME BOX" IS NOT A TERM FROM ANY SOURCE IN THIS REPOSITORY.** It occurs **zero**
> times in `03_LESSON_NOTES/` and **zero** times in MMM-NOTES. It arrived with a build
> request. The NY prime box maps onto a real documented object so only its *name* is
> unsourced; the London prime box has no source at all and ships off.

> ⚠ **`A-019` — the course prints the session table and NO TIMEZONE.** Still `OPEN`, still
> `DO NOT CODE`. The instructor declines to specify (V02 `[00:49:52]` *"Listen, don't
> analyse it… These are the times"*) and says the man who taught him has died
> (V02 `[00:49:22]`). `--arm` is how `D-031`'s two arms actually get run. **Run both.
> Report both.** Divergence is a *finding*, never a selection criterion — reporting only
> the better-looking arm is `E09`/`E24`.

**Measured and useful:** at M15 and H1 the two arms produce **bar-for-bar identical
candles**; only the label moves (`CROSSCHECK_REPORT.md` §2). So the arm choice cannot change
an EMA value, a TDI value or a bar range at these timeframes — **it changes only which
session a bar falls in.** That is exactly why the session boxes, and nothing else on the
chart, are what the arm actually moves. It will **not** hold at a timeframe that does not
divide an hour.

### What the Pine tools draw that this does not

The two changeover gaps (`3:00–3:30a`, `9:00–9:30a`) are documented Tier 1 objects on the
same slide, and are **out of scope here rather than unsourced** — they read as the absence
between two boxes. The `[TOOLING]` "mktopen" open-hour boxes are **not ported at all**:
their window length is doubly corroborated but their conversion to an ET clock rests on an
unverified GMT+3 server-offset inference, which is precisely the `A-019` question. In the
Pine file they ship disabled behind a warning; here they are simply absent, which is the
same decision with less surface area.

---

## `mmm_chart_render.py` — USAGE

### Requirements

`python3` with `numpy` and `matplotlib` (Agg backend; no display needed). `mplfinance` is
**not** required — candles, boxes and the TDI panel are drawn directly so the layout,
z-ordering and the provenance strip are fully controlled.

### Input

The derived corpus at `../datasets/HISTDATA_GBPUSD_M15_H1/derived/`. **Run its QA gate
first** — `qa_histdata_htf.py` is a precondition, not a formality.

### One window

```bash
python3 06_MANUAL_BACKTEST/tools/mmm_chart_render.py \
    --data 06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M15_H1/derived/GBPUSD_M15_ARMA.csv \
    --timeframe M15 --arm A --start 2015-03-02 --window 2d \
    --out 06_MANUAL_BACKTEST/tools/chart_renders
```

### A batch of windows

```bash
python3 06_MANUAL_BACKTEST/tools/mmm_chart_render.py \
    --data .../GBPUSD_H1_ARMA.csv --timeframe H1 --arm A --window 7d \
    --batch 2015-01-05,2015-04-13,2015-08-17,2015-11-02 \
    --out 06_MANUAL_BACKTEST/tools/chart_renders
```

### Options

| Flag | Default | Notes |
|---|---|---|
| `--timeframe` | required | `M15` or `H1` |
| `--arm` | required | `A` or `B`. **The arm the FILE is stamped in.** Run both. |
| `--window` | `2d` (M15) / `7d` (H1) | `Nd` / `Nw` / `Nh` |
| `--out` | `renders` | Use `chart_renders/` — it is gitignored |
| `--no-boxes`, `--no-tdi` | off | |
| `--london-prime` | off | ⚠ enables the wholly unsourced box |
| `--hide-ema` | — | e.g. `--hide-ema 800` to see the Tier-2 set alone |
| `--width/--height/--dpi` | 1800×1150 @ 110 | |

### Legibility is the constraint, not bar count

Raised explicitly with the owner and treated as the governing constraint. **A window that
crams a month of M15 into 1800 px produces candles two pixels wide, which is not a chart
anyone can read a shape off — and reading shapes is the entire purpose.** Defaults keep a
candle body at roughly 6–14 px:

| Timeframe | Default window | Bars | Soft cap |
|---|---|---|---|
| M15 | 2 days | ~192 | 400 — warns above, renders anyway |
| H1 | 7 days | ~120 | 400 — same |

The cap warns rather than refuses: a deliberately wide overview is a legitimate thing to
want, and the warning stops it happening by accident.

### Two correctness details worth knowing

- **EMA warm-up.** Indicators are computed over the **entire** loaded series and only then
  sliced to the window. Loading just the requested window and computing an 800 EMA on it
  produces a line that looks like an EMA and is meaningless. The tool warns when fewer than
  `5 × 800` bars precede a window.
- **Pine-matching maths.** `ta.ema` is SMA-seeded then `α = 2/(n+1)`; `ta.rsi` uses Wilder's
  RMA, **not** an SMA; `ta.stdev` is **population** (divisor `n`). Ported to match, so the
  PNG and the TradingView plot agree.

### Every image carries its own provenance

Stamped on the figure, so a screenshot cannot be separated from its caveats: the `D-031`
arm, `A-019 OPEN`, the `D-043` colour warrant, the `E06` rule, the derived-not-native data
note, the H1 800-EMA warning, and — when the window spans the documented 2014-06-01/02
corpus hole — **an explicit warning that the flat stretch is missing data, not a quiet
market.**

---

## SAMPLES

`chart_renders/` is gitignored bulk. Two representative images are committed under
`chart_renders/samples/`; the full demonstration set generated 2026-08-13 was:

| Window | TF / arm | Why this one |
|---|---|---|
| 2015-03-02, 2d | M15 / A | Ordinary two-day session cycle — the baseline look. **Committed sample.** |
| 2015-03-02, 2d | M15 / **B** | The **same window on the other arm**: candles identical, session boxes shifted. `D-031` made visible in one comparison. |
| 2016-06-23, 2d | M15 / A | EU referendum — the corpus's largest event, inside DEVELOPMENT per `D-035`. |
| 2014-05-29, 5d | M15 / A | **Spans the documented 2014-06-01/02 hole** — demonstrates the missing-data warning firing. |
| 2015-08-17, 7d | H1 / A | High-volatility August 2015 week; also shows the H1 800-EMA warning. **Committed sample.** |
| 2015-12-20, 7d | H1 / A | Christmas week — a genuine short/thin market, one of the `C8`-flagged closures. |

Regenerate any of them from the commands above; nothing is lost by not committing them.
