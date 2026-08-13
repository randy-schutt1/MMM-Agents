# PT-035 — *"It's highly unlikely we're gonna lose three or four times in a row"*: the empirical premise the whole V09 risk plan rests on

> **WRITTEN AND COMMITTED BEFORE ANY BAR IN THE WINDOW WAS READ BY THIS SESSION.**
> No chart was opened, no aggregate computed, and no row of the corpus parsed for this test
> before this file existed in Git. The runner is written **after** this file is committed, and it
> prints the nulls before any rule-side number (`COMMON_PROTOCOL.md` §9 rule 1).

**Governed by:** `COMMON_PROTOCOL.md` (all sections), `D-005`, `D-007`, `D-009`, `D-010`,
`D-026`, `D-027`, `D-028`, `D-029`, `D-030`, `D-031`, `D-033`, `D-034`, `D-035`, `D-036`,
`D-036a`.

---

## 0. NUMBERING

`PT-034` is the highest number in `PRE_REGISTERED/` at the moment of writing, verified by
re-listing the directory **and** by re-deriving the identifier set against the latest integration
branch after this worktree's merge from `origin/claude/add-documents-repository-fdfb3u` at
`f3f9006`. This file takes **`PT-035`**. If a collision is ever found with a concurrently-authored
test, **this file is the one that renames** — it is cited from no decision entry.

---

## 1. THE CLAIM UNDER TEST

**Source: V09, `[00:06:08]`–`[00:06:20]`. Speaker: `GUEST` — V09 carries zero course-author
runtime. Under `D-033` this is NORMATIVE evidence at equal weight.**

> *"Believe it or not, this is still a rather aggressive approach to risk management. However I
> believe that with our training **it's highly unlikely we're gonna lose three or four times in a
> row**. If of course we've put the time in to develop the rest of our game."*

**This is not a decorative aside. It is the load-bearing empirical premise of the entire V09
position-sizing rule**, which is printed on frame 10 and stated at `[00:08:20]`–`[00:08:43]`:

```text
loss 1 -> same lot size
loss 2 -> same lot size
loss 3 -> same lot size
loss 4 -> recalculate (account is now 8% down)
```

**Holding size through three consecutive losses is only prudent if three consecutive losses are
rare.** If they are common, the rule is a mild martingale: it declines to reduce exposure during
exactly the stretch in which the trader is losing. The lesson says they are rare. **Nobody has
checked.**

### The supporting claim on the same slide family, also under test

> Frame 5, printed: *"With 2% risk at Stop Loss, one can lose **THREE TRADES IN A ROW** and still
> have enough margin to come back and NEGATE the LOSS with just one trade!"*

### Two things this test explicitly is NOT

| Not this | Why |
|---|---|
| A test of a V09 **entry rule** | **V09 states no entry rule.** It is a money-management lesson. `D-030` forbids inventing one |
| A test of *"with our training"* | V09's *"training"* is V08's HOD/LOD drill, whose recognition criterion is `A-061` (*"the fast move is false"*) — **an undefined adjective**. `D-030` binds. The conditional half of the claim is **not** tested here, and §6a says what that costs |

**What IS testable, exactly:** *"three or four in a row"* is a claim about the **loss-run
distribution of a trade sequence**, and V09 supplies both geometries that generate one
(`25/50` and `15/50`). The distribution can be measured on real GBP/USD without any pattern
definition whatsoever.

---

## 2. WHAT IS AVAILABLE IN CLOSED FORM BEFORE THE DATA IS READ, STATED HERE SO IT CANNOT LATER BE PRESENTED AS A DISCOVERY

`COMMON_PROTOCOL.md` §9 rule 2 and `PT-034`'s precedent: anything derivable without the corpus is
stated **now**.

### 2a. The drawdown arithmetic is exact and V09 is right about it

Because the rule **holds lot size constant** across losses 1–4, each loss costs the **same
dollars**, not the same percentage. So four losses cost exactly `4 × 2% = 8.0%` of the original
balance — **not** `1 − 0.98⁴ = 7.76%`, which is what a session assuming per-trade recalculation
would compute.

**V09's `8%` is correct, and the naive check is the one that is wrong.** Recorded here because a
reviewer re-deriving it the obvious way will get 7.76% and think a defect has been found.

### 2b. Break-even hit rates, from V09's own geometries

| Geometry | Source | Break-even |
|---|---|---|
| `−25 / +50` (2:1) | `[00:04:55]`, frame 6 | **33.33%** |
| `−15 / +50` (3.33:1) | `[00:03:49]`–`[00:03:56]`, frames 5, 13 | **23.08%** |

### 2c. The i.i.d. loss-run probability, as a function of hit rate — the comparator

For independent trades with win probability `p`, the probability that a specific block of `k`
consecutive trades are **all** losses is `(1 − p)^k`. Over a sequence of `n` trades the
probability of **at least one** run of `k` losses has a standard recursion, which the runner
implements and prints.

Two anchor values, computed now:

| `p` | `(1−p)³` | `(1−p)⁴` |
|---|---|---|
| **0.3333** (2:1 break-even) | **29.6%** | **19.8%** |
| **0.50** (V09's *">50% accuracy"* claim, `A-067`) | **12.5%** | **6.25%** |
| **0.73** (midpoint of `PT-034`'s measured 70.5–76.8% HOD/LOD-proximity band) | **2.0%** | **0.5%** |

**So the truth of *"highly unlikely"* is entirely a function of the hit rate the training
delivers, and the lesson never states one.** At the break-even rate its own geometry implies,
a four-loss run happens roughly one block in five. **That is not "highly unlikely" by any
reading, and it needs no data to say so.**

### 2d. What therefore remains genuinely empirical — the whole point of the design below

Everything above assumes **independence**. Real FX outcomes are not independent: volatility and
direction cluster by regime, so consecutive stop-outs plausibly bunch. **If they do, the true
`P(4-run)` is HIGHER than §2c's table, and V09's plan is worse than even the pessimistic
closed-form reading.** That is measurable, it is not derivable, and it is what this test is for.

---

## 3. THE FOUR PRE-REGISTERED OBSERVABLES

All are computed over `W-C′` (`2013-01-06 → 2016-06-30`, `D-035` DEVELOPMENT), on the HistData
M1 corpus aggregated to M15 (`D-036a`), in **both `D-031` arms**, at **both V09 geometries**.

### `O1` — THE ARITHMETIC AUDIT, REPORTED AS A CHECK ON THE RUNNER

Re-derive every number V09 states in its worked example (`V09_SOURCE_NOTES.md` §2c) in committed
code. **Reads no market data.** Reported first, because if the runner cannot reproduce
arithmetic that is already known to close, nothing it says about the corpus is trustworthy.

### `O2` — THE REALIZED PER-TRADE HIT RATE OF A MATCHED-RANDOM ENTRY

`k / n` and its Wilson 95% interval, per geometry, per arm. **This is the null's own hit rate and
it is the input to `O3`.** It is reported for its own sake as well: it is the honest answer to
*"what does an untrained entry get at V09's geometry"*.

### `O3` — THE LOSS-RUN FREQUENCY, OBSERVED vs i.i.d. — THE FOCAL MEASURE

For each of `D-029`'s **1,000** iterations, draw a matched-random sequence of `n` trades in
**chronological order**, and record:

| Statistic | Definition |
|---|---|
| `run3_obs` | fraction of the sequence's length-3 blocks that are all losses |
| `run4_obs` | fraction of the sequence's length-4 blocks that are all losses |
| `run3_iid` | `(1 − p̂)³` using **that iteration's own** `p̂` |
| `run4_iid` | `(1 − p̂)⁴` using that iteration's own `p̂` |
| `maxrun` | longest all-loss run in the sequence |

**The focal quantity is the paired difference `run4_obs − run4_iid`**, reported as a median with
a bootstrap 95% interval and as the fraction of iterations in which it is positive.

> **Using each iteration's own `p̂` is the design decision that makes this a clustering test and
> not a hit-rate test.** It removes the level of the hit rate from the comparison entirely, so the
> only thing left to differ is the **arrangement** of wins and losses. Stated before the run
> because it is the choice a post-hoc analysis would be most tempted to make differently.

### `O4` — THE HIT RATE REQUIRED FOR THE CLAIM TO BE TRUE

Closed form, using the observed clustering adjustment from `O3`. Solve for the smallest `p` at
which `P(at least one 4-loss run in 100 trades) ≤ 5%`, both under i.i.d. and under the observed
clustering. **Reported against V09's own `>50%` claim (`A-067`) and against `PT-034`'s measured
70.5–76.8% band.**

> `PT-034`'s band is used as a **reference point that is quoted, never assumed**: it carries its
> own disclosed defect (`REVIEW_INDEX.md` open item 67 — its rule arm knows where the day's
> extreme is). It is cited here to give `O4`'s answer a scale, and **no conclusion in §6 depends
> on it.**

---

## 4. THE NULLS

### `N1` — matched random entry (`D-026` required form, `D-029` parameters)

| Parameter | Value | Why |
|---|---|---|
| Iterations | **1,000** | `D-029` headline standard |
| Seed | **20260812** (`COMMON_PROTOCOL.md` §5 batch constant) | `D-029` — recorded so the control is reproducible |
| Instrument | GBP/USD | `D-007` |
| Eligible window | `03:00`–`17:00` on the corpus clock, per arm — the standing eligible band `mmm_lib.TradeGrid` uses | `D-029`: the same opportunity set the geometry would trade |
| Direction — primary arm | **50/50 long/short, drawn per trade** | V09 states **no** directional rule, so there is no rule direction to match. This is `D-029`'s *secondary* (random-direction) arm promoted to primary **because the lesson supplies no other option**, and it is declared as such rather than dressed up as the primary form |
| Stop / target | **`25 / 50`** and **`15 / 50`**, run separately | V09's two stated geometries, `[00:04:55]` and `[00:03:49]` |
| **Entry PRICE convention** | **The CLOSE of the selected M15 bar.** Identical in every arm and every cell of this test | ⭐ **Stated here in the parameter table to discharge `REVIEW_INDEX.md` open item 65** (`V08_REVIEW_R1.md` `M2`), which required the next `PT` carrying a matched-random null to fix the null's entry price in the pre-registration rather than in the runner. **This test has no arm with a different anchor**, so `PT-034`'s defect cannot recur here |
| Resolution | First touch on **M1** bars; **stop wins a same-bar tie** | `COMMON_PROTOCOL.md` convention C-4 |
| Horizon | Position closed at `17:00` on the corpus clock if unresolved; unresolved trades are **excluded from the run analysis and counted** | Stated before the run; an open position is neither a win nor a loss and must not be silently scored as either |
| Sequence length `n` | **200** trades per iteration, drawn **in chronological order without replacement** | Order is the whole point of a run statistic. A shuffled draw would destroy exactly the clustering `O3` measures |

### `N2` — the i.i.d. comparator

Not a simulation: the closed-form `(1 − p̂)^k` computed from each iteration's own realized hit
rate, per `O3`. **This is the control that makes the finding readable** — `D-026`'s requirement is
a comparator that isolates the variable under test, and here that variable is *arrangement*, not
*rate*.

### `N3` — a shuffled-order sanity control

The same 1,000 sequences, **shuffled**, re-measured. Under shuffling all clustering must vanish
and `run4_obs − run4_iid` must centre on zero. **If it does not, the estimator is biased and the
whole test is void.** Reported before `O3`.

---

## 5. CELLS — TWO GEOMETRIES × TWO `D-031` ARMS, ALL FOUR ALWAYS REPORTED

| Cell | Geometry | Arm |
|---|---|---|
| `A25` | `−25 / +50` | **A** — corpus stamps verbatim (fixed `UTC−5`, no DST) |
| `B25` | `−25 / +50` | **B** — `America/New_York`, `+1h` during US DST |
| `A15` | `−15 / +50` | **A** |
| `B15` | `−15 / +50` | **B** |

**`D-031`'s binding rule applies: both arms are reported every time. Divergence is a finding,
never a selection criterion** (`E09`, `E24`).

---

## 6. THE DECISION RULE — FIXED NOW, BEFORE ANY NUMBER EXISTS

On the claim *"it's highly unlikely we're gonna lose three or four times in a row"*, evaluated at
the **matched-random hit rate**, i.e. **without** the training the claim conditions on:

| Verdict | Condition |
|---|---|
| **CONTRADICTED AS STATED** | `run4_obs` median ≥ **10%** in **all four** cells. A one-in-ten block of four is not "highly unlikely" under any ordinary reading |
| **PARTIALLY SUPPORTED** | `run4_obs` median between **5% and 10%** in a majority of cells |
| **CONFIRMED AS STATED** | `run4_obs` median < **5%** in **all four** cells |
| **INDETERMINATE** | Cells disagree across the 5%/10% boundaries, or `N3` fails |

On the **separate** question of clustering, which is the genuinely novel measurement:

| Verdict | Condition |
|---|---|
| **CLUSTERING CONFIRMED** | Median `run4_obs − run4_iid` **> 0** with a bootstrap 95% interval excluding 0, in ≥ 3 of 4 cells |
| **CLUSTERING NOT DETECTED** | Interval includes 0 in ≥ 2 of 4 cells |
| **ANTI-CLUSTERING** | Median **< 0** with interval excluding 0 in ≥ 3 of 4 cells — losses are more evenly spread than chance |

**Sample sufficiency, pre-labelled** (`BACKTEST_EVIDENCE_STANDARD.md` §4.1): every reported rate
carries `n` and a Wilson interval. Any cell whose usable `n` falls below **30** is labelled
`SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` **before** its number is read.

### 6a. THIS SESSION'S PREDICTION, RECORDED BEFORE THE RUN

**Committed here, in Git, before the runner exists.**

| # | Prediction | Confidence |
|---|---|---|
| **P1** | `O1` reproduces every V09 number exactly **except** the second-winner recovery, which will land at **$12,438.40** against a stated $12,500 (`C-014`) | **HIGH** — this is arithmetic already done by hand in `V09_SOURCE_NOTES.md` §2c; `O1` is a check on the runner, not a discovery |
| **P2** | `O2` will show a matched-random hit rate **near but not exactly at** the break-even values of §2b — around **0.30–0.36** at `25/50` and **0.20–0.26** at `15/50` — because first-touch resolution on a random entry is close to, but not identical to, the geometric ratio | **MEDIUM** |
| **P3** | **`run4_obs` will exceed 10% in all four cells, giving CONTRADICTED AS STATED** | **HIGH** — §2c makes this near-arithmetic at the hit rates P2 expects |
| **P4** | **`run4_obs > run4_iid`: losses will cluster.** Direction pre-registered as positive | **MEDIUM** — the mechanism (regime persistence) is real, but the effect may be small at a 200-trade scale, and `N3` may show the estimator has more noise than the effect |
| **P5** | `O4` will show the required hit rate for the claim to hold sits **above 50%**, i.e. **V09's own `">50% accuracy"` claim is NOT sufficient to make its own loss-run claim true** | **MEDIUM-HIGH** |

> **P5 is the prediction this session most wants to be wrong about**, because if it is right, two
> of V09's statements are in tension: the accuracy figure it advertises does not deliver the loss
> behaviour it promises. **That tension would be a finding about the lesson, and it is registered
> as a prediction rather than discovered as a conclusion precisely so it cannot be presented as
> one.** If `O4` lands below 50%, P5 is recorded as **wrong** and the claim survives on this axis.

---

## 7. WINDOW, HOLDOUT, DATA

| Field | Value |
|---|---|
| Window | **`W-C′` = `2013-01-06` → `2016-06-30`** — `D-035` DEVELOPMENT, in full |
| Holdout | `2016-07-01` → `2017-12-29` — **not opened.** The corpus on disk was truncated at `2016.06.30` on arrival (`D-036a`) and contains no post-boundary row |
| Source | HistData.com GBP/USD **M1** CSV corpus, SHA-256 in `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt`, aggregated by `scripts/aggregate_m15.py` |
| Week open | **22:00 UTC / Sunday 17:00 local, fixed `UTC−5`** (`D-036a`). Not FXCM's 21:00 UTC |
| QA gate | `scripts/qa_histdata_m1.py` → `QA_REPORT.txt`. **Precondition on the run**, asserted by the runner before any bar is read |
| Level comparability | Price **levels** here are **not** comparable with the V02–V06 TradingView/FXCM homework (`D-036a`). This test makes only **distance** claims (pips) and **count** claims, both of which travel |

### 7a. `C8` DISPOSITIONS — PRE-REGISTERED BY NAME, AS THE QA GATE REQUIRES

`QA_REPORT.txt` flags **11 sessions**; those falling inside `W-C′` are dispositioned here,
**before** any result exists:

| Session | Disposition | Ground |
|---|---|---|
| `2013-01-01 Tue` | **INCLUDE** | Dec/Jan market closure — real market behaviour, not a defect |
| `2013-12-25 Wed` | **INCLUDE** | Same |
| `2014-01-01 Wed` | **INCLUDE** | Same |
| `2014-12-24 Wed`, `2014-12-25 Thu` | **INCLUDE** | Same |
| `2015-01-01 Thu` | **INCLUDE** | Same |
| `2015-12-24 Thu`, `2015-12-25 Fri` | **INCLUDE** | Same |
| `2016-01-01 Fri` | **INCLUDE** | Same |
| **`2014-06-01 Sun`** | **EXCLUDE BY NAME** | **The data hole.** 0 bars against a nominal ~420 |
| **`2014-06-02 Mon`** | **EXCLUDE BY NAME** | 521 of ~1,440 bars; ~22 continuous hours absent (`D-036a` correction block) |

**The `E09` line, drawn explicitly:** `E09` forbids excluding an observation because of **what the
market did**. The 2014-06-01/02 exclusion is because **the corpus does not contain what the market
did.** That distinction is why `C8` exists and it is stated here so no later reader mistakes a
data-integrity exclusion for a convenience one. **The exclusion count is reported beside every
`n`.**

> **This test is unusually insensitive to the holiday sessions and that is stated rather than
> relied on**: a short session simply offers fewer eligible entry bars to the random draw. It is
> **not** insensitive to the data hole, which would fabricate a spurious ordering discontinuity in
> a sequence statistic — which is exactly why it is excluded by name.

### 7b. WHAT WOULD MAKE THIS TEST VOID

Stated before the run, so the escape hatch cannot be invented afterwards:

1. **`N3` fails** — shuffled sequences do not centre `run4_obs − run4_iid` on zero. The estimator
   would then be biased and **no `O3` number may be reported as a finding**.
2. **The QA gate fails.**
3. **Any cell's usable `n` < 30** — that cell is descriptive only, and if all four fall below,
   the test is `INDETERMINATE`.

---

## 8. MANDATORY SCOPE STATEMENT

To be carried, in this form, on **every** report of this test's result:

> **`PT-035` tests one empirical premise of one lesson's risk plan, at a matched-random entry.**
> It is **not** a test of the Market Maker Method, of V09's position-sizing formula, or of any
> entry rule — **V09 states no entry rule and none was invented** (`D-030`).
>
> **The claim under test is conditional — *"with our training"* — and the training is NOT
> reproduced here**, because V08's HOD/LOD recognition criterion is `A-061`, an undefined
> adjective. **A result at the matched-random rate therefore bounds the claim from below: it says
> what happens with no skill, not what happens with the skill the lesson assumes.** A
> `CONTRADICTED AS STATED` verdict means *the claim is false for an untrained entry*, and it says
> **nothing** about whether the training closes the gap. `O4` is what converts that bound into a
> statement about how much skill would be required.
>
> Speaker: **`GUEST`** (V09 carries zero course-author runtime). Under `D-033` this is normative
> evidence at equal weight; the tag is provenance, not demotion.
>
> Price **levels** are not comparable with the V02–V06 FXCM homework (`D-036a`). Only distance and
> count claims travel.
>
> Per `D-009`, no figure here is a target and no parameter was tuned toward one.

---

## 9. TO RUN THIS

```bash
python3 06_MANUAL_BACKTEST/V09/run_pt035.py
```

Writes `06_MANUAL_BACKTEST/V09/data/pt035_output.txt` and `pt035_results.json`. The observation
is recorded in `06_MANUAL_BACKTEST/V09/BT_V09_0001.md`.

**`COMMON_PROTOCOL.md` §9 rule 7 applies: once this file is committed it is NOT edited to match
what the runner returns.** A defect found in the pre-registration is disclosed in the observation
and, if it needs fixing, fixed by issuing a new `PT` number.
