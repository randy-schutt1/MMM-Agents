# PT-019 — The weekend gap, and the one mechanical rationale in V01

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V01 [00:48:58]–[00:49:44], [00:49:12], [00:50:17]; V02 [00:05:24]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

*"Don't carry trades through on Friday"* is the **only** instruction in V01 whose rationale
is **mechanical rather than pattern-based** — `V01_INTERPRETATION.md` §7 `M5` singles it out
for exactly that, and then refuses to code it because he gives no time, no session and no
exception handling. V02 restates the instruction flatly: *"You always get out on Friday, my
friend, always"* `[00:05:24]`.

The rationale is a claim about **execution**, not about the dealer: a position held over the
weekend is filled at the first available price on the Sunday open, so the weekend gap is a
risk that no stop can bound.

That is measurable directly and it is the last piece of V01 that has never been checked.
It is also the one test in this batch whose result is **actionable regardless of whether
the Market Maker Method works at all** — the gap distribution of GBP/USD is a fact about
the instrument, and it will still be true if every other test in this batch returns null.

---

## 2. THE QUESTION

> How large is the GBP/USD weekend gap, how often does it exceed the stop distances this
> course teaches, and does it exceed the largest intra-week overnight gap?

Null hypothesis: **the weekend gap is not distinguishable** from the gaps that occur at
other daily boundaries within the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-C** — 2013-01-06 → 2017-12-29, ~260 weekends |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Gap definition | `open(first bar of the new trading week) − close(last bar of the previous week)`, in pips, signed and absolute. **Boundaries by timestamp lookup, never by bar count** |
| Measure 1 | Distribution of absolute gap size; median, 90th, 99th percentile, maximum |
| Measure 2 | **Share of weekends whose gap exceeds 10, 15, 18 and 50 pips** — the instructor's own stop and target numbers (V04 `[00:04:43]`, `[00:05:07]`), so the risk is expressed in the units the course uses |
| Measure 3 | Gap fill: share of gaps closed within 4 h, 24 h and by the week's end, with time-to-fill |
| Measure 4 | Comparison against **intra-week daily-boundary gaps** at the same clock instant on Mon–Thu |
| Measure 5 | Directional test: is the gap's sign related to the **prior Friday's** direction? A "the dealer squares his books" reading predicts a relationship; no relationship is the null |
| Excluded weekends | **None.** Holiday weekends are retained and reported separately |
| Decision point | Friday close. Everything after is outcome |
| Sample | ~260 weekends. ≥ 30 satisfied |

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | Measure 4's intra-week boundary gaps. Same instrument, same clock, same measurement; only the calendar position changes |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`: "gaps" computed at shifted week boundaries, most of which fall inside continuous trading and should therefore be near zero. A sanity control that catches a harvest defect before it becomes a finding |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| A material share of weekend gaps exceed 18 pips | **The instructor's rationale holds on its own terms**: an 18-pip stop cannot bound weekend risk, and the Friday-flat instruction is justified mechanically rather than doctrinally. The clearest supportable instruction in V01 |
| Gaps are almost always small | The rationale is weak on this instrument in this era. Report prominently. The instruction may still be right for other reasons; this test speaks only to the stated one |
| Gaps fill quickly and consistently | Interesting and **must not be turned into a strategy here.** A gap-fill edge is not in this course; recording one as if it were would be `E02` and `D-030` at once |
| Measure 5 shows a directional relationship | A genuinely new observation. Record as such — an observation, not a rule, and not attributed to the instructor, who says nothing about gap direction |

## 6. MANDATORY SCOPE STATEMENT

> PT-019 measures the GBP/USD weekend gap. It tests the **stated rationale** for the
> Friday-flat instruction, not the instruction itself — the instruction names no time, no
> session and no exception, so there is no rule with parameters to apply
> (`V01_INTERPRETATION.md` §7 `M5`). No gap-fill trading rule may be derived from this test.

## 7. TO RUN THIS

1. Close `I-007`; **record the feed's week-open and week-close timestamps** — this test is
   *entirely* about those two instants; confirm W-C is DEVELOPMENT.
2. Harvest with timestamps from DOM text only.
3. Run the shifted-boundary sanity control **first**; a non-zero result there means the
   harvest is wrong and no other number in the test can be trusted.
4. Report the five largest gaps as the pre-registered sensitivity appendix, retained in the
   headline distribution.
5. Write `BT_V01_NNNN.md` from the template, §0 referencing this file.
