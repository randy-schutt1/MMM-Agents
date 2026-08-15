# Cross-check of the derived M15 / H1 bars — narrative and verdict

> **Run:** 2026-08-13 · **Script:** `../../scripts/crosscheck_htf.py` ·
> **Raw output:** `CROSSCHECK_REPORT.txt` (this file summarises it; that file is the evidence)
> **Verdict:** `PASS` on all seven checks — **and read §0 before reading that as reassurance.**

---

## §0 — WHAT WAS ASKED FOR, WHAT WAS RUN, AND THE DIFFERENCE

**Asked for:** the derived M15/H1 bars compared against **HistData.com's native M15 and H1
files**, over at least a full month of overlap.

**Ran instead:** seven internal-consistency checks.

**Why:** HistData publishes **no M15 and no H1**, in any format, on any platform. Its FAQ:
*"We can only deliver you time ordered Tick and M1 (1 minute) data."* Measured and hashed —
`VENDOR_TIMEFRAME_AVAILABILITY.md`. The external comparison is not unrun, it is
**unavailable from this vendor**.

**The consequence, stated once and plainly:**

> Seven PASSes establish that this aggregation is **self-consistent**. They do **not**
> establish that its bucket boundaries agree with anyone else's, because nothing here
> compares them to anyone else's. Self-consistent is a strictly weaker claim than correct,
> and an unmeasured quantity is not a passing grade.

What the checks *are* good for: every one of them is a failure mode that has silently
corrupted a real backtest, and any of them firing would have meant these bars were unusable.
None fired. That is worth having. It is not a validation.

---

## §1 — THE SEVEN CHECKS

| | Check | Result | What it establishes | What it cannot |
|---|---|---|---|---|
| **X1** | Independent re-implementation | **PASS** — 4/4 files, bar-for-bar | A second, structurally different aggregator (single-pass close-the-run) reproduces `aggregate_m15.py` (dict-accumulate-then-sort) exactly. The two have non-overlapping failure modes: a dict aggregator survives out-of-order input silently, a run aggregator does not. | Anything about the *spec* both implement. Two correct implementations of a wrong rule agree perfectly. |
| **X2** | Reproducibility vs `D-036a` | **PASS** — 86,824/86,824 both arms | The M15 files this session derived are identical to the ones `D-036a` built and its window-coverage table counts. The M1 corpus has not drifted, and the numbers in `D-036a` still describe the bytes on disk. | Nothing about H1 — `D-036a` never built one. |
| **X3** | Transitivity, H1(M1) vs H1(M15) | **PASS** — 21,708/21,708 both arms | The 15- and 60-minute grids **nest**. Aggregating M1→H1 directly and M1→M15→H1 give identical bars. A boundary error in either grid breaks this and very little else catches it. | Whether the shared grid origin (midnight of the bar's own day) is the right origin. |
| **X4** | Containment | **PASS** — 217,064 bars, all four files, **every bar checked, not sampled** | Each derived bar's O/H/L/C is exactly reconstructible from the M1 bars inside its own window, and every member bar maps back into that window. This is the off-by-one-window check. | Whether the window's *edges* fall where a vendor would put them. |
| **X5** | `D-031` arm correspondence | **PASS** — 0 positional mismatches, M15 and H1 | Arm A and Arm B produce **bar-for-bar identical candles**; only the label moves. Offsets are exactly `0h` (30,343 M15 bars / 7,587 H1) or `+1h` (56,481 / 14,121) and nothing else. | — (see §2, this is the substantive finding) |
| **X6** | DST transition audit | **clean** — 7 changeovers, 0 duplicate stamps | No bar lands on a skipped or repeated local hour on either arm, at either timeframe. The market is shut across the 02:00 changeover (the week opens Sunday 17:00), so the offset flips at a weekend boundary where there is nothing to corrupt. | — |
| **X7** | Bucket occupancy census | **report** — M15 96.28% complete, H1 89.28% | Partial buckets are located and counted. They cluster on session edges, Dec/Jan closures and the documented 2014-06-01 hole. | Nothing — it is a census, deliberately not a gate. A synthetic flat candle would be worse than a gap. |

The 7 DST changeovers audited: `2013-03-10`, `2013-11-03`, `2014-03-09`, `2014-11-02`,
`2015-03-08`, `2015-11-01`, `2016-03-13`. `2016-11-06` falls outside the corpus, which
terminates at the `D-035` boundary — correct, not a miss.

---

## §2 — THE ONE SUBSTANTIVE FINDING: AT M15 AND H1, `D-031`'s ARMS MOVE NO CANDLE

X5 is the check worth reading twice.

**Measured:** Arm A and Arm B are bar-for-bar identical in O/H/L/C, at both timeframes, over
all 86,824 (M15) and 21,708 (H1) bars. Zero positional mismatches. The label offset takes
exactly two values, `0h` and `+1h`, and never anything else.

**Why it must be so, so nobody reads it as luck:** Arm B is Arm A shifted by a whole number
of hours, and both 15 and 60 divide 60. A whole-hour shift therefore maps the bucket grid
onto itself. The candles cannot change; only their names can.

**Why it matters anyway — this is the useful half.** `D-031` requires both arms be run and
both reported, and the *cost* of that has always been the argument against doing it. At
these timeframes the cost is now known to be nil for anything shape-based:

> **The arm choice cannot change a candle at M15 or H1. It changes only which SESSION a
> candle falls in.** So the `A-019` timezone question has no bearing whatsoever on
> EMA values, TDI values, bar ranges, or any measurement made on the candles themselves —
> and full bearing on every claim involving a session boundary.

**Two cautions, because that finding is easy to over-read:**

1. **It is timeframe-specific and it will stop being true.** It holds because the shift is a
   whole hour. Any timeframe that does not divide an hour — M90, H4 anchored off-hour — and
   the arms *will* cut different candles. Do not carry this forward as a general property of
   `D-031`.
2. **It does not narrow `A-019` by one inch.** The session table still has no stated
   timezone, the instructor still declines to give one, and every session-dependent claim
   still needs both arms reported. What this establishes is where the question *cannot*
   reach, not an answer to it.

---

## §3 — WHAT CHANGES ABOUT `D-036a`'s OWN FIGURES: NOTHING, AND IT WAS CHECKED

The census checks were re-run at the two new granularities, against `D-036a`'s recorded M1
figures. Every one reproduces:

| `D-036a` figure | M1 (recorded) | M15 (measured here) | H1 (measured here) |
|---|---|---|---|
| Sunday-delimited week opens | 181 | **181** | **181** |
| Intra-week re-opens (never week boundaries) | 6 | **6** | **6** |
| Weeks not closing Friday | 3 | **3** | **3** (Arm A) |
| Week open, Arm A time-of-day | 17:00, fixed | **17:00 × 181, no exceptions** | **17:00 × 181** |
| Seasonal shift on Arm A (DST) | none | **none** | **none** |
| The 2014-06-01/02 hole | present | **present** | **present** |

The Arm A week-open result is a genuine independent corroboration of `D-036a`'s
fixed-offset conclusion — 181 opens landing on 17:00 with **zero** exceptions at both new
timeframes, where the M1 measurement had 170 exact and the rest at 17:01–17:10 (late opens
that aggregation absorbs into the 17:00 bucket). Arm B correctly shows the DST shift:
modal open 17:00 in Nov–Feb, 18:00 in Mar–Oct.

### One divergence, and it is `I-010` Question 2 surfacing again

`SETUP_ISSUES.md` `I-010` Q2 records that Arm B spills **4 M15 bars** past the `D-035`
boundary into wall-clock `2016-07-01`. **At H1 the same spill is 1 bar** — `2016-07-01
00:00`, flagged by `C8` as *"2016-07-01 Fri, 1 bar"*. A knock-on: under Arm B the H1
"weeks not closing on a Friday" count reads **2**, not 3, because the 2016-06-26 week now
ends on Friday 2016-07-01 instead of Thursday 2016-06-30.

**This is not a new defect and it is not this dataset's to fix.** It is the same unstated
clock `I-010` Q2 already asks about, appearing at a new granularity. `I-010` recommends —
and does not decide — that the boundary be declared **absolute, in the corpus's native
UTC−5 (Arm A) clock**. **The owner call is still owed.** Until it is made, any H1 Arm B
window running to the `D-035` boundary must state which of the two readings it used.

---

## §4 — A QA MISFIRE, RECORDED RATHER THAN QUIETLY FIXED

`qa_histdata_htf.py`'s check `C9` asserts that the documented 2014-06-01/02 hole is **still
visible** after aggregation — a gate that fails if a known-bad input starts looking clean,
which is what an aggregator that invents bars would produce.

**On its first run C9 FAILED, and the defect was in the assertion, not in the data.** The
M1 corpus resumes at `2014-06-02 15:01`. At M15 that minute falls inside the `15:00–15:15`
bucket, so a `15:00` bar legitimately exists, built from the fourteen surviving minutes.
The assertion had been written against the raw `[17:00, 15:01)` interval rather than against
the bucket grid, and duly flagged a correct bar as an invented one.

Recorded because it is the same failure shape `D-036a` records twice — **a check that
treats a boundary as an absence** — and because it cost exactly one false alarm, precisely
because it fired loudly rather than passing quietly. The corrected form asserts two things:
the buckets *wholly* inside the hole are empty, **and** the resumption bucket is present. If
the second half failed, the hole would be longer than the record says and the record would
be wrong.

---

## §5 — REPRODUCING THIS

```bash
python3 06_MANUAL_BACKTEST/scripts/crosscheck_htf.py \
    06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/raw \
    06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M15_H1/derived \
    --legacy-m15-dir 06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1
```

Runs in ~26 s over the full 1,297,781-bar corpus. Exit 0 on pass. Every figure above is
reproducible from files whose SHA-256 is recorded in `derived/SHA256SUMS.txt` — `E06`
satisfied: nothing here was read off a rendering.
