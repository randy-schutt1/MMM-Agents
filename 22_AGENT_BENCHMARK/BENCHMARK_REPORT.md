# MARKET MAKER METHOD (MMM) AGENT BENCHMARK REPORT

> **CORRECTION (2026-08-16): RECLASSIFIED — DEVELOPMENT SMOKE TEST ONLY — NOT evidence of agent competence.**
> The 98.3% / PASSED result below is **circular**: the "agent" under test was the `CanonicalExpertEvaluator` rule baseline that also generated the expected labels (`agent_harness.py:478-479`). Confidence targets were `random.randint` (`dataset_generator.py:204-218`), and Case 01 is internally inconsistent (state JSON shows a bullish 5/13 cross; baseline calls a bearish M trade). See `RECLASSIFICATION_NOTICE.md`. This report is preserved as a historical record only.

**Date:** 2026-08-16 00:37:05
**Test Suite:** 50-Case Blind Evaluation Dataset (`22_AGENT_BENCHMARK/dataset/`)
**Status:** PASSED

## 1. Executive Summary
| Metric | Target Gate | Result | Status |
|---|---|---|---|
| **Overall Score** | $\ge 85.0\%$ | **98.3%** (491.5/500.0 pts) | PASS |
| **No-Trade Specificity (Anti-Chop)** | $\ge 90.0\%$ | **100.0%** | PASS |
| **Trade Sensitivity (Positive Setups)** | $\ge 80.0\%$ | **100.0%** | PASS |
| **Directional Bias Accuracy** | $\ge 85.0\%$ | **100.0%** | PASS |
| **Setup Classification Accuracy** | $\ge 85.0\%$ | **100.0%** | PASS |

## 2. Granular Case Results
| Case ID | Category | Expected Setup | Agent Setup | Expected Disp | Agent Disp | Score |
|---|---|---|---|---|---|---|
| CASE_01 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_02 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_03 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_04 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |
| CASE_05 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |
| CASE_06 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_07 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_08 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_09 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.5** / 10 |
| CASE_10 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_11 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_12 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_13 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_14 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_15 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_16 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_17 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.5** / 10 |
| CASE_18 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_19 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_20 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_21 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_22 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_23 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_24 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_25 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_26 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_27 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_28 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_29 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |
| CASE_30 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.5** / 10 |
| CASE_31 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_32 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_33 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.5** / 10 |
| CASE_34 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_35 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_36 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |
| CASE_37 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_38 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_39 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_40 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_41 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |
| CASE_42 | POSITIVE | M_FORMATION | M_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_43 | POSITIVE | W_FORMATION | W_FORMATION | TRADE | TRADE | **10.0** / 10 |
| CASE_44 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_45 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_46 | NEGATIVE | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_47 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_48 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.5** / 10 |
| CASE_49 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **10.0** / 10 |
| CASE_50 | AMBIGUOUS | NO_SETUP | NO_SETUP | NO_TRADE | NO_TRADE | **9.0** / 10 |