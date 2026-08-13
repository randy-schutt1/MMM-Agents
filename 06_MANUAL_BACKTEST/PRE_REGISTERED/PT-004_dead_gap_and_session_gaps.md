# PT-004 — Are the printed "Dead Gap" and the two session gaps actually quiet?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 (printed slide, [00:45:55]; spoken [00:50:32])
BLOCKERS:   I-007 · D-028 boundary dates unpinned · C-004 (see §3a)
            RESOLVED 2026-08-13 (D-034 / D-035 / D-036a), I-007/D-028 PAIR ONLY: I-007
            CLOSED, D-028 PINNED at 2016-07-01, W-A confirmed inside DEVELOPMENT. Data
            source is now the HistData GBP/USD M1 CSV corpus. Data-availability blocker
            CLEARED. C-004 remains OPEN, unaffected by this entry — see §3a.
ATTESTATION: No chart in W-A was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The V02 slide prints three inactive windows:

```text
5pm – 8pm      Dead Gap
Asian Session  8:30pm – 3:00am     Gap 3:00–3:30
London Session 3:30am – 9:00am     Gap 9:00–9:30
```

The 5pm–8pm "Dead Gap" is, like the 5pm reset, **printed and never spoken**
(`V02_INTERPRETATION.md` §10.2 U2). The two half-hour gaps are printed *and* spoken
(`[00:50:32]` *"3 to 3:30 is the gap, 4 o'clock session open"*).

This is the cheapest possible check on whether the instructor's session map describes
**GBP/USD** at all. It needs no pattern, no indicator, no entry, and no definition the
course owes. If the three named windows are not measurably quieter than their neighbours,
then the map is a diagram of a different market, a different era, or a different broker's
feed — and every session-gated rule downstream is standing on it.

It is also the natural companion to PT-003: PT-003 asks whether **17:00** is a boundary;
PT-004 asks whether the **three hours after it** are what the slide says they are.

---

## 2. THE QUESTION

> Is realised GBP/USD range in the three printed inactive windows lower than in the
> adjacent active windows, and lower than a randomly re-labelled clock would produce?

Null hypothesis: **the named windows are not distinguishable** from the surrounding hours.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute |
| Window | **W-A** — 2015-01-04 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-A conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| Windows under test | (i) 17:00–20:00 "Dead Gap"; (ii) 03:00–03:30 gap; (iii) 09:00–09:30 gap |
| Comparators | For each, the equal-length window **immediately before** and **immediately after** it |
| Metric 1 | Mean per-bar true range, in pips |
| Metric 2 | Mean absolute net movement across the window, in pips |
| Metric 3 | Share of **daily** extremes falling inside the window (a genuinely dead window should hold almost none) |
| Weekday handling | Sunday and Friday are **retained and reported separately**, because the week's open and close sit inside the 17:00–20:00 window on those days and would otherwise contaminate a weekday average |
| **Where the week open actually falls — pinned 2026-08-13, `D-036a`** | The row above was written when the week open was un-pinned. It is now measured, and it lands **inside window (i), at its edge**: **Arm A — 17:00 exactly, the FIRST bar of the Dead Gap window** (corpus is natively fixed UTC−5; 172 of 187 week opens at exactly 17:00). **Arm B — 18:00 during US DST** (one hour into the window), **17:00 during standard time**. So the Sunday instance's contamination is not merely "inside the window" but **arm- and season-dependent in position**. The separate-reporting rule stands unchanged; **the two arms must be compared on the Sunday instance specifically**, and any divergence there is a `D-031` finding, not a defect |
| Decision point | None — distributional |
| Sample | ~260 instances per window. ≥ 30 satisfied |

### 3a. `C-004` is a live contradiction here and is handled, not assumed away

The slide prints London open at **3:30am**; the audio at `[00:50:32]` says *"3 to 3:30 is
the gap, **4 o'clock session open**"*, thirty minutes later, in the same lesson, one week
before the 2012 UK DST change he explicitly flags. `CONTRADICTIONS.md` `C-004` is open.

**This test does not choose.** The 03:00–03:30 gap is measured as printed, and
**03:30–04:00 is reported as a fourth window** so the two readings can be compared on the
same data. If 03:30–04:00 looks like gap rather than session, that is evidence bearing on
`C-004` — recorded there, resolving nothing on its own.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812` |
| **Second — the natural control** | The **full 24-hour profile** of mean per-bar range, computed for all 96 fifteen-minute slots. The three named windows are then read off a curve that exists independently of them, which prevents the "found what we went looking for" failure |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| All three windows are local minima of the 24h profile | The session map is a real description of GBP/USD activity. **Necessary** support for every timing rule; sufficient for none |
| The Dead Gap holds but the half-hour gaps do not | The likeliest partial result. Half-hour resolution may simply be below what a 15m series can show — say so rather than reporting a null as a refutation |
| No window is distinguishable | **The printed map does not describe this instrument at this sample.** Report prominently. It would put `A-019` in a harsher light: an unknown timezone applied to a map that does not fit is two problems, not one |
| Arms diverge | Expected and informative — the whole table shifts an hour between arms. Report both profiles |

## 6. MANDATORY SCOPE STATEMENT

> PT-004 tests whether three printed inactive windows are quiet on GBP/USD. It is **not**
> a test of any trading rule, and a favourable result is not evidence that trading those
> sessions works. *"The MM Spread Is Set"* is a claim about broker spread that candle data
> cannot see and that this test does not touch.

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
3. Build the full 96-slot 24-hour profile **first**, for both arms, before extracting any
   named window.
4. Run N2 before comparing.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file. Record the `C-004`
   observation against `CONTRADICTIONS.md` as evidence, not as a resolution.
