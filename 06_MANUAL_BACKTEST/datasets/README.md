# DATASETS

Provenance for chart data used in manual backtesting.

## STATUS: TWO DATASETS REGISTERED

| Dataset | Governing decision | Directory |
|---|---|---|
| HistData GBP/USD M1, 2013 → 2016-H1 | `D-036a` | `HISTDATA_GBPUSD_M1/` |
| **Derived** GBP/USD **M15 + H1**, both `D-031` arms | `D-036a` (parent); no new decision — it introduces no new source | `HISTDATA_GBPUSD_M15_H1/` |

> ⚠ **The second is DERIVED, not imported.** HistData publishes **tick and M1 only** — its
> own FAQ: *"We can only deliver you time ordered Tick and M1 (1 minute) data."* Measured
> and hashed at `HISTDATA_GBPUSD_M15_H1/VENDOR_TIMEFRAME_AVAILABILITY.md`. Those M15/H1
> bucket boundaries are **ours**: reproducible, internally cross-checked seven ways, and
> **never compared against an independent vendor's bars.** Read that directory's `README.md`
> before citing anything built on it.

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
- **Weekends** are absent by construction, not gaps. **181 Sunday-delimited week opens**
  (not 187 — that earlier figure counted mid-week holiday re-opens as week opens; see the
  second correction block in `D-036a`). Also present: **6 intra-week re-opens**, which are
  **never** week boundaries, and **3 weeks that close on a Thursday** (`2015-12-20`,
  `2015-12-27`, and `2016-06-26` — the last an artifact of this corpus's truncation at the
  `D-035` boundary, not a market closure).
- **Intra-week gaps:** only 3 at ≥ 30 minutes, 4h43m total across 3.5 years.
- **ONE UNEXPLAINED HOLE — `2014-06-01` / `2014-06-02`.** The corpus is absent from
  **Sun 2014-06-01 17:00 to Mon 2014-06-02 15:01**, ~22 continuous hours covering a full
  week open plus a Monday Asian and London session. It is the only unexplained absence in
  the corpus. **Any test whose window spans it must exclude it by name and count the
  exclusion.** Found by `C8`, which was added *after* the first QA sign-off missed it —
  see the correction block in `D-036a`.
- **Nine Dec/Jan short sessions** are genuine market closures, not defects — but a partial
  session still cannot support a full-window measurement, so the same
  explicit-disposition rule applies.
- **Calendar weeks ≠ trading weeks.** W-C′ holds **182 calendar Sundays** → **181
  calendar-complete Sun→Fri weeks** → **180 trading weeks** once the 2014-06-01 hole is
  excluded. Any `n` denominated in "weeks" must say which of the three it counts; the
  re-issued tests `PT-025`–`PT-032` are denominated in **trading weeks**.
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
