# PT-008 — "The dealer must cut" the first-eight-hours range of the week

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V03 [00:12:46]–[00:13:29] and its slide; V04 [00:16:06]–[00:16:15]
BLOCKERS:   I-007 (the feed decides where the week opens — see §3a) · D-028 unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

This is **the most mechanically specific instruction in V01–V04**. It names a timeframe, a
count and two drawable prices, and it is given twice, by the instructor, in two lessons:

> *"What I want you to do on the four hour chart is block the first eight hours off. Mark
> the high of the first eight hours and mark the low of the first eight hours, two bars."*
> V03 `[00:12:46]`–`[00:12:54]`
> *"Block off the first eight hours that draw a line all the way across your chart. Those
> are your psychological support and resistance levels."* V04 `[00:16:11]`–`[00:16:15]`

And the slide states the prediction outright: *"Dealer **must cut** the perceived support
and resistance zone to make money and get traders in the game"* (`V03_SOURCE_NOTES.md`
§4a) — a stronger verb than the spoken *"has to exploit"*.

**"Must cut" is a falsifiable claim about a measurable object.** No pattern, no indicator,
no undefined noun. It is also the object every weekly rule downstream measures from, which
makes it the weekly-scale equivalent of what PT-001 is doing at daily scale.

---

## 2. THE QUESTION

> Is the first-eight-hours range of the GBP/USD week breached — and is that breach more
> than what an arbitrarily placed eight-hour block would deliver?

Null hypothesis: **it is not special.** An eight-hour block at the week's open is breached
at the same rate, at the same speed and by the same distance as an eight-hour block placed
anywhere else in the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | **4-hour** for the block (the instructor's own: *"two bars"*); 15-minute for breach timing |
| Window | **W-C** — 2013-01-06 → 2017-12-29, ~260 weeks |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| The block | High and low of the **first two 4-hour bars of the trading week**, boundaries **looked up from bar timestamps, never counted in bars** (the V04 `M1` defect) |
| Measure 1 — **is it cut?** | Share of weeks in which price trades beyond the block high, beyond the block low, beyond **both**, beyond **neither** |
| Measure 2 — **when?** | Time from block close to first breach, in hours |
| Measure 3 — **how far?** | Maximum excursion beyond each edge, in pips |
| Measure 4 — **which first?** | Which edge is breached first, and whether the week's extreme ends up on that side |
| Variation reported, not modelled | *"he adds an extra four hours on this example. Four, eight, twelve hours"* V03 `[00:29:51]`. The 12-hour block is reported as a **pre-registered second arm**; the 8-hour block is the headline, because that is what the slide prints |
| Decision point | Block close. Measures 2–4 are outcomes; **nothing after the block close informs the block itself** |
| Sample | ~260 weeks. ≥ 30 satisfied |

### 3a. `I-007` bites harder here than anywhere else in this batch

The block **is** the first two bars of the week, so its value depends entirely on when the
feed opens the week. Feeds differ by hours, and some do not print Sunday bars at all —
`V03_INTERPRETATION.md` §9.2 flags exactly this ("the instructor's feed shows Sunday
candles; many modern feeds do not").

**The declared feed's week-open timestamp is recorded in the observation as a first-class
parameter**, and a feed change is a new test ID, not an adjustment.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`. The price path is untouched; only the week boundary moves. This isolates "the week's *opening* block" from "any eight-hour block" |
| **Second — the natural control** | Eight-hour blocks at **every** 4-hour offset through the week, measured identically. The week-open block is ranked among them rather than tested alone |
| **Third** | Block-width control: the same measures for blocks of 4, 8, 12 and 24 hours, so a "wider blocks get breached less" artifact cannot masquerade as a finding about the week's open |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| The week-open block is breached at a rate indistinguishable from shifted blocks | **The week's opening range carries no special status at this sample.** A foundational null for the weekly half of the method — report prominently |
| Breach rate is ordinary but breach *timing* is not (e.g. concentrated early) | A narrower, real finding, and the more likely one. Report the timing distribution |
| The block is breached on both sides in most weeks | The "must cut" language is satisfied trivially, and the measure that matters becomes *which side first* (measure 4) rather than *whether* |
| First-breach side predicts the week's extreme side | **This is the result PT-009 is built to follow up.** It is reported here as an association, not as a rule, and PT-009 tests it as a prediction |

## 6. MANDATORY SCOPE STATEMENT

> PT-008 tests whether the first-eight-hours range of the week is breached, when and how
> far. It is **not** a test of the anchor point (`A-001`), the level (`A-004`), the M/W
> (`A-011`) or any entry. It measures a drawn range and reports what price did to it.

## 7. TO RUN THIS

1. Close `I-007`; **record the feed's week-open timestamp explicitly**; confirm W-C sits
   inside DEVELOPMENT.
2. Harvest 4h and 15m bars with timestamps from DOM text only; derive week boundaries by
   timestamp lookup.
3. Run N3 and the offset sweep **before** looking at the week-open block's numbers.
4. Report the five largest-range weeks in W-C as the pre-registered sensitivity appendix
   (`COMMON_PROTOCOL.md` §3), as an appendix and not as a filtered re-run.
5. Write `BT_V03_NNNN.md` from the template, §0 referencing this file.
