# DATASETS

Provenance for chart data used in manual backtesting.

## STATUS: ONE DATASET REGISTERED

| Dataset | Governing decision | Directory |
|---|---|---|
| HistData GBP/USD M1, 2013 → 2016-H1 | `D-036a` | `HISTDATA_GBPUSD_M1/` |
| …**extended** 2017 → 2025, M1 + derived M15/H1 | `D-044` | `HISTDATA_GBPUSD_M1/` (`raw/`, `derived_ext/`) |

> **⚠ THE SAME DIRECTORY NOW HOLDS TWO POLICY BLOCKS.** `2013-01-06 → 2016-06-30` is `D-035`
> DEVELOPMENT; `2017-01-01 → 2025-12-31` is the `D-044` extension, released by the owner for
> forward-testing and backtesting. `2016-07-01 → 2016-12-31` is **still a sealed `D-035`
> holdout and is not on disk.** Loading code defaults to DEVELOPMENT and the extension must be
> named to be reached — see the `D-044` section below, and `D-044` §2 in `DECISIONS.md`.

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

## REGISTERED: THE `D-044` EXTENSION — 2017 → 2025

Declared by **`D-044`** (2026-08-14) on the owner's ruling *"This can be used to forward test
and backtest. Pull 2017-2025 if that's easiest."* Same vendor, same product, same `get.php`
method as `D-036a`. **`D-036a`'s four files are untouched and their SHA-256 is unchanged.**

| Field | Value |
|---|---|
| Files | `raw/DAT_MT_GBPUSD_M1_{2017…2025}.csv` — nine full-year files |
| Retrieved | **2026-08-14** |
| Span | **2017-01-02 02:00 → 2025-12-31 16:57** · 3,297,475 rows served, **3,297,055** after de-duplication |
| Corpus total | **13 files, 4,594,836 M1 bars**, 2013-01-01 → 2025-12-31 |
| Derived | `derived_ext/GBPUSD_M15_ARM{A,B}.csv` **307,576** bars/arm · `derived_ext/GBPUSD_H1_ARM{A,B}.csv` **76,901** bars/arm, continuous 2013 → 2025 |
| Integrity | `raw/SHA256SUMS.txt`, `derived_ext/SHA256SUMS.txt` — **both committed** |
| QA | `QA_REPORT_EXT.txt` **PASS** (as consumed) · `QA_REPORT_EXT_RAW.txt` **FAIL** (as served — kept deliberately, see below) |

### Usage policy — read this before loading anything

- **`2013-01-06 → 2016-06-30`** — `D-035` DEVELOPMENT. Unchanged.
- **`2016-07-01 → 2016-12-31`** — `D-035` HOLDOUT, **STILL SEALED, NOT ON DISK.** This is now
  the project's *only* intact holdout, and it carries the October 2016 flash crash.
- **`2017-01-01 → 2017-12-29`** — was `D-035` HOLDOUT, **RELEASED** by `D-044`. It is no
  longer out-of-sample and **must not be cited as such.**
- **`2017-12-30 → 2025-12-31`** — outside `D-035`'s corpus entirely. Available.

`mmm_lib.load_m1()` / `load_m15()` **default to DEVELOPMENT**; pass `scope="extended"` to reach
the `D-044` years. Every pre-`D-044` runner therefore behaves exactly as it did — verified: all
25 re-run byte-identical (`D-044` §6).

### Notes — what differs from 2013-2016, and it is not nothing

- **⚠ A DUPLICATED HOUR, EVERY YEAR FROM 2019.** The vendor emits `19:00`-`19:59` **twice** on
  the EU fall-back Sunday — 2019-10-27, 2020-10-25, 2021-10-31, 2022-10-30, 2023-10-29,
  2024-10-27, 2025-10-26; **420 rows**. 2013-2018 have **zero** duplicate stamps. All 420 pairs
  carry **identical OHLC**, which is the only reason removing the copy is admissible; the
  loaders check that identity and **refuse to run** if a duplicated stamp ever carries a
  different bar. **The raw CSVs are not edited** — they still match `raw/SHA256SUMS.txt`, and
  `QA_REPORT_EXT_RAW.txt` is committed *failing* so the defect stays visible.
- **⚠ 2023-02-26 → 2023-07-23 IS MATERIALLY DEGRADED.** 2023 is ~13% light (322,467 bars vs a
  ~372,000 median) with **672 intra-week gaps totalling 32 d 15 h** — every other year in the
  corpus has ≤ 7 gaps and ≤ 7 h. For scale, the `2014-06-01` hole `D-036a` flagged is 22 hours.
  **Any test spanning this block needs an explicit pre-registered disposition, and the honest
  default is to exclude it by name and count the exclusion.**
- **⚠ THE 17:00 WEEK OPEN DOES NOT CARRY FORWARD BY NAME PAST 2018.** 23 week opens sit at 16h,
  all inside the March/October windows where US and EU DST disagree. The `D-036a` corpus has
  **0 of 181** off-hour opens; 2017 and 2018 have none. Pooled across all nine years the modal
  open is still 17h in all twelve months and there is **no seasonal shift** — but a
  week-boundary test on 2019+ must state its convention rather than inheriting `W-C′`'s.
- **Format holds otherwise:** column layout, 6-d.p. quotes, **structurally zero volume** (still
  not traded volume, still unreadable by any test), and `C4` OHLC coherence all pass on
  3,297,475 / 3,297,475 rows.
- **Other unexplained short sessions,** named so nobody rediscovers them: `2019-05-26` (absent),
  `2019-05-27`, `2020-11-30` (300 bars), `2021-05-31` (239 bars), `2023-03-17`, `2023-03-24`,
  `2023-04-06`, `2023-04-07` (absent).
- **Price levels remain NOT comparable with the V02-V06 FXCM homework** (`D-034` fact 2,
  `D-036a`). Unchanged by this extension.
- **2026 was not pulled.** The current year is partial and moves between fetches.

## LATER: DATASET GOVERNANCE (PHASE 4+)

When automation begins, data is divided into **development**, **validation**,
**holdout**, and **forward** sets, with all boundaries recorded in
`00_SYSTEM/DECISIONS.md`.

Holdout data is not inspected repeatedly during tuning — that silently converts it
into development data and destroys the only honest estimate of generalization the
project will have.
