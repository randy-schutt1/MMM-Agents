# PT-002 — Do GBP/USD turning points cluster at the six boundaries V01 names?

```text
STATUS:      PARTIALLY NON-CONFORMING UNDER D-035 — THE W-C ARM IS SUPERSEDED BY PT-025,
             2026-08-13. THE W-A ARM IS UNAFFECTED AND STAYS RUNNABLE IN THIS FILE.
             NEVER RUN. NOT EDITED INTO CONFORMANCE. RETAINED, NOT DELETED.

             READ THIS BEFORE RUNNING ANYTHING FROM THIS FILE:
               - W-A arm (2015-01-04 -> 2015-12-31, DAILY extremes): CONFORMS. It lies
                 wholly inside D-035 DEVELOPMENT and is RUNNABLE under D-036a. Run it
                 from this file.
               - W-C arm (2013-01-06 -> 2017-12-29, WEEKLY extremes): NON-CONFORMING.
                 DO NOT RUN IT FROM THIS FILE. It is re-issued as PT-025 on
                 W-C' = 2013-01-06 -> 2016-06-30.

             WHY, AND A DEFECT IN D-035 THAT IS RECORDED RATHER THAN CORRECTED HERE:
             D-035 pins the project-wide D-028 split at 2016-07-01 -- DEVELOPMENT
             2013-01-06 -> 2016-06-30, HOLDOUT 2016-07-01 -> 2017-12-29 -- and its
             consequence-1 conformance table lists PT-002 among the CONFORMING tests.
             THAT IS WRONG. Section 3 of this file declares TWO windows, and the second
             of them is W-C, which straddles the boundary by 546 days exactly as
             PT-008 ... PT-013 and PT-019 do. INDEX.md 1 has recorded this file's window
             as "W-A, W-C" since the batch was written. D-035 classified the file by its
             first window and missed the second, so the re-issue obligation it created
             was one test short.

             The correction is written up in PRE_REGISTERED/_PROPOSED_DECISION_REISSUE.md
             for the owner to integrate. NO SESSION MAY EDIT DECISIONS.md TO FIX IT BY
             SIDE-EFFECT.

             D-027 requires that a range change create a NEW TEST ID with the abandoned
             test retained and marked. PT-025 carries the W-C arm's question, six
             boundaries, proximity bands, nulls, seed and scope onto W-C', and declares
             as costs rather than as details everything the substitution changes:
               - data source: HistData GBP/USD M1 CSV corpus (D-036a), not TradingView
                 / FXCM (D-034);
               - week open: 22:00 UTC (Sunday 17:00, fixed UTC-5, no DST), NOT 21:00 UTC
                 -- which matters here because two of the six boundaries ARE the week
                 boundary;
               - the trading week is 120 hours and is NOT five equal days (Sunday 7h,
                 Friday 17h), so the covered-fraction expectation must be
                 exposure-weighted;
               - sample: 180 TRADING weeks x 2 extremes = 360, not the ~520 claimed in
                 3 below. W-C' holds 182 calendar Sundays but only 181 observable
                 Sunday week opens, and the week of 2014-06-01 is EXCLUDED BY NAME --
                 the corpus is absent from Sun 2014-06-01 17:00 to Mon 2014-06-02
                 15:01 (~22 hours), so neither week boundary can be placed. Surfaced
                 by QA check C8, which was ADDED AFTER PT-025 was drafted.

             NOTHING IN THIS FILE WAS CHANGED except this status block.

--- original status block, as pre-registered 2026-08-12, unchanged ---
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V01
BLOCKERS:   I-007 (no data source declared) · D-028 boundary dates unpinned
ATTESTATION: No chart in W-A or W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md` (units, harvest rule, windows, arms, nulls, seed).
Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

V01's slide at `[00:30:35]` prints a **closed list of six** trap-move locations:

```text
Beginning Of The Week (Sun / Mon)   Beginning Of The Day
Beginning Of The Session            End Of The Session
End Of The Day                      End Of The Week
```

Every one of the six is a **clock time**. Not a pattern, not an indicator, not a
definition the course owes and has not paid. That makes this the rarest thing in the
corpus: a `VISUAL` + `EXPLICIT` instructor claim (`V01_INTERPRETATION.md` §10.1 U5) that
can be tested without approximating anything.

It is also the claim the rest of the method leans on hardest. If turning points do **not**
concentrate at session boundaries on GBP/USD, then "timing and pattern, pattern and
timing — interchangeable" (V02 `[00:48:41]`) has no timing half, and every session-gated
rule downstream inherits that.

> The V01 interpretation records that this session's predecessor **over-generalised** the
> spoken enumeration into "every session boundary" and the slide refuted it (`G5`, §10.1
> U5). This test uses **the slide's six, and only the six.**

---

## 2. THE QUESTION

> Do daily and weekly extremes on GBP/USD form disproportionately close to the six
> printed boundaries, relative to the same measurement on a randomly re-labelled clock?

Null hypothesis: **they do not.** Extreme timestamps are distributed across the trading
day and week no differently from what a shifted clock produces.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Windows | **W-A** (2015-01-04 → 2015-12-31) for daily extremes; **W-C** (2013-01-06 → 2017-12-29) for weekly extremes |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` (`COMMON_PROTOCOL.md` §3a) |
| Timezone | **Both `D-031` arms**, always reported |
| The six boundaries | Week open; day open; session open; session close; day close; week close — **placed from the V02 printed table** (`COMMON_PROTOCOL.md` §4). London and New York opens/closes are the "session" boundaries; the Asian open at 8:30pm is included as a session boundary |
| Measured object | The timestamp of (a) each day's high and low; (b) each week's high and low |
| Proximity band | **±30 minutes** of a boundary, pre-registered. Reported **also** at ±15 and ±60 as a pre-registered sensitivity, all three every time |
| Decision point | None — this is a distributional measurement, not an entry test |
| Sample | ~260 days × 2 extremes (W-A); ~260 weeks × 2 extremes (W-C). Comfortably ≥ 30 |

**No entry, no stop, no target.** This test measures *where in the clock* the market turns.
It does not trade.

### 3a. The arithmetic that must be reported alongside the result

Six boundaries × a ±30-minute band = **6 hours of a 24-hour day** on the widest reading,
before overlaps are removed. A clustering result is meaningless unless the *expected*
share under the null is stated in the same table as the observed share. **Report the
overlap-corrected covered fraction of the trading week explicitly.** A finding of "41% of
extremes fall in the bands" against an expected 38% is a null result, and must be written
as one.

## 4. BASELINE

| Arm | Null | Purpose |
|---|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812` | The price path is untouched; only the clock labels move. This isolates the claim exactly: does *the clock* carry the information? |
| **Second** | **N3 — week-anchor shift** (weekly extremes only), 1,000 draws | Same logic at week scale |
| **Third** | Uniform-time expectation, computed analytically | A sanity check on N2; a large disagreement between them is a bug, not a finding |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Observed share indistinguishable from N2 | **The six boundaries carry no detectable timing information on GBP/USD at this sample.** A foundational null — report prominently, do not bury |
| Clustering at some boundaries, not others | The most likely real outcome and the most useful. Report the per-boundary breakdown; a method that works at London open and not at day close is a narrower method, not a broken one |
| Clustering at all six | Necessary support for every session-gated rule in V01–V04. **Not** evidence that any entry rule works |
| Arms A and B diverge | A `D-031` finding in its own right — report both, state the overlap, conclude nothing about which timezone is "right" |

## 6. MANDATORY SCOPE STATEMENT

> PT-002 tests whether GBP/USD turning points cluster at six printed clock boundaries. It
> is **not** a test of the Market Maker Method's trap move, which is `A-002` and remains
> undefined as a pattern. A favourable result supports the *premise* that timing carries
> information. It says nothing about whether a trap move can be recognised at the hard
> right edge, and nothing about any entry.

## 7. TO RUN THIS

1. Close `I-007`; confirm the windows sit inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a).
2. Harvest 15m bars with timestamps, DOM text only (`COMMON_PROTOCOL.md` §2).
3. Compute both `D-031` arms' boundary sets before touching the extreme timestamps.
4. Run N2/N3 and record their distributions **before** looking at the observed share.
5. Write `BT_V01_NNNN.md` from the template, §0 referencing this file.
