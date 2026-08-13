# PT-003 — Is 5pm the day boundary? The printed "High / Low Reset"

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 (printed slide, [00:45:55])
BLOCKERS:   I-007 · D-028 boundary dates unpinned
ATTESTATION: No chart in W-A was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The first line of the V02 session table is the one nobody has looked at:

```text
5pm    High / Low Reset (The MM Spread Is Set)
```

**It is printed and never spoken** — `V02_INTERPRETATION.md` §10.2 U2 records it as one of
two items on that slide absent from the audio entirely. It is therefore *authored* material
(stronger than ASR) that has never been examined.

And it makes a claim with teeth. Everything in this method that says "the day" — the high
of the day, the low of the day, the daily range, `HOD`/`LOD` — depends on **when the day
starts**. If the instructor's 5pm reset is real, then a midnight-anchored day is the wrong
unit and every daily measurement in this project is being taken on the wrong grid. That is
a cheap thing to check and an expensive thing to be wrong about.

The claim is also purely mechanical: no pattern, no indicator, no definition owed.

---

## 2. THE QUESTION

> Does a GBP/USD trading day anchored at **17:00** contain its extremes more coherently
> than one anchored at **00:00** — and does the 17:00 instant behave like a boundary at
> all?

Null hypothesis: **17:00 is an ordinary hour.** A 17:00-anchored day is no more coherent
than a day anchored at any other hour of the clock.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-A** — 2015-01-04 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** (`5pm` is `17:00` in the chart's own zone; the arms move it) |
| Metric 1 — **extreme separation** | For each candidate anchor hour `h`, the mean absolute time-gap between the day's high and the day's low, in bars. A "reset" day should place its extremes *inside* the day rather than adjacent across the boundary |
| Metric 2 — **boundary adjacency** | Share of days whose high **or** low falls within 30 minutes of the anchor. A real boundary should be a *rare* place for an extreme, not a common one |
| Metric 3 — **range concentration** | Gini-style concentration of the day's true range across its 96 fifteen-minute bars |
| Candidate anchors | **All 24 hours**, `h = 00:00 … 23:00`. 17:00 is one row of a table it does not get to be the headline of |
| Decision point | None — distributional |
| Sample | ~260 days per anchor. ≥ 30 satisfied |

**The 24-anchor sweep is the point of the design.** Testing only 17:00 against only 00:00
would give a two-way comparison that a coin flip wins a quarter of the time. Ranking 17:00
among all 24 candidates is falsifiable in a way that binary comparison is not, and it is
pre-registered here so the ranking cannot be reframed afterwards.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812`. Gives the null distribution of each metric under a randomised clock |
| **Second — the natural control** | The other 23 anchor hours, measured identically. This is the strongest available comparator because it holds the price series, the sample and the metric fixed and varies **only the anchor** |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| 17:00 ranks mid-pack among 24 anchors | **The printed reset is not visible in GBP/USD price at this sample.** Report prominently. The slide stays on the record as what the course teaches; this is what the market did |
| 17:00 ranks top-3 on all three metrics | Strong support for a 17:00-anchored day. Consequence: this project's daily measurements should move to that grid — **and that is a `DECISIONS.md` change, not a finding a backtest gets to make on its own** |
| 17:00 ranks top-3 on one metric only | Report all three. Do not headline the one that worked (`E09`) |
| Arms A and B rank 17:00 differently | A `D-031` finding: the reset is one hour off in one arm, which is itself informative about `A-019` |

## 6. MANDATORY SCOPE STATEMENT

> PT-003 tests whether the daily high/low "reset" printed on the V02 session slide is
> visible in GBP/USD price. It is **not** a test of *"The MM Spread Is Set"* — the spread
> mechanism is a claim about broker behaviour that candle data cannot observe, and no
> result here bears on it. `A-019` (no timezone printed) is unaffected either way.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-A sits inside DEVELOPMENT.
2. Harvest 15m bars with timestamps from DOM text only.
3. Compute all three metrics for all 24 anchors **and both arms** in one pass, so that no
   ordering of the computation can influence what is looked at first.
4. Run N2 before ranking anything.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
