# DATASETS

Provenance for chart data used in manual backtesting.

## STATUS: ONE DATASET REGISTERED

| Dataset | Governing decision | Directory |
|---|---|---|
| HistData GBP/USD M1, 2013 → 2016-H1 | `D-036a` | `HISTDATA_GBPUSD_M1/` |

## WHAT LIVES HERE

Documentation, not bulk data. Raw price files are gitignored (`*.csv` dumps,
`*.parquet`, `*.db`) — record where the data came from, not the data itself.

A small, intentional sample may be force-added with `git add -f` when it is
genuinely needed to reproduce a specific observation.

## RECORD FOR EACH DATASET

| Field | Why |
|---|---|
| Source / platform / broker feed | Different feeds differ at the candle level |
| Instrument | GBP/USD unless the course requires otherwise |
| Timeframe(s) | |
| Date range | |
| Timezone | Session boundaries are meaningless without it |
| Retrieved on | |
| Notes | Gaps, weekend handling, DST behaviour, known anomalies |

## REGISTERED: `HISTDATA_GBPUSD_M1`

Declared by **`D-036a`** (2026-08-13), which amends `D-034` for the pre-registered
historical windows only. TradingView / FXCM remains the standing source for recent and
live chart work.

| Field | Value |
|---|---|
| Source / platform / feed | **HistData.com**, free tier, no account, no login. `MetaTrader` format, **M1 bid bars** |
| Instrument | GBP/USD (`D-007`) |
| Timeframe(s) | **M1** as retrieved; **M15** derived locally per `D-031` arm by `../scripts/aggregate_m15.py` |
| Date range | **2013-01-01 17:00 → 2016-06-30 23:59** — 1,297,781 M1 bars |
| Timezone | **Fixed UTC−5 ("EST"), no DST.** Week open **Sunday 17:00 = 22:00 UTC**, year-round. This is `D-031` **Arm A natively**; Arm B is `+1h` during US DST |
| Retrieved on | **2026-08-13**, HTTP POST to the vendor's public `get.php` form endpoint |
| Integrity | **SHA-256 per file** in `raw/SHA256SUMS.txt` |
| QA | `QA_REPORT.txt` — C1–C4 **PASS**; C5–C7 reviewed and signed off in `D-036a` |

### Notes — gaps, weekend handling, DST, known anomalies

- **Holdout never on disk.** The vendor publishes past years whole. The 2016 file was
  truncated at `2016.06.30` **on arrival** (186,608 post-boundary rows discarded,
  untruncated CSV and zip deleted, nothing past the boundary ever read). `D-035`'s holdout
  is intact. **Any session extending this corpus must repeat that or record the breach.**
- **Weekends** are absent by construction, not gaps. 187 week opens detected.
- **Intra-week gaps:** only 3 at ≥ 30 minutes, 4h43m total across 3.5 years.
- **DST:** none. Modal week open is 17:00 in all twelve months.
- **Volume is structurally zero** in this vendor's data. Carried for format compatibility.
  **It is not traded volume and no test may read it.**
- **Spikes are real events, not corruption.** Only six days contain any M1 bar over 100
  pips; 26 such bars fall on **2016-06-23** (EU referendum, inside DEVELOPMENT per
  `D-035`). Nothing is excluded.
- **Price levels are NOT comparable with the V02–V06 FXCM homework.** FXCM serves no
  2013–2016 data, so the `D-034` cross-vendor offset cannot be measured for these windows.
  Only *shape* and *distance* claims travel. See `D-036a`.
- **Open clock questions:** `SETUP_ISSUES.md` `I-010`.

## LATER: DATASET GOVERNANCE (PHASE 4+)

When automation begins, data is divided into **development**, **validation**,
**holdout**, and **forward** sets, with all boundaries recorded in
`00_SYSTEM/DECISIONS.md`.

Holdout data is not inspected repeatedly during tuning — that silently converts it
into development data and destroys the only honest estimate of generalization the
project will have.
