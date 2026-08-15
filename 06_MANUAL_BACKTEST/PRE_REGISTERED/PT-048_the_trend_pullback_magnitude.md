# PT-048 — V20's *"THE TREND MOVE WILL CONTAIN 20 TO 25 PIP PULLBACKS"*

**Pre-registered:** 2026-08-15, by the V20 student session.
**Status at commit time:** ⚠️ **NO BAR HAS BEEN READ. NO RUNNER EXISTS.** This file is committed
**before** `run_pt048.py` is written, per `COMMON_PROTOCOL.md` §9 rule 7. **If the runner and this
file ever disagree, THIS FILE GOVERNS**, neither is edited, and the disagreement is reported in
`BT_V20_0001.md`.

---

## §1 — THE CLAIM UNDER TEST

**Printed** on V20's `REMEMBER` slide at `39:45`, and spoken at `[00:41:43]`–`[00:41:56]`:

> *"MMs Need To Book Profit Also So **The Trend Move Will Contain 20 To 25 Pip Pullbacks** And 3
> Levels Of Move With Corresponding Levels Of Consolidation"*

**The testable core, in one sentence:**

> Inside a directional trend leg, the **pullbacks against the direction of travel** should have a
> central tendency of **20–25 pips**.

⭐ **This is chosen over V20's other candidates for a specific reason: it can be REFUTED.** It names
a narrow magnitude band, and the corpus already contains a figure pointing the other way — V19's
homework measured a **median maximum 2-hour pullback off the session high of 41–46 pips**. **If
V20's `20–25` describes the same quantity, that measurement contradicts it.** ⚠️ **It probably does
not describe the same quantity (§2a), and that is exactly what this test is for.**

### §1a — ⚠️ WHAT THIS TEST DELIBERATELY DOES **NOT** TEST

* **Not the `3 levels of move`.** *"Level"* is undefined here in the way `A-004` has always been
  undefined. **No count is scored.**
* **Not *"slow and steady"*** (`39:45`, printed). Not a measurable.
* **Not the one-third entry** (`[00:29:14]`). ***"Handle"* is undefined — `A-136`, `D-030`.**
* **Not the outside structure**, and not *"absolute sign of reversal"* (`[00:01:41]`). Identifying
  one needs a vector/aggression definition the lesson does not supply.
* **Not `L3`.** No MA periods, no separation distance, no chop duration — `A-138`.
* **It is not a strategy backtest.** No entry, exit, stop, target, size or P&L anywhere.

---

## §2 — ⚠️⚠️ THE PRE-REGISTERED WEAKNESSES, DECLARED BEFORE THE RUN

### (a) ⭐ *"PULLBACK"* IS NOT DEFINED BY THE LESSON, AND THIS IS THE LARGEST THREAT

V20 says *"the trend move will contain 20 to 25 pip pullbacks"* while pointing at charts. **The
operationalisation in §3 is a DECLARED CONVENTION OF THIS TEST.**

⚠️⚠️ **AND THE CONVENTION IS THE WHOLE BALLGAME HERE.** A *"pullback"* measured as **the maximum
adverse excursion inside a leg** will be systematically **larger** than one measured as **a
swing-to-swing retracement**, which will in turn differ from **the depth of a single bar's
counter-move**. **V19's homework measured a MAXIMUM and got 41–46 pips; a swing measure will give a
smaller number by construction.** **This test therefore reports THREE definitions, all three
pre-declared here, and refuses to pick a winner after seeing them** (§3).

### (b) *"TREND MOVE"* IS NOT DEFINED EITHER

The trend-leg identification in §3 is this test's convention. **`D-031`'s two timezone arms are both
run** and no named session is conditioned on — V20's only clock reference carries a zone
(`[00:34:05]`, *"New York time"*) but it timestamps a **reading**, not a boundary
(`V20_INTERPRETATION.md` §2.6).

### (c) THE TIMEFRAME IS `M15`, AND FOR THE FIRST TIME THAT IS ATTESTED RATHER THAN DERIVED

Three V20 charts print `GBPCHF,M15`, `GBPUSD,M15`, `USDCHF,M15`
(`04_SCREENSHOTS/V20/INDEX.md` §11). ⚠️ **V20 still never SAYS `M15`**, so the bar size remains a
reading of the instructor's charts rather than an instruction. **No robustness arm on bar size is
run and that limitation is declared.**

### (d) INSTRUMENT

GBP/USD, per `D-011`. ⚠️ **V20's own worked examples are `GBPCHF`, `GBPUSD` and `USDCHF`** — only
one of the three is the research instrument, and V20 explicitly says crosses behave differently
(V19 `[00:18:41]` gave *"as high as 50 on some of the crosses"*). **A `20–25` band derived partly
from crosses being tested on GBP/USD is a mismatch this file names in advance.**

### (e) THE FIGURE MAY BE A ROUND-NUMBER IDIOM

`15 to 25`, `20 to 25` and `25 to 50` all appear across V19 and V20. ⚠️ **These may be the same
loose idea rendered three ways rather than three measurements.** **A result landing anywhere in
`15–50` should NOT be read as confirming the specific `20–25` band**, and §5's decision rule is
written to prevent that.

---

## §3 — OPERATIONAL DEFINITIONS — FIXED NOW

Data: HistData GBP/USD M1 → M15 via `mmm_lib.load_m15()`, arms **A** and **B** (`D-031`), scope
**DEVELOPMENT only** (`D-035`; the 2016-07-01 → 2016-12-31 holdout is sealed and not on disk).
Windows (`COMMON_PROTOCOL.md` §3): **`W-A`** (2015) primary, **`W-B`** (2014-01-05 → 2015-12-31)
as a **wider-window replication** — ⚠️ **`W-B` CONTAINS `W-A`; it is not independent, and this file
says so in advance rather than being corrected later** (the wording defect `BT_V19_0001.md` §6 had
to fix in `PT-047`).

### The trend leg

Over each session day's post-box bars (`03:00 → 17:00`, 56 M15 buckets), on the day's close series:

1. A **swing pivot** is a bar whose high is the maximum (or low the minimum) of the `±3` bars
   around it.
2. A **trend leg** is a run from a swing low to a swing high (up-leg) or high to low (down-leg)
   whose net displacement is **≥ 40 pips**. *(40 is fixed now: it is twice the top of the claimed
   pullback band, so a leg must be big enough to contain one.)*
3. Legs shorter than **6 bars** are discarded.

### The three pullback measures — ALL THREE PRE-DECLARED, NONE PRIMARY-BY-HINDSIGHT

| ID | Definition |
|---|---|
| **`P1`** | ⭐ **PRIMARY — swing retracement.** For each interior counter-swing inside the leg, the distance from its local extreme back against the leg direction, in pips |
| **`P2`** | **Maximum adverse excursion** inside the leg — the deepest single counter-move from the running extreme. **Comparable to V19's homework measure** |
| **`P3`** | **Single-bar counter-move** — the largest one-bar move against the leg direction, in pips |

**`P1` is the primary and it is named as primary HERE, before any number exists**, because a
*"pullback"* in a lesson pointing at swings on a chart is most naturally a swing retracement.

### The outcome

For each measure: the **median**, the **IQR**, and the **fraction landing inside `[20, 25]` pips**,
with **a Wilson 95 % interval on that fraction and a bootstrap 95 % interval on the median.**

⚠️⚠️ **INTERVALS ARE MANDATORY AND ARE PRE-REGISTERED AS MANDATORY.** `BACKTEST_EVIDENCE_STANDARD.md`
§4.2 requires an interval on every rate and §5 makes one a condition of the `EVIDENTIAL` class.
⭐ **`REVIEW_INDEX.md` item 302 charged the V19 session `MAJOR` for omitting exactly this, and that
finding is why this sentence is in the pre-registration rather than discovered in review.**

---

## §4 — THE BASELINE (`D-026`)

**`N1` — matched random windows.** For each identified leg, draw a same-length window starting at a
random bar from the same day-hour pool with no leg condition, and compute the same three measures.
**10,000 iterations, `seed = mmm_lib.SEED`.** This holds the market and the leg-length distribution
fixed and destroys only *"this is a trend leg"*. **The claim is that trend legs have a
characteristic pullback size; the null is that any window of the same length looks the same.**

**`N3` — the fragility guard.** ⚠️ Fires, and **downgrades any positive result to `FRAGILE`**, if
**any** of:

* arms **A** and **B** disagree on whether the primary median lies in `[20, 25]`;
* `W-A` and `W-B` disagree in the same sense;
* fewer than **30 legs** are identified on any cell;
* removing the single largest `P1` value moves the primary median by more than **2 pips**.

---

## §5 — THE DECISION RULE, FIXED NOW

On **arm A, window `W-A`, measure `P1`** (the primary cell):

| Verdict | Condition |
|---|---|
| **CONFIRMED** | median `P1` lies **inside `[20, 25]`** pips **AND** its bootstrap 95 % interval also lies **entirely inside `[20, 25]`** **AND** `N3` does not fire |
| **PARTIAL** | the median lies inside `[20, 25]` but its **interval escapes the band** — the location is consistent with the claim, the precision does not establish it |
| **REFUTED** | the median lies **outside `[20, 25]`** and the interval **excludes** the band |
| **FRAGILE** | any `N3` condition fires. **Reported as a null.** |

⚠️⚠️ **NOTE WHAT `CONFIRMED` REQUIRES HERE AND WHY IT IS DELIBERATELY HARSH.** It demands the
**interval** inside the band, not just the point estimate. **This is the standard `PT-047` failed to
meet and was charged `MAJOR` for** (`REVIEW_INDEX.md` item 302). **Setting the bar at the interval
BEFORE the run is the correct response to that finding**, and it means a `PARTIAL` here is the
likely and honest outcome rather than a disappointment.

⭐ **And note what none of the verdicts mean: nothing about tradeability.** No cost, spread,
slippage or execution is modelled; `D-006` defers all of it to Phase 8.

---

## §6 — WHAT WOULD MAKE THIS TEST WRONG

1. **The `±3` swing-pivot definition is this test's convention** (§2a). A reviewer preferring ZigZag,
   fractals or a different lookback would build a different leg set. **The single largest attack.**
2. **The `≥ 40` pip leg floor is arbitrary within its motivation.** Fixed before the run so it cannot
   be tuned, but not derived from the lesson.
3. **`P1` was named primary on a reading of the word *"pullback"*, not on evidence.** If the
   instructor meant `P2`, the comparable figure is V19's 41–46 pips and this test's primary answers
   a question he did not ask.
4. **GBP/USD is one instrument and V20's examples are mostly not it** (§2d).
