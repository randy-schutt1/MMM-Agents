# PT-016 — "Asian range, what is it? 41 pips, that's good. Steve said less than 50"

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V03 [00:44:48]–[00:44:51]; printed card "Asian Range =41" ([00:44:19] slide)
BLOCKERS:   I-007 · D-028 unpinned · PROVENANCE CAVEAT — see §1a, and it is not small
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

Reading his own sample flashcard aloud, the instructor states a **numeric filter on the
box itself** — the only one anywhere in V01–V04:

> *"Asian range, what is it? **41 pips, that's good. Steve said less than 50**."*
> V03 `[00:44:48]`–`[00:44:51]`

and the card prints `Asian Range =41` beside `R = 41.4` (`V03_SOURCE_NOTES.md` §4d).

Every other test in this batch treats the Asian range as a **boundary**. This one treats it
as a **quantity** — and the claim is that the box's *size* determines whether the day is
tradeable at all. That is a different, orthogonal question, and if it holds it is a
first-class filter that would sit upstream of `PT-001`, `PT-015`, `PT-017` and `PT-018`.

### 1a. The provenance caveat, stated before the test rather than after

`V03_INTERPRETATION.md` §7 lists this as a machine candidate and gives the objection:
*"Attributed to prior teaching never captured in V01/V02"*. The instructor is quoting
himself in the third person — *"Steve said"* — from material outside this 21-video library.
So:

- The threshold **is in the corpus**, spoken by the course's author, printed on his own
  card. It is **not** invented by this session, and it is **not** guest material.
- The lesson that established it **is not in this library**, so it cannot be checked
  against its original statement.

**Consequence, binding on the run session:** whatever this test finds, `< 50 pips` may not
enter `12_MASTER_SPEC/` or `13_MACHINE_SPEC/` on the strength of it. It is tested as a
**conditioning variable**, and a favourable result makes it a research finding, not a rule.

---

## 2. THE QUESTION

> Do days whose Asian range is **< 50 pips** produce different subsequent excursion
> behaviour from days whose Asian range is **≥ 50 pips**?

Null hypothesis: **they do not.** Box size carries no information about what follows.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| The box | Asian window 8:30pm–3:00am per the V02 printed table |
| Split | **Arm L: box range < 50 pips** · **Arm H: box range ≥ 50 pips**. The cut is the instructor's, not this session's |
| Reported alongside | The **full box-range distribution** with the 50-pip cut marked, and the outcome measures as a **continuous function of box range** in 10-pip bins — so that if 50 is the wrong cut, the data says where the right one is without anyone having chosen it |
| Outcome measures | (a) maximum excursion beyond the box, in pips; (b) whether the day's extreme forms beyond the box; (c) the `PT-001`/`PT-015` trade proxy — first close 25–50 pips beyond, away-direction, stop 18, target 50 (V04 `[00:04:43]`, `[00:05:07]`) |
| Decision point | Box close (03:00). **Box size is fully known then; nothing after it enters the arm assignment** |
| Sample | ~520 days split across two arms. ≥ 30 per arm expected; reported per arm if not |

The continuous-function reporting is the safeguard. A binary split at a threshold from an
uncapturable lesson invites the reader to believe the threshold; the binned curve shows
whether anything happens at 50 at all.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry** within each arm separately, 1,000 iterations, seed `20260812` |
| **Second — the natural control** | A **random median split** of the same days by box range (i.e. the split point that has no doctrinal claim attached). If the random-median split separates outcomes as well as the 50-pip split does, then 50 is doing nothing that "big box vs small box" does not already do |
| **Third** | Volatility control: box range is correlated with the day's eventual range almost mechanically. Outcome (a) is therefore **also** reported normalised by the day's own true range |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Arm L outperforms arm H, and 50 is near the curve's inflection | The filter has empirical support at this sample. **Still not doctrine** — §1a. Record as a research finding and flag for the lesson that may yet teach it |
| Arm L outperforms but the inflection is elsewhere (say 35) | The *direction* of the claim holds and the *number* does not. Report both plainly; do not adopt 35, which would be this session's number and `D-010`'s exact prohibition |
| No separation | The filter does nothing on GBP/USD at this sample. Report prominently; it removes an attractive-looking parameter from later consideration, which is worth as much as adding one |
| Arms A and B disagree | The box moves an hour between `D-031` arms and its measured range moves with it. Report both; a filter whose input is timezone-sensitive is a filter with a hidden parameter |

## 6. MANDATORY SCOPE STATEMENT

> PT-016 tests a threshold the instructor attributes to teaching **outside this 21-video
> library**. It is not a test of the Market Maker Method entry rule; it conditions a proxy
> trigger on box size. **No result here authorises `< 50 pips` as a course rule**, and any
> report of it carries §1a's caveat in the same paragraph as the number.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-B is DEVELOPMENT. Run **PT-014** first for the excursion
   distribution this test conditions.
2. Harvest with timestamps from DOM text only.
3. Compute the box-range distribution and the random-median control **before** applying the
   50-pip cut.
4. Write `BT_V03_NNNN.md` from the template, §0 referencing this file, with §1a reproduced
   verbatim in its notes.
