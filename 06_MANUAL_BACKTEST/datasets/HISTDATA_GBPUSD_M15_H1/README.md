# `HISTDATA_GBPUSD_M15_H1` — derived M15 and H1 bars for visual chart study

> **Created:** 2026-08-13 · **Branch:** `feature/m15-h1-chart-backtest`
> **Status:** `DERIVED CORPUS — QA GATE PASSED — BOUNDARIES UNVALIDATED EXTERNALLY`
> **Parent corpus:** `../HISTDATA_GBPUSD_M1/` (`D-036a`)
> **Primary consumer:** `../../tools/mmm_chart_render.py`

---

## ⚠ READ FIRST — THE ONE THING THAT IS NOT WHAT IT LOOKS LIKE

This directory is named for a vendor and a timeframe, and **the vendor does not publish
that timeframe.** HistData.com serves tick and M1 only, on every platform, and says so on
its own FAQ. These bars are **aggregated locally** from the `D-036a` M1 corpus by
`../../scripts/aggregate_m15.py`.

**The bucket boundaries are ours.** They are reproducible, auditable and internally
cross-checked seven ways with every check passing — and they have **never been compared
against an independent vendor's M15 or H1**, because no such file is available from this
source. See `VENDOR_TIMEFRAME_AVAILABILITY.md` for the measurement and the hashes, and
`CROSSCHECK_REPORT.md` §0 for why seven PASSes is a weaker claim than it sounds.

---

## THE RECORD (the fields `../README.md` requires of every dataset)

| Field | Value |
|---|---|
| **Source / platform / feed** | **Derived.** Parent: HistData.com free tier, MetaTrader format, **M1 bid bars** (`D-036a`). No M15 or H1 is published by this vendor. |
| **Instrument** | GBP/USD (`D-007`) |
| **Timeframe(s)** | **M15** and **H1**, both aggregated locally |
| **Date range** | **2013-01-01 17:00 → 2016-06-30 23:45** (M15, Arm A) / **→ 23:00** (H1, Arm A). Arm B spills to `2016-07-01 00:45` (M15) and `00:00` (H1) — see `I-010` Q2 below. |
| **Bars** | M15 **86,824** per arm · H1 **21,708** per arm |
| **Timezone** | **Arm A** = fixed UTC−5, no DST (the corpus's native stamp). **Arm B** = `America/New_York`, DST-tracking. `D-031`. |
| **Retrieved / built** | **2026-08-13**, from the M1 files hashed in `../HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` |
| **Integrity** | **SHA-256 per file** in `derived/SHA256SUMS.txt` — **committed**, unlike the parent's (see "A gap in the parent's provenance" below) |
| **QA** | `QA_REPORT_{M15,H1}_ARM{A,B}.txt` — **C0–C4 and C9 PASS on all four files.** C5–C8 are reports and need human sign-off. |
| **Cross-check** | `CROSSCHECK_REPORT.md` (+ `.txt`) — X1–X7, all clean |
| **Aggregation rule** | Open of the first M1 bar in the window · High = max · Low = min · Close of the last. A bucket is emitted **only if at least one M1 bar falls inside it** — holidays and weekends stay absent rather than becoming synthetic flat candles. |
| **Volume** | **Structurally zero** in the parent data. Carried for format compatibility. **It is not traded volume and no test or chart may read it.** |
| **Location** | Bars gitignored; **provenance, hashes, QA and cross-check reports committed.** |

### Files

```text
derived/GBPUSD_M15_ARMA.csv    86,824 bars   gitignored
derived/GBPUSD_M15_ARMB.csv    86,824 bars   gitignored
derived/GBPUSD_H1_ARMA.csv     21,708 bars   gitignored
derived/GBPUSD_H1_ARMB.csv     21,708 bars   gitignored
derived/SHA256SUMS.txt                       COMMITTED
QA_REPORT_M15_ARMA.txt  QA_REPORT_M15_ARMB.txt   COMMITTED
QA_REPORT_H1_ARMA.txt   QA_REPORT_H1_ARMB.txt    COMMITTED
CROSSCHECK_REPORT.md  CROSSCHECK_REPORT.txt      COMMITTED
VENDOR_TIMEFRAME_AVAILABILITY.md                 COMMITTED
_evidence/                  captured vendor pages, gitignored, hashed in-place
```

Column format is the parent's, unchanged: `YYYY.MM.DD,HH:MM,O,H,L,C,V`.

---

## THE HOLDOUT WAS NEVER TOUCHED

`D-035` pins DEVELOPMENT/HOLDOUT at **2016-07-01**. The parent M1 corpus was truncated at
`2016.06.30` **on arrival** and no post-boundary row has ever been on disk. **These files
inherit that and add nothing** — they are aggregations of a corpus that stops at the
boundary, so no post-boundary bar can exist to aggregate. `E23` did not occur here and
could not have.

The one nuance, already on the register: under **Arm B** the `+1h` DST shift relabels the
last few Arm A bars to a wall-clock stamp of `2016-07-01` — **4 bars at M15** (recorded in
`I-010` Q2) and **1 bar at H1** (measured here). No new data is involved; it is the same
development-side minutes wearing a different clock. `I-010` Q2 asks which clock the `D-035`
boundary is stated in and **the owner call is still owed.**

---

## THE `D-031` ARMS ARE FREE AT THESE TIMEFRAMES — AND `A-019` IS UNTOUCHED

Measured over every bar (`CROSSCHECK_REPORT.md` §2): Arm A and Arm B produce **bar-for-bar
identical candles** at M15 and H1. Only the timestamp label moves, by exactly `0h` or `+1h`.

This holds because the shift is a whole hour and both 15 and 60 divide 60, so the shift maps
the bucket grid onto itself. **It will not hold at a timeframe that does not divide an
hour.** Do not generalise it.

What it means in practice: **the arm cannot change an EMA value, a TDI value or a bar range
at these timeframes. It changes only which SESSION a bar falls in.** So `A-019` — the
course states a session table and no timezone, still `OPEN`, still `DO NOT CODE` — bears on
every session-boundary claim and on nothing measured off the candles themselves. Both arms
are still built, and `D-031` still requires both be reported for anything session-dependent.

---

## KNOWN DEFECTS THAT SURVIVE INTO THESE FILES — BY DESIGN

An aggregation that made these disappear would be worse than the defects.

- **The 2014-06-01/02 hole.** ~22 trading hours absent (Sun 17:00 → Mon 15:01, Arm A).
  Present at both timeframes. `C9` is a **gating check that fails if it stops being
  visible.** Any window spanning it must exclude it by name and count the exclusion — and
  `mmm_chart_render.py` stamps a warning on any image that spans it, so the flat stretch is
  never mistaken for a quiet market.
- **Nine Dec/Jan short sessions** — genuine market closures, not defects. A partial session
  still cannot support a full-window measurement.
- **Three weeks closing on a Thursday** — `2015-12-20`, `2015-12-27`, and `2016-06-26` (the
  last an artifact of this corpus's truncation at the `D-035` boundary). Under Arm B at H1
  the count reads 2, for the `I-010` Q2 reason above.
- **Spikes are real events.** The H1 census's largest is `2016-06-23 23:00`, 959 pips — the
  EU referendum, inside DEVELOPMENT per `D-035`. **Nothing is excluded.**

---

## PRICE LEVELS ARE NOT COMPARABLE WITH THE V02–V06 FXCM HOMEWORK

Inherited from `D-036a` and unchanged: FXCM serves no 2013–2016 GBP/USD, so the
cross-vendor level offset cannot be measured for these windows. **Only shape and distance
claims travel.** A chart rendered from this corpus may be compared with a course screenshot
for *shape*; its *levels* may not be read across.

---

## A GAP IN THE PARENT'S PROVENANCE, FOUND WHILE BUILDING THIS

`D-036a` cites `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` as its integrity evidence.
**That file is in no branch of this repository.** The old `.gitignore` rule
`06_MANUAL_BACKTEST/datasets/**` had only two exceptions and swallowed it, so the manifest
exists only on the machine that built the corpus. A checksum nobody else holds cannot verify
anything, and a decision entry citing it is citing something a reviewer cannot open.

This branch fixes the rule — provenance files (`*.md`, `QA_REPORT*.txt`, `SHA256SUMS.txt`)
are now un-ignored while the bars stay out — and commits this dataset's manifest
accordingly. **The M1 dataset's own manifest is still uncommitted and is owed the same
treatment**; doing it means force-adding a file this session did not produce, on a branch
that does not own that corpus, so it is flagged rather than done.

---

## REPRODUCING THE WHOLE THING

```bash
RAW=06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/raw
OUT=06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M15_H1/derived

for tf in 15 60; do for arm in A B; do
  python3 06_MANUAL_BACKTEST/scripts/aggregate_m15.py "$RAW" --arm $arm --timeframe $tf \
      --out "$OUT/GBPUSD_$([ $tf = 15 ] && echo M15 || echo H1)_ARM$arm.csv"
done; done
```

Then the gate, which is a **precondition on drawing any study window** from these files:

```bash
python3 06_MANUAL_BACKTEST/scripts/qa_histdata_htf.py "$OUT/GBPUSD_M15_ARMA.csv" --timeframe 15 --arm A
```

and the cross-check, per `CROSSCHECK_REPORT.md` §5.

---

## WHAT THIS CORPUS IS FOR — AND THE LINE IT MUST NOT CROSS

It exists to feed `../../tools/mmm_chart_render.py`, which draws study charts for
**pattern-recognition practice**. That is a different activity from the PT-series numerical
backtests, and the distinction is not cosmetic:

- A PT test **states a prediction in advance**, pre-registers it, runs it once, and reports
  what it gets. The discipline exists because a hypothesis revisable after seeing the data
  is not a hypothesis.
- The renderer **makes no prediction**, so there is nothing to pre-register — **and
  therefore produces no evidence.** Studying two hundred windows and forming an impression
  is not a finding, closes no ambiguity, and may not be cited in a mastery report.

Nothing stops this corpus being used for a numerical test later; if it is, that test carries
the full PT discipline, and `E06` applies as always — **a chart may be looked at; nothing
may be measured off one.**
