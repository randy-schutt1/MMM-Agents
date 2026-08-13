# PRE-REGISTERED TESTS — INDEX

Every test in this directory was written **before** any chart in its window was opened.
That is the whole point of the directory: a prediction locked in before the outcome is
known is evidence; the same prediction written afterwards is a story.

```text
STATUS:  22 tests pre-registered · 1 run (PT-022)
GATE:    I-007 (no STANDING chart data source declared) blocks PT-001 ... PT-021.
         PT-022 declares its own source, feed and chart timezone in its observation
         and pins the D-028 boundary; I-007 stays OPEN project-wide, because a
         standing declaration is the owner's to make, not one test's.
```

---

## 1. THE BATCH

| ID | Question | Lesson | Window |
|---|---|---|---|
| **PT-001** | Does the Asian range boundary carry predictive information? (25–50 pip excursion) | V02/V04 | pinned at run time |
| **PT-002** | Do turning points cluster at the six printed trap-move boundaries? | **V01** | W-A, W-C |
| **PT-003** | Is 5pm the day boundary? The printed "High / Low Reset" | V02 | W-A |
| **PT-004** | Are the printed "Dead Gap" and the two session gaps actually quiet? | V02 | W-A |
| **PT-005** | "Take a trade at 8 o'clock and then 9:30 when the dealer hits your stops" | V02 | W-B |
| **PT-006** | The NYC Reversal — does a new session reverse the old one's direction? | V02 | W-A |
| **PT-007** | The two named vector-candle clock windows: 8:31 and 4:30 London | V02 | W-B |
| **PT-008** | "The dealer must cut" the first-eight-hours range of the week | **V03** | W-C |
| **PT-009** | Does the first move out of the week's opening range reverse? | **V01** | W-C |
| **PT-010** | On which weekday does the week make its high and its low? | **V01**/V02 | W-C |
| **PT-011** | Is the rest of the week a "unidirectional swing" after the extreme? | V02/V03 | W-C |
| **PT-012** | "They will not go below last week's peak formation" — barrier survival | V02 | W-C |
| **PT-013** | Are Sunday and Monday the week's accumulation phase? | V02 | W-C |
| **PT-014** | Is 25–50 pips actually the modal excursion beyond the box? | V02/**V04** | W-B |
| **PT-015** | Does a ceiling exist? >50 pips versus 25–50 | **V04** | W-B |
| **PT-016** | "Asian range… less than 50" as a filter | **V03** | W-B |
| **PT-017** | "In profit in 15 to 45 minutes. Guaranteed." | **V04** | W-B |
| **PT-018** | The two-hour time stop — is "not in profit yet" predictive? | V02 | W-B |
| **PT-019** | The weekend gap, and the one mechanical rationale in V01 | **V01** | W-C |
| **PT-020** | The London-open asymmetric conditional | **V03** | W-B |
| **PT-021** | DNC and the straightaway test | V02 | W-B |
| **PT-022** | *"They don't usually run like London"* — is the New York window's realised range smaller? | **V06 — GUEST** | W-A |

Shared machinery — units, the no-pixel measurement rule, the three windows, the two
`D-031` timezone arms, the four null models, the fixed seed, and the `D-030` exclusion
list — is in **`COMMON_PROTOCOL.md`**. Each file still carries its own pre-registration.

## 2. COVERAGE

| Lesson | Tests | Note |
|---|---|---|
| **V01** | PT-002, 009, 010, 019 (+ PT-013 partly) | The framing lesson finally gets tested: the six trap boundaries, the first-move prohibition, the weekly cycle's calendar shape, the Friday-flat rationale |
| **V02** | PT-003, 004, 005, 006, 007, 011, 012, 013, 018, 021, 014 | The densest lesson and the densest coverage. Six of these come from the **printed session table and slides**, which no prior work has touched |
| **V03** | PT-008, 016, 020 (+ PT-009, 011) | The first-8-hours block, the box-size filter, the one crisp conditional |
| **V04** | PT-014, 015, 017 (+ PT-001) | The prescriptive lesson: the excursion band, its missing ceiling, and `CL1` |
| **V05** | **none** | `D-025` — zero course-author runtime |
| **V06** | **PT-022** | See the note below. `D-025` still excludes every normative statement in V06 from the methodology; `D-032` permits one measurable claim to be **tested** |

> **CHANGED 2026-08-13, and the superseded reading is retained above the change rather than
> corrected away.** This table previously read **"V06 — none — `D-025` — zero course-author
> runtime, and the most complete system in the corpus is entirely inadmissible."** That was
> correct as a statement about **adoption** and it remains correct: nothing in V06 has entered
> or may enter the methodology.
>
> What changed is scope, by owner direction recorded as **`D-032`**: *guest material may be
> tested, never adopted; a test is not a citation.* `PT-022` measures one arithmetic claim —
> whether the New York session window's realised range is smaller than London's — chosen because
> it is the **only** claim in V06 that survives `D-030`. Every other claim in that lesson needs
> *push*, *pullback*, *nameable pattern* or a moving-average type, none of which the course has
> defined, and all of them stay untestable.
>
> **`COMMON_PROTOCOL.md` §8 is narrowed by the same entry, to the normative half only, and
> `PT-002`…`PT-021` are unaffected** — none of them draws on V05 or V06.

By kind: **7 clock/session-structure**, **6 weekly-structure**, **5 Asian-range/location**,
**2 management**, **1 mechanical (gap)**. No two tests ask the same question, and the four
that share the Asian-range box (PT-014/015/016/017/018/020/021) each condition it
differently — size, ceiling, timing, management, session, prior breach.

## 3. RUN ORDER

Dependencies are real and are stated so that a later test cannot be tuned by an earlier
one's result.

```text
PT-014  ─┬─►  PT-001, PT-015, PT-016, PT-017  ─►  PT-018
         └─►  PT-021, PT-020
PT-008  ──►  PT-009
PT-003  ──►  PT-004        (both build the 24-hour / 96-slot profile)
independent:  PT-002, PT-005, PT-006, PT-007, PT-010, PT-011, PT-012, PT-013, PT-019
```

`PT-014` runs first in its family because it reports the excursion distribution the others
select inside; discovering after the fact that a band selects a tail is how a thin sample
gets explained away instead of reported.

## 4. WHAT IS DELIBERATELY NOT TESTED

`COMMON_PROTOCOL.md` §7 carries the full list with its blocking record. In short: the M/W
(`A-011`), the second leg (`A-007`), TDI and everything TDI-shaped (`A-039`, `A-031`,
`A-032`), "the level" (`A-004`), the anchor point (`A-001`), outside structure (`A-033`),
"Mayo" and the moving averages (`A-020`), ADR × 3 (no defined cycle, no stated lookback),
the halved Asian range (`A-037`), the 22/33 trades (`A-023`, `A-024`), half-Batman
(`A-022`), and any specific day count (`C-001` — PT-012 measures the distribution and
adopts no value).

Two things are worth stating positively rather than as absences:

- **V04's CL7** — *"the high of the week and the high of the day form at the same time"*
  `[00:19:47]` — was considered and **rejected as untestable-as-stated**: the week's high
  necessarily *is* the high of the day it occurs on, so the claim is true by construction.
  The non-trivial reading requires the railroad-track / M identification, which is `A-011`.
  Recorded here so a later session does not read the gap as an oversight.
- **The retracted 89.1%/81.9% backtest figure** (V02 `[00:37:37]`, *"don't quote me on the
  amount"*) is not a target anywhere in this batch. `PT-001` and `PT-015` test the
  *condition* that anecdote describes; the *number* is not a benchmark, per `D-009`.

## 5. WHAT THE RUN SESSION MUST NOT DO

1. **Do not edit a `PT-NNN` file to match what was found.** A changed window is a new test
   ID (`D-027`); the abandoned one is retained and marked.
2. **Do not run any of these before `I-007` closes** and the `D-028` boundary dates are
   pinned and checked against every window (`COMMON_PROTOCOL.md` §3a).
3. **Do not read a price from a pixel** (`COMMON_PROTOCOL.md` §2).
4. **Do not report one `D-031` arm.** Both, every time.
5. **Do not report only the tests that found something.** All 21, including the nulls —
   `BACKTEST_EVIDENCE_STANDARD.md` §4.3, `E25`.
6. **Do not grade a test by whether it flatters the course.** `A null result honestly
   obtained is worth more to this project than a favourable one that cannot be read.`
