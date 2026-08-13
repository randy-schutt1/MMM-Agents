# PT-005 — "Take a trade at 8 o'clock and then 9:30 when the dealer hits your stops"

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:51:03]–[00:51:20]; V01 [00:46:09]
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

This is **the only falsifiable prediction the instructor states as an experiment for the
student to run**, anywhere in V01–V04:

> *"Forex Factory shows New York open at 8. Well, go to Forex Factory and hang out with
> them at 8… Forex Factory is clueless."* `[00:51:03]`–`[00:51:13]`
> *"**Take a trade at 8 o'clock and then 9:30 when the dealer hits your stops**, come back
> next week and tell me."* `[00:51:20]`

He names the entry time, the adverse event, the time of the adverse event, and the way to
check. He does not name a pattern, an indicator, a stop, a target or a "second leg". The
prediction is complete as spoken — which nothing else in the corpus is.

It also tests the corpus's cleanest surviving time value. V01 `[00:46:09]` *"US session
starts at 930 New York Eastern"* is the one time reference that `V01_INTERPRETATION.md`
§2 records as not garbled, and the V02 slide prints `New York Session: 9:30-5pm`.

---

## 2. THE QUESTION

> Is adverse excursion against a position opened at **08:00** concentrated in the
> **09:30–10:00** half-hour, relative to the rest of the 08:00–12:00 stretch?

Null hypothesis: **it is not.** Adverse excursion accrues in proportion to elapsed time
and prevailing volatility, with nothing special at 09:30.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-B conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| Entry | Mechanical: at the **08:00 bar close**, every trading day, no filter of any kind. Both directions run as separate arms (long-only and short-only), because the instructor names no direction |
| Stop | **18 pips** — the instructor's stated maximum (V04 `[00:04:43]`). Not fitted |
| Target | **50 pips** — the figure in his worked arithmetic (V04 `[00:05:07]`). Not fitted |
| Primary measure | **Time-of-day of the stop-out**, binned in 30-minute slots from 08:00 to 12:00 |
| Second measure | Maximum adverse excursion accrued in each 30-minute slot, in pips, whether or not the stop is hit |
| Decision point | The 08:00 close. **No later bar is consulted for eligibility** — there is no eligibility rule to consult it for |
| Sample | ~520 days × 2 directions. ≥ 30 satisfied by a wide margin |

**Every day is taken.** No news filter, no "behaved" filter, no volatility filter. Any
filter here would be this session's invention, and the guest's ADR/behaviour filters are
excluded by `D-025`.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry**: same window, same stop/target, same direction, entry bar drawn at random from 08:00–12:00. 1,000 iterations, seed `20260812` |
| **Second** | **N2 — circular clock shift**, 1,000 draws. Tests whether *09:30 specifically* matters or merely *some* hour does |
| **Third — the natural control** | The same 08:00 entry with the stop-out clock measured against a **08:00-relative** grid rather than a wall-clock grid. If stop-outs cluster at "90 minutes after entry" rather than "09:30", the finding is about elapsed time, not about the New York open — and those are different claims |

The third arm is what makes this test worth running. Without it, a stop-out spike at 09:30
is indistinguishable from a stop-out spike at *entry + 90 minutes*, and the instructor's
claim is specifically about the clock.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Stop-outs spike at 09:30–10:00 in wall-clock but not in entry-relative terms | **The instructor's prediction holds as stated.** The strongest single vindication available in V01–V04 |
| Spike appears in both grids | The result is about elapsed time, not the New York open. **Report it as such** — it is a real finding and it is not his claim |
| No spike anywhere | The prediction fails on GBP/USD at this sample. Report prominently (`E25`); it bears directly on the "Forex Factory is clueless" framing |
| Arm A spikes at 09:30 and arm B at 08:30 (or vice versa) | The sharpest possible `D-031` result — a one-hour displacement is exactly what separates the arms. Report both; conclude nothing about `A-019`, which stays open |

## 6. MANDATORY SCOPE STATEMENT

> PT-005 tests one clock claim: that adverse movement against an 08:00 position
> concentrates at 09:30. The 08:00 entry is a **measurement device**, not a strategy, and
> its win rate is not a result about the method — the instructor's own entry requires a
> second leg (`A-007`) and TDI (`A-039`), neither of which is taught in V01–V04. Any
> profitability figure produced here must be reported with that sentence attached.

## 7. TO RUN THIS

1. ~~Close `I-007`; confirm W-B sits inside DEVELOPMENT.~~ **Both resolved — `D-034` closed
   I-007, `D-035` pinned D-028 at 2016-07-01, W-B confirmed inside DEVELOPMENT
   (`COMMON_PROTOCOL.md` §3a). Run the data-QA gate
   (`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`) as a precondition and cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`.**
2. ~~Harvest 15m bars with timestamps from DOM text only.~~ **Source is the HistData
   GBP/USD M1 CSV corpus (`D-036a`), aggregated locally to 15m by
   `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` (`GBPUSD_M15_ARMA.csv` /
   `GBPUSD_M15_ARMB.csv` per `D-031` arm). Every quote is a number parsed from the
   checksummed file, per `COMMON_PROTOCOL.md` §2's restated `E06` — no value is read
   from a chart rendering.**
3. Run N1 and N2 and record their distributions **before** looking at the observed
   stop-out histogram.
4. Produce the wall-clock and entry-relative histograms in the same pass.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
