# PT-036 — V10's two quantitative structure claims: the **600–1000 pip week** and the **Friday close 25–50 pips off both extremes**

```text
STATUS:   PRE-REGISTERED. NOT RUN.
DATE:     2026-08-13
LESSON:   V10 -- Bootcamp1 Wk3 040112 (96mins).swf
          SHA-256 a37ba371ca2d5c807553c7b9a827a91c479509dd5223b64eadf85995481a3de1
SPEAKER:  the COURSE AUTHOR, 100% of runtime (D-033 makes this immaterial to
          weight; recorded because provenance is owed)

THIS FILE IS COMMITTED BEFORE THE RUNNER EXISTS AND BEFORE ANY BAR IS READ.
No price, statistic, count or distribution from W-C' has been examined by the
session writing it. The predictions in §6 are committed in the same commit as
the design, and the runner is a SEPARATE, LATER commit (D-026, D-027,
BACKTEST_EVIDENCE_STANDARD.md; the PT-035 / BT_V09_0001 precedent).
```

## 0. NUMBERING

`PT-036` is the next free number: `PT-001` … `PT-035` exist, `PT-035` being V09's.
Allocated against the **integration branch** state after this session's merge, per `D-038a`
consequence 1.

---

## 1. THE CLAIMS UNDER TEST

Both are **quantitative, explicit, spoken by the course author, and measurable from OHLC alone.**
Neither requires a single term the course has left undefined — which is why these two were chosen
and V10's headline trade was not (see §2).

### `M1` — the weekly range

> `[00:14:09]`–`[00:14:17]` — *"It means peak formation high to peak formation low **600 to 1000
> pips** is the range"*
>
> `[00:14:38]` — *"The range is about **a thousand pips a week**, but the dealer should come off
> that number and end back below that"*

**Two qualifiers the speaker attaches, carried into the test rather than dropped** (`E03`):

- `[00:14:26]`–`[00:14:35]` — the upper end is attributed to **crosses**: *"why 1000 pips you got
  [to] account for pairs like GJ, G[C] … those big cross pairs that move a lot so ADRs are a little
  higher"*. **GBP/USD is a major, so the claim's own logic puts it at the LOWER end of the band —
  i.e. nearer 600 than 1000.** This makes the test *more* favourable to the claim, not less, and it
  is stated here so the favourable reading is the one on trial.
- `[00:14:43]` — *"unless he's shifting the zone or something else is going on"*. An exception with
  no stated trigger; **it cannot be operationalised and is therefore NOT used to exclude any week.**
  Recorded so that a later session cannot invoke it retroactively to rescue a failed test — that
  would be `E09`.

### `M2` — the Friday close

> `[00:13:41]`–`[00:13:52]` — *"the dealer will end **always** 25 to 50 pips off of the high **and**
> 25 to 50 pips off of the low, the reason for this is simple: to trap the traders going into the
> weekend and hit them with the gap"*

Context, `[00:13:03]`–`[00:13:28]`: the question is about **Friday**, about the **ADR**, and the
answer is that price returns to *"about mid range"*, *"your 50% fib"*.

**The word *"always"* is the speaker's own and is quoted, not softened.** `M2` is scored against it.

---

## 2. WHAT THIS TEST DELIBERATELY DOES **NOT** TEST, AND WHY

**V10's headline contribution is the SAFETY TRADE, and it is NOT tested here.**

`V10_INTERPRETATION.md` Q6 counts its conditions: **two of seven are codable today.** The other
five rest on `blue box` (`A-076`), the lock threshold (`A-077`), `second leg` (`A-007`),
`consolidation`, and `the level` (`A-004`). **`D-030` forbids approximating any of them**, and the
hazard is specific and severe: the safety trade's anchor is defined **retrospectively** as the
week's extreme (`[01:14:06]`, `A-010`), so a naive backtest would use the *actual* weekly extreme
and thereby commit **lookahead bias** (`E08`) — producing a flattering number whose caveat would not
survive being quoted twice.

**Not testing it is the finding.** It is reported in `BT_V10_0001` §1 and in the mastery report's
dimension G with equal prominence to anything that *is* measured, per
`BACKTEST_EVIDENCE_STANDARD.md` §4.3 and `E25`.

### ⭐ A SECOND, DELIBERATE DESIGN CHOICE — THE `open item 80` CENSORING BIAS IS DESIGNED OUT

`REVIEW_INDEX.md` open item **80** escalates a resolution/censoring bias found in V09's backtest: a
**day-end horizon censors a far target more often than a near stop**, biasing an estimated hit rate
downward, and it *"may affect other tests in the `PT-002`…`PT-032` family sharing that geometry."*

**`PT-036` has that geometry nowhere in it, and this is by design rather than by luck.**

| Property of the item-80 bias | `PT-036` |
|---|---|
| Requires a **barrier race** (target vs stop) | **No barrier of any kind.** `M1` is a range statistic; `M2` is a position statistic |
| Requires an **asymmetric horizon** that can expire | **No horizon.** Both measures are evaluated on a **completed** week / completed Friday session |
| Produces **unresolved / censored** observations | **Zero possible.** Every completed week has a high, a low and a Friday close. `n_resolved == n` by construction |
| Estimand is a **hit rate under censoring** | Estimands are a **range in pips** and a **distance in pips** — directly observed, not inferred from a race |

**This is asserted as a property of the design and is also CHECKED at run time**: the runner asserts
that no observation is dropped for non-resolution, and `BT_V10_0001` reports the count of censored
observations, which must be **0**. If it is not 0, the test is **VOID** (§7b).

---

## 3. THE PRE-REGISTERED OBSERVABLES

### `O1` — `M1`: the distribution of the weekly high-to-low range, in pips

For every usable week in `W-C'`: `range_pips = (week_high − week_low) / 0.0001`.

Reported: **n**, median, mean, 5th/25th/75th/95th percentiles, min, max, **and the proportion
falling inside `[600, 1000]`** with a **bootstrap 95% CI** (10,000 resamples, seed recorded).

**`peak formation high/low` is operationalised as the week's extreme on V10's own definition**
(`[01:13:58]`–`[01:14:06]`, `A-010`) — *"the highest point on a chart within the week, or the lowest
point on the chart within the week."* **This is the course's definition, not the agent's**, which is
what makes `M1` testable at all under `D-030`.

### `O2` — `M1` scale diagnostic: the factor by which the claim misses, if it misses

`median_observed / 800` (the band's midpoint), and the **percentile of the observed distribution at
which 600 pips sits**.

**Why this is pre-registered rather than added afterwards.** If `M1` fails, the *interesting*
question is immediately *"by how much, and is it a unit error?"* A well-known candidate is
**pip vs. point on a 5-digit feed** (600 "points" = 60 pips). **Fixing the diagnostic in advance
stops it becoming a post-hoc rescue**: `O2` is reported whatever the result, and it **does not
change `M1`'s verdict** under any outcome (§6).

### `O3` — `M2a`: the Friday close's distance from Friday's high and from Friday's low

For every usable week's **Friday session**: `d_high = (F_high − F_close)/0.0001` and
`d_low = (F_close − F_low)/0.0001`, both ≥ 0 by construction.

Reported: the **joint** proportion satisfying `25 ≤ d_high ≤ 50` **AND** `25 ≤ d_low ≤ 50` — the
claim as stated — with a bootstrap 95% CI; plus each marginal separately; plus the medians.

### `O4` — `M2b`: the derived range implication — **LABELLED AS DERIVED, NOT AS THE INSTRUCTOR'S**

If `M2a` holds then Friday's range is arithmetically confined to **50–100 pips**. Reported: the
proportion of Fridays with `range ∈ [50, 100]`, and the median Friday range.

> **This inference is the agent's, not the lesson's** (`V10_INTERPRETATION.md` Q2). It is reported
> in its own row, under its own heading, and **`M2`'s verdict is taken from `O3` alone.** `O4` is
> diagnostic colour. Attributing it to the instructor would be `E01`/`E02`.

### `O5` — `M2` specificity: **is Friday actually different from Monday–Thursday?**

The same close-position measurement on **each weekday**, reported as a 5-row table.

**This is the measure that decides whether `M2` says anything about *Friday*.** The claim's stated
mechanism is weekend-specific — *"to trap the traders going into the weekend and hit them with the
gap."* If Monday through Thursday behave the same, then whatever `M2a` finds is a fact about **daily
closes in general**, not about Friday, and the mechanism is unsupported **even if the numbers land
inside the band.**

---

## 4. THE NULLS — `D-026`, `D-029`

`D-026`'s named default is *matched random entry*, which is the correct control for a **rule that
takes trades**. **`PT-036` takes no trades**, so a random-entry baseline would be a control for a
quantity this test does not estimate. The **matched controls for a distributional claim** are used
instead, following the `PT-028` precedent in this same batch (exposure-weighted null for a
weekday-distribution claim, not random entry).

**Stated plainly so it is not read as an evasion: this test's nulls are LISTED HERE, IN ADVANCE, and
each is a genuine comparator that the claim could fail against.**

### `N1` — the empirical distribution with interval, for `M1`

The observed weekly-range distribution itself, with bootstrap CIs. A range claim is falsified or
confirmed **directly** by where the distribution sits; there is no latent parameter to control for.
`n ≥ 30` is satisfied by construction (≈180 weeks) — `E24` labelling is nonetheless applied to any
sub-cell that falls below 30.

### `N2` — the uniform-close null, for `M2`

If Friday's close were **uniformly distributed within Friday's own high–low range**, what proportion
would land 25–50 pips from **both** extremes? Computed **analytically per Friday from that Friday's
realised range** — so the null is *matched* on the day's own volatility, which is the confound that
would otherwise drive the result. Reported alongside `O3`.

**This is the null that matters**: a wide Friday cannot satisfy `M2a` at all, and a 75-pip Friday
satisfies it almost automatically. `N2` removes exactly that artifact.

### `N3` — the weekday control, for `M2`

`O5` doubles as the null for Friday-specificity. **Mon–Thu are the matched comparison group**: same
instrument, same corpus, same measurement, differing only in the variable the claim names.

### `N4` — a shifted-boundary sanity control, for `M1`

The week roster rebuilt on a boundary shifted by **+24 h** (Monday 17:00 anchors), via
`mmm_week.weeks_from_offset`. If the 600–1000 pip claim is a real property of *the dealer's week*
rather than an artifact of any arbitrary 5-day window, the two rosters should differ. **If they are
indistinguishable, `M1` is measuring "how far GBP/USD travels in five days" and not anything about
week structure** — which is reported as such.

**Seed for every bootstrap and every shuffle: `20260813`. Iterations: 10,000.** Recorded here, before
the run, per `D-029`.

---

## 5. CELLS — TWO `D-031` ARMS, BOTH ALWAYS REPORTED

| Arm | Clock | Week open |
|---|---|---|
| **A** | corpus stamps verbatim, fixed UTC−5, no DST | Sunday 17:00 local = 22:00 UTC |
| **B** | `America/New_York`, DST active (stamp +1 h in US DST) | Sunday 17:00/18:00 local, same physical instant |

**`D-031` binding rule: BOTH arms are reported for every observable, every time. Divergence is a
finding; reporting only the better arm is `E09` + `E24`.**

`M2`'s Friday session is delimited on the arm's own clock, so the arms genuinely differ for `M2`
(a one-hour shift moves the session boundary) and are near-identical for `M1` (the week span is one
physical instant relabelled — `mmm_week` module docstring). **That asymmetry is predicted here, in
advance**, so that near-identical `M1` arms are not later presented as a robustness result.

---

## 6. THE DECISION RULE — FIXED NOW, BEFORE ANY NUMBER EXISTS

| Measure | `CONFIRMED AS STATED` | `PARTIALLY SUPPORTED` | `CONTRADICTED AS STATED` |
|---|---|---|---|
| **`M1`** | ≥ 50% of usable weeks have range ∈ [600, 1000] | 20–50% | **< 20%** |
| **`M2a`** | ≥ 50% of Fridays satisfy the joint 25–50 band | 20–50% | **< 20%** |
| **`M2` specificity** | Friday's joint rate exceeds every Mon–Thu rate by ≥ 10 percentage points | exceeds some | **does not exceed the Mon–Thu maximum** |

**The word *"always"* in `M2` deserves a comment made now rather than after the fact.** A literal
reading sets the bar at 100% and would be trivially contradicted by one exception, which is a
strawman. **The 50% threshold above is deliberately generous to the claim** and is the number this
test is scored on. **The literal reading is ALSO reported** — the exact proportion — so a reader can
apply the strict standard themselves.

**Thresholds are fixed here and may not be moved after the numbers are seen.** Moving one is `E09`.

### 6a. THIS SESSION'S PREDICTIONS, COMMITTED BEFORE THE RUN

Written before any bar of `W-C'` was read by this session, and committed in this file.

| # | Prediction | Confidence | Reasoning |
|---|---|---|---|
| **P1** | **`M1` is CONTRADICTED AS STATED**, with < 5% of weeks in [600, 1000] | **High** | GBP/USD weekly ranges in 2013–2016 are, to my prior knowledge of the instrument, typically 150–350 pips. 600 is roughly double a *large* week |
| **P2** | `O2`'s median-to-800 factor lands between **0.15 and 0.40** — i.e. the claim overshoots by roughly **2.5× to 7×** | Medium | Follows from P1's magnitude estimate; stated numerically so it can be WRONG |
| **P3** | **`M2a` is CONTRADICTED AS STATED**, < 20% joint | Medium-high | The joint band requires Friday's range to be 50–100 pips. Typical GBP/USD Friday ranges are wider, and a close 25–50 from *both* extremes is a narrow target |
| **P4** | **`M2` FAILS the specificity test** — Friday will not exceed the Mon–Thu maximum by 10pp | Medium | I know of no mechanism that would make Friday's *close position within its own range* differ much from other days, notwithstanding the weekend-gap rationale |
| **P5** | `N2`'s uniform-close null lands **close to** the observed `M2a` rate (within 10pp) | Medium | If true, `M2a` carries little information beyond Friday's range width |
| **P6** | `N4`'s shifted roster is **NOT** distinguishable from the true roster on `M1` | Medium-low | Stated as the prediction I am least confident in; a real week structure would falsify it |
| **P7** | The two `D-031` arms differ **negligibly on `M1`** and **detectably on `M2`** | High | Structural, per §5 — a near-free prediction, and it is labelled as such rather than banked as a success |

**P7 is flagged as cheap on purpose.** A prediction tally that includes a structural certainty
alongside genuine forecasts inflates itself; `BT_V10_0001` reports P7 separately from P1–P6.

---

## 7. WINDOW, HOLDOUT, DATA — `D-027`, `D-028`, `D-035`, `D-036a`

| Field | Value |
|---|---|
| Instrument | **GBP/USD** (`D-007`) |
| Window | **`W-C'` = 2013-01-06 → 2016-06-30** — `D-035`'s DEVELOPMENT block **exactly** |
| Holdout | **2016-07-01 → 2017-12-29 — NOT OPENED.** Cannot be: it is not on disk (`D-036a` truncated on arrival) |
| Timeframe | **M15**, aggregated locally from M1 by `aggregate_m15.py` |
| Source | **HistData.com M1 CSV corpus** (`D-036a`), SHA-256 recorded in `raw/SHA256SUMS.txt` |
| Week open | **Sunday 17:00 local, fixed UTC−5 = 22:00 UTC** — HistData's, **NOT** FXCM's 21:00 UTC |
| Week rule | **A week is delimited by its Sunday 17:00 open; an intra-week holiday re-open is NEVER a week boundary.** Never derived from `C7`'s open list |
| QA gate | `qa_histdata_m1.py` → `QA_REPORT.txt` is a **precondition on the run** and is cited in `BT_V10_0001` |
| Level comparability | **Price LEVELS are not comparable with V02–V06 FXCM homework** (`D-036a`). Only **shape and distance** claims travel. **`M1` and `M2` are both distance claims, so this test is unaffected** — stated because it is the rare case where the limitation does not bite |

### 7a. `C8` DISPOSITIONS — PRE-REGISTERED BY NAME

The QA gate requires an explicit, pre-registered disposition for every `C8`-flagged session.
**These are INHERITED from the batch convention, not newly chosen**, because re-deciding them after
a check surfaced them is the suit-the-result move the gate exists to prevent.

| Session / week | Disposition | Reason |
|---|---|---|
| **week of 2014-06-01** (the ~22 h data hole) | **EXCLUDE by name** | The corpus does not contain what the market did. **This is a data-integrity exclusion, not an `E09` convenience one** — the distinction `C8` was written to make |
| 2013-01-01, 2013-12-25, 2014-01-01, 2014-12-24/25, 2015-01-01, 2015-12-24/25, 2016-01-01 (six Dec/Jan closure weeks) | **INCLUDE, report separately** | Holiday closures are **real market behaviour**. `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation as unrepresentative |
| **week of 2016-06-26** (truncated by the DEVELOPMENT boundary) | **EXCLUDE** | Cut by a non-market event — the `D-035` pin. It has no Friday, so `M2` is undefined for it and `M1` would measure a partial week |
| The three **Thursday-closing** weeks (2015-12-20, 2015-12-27, 2016-06-26) | **`M1` INCLUDE; `M2` EXCLUDE, reported by name** | `M2` is a claim about **Friday**. A week with no Friday session cannot test it. **Excluding them from `M2` is required by the claim's own terms, and the count is reported beside `n`** |

**Every reported `n` carries its exclusion count beside it**, per the `D-036a` binding consequence.

**Expected `n` before the run** (calendar arithmetic only, no price read): **≈180 trading weeks** for
`M1`; **≈178** Fridays for `M2` after the Thursday-closing exclusions. **The realised numbers are
reported as realised**, not rounded to these.

### 7b. WHAT WOULD MAKE THIS TEST VOID

Stated in advance so it cannot be negotiated afterwards:

1. **Any censored or unresolved observation.** §2 asserts the design admits none. If the runner
   reports `censored > 0`, the design claim is false and **both measures are VOID**, not merely
   weakened.
2. **A holiday re-open in the week roster.** `mmm_week.build_weeks` asserts this; if the assertion
   fires, every number is wrong.
3. **Any bar outside `W-C'`.** `assert_development` fires per slice.
4. **A `QA_REPORT.txt` that does not gate clean on C1–C4.**
5. **Fewer than 30 usable weeks** in any cell whose rate is quoted without the
   `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` label (`E24`).

---

## 8. MANDATORY SCOPE STATEMENT

**What a result here does and does not license** — the `PT-001` §7 form.

- The speaker is the **course author**. Under `D-033` his material is normative, so unlike the V05–V09 guest tests **no speaker-based fence applies**. This is the first `PT` in the corpus for which that is true without qualification.
- **A CONTRADICTION of `M1` or `M2` is a finding about a stated NUMBER, not about the method.** The safety trade is untested here (§2) and nothing in this file bears on whether it works.
- **A CONFIRMATION would not validate the method either.** It would say a descriptive figure about GBP/USD holds in 2013–2016.
- **Results are GBP/USD-specific.** `M1`'s own qualifier attributes the upper band to crosses; **this test cannot speak to GJ or GC at all**, and no result here may be generalised to them.
- **Price levels are not comparable with V02–V06 homework** (`D-036a`). Distances are.
- **The window is 2013–2016; the lesson was recorded in 2012.** The corpus does not reach 2012 at any usable resolution. **This is a real external-validity limit and it is stated before the result, not after.**

---

## 9. TO RUN THIS

```bash
python3 06_MANUAL_BACKTEST/scripts/run_pt036.py \
  > 06_MANUAL_BACKTEST/V10/data/pt036_output.txt
```

The runner is committed **separately and after this file**, and its output is committed after that.
`COMMON_PROTOCOL.md` §9 rule 7 applies: **if the runner and this pre-registration disagree, the
pre-registration governs and neither is edited** — the disagreement is reported in `BT_V10_0001`.
That rule has already fired twice in this project (`BT_V08_0001`, `BT_V09_0001`), both times against
the runner.
