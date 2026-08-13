# PT-028 — On which weekday does the GBP/USD week make its high and its low? (RE-ISSUE of PT-010)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-010, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-010 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V01 [00:34:47]-[00:35:55], [00:52:38]; V02 [00:04:15], [00:00:03]-[00:00:26]
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
WARNING:     THIS IS THE ONE TEST IN THE RE-ISSUED SET WHOSE SAMPLE GOES MARGINAL.
             See 3b. It is stated here, at the top, because it is a finding about the
             design and must not be discovered in a review.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` · `D-026`/`D-029` · `D-027`/`D-028` · **`D-030`** · **`D-031`** ·
`D-034` → **`D-036`/`D-036a`** · **`D-035`**.

---

## 0. WHY THIS FILE EXISTS, AND WHAT THE SUBSTITUTIONS COST

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30**, **HOLDOUT = 2016-07-01 → 2017-12-29**.
`PT-010`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-010` | **PT-028** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 weeks → **180 usable trading weeks**, and **that pushes two of the six weekday cells under n = 30** — §3b–§3d |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable** with the V02–V06 homework |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | **the weekday categories change shape** — §3a |
| Everything else | — | **unchanged** — question, measures, focal prediction, nulls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). This test reports **weekdays and
   timestamps**, which are neither — they are calendar facts, and they travel intact.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. **Not excluded** (`E09`). Stated now that it is very likely to appear in
   the sensitivity appendix.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The weekly cycle is the course's founding thesis — *"same shit every week"* V01 `[00:52:38]` —
and its shape has one consequence that survives every open ambiguity: **the week turns in the
middle.**

> *"The anchor point is where the midweek reversal comes in."* V02 `[00:04:15]`
> *"sometimes could come in high on Tuesday, chop around, hit it again Wednesday"* V02
> `[00:00:03]`; *"They can come back on Thursday too and give you three tops."* `[00:00:13]`

*Anchor point* is `A-001`, *midweek reversal* is `A-012`, and both are undefined — **so this
test uses neither.** It measures the one thing that needs no definition: the weekday on which
the week's actual high and actual low print. If the cycle is real at all, weekly extremes
concentrate mid-week. If they are uniform across the week, the cycle's calendar shape has no
support on this instrument, whatever the anchor turns out to be.

This is the cheapest available check on the largest claim in the corpus, and it is **exactly the
check nobody has run**: `V04_HOMEWORK.md` measured four weeks, one per pair, and labelled itself
`DESCRIPTIVE` for that reason.

---

## 2. THE QUESTION

> Is the weekday distribution of GBP/USD weekly highs and lows non-uniform, and does it
> concentrate on Tuesday–Wednesday?

Null hypothesis: **it is uniform** — corrected for exposure (§3a). A weekly extreme is as likely
in any equal-length stretch of the trading week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute (for the timestamp of the extreme); 4-hour for cross-check |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`: 187 opens, modal 17:00 in all twelve months, no seasonal shift). **NOT FXCM's 21:00 UTC** |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2) |
| Timezone | **Both `D-031` arms** (a one-hour shift can move an extreme across a day boundary — and on this corpus it also **resizes the Sunday category**, §3a) |
| Measure 1 | Weekday of the week's high; weekday of the week's low. **Sunday is its own category and is never merged into Monday** — this corpus **does** print Sunday bars |
| Measure 2 | Hour-of-week of each extreme, in **4-hour bins** — a finer view that does not depend on the day boundary. 120-hour week → **30 bins** |
| Measure 3 | Joint distribution: (high weekday, low weekday) pairs, and the **sign of `high_day − low_day`** — the cycle's *direction of travel* through the week |
| Pre-registered focal prediction | The **mode** of both marginal distributions falls on **Tuesday or Wednesday** |
| Excluded weeks | **None.** Holiday-shortened weeks are retained and reported separately |
| Decision point | None — distributional |
| **Sample** | **180 TRADING weeks** — denominated in **trading weeks present in the corpus with an observable week open**, not calendar weeks (181 calendar-complete, less the **2014-06-01** data hole) — each contributing one high-weekday and one low-weekday. **Marginal in two cells — read §3d before quoting any rate** |

Measure 3 is the one that distinguishes a real cycle from a boundary artifact: a week that sets
its low early and its high late is a trend week, not a cycle week, and the joint distribution
separates them without anyone having to name an anchor.

### 3a. The weekday categories are NOT equal-length, and the null must not pretend they are

The trading week on this corpus runs **Sunday 17:00 → Friday 17:00 local = 120 hours**, and it
is **not** five equal days:

| Weekday | Hours in the trading week (Arm A) | Share |
|---|---|---|
| **Sunday** | **7 h** (17:00 → 24:00) | 5.8% |
| Monday | 24 h | 20.0% |
| Tuesday | 24 h | 20.0% |
| Wednesday | 24 h | 20.0% |
| Thursday | 24 h | 20.0% |
| **Friday** | **17 h** (00:00 → 17:00) | 14.2% |

**A per-weekday-uniform null (1/6 each) is wrong and would manufacture a result.** The
analytic baseline is **exposure-weighted** by the hours actually present in each week, computed
per week from timestamps (holiday weeks differ). `PT-010` already said *"uniform expectation
over the trading days actually present in each week"*; this file makes the arithmetic explicit
because the vendor's 17:00 open makes Sunday a **7-hour** category rather than the fuller
Sunday a 21:00-UTC feed would print, and a reader who assumes 1/6 will misread the table.

**Arm B changes these numbers.** Under `America/New_York` DST the week opens at local 18:00 in
summer, so **Sunday is 6 hours in DST weeks and 7 in standard-time weeks**, and Friday is
correspondingly 18/17. **The exposure weights are therefore computed per arm and per week, never
once for the batch.**

### 3b. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong, and every expected count below is denominated in the corrected number.** Against the
corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **TRADING weeks used by this test** | **180** | 181 complete weeks, less the **2014-06-01** data hole (§3c) |

**Two facts a naive reading of `C7` gets backwards:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** looks like a week open.
   `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit **inside** weeks
   that opened normally on Sunday. **A run session taking week boundaries from `C7` would split
   those four weeks in two and then report two weekly extremes where there is one.**
   Pre-registered: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open
   is never a week boundary.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** Zero bars
   for `2014-06-01 Sun` (nominal ~420), **521 of 1,440** for `2014-06-02 Mon`: **~22 continuous
   hours missing**. `C8` marks it `*** ABSENT AND UNEXPLAINED ***`.

### 3c. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME, NOT LEFT TO RUN TIME

`QA_REPORT.txt`'s gate requires an explicit disposition for every `C8`-flagged session. Eleven
sessions fall into **seven weeks** inside `W-C′`, and the disposition is **not uniform**:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE, report separately** — Wed exposure ≈ 0 h that week |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE BY NAME** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — **zero Friday exposure** |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — **zero Friday exposure** |

*(The eleventh, `2013-01-01 Tue`, lies **outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED — and why this test handles them correctly by
construction.** `PT-010` pre-registered *"Excluded weeks: **None.** Holiday-shortened weeks are
retained and reported separately"*, and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an
observation for being unrepresentative (`E09`). **Re-deciding that now, after a QA check
surfaced them, would be the suit-the-result choice the gate exists to prevent.** Crucially, this
test's null is **exposure-weighted per week** (§3a), so a week with a closed Wednesday
contributes **zero Wednesday exposure** and cannot inflate or deflate that cell — the design
already absorbs a real closure. **A real closure is market structure and belongs in the
denominator. A data hole is not, and does not.**

**Why 2014-06-01 is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation for **what the market did**. This is excluded because **the corpus does not contain
what the market did**. Including it would be worse than dropping it: the exposure weighting
would record 22 missing hours — the whole Sunday session and 15 hours of Monday — as **genuine
zero exposure**, encoding a corpus defect as a market fact and biasing the Sunday cell downward
in exactly the cell that is already thinnest. **Mechanical, by name, counted.**

### 3d. THE SAMPLE, HONESTLY — AND THE TWO CELLS THAT FALL BELOW n = 30

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **TRADING weeks used** | 260 | **180** |
| Weekly highs | 260 | **180** |
| Weekly lows | 260 | **180** |

The **marginal totals are fine**: `n = 180` per marginal distribution, six times
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor.

**The cells are not.** Under the exposure-weighted null of §3a, at **180 trading weeks**:

| Weekday | Expected highs (Arm A) | Expected lows | Verdict against the n = 30 floor |
|---|---|---|---|
| **Sunday** | **10.5** | **10.5** | ❌ **below 30 — descriptive only** |
| Monday | 36.0 | 36.0 | ✅ |
| Tuesday | 36.0 | 36.0 | ✅ |
| Wednesday | 36.0 | 36.0 | ✅ |
| Thursday | 36.0 | 36.0 | ✅ |
| **Friday** | **25.5** | **25.5** | ❌ **below 30 — descriptive only** |

**These are equal-week upper bounds.** The realised exposure-weighted expectations are
**slightly lower still** for the affected weekdays, because the six included holiday weeks carry
reduced exposure — **`2015-12-20` and `2015-12-27` contribute zero Friday hours**, and three
others contribute a shortened Wednesday or Thursday. **The Friday expectation is therefore
below 25.5, not above it. The two marginal verdicts are robust in the direction that matters.**

**Four statements that follow, all pre-registered:**

1. **Sunday was already marginal at `W-C` (expected ≈ 15.2 over 260 weeks). Friday was not
   (≈ 36.8) and now is.** The shortened window **created** one marginal cell and worsened
   another. **This is a finding about the re-issue, not a failure of it**, and it is recorded
   here rather than reported as a surprise. **Correcting calendar weeks to trading weeks moved
   the figures by less than one observation and changed no verdict** — but the inputs are now
   right, which is the point.
2. **Any rate quoted from the Sunday or Friday cell carries `SAMPLE INSUFFICIENT FOR INFERENCE
   — descriptive only` in the same sentence** (`COMMON_PROTOCOL.md` §9.4). The **focal
   prediction (Tue/Wed) is unaffected** — those cells are comfortably above the floor, which is
   fortunate and is **not** a reason to quietly drop the two thin ones.
3. **Measure 3's 6 × 6 joint table is DESCRIPTIVE ONLY at this sample.** 36 cells over 180 weeks
   averages **5.0 per cell**, and the Sunday row/column average **~1**. **No χ² statistic or
   p-value may be quoted for the joint table.** What *is* inferentially usable from Measure 3 is
   the **sign of `high_day − low_day`**, which is a single binary/ordinal summary at n = 180 —
   and that is what the headline reports. The full 36-cell table is printed as a **raw count
   matrix**, labelled descriptive.
4. **Measure 2's 30-bin hour-of-week histogram averages 6.0 highs per bin** (180 ÷ 30). Report
   **counts and the N3 shift distribution**; **no per-bin inference**, and no bin's rate quoted
   without the §4.1 label. This was already true at `W-C` (8.7 per bin) and is worse here.

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally — **this test's own unit of
> analysis**, which is how a missing session hid inside a weekday count). §3b, §3c and §3d are
> the **correction that check forced**, made **before any bar in `W-C′` was read**.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **Exposure-weighted expectation** over the hours actually present in each week (§3a), computed analytically, with a χ² and its p-value **on the six-cell marginals only** — never on the joint table — **and** the raw counts |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`. If extremes cluster mid-week under *any* week anchor, the finding is about the middle of a 5-day span, not about Tuesday |
| **Third — the natural control** | The same measurement on **randomly re-blocked 5-day spans** that do not respect the calendar week. This separates *"the calendar week is a real unit for GBP/USD"* from *"any 5-day span has a middle"* |

**The second and third arms are not decoration.** A distribution over five days will look
non-uniform by eye almost every time; the arms are what turn "looks clustered" into a statement.

Baselines are run **before** the observed distribution is read.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Modes on Tue/Wed, surviving both shift controls | Support for the weekly cycle's calendar shape. **The single most useful positive result available from V01–V02** — and still not support for any entry rule |
| Non-uniform but modes elsewhere (e.g. Friday) | A real finding that contradicts the taught shape. **If the mode is Friday or Sunday, it lands in a cell flagged §3d-marginal and must be reported with that label attached** — a marginal mode is still a finding, and hiding the label would be `E24` |
| Indistinguishable from the exposure-weighted expectation | **The weekly cycle has no calendar signature on GBP/USD at this sample.** Report prominently. This is the null the project most needs to know about early |
| Arms A and B disagree | Reported; a one-hour timezone shift moving the answer would itself be a `D-031` finding worth having — **and on this corpus it also resizes the Sunday and Friday cells** (§3a), so state which part of any disagreement is exposure arithmetic |

## 6. MANDATORY SCOPE STATEMENT

> **PT-028 measures when GBP/USD weekly extremes print.** It is **not** a test of the anchor
> point (`A-001`), the midweek reversal (`A-012`), the peak formation (`A-010`) or the M/W
> (`A-011`) — none of which is defined in V01–V06 — and it adopts **no** day count, so it takes
> no position on `C-001`. A clustering result would be *consistent with* the taught cycle; it
> would not identify an anchor on any single week, which is what a trader would actually need.
>
> It **re-issues `PT-010`** onto `W-C′` under `D-035`; `PT-010` is retained, marked and never
> run, and no result here may be reported as `PT-010`'s result.
>
> **The Sunday and Friday cells are below n = 30 and are descriptive only** (§3d). **The 6 × 6
> joint table is descriptive only and carries no χ².** The **week open is 22:00 UTC**, not
> FXCM's 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
3. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
4. Derive week boundaries from the **22:00 UTC / 17:00-local** week open, by timestamp lookup,
   never by bar count, and **never from `C7`'s open list**, which counts intra-week holiday
   re-opens as opens (§3b.1). Record the realised week roster and count, and **apply §3c's
   dispositions by name**: exclude the week of **2014-06-01**; include and report separately the
   six Dec/Jan holiday weeks.
5. **Compute the per-week, per-arm exposure weights (§3a) before any extreme is located.**
6. Compute all three measures and both arms in one pass.
7. Run the two shift controls **before** reading the observed distribution.
8. Report the five largest-range weeks as the pre-registered sensitivity appendix.
9. **Attach the §3d labels to every Sunday, Friday, joint-table and per-bin figure, in the same
   sentence as the figure.**
10. Write `BT_V01_NNNN.md` from the template, §0 referencing **this file and `PT-010`**.
11. **Neither this file nor `PT-010` is ever edited to match what was found.**
