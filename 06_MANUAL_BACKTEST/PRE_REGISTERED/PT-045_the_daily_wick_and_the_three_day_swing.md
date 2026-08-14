# PT-045 — V17's **daily wick** and its **three-day unidirectional swing**: two claims from the `TREND` lesson, tested against a shuffled-day null

**Pre-registered:** 2026-08-14, on branch `video/v17`.
**Committed BEFORE the runner exists and before a single bar is read**, per
`COMMON_PROTOCOL.md` §9 and the `PT-036` / `PT-041` / `PT-043` / `PT-044` precedent.

---

## §0 — NUMBERING

`PT-044` is the highest pre-registered test on `video/v16`. This is **`PT-045`**. ⚠ If a
concurrently running session has allocated `PT-045` against the same state, this file is renumbered
on integration under `D-047` §4 / `D-042` §4 and **the design is not touched** — exactly as V15's
items were renumbered.

---

## §1 — THE CLAIMS

V17's second half is a printed, three-slide account of a **three-day dealer cycle**
(`V17_SOURCE_NOTES.md` §11). Most of it is untestable by this project today, and `§1b` says why.
**Two statements inside it contain no undefined term.**

**Claim `W` — THE WICK.** `[00:42:48]`–`[00:43:03]`:

> *"They'll make the clothes off of those numbers open high low clothes **gives you the wick on the
> daily candle** \| … **the wick on the daily candle represents the consolidation off of the higher
> off of the low** To end the cycle for 24 hours which paints the daily candle"*

**Claim `S` — THE SWING.** `[00:42:25]` and the printed `3 Day Cycle` slide
(`V17_00-42-10_…png`):

> *"Once the trend is set there'll be a **unidirectional swing for two and a half to three days**"*
> `Trend Is Generally Setup As A 3 Day Cycle.`

### §1a — WHY THESE TWO AND NOT THE OTHERS

Both can be evaluated from OHLC alone. **Neither requires an `M`, a `W`, a peak formation, a level
count, a TDI band, a "vector candle" or the word "aggressively"** — which is to say, neither
requires anything `A-010`, `A-011`, `A-036`, `A-084`, `A-097`, `A-118` or `A-120` has left open.

### §1b — WHAT IS **NOT** TESTED HERE, AND WHY — STATED BEFORE THE RUN

| V17 claim | Why not tested |
|---|---|
| The safety trade (`§8a`) | needs `V`/`W` (`A-010`/`A-011`) and a peak-formation test |
| *"shark fin ⇒ ≥ 50 pips"* `[00:38:41]` | needs the TDI band levels — `A-084`, blocked, **3,908 frames, zero dialogs** |
| The `333` trade | needs *"vector candle"*, undefined (`A-097`) |
| The pivot-zone shift (`§3`) | three of five antecedents undefined (`A-109`) |
| Day 1 / Day 2 / Day 3 as *labelled* | Day 1 requires a peak formation |
| *"heavy net short"* `[00:48:50]` | dealer inventory is **not observable from price**, at all, ever |

⚠⚠ **Four of V17's five most interesting claims are untestable by this project today. That is a
finding about the corpus and it is recorded here, in advance, so that a modest result on two
peripheral claims is not read as a verdict on the lesson.**

---

## §2 — THE QUESTIONS

**`Q1` (wick):** Do daily candles carry wicks on both ends materially more than a **volatility-
matched random walk** built from the same day's own minute returns? *"The wick represents the
consolidation"* is a claim that the wick is **produced by a mechanism**. If a shuffled day produces
the same wick geometry, the claim explains nothing that ordinary path geometry does not.

**`Q2` (swing):** After a mechanical directional reversal, does price continue in the new direction
for **2–4 days** more often than the same series' unconditional run-length distribution?

⚠⚠ **`Q2` USES A PROXY AND THE PROXY IS DECLARED HERE, NOT DEFENDED AS EQUIVALENT.** V17's Day 1 is
a *peak formation* reversal. This test uses **a daily close that flips the sign of a 3-day run**.
**These are not the same object.** If the reviewer judges the proxy uninformative about V17, `Q2`
tests nothing about this lesson and `§8` says so.

---

## §3 — CONSTRUCTION — every definition fixed here, before any data is read

**Instrument:** GBP/USD, the `HISTDATA_GBPUSD_M1` corpus, `D-036a`. **Pip = 0.0001.**

**Session day:** `mmm_lib` convention **`C-1`** — day `D` = `[ D−1 17:00, D 17:00 )` on the arm's
own clock. **Not redefined here.**

**Daily OHLC:** `O` = first M1 open in the session day; `H`/`L` = extremes; `C` = last M1 close.

**Wicks, in pips:**

```text
body_hi = max(O, C)          body_lo = min(O, C)
upper   = (H - body_hi) / PIP
lower   = (body_lo - L) / PIP
range   = (H - L)      / PIP
wick_frac = (upper + lower) / range        # 0 = marubozu, 1 = doji
```

**Daily direction:** `sign(C_d − C_{d−1})`. **Days with `C_d == C_{d−1}` are dropped and counted.**

**A REVERSAL day `R`:** `sign(R) ≠ 0` and `sign(R−1) = sign(R−2) = sign(R−3) = −sign(R)`.
**Three same-sign days then a flip.** Fixed now; no tuning.

**RUN LENGTH from `R`:** the number of consecutive session days from `R` inclusive carrying
`sign(R)`.

### §3a — THE INCLUSION FILTER, AND IT IS THE ONLY ONE

A session day enters if **all 96 fifteen-minute buckets of its 24-hour span carry a bar**
(`mmm_lib` **`C-6`**). Exclusions are **counted and reported**, never dropped quietly. **No holiday
filter, no news filter, no volatility filter** (`COMMON_PROTOCOL.md` §3 disclosure 1).

Reversal and run-length tests additionally require **days `R−3 … R+4` all present and consecutive**;
sequences broken by an excluded day are **dropped and counted**, not bridged.

### §3b — BOTH `D-031` ARMS, BOTH REPORTED

Arm `A` (raw file clock) and Arm `B` (`+1 h` during US DST). **Both are run and both are reported.
Neither is preferred and they are never pooled.**

---

## §4 — WINDOWS AND DATA

| | Window | Scope |
|---|---|---|
| **`W-D`** | `2013-01-02 → 2016-06-30` | `D-035` DEVELOPMENT — the **primary** window |
| **`W-E`** | `2017-01-03 → 2025-12-31` | the `D-044` extension — the **replication** window |

**`2016-07-01 → 2016-12-31` is sealed, is not on disk, and is not touched.** The two windows are
**reported separately and never pooled** (`PT-044` §4, unchanged).

`mmm_lib.qa_gate()` is a precondition on the run, per `COMMON_PROTOCOL.md` §1.

---

## §5 — OUTCOME MEASURES

| | Measure |
|---|---|
| `O1` | Median `wick_frac` across included days |
| `O2` | Fraction of days with **both** `upper ≥ 5 pips` and `lower ≥ 5 pips` |
| `O3` | ⭐ `O1` and `O2` recomputed on the **SHUFFLED-DAY CONTROL** (`§5a` `N1`), and the **difference** |
| `O4` | Distribution of run length from a reversal day: median, and `P(run ∈ {2,3,4})` |
| `O5` | `P(run ≥ 3 │ reversal)` against the **unconditional** `P(run ≥ 3)` over all runs in the series |
| `O6` | Mean signed cumulative pips over `R … R+2` in `sign(R)`'s direction, with a bootstrap interval |

## §5a — CONTROLS, FIXED NOW (`D-026` / `D-029`)

* **`N1` — THE SHUFFLED-DAY NULL, and it is the core of `Q1`.** For each included day, take that
  day's own 1,440 M1 **close-to-close returns**, permute them with a fixed seed, and rebuild a
  synthetic path from the same `O`. **Volatility, return distribution and day length are preserved
  exactly; only the ORDER is destroyed.** Recompute `O1`/`O2`. `ITERATIONS` and `SEED` are
  `mmm_lib`'s, unchanged.
* **`N2` — the unconditional run-length distribution**, over every run in the series, not just
  post-reversal ones. This is `O5`'s comparator.
* **`N3` — a date-shifted reversal set:** the same count of reversal days drawn at random from
  non-reversal days, same seed. Guards against `O4` reflecting the series' general run structure.
* **`N4` — exclusions are counted and printed beside every `n`.** The honest form is
  `n = 812 (17 excluded for incomplete sessions, 4 for zero daily change)`.

---

## §6 — DECISION RULE — FIXED NOW, BEFORE THE RUN

**Claim `W` (wick):**

| Result | Verdict |
|---|---|
| `O1` real − `O1` shuffled **> +0.05** AND `O2` real − `O2` shuffled **> +0.05** | **SUPPORTED** |
| both differences within `±0.05` | ⭐ **NOT SUPPORTED — the wick is path geometry, not a mechanism** |
| either difference **< −0.05** | **CONTRADICTED** |
| the two disagree in sign | **INDETERMINATE**, reported as such |

**Claim `S` (swing):**

| Result | Verdict |
|---|---|
| median run ∈ `[2,4]` AND `P(run ≥ 3│rev)` exceeds `N2` by **> 0.05** | **SUPPORTED** |
| median run ∈ `[2,4]` but the `N2` margin is `≤ 0.05` | ⚠ **WEAKLY SUPPORTED** — the number is right and the *conditioning* adds nothing |
| median run outside `[2,4]` | **CONTRADICTED AS STATED** |

**`W-E` is scored under the identical rule and reported beside `W-D`. If the two windows disagree,
BOTH are reported and neither is suppressed** (`PT-044` §6, unchanged).

---

## §7 — PREDICTIONS, COMMITTED BEFORE THE RUN

**Recorded so that being wrong is visible.**

| # | Prediction |
|---|---|
| `P1` | `O1` (real, `W-D`) will fall in **0.30 – 0.45** |
| `P2` | `O2` (real, `W-D`) will exceed **0.90** |
| `P3` | ⭐ **Claim `W` will be `NOT SUPPORTED`** — the shuffled control will produce wicks of a very similar size, because a random walk that ends anywhere but its own extreme has two wicks by construction |
| `P4` | Median run length from a reversal will be **2**, i.e. **below** the lesson's *"two and a half to three days"* |
| `P5` | `P(run ≥ 3 │ reversal)` will exceed the unconditional rate by **less than 0.05** ⇒ claim `S` **WEAKLY SUPPORTED** at best |
| `P6` | `W-D` and `W-E` will **agree on both verdicts** |

⚠ **`P3` predicts this session's own headline test fails.** That is deliberate: a control that the
claim was always going to beat is not a control.

---

## §8 — WHAT A RESULT HERE WOULD AND WOULD NOT MEAN

**Would:** establish whether two statements V17 makes about daily-bar geometry and multi-day
persistence describe GBP/USD over 13 years, on two disjoint windows and two timezone arms, against a
null that preserves volatility.

**Would NOT:**

1. **Test the three-day cycle as the lesson means it.** `§2` `Q2`'s proxy is a mechanical sign flip,
   **not** a peak formation. **A `CONTRADICTED` on `S` does not refute V17's Day 1.**
2. **Say anything about the safety trade**, which is the lesson's actual recommendation and the
   thing it spends its last three minutes on.
3. **Generalise past GBP/USD.** One instrument.
4. **Bear on 2012.** The corpus starts in 2013; **the lesson was recorded in 2012 and no 2012 data
   is on disk.** Every V-series test carries this and it is restated rather than assumed.
5. **Say anything about whether the wick is *"consolidation"* in the causal sense.** A `SUPPORTED`
   on `W` would show the geometry is non-random; it would not show *why*.

---

## §9 — LIMITATIONS DECLARED IN ADVANCE

* **The shuffle null destroys autocorrelation as well as ordering.** If GBP/USD minute returns are
  meaningfully autocorrelated, `N1` is a slightly *weaker* path than reality and would bias `O3`
  **toward** `SUPPORTED`. **Stated now**, so a `SUPPORTED` result is read with it.
* **`C-1`'s 17:00 boundary is a convention, not V17's.** V17 never states a daily boundary. A
  different boundary gives different wicks. **`O1` is therefore a statement about `C-1` days**, and
  this is exactly the class of hidden dependency `A-107` and `C-023` are about.
* **`§3`'s reversal definition uses a 3-day prior run** because V17's cycle is 3 days. **That is a
  choice, it is fixed here, and it is not tuned.** No second definition will be tried after seeing
  the first result; if one is, `BT_V17_0001.md` will say so and mark the original superseded rather
  than replacing it (`REMEDIATION_PROTOCOL.md` §2).
* **`n` for the reversal test will be small.** A 3-day run followed by a flip is not common. If
  `n < 60` in either window, the verdict is reported **with the interval and with an explicit
  underpowered flag**, not suppressed.
