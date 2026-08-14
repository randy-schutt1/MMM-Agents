# Scoring Rubric

## Per-case score — 15 points

| Component | Points | Standard |
|---|---:|---|
| HOD | 2 | Exact wick price and first matching timestamp inside the printed trading-day window |
| LOD | 2 | Exact wick price and first matching timestamp inside the printed trading-day window |
| Signature/direction classification | 2 | Correct valid, BUY, SELL, NO TRADE, invalid, DNC, wait, unresolved, or none-confirmable state |
| Signature/direction reasoning and sequence | 2 | Applies peak, pull-away, consolidation, direction, stop hunt, and second-leg conditions in order; direction cases include a marked arrow or rejection |
| HOW/PFH retrospective | 2 | Exact completed-week wick high and first matching timestamp |
| LOW/PFL retrospective | 2 | Exact completed-week wick low and first matching timestamp |
| Provenance and uncertainty | 2 | Correct evidence labels; does not invent missing geometry or stop |
| Lookahead and lock integrity | 1 | Phase A is immutable before Phase B reveal |

Total: 46 × 15 = **690 points**.

## Passing standard

- Overall: at least **587/690 (85.1%)**.
- Easy, intermediate, and difficult tiers: each at least **80%**.
- Combined HOD/LOD/ HOW/LOW points: at least **90%**.
- Signature classification/reasoning: at least **85%**.
- The 10 mixed direction cases: at least **85%**, with no unsupported BUY/SELL decision.
- Provenance/uncertainty: at least **90%**.
- Lookahead/lock integrity: **100%**.
- No critical failure.

## Critical failures

| Code | Failure | Effect |
|---|---|---|
| ECF-1 | Opens or uses the completed-week chart before Phase A is locked | Case zero; lookahead gate fails; tier retest |
| ECF-2 | Revises Phase A after the completed-week reveal | Attempt integrity fails |
| ECF-3 | Uses future movement to validate or invalidate a signature trade | Case zero; lookahead/provenance gates fail |
| ECF-4 | Fabricates level, box, stop-hunt, M/W, second-leg, TDI, peak-lock, or stop rules | Case zero; signature/provenance gates fail |
| ECF-5 | Calls a V02/V04 named trade the official V10 signature trade without evidence | Case zero; taxonomy remediation required |
| ECF-6 | Ignores DNC, a missing visible stop hunt, or a missing second leg | Case zero; signature gate fails |
| ECF-7 | Uses candle bodies/closes when the task requires wick extrema | Lose the affected extrema points; repeated use triggers extrema retest |
| ECF-8 | Uses calendar midnight instead of the printed 17:00–16:45 window | Lose both day-extrema components; repeated use triggers day-boundary retest |
| ECF-9 | Opens the answer key, unassigned files, prior attempts, or absent holdout | Attempt invalid |

## Retesting

Retests use unused weeks, new target days, and re-ordered safety facts. A lookahead failure replaces the entire affected tier. A signature failure requires both fully stipulated and raw-chart cases. An extrema failure requires fresh weeks with close competing wick values.
