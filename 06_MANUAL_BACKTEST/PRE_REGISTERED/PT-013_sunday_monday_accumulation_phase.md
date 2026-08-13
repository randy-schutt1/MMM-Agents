# PT-013 — Are Sunday and Monday the week's accumulation phase?

```text
STATUS:      NON-CONFORMING UNDER D-035 — SUPERSEDED BY PT-031, 2026-08-13.
             NEVER RUN. NOT EDITED INTO CONFORMANCE. RETAINED, NOT DELETED.

             WHY: this file pre-registered W-C (2013-01-06 -> 2017-12-29) as its window.
             D-035 pins the project-wide D-028 split at 2016-07-01 -- DEVELOPMENT
             2013-01-06 -> 2016-06-30, HOLDOUT 2016-07-01 -> 2017-12-29. W-C STRADDLES
             that boundary by 546 days, so 30% of this test's window lies in the
             holdout, which no session may open during the Student Phase (D-027, D-028).

             D-027 is explicit that changing a range creates a NEW TEST ID and that the
             abandoned test is retained and marked. COMMON_PROTOCOL.md 3a says the same
             and names the replacement window: W-C' = 2013-01-06 -> 2016-06-30. PT-031
             carries this test's question, three day-set arms, four metrics, three
             controls, seed and scope onto W-C', and declares as costs rather than as
             details everything the substitution changes:
               - data source: HistData GBP/USD M1 CSV corpus (D-036a), not TradingView
                 / FXCM (D-034);
               - week open: 22:00 UTC (Sunday 17:00, fixed UTC-5, no DST), NOT 21:00 UTC;
               - 3a's conditional RESOLVES: this corpus DOES print Sunday bars, so arm 2
                 (Sunday alone) RUNS. It is 7 hours long, and "Sunday + Monday" is
                 therefore 31 HOURS, not two days -- against 48-hour controls. The
                 length-normalised comparison is promoted to headline in PT-031, because
                 a raw range comparison is rigged by arithmetic alone;
               - Thursday+Friday has no remaining week, so its containment and
                 first-breach metrics are NOT APPLICABLE, never zero;
               - sample: 180 TRADING weeks for arms 1-2 and 179 for arm 3 (which needs
                 the previous week's Friday), not the ~260 per arm claimed in 3 below.
                 W-C' holds 182 calendar Sundays but only 181 observable Sunday week
                 opens, and the week of 2014-06-01 is EXCLUDED BY NAME from ALL THREE
                 ARMS -- the corpus holds ZERO bars for Sun 2014-06-01, so the Sunday
                 session that arm 2 IS, and that arms 1 and 3 contain, does not exist
                 there. Surfaced by QA check C8, which was ADDED AFTER PT-031 was
                 drafted -- and C8 is precisely the check that asks whether the Sunday
                 session is actually present.

             THIS FILE HAS NEVER BEEN RUN AND MUST NOT BE RUN.
             NOTHING IN THIS FILE WAS CHANGED except this status block.

--- original status block, as pre-registered 2026-08-12, unchanged ---
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:09:22]–[00:09:51], [00:11:44]–[00:12:15]
BLOCKERS:   I-007 (Sunday bars are feed-dependent — see §3a) · D-028 unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

This is the analogy the whole weekly cycle is built on, stated four times in one lesson:

> *"What's the Asian session? Accumulation."* `[00:09:22]`
> *"So if the Asian session is accumulation, then **Sunday and Monday is the Asian session
> for the week**."* `[00:09:29]`

If it holds, the intraday method transfers to the week and V02's central claim has support.
If Sunday+Monday is an ordinary two-day span on GBP/USD, the transfer is an analogy and
nothing more — and three lessons of weekly-scale teaching rest on it.

The claim has a measurable core: an **accumulation phase is a low-range, range-bound span
whose boundaries later matter**. Range, containment and subsequent boundary-relevance are
all measurable. Nothing blocked is required.

### 1a. The instructor relaxes the days himself, so the test must too

> *"I could say Sunday is the Asian session… The first part of the week, Sunday, Monday,
> Tuesday, could be **Friday, Sunday, Monday**."* `[00:11:44]`

`V02_INTERPRETATION.md` `G9` is explicit: **do not encode the days.** The *role* is fixed;
the *calendar* is not. This test therefore pre-registers **all three day-sets he names as
separate arms**, all reported — which converts his own hedge from a get-out into a measured
comparison.

---

## 2. THE QUESTION

> Is the Sunday+Monday span systematically lower-range and more contained than the spans
> that follow it — and do its boundaries matter to the rest of the week?

Null hypothesis: **it is not.** Sunday+Monday behaves like any two-day span in the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute; 4-hour cross-check |
| Window | **W-C** — 2013-01-06 → 2017-12-29 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| **Arm 1** | **Sunday + Monday** — the headline reading |
| **Arm 2** | **Sunday alone** — `[00:11:44]` |
| **Arm 3** | **Friday + Sunday + Monday** — `[00:11:44]`, length-normalised |
| Metric 1 — range | Span range in pips, and as a share of the whole week's range |
| Metric 2 — containment | Share of the remaining week's bars that trade **inside** the span's high/low |
| Metric 3 — boundary relevance | Whether the week's extreme forms beyond the span's edge, and the distance |
| Metric 4 — the false move | Time from span close to the first breach of either edge (shared definition with PT-008/PT-009, computed here at day rather than 8-hour granularity) |
| Excluded weeks | **None.** Weeks with a holiday Monday are retained and reported separately |
| Decision point | Span close. Metrics 2–4 are outcomes |
| Sample | ~260 weeks per arm. ≥ 30 satisfied |

### 3a. Sunday bars are a feed property, not a market property

Some feeds print a short Sunday session; some fold it into Monday; some do not print it at
all. Arm 2 (**Sunday alone**) is **unrunnable on a feed with no Sunday bars**, and if that
is the declared feed the correct action is to record arm 2 as `NOT RUNNABLE ON THIS FEED`
in the observation — **not** to silently redefine it as "Monday's first eight hours". That
substitution would be `D-030`'s exact prohibition, and it would be invisible six months on.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | The same metrics for **every other two-day span** in the week (Mon+Tue, Tue+Wed, Wed+Thu, Thu+Fri). Ranking Sun+Mon among them holds week, instrument and metric fixed and varies only the days |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812` |
| **Third** | Length-normalised comparison across arms 1–3, so a three-day arm cannot win on range simply by being longer |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Sun+Mon is the lowest-range two-day span in most weeks, and its edges are later relevant | Support for the analogy that carries V02's weekly teaching |
| Low range but no boundary relevance | Half the claim. "Quiet" and "the level the dealer later exploits" are different assertions and this outcome separates them — which is the most useful thing this test can do |
| Sun+Mon ranks mid-pack | **The analogy has no measurable support at this sample.** Report prominently |
| A different arm wins | Report all three and adopt none as doctrine. The instructor names all three himself, so a winner among them is a measurement, not a correction of him |

## 6. MANDATORY SCOPE STATEMENT

> PT-013 tests whether the week's opening days are a low-range, later-relevant span on
> GBP/USD. **"Accumulation" is not defined by the course** (`V02_SOURCE_NOTES.md` §3 —
> given as an answer, never expanded), so this test measures a proxy it names explicitly:
> range, containment and boundary relevance. It is not a test of contract accumulation,
> which no candle chart can observe.

## 7. TO RUN THIS

1. Close `I-007`; **record whether the feed prints Sunday bars**; confirm W-C is
   DEVELOPMENT.
2. Harvest with timestamps from DOM text only.
3. Compute the four other two-day spans **before** looking at Sun+Mon.
4. Report all three arms and both `D-031` arms every time.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
