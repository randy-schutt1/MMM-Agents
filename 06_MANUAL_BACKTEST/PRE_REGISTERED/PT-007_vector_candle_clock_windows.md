# PT-007 — The two named vector-candle clock windows: 8:31 and 4:30 London

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:43:52]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
            RESOLVED 2026-08-13 (D-034 / D-035 / D-036a): I-007 CLOSED, D-028 PINNED at
            2016-07-01, W-B confirmed inside DEVELOPMENT. Data source is now the
            HistData GBP/USD M1 CSV corpus. Data-availability blocker CLEARED. NONE
            remaining from this pair.
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

Listing how the dealer conceals stop hunts, the instructor names **two exact clock
minutes**:

> *"Concealing them behind news and announcements. **Using the vector candle at the release
> of the news at 8:31. Using the vector candle at 4:30 London.**"* `[00:43:52]`

"Vector candle" is `A-035` and is **not** used here — this test does not identify one, does
not count them, and does not require the term to mean anything. What it uses is the part
of the sentence that is a measurement: **two named minutes**, and the claim that outsized
moves are placed there deliberately.

That is testable on a clock alone, and it is the finest-grained timing claim in the corpus
— everything else names an hour or a session. A minute-resolution claim is much easier to
falsify, which is precisely why it is worth testing.

---

## 2. THE QUESTION

> Do the 15-minute bars covering **08:30–08:45** and **04:30–04:45** carry outsized range,
> and do daily extremes form in them disproportionately?

Null hypothesis: **they do not.** Those two bars are ordinary members of the intraday
volatility profile.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute primary; **5-minute confirmatory** ~~where the feed supplies it~~ **where a 5-minute file has been aggregated from the M1 corpus — see §7 step 1**, because a claim about `8:31` is finer than a 15m bar can resolve |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-B conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| Windows under test | (i) the bar containing **08:30**; (ii) the bar containing **04:30** |
| Metric 1 | Rank of that bar's true range within the day's 96 bars |
| Metric 2 | Share of days on which the day's high or low is set inside that bar |
| Metric 3 | Share of days on which that bar's range exceeds 2× the day's median bar range |
| Weekday split | **Reported by weekday**, pre-registered: US macro releases cluster on particular weekdays, and a Friday-only effect is a different finding from an every-day effect |
| Excluded days | **None** |
| Decision point | None — distributional |
| Sample | ~520 instances per window. ≥ 30 satisfied |

### 3a. What this test cannot do, stated before it is run

**No economic calendar exists in this corpus.** This test therefore cannot separate
*"the dealer places a move at 8:31"* from *"US data is released at 8:30"*. Those are
different explanations of the same observation, and the second is the mundane one.

The test measures the **clock**, which is what the instructor named. If the bars are
outsized, the honest report is *"outsized range is concentrated in the named bars; the
cause is not identified and the obvious candidate is the release schedule itself"*. A
report that read a clock result as evidence of dealer intent would be exactly the
inference this project's `G7` refuses.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812` |
| **Second — the natural control** | The full 96-slot intraday range profile (shared with PT-004), against which the two named bars are ranked rather than merely tested |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Both bars rank in the top decile of the profile | The instructor's two named minutes are real features of GBP/USD. Cause unidentified — see §3a |
| One holds, one does not | Report both. The 04:30 bar sits inside `C-004`'s disputed London-open half-hour, so a difference between the two is also a `C-004` datum |
| Neither is distinguishable | The claim fails at this sample. Report prominently |
| 5-minute data contradicts 15-minute data | The finer series governs, and the discrepancy is itself reported — a 15m bar averages away exactly the effect being claimed |

## 6. MANDATORY SCOPE STATEMENT

> PT-007 tests whether two named clock minutes carry outsized GBP/USD range. It is **not**
> a test of the "vector candle" (`A-035`, undefined), **not** a test of the stop hunt
> (`A-002`/`A-049`, undefined and disputed between two guest accounts), and **not**
> evidence of dealer intent. It measures a clock and reports a clock.

## 7. TO RUN THIS

1. ~~Close `I-007`; confirm W-B sits inside DEVELOPMENT.~~ **Both resolved — `D-034` closed
   I-007, `D-035` pinned D-028 at 2016-07-01, W-B confirmed inside DEVELOPMENT
   (`COMMON_PROTOCOL.md` §3a). Run the data-QA gate
   (`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`) as a precondition and cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`.**
   ~~Establish whether the feed supplies 5-minute history over the whole window before
   starting, and record the answer.~~ **The HistData M1 corpus (`D-036a`) natively covers
   the whole window at 1-minute resolution — finer than the 5-minute series this step
   asks for. No 5-minute derived file exists yet; whether one has been aggregated from
   the M1 corpus (analogous to `aggregate_m15.py`) still needs recording before
   harvesting.**
2. ~~Harvest with timestamps from DOM text only.~~ **Source is the HistData GBP/USD M1
   CSV corpus (`D-036a`), aggregated locally to 15m by
   `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` (`GBPUSD_M15_ARMA.csv` /
   `GBPUSD_M15_ARMB.csv` per `D-031` arm). Every quote is a number parsed from the
   checksummed file, per `COMMON_PROTOCOL.md` §2's restated `E06` — no value is read
   from a chart rendering.**
3. Build the full intraday profile first; extract the two named bars from it afterwards.
4. Run N2 before ranking.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
