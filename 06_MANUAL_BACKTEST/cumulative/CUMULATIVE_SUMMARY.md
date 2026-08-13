# CUMULATIVE SUMMARY — every pre-registered test run to date

```text
STATUS:   21 of the 33 pre-registered PT files have been RUN and REPORTED.
COVERAGE: this file lists EVERY test that has been run, whatever it found.
          `BACKTEST_EVIDENCE_STANDARD.md` §4.3: "A summary naming only the tests
          that worked is invalid." Nothing here is omitted for being null.
UPDATED:  2026-08-13, on branch `infra/gbpusd-historical-data`, after the eight
          `D-035` re-issues and `PT-002`'s W-A arm were run.
```

**Summaries never replace individual observations.** Every figure below is a pointer;
the record is the `BT_VXX_NNNN.md` file named beside it, and the caveats that govern
each number live there, not here.

---

## 1. THE HEADLINE COUNT

| Disposition | Count |
|---|---|
| **`SUPPORTED`** (clears its own pre-registered null) | **4** |
| **`SUPPORTED` but trivially / not specially** | **1** |
| **`SPLIT`** — the comparison and the magnitude disagree | **2** |
| **`CONTRADICTED`** — the data runs against the taught claim | **3** |
| **`INDISTINGUISHABLE FROM THE NULL` / `NOT SUPPORTED`** | **9** |
| **`INDETERMINATE` / `DESCRIPTIVE` only** | **2** |
| **RUN, but `SAMPLE INSUFFICIENT` by design** | **1** (PT-023) |
| **Total run** | **21** |

**Never run, and never to be run:** `PT-008`, `PT-009`, `PT-010`, `PT-011`, `PT-012`,
`PT-013`, `PT-019`, and `PT-002`'s W-C arm — all **retired unrun** as non-conforming
under `D-035`, and all re-issued. `PT-022` — **superseded, period unobtainable**.
`PT-001` — still pins its period at run time.

---

## 2. THE FULL TABLE

### 2a. Weekly-scale — the eight `D-035` re-issues, plus `PT-002`'s daily arm

All on **`W-C′` 2013-01-06 → 2016-06-30**, the HistData corpus (`D-036a`), 180 trading
weeks unless stated, both `D-031` arms, seed `20260812`.

| PT | Question | Record | **Disposition** |
|---|---|---|---|
| **PT-002** (W-A arm) | Do **daily** extremes cluster at the six printed boundaries? | `V01/BT_V01_0001` | **NOT SUPPORTED** — N2 pct 60.6 / 39.1. The apparent 35% excess is the **arcsine** endpoint artifact |
| **PT-025** | Do **weekly** extremes cluster at the six boundaries? | `V01/BT_V01_0002` | **NOT SUPPORTED** — N2 pct 76.6 / 76.8; **below** N3 (20.8 / 29.0) |
| **PT-026** | Is the first-eight-hours range of the week cut? | `V03/BT_V03_0003` | **SUPPORTED TRIVIALLY, NOT SPECIAL** — cut in **180/180** weeks; rank **7 of 23** on a matched basis |
| **PT-027** | Does the first move out of the week's opening range reverse? | `V01/BT_V01_0003` | **SUPPORTED** — the prohibited trade returns **−5.16 pips**, N1 pct **0.9** |
| **PT-028** | On which weekday does the week make its high and low? | `V01/BT_V01_0004` | **CONTRADICTED** — mode is **Friday** for both, not Tue/Wed; χ² p < 0.001 |
| **PT-029** | Is the rest of the week a unidirectional swing? | `V02/BT_V02_0008` | **SPLIT** — clears all three controls (100/100/96.5) at an absolute efficiency of **0.1153** |
| **PT-030** | Is the previous week's extreme a barrier? (n = 178) | `V02/BT_V02_0009` | **CONTRADICTED** as absolute; **NOT SUPPORTED** statistically — breached ~half the time |
| **PT-031** | Are Sunday and Monday the accumulation phase? | `V02/BT_V02_0010` | **NOT SUPPORTED** on the governing metric — mid-pack; **verdict depends on the normalisation** |
| **PT-032** | The weekend gap and the Friday-flat rationale | `V01/BT_V01_0005` | **SUPPORTED** — **20.0%** of weekends exceed the course's own 18-pip stop |

### 2b. Day-scale — the twelve run in the earlier batch (`df7eab6`, `9eb2d0c`)

W-A / W-B on the same corpus. Summarised from their own records.

| PT | Question | Record | **Disposition** |
|---|---|---|---|
| PT-003 | Is 5pm the day boundary? | `V02/BT_V02_0003` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-004 | Are the Dead Gap and the session gaps quiet? | `V02/BT_V02_0004` | **SPLIT** — the Dead Gap holds, the half-hour gaps do not |
| PT-005 | The 8:00 / 9:30 stop-hunt | `V02/BT_V02_0005` | **INDISTINGUISHABLE FROM THE NULL** — peak is 08:30–09:00, not 09:30 |
| PT-006 | Does a new session reverse the old one? | `V02/BT_V02_0006` | **CONTRADICTED** on Arm A — London **continues** |
| PT-007 | The 8:31 and 4:30 vector-candle windows | `V02/BT_V02_0007` | **SUPPORTED** on Arm A — ranks 1 and 2 of 96; cause unidentified |
| PT-014 | Is 25–50 pips the modal excursion? | `V04/BT_V04_0001` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-015 | Does a >50-pip ceiling exist? | `V04/BT_V04_0002` | **INDISTINGUISHABLE FROM THE NULL** on hit rate |
| PT-016 | "Asian range under 50" as a filter | `V03/BT_V03_0001` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-017 | "In profit in 15 to 45 minutes. Guaranteed." | `V04/BT_V04_0003` | **SUPPORTED** on timing of meaningful profit; null on anything bankable |
| PT-018 | The two-hour time stop | `V02/BT_V02_0001` | **SUPPORTED** on the underlying claim; hit rate `DESCRIPTIVE` |
| PT-020 | The London-open asymmetric conditional | `V03/BT_V03_0002` | **INDISTINGUISHABLE FROM THE NULL**; variance claim **contradicted in direction** |
| PT-021 | DNC and the straightaway test | `V02/BT_V02_0002` | **INDISTINGUISHABLE FROM THE NULL** |

### 2c. Guest-material and concurrent-session tests

| PT | Record | **Disposition** |
|---|---|---|
| PT-023 | `V06/BT_V06_0001` | **`DESCRIPTIVE`** — n = 12, below the floor **by design**, and partly contaminated |
| PT-024 | `V06/BT_V06_0001` | run on a second vendor; see that file |
| PT-033 | `V07/BT_V07_0001` | **`INDETERMINATE`** — and the day boundary is why |

---

## 3. WHAT SURVIVES, AND WHAT DOES NOT

**Four claims clear their own pre-registered nulls**, and none of them is an entry rule:

1. **`PT-032` — the Friday-flat rationale.** One weekend in five gaps past the 18-pip stop
   the course itself teaches, and the figure is a **lower bound** (no spread in the corpus).
   **The clearest supportable instruction in V01**, and the only one whose rationale is
   mechanical rather than pattern-based.
2. **`PT-027` — "do not take the first move of the week".** The prohibited trade loses
   5.16 pips where a matched random entry is break-even; **N1 percentile 0.9**. The
   prohibition is doing real work.
3. **`PT-007` — the 8:31 and 4:30 clock windows.** Ranks 1 and 2 of 96 on Arm A. **The cause
   is unidentified and the mundane candidate — the release calendar — is strongly indicated.**
4. **`PT-017` / `PT-018`** — partial, on timing rather than on anything bankable.

**Three claims are contradicted by the data**, not merely unsupported:

- **`PT-028`** — the week's extremes print on **Friday**, and Tuesday/Wednesday are the two
  most *depleted* cells. The taught mid-week turn is the opposite of what GBP/USD did.
- **`PT-030`** — *"they will not go below last week's peak formation"* is stated absolutely
  and is breached in about half of weeks, by a median of 76–101 pips.
- **`PT-006`** — a new session **continues** the old one's direction rather than reversing it.

**A recurring mechanism explains several of the nulls, and it is worth stating once.** The
extremes of a random-walk path concentrate at the **edges of any window**, wherever the edges
are placed — the arcsine law. It is measured directly in `BT_V01_0001` §2 at day scale and
reappears in `BT_V01_0004` §3 at week scale. **It makes boundary-clustering claims look true
against a naive uniform-time expectation and false against a shift control**, and it is why
`PT-002` and `PT-025` both return null while their raw excess looks like +31–35%.

---

## 4. FIVE PLACES WHERE THE MEASUREMENT ALMOST PRODUCED A FALSE POSITIVE

Recorded because each was caught by a pre-registered control or a disclosed check, and
each would otherwise have been reported as a finding:

| # | Test | What would have been reported | What the check showed |
|---|---|---|---|
| 1 | `PT-002` / `PT-025` | "+35% clustering at the six boundaries" | The arcsine artifact. N2 absorbs it; the analytic null cannot |
| 2 | `PT-026` | "the week-open block ranks **1 of 30**" | Outcome-window confound. Matched basis: **7 of 23** |
| 3 | `PT-031` | "Sun+Mon is the quietest span in 63% of weeks" | A 31-hour span against 48-hour ones. Normalised: **mid-pack** |
| 4 | `PT-025` | N3 percentile 8.3 (raw share) | The real week boundaries coincide with 17:00 and add no covered area; corrected: **20.8** |
| 5 | `PT-027` | 66,443 "later breaches" in 180 weeks | Bars spent outside the block, not breach events. Corrected: **1,586** |

**And one place where a pre-registration's own expectation was reversed:** `PT-032` §3a‴
expected the two ≥ 72 h extended closures to be the sample's strongest evidence. They are two
of its **smallest** gaps (−7.10 and +0.40 pips) — they are Christmas and New Year.

---

## 5. WHAT NO SUMMARY HERE MAY BE READ AS SAYING

- **No win rate anywhere in this corpus validates the method** (`D-009`). Every claimed
  accuracy figure from the course is a **hypothesis under test**, never a target.
- **Nothing here is an entry rule.** The four supported results are a prohibition, a
  risk rationale, a clock observation with an unidentified cause, and a timing observation.
- **Price levels on this corpus are not comparable with the V02–V06 FXCM homework**
  (`D-036a`). Only **shape and distance** claims travel.
- **The `D-035` HOLDOUT (2016-07-01 → 2017-12-29) has never been opened** and is not on
  disk. Every result above is a **DEVELOPMENT-block** result and carries whatever
  optimism that implies.
- **The undefined vocabulary is still undefined.** `A-001`, `A-002`, `A-004`, `A-006`,
  `A-010`, `A-011`, `A-012`, `C-001` and the rest are untouched by any test above;
  `D-030` blocked them and still does.
