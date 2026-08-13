# PT-025 — Do GBP/USD **weekly** extremes cluster at the six boundaries V01 names? (RE-ISSUE of PT-002's W-C arm)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-002's W-C arm ONLY. PT-002 is NON-CONFORMING under D-035 on that arm
             and is retained and marked, unedited except for its status block.
             PT-002's W-A arm (daily extremes) is UNAFFECTED and stays runnable in
             PT-002 itself. This file does not re-issue it and must not be read as
             replacing PT-002 wholesale.
LESSON:      V01 [00:30:35] and its printed slide
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
```

Shared machinery: `COMMON_PROTOCOL.md` (units, measurement rule, windows, arms, nulls, seed).
Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` instrument · `D-026`/`D-029` baseline · `D-027`/`D-028` period & holdout ·
**`D-030`** no approximated definitions · **`D-031`** timezone arms · `D-034` →
**`D-036`/`D-036a`** data source · **`D-035`** the pinned boundary and this re-issue obligation.

---

## 0. WHY THIS FILE EXISTS — THE `D-035` RE-ISSUE, AND A DEFECT IN `D-035`'s OWN TABLE

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30** and **HOLDOUT = 2016-07-01 →
2017-12-29**. `W-C` (`2013-01-06 → 2017-12-29`) **straddles that boundary by 546 days**, so
every test carrying `W-C` is non-conforming and must be re-issued under a new `PT` number onto
a window inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a; `D-027`).

`D-035` consequence 1 lists **`PT-002` among the tests that conform.** **That is wrong, and it
is the reason this file exists.** `PT-002` §3 declares:

> *"Windows | **W-A** (2015-01-04 → 2015-12-31) for daily extremes; **W-C** (2013-01-06 →
> 2017-12-29) for weekly extremes"*

— and `PRE_REGISTERED/INDEX.md` §1 has recorded `PT-002`'s window as **"W-A, W-C"** since the
batch was written. `PT-002` is a **two-window test**. Its `W-A` arm conforms; its `W-C` arm
straddles the boundary exactly as the seven named tests do. `D-035`'s conformance table
classified the file by its first window and missed the second. The correction is proposed in
`_PROPOSED_DECISION_REISSUE.md` for the owner to integrate — **no session may edit
`DECISIONS.md` to fix it by side-effect.**

### 0a. What changed, and what each substitution costs

| Field | `PT-002` (W-C arm) | **PT-025** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **180 usable** (§3b–§3d). A 31% loss of sample and the whole 2017 regime |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | price **levels** no longer comparable with the V02–V06 homework — see §0b |
| Week open | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | the week boundary moves **one hour**; every weekly extreme is measured on a different grid |
| Scope | daily **and** weekly extremes | **weekly extremes only** | the daily arm stays in `PT-002`, which is runnable |
| Everything else | — | **unchanged** — question, nulls, seed, bands, decision handling | — |

### 0b. Three losses that are not negotiable and are stated before any result

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   level offset cannot be measured for this window. **Levels here are not comparable with the
   V02–V06 FXCM homework. Only shape and distance claims travel** (`D-036a`;
   `COMMON_PROTOCOL.md` §1). Every report of this test says so.
2. **The October 2016 flash crash is in HOLDOUT and is unavailable to the Student Phase at
   all.** `COMMON_PROTOCOL.md` §3 disclosure 1 promised a sensitivity appendix covering it;
   that promise is discharged only over what remains.
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. It is **not excluded** — excluding it would be `E09`. It is stated
   **now** that it is very likely to appear in the five-largest-range-weeks appendix, so that
   its appearance there cannot later be presented as a discovery, and so that its position at
   the very edge of the window is on the record rather than found in review.

---

## 1. WHY THIS TEST IS WORTH RUNNING

V01's slide at `[00:30:35]` prints a **closed list of six** trap-move locations:

```text
Beginning Of The Week (Sun / Mon)   Beginning Of The Day
Beginning Of The Session            End Of The Session
End Of The Day                      End Of The Week
```

Every one of the six is a **clock time**. Not a pattern, not an indicator, not a definition
the course owes and has not paid. That makes this the rarest thing in the corpus: a `VISUAL` +
`EXPLICIT` instructor claim (`V01_INTERPRETATION.md` §10.1 U5) that can be tested without
approximating anything.

It is also the claim the rest of the method leans on hardest. If turning points do **not**
concentrate at session boundaries on GBP/USD, then *"timing and pattern, pattern and timing —
interchangeable"* (V02 `[00:48:41]`) has no timing half, and every session-gated rule
downstream inherits that.

> The V01 interpretation records that this session's predecessor **over-generalised** the
> spoken enumeration into "every session boundary" and the slide refuted it (`G5`, §10.1 U5).
> This test uses **the slide's six, and only the six.**

**Why the weekly arm is worth carrying separately from the daily one.** Two of the six
boundaries — *Beginning Of The Week* and *End Of The Week* — exist **only** at week scale. The
daily arm in `PT-002` cannot reach them. If this file were dropped rather than re-issued, the
two boundaries the course states most emphatically would go untested.

---

## 2. THE QUESTION

> Do **weekly** extremes on GBP/USD form disproportionately close to the six printed
> boundaries, relative to the same measurement on a randomly re-labelled clock?

Null hypothesis: **they do not.** Weekly-extreme timestamps are distributed across the trading
week no differently from what a shifted clock produces.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block** | **DEVELOPMENT, confirmed.** `D-035` sets DEVELOPMENT = 2013-01-06 → 2016-06-30. `W-C′` is that block exactly; it cannot straddle the boundary because it **is** the boundary |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 per file in `raw/SHA256SUMS.txt`. Aggregated to 15m by `06_MANUAL_BACKTEST/scripts/aggregate_m15.py`, one file per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST.** This is the HistData boundary, measured across 187 week opens (`D-036a`, QA `C7`). **It is NOT FXCM's 21:00 UTC**, and the two "Beginning/End Of The Week" boundaries below are placed from **22:00 UTC** |
| **Data-QA gate** | **Precondition on the run.** `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`; report at `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`. `C1`–`C4` must PASS (they do); `C5`–`C8` human sign-off recorded in `D-036a`. The report is cited in the observation |
| Measurement rule | `E06` as restated for a CSV corpus (`COMMON_PROTOCOL.md` §2, `D-036a`): every quote is a number parsed from a checksummed file. **Nothing is measured off a rendering of any kind** |
| Timezone | **Both `D-031` arms, always reported.** Arm A = corpus stamps **verbatim** (the corpus is natively UTC−5); Arm B = corpus stamp **+1h during US DST**, unchanged otherwise |
| The six boundaries | Week open; day open; session open; session close; day close; week close — **placed from the V02 printed table** (`COMMON_PROTOCOL.md` §4). London and New York opens/closes are the "session" boundaries; the Asian open at 8:30pm is included as a session boundary |
| Measured object | The timestamp of **each week's high and each week's low** |
| Proximity band | **±30 minutes** of a boundary, pre-registered. Reported **also** at ±15 and ±60 as a pre-registered sensitivity, all three every time |
| Decision point | None — this is a distributional measurement, not an entry test |
| Excluded weeks | **None.** Holiday-shortened weeks are retained and reported separately |
| **Sample** | **180 TRADING weeks × 2 extremes = 360 timestamps**, denominated in **trading weeks present in the corpus with an observable week open** — not calendar weeks. 181 calendar-complete weeks less the **2014-06-01** data hole, excluded by name (§3b–§3d) |

**No entry, no stop, no target.** This test measures *where in the clock* the market turns. It
does not trade.

### 3a. The arithmetic that must be reported alongside the result

Six boundaries × a ±30-minute band = **6 hours of a 24-hour day** on the widest reading,
before overlaps are removed. A clustering result is meaningless unless the *expected* share
under the null is stated in the same table as the observed share. **Report the
overlap-corrected covered fraction of the trading week explicitly.** A finding of "41% of
extremes fall in the bands" against an expected 38% is a null result, and must be written as
one.

**One correction the vendor change forces here.** The trading week on this corpus runs
**Sunday 17:00 → Friday 17:00 local = 120 hours**, not 5 × 24 = 120 hours spread evenly:
Sunday contributes **7 hours**, Monday–Thursday **24 hours** each, Friday **17 hours**. The
covered-fraction denominator is the **120-hour trading week**, and the per-boundary expected
shares are **exposure-weighted**, never per-weekday-uniform. Getting this wrong would
manufacture a Sunday clustering result out of arithmetic.

### 3b. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong, and the corpus disagrees with the calendar.** Corrected against the corpus's own census
(QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start, which precedes `W-C′`) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **Calendar-complete weeks WITH an observable Sunday open** | **180** | 181 complete weeks, less the week of **2014-06-01**, which has none |

**Two facts that a naive reading of `C7` gets backwards, and both change results:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** is indistinguishable from a week open
   in that tally. `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` all
   fall **inside** weeks that opened normally on Sunday. **A run session that derives week
   boundaries from `C7` would split those four weeks in two.** Pre-registered here:
   **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open is never a week
   boundary.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** The corpus
   holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for
   `2014-06-02 Mon`: **~22 continuous hours missing**, covering the entire week open. `C8` marks
   it `*** ABSENT AND UNEXPLAINED ***`. It is the only unexplained hole in 3.5 years.

### 3c. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME, NOT LEFT TO RUN TIME

`QA_REPORT.txt`'s gate line requires that *"any session flagged by `C8` must have an explicit,
**PRE-REGISTERED** disposition (include / exclude / report separately) in the test that spans
it."* `C8` flags **eleven sessions**, which fall into **seven weeks** inside `W-C′` — and the
disposition is **not uniform**, because the two categories are not the same kind of thing.

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0 bars) | market closure | **INCLUDE, report separately** |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** |
| **2014-06-01** | **Sun 2014-06-01 (0), Mon 2014-06-02 (521)** | **DATA DEFECT** | **EXCLUDE BY NAME** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** |

*(The eleventh flagged session, `2013-01-01 Tue`, is the corpus's opening fragment and lies
**outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED, and why that is not a choice made today.** The
originals pre-registered *"Excluded weeks: **None.** Holiday-shortened weeks are retained and
reported separately"*, and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation
for being unrepresentative (`E09`). The corpus is **correct** in those weeks: the market was
shut. **Re-deciding this now, after a QA check surfaced them, would be exactly the
suit-the-result choice the gate exists to prevent.** The disposition is inherited; what is new
is that the six weeks are **named**.

**Why the 2014-06-01 week is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation because of **what the market did**. This exclusion is because **the corpus does not
contain what the market did**. Every one of this test's six boundaries is placed from a
timestamp, and two of them — *Beginning Of The Week* and *End Of The Week* — cannot be placed
at all for that week; a weekly extreme drawn from a week missing its first 22 hours is also
simply the extreme of a shorter week. The exclusion is **mechanical, by name, and counted**.

**One consequence of including the holiday weeks that must be honoured, not averaged away.**
`2015-12-20` and `2015-12-27` **end on Thursday** — their Fridays hold zero bars. The *End Of
The Week* boundary for those two weeks is the **realised last bar**, never a nominal Friday
17:00. Placing a boundary where the corpus has no data would invent one.

### 3d. The sample, computed honestly, and where it is thin

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar Sundays | 260 | **182** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **Weeks USED (complete, with an observable open)** | 260 | **180** — 181 less the 2014-06-01 hole (§3c) |
| **Weekly-extreme timestamps** | 520 | **360** |

**`n = 180` weeks / 360 timestamps clears `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by
a wide margin**, and so does every headline band count at ±30 minutes. **Nothing in this test is
marginal at the headline level.**

**Where it is thin, said before the run rather than after:** the **per-boundary** breakdown
(§5 row 2 — the most likely real outcome) splits 360 timestamps across **six** boundaries ×
**two** `D-031` arms. A boundary that attracts 8% of extremes yields ~29 observations — **below
30, and it must carry `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` in the same
sentence as any rate quoted from it** (`COMMON_PROTOCOL.md` §9.4). This was already true at
`W-C`'s 520 timestamps for any boundary under 6%; the shortened window makes it bite sooner.
**It is reported as a property of the design, not discovered as a disappointment.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3b, §3c and §3d above are the
> **correction that check forced**, made **before any bar in `W-C′` was read**, and the
> correction is recorded rather than folded in silently.

## 4. BASELINE

| Arm | Null | Purpose |
|---|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812` | The price path is untouched; only the clock labels move. This isolates the claim exactly: does *the clock* carry the information? |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812` | The same logic at week scale, and the one that matters most here: two of the six boundaries **are** the week anchor, so a week-anchor shift is the only control that can tell "the week opens here" from "a week opens somewhere" |
| **Third** | Exposure-weighted uniform expectation, computed analytically over the 120-hour trading week (§3a) | A sanity check on N2; a large disagreement between them is a bug, not a finding |

Baselines are run **before** the rule arm's aggregate is looked at (`COMMON_PROTOCOL.md` §9.1).

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Observed share indistinguishable from N2 | **The six boundaries carry no detectable timing information for GBP/USD weekly extremes at this sample.** A foundational null — report prominently, do not bury |
| Clustering at some boundaries, not others | The most likely real outcome and the most useful. Report the per-boundary breakdown **with §3d's per-cell sample warning attached**; a method that works at London open and not at day close is a narrower method, not a broken one |
| Clustering at all six | Necessary support for every session-gated rule in V01–V04. **Not** evidence that any entry rule works |
| Arms A and B diverge | A `D-031` finding in its own right — report both, state the overlap, conclude nothing about which timezone is "right" |
| The week-open / week-close boundaries behave differently from the four intraday ones | Directly relevant to `I-010` Q1: this corpus's week opens at **22:00 UTC** and FXCM's at 21:00, and whether those are the same instant in winter is **unresolved**. Report the two week boundaries separately from the four intraday ones so a later cross-source comparison is possible |

## 6. MANDATORY SCOPE STATEMENT

> **PT-025 tests whether GBP/USD weekly extremes cluster at six printed clock boundaries.** It
> is **not** a test of the Market Maker Method's trap move, which is `A-002` and remains
> undefined as a pattern. A favourable result supports the *premise* that timing carries
> information. It says nothing about whether a trap move can be recognised at the hard right
> edge, and nothing about any entry.
>
> **It re-issues only the W-C arm of `PT-002`.** `PT-002`'s W-A daily arm is a separate,
> conforming, still-live test and no result here may be reported as `PT-002`'s result.
>
> **Price levels on this corpus are not comparable with the V02–V06 FXCM homework** (`D-036a`).
> Only shape and distance claims travel. The **week open is 22:00 UTC**, not FXCM's 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first.** `python3 06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`; confirm
   `C1`–`C4` PASS and cite `QA_REPORT.txt` in the observation. `C5`–`C8` sign-off is `D-036a`'s.
2. Build **both** `D-031` arms: `aggregate_m15.py RAW_DIR --arm A` and `--arm B`. Record each
   file's row count and span in the observation.
3. Confirm the window: `2013-01-06 → 2016-06-30`, wholly inside `D-035` DEVELOPMENT. **Do not
   read, print or count any row past 2016-06-30**; per `D-036a` the holdout is not on disk and
   must stay that way. (`I-010` Q2 — which arm's clock the boundary is stated in — is **OPEN**;
   Arm B's aggregation spills 4 bars into wall-clock 2016-07-01. **Record which convention was
   used; do not decide it here.**)
4. Derive week boundaries **by timestamp lookup from the 22:00 UTC / 17:00-local week open**,
   never by counting bars — and **never from `C7`'s open list**, which counts intra-week
   holiday re-opens as opens (§3b.1). Record the realised week roster and its count (§3d), and
   **apply §3c's dispositions by name**: exclude the week of **2014-06-01**, include and report
   separately the six Dec/Jan holiday weeks, and place the *End Of The Week* boundary for
   **2015-12-20** and **2015-12-27** at the realised last bar, not a nominal Friday 17:00.
5. Compute both arms' boundary sets **before** touching the extreme timestamps.
6. Run N2, N3 and the analytic expectation and record their distributions **before** looking at
   the observed share.
7. Report the five largest-range weeks in `W-C′` as the pre-registered sensitivity appendix
   (`COMMON_PROTOCOL.md` §3 disclosure 1) — as an appendix, never as the headline, and **never
   as a filtered re-run**. The EU referendum week is expected there (§0b.3) and is not removed.
8. Write `BT_V01_NNNN.md` from `00_SYSTEM/TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`, §0
   referencing **this file and `PT-002`**.
9. **Neither this file nor `PT-002` is ever edited to match what was found.**
