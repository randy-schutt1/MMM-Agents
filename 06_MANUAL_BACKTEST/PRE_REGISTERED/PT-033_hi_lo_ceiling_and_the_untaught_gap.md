# PT-033 — "Hi-Lo": the ceiling of an entry at the day's extreme, and the size of the untaught gap

> **WRITTEN AND COMMITTED BEFORE ANY BAR IN THE WINDOW WAS READ.**
> No chart was opened, no aggregate was computed, and no row of the corpus inside the test
> window was parsed before this file existed in Git. The runner script is written **after**
> this file is committed, and it prints the nulls before the rule arm
> (`COMMON_PROTOCOL.md` §9 rule 1).

**Governed by:** `COMMON_PROTOCOL.md` (all sections), `D-005`, `D-007`, `D-026`, `D-027`,
`D-028`, `D-029`, `D-030`, `D-031`, `D-033`, `D-034`, `D-035`, `D-036`, `D-036a`.

---

## 0. NUMBERING NOTE — READ IT, BECAUSE THIS REPOSITORY HAD TWO SESSIONS RUNNING AT ONCE

`PT-025` … `PT-032` were created **by a different session, concurrently with this one**, as the
`D-035` re-issues of the seven `W-C` tests. This file takes **`PT-033`** after re-listing the
directory immediately before writing. If a collision is ever found, **this file is the one that
renames**, because the re-issue batch is cited from `D-035` and this one is not.

---

## 1. THE CLAIM UNDER TEST

**Source: V07, `[00:07:17]`. Speaker: `GUEST` — V07 carries zero course-author runtime.**

> *"If you can master high low and get in at the high of the day or the lower day within a few
> pips, you're going to make pips every day."*

Corroborating statements in the same lesson, all `GUEST`:

| Marker | Words |
|---|---|
| `[00:07:13]` | *"Can this be the holy grail of daily trading?"* |
| `[00:07:31]` | *"What other things can we confirm that with so that we can be sure we get in high low?"* |
| `[00:21:04]` | *"Coupling those entries now, the next level with high low entries to maximize your reward versus your risk is the next level to get you great graphs every time."* |
| printed, `V07_00-08-00` | slide bullet **"Hi-Lo — Can this be all I need?"** |
| printed, `V07_00-19-30` | *"Couple it with a Hi-Lo entry for smaller risk and maximum gain and you will have great trade grabs the majority of the time."* |
| printed, `V07_00-13-55` et al. | the chart panel prints **`Pips To HOD`** and **`Pips To LOD`** live |

**The exit used in the test is the lesson's own**, stated four times in speech and once in print:

| Marker | Words |
|---|---|
| `[00:13:45]` | *"Put it in right up to a nice 50."* |
| `[00:15:17]` | *"got in in the shadow box, got out for 50 over here"* |
| `[00:16:24]` | *"I tried to trail as opposed to getting out of 50."* |
| `[00:46:06]`–`[00:46:24]` | *"calculate at a very minimal basis, one trade, 50 pips"* |
| printed, `V07_00-19-15` | **"Exit +50 pips & 8.57% gain"** |

---

## 2. WHY THIS CLAIM AND NOT A BETTER-KNOWN ONE — THE `D-030` ARGUMENT

**`D-030` blocks almost everything else V07 says.** *Second leg* (`A-007`), *level* (`A-004`),
*M/W* (`A-011`), *railroad tracks*, *tilted* (`A-058`), *A pattern* (`A-057`), *shark fin*
(`A-032`) and TDI (`A-039`) are all named and undefined, so a test of any of them would measure
**this session's definition** and attribute the number to the course. That is the exact failure
`D-030` exists to prevent, and the drawdown claim at `[00:08:04]` — the most tempting target in
the lesson — dies on it.

**This claim survives, and the reason is precise:**

> *high of the day* and *low of the day* are **arithmetic** once a day boundary is fixed. They
> need no course definition. What V07 withholds is not the *definition* of the object but the
> *method of finding it in real time* — which it credits to "Jim" three times (`[00:07:38]`,
> `[00:21:16]`, `[00:38:26]`) and never teaches (`A-056`).

That asymmetry is the whole design of this test. **A rule whose target is computable but whose
method is missing has a measurable ceiling and an unmeasurable middle**, and reporting the
ceiling honestly is more useful than pretending the middle can be simulated.

### 2a. What this test therefore CANNOT do, stated before it runs

- It **cannot** show that Hi-Lo trading works, because the lesson supplies no way to identify
  the extreme in advance and this test does not invent one.
- It **cannot** show that Hi-Lo trading fails, for the same reason.
- A high ceiling is **not** a favourable result for the claim. It is the *precondition* for the
  claim being worth anything, and it is the arithmetic the claim's "every day" rests on.

---

## 3. THE THREE PRE-REGISTERED OBSERVABLES

Let a **trading day** be a contiguous block of 15-minute bars under a declared day boundary
(§5). For each day `d`:

- `HOD(d)` = max of the day's bar highs; `LOD(d)` = min of the day's bar lows.
- `RANGE(d)` = `HOD(d) − LOD(d)`, in pips (1 pip = 0.0001).

### `O1` — THE CEILING

The distribution of `RANGE(d)`, and the fraction of days with `RANGE(d) ≥ T` for the
**pre-registered grid**

```text
T ∈ {10, 20, 30, 40, 50, 60, 80, 100} pips
```

**No single `T` is selected.** `D-010` forbids inventing a threshold; the whole grid is reported
and the reader picks. `T = 50` is the one that matters for `O2` **because the lesson states 50**,
not because this session chose it.

### `O2` — THE 50-PIP TEST AT PERFECT HINDSIGHT

Two observations per day, taken as a pair and never selected between:

| Observation | Entry | Direction | Target | Deadline |
|---|---|---|---|---|
| `SHORT` | the bar that made `HOD(d)` | short | entry − 50 pips | end of day `d` |
| `LONG` | the bar that made `LOD(d)` | long | entry + 50 pips | end of day `d` |

- **The entry bar itself is excluded from the target scan** — the target must be reached by the
  low (short) or high (long) of a **subsequent** bar in the same day. This is the conservative
  choice and it is fixed here, before any run.
- **No stop.** The claim contains none, V07 states none, and inventing one would be `D-010`.
  The observation is binary: target reached before the day ends, or not.
- Reported: `f50` = fraction of observations reaching target, per direction and pooled; and
  `f50_day` = fraction of **days** on which at least one of the two reached target.

### `O3` — HOW FAST IT DEGRADES WITH IMPRECISION

*"within a few pips"* is the claim's own hedge, and it is not a number. Rather than pick one,
run `O2` again with entry at the **first** bar of the day whose high is within `X` pips of
`HOD(d)` (short) or whose low is within `X` pips of `LOD(d)` (long), for the pre-registered grid

```text
X ∈ {0, 2, 5, 10} pips
```

`X = 0` is `O2` restricted to the first touch of the exact extreme. **`O3` is still hindsight** —
it knows `HOD(d)` — and it measures only *tolerance*, never *foresight*.

---

## 4. THE NULLS

| ID | Null | Held constant | Randomized |
|---|---|---|---|
| **N1** | **Matched random entry** — `D-026`'s required form, `COMMON_PROTOCOL.md` §5 | instrument, day, eligible bars, target distance (50 pips), deadline (end of day), direction, and `n` | the entry bar, drawn uniformly from the day's bars excluding the last one |
| **N1b** | **Matched random entry, random direction** — `D-029`'s secondary arm | as N1 | entry bar **and** direction |

Fixed, per `COMMON_PROTOCOL.md` §5:

| Parameter | Value |
|---|---|
| Iterations | **1,000** |
| Seed | **`20260812`** — the batch constant. Pre-registered so seed-shopping is impossible |
| Order | **Nulls computed and printed before the rule arm's aggregate** (§9 rule 1) |

> ### ⚠ WHAT N1 IS FOR HERE, AND WHAT IT IS NOT — READ BEFORE QUOTING ANY PERCENTILE
>
> **The rule arm uses hindsight. It is therefore expected to beat N1, and a percentile of 100
> would be a tautology, not a finding.** N1 is run for one reason only: **to size the gap
> between what a perfect Hi-Lo entry buys and what an arbitrary entry buys.** That difference
> is the value of the skill V07 names and does not teach.
>
> **No report of this test may quote the rule arm's percentile within N1 as evidence that the
> Hi-Lo claim is supported.** Doing so would be `E24` and would be dishonest in a way that
> would be hard to catch later. Stated here, before the number exists.

**N2 / N3 are not run**, and the reason is on the record: this test does not ask whether a clock
or a week boundary carries information. It asks about a within-day extreme, and a circular clock
shift would destroy the day whose extreme is the subject.

---

## 5. THE TWO DAY DEFINITIONS, BOTH REPORTED

*"the day"* is not defined in V07. Rather than choose one — which would be `D-010` — the test
runs **both**, in the `D-031` spirit, and **both are always reported**:

| Day def | Boundary | Why it is a candidate |
|---|---|---|
| **`D-SESSION`** | **17:00 → 17:00 local** | The corpus's own session day. `D-036a` measured 172 of 187 week opens at exactly 17:00 local, fixed year-round. It is also the day an MT4 `Pips To HOD` indicator computes, and V07's frames print exactly that indicator |
| **`D-MIDNIGHT`** | **00:00 → 00:00 local** | The calendar day |

**Divergence between them is a finding, never a selection criterion.** Reporting only the more
favourable day definition is `E09` + `E24`, the same prohibition `D-031` places on its two arms.

## 5a. The `D-031` timezone arms

| Arm | Definition | File |
|---|---|---|
| **A** | fixed `UTC−5`, no DST | `GBPUSD_M15_ARMA.csv` — file timestamps **verbatim** (the corpus is natively Arm A, `D-036a`) |
| **B** | `America/New_York` with DST | `GBPUSD_M15_ARMB.csv` — Arm A **+1 h** during US DST |

**Both arms × both day definitions = four cells. All four are reported.**

---

## 6. THE DECISION RULE — FIXED NOW

The claim's operative words are *"you're going to make pips every day"*. Read at the ceiling:

| Verdict | Condition |
|---|---|
| **`CONFIRMED AS TAUGHT`** | `f50_day ≥ 0.95` in **all four** cells (both arms × both day definitions) at `X = 0` |
| **`CONTRADICTED AS TAUGHT`** | `f50_day < 0.50` in **all four** cells at `X = 0` |
| **`OVERSTATED`** | `f50_day` lands between, in any cell — i.e. the ceiling is real but *"every day"* is not literal |
| **`INDETERMINATE`** | the cells disagree across the 0.50 / 0.95 boundaries |

**Conjunctive across cells**, deliberately: a verdict that holds in one cell and not another is
not a verdict, it is a selection.

### 6a. THIS SESSION'S PREDICTION, RECORDED BEFORE THE RUN

**I predict `OVERSTATED`**, with `f50_day` somewhere in **0.70 – 0.90**, and I predict the
`SHORT` and `LONG` observations will be close to symmetric.

Reasoning, so the prediction can be judged rather than just scored: GBP/USD daily ranges in
2013–2016 are typically ~70–120 pips, so a 50-pip run *from* the day's extreme should usually be
available — but a day whose whole range is under 50 pips makes it arithmetically impossible, and
those days are not rare. **If `f50_day` comes back ≥ 0.95 I was wrong, and this file says so.**

---

## 7. WINDOW, HOLDOUT, DATA

| Field | Value |
|---|---|
| Instrument | **GBP/USD** (`D-007`) |
| Window | **2013-01-06 → 2016-06-30** — the `W-C′` DEVELOPMENT window (`COMMON_PROTOCOL.md` §3a) |
| Timeframe | **15-minute** (`D-034`) |
| Source | **HistData.com M1, aggregated to M15** (`D-036a`), `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/` |
| Integrity | SHA-256 per raw file in `raw/SHA256SUMS.txt`; the runner re-hashes the two M15 files it reads and prints the digests |
| QA gate | `qa_histdata_m1.py` — C1–C4 `PASS`, C5–C7 signed off (`QA_REPORT.txt`). **Precondition, cited in the observation** |
| Holdout | **2016-07-01 → 2017-12-29** (`D-035`). **Never on disk** — the vendor's 2016 file was truncated at `2016.06.30` on arrival and the untruncated copy deleted (`D-036a`). `E23` cannot occur here |
| Measurement | **Numbers parsed from a checksummed file. Nothing measured off a rendering** (`E06` as restated by `D-036a`) |
| Exclusions | **None.** Days with fewer than 4 bars under a given day definition are dropped by a mechanical rule stated in the runner and counted in the report; nothing is dropped for its result |

**Level comparability, disclosed:** `D-036a` records that the cross-vendor level offset is
**unmeasurable** for these windows, because FXCM serves no 2013–2016 data. **The price *levels*
in this test are not comparable with V02–V06 homework.** This test makes only **distance**
claims (pips of range, pips to target), which do travel.

---

## 8. MANDATORY SCOPE STATEMENT

Any report of this test carries this verbatim:

> **PT-033 measures the arithmetic ceiling of an entry at the day's true extreme, using
> hindsight.** It is **not** a test of a tradable rule: V07 names "Hi-Lo" as a primary method,
> recommends it in print, and does **not** teach how to identify the extreme in real time
> (`A-056`), so no version of this test can be executed forward. A high ceiling does **not**
> support the claim; it establishes only that the claim is arithmetically possible. The rule
> arm's advantage over the matched-random-entry null is a measure of **the value of the missing
> skill**, and may never be quoted as evidence that the Hi-Lo claim is correct. Nothing here
> bears on any other V07 statement, all of which remain blocked by `D-030`.

---

## 9. TO RUN THIS

```bash
python3 06_MANUAL_BACKTEST/V07/run_pt033.py
```

The runner:

1. re-hashes both M15 files and prints the digests,
2. builds the four cells (2 `D-031` arms × 2 day definitions),
3. computes and **prints `N1` and `N1b` first**,
4. then computes `O1`, `O2`, `O3`,
5. writes raw results to `06_MANUAL_BACKTEST/V07/data/pt033_results.json`.

Seed `20260812` is fixed in the script. **This file is never edited to match what was found**
(`COMMON_PROTOCOL.md` §9 rule 7).
