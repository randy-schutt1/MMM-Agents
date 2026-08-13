# PT-015 — Does a ceiling exist? Excursions beyond 50 pips versus 25–50

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V04 [00:15:43]; the open question is V04_INTERPRETATION.md §3.3 / Q3
BLOCKERS:   I-007 · D-028 boundary dates unpinned
RELATION:   Directly answers a question the V04 study raised and could not settle.
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

`V04_INTERPRETATION.md` §3.3 states the gap precisely, and flags it as `Q3`:

> *"I1 treats 25–50 as a band with a floor and a ceiling. **Whether >50 pips disqualifies a
> setup is never stated.** The instructor only ever says the dealer goes 25–50; he never
> says 'and not more'. Reading the upper bound as a filter would be an invention. **I1
> therefore asserts the floor and is silent on the ceiling.**"*

That silence is not academic. It changes what condition (a) of the only stated entry rule
in the course admits, and the V04 mastery report lists it among the items the reviewer was
asked to test. **A backtest can answer it where the transcript cannot** — not by deciding
what the instructor meant, but by measuring whether the two populations behave differently.

If >50 pip excursions behave like 25–50 excursions, the ceiling is a distinction without a
difference and the corpus can record that. If they behave differently, the ceiling is a
real boundary that the source happens not to state — and `Q3` becomes a live research
question rather than a footnote.

---

## 2. THE QUESTION

> Do excursions of **>50 pips** beyond the Asian range produce a different subsequent
> distribution from excursions of **25–50 pips**?

Null hypothesis: **they do not.** Excursion magnitude beyond 25 pips carries no additional
information about what follows.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| The box | Asian window 8:30pm–3:00am per the V02 printed table |
| **Strata, fixed now** | **S1: 10–24 pips** · **S2: 25–50 pips** · **S3: 51–100 pips** · **S4: >100 pips** |
| Why these cuts | They are **the instructor's own numbers**, not chosen by this session: 10, 25–50 and 100 are the three severities named at V02 `[00:44:59]`; 25–50 is the criterion at V04 `[00:15:43]` |
| Trigger | First 15m **close** whose excursion beyond the box edge falls in the stratum |
| Decision point | That close. **No later bar is consulted for stratum assignment** — a day is assigned by its *first qualifying* close, so the strata are disjoint and no day is counted twice |
| Direction | Away from the box, matching V04's geometry (breach high → short bias; breach low → long bias) — identical to `PT-001` so the results compose |
| Stop / target | **18 / 50 pips** — V04 `[00:04:43]`, `[00:05:07]`. The instructor's numbers, not fitted, identical to `PT-001` |
| Sample | Target ≥ 30 per stratum. **If a stratum falls short it is reported as `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` and is not merged into a neighbour** |

**Stratum merging is forbidden after the fact.** Collapsing S3 and S4 because S4 came up
thin would be choosing a cut after seeing the data, which is `E09` no matter how reasonable
it looks at the time.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry** per stratum: same window, same session hours, direction matched, same stop/target, same n, 1,000 iterations, seed `20260812`. Each stratum gets its own baseline — a shared one would hide that larger excursions occur on more volatile days |
| **Second — the natural control** | **S1 (10–24 pips)** is the course's own "too small, stays in the box" case. It is the natural low-side comparator for S2 |
| **Third** | Volatility-matched pairing: S2 and S3 days matched on the day's prior true range, so *"bigger excursions happen on bigger days"* cannot masquerade as a ceiling effect |

The third arm decides the test. Excursion size and day volatility are obviously coupled;
without the matching, any difference between S2 and S3 is a statement about volatility.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| S2 and S3 behave alike (volatility-matched) | **There is no ceiling.** `Q3` is answered in the negative on this instrument: the upper bound is a description of the dealer's typical size, not a filter. Record against `V04_INTERPRETATION.md` `Q3` and `A-018`-adjacent machine candidates as **evidence, not as doctrine** — only the course can say what its rule means |
| S3 clearly worse than S2 after matching | A ceiling exists in the data. **This still does not make it the instructor's rule** — it makes `Q3` an important open question with an empirical hint attached |
| S1 behaves like S2 | The floor is the weaker part of the criterion, which would be a surprise worth reporting prominently — it is the half `V04_INTERPRETATION.md` §3.2 says rests on a single prescriptive utterance |
| Everything indistinguishable from N1 | Excursion size carries no information at all, which subsumes the ceiling question and is the most important possible outcome. Report it first, not last |

## 6. MANDATORY SCOPE STATEMENT

> PT-015 compares excursion strata. Like `PT-001`, it tests a **prior** question that the
> Market Maker Method's entry rule presupposes; it is **not** a test of that rule, which
> also requires an M/W second leg (`A-011`, `A-007`) and TDI confirmation (`A-039`) — none
> of which is taught in V01–V06. **No result here may be reported as establishing what the
> instructor meant by "25 to 50".** `Q3` is a question about the source and is closed only
> by the source.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-B is DEVELOPMENT. **Run PT-014 first** — its distribution tells
   you whether S3 and S4 will reach n ≥ 30 at all.
2. Harvest with timestamps from DOM text only.
3. Build the volatility-matched pairing **before** comparing strata outcomes.
4. Run all four strata's baselines before looking at any stratum's result.
5. Write `BT_V04_NNNN.md` from the template, §0 referencing this file.
