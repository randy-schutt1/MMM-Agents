# DATASETS

Provenance for chart data used in manual backtesting.

## STATUS: EMPTY

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

## LATER: DATASET GOVERNANCE (PHASE 4+)

When automation begins, data is divided into **development**, **validation**,
**holdout**, and **forward** sets, with all boundaries recorded in
`00_SYSTEM/DECISIONS.md`.

Holdout data is not inspected repeatedly during tuning — that silently converts it
into development data and destroys the only honest estimate of generalization the
project will have.
