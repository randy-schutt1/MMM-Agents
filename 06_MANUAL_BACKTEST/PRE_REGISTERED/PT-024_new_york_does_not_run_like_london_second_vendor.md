# PT-024 — "They don't usually run like London" (SECOND-VENDOR RE-ISSUE of PT-023)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-023 (which re-issued PT-022). BOTH are retained, unedited.
             PT-023 IS STILL RUN AND STILL REPORTED — see §4. This file does not
             replace it; it runs alongside it on a second vendor.
ATTESTATION: AT THE MOMENT OF WRITING, NO WINDOW RANGE HAS BEEN COMPUTED FROM ANY
             SOURCE. PT-023's harvest completed minutes before this file was written
             and NOTHING has been read from it except the bar count (1,677) and the
             date range (2026-07-20 .. 2026-08-13) printed by the harvester itself.
             run_pt023.py has NOT been executed. No London range, no New York range,
             no difference, no fraction, no null distribution exists yet for any
             vendor. That is what makes this a pre-registration and not a rewrite.
SCOPE:       GUEST claim. Tested under D-032, excluded from doctrine under D-025.
```

**PT-022 governs everything not restated in PT-023 or here.** The question, the null, the
mechanical bias, the operationalisation and its weakness, both outcomes, both nulls, the seed
and the four decision rules are unchanged across all three files.

---

## 1. WHY A SECOND RE-ISSUE, AND WHY THIS IS NOT PERIOD-SHOPPING

PT-023 pre-registered **TradingView/FXCM, 15-minute**, and the whole `D-028` DEVELOPMENT block
of whatever that feed served. The harvest has now completed and the throughput, not the feed
depth, turned out to be the binding constraint:

| | Expected | Actual |
|---|---|---|
| Feed depth (measured before PT-023 was written) | back to **2026-05-31** | unchanged — the feed does reach it |
| **Harvestable** in 200 screens | most of that | **1,677 bars, 2026-07-20 → 2026-08-13 — 24 days** |

The DOM-hover harvester advances roughly 8 net bars per drag at chart default zoom. Reaching
2026-05-31 would take on the order of **900 screens and four hours**, for one symbol.

**Consequence for PT-023, stated before its numbers are read:** a 24-day span yields a
DEVELOPMENT block of ~17 days and **n ≈ 13 included weekdays**, which is below
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30. **PT-023 will therefore almost certainly
return `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`,** which is one of its four
pre-registered outcomes. **It is still run and still reported in full** (`COMMON_PROTOCOL.md`
§9 rule 6: every test performed is reported).

**Why this is not shopping for a period.** Shopping means looking at results and choosing the
window that flatters them. **No result exists.** Not one window range has been computed, on any
vendor, at the time of writing. The change is forced by a throughput measurement taken from the
harvester's own completion line, and both prior files are retained so the sequence is auditable:
PT-022 (period out of reach) → PT-023 (period reachable but not harvestable at n≥30) → PT-024
(a vendor that serves the span directly).

## 2. WHAT CHANGED FROM PT-023

| Field | PT-023 | PT-024 | Justification |
|---|---|---|---|
| **Vendor** | TradingView / FXCM | **Yahoo Finance chart API** | Serves ~60 days directly as JSON; no hover throughput limit |
| **Transport** | Data Window DOM text | **JSON numbers, UTC epoch timestamps** | A *stronger* form of `COMMON_PROTOCOL.md` §2's no-pixel rule: **nothing is rendered at all** |
| **Timeframe** | 15-minute | **30-minute** | See §2a — 30m resolves both window boundaries exactly |
| **Available span** | 24 days harvestable | **2026-05-21 → 2026-08-13, ~60 days** | Measured from the API's own response; only bar counts and dates were read |
| **Everything else** | — | **unchanged** | Question, windows, arms, outcomes, nulls, seed, decision rules |

### 2a. Why 30-minute bars are fit for purpose, and not a compromise

PT-023 specified 15-minute bars for one stated reason: *"the 3:30 and 9:30 boundaries do not
fall on hourly marks"*. **Both boundaries fall exactly on 30-minute marks**, so a 30-minute
series resolves the London window `03:30–09:00` and the New York window `09:30–17:00` with **no
boundary error at all.**

What is lost is *within-window* resolution — the range of a window is the max high and min low
of its bars, and coarser bars cannot move that. **A window's high/low is identical whether
computed from 15m or 30m bars**, because a 30m bar's high is the max of its two 15m highs. The
two timeframes give **exactly the same window ranges**, up to vendor noise.

> This is stated as a claim that can be checked, not assumed: if PT-023 and PT-024 overlap in
> calendar time, their window ranges for the overlapping days should agree to within the
> cross-vendor noise measured in `V06_HOMEWORK.md` §9.4 (sub-pip to a few pips typically). §5
> requires that comparison to be reported.

## 3. THE PERIOD RULE — UNCHANGED IN FORM FROM PT-023 §2

`T0` and `T1` from the vendor's own response after dropping null bars; `B = T0 + 0.70 × (T1 −
T0)` floored to the day; **DEVELOPMENT = `T0 → B`**; the **HOLDOUT is not opened**, not even to
count bars; `T0`, `T1`, `B` appended to `D-028` before any window statistic is computed.

**A disclosure that belongs here rather than in a footnote.** This session has previously seen
**2026-07-30 → 2026-08-13** while performing V06's homework. On a ~60-day span the `D-028`
boundary falls near **2026-07-16**, so the previously-seen fortnight lands **inside the HOLDOUT**
and outside the test window. **That is a fortunate alignment, not a designed one**, and if the
arithmetic had placed the boundary later the correct action would have been to say so and treat
the overlap as contamination. It is checked in §5 and reported either way.

## 4. PT-023 IS STILL RUN AND STILL REPORTED

Not as a formality:

1. **`COMMON_PROTOCOL.md` §9 rule 6** — every test performed is reported, including the ones
   that found nothing. A summary naming only the test that reached n≥30 would be invalid.
2. **It is a genuine second-vendor replication**, at a different timeframe, over an overlapping
   period. Two vendors agreeing on the *direction* of the effect where they overlap is
   worth more than either alone, even when one is underpowered.
3. **`SAMPLE INSUFFICIENT` is a real result**, and reporting it plainly is the discipline the
   `n < 30` rule exists to enforce.

## 5. WHAT THIS RUN MUST REPORT, WHETHER OR NOT IT IS FLATTERING

- **Both tests, PT-023 and PT-024, in one observation file**, with PT-023's `n` and its
  `SAMPLE INSUFFICIENT` label in the same sentence as any number drawn from it.
- **Both `D-031` arms**, always, for both tests.
- **Both nulls**, run **before** the rule arm's aggregate is read.
- **The overlap check of §2a** — do the two vendors agree on window ranges for the days they
  share?
- **The holdout check of §3** — did the previously-seen fortnight fall inside the HOLDOUT?
- **`O1` and `O1b` even where they disagree**, with neither preferred.
- The three costs PT-023 §3 declared — thin `n`, no DST straddle, 2026 regime — **all of which
  still apply here**, plus one new one: **~60 days is still a single volatility regime**, and
  n ≈ 30 sits exactly on the floor rather than comfortably above it.

## 6. MANDATORY SCOPE STATEMENT

PT-022 §8, verbatim, applies to this test unchanged.
