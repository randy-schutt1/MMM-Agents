# Scoring Rubric

## Per-case score — 10 points

| Component | Points | Standard |
|---|---:|---|
| Classification/decision | 2 | Correct state: valid, invalid, pass, unresolved, calculation result, or source rank |
| Evidence-based reasoning | 2 | Uses only visible facts and cites the controlling condition |
| Sequence | 1 | Orders prerequisites, trigger, invalidation, and post-decision steps correctly |
| Chart markup | 1 | Required objects are placed/labeled without future data; N/A cases earn by correctly stating N/A |
| Calculation | 1 | Correct units and arithmetic; N/A cases earn by refusing invented arithmetic |
| Provenance | 1 | Correct source tier and `EXPLICIT`/`VISUAL`/`IMPLIED`/`INFERRED`/`UNRESOLVED` label |
| Uncertainty calibration | 1 | Confidence matches evidence; open ambiguity is not forced closed |
| Lookahead control | 1 | Uses only decision-time information and preserves first answer |

## Penalties and critical failures

The following are critical even when direction or outcome is correct:

| Code | Critical failure | Effect |
|---|---|---|
| CF-1 | Uses future candles or outcome to classify the decision point | Case = 0; Lookahead dimension fails; contaminated block must be retaken on new charts |
| CF-2 | Fabricates a course rule or arbitrary numeric threshold | Case = 0; Provenance and Ambiguity dimensions fail |
| CF-3 | Ignores an explicit invalidation/prohibition | Case = 0; Sequence dimension fails |
| CF-4 | Treats Tier 2 notes, owner attestation, interpretation, or test result as stronger than the recording | Case = 0; Provenance dimension fails |
| CF-5 | Gives false certainty where answer key is `UNRESOLVED`/`INSUFFICIENT` | Case = 0; Ambiguity dimension fails |
| CF-6 | Alters the first answer after outcome/reveal without preserving it | Entire attempt invalid; retest required |
| CF-7 | Risks more than the explicit cumulative account limit in a V09 calculation, or applies 2% separately to simultaneous trades | Case = 0; Risk gate fails |
| CF-8 | Opens or uses reserved holdout data | Entire attempt invalid; evidence-protocol remediation required |

Non-critical arithmetic slips lose the calculation point and any classification point dependent on them. A profitable outcome never restores points lost for an invalid decision.

## Overall thresholds

- **Pass:** at least 748/880 (85.0%), every mastery dimension at least 80%, no critical failure, and all hard gates passed.
- **Conditional retest:** 660–747 (75.0–84.9%) with no critical failure and no hard-gate failure. Retest failed dimensions plus linked concepts.
- **Not mastered:** below 660, any critical failure, or any hard-gate failure.

## Hard gates

A high aggregate cannot compensate for:

| Gate | Minimum |
|---|---:|
| Risk/position sizing | 90% on V09 and risk-integration cases; no CF-7 |
| Sequence | 85%; no CF-3 |
| Lookahead control | 100%; no CF-1/CF-6 |
| Provenance | 90%; no CF-2/CF-4 |
| Ambiguity calibration | 85%; no CF-5 |

## Dimension scoring

For each mastery dimension, sum the points from cases where that dimension is primary, divided by available points. Secondary mappings support diagnosis but do not dilute the primary score. The coverage matrix is the controlling map.

## Retest requirements

- Retests use different chart periods and reworded calculations.
- The original attempt remains immutable and attached to the retest.
- Any lookahead failure requires the entire affected chart block to be replaced.
- A provenance/ambiguity failure requires mixed Tier 1/Tier 2/interpretation source cards.
- A risk failure requires a fresh multi-position allocation plus win/loss sequence.
- Two failed retests on the same hard gate require instructor-led remediation before a third attempt.

## Video-linked remediation

| Error pattern | Remediation |
|---|---|
| Weekly context/first move/Friday hold | Re-study V01 §§2b–2f and V02 weekly/session sections; redo H4 weekly markup |
| 22/DNC/second-leg sequence | Re-study V02 §§2a, 2e, 2g–2h; explicitly list what is still undefined |
| H4 first-eight-hours/flashcards | Re-study V03 §§2a, 2h–2j and visual examples |
| Blended V04 instructor/guest rules | Re-study V04 speaker boundary and C-005; build two separate checklists |
| Makes up unclear patterns | Re-study V05 pass discipline and hard-right-edge R&D |
| Push/level false certainty | Re-study V06/V07 and D-030; practise `INSUFFICIENT INFORMATION` responses |
| Confirmation/high-low confusion | Re-study V08 §6 and C-009; separate basic live entry from demo drill |
| Position sizing/cumulative exposure | Re-study V09 §§2–5 and redo formula sequence by hand |
| Safety trade without prerequisites or stop | Re-study V10 §§6–8 and §15; list missing definitions and no-stop limitation |
| Outcome = correctness | Re-study `STUDY_PROTOCOL.md` manual-backtest section and grade four outcome/application quadrants |
