# PT-040 — Does `A-084`'s smoothing ambiguity change the RSI thresholds V11 states?

```text
STATUS:      PRE-REGISTERED -- NOTHING HAS BEEN RUN
WRITTEN:     2026-08-13
SESSION:     V12 student, branch video/v12, isolated worktree (D-038)
NUMBER:      PT-040. Verified FREE before allocation -- PT-037 and PT-038 are V10's
             reservations, PT-039 is V11's re-issued test (owner ruling, REVIEW_INDEX
             item 99), and every occurrence of "PT-040" in the tree at the time of
             writing is prose stating that it was NOT allocated.
GOVERNED BY: COMMON_PROTOCOL.md (§1 instrument/units/data, §2 measurement, §5 seed,
             §9 rules). BACKTEST_EVIDENCE_STANDARD.md. D-005, D-007, D-009, D-010,
             D-026, D-027, D-029, D-030, D-031, D-035, D-036a.
```

> ### ATTESTATION — the whole value of this file
>
> **The session writing this has opened no chart, loaded no price series, computed no
> RSI, and inspected no GBP/USD outcome data of any kind.** Every threshold, window,
> smoothing length, sample definition and decision rule below is fixed **now**, before
> a single bar is read. The runner `run_pt040.py` **does not yet exist**; it will be
> written after this file is committed, and the ordering is verifiable by
> commit timestamp (`D-026`).
>
> `COMMON_PROTOCOL.md` §9 rule 7: **if the runner and this file ever disagree, THIS FILE
> GOVERNS**, neither is edited, and the disagreement is reported in `BT_V12_0001.md`.

---

## 1. THE QUESTION, AND WHY IT IS THIS ONE

**V12 closed `A-080`.** The course author states the RSI lookback four times —
*"I like the RSI line to be set at **21**"* `[00:07:24]`, *"**21 closing periods back**…
instead of 14 periods"* `[00:08:09]`, *"we have this line set to 21, **21 look back
periods**, that's all"* `[00:10:51]` — and declares it the group's template preset.
That was the single largest blocker in V11's half of this session.

**And it did not fully unblock what it was supposed to unblock.** `A-084`, opened by this
session, asks:

> **Is the green line plotted in the TDI sub-window `RSI(21)`, or a SMOOTHING of
> `RSI(21)`?**

V12 says only that *"TDI is developed off of the RSI, so there's your RSI line"*
`[00:11:22]` — **lineage, not identity**. Dean Malone's shipped TDI plots its green line
as a short moving average **of** the RSI, and V12 states no smoothing length. V11's
threshold claims (`50` bias baseline, `80/40` bull range, `60/20` bear range, `80/20`
overextension) are read **off the line in the sub-window**, so if that line is smoothed,
testing them against a raw `RSI(21)` tests a different series.

**This test does not resolve `A-084`. It measures whether `A-084` MATTERS.**

```text
THE QUESTION:
  Over the pre-registered window, does it make a MATERIAL difference to the
  threshold statistics V11's claims depend on whether the series is RSI(21)
  or a short moving average of RSI(21)?
```

**If the answer is no, `A-084` is an unresolved definition with no practical
consequence for threshold-crossing claims, and V11's RSI half is unblocked in
practice.** If the answer is yes, V11's RSI claims **stay blocked** until a lesson
supplies the smoothing length, and this file says so in advance.

**This is `A-084`'s own *Required Research* option (c), pre-registered.**

---

## 2. ⛔ WHAT THIS TEST DOES **NOT** TEST — read before quoting any number from it

Five things, each of which a reader could mistake this for:

1. **It does NOT test whether V11's threshold claims are true.** The `80/40` bull range
   and `60/20` bear range are claims *conditional on an uptrend or a downtrend*, and
   **the corpus has never defined either** — `A-070`, `A-004`, `A-061`. A test of the
   claims requires a trend definition that `D-030` forbids inventing. **This test is
   about the SERIES, not about the CLAIMS.**
2. **It does NOT test the TDI.** Three of the TDI's four parameters are unstated
   (`A-039`, `A-085`, `A-086`) and the indicator is not reconstructible. **No TDI is
   built here.** Only a plain RSI and moving averages of it.
3. **It does NOT adopt a smoothing length.** The lengths in §4 are a **sensitivity
   sweep over the ambiguity**, not a candidate value. **`D-030` is not breached by
   asking "does the choice matter?"** — it would be breached by answering "the choice
   is 2". **No `k` is adopted, recommended, or carried into any other artifact.**
4. **It does NOT test V12's 85% claim** (`[00:01:04]` *"is good for approximately
   85%"*). That claim rests on *"the second leg of an M or W"* (`A-011`, undefined
   across nine lessons) and *"above or below the blue box"* (`A-076`, undefined). **It
   is the most falsifiable thing V12 says and it is not testable by this corpus.**
   Recorded here so a reader does not assume it was quietly skipped.
5. **It does NOT establish that `RSI(21)` is the right period for anything other than
   what the course says it is.** `A-080` closed on the instructor's own statement about
   his own preset. This test **consumes** that closure; it does not re-verify it.

---

## 3. CONSTRUCTION — fixed now

### 3.1 Series

| Symbol | Definition |
|---|---|
| `C` | The **closing price** of each M15 bar, from the checksummed HistData GBP/USD M1 corpus aggregated to 15 minutes (`D-036a`, `COMMON_PROTOCOL.md` §1). **Nothing is read from a rendering** (§2 of that file) |
| `R` | **Wilder's RSI, period 21**, computed on `C`. Wilder smoothing (`alpha = 1/21`), the standard formulation, seeded by a simple mean of the first 21 gains and losses. **21 is the course's number** (`A-080`) |
| `S_k` | **The simple moving average of `R` over `k` bars**, for `k` in §4's set. `S_1 = R` by construction and is included as the identity control |

**Why M15.** V12 `[00:03:24]` *"I want you to learn how to use the indicator on the
**15-minute chart**"*; V11 teaches the RSI on the 15-minute; `MMM-NOTES` and every prior
`PT` in this project use the 15-minute as primary. **Not a free choice.**

**Why Wilder's RSI.** It is *the* RSI — the formulation the name denotes, and the one
`[00:08:09]`'s *"averaging that out"* over *"21 closing periods back"* describes. **If a
reviewer holds that a simple-average RSI variant should have been used, that is a
disagreement about the standard formula and not about this design**; the runner will
print both the Wilder and the simple-average variant of `R` as a **secondary
robustness line** (`N3`) so the question is answerable from the committed output without
a re-run.

### 3.2 The thresholds — taken from V11, not chosen here

Every threshold below is a number **the course prints**. None is selected by this
session.

```text
T = { 20, 40, 50, 60, 80 }
```

| Threshold | Where the course states it |
|---|---|
| `50` | V11 printed frame `31:25`, *"Mid Point or Basis Level of 50"*; V11 `[00:30:13]`–`[00:31:03]`; V12 `[00:13:32]` *"there's your 50"* |
| `80`, `40` | V11 printed `31:25` and `37:30`, *"Bull Range: 80/40"* |
| `60`, `20` | V11 printed `31:25` and `37:30`, *"Bear Range: 60/20"*. `80/20` also printed as *"Overbought/Oversold"* |

### 3.3 Window — `W-A`, and the `D-035` holdout is asserted on every slice

```text
W-A = 2015-01-04 -> 2015-12-31 23:59   (COMMON_PROTOCOL.md §3; mmm_lib.WINDOWS["W-A"])
```

**`W-A` is chosen because it is the batch's standard primary window and requires no new
justification.** `D-035`'s holdout (2016-07-01 onward) is **asserted on every slice** via
`mmm_lib.assert_development`, which exits non-zero on breach.

**A second window is pre-registered as a robustness cell, not as a second primary:**
`W-B` = 2014-01-05 → 2015-12-31. **`W-A` is the primary. `W-B` cannot rescue a `W-A`
result and is not permitted to.**

### 3.4 `D-031` arms

Both arms are run and both are reported: **Arm A** (fixed UTC−5, no DST) and **Arm B**
(US DST-tracking), per `D-031` and `mmm_lib.shift_to_arm`.

> ⚠️ **`REVIEW_INDEX.md` item 101 does NOT bite on this test, and the reason is stated
> so a reviewer does not have to check.** Item 101 found that `D-031` Arm B corrupts any
> test whose **unit of analysis is the session day**, because the ±1 h shift breaks the
> 96-bucket completeness rule. **This test's unit of analysis is the BAR.** There is no
> session-day construction, no completeness rule, no `C-1` day boundary, and no
> per-day exclusion anywhere in the design. **Arm B is therefore a clean robustness
> check here**, and this is the first `PT` since item 101 for which that is true.
> **The arms should agree almost exactly** — a clock shift relabels bars, it does not
> change the close series — and **any material disagreement is a TOOLING BUG, not a
> finding.** That expectation is recorded now so it cannot be rationalised later.

---

## 4. OBSERVATIONS — every number the run will report, fixed now

**Smoothing lengths swept:** `k ∈ {1, 2, 3, 5}`. `k = 1` is the identity control.
**No `k` is adopted (§2.3).**

### `O1` — Marginal occupancy

For each `k` and each `t ∈ T`: the fraction of M15 bars with `S_k ≥ t`.

```text
O1(k, t) = #{ bars : S_k >= t } / #{ bars }
```

### `O2` — ⭐ Side disagreement, the primary observation

For each `k ≥ 2` and each `t ∈ T`: the fraction of bars on which `S_k` and `R` fall on
**opposite sides** of `t`.

```text
O2(k, t) = #{ bars : (S_k >= t) XOR (R >= t) } / #{ bars }
```

**This is the number the decision rule in §5 turns on**, because a threshold claim is a
claim about which side of a line the series is on.

### `O3` — Crossing-count ratio

For each `k` and `t`: the number of sign changes of `S_k − t`, as a ratio to `R`'s.
**A smoothed series crosses less often**; this measures how much less, and it is the
observation most likely to differ even when `O2` is small.

### `O4` — Bull/bear range occupancy, both readings

For each `k`: the fraction of bars in `[40, 80]` and in `[20, 60]`, and the fraction in
**neither** and in **both** (the ranges overlap on `[40, 60]`).

**`O4` is DESCRIPTIVE and is pre-registered as such.** It is reported because V11's range
claims are the most-quoted RSI content in the corpus and a reader will want the marginals
beside the disagreement figures. **It tests nothing** — the claims are conditional on
trend (§2.1) — and **`BT_V12_0001.md` must classify it `DESCRIPTIVE`**
(`BACKTEST_EVIDENCE_STANDARD.md`).

### `N1` — Bar-count and coverage

Bars in `W-A` per arm, bars discarded to RSI warm-up (the first 21), and the date span
actually covered. **Reported before any rate**, per `COMMON_PROTOCOL.md`.

### `N2` — Window robustness

`O1`–`O3` repeated on `W-B`. **Reported beside `W-A`, never instead of it.**

### `N3` — Formula robustness

`O2` repeated with `R` computed by the **simple-average** RSI variant rather than
Wilder's (§3.1). **Reported as a line, not as a verdict.**

---

## 5. ⭐ THE DECISION RULE — FIXED BEFORE THE RUN

Let

```text
M = max over k in {2,3,5}, t in {20,40,50,60,80}  of  O2(k, t)     [W-A, Arm A]
```

`M` is the **worst-case side-disagreement across every smoothing length and every
course-stated threshold**, on the primary window and the primary arm.

| If | Verdict | What it means for `A-084` and for V11 |
|---|---|---|
| **`M ≤ 2.0 pp`** | ⭐ **IMMATERIAL** | The smoothing ambiguity does not change which side of a course threshold the series is on, at any threshold, for any of the swept lengths. **`A-084` stays OPEN as a definitional gap and is recorded as having NO PRACTICAL CONSEQUENCE for threshold-crossing claims.** V11's RSI half may be tested on `RSI(21)` directly, with `A-084` cited |
| **`2.0 pp < M ≤ 5.0 pp`** | **INCONCLUSIVE** | Neither unblocked nor confirmed blocked. **No claim moves.** A test of a V11 threshold claim must report `A-084` as a live uncertainty of up to `M` |
| **`M > 5.0 pp`** | **MATERIAL** | The choice of smoothing changes the answer. **V11's RSI threshold claims STAY BLOCKED** pending a course statement of the smoothing length, and `A-084` is promoted from a definitional note to an active blocker |

**The 2 pp and 5 pp boundaries are set now, in advance, and are not adjusted after the
run under any circumstance** (`D-029`, `COMMON_PROTOCOL.md` §9). They are chosen on the
same reasoning `PT-039` §4 used for its `+5 pp` feature bar: **5 pp is the smallest
difference this project has been willing to call a real effect anywhere**, and 2 pp is
the resolution below which a difference is not worth acting on.

### Secondary decision points, also fixed now

| Observation | Pre-registered expectation | If violated |
|---|---|---|
| **Arm A vs Arm B** | Agree to within **0.5 pp** on every `O2` cell | **Report as a SUSPECTED TOOLING BUG in `BT_V12_0001.md` §1a, not as a finding.** A clock relabel cannot change a close series (§3.4) |
| **`O1(1, 50)`** | In `[45%, 55%]` — an RSI is near-symmetric about its midpoint | Outside that band, **stop and report**: either the corpus or the RSI implementation is wrong, and no other number in the run may be quoted |
| **`O3(k, t)` for `k ≥ 2`** | **< 1.0** (a smoothed series crosses less) | A ratio ≥ 1.0 is an implementation error; **report, do not interpret** |
| **`N2` (`W-B`)** | Same verdict band as `W-A` | A different band is **reported prominently** and the `W-A` verdict still governs (§3.3) |

---

## 6. WHAT WOULD MAKE THIS TEST WRONG

Stated in advance, per `BACKTEST_EVIDENCE_STANDARD.md`:

1. **If the plotted TDI line is neither `RSI(21)` nor a simple MA of it** — e.g. an
   exponential or Wilder smoothing of the RSI, or an RSI of a smoothed price — then the
   swept family misses the truth and `M` is not the right quantity. **The sweep covers
   the shipped TDI's construction (a short SMA of the RSI) and nothing wider, and that
   is a limitation, not a hedge.**
2. **If `A-080`'s `21` is the smoothed line's period rather than the RSI's**, the whole
   construction is off by one indirection. `[00:08:09]` *"21 closing periods back for our
   line… instead of 14 periods"* is **strong evidence against** this reading — `14` is
   the RSI's default, not any smoothing default — but it is not conclusive and it is
   recorded as the design's main interpretive assumption.
3. **If GBP/USD M15 in `W-A` is unrepresentative** of the pairs and periods V11's charts
   show. `W-B` is the robustness cell and it is the same instrument.

---

## 7. PROVENANCE AND REPRODUCTION

| Item | Value |
|---|---|
| Data | `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record, QA gate C1–C4 **PASS** as a precondition (`COMMON_PROTOCOL.md` §1) |
| Runner | `06_MANUAL_BACKTEST/scripts/run_pt040.py` — **does not exist at the time this file is committed** |
| Output | `06_MANUAL_BACKTEST/V12/data/pt040_output.txt`, committed verbatim and never edited (`D-027`) |
| Report | `06_MANUAL_BACKTEST/V12/BT_V12_0001.md` |
| Seed | **`20260813`**, recorded here before the run. ⚠️ **`REVIEW_INDEX.md` item 113** records that `mmm_lib.provenance_header()` prints the **library** batch constant `20260812` rather than the calling runner's seed. **This test uses NO randomisation** — every observation in §4 is a deterministic count over a fixed series, with no bootstrap, no permutation and no shuffle — **so the seed is recorded for form and affects nothing.** The banner discrepancy item 113 describes will therefore appear in this run's header **and is harmless here**; it is stated so a reader does not have to re-derive that |
