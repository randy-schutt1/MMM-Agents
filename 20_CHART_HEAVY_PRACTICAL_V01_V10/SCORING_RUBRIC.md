# Scoring Rubric — Chart-Heavy Practical

## Per-case score — 12 points

| Component | Points | Standard |
|---|---:|---|
| Classification or required decision | 2 | Correct valid/invalid/pass/wait/unresolved/calculation state |
| Evidence-based reasoning and sequence | 2 | Uses controlling prerequisites in order and no outcome reasoning |
| Chart markup | 3 | Required lines, boxes, candles, timestamps, and labels are accurate and prospective |
| Measurement or calculation | 2 | Correct OHLC values, pip conversion, risk arithmetic, and units; earns full credit for correctly refusing unavailable arithmetic |
| Provenance and uncertainty | 2 | Separates `EXPLICIT`, `VISUAL`, `IMPLIED`, `INFERRED`, and `UNRESOLVED` and calibrates confidence |
| Lookahead control | 1 | Uses only permitted information and preserves the first answer |

Total: 60 × 12 = **720 points**.

## Passing and hard gates

- Overall pass: at least **612/720 (85%)**.
- Every block: at least **80%**.
- Chart-markup component: at least **85%** overall.
- Decision/reasoning component: at least **85%** overall.
- Risk block F: at least **90%**.
- Provenance/uncertainty component: at least **90%**.
- Lookahead component: **100%**.
- No critical failure.

An aggregate score cannot compensate for a failed hard gate.

## Critical failures

| Code | Failure | Effect |
|---|---|---|
| PCF-1 | Uses future candles/outcome to make or revise Phase A | Case zero; lookahead gate fails; affected block retest |
| PCF-2 | Opens `instructor_only/`, answer key, adjacent unassigned data, or absent holdout | Attempt invalid |
| PCF-3 | Fabricates a chart rule, threshold, TDI definition, stop, or pattern anatomy | Case zero; provenance/ambiguity gates fail |
| PCF-4 | Ignores an explicit prohibition or invalidation | Case zero; decision/sequence gate fails |
| PCF-5 | Treats a completed screenshot or profitable outcome as proof of a valid rule | Case zero; provenance gate fails |
| PCF-6 | Risks more than cumulative 2% or applies 2% independently to simultaneous positions | Case zero; risk gate fails |
| PCF-7 | Gives false certainty where the key is `UNRESOLVED`/`INSUFFICIENT` | Case zero; ambiguity/provenance gates fail |
| PCF-8 | Alters or replaces the first locked response/marked chart | Attempt invalid |

## Remediation

- Block A: V01 trap contexts and V03 first-eight-hours markup.
- Block B/C: V10 retrospective PFH/PFL boundary and prospective uncertainty.
- Block D: V05 pass discipline plus the relevant unresolved term in V02/V04/V06/V07/V08/V10.
- Block E: V08 basic confirmation versus demo-only extreme entry and C-009.
- Block F: V09 cumulative risk/recalculation and V10 missing-stop boundary.
- Block G: sourcing hierarchy, screenshot evidence limits, and hard-right-edge contamination.

