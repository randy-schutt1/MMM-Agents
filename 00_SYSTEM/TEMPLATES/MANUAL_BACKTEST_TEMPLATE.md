# BT_VXX_NNNN — MANUAL BACKTEST OBSERVATION

> Copy to `06_MANUAL_BACKTEST/VXX/BT_VXX_NNNN.md`. One file per observation.
> Delete these instruction blocks.

**The decision-point section is completed BEFORE any future candle is revealed.**
Fill sections 1–5, save, then reveal the outcome and fill sections 6–8. Filling
them together destroys the entire value of the record.

Test IDs are never reused. A superseded observation keeps its ID and is marked
`SUPERSEDED`; the replacement gets a new one.

---

## 0. PRE-REGISTRATION — COMPLETE BEFORE OPENING ANY CHART IN THE RANGE

> **HARD GATE (`DECISIONS.md` D-026 / D-027).** This section is filled in, committed,
> and the corresponding `DECISIONS.md` entries recorded **before** the first chart in
> the test period is examined. A `BT_` file whose §0 was written after the charts were
> seen is `INVALID` — it is not fixable by editing, and `scripts/validate_project.py`
> will fail if the decision records are missing.
> Specification: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

| Field | Value |
|---|---|
| Rule under test (verbatim + source ref) | |
| `DECISIONS.md` pre-registration entry | D-0XX |
| Instrument | |
| Timeframe | |
| Date range (inclusive) | |
| Session boundaries + timezone | |
| Eligible entry window | |
| Expected number of decision points | |
| Development or holdout block? | **DEVELOPMENT** — holdout must not be opened (D-027) |
| Pre-registered by / date | |
| Charts opened after this section was committed? | YES / NO — must be YES |

### Baseline — defined here, before any result exists

| Field | Value |
|---|---|
| Baseline type | Matched random entry (**required**) |
| Held constant | instrument, session, eligible window, stop distance, target distance, n |
| Randomized | entry bar; direction: RANDOM / FIXED-TO-RULE (state which) |
| Iterations | ≥ 200 |
| Second arm — inside-box vs outside-box contrast | RUN / NOT APPLICABLE (justify) |
| Third arm — buy-and-hold / drift | RUN / SKIPPED |
| Baseline script | `scripts/…` |

**Choosing or adjusting a baseline after seeing the rule's result is `E21`, CRITICAL.**

---

## 1. IDENTIFICATION

| Field | Value |
|---|---|
| Test ID | `BT_VXX_NNNN` |
| Date recorded | |
| Instrument | GBP/USD |
| Timeframe | |
| Chart date/time at decision point | (include timezone) |
| Data source | (feed / platform) |
| Lesson | VXX |
| **Exact rule being tested** | Quote it, with source reference `S4` / `[HH:MM:SS]` |

The rule must be stated before the observation begins. "Testing the lesson
generally" is not a test.

---

## 2. MARKET CONTEXT AT DECISION POINT

Only what is knowable at the decision candle.

| Field | Value |
|---|---|
| Higher-timeframe context | |
| Day of week / session | |
| Recent structure | |
| Anything the lesson says to check first | |

---

## 3. EVIDENCE VISIBLE AT DECISION TIME

The core anti-hindsight section. Everything here must be visible on the chart at
the decision candle, with the future hidden.

| # | Observation | Supports / contradicts the setup |
|---|---|---|
| 1 | | |

**Screenshot before:** `BT_VXX_NNNN_before.png` (future candles hidden)

Confirm: `[ ] The screenshot shows only data available at the decision point.`

---

## 4. CLASSIFICATION — RECORDED BEFORE REVEALING THE OUTCOME

| Field | Value |
|---|---|
| Setup present? | VALID / INVALID / BORDERLINE / INSUFFICIENT INFORMATION |
| Reasoning | |
| Which criteria are met | |
| Which criteria are **not** met | |

`INSUFFICIENT INFORMATION` is a legitimate answer and is valued. False certainty is
more dangerous than calibrated uncertainty.

If `INVALID`, state precisely **why** — which rule fails. "Doesn't look right" is
not a rejection reason the reviewer can verify.

---

## 5. PLAN — RECORDED BEFORE REVEALING THE OUTCOME

Only if classified VALID or BORDERLINE.

| Field | Value |
|---|---|
| Entry criteria | |
| Entry level | |
| Invalidation criteria | |
| Stop level | |
| Target(s) | |
| Risk (R) definition | |
| Expected outcome | |

---

## 6. OUTCOME — AFTER REVEALING SUBSEQUENT CANDLES

| Field | Value |
|---|---|
| What actually happened | |
| Entry triggered? | |
| Result | WIN / LOSS / BREAKEVEN / NO ENTRY / N/A |
| Result in R | |
| MAE | |
| MFE | |
| Time in trade | |

**Screenshot after:** `BT_VXX_NNNN_after.png`

---

## 7. GRADING — TWO SEPARATE JUDGEMENTS

These are independent. Conflating them is reviewer error code E14.

| Judgement | Value |
|---|---|
| **Was the rule applied correctly?** | YES / NO / PARTIALLY |
| **Was this a valid setup?** | YES / NO / BORDERLINE |
| **Trade outcome** | WIN / LOSS / BREAKEVEN / NO ENTRY |

Combined classification:

```text
Correct Setup   / Winner
Correct Setup   / Loser        ← a correct application; keep it
Incorrect Setup / Winner       ← still an error; do not let it inflate confidence
Incorrect Setup / Loser
Borderline      / Unresolved
```

**This observation:** 

### Mistake classification (if any)

| Code | Description |
|---|---|
| | e.g. E05 wrong pattern boundary, E06 false positive, E07 false negative |

---

## 8. NOTES

What was learned. What was ambiguous in the moment. What the lesson does not
address about this situation.

---

## 9. INTEGRITY CHECKLIST

- [ ] The rule being tested was stated before the observation
- [ ] Sections 1–5 were completed before any future candle was revealed
- [ ] The "before" screenshot genuinely hides the future
- [ ] The classification was not revised after seeing the outcome
- [ ] This observation is retained regardless of result
- [ ] Rule application was graded separately from trade outcome
- [ ] No setup boundary was drawn using a future high or low
- [ ] §0 pre-registration was committed **before** any chart in the range was opened
- [ ] The baseline was defined in §0 and has not been altered since
- [ ] This observation lies in the DEVELOPMENT block, not the reserved holdout
- [ ] This test is recorded in the run log whether or not it found anything

If any box is unchecked, this observation is **invalid** and must be redone with a
new test ID. Do not fix it by editing the text. See `REMEDIATION_PROTOCOL.md` §2.

---

## 9b. RESULT CLASSIFICATION

| Field | Value |
|---|---|
| n (decision points in this test) | |
| Classification | `DESCRIPTIVE` (no baseline or n<30) / `EVIDENTIAL` / `INVALID` |
| Hit rate | with 95% interval — **never a bare percentage** |
| Baseline distribution | median, 5–95% range, iterations |
| Rule vs baseline | percentile of the baseline distribution |
| Verdict | e.g. *"cannot be distinguished from chance at this sample"* |

If n < 30, write this verbatim and do not quote a rate without it:

```text
SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only.
```

**A null result stated plainly is worth more than a favourable one that cannot be
read.** Report it with the same prominence.

---

## 10. STATUS

```text
STATUS: VALID OBSERVATION
```

If superseded later:

```text
STATUS: SUPERSEDED — INVALID PROCEDURE (see 18_REVIEW/VXX/VXX_REVIEW_R<n>.md)
REPLACED BY: BT_VXX_NNNN
```

Superseded observations are never deleted.
