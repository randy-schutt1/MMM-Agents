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
Every input in both files carries one tag — `[TIER 1]`, `[TIER 2]`, `[TOOLING]`,
`[OWNER-ATTESTED]` or `[DEFAULT]` — in the code comments and in the TradingView tooltips. The
table below is the same information.

> **`[OWNER-ATTESTED]` was added 2026-08-13 (`D-042`).** It means *the project owner stated this
> directly*. It ranks **above `[DEFAULT]`** — testimony beats this file's invention — and **below
> `[TIER 1]`** — no recording or frame shows it. It is **not a tier**: `D-041` established that
> owner attestation sits *outside* the source hierarchy, as an adjudication warrant.
> **Where a recording contradicts an `[OWNER-ATTESTED]` value, the contradiction is named at the
> value and put to the owner — never resolved here.** ⭐ **That rule has now been exercised end to
> end and it worked.** The 5/13 EMA colours were flagged as contradicted by V07 `[00:25:34]`
> (`I-011`), shipped with the flag attached rather than silently "fixed", and **the owner
> reversed** — `D-043`, 2026-08-13. See the ✅ block below. **An `[OWNER-ATTESTED]` value is
> therefore not a settled value; it is the best available one until the owner is asked again.**

---

## What is implemented

| Component | File | Pane |
|---|---|---|
| Five EMAs — 5, 13, 50, 200, 800; each independently toggleable, each with its own colour and period input | `MMM_Indicator.txt` | overlay |
| Session boxes — Asian, London, London "prime", New York, NY "prime", the 5pm–8pm dead gap, and two "mktopen" open-hour boxes; each independently toggleable | `MMM_Indicator.txt` | overlay |
| The 5pm high/low reset, as a vertical line on the dead gap's opening bar | `MMM_Indicator.txt` | overlay |
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
| **5pm high/low reset** | 5:00pm | **1** | Same slide: *"5pm High / Low Reset (The MM Spread Is Set)"*. One of two lines `V02_SOURCE_NOTES.md` §4b flags as appearing **only** on the slide and never in the audio. |
| **Dead gap** | 5:00pm – 8:00pm | **1** | Same slide: *"5pm to 8pm Dead Gap"*. The other slide-only line. |
| The session-box concept, and that the Asian box is one of them | — | **2** | `MMM-NOTES` **p.40**, *"Colour-Coded Sessions"*: *"Two boxes can be drawn. The 1st is drawn around the Asian session and simply denotes the area of consolidation that is expected during this period… It is just a guide."* |
| NY "prime" box **window** (NY open + ~3h → 09:30–12:30) | 3 hours | **2** | `MMM-NOTES` **p.40**: the second box *"starts at the beginning of the NY open and runs for about 3 hours"*, flagged as the **New York Reversal** window. |
| TDI's four lines and their roles (structure only) | — | **2** | `MMM-NOTES` **p.45–47**, recorded at `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2a. |

### 🔧 Recovered from tooling — a new evidence class, tagged `[TOOLING]`

Owner-supplied MT4 artifacts in `~/Desktop/Trading/Indicators/`. **This is neither Tier 1 nor
Tier 2** — see the A-039 section for why that distinction is being kept rather than quietly
collapsed.

| Parameter | Value | Source |
|---|---|---|
| **EMA 50 / 200 / 800 colours** | **Aqua / White / Blue** | `3M-shadow-boxes-15M.tpl` — a **15-minute** template, `method=1` (MT4 `MODE_EMA`), colours `16776960` / `16777215` / `16711680`. The 800-on-15m independently corroborates Tier-1 V09. ⭐ **`[OWNER-ATTESTED]` too, as of 2026-08-13 (`D-042`): the owner, asked separately and without reference to this template, named the same three colours for the same three periods** — water aqua, mayonnaise white, blueberry blue. Two warrants that were never consulted against each other and agree. ⚠ the 200 is white — invisible on a white background. |
| "mktopen" open-hour **window length** | 2 × 1 hour | `!sm_WorkTime_v1.5b` `Begin_5a=10:00/End_5a=11:00`, `Begin_5b=16:00/End_5b=17:00` — independently reproduced by the 284 rectangles in `3M-shadow-boxes-15M.tpl`. **Their ET placement is NOT sourced — see below. Ships disabled.** |
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
| ~~**EMA 5 and 13 colours**~~ | ~~cyan / orange~~ | ⬆ **PROMOTED OUT OF THIS TABLE 2026-08-13 — they are `[OWNER-ATTESTED]`, no longer invented. Retained struck-through per `REMEDIATION_PROTOCOL.md` §2.** ⚠ ~~`D-042`: 5 red / 13 yellow, contested by a Tier 1 recording~~ → **FINAL: `D-043` — 5 = mustard = YELLOW, 13 = ketchup = RED**, the owner having reversed. The 5's colour is now Tier 1 corroborated. See the ✅ block immediately below. |
| **"mktopen" boxes' ET placement** | 03:00–04:00 and 09:00–10:00 | The artifacts record **broker server** time and no artifact states the offset. A GMT+3 server fits well (see below) but **that is a curve-fit by this session, not a source**. Ships **disabled**. |
| EMA source | `close` | Not specified by any source. |
| **Session timezone** | Arm A, `UTC-5` | **This is the big one — see the next section.** |
| Day mask | `1234567` | The corpus states no day mask for the intraday table. |
| **London "prime" box (whole object)** | `03:30–07:30`, **OFF by default** | **No source defines any London sub-box.** See below. |
| The name *"prime"* on the NY box | — | The source calls it the **NY Reversal** box. The *window* is Tier 2; only the *name* is invented. |
| **TDI volatility-band std-dev multiple** | 1.6185 | **Still a guess.** The MT4 indicator exposes no input for it, so it is compiled into the `.ex4` and the template cannot reveal it. Remains the Tier-3 public value. See the A-039 section. |
| Box styling, label text, right-extension | — | Cosmetic. |

### ✅ Owner-attested — FINAL as of `D-043`; `I-011` is CLOSED and the tape agrees

> ### ⚠ THE 5 AND THE 13 SWAPPED COLOURS ON 2026-08-13
> If you are working from a cached copy, a screenshot, or `D-042`'s wording: **the 5 is now
> YELLOW and the 13 is now RED**, and the **nicknames moved with the periods**. `D-042` §2's
> assignment is superseded. The superseded text is retained below the fold
> (`REMEDIATION_PROTOCOL.md` §2).

> *"I was wrong. It's the reverse. **5=mustard=yellow, 13=ketchup=red.**"*
> — project owner, 2026-08-13, `DECISIONS.md` **`D-043`**, answering `I-011`

**The final mapping, and the script's defaults:**

| Period | Nickname (`D-043`) | Colour | Warrant |
|---|---|---|---|
| **5** | **mustard** | **yellow** `#FFFF00` | `[OWNER-ATTESTED]` (`D-043`) + ✅ **`[TIER 1]` on the colour** — V07 `[00:25:34]` |
| **13** | **ketchup** | **red** `#FF0000` | `[OWNER-ATTESTED]` (`D-043`) — no corroboration |
| **50** | water | **aqua** `#00FFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` — unchanged |
| **200** | mayonnaise | **white** `#FFFFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` — unchanged |
| **800** | blueberry | **blue** `#0000FF` | `[OWNER-ATTESTED]` + `[TOOLING]` — unchanged |

**Cite them as `OWNER-ATTESTED (D-043), not observed on-screen`**, with the single exception noted
below. No captured frame in `04_SCREENSHOTS/` carries a legend, and no speaker in V01–V11 names a
colour and a **nickname** in the same sentence. **This is owner testimony about the owner's own
charts — a stronger basis than the generic placeholders it replaced, and categorically not a video
observation.** Do not let the promotion out of the DEFAULT table read as *"the course says so"*.

#### ⚠ TWO mappings reversed — and the one that looks like it reversed did NOT

The owner's sentence bundles nickname + period + colour, but the project stores **two** decisions
on **two** axes, and **both** flip:

| Axis | Stored in | Before → After | |
|---|---|---|---|
| **nickname ↔ period** | `D-041` | ketchup 5 · mustard 13 → **ketchup 13 · mustard 5** | 🔄 REVERSED |
| **period ↔ colour** | `D-042` §2 | 5 red · 13 yellow → **5 yellow · 13 red** | 🔄 REVERSED |
| **nickname ↔ colour** | the composition of the two | ketchup red · mustard yellow | ✅ **UNCHANGED** |

The two reversals are on adjacent axes and **cancel where they meet**: the condiments keep their
obvious colours and **the periods moved underneath them**. In this file that means both the colour
constant *and* the nickname change on each of the two EMA lines, while *"ketchup is red"* was never
wrong. **A reader correcting only the nickname→colour pairing would correct nothing.**

#### The conflict is resolved — and V07 now AGREES

> **V07 `[00:25:34]`** — Tier 1, frame `04_SCREENSHOTS/V07/INDEX.md` row 22:
>
> *"The only other lines in here, look, **this yellow one is a five moving average.** I made it
> dotted in the 13, 50 and the 200."*

`D-042` §3 flagged this as contradicting the owner's `5 = red`, refused to adjudicate it
(`SOURCING_HIERARCHY.md` §3.2 **Case C**) and filed `I-011`. **The owner has answered, and
reversed.** `I-011` is **CLOSED — `RESOLVED — OWNER ATTESTATION`.**

**What that agreement is and is not worth:**

1. **It is corroboration, not the warrant.** The owner's attestation closed `I-011` either way —
   had the owner confirmed red/yellow, V07 would have been annotated as a guest's private palette
   instead. **Do not write this up as the recording forcing the ruling.**
2. **One cell gains a genuine Tier 1 basis:** *"the 5 EMA is yellow"*, stated by one speaker in one
   sentence with no chaining. That is the only cell in this table with a Tier 1 colour.
3. **Nothing becomes `RESOLVED BY COURSE`.** *Mustard = 5* still requires chaining V07's
   *yellow = 5* through the owner's *mustard = yellow*, and **no speaker makes that join.** It is
   the same `D-030` two-warrant chain this README refused when it pointed the *inconvenient* way —
   and it does not become sound by now pointing the convenient way. **The discipline has to run in
   both directions or it was never discipline.** Only the **800** has a Tier 1 *period*
   (V09 `[00:41:43]`).
4. **The guest-palette explanation is no longer needed and is not thereby disproven.**
   `[00:27:24]` *"the dashed ones like this are 30 minute versions"* and `[00:27:33]` *"the blue
   heavy ones are 60 minutes"* still show the V07 speaker using his own multi-timeframe
   convention. There is simply no divergence left to explain.

**If you are matching this script against a V07 screenshot, the 5 should now look RIGHT** — that is
the check that this swap landed correctly.

<details>
<summary><b>⛔ SUPERSEDED — the <code>D-042</code> mapping and its contested-conflict block, retained per <code>REMEDIATION_PROTOCOL.md</code> §2</b></summary>

> ### ⚠ Owner-attested — and two of the five are CONTRADICTED BY TAPE (`D-042`, `I-011`)
>
> | Period | Nickname (`D-041`) | Colour | Warrant |
> |---|---|---|---|
> | **5** | ketchup | **red** `#FF0000` | `[OWNER-ATTESTED]` (`D-042`) — ⚠ **contested** |
> | **13** | mustard | **yellow** `#FFFF00` | `[OWNER-ATTESTED]` (`D-042`) — ⚠ **contested** |
> | **50** | water | **aqua** `#00FFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` |
> | **200** | mayonnaise | **white** `#FFFFFF` | `[OWNER-ATTESTED]` + `[TOOLING]` |
> | **800** | blueberry | **blue** `#0000FF` | `[OWNER-ATTESTED]` + `[TOOLING]` |
>
> **Tier 1 puts YELLOW on the 5. The owner puts RED on the 5 and YELLOW on the 13.**
>
> **And the consequence runs past colour.** The owner's mapping also gives ketchup = red and
> mustard = yellow. Chain that to V07's yellow = 5 and you get **mustard = 5, ketchup = 13** — the
> assignment `D-041` **overturned** on 2026-08-13. This is a **second, independent route back to
> the reversed nickname mapping**, and unlike the first (three Tier 3 web sources) it **starts from
> a recording**. *(This is the reasoning the owner went on to confirm — the chain was right, and it
> was still correct not to adopt it unilaterally.)*
>
> **Why this file shipped the owner's colours anyway, and refused to resolve it:** (1) no speaker
> makes the colour→nickname join, so chaining is the `D-030` error; (2) `D-041` was an explicit
> definitive owner ruling only the owner could reverse, and `REMEDIATION_PROTOCOL.md` §2 forbids
> the quiet edit in either direction; (3) a cheap innocent explanation was live — the V07 speaker
> is a **guest** describing his own multi-timeframe palette minutes later.
>
> **Filed `00_SYSTEM/SETUP_ISSUES.md` `I-011`, `OPEN`**, per `SOURCING_HIERARCHY.md` §3.2 **Case C**
> (*do not adjudicate, surface to the owner*). **One owner sentence closes it.** Until then: if you
> are matching this script against a V07 screenshot, **expect the 5 to look wrong.**
>
> **⭐ That is exactly what happened, and it is the point.** Case C — the rule that forbids a
> session from resolving a genuine conflict — is what produced the correct answer here. Had this
> file chained the inference and "fixed" the mapping itself, or suppressed the finding as a mere
> colour question, the error would have stood.

</details>

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

- The **5pm high/low reset** and the **5pm–8pm dead gap** are now drawn (added 2026-08-13). The
  two **changeover gaps** (3:00–3:30a, 9:00–9:30a), printed on the same Tier-1 V02 slide, are
  still **not** drawn — a scope decision, not a sourcing gap, and available to a future version.
- The reset is drawn as a **vertical line marking the 17:00 boundary**, not as a pair of
  high/low levels. The slide says the high/low *resets* there; it does not say the levels are
  plotted, and inventing a rendering the source does not describe would be an approximation.
  The tooling's own `!SM_Daily_HiLo` does plot such levels, which is a reasonable future
  addition once the class in the draft decision is adopted.
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

## Other finds in the owner's `~/Desktop/Trading/Indicators/`

The owner approved (2026-08-13) admitting these artifacts as a **new evidence class scoped to
parameters only** — never doctrine. The admitting decision is drafted at
[`DRAFT_D-041_platform_artifacts.md`](DRAFT_D-041_platform_artifacts.md) and is **NOT adopted**:
`DECISIONS.md` is a **policy ledger**, editable only on the integration branch (`D-038a`), so
writing it from this branch would be the exact breach that rule names. Until it is adopted the
`[TOOLING]` tag is provisional and closes no record.

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
**Its clock times are raw broker server time** (the companion binary is named
`sm_WorkTime_no_autogmt`, so GMT auto-detection is off) and no artifact states the offset.

`draw_mktopen_box=true` defines **two one-hour windows**, `10:00–11:00` and `16:00–17:00` — and
those are reproduced independently by find 3 below. Both are now in the script as the
**"mktopen" open-hour boxes, shipped disabled**; see the timezone caveat there. `A-019` is
untouched and `D-031`'s two arms are undisturbed.

**3. `3M-shadow-boxes-15M.tpl` — the richest single file in the folder.** Two payloads.

*The EMA colours* (adopted, `[TOOLING]`): a **15-minute** template with three EMAs
(`method=1` = `MODE_EMA`) at 50 = **aqua**, 200 = **white**, 800 = **blue**. An 800 EMA on a
15-minute chart independently corroborates Tier-1 V09.

> **A lead for `A-020`, deliberately NOT adopted.** The 800 being *blue* makes "blueberry" read
> as plain colour-naming — which makes **white = 200 = "mayonnaise"** a strong candidate for
> A-020's still-open half (the *period* behind "Mayo"). It is inference from colour semantics
> with no speaker behind it, which is exactly what **`D-030`** forbids adopting. No EMA in the
> script is labelled "Mayo". Logged as the best lead A-020 has had; the register decides.

> **UPDATE 2026-08-13 — the register decided, and it decided the other way round.**
> `D-042` records the owner's full colour mapping, which **agrees with this template on all three
> of its rows** (water aqua, mayonnaise white, blueberry blue) — so the lead above turns out to
> have been pointing at the right answer. **It was still correct not to adopt it**, because what
> settled it was an attestation, not the colour semantics. The same session then found the mirror
> case: V07 `[00:25:34]` puts **yellow on the 5**, which chained through the owner's
> *mustard = yellow* would reverse `D-041` — and that chain was **refused on exactly the grounds
> quoted above**, and surfaced as `00_SYSTEM/SETUP_ISSUES.md` `I-011` instead.
>
> ⭐ **UPDATE 2026-08-13 — `D-043`: the owner answered and REVERSED. The chain was pointing at the
> right answer, and refusing to walk it was still correct.** *"I was wrong. It's the reverse.
> 5=mustard=yellow, 13=ketchup=red."* `I-011` is **CLOSED**. **This is the second time in this
> file that a refused colour-semantics inference turned out to be right** — first
> *blueberry = blue*, now *yellow = 5*. **Neither is a licence to start chaining.** What settled
> both was an attestation; the inference was never the warrant, and a chain that happens to land
> correctly twice is still a chain. `D-030` is unchanged. See the ✅ `[OWNER-ATTESTED]` block
> earlier in this file.

*284 drawn rectangles* (Mar–May 2015), whose start/end times cluster hard:

```text
03:30 → 10:00   (6.5h, x50)      10:00 → 11:00   (1h, x42)
10:00 → 16:30   (6.5h, x142)     16:00 → 17:00   (1h, x42)
16:30 → 23:45   (x50)
```

The two one-hour clusters are the same numbers as `sm_WorkTime`'s `mktopen` windows — two
artifacts, different mechanisms, identical values. If the broker ran **GMT+3** (common for MT4;
the sample straddles a DST switch) the three large boxes align closely with `MMM-NOTES` p.8's GMT
table — Asian `00:30–07:00 GMT` **to the minute** — and the two small ones land on the London
open and the NY equities open. **That offset is a curve-fit by this session, not a sourced fact**,
which is precisely the `A-019` question, so it is registered as a `D-031`-style arm and the boxes
ship off.

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
