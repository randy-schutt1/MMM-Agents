# PRE-REGISTERED TESTS — INDEX

Every test in this directory was written **before** any chart in its window was opened.
That is the whole point of the directory: a prediction locked in before the outcome is
known is evidence; the same prediction written afterwards is a story.

```text
STATUS:  33 test FILES pre-registered · 2 run (PT-023, PT-024)
         PT-001 ... PT-032 are accounted for below. PT-033 was written by a CONCURRENT
         SESSION (I-009) and is listed, not summarised — its owning session states its
         own window, nulls and coverage.
         PT-022 SUPERSEDED — PERIOD UNOBTAINABLE (feed depth), retained unedited
         PT-023 RUN AND REPORTED, expected n<30 — re-issued on a second vendor as PT-024
         All three carry the same question, nulls, seed and decision rules
         PT-025 ... PT-032 ADDED 2026-08-13 — the D-035 re-issues, see section 1a
         PT-008/009/010/011/012/013/019 RETIRED UNRUN — non-conforming under D-035
         PT-002 PARTIALLY retired — its W-C arm only; its W-A arm stays runnable
GATE:    UPDATED 2026-08-13 (later, same day). ALL THREE PRIOR BLOCKERS ARE DISCHARGED
         FOR THE HISTORICAL WINDOWS:
           1. I-007 — CLOSED (D-034: TradingView, FXCM feed).
           2. D-028 boundary — PINNED at 2016-07-01 (D-035): DEVELOPMENT
              2013-01-06 -> 2016-06-30, HOLDOUT 2016-07-01 -> 2017-12-29.
           3. DATA AVAILABILITY — CLEARED (D-036a). D-036 showed the TradingView
              bar-allowance exits close ~6% of the gap; the owner took the import path.
              W-A / W-B / W-C' are served in full by the HistData GBP/USD M1 CSV corpus
              (1,297,781 bars, 2013-01-01 -> 2016-06-30, QA C1-C4 PASS).
              THE WEEK OPEN IS 22:00 UTC ON THAT CORPUS, NOT FXCM'S 21:00 UTC.
              PRICE LEVELS ARE NOT COMPARABLE WITH THE V02-V06 FXCM HOMEWORK.
           4. THE W-C STRADDLE — DISCHARGED 2026-08-13 by the re-issue in section 1a.
              EIGHT tests were non-conforming, not the seven D-035 named: its
              conformance table missed PT-002's SECOND window. The correction and the
              proposed decision text are in _PROPOSED_DECISION_REISSUE.md, awaiting
              owner integration into DECISIONS.md.
         RUNNABLE NOW: PT-002 (W-A arm only), PT-003 ... PT-007, PT-014 ... PT-018,
                       PT-020, PT-021, PT-025 ... PT-032.
         MUST NEVER RUN: PT-008, PT-009, PT-010, PT-011, PT-012, PT-013, PT-019, and
                       PT-002's W-C arm. Read their status blocks first.
         PT-001 still pins its period at run time.
         The prior gate line, retained: "I-007 (no STANDING chart data source declared)
         blocks PT-001 ... PT-021. PT-022 declares its own source, feed and chart
         timezone in its observation and pins the D-028 boundary; I-007 stays OPEN
         project-wide, because a standing declaration is the owner's to make."
```

---

## 1. THE BATCH

| ID | Question | Lesson | Window |
|---|---|---|---|
| **PT-001** | Does the Asian range boundary carry predictive information? (25–50 pip excursion) | V02/V04 | pinned at run time |
| **PT-002** | Do turning points cluster at the six printed trap-move boundaries? | **V01** | **W-A only** — its **W-C** arm is non-conforming and is re-issued as **PT-025** |
| **PT-003** | Is 5pm the day boundary? The printed "High / Low Reset" | V02 | W-A |
| **PT-004** | Are the printed "Dead Gap" and the two session gaps actually quiet? | V02 | W-A |
| **PT-005** | "Take a trade at 8 o'clock and then 9:30 when the dealer hits your stops" | V02 | W-B |
| **PT-006** | The NYC Reversal — does a new session reverse the old one's direction? | V02 | W-A |
| **PT-007** | The two named vector-candle clock windows: 8:31 and 4:30 London | V02 | W-B |
| ~~**PT-008**~~ | "The dealer must cut" the first-eight-hours range of the week | **V03** | ~~W-C~~ — **RETIRED UNRUN, → PT-026** |
| ~~**PT-009**~~ | Does the first move out of the week's opening range reverse? | **V01** | ~~W-C~~ — **RETIRED UNRUN, → PT-027** |
| ~~**PT-010**~~ | On which weekday does the week make its high and its low? | **V01**/V02 | ~~W-C~~ — **RETIRED UNRUN, → PT-028** |
| ~~**PT-011**~~ | Is the rest of the week a "unidirectional swing" after the extreme? | V02/V03 | ~~W-C~~ — **RETIRED UNRUN, → PT-029** |
| ~~**PT-012**~~ | "They will not go below last week's peak formation" — barrier survival | V02 | ~~W-C~~ — **RETIRED UNRUN, → PT-030** |
| ~~**PT-013**~~ | Are Sunday and Monday the week's accumulation phase? | V02 | ~~W-C~~ — **RETIRED UNRUN, → PT-031** |
| **PT-014** | Is 25–50 pips actually the modal excursion beyond the box? | V02/**V04** | W-B |
| **PT-015** | Does a ceiling exist? >50 pips versus 25–50 | **V04** | W-B |
| **PT-016** | "Asian range… less than 50" as a filter | **V03** | W-B |
| **PT-017** | "In profit in 15 to 45 minutes. Guaranteed." | **V04** | W-B |
| **PT-018** | The two-hour time stop — is "not in profit yet" predictive? | V02 | W-B |
| ~~**PT-019**~~ | The weekend gap, and the one mechanical rationale in V01 | **V01** | ~~W-C~~ — **RETIRED UNRUN, → PT-032** |
| **PT-020** | The London-open asymmetric conditional | **V03** | W-B |
| **PT-021** | DNC and the straightaway test | V02 | W-B |
| **PT-022** | *"They don't usually run like London"* — is the New York window's realised range smaller? | **V06 — GUEST** | W-A — **SUPERSEDED, period unobtainable** |
| **PT-023** | The same question, re-issued on the period the feed actually serves | **V06 — GUEST** | FXCM 15m, ~24 days harvestable — **run, n<30 expected** |
| **PT-024** | The same question again, on a second vendor that serves ~60 days | **V06 — GUEST** | Yahoo 30m, `D-028` DEVELOPMENT block |
| **PT-025** | *(re-issue of PT-002's W-C arm)* Do **weekly** extremes cluster at the six printed boundaries? | **V01** | **W-C′** |
| **PT-026** | *(re-issue of PT-008)* "The dealer must cut" the first-eight-hours range of the week | **V03** | **W-C′** |
| **PT-027** | *(re-issue of PT-009)* Does the first move out of the week's opening range reverse? | **V01** | **W-C′** |
| **PT-028** | *(re-issue of PT-010)* On which weekday does the week make its high and its low? | **V01**/V02 | **W-C′** |
| **PT-029** | *(re-issue of PT-011)* Is the rest of the week a "unidirectional swing" after the extreme? | V02/V03 | **W-C′** |
| **PT-030** | *(re-issue of PT-012)* "They will not go below last week's peak formation" — barrier survival | V02 | **W-C′** |
| **PT-031** | *(re-issue of PT-013)* Are Sunday and Monday the week's accumulation phase? | V02 | **W-C′** |
| **PT-032** | *(re-issue of PT-019)* The weekend gap, and the one mechanical rationale in V01 | **V01** | **W-C′** |
| **PT-033** | *"Hi-Lo"* — the ceiling of an entry at the day's extreme, and the size of the untaught gap | *see the file* | *see the file* |

> **`PT-033` was authored by a DIFFERENT SESSION, concurrently with the `D-035` re-issue batch**
> (`SETUP_ISSUES.md` `I-009` — two sessions share this working tree). Its row above records only
> its title; **its owning session states its own lesson, window, nulls and coverage**, and this
> index defers to that file. `PT-033` §0 records the numbering handshake from its side: it took
> `PT-033` after re-listing the directory, and it renames if a collision is ever found.
>
> One cross-session discrepancy, recorded rather than silently reconciled: **`PT-033` §0
> describes the re-issue batch as covering *"the seven `W-C` tests"*. It is EIGHT** — `D-035`'s
> conformance table missed `PT-002`'s second window (§1a). The correction belongs in
> `DECISIONS.md` via `_PROPOSED_DECISION_REISSUE.md`, and **no session may edit another
> session's `PT` file to align the wording.**

Shared machinery — units, the no-pixel measurement rule, the three windows, the two
`D-031` timezone arms, the four null models, the fixed seed, and the `D-030` exclusion
list — is in **`COMMON_PROTOCOL.md`**. Each file still carries its own pre-registration.

## 1a. THE `D-035` RE-ISSUE — EIGHT TESTS, NOT SEVEN

`D-035` pinned the project-wide `D-028` split at **2016-07-01** (DEVELOPMENT
`2013-01-06 → 2016-06-30`; HOLDOUT `2016-07-01 → 2017-12-29`) and recorded — without
discharging — that every test carrying **`W-C`** (`2013-01-06 → 2017-12-29`) **straddles that
boundary by 546 days** and must be **re-issued under a new `PT` number** onto a conforming
window, with the original **retained and marked, never edited** (`D-027`;
`COMMON_PROTOCOL.md` §3a). Executed here on **2026-08-13**, onto
**`W-C′` = `2013-01-06 → 2016-06-30`**.

| Original | Re-issued as | Honest `n` on `W-C′` | Was it in `D-035`'s list? |
|---|---|---|---|
| **`PT-002`** — **W-C arm only** | **`PT-025`** | **180** weeks × 2 extremes = **360** | ❌ **No — `D-035` listed `PT-002` as CONFORMING. It is not.** See below |
| `PT-008` | **`PT-026`** | **180** weeks | ✅ |
| `PT-009` | **`PT-027`** | **≤ 180** weeks (one trigger per week at most) | ✅ |
| `PT-010` | **`PT-028`** | **180** weeks — ⚠️ **two weekday cells below n = 30** | ✅ |
| `PT-011` | **`PT-029`** | **180** weeks | ✅ |
| `PT-012` | **`PT-030`** | **180** weeks × 2 barriers = **360** | ✅ |
| `PT-013` | **`PT-031`** | **180** / **180** / **179** by day-set arm | ✅ |
| `PT-019` | **`PT-032`** | **180** weekend gaps | ✅ |

> **`D-035`'s conformance table is defective in one row, and this is where it is recorded.**
> Consequence 1 of `D-035` lists **`PT-002`** among the tests that conform. **It does not.**
> `PT-002` §3 pre-registers **two** windows — *"**W-A** … for daily extremes; **W-C** … for
> weekly extremes"* — and **this index has recorded it as "W-A, W-C" since 2026-08-12.** Its
> `W-C` arm straddles the boundary by the same 546 days as the other seven; `D-035` filed the
> test by its **first** window.
>
> **`PT-002` is marked PARTIALLY non-conforming, not superseded.** Its `W-A` daily arm conforms,
> is unblocked by `D-036a`, and **stays runnable in `PT-002` itself**. Only its weekly arm moves
> to `PT-025`.
>
> **No session may edit `DECISIONS.md` to correct this by side-effect.** The proposed correction
> (an append to `D-035`) and the proposed new entry recording the executed re-issue are written
> out in **`_PROPOSED_DECISION_REISSUE.md`**, awaiting owner integration.

**What every re-issue carries that its original could not:**

| | Original (`W-C`) | Re-issue (`W-C′`) |
|---|---|---|
| Window | 2013-01-06 → **2017-12-29** — straddles | **2013-01-06 → 2016-06-30** — **is** the DEVELOPMENT block |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`), SHA-256 on record, aggregated by `scripts/aggregate_m15.py` |
| **Week open** | **21:00 UTC** (FXCM) | **22:00 UTC** — Sunday 17:00, **fixed UTC−5, no DST** |
| QA | — | **`scripts/qa_histdata_m1.py` → `QA_REPORT.txt` is a PRECONDITION**, cited in every run |
| `D-031` arms | both, harvested twice by hand | **both, one flag** — Arm A = corpus stamps verbatim, Arm B = +1h during US DST |
| Levels | comparable with V02–V06 homework | **NOT comparable.** Only shape and distance claims travel |
| 2016 events | referendum **and** flash crash in window | referendum (2016-06-23) **in DEVELOPMENT and retained**; flash crash (2016-10-07) **in HOLDOUT, unavailable** |
| Sample | *"~260 weeks"* | **180 TRADING weeks** — 182 calendar Sundays, but only **181 observable Sunday week opens**, less the **2014-06-01** data hole. Counts are denominated in **trading weeks present in the corpus**, never calendar weeks |
| Data-completeness | assumed | **QA `C8` session-completeness census**, added **after** these files were drafted |

### 1b. CALENDAR WEEKS ARE NOT TRADING WEEKS — THE CENSUS EVERY RE-ISSUE IS DENOMINATED IN

The first drafts of `PT-025`…`PT-032` counted **calendar Sundays** and called them week opens.
**The corpus disagrees with the calendar**, and every `n` above is the corrected figure:

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | QA `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | QA `C7` |
| — opening on another weekday | **5** | QA `C7` |
| **TRADING weeks the re-issues use** | **180** | 181 complete weeks, less the **2014-06-01** data hole |

**Two traps, both pre-registered against in every affected file:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** is indistinguishable from a week open
   in that tally. `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit
   **inside** weeks that opened normally on Sunday. **Taking week boundaries from `C7` would
   split those four weeks in two.** Every re-issue states: **a week is delimited by its Sunday
   17:00 open; an intra-week holiday re-open is never a week boundary.**
2. **`2014-06-02 Mon 15:01` IS a week start, and it is a DATA DEFECT.** The corpus holds **zero
   bars** for `2014-06-01 Sun` and **521 of 1,440** for `2014-06-02 Mon` — **~22 continuous hours
   missing, covering the entire week open.** It is **the only unexplained hole in 3.5 years**.
   **Excluded by name from all eight re-issues, counted in every reported `n`.**

**`C8` — the check that found it — was added to `qa_histdata_m1.py` AFTER these files were
drafted.** `C6` had excluded the hole **by construction** (its gap census skips anything ≥ 12 h
as "the weekend", and a missing session is indistinguishable from a weekend by duration alone)
and `C7` had rendered it cosmetic (a decorative **Monday** entry in a weekday tally). Every
re-issue records the correction rather than folding it in silently.

**`C8` dispositions are pre-registered per test and are NOT uniform** — `QA_REPORT.txt`'s gate
requires an explicit disposition for each flagged session. Eleven flagged sessions fall into
**seven weeks** inside `W-C′`: **six Dec/Jan market closures → INCLUDE, report separately** (the
disposition the originals already carried; re-deciding it now would be the suit-the-result
choice the gate exists to prevent), and **one data hole → EXCLUDE by name**. `PT-030` excludes
**two** weeks, because the week of **2014-06-08** inherits the defect through its barrier.
`PT-032` excludes the **2014-05-30 → 2014-06-02 "weekend gap"** specifically, because measuring
it would **fabricate a ~22-hour gap out of missing data** on the one test whose headline is gap
size.

**The honest sample findings:** `W-C′` is 1,272 days and yields **180 trading weeks** against
`W-C`'s **260** — a **31% loss**. Every headline `n` still clears
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by a wide margin. **`PT-028` is the exception
and it is flagged in its own status block**: the trading week is **120 hours and not five equal
days** (Sunday **7 h**, Mon–Thu **24 h**, Friday **17 h**), so under the exposure-weighted null
the expected **Sunday (≈ 10.5)** and **Friday (≈ 25.5)** cells fall **below 30** and are
descriptive only — Sunday was already marginal at `W-C` (≈ 15.2), **Friday was not (≈ 36.8)** —
and its 6 × 6 joint weekday table averages **5.0 per cell** and carries **no χ²**. Those two
figures are **equal-week upper bounds**: two included holiday weeks carry **zero Friday
exposure**, so the realised Friday expectation is lower still, and **the marginal verdicts are
robust in the direction that matters**. Subset cells in `PT-027`, `PT-030`, `PT-031` and
`PT-032` have run-time-unknown counts and each file **pre-registers the `n < 30` label** rather
than negotiating it after the number is seen.

## 2. COVERAGE

| Lesson | Tests | Note |
|---|---|---|
| **V01** | PT-002 (W-A arm), **PT-025**, **PT-027**, **PT-028**, **PT-032** (+ PT-031 partly) | The framing lesson finally gets tested: the six trap boundaries, the first-move prohibition, the weekly cycle's calendar shape, the Friday-flat rationale. ~~PT-009, 010, 019~~ and PT-002's W-C arm were **retired unrun** under `D-035` and re-issued — §1a |
| **V02** | PT-003, 004, 005, 006, 007, 018, 021, 014, **PT-029**, **PT-030**, **PT-031** | The densest lesson and the densest coverage. Six of these come from the **printed session table and slides**, which no prior work has touched. ~~PT-011, 012, 013~~ **retired unrun** and re-issued — §1a |
| **V03** | **PT-026**, 016, 020 (+ **PT-027**, **PT-029**) | The first-8-hours block, the box-size filter, the one crisp conditional. ~~PT-008~~ **retired unrun** and re-issued — §1a |
| **V04** | PT-014, 015, 017 (+ PT-001) | The prescriptive lesson: the excursion band, its missing ceiling, and `CL1` |
| **V05** | **none** ⚠️ **and this is now a GAP, not a ruling** | ~~`D-025` — zero course-author runtime~~ → **`D-033`, 2026-08-13: guest material is normative on equal footing.** V05 is a methods-of-study lesson, so it may yield few testable claims regardless — but the *exclusion* is gone and the lesson must be re-read for testable content. **Owed, not done here** |
| **V06** | **PT-022** (superseded) → **PT-023** + **PT-024** (both run, both reported) ⚠️ **more are now owed** | ~~`D-025` excludes every normative statement; `D-032` permits one claim to be tested~~ → **`D-033`**: the exclusion is reversed and `D-032`'s fence is superseded. V06's stated system — trigger, filter, location rule, counting rule, stop, target, time stop, exit — **is now admissible doctrine and testable as such.** **But `D-030` is untouched**, and it independently blocks every part that needs *push*, *pullback*, *nameable pattern* or a moving-average type. Which V06 claims survive `D-030` on a fresh reading is **follow-up work** |

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

> **CHANGED AGAIN 2026-08-13 (later, same day) — `D-033`, and the note above is now history
> too.** Owner direction: *"all knowledge is created equal."* `D-025`'s normative exclusion is
> **superseded**, and `D-032`'s narrower test-but-never-adopt fence is superseded with it.
> Guest-presented material — V05, V06, V04 Segment B — is **normative evidence on equal footing
> with the course author**: it may define rules and thresholds, enter the master and machine
> specs and the concept library, close `A-xxx`/`C-xxx` records, and be cited for or against any
> other statement.
>
> **Three things this does not do**, because each is the way a future session will misread it:
>
> 1. **`D-030` is untouched.** *push*, *pullback*, *nameable pattern*, M/W anatomy, "the level",
>    the second leg, TDI, ADR's lookback — all still undefined by the course, all still
>    untestable, **whoever said them**. `COMMON_PROTOCOL.md` §7's exclusion list is unchanged.
> 2. **`PT-022`/`PT-023`/`PT-024` and `BT_V06_0001` are not withdrawn or re-scoped.** Work done
>    under a narrower fence is valid under a wider one; their `D-032` scope statements are now
>    historical annotations rather than live constraints.
> 3. **`PT-002`…`PT-021` are still unaffected** — none draws on V05 or V06, no window moves, no
>    pre-registration is edited. What changes is that V05/V06-derived tests are now **owed**,
>    under new `PT` numbers, by a later session.

By kind: **7 clock/session-structure**, **6 weekly-structure**, **5 Asian-range/location**,
**2 management**, **1 mechanical (gap)**. No two tests ask the same question, and the four
that share the Asian-range box (PT-014/015/016/017/018/020/021) each condition it
differently — size, ceiling, timing, management, session, prior breach.

> **These counts are of QUESTIONS, not of files, and the `D-035` re-issue did not change them.**
> `PT-025` … `PT-032` carry the same eight questions under new numbers on a conforming window
> (§1a); the retired originals are not counted twice.

## 3. RUN ORDER

Dependencies are real and are stated so that a later test cannot be tuned by an earlier
one's result.

```text
PT-014  ─┬─►  PT-001, PT-015, PT-016, PT-017  ─►  PT-018
         └─►  PT-021, PT-020
PT-026  ──►  PT-027        (was PT-008 ──► PT-009; both are retired unrun)
PT-003  ──►  PT-004        (both build the 24-hour / 96-slot profile)
independent:  PT-002 (W-A arm), PT-005, PT-006, PT-007,
              PT-025, PT-028, PT-029, PT-030, PT-031, PT-032
```

**`PT-027` consumes `PT-026`'s block definition and must not be run before it** — running them
in the other order would mean tuning the block against `PT-027`'s outcome. **`PT-008` is retired
unrun and must not be run to supply that block**, which is why the dependency edge moved rather
than being inherited.

`PT-014` runs first in its family because it reports the excursion distribution the others
select inside; discovering after the fact that a band selects a tail is how a thin sample
gets explained away instead of reported.

## 4. WHAT IS DELIBERATELY NOT TESTED

`COMMON_PROTOCOL.md` §7 carries the full list with its blocking record. In short: the M/W
(`A-011`), the second leg (`A-007`), TDI and everything TDI-shaped (`A-039`, `A-031`,
`A-032`), "the level" (`A-004`), the anchor point (`A-001`), outside structure (`A-033`),
"Mayo" and the moving averages (`A-020`), ADR × 3 (no defined cycle, no stated lookback),
the halved Asian range (`A-037`), the 22/33 trades (`A-023`, `A-024`), half-Batman
(`A-022`), and any specific day count (`C-001` — ~~PT-012~~ **PT-030** measures the distribution
and adopts no value).

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
2. ~~**Do not run any of these before `I-007` closes** and the `D-028` boundary dates are
   pinned and checked against every window (`COMMON_PROTOCOL.md` §3a).~~ **Both conditions are
   now met — `D-034` and `D-035` — and the check was run: W-A and W-B conform, W-C does not.**
   ~~The rule that replaces this one: **do not run any of these until the data-availability
   blocker is resolved** (`D-035` options A / B / C), and **do not run a W-C test at all** until
   it has been re-issued under a new `PT` number with a window inside DEVELOPMENT.~~ **Both
   replacement conditions are now met too — `D-036a` cleared data availability, and §1a
   discharged the re-issue.** The rule that replaces *them*: **do not run `PT-002`'s W-C arm,
   and do not run `PT-008`, `PT-009`, `PT-010`, `PT-011`, `PT-012`, `PT-013` or `PT-019` at all
   — ever.** They are retired unrun. Run `PT-025` … `PT-032` instead, and **read each one's §0
   before starting**, because the vendor change moved the week open to **22:00 UTC** and made
   price levels non-comparable with the V02–V06 homework.
2a. **Run the data-QA gate before any test on the HistData corpus.**
   `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`; `C1`–`C4` must PASS; cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt` in the observation (`D-036a`).
   **`C5`–`C8` need human sign-off, and `C8` is binding**: every flagged session must have an
   explicit **pre-registered** disposition in the test that spans it (§1b). **Do not derive week
   boundaries from `C7`'s open list** — it counts intra-week holiday re-opens as week opens.
2b. **Do not read, print or count a single row past 2016-06-30.** The `D-035` holdout is not on
   disk and must stay that way; any session extending the corpus repeats the truncation
   discipline or records the breach (`D-036a`). Opening it is `E23`.
3. **Do not read a price from a pixel** (`COMMON_PROTOCOL.md` §2) — and on the CSV corpus,
   **nothing is measured off a rendering of any kind**; every quote is a number parsed from a
   checksummed file (`D-036a`'s `E06` restatement).
4. **Do not report one `D-031` arm.** Both, every time.
5. **Do not report only the tests that found something.** ~~All 21~~ **All 21 questions of the
   original batch — carried now by 14 still-live originals (`PT-001`–`PT-007`, `PT-014`–`PT-018`,
   `PT-020`, `PT-021`) plus the 8 re-issues (`PT-025`–`PT-032`); that is 22 files for 21
   questions, because `PT-002` and `PT-025` split one question across two windows** — including
   the nulls (`BACKTEST_EVIDENCE_STANDARD.md` §4.3, `E25`).
5a. **Do not round a sample up, and do not count calendar weeks.** `W-C′` gives **180 trading
   weeks** (§1b), not "~260", not "182", not
   "about 180". Where a stratum or subset falls below 30, the label
   `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` goes in the **same sentence** as the
   figure — see `PT-028` in particular, whose Sunday and Friday cells are below the floor.
6. **Do not grade a test by whether it flatters the course.** `A null result honestly
   obtained is worth more to this project than a favourable one that cannot be read.`
