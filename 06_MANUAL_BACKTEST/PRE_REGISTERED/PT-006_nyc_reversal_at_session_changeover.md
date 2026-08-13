# PT-006 — The NYC Reversal: does the new session reverse the old one's direction?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:34:05], [00:34:09]; printed slide [00:33:10] "( NYC Reversal)"
BLOCKERS:   I-007 · D-028 boundary dates unpinned
            RESOLVED 2026-08-13 (D-034 / D-035 / D-036a): I-007 CLOSED, D-028 PINNED at
            2016-07-01, W-A confirmed inside DEVELOPMENT. Data source is now the
            HistData GBP/USD M1 CSV corpus. Data-availability blocker CLEARED. NONE
            remaining from this pair.
ATTESTATION: No chart in W-A was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

Two statements, one spoken and one printed, make the same claim:

> *"**The new session brings a new target and a new market maker on duty.**"* `[00:34:05]`
> *"That's why if you're in something, it's up a little bit and then all of a sudden the
> red box shows up and now you're stopped out. **The new guy came on and he changes the
> direction.**"* `[00:34:09]`

and on the slide at `[00:33:10]`: *"New Session Brings New Targets For Market Makers
**( NYC Reversal)**"* — a printed name for the effect that is **never spoken**
(`V02_INTERPRETATION.md` §10.2 U3).

This is the mechanism underneath the lesson's clearest actionable instruction — *"always
look to take profit at session changeover"* `[00:33:05]`. The instruction is only sound if
the claim underneath it is true. And the claim is directional, mechanical and testable
with nothing but timestamps and closes: no pattern, no indicator, no "second leg".

---

## 2. THE QUESTION

> Is the direction of GBP/USD in the hour **after** the New York open the opposite of its
> direction during the London session, more often than chance?

Null hypothesis: **the two directions are independent.** Post-changeover direction is
unrelated to the direction of the session that preceded it.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute |
| Window | **W-A** — 2015-01-04 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-A conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| Prior-session direction | Sign of `close(09:00) − open(03:30)` — the London session exactly as the V02 table prints it |
| Post-changeover direction | Sign of `close(10:30) − open(09:30)` — the first hour of New York as printed |
| Primary measure | Share of days on which the two signs **differ** |
| Second measure | The same at 30 min, 2 h, and to the 17:00 close, all pre-registered, all reported |
| Third measure | The same test at the **other** changeover — Asian→London at 03:30 — because a "new market maker on duty" claim that is true only at one changeover is a narrower claim and worth distinguishing |
| Excluded days | **None.** Days where either leg closes flat (sign = 0) are reported as a separate count, not dropped silently |
| Decision point | 09:30. Nothing after it informs the classification of the prior session |
| Sample | ~260 days. ≥ 30 satisfied |

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812`. Establishes the reversal rate between two arbitrary adjacent windows of the same lengths |
| **Second — the natural control** | The same measurement on **all 24 candidate changeover hours**, so 09:30 is ranked rather than merely tested. Identical logic to PT-003's 24-anchor sweep, and identical reason |
| **Third** | Serial-correlation control: the reversal rate between two adjacent windows of the same lengths **inside** the London session, where no changeover occurs. This separates "sessions reverse each other" from "GBP/USD mean-reverts at this horizon generally" |

The third arm is the one that decides what the result means. Mean reversion at a 5-hour
horizon would produce a reversal rate above 50% with no market maker involved at all.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Reversal rate at 09:30 exceeds both the clock-shift null and the within-session control | Support for the NYC Reversal as a **timed** effect. The take-profit-at-changeover instruction gains a mechanism |
| Elevated at 09:30 *and* within-session | The effect is generic mean reversion, not a session changeover. **This is the most likely trap in the whole test and the third arm exists to catch it** |
| Indistinguishable from 50% | The claim fails at this sample. Report prominently — it would weaken the lesson's clearest actionable instruction, which is exactly the kind of result that must not be buried (`E25`) |
| 03:30 reverses but 09:30 does not (or vice versa) | A narrower true claim. Report the per-changeover breakdown |

## 6. MANDATORY SCOPE STATEMENT

> PT-006 tests whether session changeover is associated with a direction change on
> GBP/USD. It does **not** test *"a new market maker on duty"* — that is a claim about who
> is behind the price, which candle data cannot observe, and which this project treats as
> the instructor's teaching model rather than a microstructure fact
> (`V01_INTERPRETATION.md` §3 G7). It also does **not** test the take-profit rule, which
> requires an entry the course has not specified.

## 7. TO RUN THIS

1. ~~Close `I-007`; confirm W-A sits inside DEVELOPMENT.~~ **Both resolved — `D-034` closed
   I-007, `D-035` pinned D-028 at 2016-07-01, W-A confirmed inside DEVELOPMENT
   (`COMMON_PROTOCOL.md` §3a). Run the data-QA gate
   (`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`) as a precondition and cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`.**
2. ~~Harvest 15m bars with timestamps from DOM text only.~~ **Source is the HistData
   GBP/USD M1 CSV corpus (`D-036a`), aggregated locally to 15m by
   `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` (`GBPUSD_M15_ARMA.csv` /
   `GBPUSD_M15_ARMB.csv` per `D-031` arm). Every quote is a number parsed from the
   checksummed file, per `COMMON_PROTOCOL.md` §2's restated `E06` — no value is read
   from a chart rendering.**
3. Compute all three arms and both `D-031` arms in one pass.
4. Run N2 and the within-session control **before** looking at the 09:30 number.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
