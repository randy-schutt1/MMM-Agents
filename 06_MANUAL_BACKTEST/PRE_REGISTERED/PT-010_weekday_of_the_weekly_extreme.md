# PT-010 — On which weekday does the GBP/USD week make its high and its low?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V01 [00:34:47]–[00:35:55], [00:52:38]; V02 [00:04:15], [00:00:03]–[00:00:26]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The weekly cycle is the course's founding thesis — *"same shit every week"* V01
`[00:52:38]` — and its shape has one consequence that survives every open ambiguity:
**the week turns in the middle.**

> *"The anchor point is where the midweek reversal comes in."* V02 `[00:04:15]`
> *"sometimes could come in high on Tuesday, chop around, hit it again Wednesday"*
> V02 `[00:00:03]`; *"They can come back on Thursday too and give you three tops."*
> `[00:00:13]`

*Anchor point* is `A-001`, *midweek reversal* is `A-012`, and both are undefined — **so
this test uses neither.** It measures the one thing that needs no definition: the weekday
on which the week's actual high and actual low print. If the cycle is real at all, weekly
extremes concentrate mid-week. If they are uniform across the week, the cycle's calendar
shape has no support on this instrument, whatever the anchor turns out to be.

This is the cheapest available check on the largest claim in the corpus, and it is
**exactly the check nobody has run**: `V04_HOMEWORK.md` measured four weeks, one per pair,
and labelled itself `DESCRIPTIVE` for that reason.

---

## 2. THE QUESTION

> Is the weekday distribution of GBP/USD weekly highs and lows non-uniform, and does it
> concentrate on Tuesday–Wednesday?

Null hypothesis: **it is uniform.** A weekly extreme is as likely on any trading day.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute (for the timestamp of the extreme); 4-hour for cross-check |
| Window | **W-C** — 2013-01-06 → 2017-12-29, ~260 weeks |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** (a one-hour shift can move an extreme across a day boundary) |
| Measure 1 | Weekday of the week's high; weekday of the week's low. Sunday bars counted as their own category if the feed prints them, **never merged into Monday** |
| Measure 2 | Hour-of-week of each extreme, in 4-hour bins — a finer view that does not depend on the day boundary |
| Measure 3 | Joint distribution: (high weekday, low weekday) pairs, and the sign of `high_day − low_day` — which is the cycle's *direction of travel* through the week |
| Pre-registered focal prediction | The **mode** of both marginal distributions falls on **Tuesday or Wednesday** |
| Excluded weeks | **None.** Holiday-shortened weeks are retained and reported separately |
| Decision point | None — distributional |
| Sample | ~260 weeks. ≥ 30 satisfied |

Measure 3 is the one that distinguishes a real cycle from a boundary artifact: a week that
sets its low early and its high late is a trend week, not a cycle week, and the joint
distribution separates them without anyone having to name an anchor.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | Uniform expectation over the trading days actually present in each week, computed analytically, with a χ² and its p-value **and** the raw counts |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`. If extremes cluster mid-week under *any* week anchor, the finding is about the middle of a 5-day span, not about Tuesday |
| **Third — the natural control** | The same measurement on **randomly re-blocked 5-day spans** that do not respect the calendar week. This separates "the calendar week is a real unit for GBP/USD" from "any 5-day span has a middle" |

**The second and third arms are not decoration.** A distribution over five days will look
non-uniform by eye almost every time; the arms are what turn "looks clustered" into a
statement.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Modes on Tue/Wed, surviving both shift controls | Support for the weekly cycle's calendar shape. **The single most useful positive result available from V01–V02** — and still not support for any entry rule |
| Non-uniform but modes elsewhere (e.g. Friday) | A real finding that contradicts the taught shape. Report prominently; it would bear on `C-001` indirectly and on V01's `CL3` (*"Is it always like this?" — "Yeah"*) directly |
| Indistinguishable from uniform | **The weekly cycle has no calendar signature on GBP/USD at this sample.** Report prominently. This is the null the project most needs to know about early |
| Arms A and B disagree | Reported; a one-hour timezone shift moving the answer would itself be a `D-031` finding worth having |

## 6. MANDATORY SCOPE STATEMENT

> PT-010 measures when GBP/USD weekly extremes print. It is **not** a test of the anchor
> point (`A-001`), the midweek reversal (`A-012`), the peak formation (`A-010`) or the M/W
> (`A-011`) — none of which is defined in V01–V06 — and it adopts **no** day count, so it
> takes no position on `C-001`. A clustering result would be *consistent with* the taught
> cycle; it would not identify an anchor on any single week, which is what a trader would
> actually need.

## 7. TO RUN THIS

1. Close `I-007`; record the feed's week-open timestamp; confirm W-C is DEVELOPMENT.
2. Harvest with timestamps from DOM text only.
3. Compute all three measures and both arms in one pass.
4. Run the two shift controls **before** reading the observed distribution.
5. Report the five largest-range weeks as the pre-registered sensitivity appendix.
6. Write `BT_V01_NNNN.md` from the template, §0 referencing this file.
