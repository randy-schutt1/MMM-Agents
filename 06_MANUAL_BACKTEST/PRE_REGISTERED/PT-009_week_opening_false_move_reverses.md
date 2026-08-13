# PT-009 — Does the first move out of the week's opening range reverse?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V01 [00:38:27], [00:38:39], [00:39:53], [00:43:07]; V02 [00:09:44]–[00:09:51], [00:14:17]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

*"Do not take the first move of the week"* is **the clearest instruction in V01** — stated
three times as a prohibition (`V01_INTERPRETATION.md` I1, `EXPLICIT`, High confidence) —
and V02 supplies the mechanism:

> *"They are where the false move, where the dealer traps the traders."* `[00:09:44]`
> *"If they make the false move… and you bite on that… they are now trapped for the entire
> week."* `[00:14:17]`

A prohibition is only justified if the thing prohibited loses. **This test asks whether it
does.** And it can be asked without defining a single blocked term, because PT-008 supplies
a measurable referent for "the first move": the first breach of the week's first-eight-hours
range (V03 `[00:12:46]`), which is the object V01's *"the first move out of the box"*
`[00:43:07]` most plausibly names and which V03/V04 make drawable.

> **The referent substitution is disclosed, not hidden.** V01's *"the box"* is `A-006` and
> its referent is open. This test does **not** claim to have resolved it. It tests a
> specific, drawable object and says so in §6 — which is the difference between an
> operationalisation and an approximation (`D-030`).

---

## 2. THE QUESTION

> After the first breach of the week's opening eight-hour range, does price return through
> the range and set the week's extreme on the **breach** side — more often than a matched
> control?

Null hypothesis: **it does not.** The first breach continues as often as it reverses.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute, with 4-hour for the block |
| Window | **W-C** — 2013-01-06 → 2017-12-29 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Trigger | First 15m **close** beyond the first-eight-hours range (PT-008's block), either side |
| Decision point | That close. **No later bar is consulted for classification** |
| Outcome 1 — **reversal** | Does price subsequently trade back through the **opposite** edge of the block before the week's close? |
| Outcome 2 — **trap geometry** | Is the week's extreme on the breach side, and does it form within X hours of the trigger? `X` reported as a distribution, **not** pre-set |
| Outcome 3 — **the prohibition priced** | Counterfactual position taken **in the breach direction** at the trigger, stop 18 pips, target 50 pips (V04 `[00:04:43]`, `[00:05:07]` — the instructor's own numbers, not fitted). This is what taking the forbidden trade would have cost or paid |
| Sample | ~260 weeks, one trigger each. ≥ 30 satisfied |

Outcome 3 is the heart of it. **The prohibition is a claim that this trade loses**, and the
only honest way to test a prohibition is to price the prohibited trade.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry** in the same weeks and the same session hours, direction matched to the breach, same stop/target, 1,000 iterations, seed `20260812` |
| **Second** | **N3 — week-anchor shift**, 1,000 draws. Answers whether the effect belongs to *the week's opening range* or to *any* range breach |
| **Third — the natural control** | **Second and later** breaches of the same block in the same week, measured identically. This is the course's own contrast: V01 forbids the *first* move and V02–V03 endorse the *return*. Holding week, instrument and geometry fixed while varying only the ordinal is the cleanest comparison available |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| First breaches reverse more than later breaches and more than N1 | **The prohibition is doing real work.** Necessary support for V01's central instruction; not sufficient for any entry rule |
| First and later breaches behave alike | The prohibition is not distinguishing anything at this sample. A significant negative, since three lessons rest on it |
| Outcome 3 shows the forbidden trade is profitable | Report it plainly and prominently. A result that embarrasses the lesson is exactly the result `E25` exists to protect |
| Reversal happens but the week's extreme is elsewhere | The "trapped for the entire week" framing is not supported even where the reversal is. Report the two outcomes separately — they are separate claims |

## 6. MANDATORY SCOPE STATEMENT

> PT-009 tests one operationalisation of *"the first move of the week"*: the first breach
> of the week's first-eight-hours range. **`A-006` — what "the box" refers to in V01
> `[00:43:07]` — remains OPEN, and this test does not close it.** Nothing here identifies
> a "false move" or a "trap move" (`A-002`), which are undefined as patterns; the trigger
> is a range breach and is reported as a range breach.

## 7. TO RUN THIS

1. Close `I-007`; record the feed's week-open timestamp; confirm W-C is DEVELOPMENT.
2. **Run PT-008 first.** This test consumes its block definition, and running them in the
   other order would mean tuning the block against this test's outcome.
3. Harvest with timestamps from DOM text only.
4. Run all three baselines before looking at the rule arm's aggregate.
5. Write `BT_V01_NNNN.md` from the template, §0 referencing this file.
