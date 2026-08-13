# PT-034 — "Risk Reward to 3:1 or greater": the arithmetic half is guaranteed, the empirical half is not

> **WRITTEN AND COMMITTED BEFORE ANY BAR IN THE WINDOW WAS READ BY THIS SESSION.**
> No chart was opened, no aggregate computed, and no row of the corpus parsed for this test
> before this file existed in Git. The runner is written **after** this file is committed, and
> it prints the nulls before the rule arm (`COMMON_PROTOCOL.md` §9 rule 1).

**Governed by:** `COMMON_PROTOCOL.md` (all sections), `D-005`, `D-007`, `D-010`, `D-026`,
`D-027`, `D-028`, `D-029`, `D-030`, `D-031`, `D-033`, `D-034`, `D-035`, `D-036`, `D-036a`.

---

## 0. NUMBERING

`PT-033` is the highest number in `PRE_REGISTERED/` at the moment of writing, verified by
re-listing the directory immediately before this file was created. This file takes **`PT-034`**.
If a collision is ever found with a concurrently-authored test, **this file is the one that
renames** — it is cited from no decision entry.

---

## 1. THE CLAIM UNDER TEST

**Source: V08, `[00:39:53]`–`[00:39:58]`. Speaker: `GUEST` — V08 carries zero course-author
runtime. Under `D-033` this is NORMATIVE evidence at equal weight.**

> *"This high low drill becomes the **crown jewel of the method** as one can **enter even tighter
> stops** thus bringing **risk we reward to three to one or greater**."*

**It is also printed**, which raises its weight — frame
`04_SCREENSHOTS/V08/V08_00-40-10_high-low-drill-crown-jewel-3-to-1.png`:

> *"Becomes the Crown Jewel of the Method as one can enter even Tighter Stops thus bringing
> **Risk Reward to 3:1 or greater!**"*

### The two numbers the claim needs, both supplied by the lesson

| Parameter | Value | Source |
|---|---|---|
| **Target** | **50 pips** | V08's own exit, stated 8× as the literal phrase *"Easy 50"* and closed at `[00:34:58]` *"We get our 50 on our next cycle up and bang 50"* |
| **Entry tolerance** | **10 pips from HOD/LOD** | **printed**, frame `V08_00-05-40`: *"The High Low Drill and Elements of Mastery for dealing **within 10 pips of HOD/LOD**"*. The audio never states a tolerance — `[00:05:35]` renders it *"with intent pips"*, which is the ASR's rendering of *in ten pips* |
| **Implied stop** | **50 ÷ 3 = 16.67 pips** | **`IMPLIED`, not stated.** Marked as arithmetic from his ratio and his target everywhere it is used |

### Why this test exists and is not a repeat of `PT-033`

`PT-033` §3 recorded, in its own words:

> *"**No stop.** The claim contains none, V07 states none, and inventing one would be `D-010`."*

**V08 supplies the missing half.** It states a ratio, so the stop is arithmetic rather than
invented; and it prints a tolerance, so `X` is the lesson's number rather than a grid this
project chose. Those are the only two things `PT-033` said it could not have.

| | `PT-033` (V07) | `PT-034` (V08) |
|---|---|---|
| Target | 50 pips | 50 pips |
| Stop | **none available** | **16.67 pips**, `IMPLIED` from *"three to one"* |
| Tolerance `X` | grid `{0,2,5,10}` **chosen by the session** | **10 pips, printed by the lesson** |
| Question | can 50 pips be reached from the day's extreme at all? | **does the 3:1 geometry survive, and does the extreme entry earn it?** |

---

## 2. THE PRIMARY FINDING IS AVAILABLE BEFORE THE DATA IS READ, AND IS STATED HERE SO IT CANNOT BE PRESENTED AS A DISCOVERY

This section is the most important in the file. **It is written before the run, deliberately, so
that a result which is true by arithmetic can never be reported as though the data established
it.**

> **Let `d` be a trading day and `LOD(d)` its lowest bar low. An entry taken at a price within
> `X` pips of `LOD(d)`, held with a within-day horizon, has maximum adverse excursion
> `MAE ≤ X` — BY CONSTRUCTION, because `LOD(d)` is the day's minimum and price cannot go below
> it inside the day.** Symmetrically for `HOD(d)` and shorts.

Three consequences follow immediately, and none of them is empirical:

1. **At the lesson's own tolerance `X = 10`, realised `R = 50 / MAE ≥ 5.0`** whenever the target
   is reached. The claimed 3:1 is exceeded by a wide margin.
2. **The 3:1 claim cannot fail within the day for any `X ≤ 16.67` pips.** The implied stop is
   unreachable.
3. **Therefore, read literally with a within-day horizon, "Risk Reward to 3:1 or greater" carries
   no information about the market.** It is a restatement of *if you enter near the low, your
   stop is near the entry* — which is true of any instrument, in any regime, in any century.

**This is a real finding and it is a negative one.** The lesson's single performance number, its
"crown jewel", is **arithmetically guaranteed rather than empirically earned**, in the form it is
stated. No run is required to establish that, and this file establishes it before any run.

### 2a. What therefore remains genuinely empirical — the whole point of the design below

| Question | Why it is not tautological |
|---|---|
| **Is the 50-pip target reached at all?** | Nothing guarantees a day's range extends 50 pips past its own extreme |
| **How much of the available tolerance does the trade actually give back?** | `MAE ≤ X` is a bound, not a value. Whether realised `MAE` sits near `X` or near zero is a fact about price behaviour at daily extremes, and it is unknown |
| **Does the geometry survive without the day's floor under it?** | Remove the within-day horizon and `LOD(d)` stops protecting the position. **This is the only arm in which the claim can fail**, and it is the decision arm |
| **Does entering at the extreme EARN the geometry, or would any entry do?** | The matched-random null answers this and nothing else does |

---

## 3. THE FOUR PRE-REGISTERED OBSERVABLES

Let a **trading day** be a contiguous block of 15-minute bars under a declared day boundary (§5).
`HOD(d)` = max of the day's bar highs; `LOD(d)` = min of the day's bar lows. `1 pip = 0.0001`.

**Entry rule, fixed here.** For tolerance `X`, the entry is the **first bar of the day whose low
is within `X` pips of `LOD(d)`** (long) or **whose high is within `X` pips of `HOD(d)`** (short).
The entry price is `LOD(d) + X` pips (long) / `HOD(d) − X` pips (short) **when that price is
inside the entry bar's range**, else the entry bar's low (long) / high (short). *This is the
conservative choice — it never assumes a fill better than the bar allows — and it is fixed
before any run.*

**The entry bar is excluded from every subsequent scan** (target, stop and MAE), as in `PT-033`.

### `O1` — THE ARITHMETIC BOUND, REPORTED AS A CHECK ON THE RUNNER

Report the fraction of observations with `MAE > X`. **The pre-registered expectation is exactly
zero.** This is not a finding; it is a **self-test of the pipeline**. A non-zero count means the
day-slicing or the entry rule is wrong, and the run is void rather than interesting.

### `O2` — HOW MUCH OF THE TOLERANCE IS ACTUALLY GIVEN BACK

For the pre-registered tolerance grid

```text
X ∈ {0, 2, 5, 10}      -- 10 is the LESSON'S number and is the HEADLINE cell
```

report, per `X`, over all observations:

- the distribution of realised `MAE` (median, quartiles, 5–95%),
- **`MAE / X`**, the fraction of the available give-back actually used,
- the fraction with `MAE = 0` (price never traded against the entry at all),
- and, among target-reaching observations only, the realised **`R = 50 / MAE`** distribution,
  with `MAE = 0` reported as a **separate count** rather than as an infinite `R`.

**No `X` is selected on the results.** The whole grid is reported and `X = 10` is the headline
because the lesson prints it.

### `O3` — IS THE TARGET REACHED, WITHIN THE DAY

The `PT-033`-comparable arm. Per `X`, per direction and pooled: the fraction of observations
whose target (`entry ± 50` pips) is reached by a **subsequent** bar before the day ends, and
`f50_day`, the fraction of days on which at least one of the two directions reached target.

> **`PT-033` published this quantity for V07 on the same corpus and the same window.** At `X = 10`
> under matching cells, **`PT-034` must reproduce it.** A disagreement is a defect in one of the
> two runners, not a finding, and this file pre-commits to reporting the comparison **whichever
> way it comes out**.

### `O4` — THE DECISION ARM: THE GEOMETRY WITHOUT THE DAY'S FLOOR

**No deadline.** From the entry bar (exclusive), scan forward through the corpus until **either**
`entry ± 50` pips (target) **or** `entry ∓ 16.67` pips (the implied stop) is touched, whichever
comes first within a bar being resolved **stop-first** when a single bar spans both — the
conservative convention, fixed here.

Report: `TARGET` / `STOP` / `UNRESOLVED at end of corpus` counts, the target-before-stop rate with
a Wilson 95% interval, and the distribution of **bars to resolution**.

**"No deadline" is not an invented parameter — it is the absence of one.** V08 states no holding
period. Its only timing remark is `[00:34:49]` *"We achieved an amount of profit past our
**two-hour mark** where we can say we can hold this trade"*, which is a **hold** rule, not a
deadline, and `PT-018` already owns the two-hour object from V04. Censoring at the end of the
corpus is reported, not hidden.

---

## 4. THE NULLS

| ID | Null | Held constant | Randomized |
|---|---|---|---|
| **N1** | **Matched random entry** — `D-026`'s required form | instrument, day, eligible bars, target (50 pips), stop (16.67 pips), horizon rule, direction, and `n` | the entry bar, drawn uniformly from the day's bars excluding the last |
| **N1b** | **Matched random entry, random direction** — `D-029`'s secondary arm | as `N1` | entry bar **and** direction |

Fixed, per `COMMON_PROTOCOL.md` §5 and `D-029`:

| Parameter | Value |
|---|---|
| Iterations | **1,000** |
| Seed | **`20260813`** — pre-registered here so seed-shopping is impossible |
| Order | **Nulls computed and printed BEFORE the rule arm's aggregate** (`COMMON_PROTOCOL.md` §9 rule 1) |
| Reported | median, 5–95% range, iterations, seed, and the rule arm's percentile within the distribution |

> ### ⚠ WHAT `N1` IS FOR HERE, AND WHAT IT IS NOT — READ BEFORE QUOTING ANY PERCENTILE
>
> **The rule arm uses hindsight: it knows where the day's extreme is. It is therefore expected to
> beat `N1`, and a high percentile is not evidence the claim is correct.** `N1` is run to size
> **the gap between a perfect extreme entry and an arbitrary one** — which is the value of the
> skill V07 named, V08 partially describes, and neither teaches.
>
> **`N1` is nevertheless the decision arm's second condition**, and that is a deliberate,
> pre-registered choice: if a random entry with the same 50/16.67 geometry resolves to target at
> the same rate as an entry at the day's extreme, then the *"crown jewel"* is the **geometry**,
> not the **drill** — and the lesson attributes it to the drill. That is a falsifiable reading of
> the claim and it is why `N1` appears in §6 rather than only in the commentary.

**`N2` / `N3` are not run.** This test asks about a within-day extreme; a circular clock shift
would destroy the day whose extreme is the subject. Same reasoning `PT-033` recorded.

---

## 5. CELLS — TWO DAY DEFINITIONS × TWO `D-031` ARMS, ALL FOUR ALWAYS REPORTED

*"The day"* is not defined in V08. Rather than choose — which would be `D-010` — both are run:

| Day def | Boundary | Why a candidate |
|---|---|---|
| **`D-SESSION`** | **17:00 → 17:00 local** | The corpus's own session day (`D-036a`: 170 of 181 week opens at exactly 17:00, fixed year-round). It is also the day an MT4 `Pips To HOD` indicator computes — and V07's frames print exactly that indicator |
| **`D-MIDNIGHT`** | **00:00 → 00:00 local** | The calendar day |

| `D-031` arm | Definition | File |
|---|---|---|
| **A** | fixed `UTC−5`, no DST | `GBPUSD_M15_ARMA.csv` — corpus stamps verbatim (natively Arm A) |
| **B** | `America/New_York` with DST | `GBPUSD_M15_ARMB.csv` — Arm A **+1 h** during US DST |

**Divergence between cells is a FINDING, never a selection criterion** (`D-031`; reporting only
the favourable cell is `E09` + `E24`).

> **`COURSE_PROGRESS.md`'s V07 GATE carry-forward item (c) is directly relevant and is honoured
> here.** `PT-033` found the **day boundary** moved its result by ~14 points while the `D-031`
> timezone arm moved it by ~0 — and the project has a standing two-arm rule for the timezone and
> **none** for the day. `PT-034` therefore carries both day definitions as first-class cells and
> **reports the day-boundary spread explicitly as a headline number**, so a second lesson's worth
> of evidence accumulates for the decision the owner has been asked to make.

---

## 6. THE DECISION RULE — FIXED NOW, BEFORE ANY NUMBER EXISTS

Judged on **`O4` at `X = 10`** (the lesson's own tolerance), across **all four cells**.

The break-even hit rate for a 3:1 payoff is **25%**. That is the arithmetic the claim's own
numbers imply, and it is the bar the claim has to clear to be worth stating.

| Verdict | Condition |
|---|---|
| **`CONFIRMED AS TAUGHT`** | target-before-stop rate **≥ 0.25** in all four cells **AND** the rule arm sits **above `N1`'s 95th percentile** in all four |
| **`CONTRADICTED AS TAUGHT`** | rate **< 0.25** in all four cells |
| **`OVERSTATED`** | rate ≥ 0.25 in all four cells, but the rule arm is **not distinguishable from `N1`** in one or more — the 3:1 geometry is real and available to **any** entry, so it is not the drill's crown jewel |
| **`INDETERMINATE`** | the cells disagree across the 0.25 boundary |

**Conjunctive across cells, deliberately**: a verdict that holds in one cell and not another is a
selection, not a verdict.

**Whatever `O4` returns, §2's arithmetic result stands and is reported first**: within the day,
the 3:1 claim is guaranteed and therefore empty. `O4` tests the version of the claim that is not
empty. **Both are reported, in that order, with equal prominence** (`BACKTEST_EVIDENCE_STANDARD.md`
§4.3).

### 6a. THIS SESSION'S PREDICTION, RECORDED BEFORE THE RUN

**I predict `OVERSTATED`.**

Specifically: **`O4` target-before-stop rate between 0.30 and 0.55**, comfortably above the 0.25
break-even; and **the rule arm above `N1`'s 95th percentile in all four cells** — which, if it
happens, would make the verdict `CONFIRMED` rather than `OVERSTATED`, so **I am predicting the
verdict and the components inconsistently on purpose and must be scored on the components.**

Stating that plainly, because it is the part a later reader should check: I expect the extreme
entry to **beat** random (hindsight is a real advantage and `PT-033` measured one), while
believing the *claim as taught* is still overstated — because §2 shows the headline number is
arithmetic, and because a 16.67-pip stop with no deadline on GBP/USD is a small stop that daily
noise should take out often. **If both components come in as predicted the rule returns
`CONFIRMED AS TAUGHT`, and my verbal prediction of `OVERSTATED` was wrong.** The decision table
governs, not my sentence.

For `O2` I predict **median `MAE / X` above 0.5 at `X = 10`** — i.e. a trade entered 10 pips off
the low typically gives back most of those 10 pips, because the entry bar is by construction near
a turning point that has not finished turning.

For `O3` I predict **agreement with `PT-033` to within rounding** at `X = 10`.

**If `O4` comes back below 0.25 I was wrong, and this file says so in advance.**

---

## 7. WINDOW, HOLDOUT, DATA

| Field | Value |
|---|---|
| Instrument | **GBP/USD** (`D-007`) |
| Window | **2013-01-06 → 2016-06-30** — the `W-C′` DEVELOPMENT window (`COMMON_PROTOCOL.md` §3a) |
| Timeframe | **15-minute** (`D-034`) |
| Source | **HistData.com M1 aggregated to M15** (`D-036a`), `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/` |
| Integrity | SHA-256 per raw file in `raw/SHA256SUMS.txt`; **the runner re-hashes the two M15 files it reads and prints the digests** |
| QA gate | `qa_histdata_m1.py` → `QA_REPORT.txt`, `C1`–`C4` **PASS**. **A precondition on this run, cited in the observation** |
| Holdout | **2016-07-01 → 2017-12-29** (`D-035`). **Never on disk** — truncated on arrival, untruncated copy deleted (`D-036a`). `E23` cannot occur |
| Measurement | **Numbers parsed from a checksummed file. Nothing measured off a rendering** (`E06` as restated by `D-036a`) |

**Level comparability, disclosed:** `D-036a` records the cross-vendor level offset as
**unmeasurable** for this window. **Price *levels* here are not comparable with V02–V06 FXCM
homework.** This test makes only **distance** claims — pips of excursion, pips to target — which
do travel.

### 7a. `C8` DISPOSITIONS — PRE-REGISTERED BY NAME, AS THE QA GATE REQUIRES

`QA_REPORT.txt` flags **11 sessions** and requires an explicit, pre-registered disposition for
each in any test whose window spans them. All 11 fall inside `W-C′`.

| Sessions | Disposition | Ground |
|---|---|---|
| `2013-01-01`, `2013-12-25`, `2014-01-01`, `2014-12-24`, `2014-12-25`, `2015-01-01`, `2015-12-24`, `2015-12-25`, `2016-01-01` — **nine Dec/Jan closures** | **INCLUDE, report separately** | These are **real market behaviour**, not defects. `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation as unrepresentative (`E09`), and `D-037` records this disposition as **inherited, not newly chosen** |
| `2014-06-01` (0 bars) and `2014-06-02` (521 of ~1440) — **the data hole** | **EXCLUDE BY NAME**, counted in every reported `n` | **The corpus does not contain what the market did.** `D-037` draws this line explicitly: `E09` forbids excluding an observation because of *what the market did*; this exclusion is because the data is *absent* |

**Mechanical drop rule, additional and stated before the run:** any day with fewer than **4**
15-minute bars under a given day definition is dropped, counted, and named in the report. Nothing
is dropped for its result.

**Every reported `n` carries its exclusion count beside it** (`D-036a` binding consequence).

### 7b. SAMPLE SUFFICIENCY, PRE-LABELLED

`W-C′` holds ~880 trading days, so `O3` and `O4` at the pooled level are far above
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's `n ≥ 30` floor. **Sub-cells that may fall below it** —
`MAE = 0` counts at small `X`, `UNRESOLVED` counts in `O4`, and any per-direction split inside a
single `X` — **are pre-labelled here** as
`SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` rather than negotiated after the number is
seen. Every rate carries a **Wilson 95% interval**.

---

## 8. MANDATORY SCOPE STATEMENT

Any report of this test carries this verbatim:

> **PT-034 measures a claim whose headline form is arithmetically guaranteed.** Within a trading
> day, an entry within `X` pips of that day's extreme cannot draw down more than `X`, so *"Risk
> Reward to 3:1 or greater"* is true by construction for any `X ≤ 16.67` pips and carries no
> information about the market as stated. The empirical arms measure what is left: whether the
> 50-pip target is reached, how much of the tolerance is given back, and whether the geometry
> survives once the day's floor is removed.
>
> **It is not a test of a tradable rule.** V08 describes where to enter (the extreme), where in
> the structure (the second leg, at a prior trap area) and what cues it (speed) — but *second
> leg* (`A-007`), *trap area* (`A-002`) and *fast* (`A-061`) are undefined, so no version of this
> test can be executed forward. The extreme is identified by **hindsight**. Any advantage over
> the matched-random null measures **the value of the missing skill**, and may never be quoted as
> evidence that the Hi-Lo claim is correct.
>
> Nothing here bears on any other V08 statement. `A-060`'s frequency claims remain blocked by
> `D-030` and are not touched by this test.

---

## 9. TO RUN THIS

```bash
python3 06_MANUAL_BACKTEST/V08/run_pt034.py
```

The runner:

1. re-hashes both M15 files and prints the digests,
2. asserts the whole window is inside DEVELOPMENT (`D-035`) and aborts otherwise,
3. builds the four cells (2 `D-031` arms × 2 day definitions),
4. applies the `C8` exclusions **by name** and prints the counts,
5. computes and **prints `N1` and `N1b` FIRST**,
6. then computes `O1`, `O2`, `O3`, `O4`,
7. writes raw results to `06_MANUAL_BACKTEST/V08/data/pt034_results.json`.

Seed `20260813` is fixed in the script. **This file is never edited to match what was found**
(`COMMON_PROTOCOL.md` §9 rule 7).
