# 06_MANUAL_BACKTEST

Manual historical chart study — the Student Phase's proof of application.

## STATUS: EMPTY — NO OBSERVATION RECORDED

## STRUCTURE

```text
06_MANUAL_BACKTEST/
├── VXX/                      ← BT_VXX_NNNN.md + before/after screenshots
├── cumulative/               ← summaries across lessons
└── datasets/                 ← chart data provenance (raw data is gitignored)
```

## WHAT THIS IS — AND IS NOT

This is **not** strategy performance measurement. That is Phase 8
(`15_AUTOMATED_BACKTEST/`). This is an educational and validation exercise: can the
agent correctly **apply** what was taught to historical data?

Primary instrument: **GBP/USD** (`DECISIONS.md` D-007).

## PROCEDURE

1. State exactly which lesson rule is being tested — before starting.
2. Select a period without choosing only obvious winners.
3. Move through the chart sequentially.
4. **Do not use future candles for the initial classification.**
5. Screenshot the decision point (future hidden).
6. Record the classification and plan.
7. Reveal subsequent candles.
8. Record the outcome.
9. Grade rule application **separately** from trade result.

## THE DISTINCTION THAT MATTERS

```text
Correct Setup   / Winner
Correct Setup   / Loser        ← a correct application; keep it, it is not a failure
Incorrect Setup / Winner       ← still an error; do not let it inflate confidence
Incorrect Setup / Loser
Borderline      / Unresolved
```

Conflating outcome with correctness is reviewer error code E14.

## NON-NEGOTIABLE

- Losers are retained. Borderline cases are retained. Mistakes are retained.
- `INSUFFICIENT INFORMATION` is a legitimate classification and is valued.
- A classification is never revised after the outcome is seen.
- No setup boundary is drawn using a future high or low.
- **Contaminated observations are redone with new IDs, not edited.** The originals
  stay, marked `SUPERSEDED` (`REMEDIATION_PROTOCOL.md` §2).
- Test IDs are never reused.

## BEFORE THE FIRST OBSERVATION — HARD GATE

**No `BT_*.md` may be written until `DECISIONS.md` carries the baseline (D-026) and the
period pre-registration (D-027) for the rule under test.** `scripts/validate_project.py`
enforces this mechanically. Specification: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

- **Baseline** — matched random entry, >=200 iterations, distribution reported. A hit
  rate with no comparator is unreadable, not merely weak.
- **Pre-registration** — period fixed before any chart in it is opened.
- **Holdout** — the reserved block stays closed during the Student Phase.
- **n >= 30** before any rate is quoted; below that, `SAMPLE INSUFFICIENT FOR INFERENCE`.
- **Null results are reported with equal prominence.**

Where the course supplies its own control, use it: V04 claims **location** changes the
outcome — same M formation, loser inside the blue box, winner outside. That contrast
removes the pattern confound and is stronger evidence than any bare hit rate.

## ALSO BEFORE THE FIRST OBSERVATION

The data source, broker/feed, timezone, and timeframes must be decided and recorded
in `DECISIONS.md` — every record's reproducibility depends on it. See
`SETUP_ISSUES.md` I-007.

Template: `00_SYSTEM/TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`
