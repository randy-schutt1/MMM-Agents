# 14_PINE — PHASE 5+ (OBSERVER → STRATEGIST)

TradingView Pine Script.

## STATUS: EMPTY — DO NOT WRITE CODE YET

No Pine Script exists, and none should be written during the Student Phase
(`DECISIONS.md` D-006).

Naming: `mmm_<component>_v<major>.<minor>.pine`

## PHASE ORDER

**Phase 5 — Observer:** indicators that *identify structures only*. No entries, no
signals, no trades. The goal is to see whether the machine sees what the human
sees.

**Phase 6 — Evaluator:** compare machine recognition against manually labelled
GBP/USD history from `09_CHART_EXAMPLES/` and `06_MANUAL_BACKTEST/`. This is the
first honest test of the machine spec.

**Phase 7 — Strategist:** only then add deterministic entries, stops,
invalidations, targets, and trade management.

## DEVELOPMENT PRINCIPLES

1. Build modular components; test one concept at a time.
2. Keep indicator logic separate from strategy logic.
3. Preserve raw detections for auditability.
4. **Avoid repainting.**
5. **Avoid lookahead bias.**
6. Use confirmed bars unless the course explicitly requires intrabar behaviour.
7. Log assumptions in the source.
8. Compare algorithmic detections against manually labelled examples.
9. Maintain version history.
10. Add visual debugging overlays.
11. Test edge cases.
12. Keep every rule traceable to the research corpus.

## THE STANDARD

> **Compilation is not validation.**

Code that compiles and produces a beautiful chart has demonstrated nothing. The
only evidence that matters is agreement with manually labelled examples — and
disagreements are findings about the spec, not bugs to tune away.

Every rule in the code carries its classification from `13_MACHINE_SPEC/`:
`DIRECT TRANSLATION` / `EMPIRICAL APPROXIMATION` / `HEURISTIC` / `UNRESOLVED`.
