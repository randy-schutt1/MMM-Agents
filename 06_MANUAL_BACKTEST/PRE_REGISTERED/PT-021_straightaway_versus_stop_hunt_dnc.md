# PT-021 — DNC and the straightaway test: does a prior opposite-side breach change what follows?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:18:44], [00:18:58], [00:19:06]
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

V02 gives a prohibition **and**, unusually, the binary test that lifts it:

> *"**DNC. Do not counter trade back into the range.**"* `[00:18:44]`
> *"Do not counter right here. This is a straightaway. Why is it a straightaway?
> **Because the dealer didn't make a stop hunt below the box.**"* `[00:18:58]`
> *"But now, **if the dealer comes back in here, that's a trade.** Do not trade back this
> way."* `[00:19:06]`

`V02_SOURCE_NOTES.md` §6 condition 4 records it as *"Qualitative, but **a genuine binary
test**"* — and it is the only genuine binary test in the lesson. `V02_INTERPRETATION.md`
`I27` grades it `EXPLICIT`, Medium-High, the second-highest confidence in the file.

Its discriminator is **entirely mechanical**: *did price breach the opposite side of the box
before this move began, or did it not?* No pattern, no indicator, no undefined noun. The
"stop hunt" label is `A-002`/`A-049` and disputed (`C-006`), and **this test does not use
it** — it uses the geometric event the instructor points at when he says it.

This is the closest the corpus comes to handing the project a **pre-specified control
group**, which is why `BACKTEST_EVIDENCE_STANDARD.md` §2.2 asks for the course's own
contrasts wherever they exist.

---

## 2. THE QUESTION

> Does a directional move out of the Asian range behave differently depending on whether the
> **opposite** edge was breached first?

Null hypothesis: **it does not.** A move out of the box is the same object whether or not
the other side was taken out beforehand.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-B conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| The box | Asian window 8:30pm–3:00am, per the V02 printed table |
| **Class SW ("stop-hunt-first")** | The opposite edge was breached by a 15m close **before** the qualifying move began, same day, after the box closed |
| **Class SA ("straightaway")** | No opposite-edge breach — the day's first excursion is the move itself |
| Qualifying move | First 15m close **≥ 25 pips** beyond an edge (the V04 floor, `[00:15:43]`) after 03:00 |
| Measure 1 — **continuation** | Maximum favourable excursion in the breach direction over the following 4 h and to the 17:00 close |
| Measure 2 — **the DNC test** | Outcome of the **counter-trade** (back into the range): stop 18, target 50 (V04 numbers). The prohibition predicts this loses in class **SA** and is acceptable in class **SW** |
| Measure 3 — **frequency** | Share of days in each class, plus days with neither |
| Decision point | The qualifying close. Class membership depends only on **prior** bars, never on later ones |
| Sample | ~520 days across two classes. ≥ 30 per class expected; reported per class |

**Measure 2 is the test.** DNC is a prohibition, and the only way to test a prohibition
honestly is to price the prohibited trade in both classes — which is what makes this design
a controlled comparison rather than a demonstration.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | **Class SA versus class SW**, which is the course's own contrast: same instrument, same box, same session, same geometry; **only the prior opposite-side breach differs**. This is the single strongest comparator available anywhere in this batch |
| **Second** | **N1 — matched random entry** within each class, direction matched, same stop/target, 1,000 iterations, seed `20260812` |
| **Third** | Volatility control: a day with breaches on both sides is by construction a wider day. Both classes' outcomes are therefore **also** reported normalised by the day's own prior true range |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Counter-trades lose in SA and are viable in SW, after volatility normalisation | **The discriminator works.** V02's binary test earns its place, and the project has its first empirically supported *filter* rather than a filter-shaped sentence |
| Both classes behave alike | The binary distinguishes nothing at this sample. Report prominently — it is the most confidently graded conditional in V02 and its failure would be a significant finding about the lesson |
| The difference disappears under volatility normalisation | The classes differ because two-sided days are wider days, not because of a stop hunt. **The third arm exists for exactly this and it is the likeliest confound in the whole batch** |
| Class SW is rare (< 30 days) | `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`, and extend the window to a new pre-registered range under a **new PT number**, never by stretching this one (`D-027`) |

## 6. MANDATORY SCOPE STATEMENT

> PT-021 tests whether a prior opposite-side breach of the Asian range changes what follows.
> It uses that breach as a **geometric event** and does **not** identify a stop hunt:
> `A-002` is undefined, `A-049` records that the course has never stated a discriminator,
> and `C-006` records that the two guest presenters who tried gave incompatible accounts —
> **both of which are excluded from doctrine by `D-025` and neither of which is used here.**
> This is not a test of the Market Maker Method entry rule, which additionally requires an
> M/W second leg (`A-007`, `A-011`) and TDI (`A-039`).

## 7. TO RUN THIS

1. ~~Close `I-007`; confirm W-B is DEVELOPMENT.~~ **Both resolved — `D-034` closed I-007,
   `D-035` pinned D-028 at 2016-07-01, W-B confirmed inside DEVELOPMENT
   (`COMMON_PROTOCOL.md` §3a). Run the data-QA gate
   (`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`) as a precondition and cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`.** Run `PT-014` first — its excursion
   distribution predicts how many days will fall into class SW.
2. ~~Harvest with timestamps from DOM text only;~~ **Source is the HistData GBP/USD M1
   CSV corpus (`D-036a`), aggregated locally to 15m by
   `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` (`GBPUSD_M15_ARMA.csv` /
   `GBPUSD_M15_ARMB.csv` per `D-031` arm); every quote is a number parsed from the
   checksummed file, per `COMMON_PROTOCOL.md` §2's restated `E06` — no value is read
   from a chart rendering.** Build the Asian box per day, both arms.
3. Assign classes from prior bars only, and **freeze the class assignment file before any
   outcome is computed.**
4. Run N1 and the volatility normalisation before comparing classes.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
