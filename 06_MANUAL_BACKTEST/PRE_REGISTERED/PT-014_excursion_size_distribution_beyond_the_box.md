# PT-014 — Is 25–50 pips actually the modal excursion beyond the Asian range?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V04 [00:10:01], [00:14:36], [00:15:43]; V02 [00:44:59], [00:43:45]
BLOCKERS:   I-007 · D-028 boundary dates unpinned · A-019 handled by D-031 arms
RELATION:   Supplies the distribution PT-001 assumes a band inside of. Run this FIRST.
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

`PT-001` tests whether excursions of **25–50 pips** beyond the Asian range carry
information. It takes the band from the instructor:

> *"The dealer vectors **25 to 50 pips** above the agent's [Asian] psychological resistance
> level"* V04 `[00:10:01]`; *"**25 to 50 pips above and below the blue box**"* `[00:15:43]`

**Nobody has checked whether that band describes GBP/USD.** And V02 says plainly that it
often does not:

> *"They change the severity of the stop hunt: 25 to 50 pips. **Maybe they'll only do 10
> pips** and it won't come out of the box and you'll be confused… **Then they'll do it 100
> pips.**"* `[00:44:59]`
> *"Sometimes they'll be below the box. Sometimes they won't. You'll miss them."* `[00:43:45]`

So the course's own position is that the band is **typical, not definitional**. Measuring
the actual distribution is prerequisite work: if the GBP/USD mode sits at 12 pips, PT-001's
band selects a tail and its sample will be small and unrepresentative — and it is far
better to know that before PT-001 runs than after it returns an odd `n`.

This is descriptive work in the service of the tests around it, and it is cheap.

---

## 2. THE QUESTION

> What is the distribution of maximum daily excursion beyond the Asian range on GBP/USD,
> and where does 25–50 pips sit within it?

Null hypothesis (weak, and the useful one): **the 25–50 band is not modal** and holds no
special position in the distribution.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| The box | High and low of the Asian window **8:30pm – 3:00am**, exactly as the V02 slide prints it (`COMMON_PROTOCOL.md` §4) |
| Measure 1 | Maximum excursion beyond the box high, and beyond the box low, per day, in pips |
| Measure 2 | Histogram in **5-pip bins from 0 to 150+**, with the 10 / 25–50 / 100 figures the instructor names marked on it |
| Measure 3 | Share of days with **no** excursion beyond either edge — the *"it won't come out of the box"* case, which is a real category and is usually invisible in a study that only looks at triggers |
| Measure 4 | Whether the first excursion of the day is the larger one, and the time of day of the maximum |
| Measure 5 | Excursion size scaled by the box's own range, dimensionless — the version that survives a change of volatility regime |
| Decision point | None — distributional |
| Sample | ~520 days × 2 edges. ≥ 30 satisfied by a wide margin |

**Every day is included**, including days with zero excursion. A distribution conditioned on
having a trigger is the exact distribution that makes a band look inevitable.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N2 — circular clock shift**, 1,000 draws, seed `20260812`: the same excursion measurement against a **sham box** built from an equally-long window placed at a random hour. Tests whether the *Asian window* box has a distinctive excursion profile or whether any 6.5-hour box does |
| **Second** | Volatility normalisation: the same histogram expressed in units of the day's own true range, so 2014 and 2015 regimes are comparable |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| The mode lies inside 25–50 | The instructor's band describes GBP/USD. **PT-001's band is sound and its sample will be representative** |
| The mode lies well below 25 | PT-001 is selecting a tail. That does not invalidate PT-001 — the rule is what it is — but the finding must be carried into PT-001's report, and PT-015's ceiling question becomes more urgent |
| The distribution is indistinguishable from the sham-box control | **The Asian window has no distinctive excursion profile**, which would be a serious negative for the box concept itself and should be read alongside PT-001's third arm |
| Arms A and B give different modes | A `D-031` finding: the box moves an hour, and the excursion profile moves with it. Report both |

## 6. MANDATORY SCOPE STATEMENT

> PT-014 measures how far GBP/USD travels beyond a fixed-window range. It is **not** a test
> of the stop hunt (`A-002`/`A-049` — undefined, and disputed between two guest accounts in
> `C-006`), **not** a test of the "vector" (`A-035`), and **not** a test of any entry rule.
> It is a distribution, reported as a distribution, and it is `DESCRIPTIVE` under
> `BACKTEST_EVIDENCE_STANDARD.md` §5 regardless of what it shows.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-B is DEVELOPMENT.
2. Harvest with timestamps from DOM text only; build the Asian box per day for both arms.
3. Build the sham-box control before reading the real histogram.
4. **Run this before PT-001, PT-015, PT-016, PT-017 and PT-018**, all of which use the same
   box and inherit this distribution's shape.
5. Write `BT_V04_NNNN.md` from the template, §0 referencing this file.
