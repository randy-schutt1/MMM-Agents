# RECLASSIFICATION NOTICE — 22_AGENT_BENCHMARK

**Date:** 2026-08-16
**Authority:** MASTER_AUDIT_2026-08-16.md and MASTER_A_PLAN_2026-08-16.md (Phase 0), located in `/Users/randyschutt/Desktop/Trading/Audit/`.

## Status

This suite is hereby reclassified:

> **DEVELOPMENT SMOKE TEST ONLY — NOT evidence of agent competence.**

The previously reported result — **98.3% (491.5/500), Status: PASSED** in `BENCHMARK_REPORT.md` — must never be cited as proof that any agent can read charts or apply the Market Maker Method.

## Why the 98.3% result is invalid as competence evidence

1. **Circularity.** The "agent" under test was the `CanonicalExpertEvaluator` rule baseline — the same rule set that generated the expected labels. The label source and the test subject were the same code (`agent_harness.py:478-479`). Generator, labels, and scorer share the same assumed rules; a near-perfect score was structurally guaranteed and measures nothing about an external agent.
2. **Fabricated confidence targets.** The dataset's expected confidence values were produced by `random.randint` (`dataset_generator.py:204-218`), not by any methodology-derived standard.
3. **Case 01 internal inconsistency.** Case 01's state JSON reports a **bullish 5/13 EMA cross** while the baseline calls a **bearish M trade** from a separate condition. The aggregate score hides rule inconsistency inside the benchmark itself.

## Standing rule

- The suite may be retained as a development smoke test of harness plumbing (I/O, scoring mechanics, dataset format).
- No document in this repository may cite the 98.3% score, the "PASSED" status, or any per-metric gate from this suite as evidence of agent competence. Historical documents are annotated, not deleted.
- Genuine agent evaluation is deferred to MASTER_A_PLAN Phases 5–7 (sealed evaluation pack, human reproducibility trial first, then blind agent gates).
