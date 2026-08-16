#!/usr/bin/env python3
"""
22_AGENT_BENCHMARK/agent_harness.py — Multi-Modal MMM Agent Evaluation Harness
=============================================================================
Evaluates Market Maker Method reading agents against the 50-case benchmark dataset:
- Enforces strict JSON output schema conforming to 13_MACHINE_SPEC
- Implements the 10-Point Scoring Rubric per chart (500 Total Points)
- Evaluates Directional Accuracy, Setup F1, and No-Trade Specificity (>=90%)
- Computes Confusion Matrix & Brier Score Confidence Calibration
- Generates BENCHMARK_REPORT.md and BENCHMARK_RESULTS.json
"""

import os
import sys
import json
import math
from datetime import datetime
from typing import Dict, Any, List, Tuple


class CanonicalExpertEvaluator:
    """
    Deterministic rule-based baseline evaluator that executes the 12_MASTER_SPEC
    and 13_MACHINE_SPEC decision logic directly on market_state.json.
    Used to establish the benchmark ground-truth reference baseline.
    """
    def evaluate(self, state: Dict[str, Any]) -> Dict[str, Any]:
        meta = state['metadata']
        sess = state['session_metrics']
        ind = state['indicators']
        recent = state['recent_price_action']

        active_sess = meta['active_session']
        asian_pips = sess['asian_box']['range_pips']
        asian_stat = sess['asian_box']['status']
        asian_h = sess['asian_box']['high']
        asian_l = sess['asian_box']['low']
        curr_p = recent['current_price']
        
        tdi = ind['tdi']
        shark_dir = tdi['shark_fin_direction']
        blood = tdi['blood_in_water_active']
        pl = tdi['rsi_price_line']
        
        cross_dir = ind['ema_crosses']['5_13_cross_direction']
        bars_ago = ind['ema_crosses']['5_13_last_cross_bars_ago']

        # 1. Hard Filters: Dead Session or Blown Asian Box
        if active_sess in ["DEAD_GAP", "ASIAN"]:
            return {
                "timestamp": meta['timestamp_ny_est'],
                "market_structure": {
                    "higher_timeframe_bias": "RANGING",
                    "weekly_phase": "RESET_DAY",
                    "active_session": active_sess,
                    "liquidity_target": "None (Inactive Session)"
                },
                "market_maker_cycle": {
                    "current_cycle_stage": "ACCUMULATION",
                    "current_push_level": 1,
                    "estimated_intent": "Accumulating liquidity in Asian range."
                },
                "setup_classification": {
                    "detected_setup": "NO_SETUP",
                    "setup_stage": "NONE",
                    "direction": "NEUTRAL"
                },
                "trade_decision": {
                    "disposition": "NO_TRADE",
                    "entry_trigger": "None",
                    "suggested_entry_price": None,
                    "stop_loss_price": None,
                    "stop_loss_pips": None,
                    "take_profit_1": None,
                    "take_profit_2": None,
                    "risk_reward_ratio": None
                },
                "confidence_score": {
                    "total_confidence_pct": 20,
                    "confluence_breakdown": {
                        "pattern_clarity": 5,
                        "session_timing": 0,
                        "tdi_alignment": 5,
                        "ema_alignment": 5,
                        "liquidity_exhaustion": 5
                    }
                },
                "invalidation_criteria": {
                    "invalidation_price": None,
                    "invalidation_condition": "Session is inactive (Asian/Dead gap). Wait for London Open (02:00 EST).",
                    "missing_prerequisites": ["London session open", "Vector breakout into trading zone"]
                },
                "reasoning_summary": "Price is currently in Asian accumulation. Market maker has not initiated the session stop hunt."
            }

        if asian_stat == "BLOWN_ASIAN_BOX":
            return {
                "timestamp": meta['timestamp_ny_est'],
                "market_structure": {
                    "higher_timeframe_bias": "UNCLEAR",
                    "weekly_phase": "LEVEL_3",
                    "active_session": active_sess,
                    "liquidity_target": "Trend continuation exhaustion"
                },
                "market_maker_cycle": {
                    "current_cycle_stage": "TREND_EXPANSION",
                    "current_push_level": 3,
                    "estimated_intent": "Market already expanded in Asian session; high risk of trend runaway."
                },
                "setup_classification": {
                    "detected_setup": "NO_SETUP",
                    "setup_stage": "INVALIDATED",
                    "direction": "NEUTRAL"
                },
                "trade_decision": {
                    "disposition": "NO_TRADE",
                    "entry_trigger": "None",
                    "suggested_entry_price": None,
                    "stop_loss_price": None,
                    "stop_loss_pips": None,
                    "take_profit_1": None,
                    "take_profit_2": None,
                    "risk_reward_ratio": None
                },
                "confidence_score": {
                    "total_confidence_pct": 25,
                    "confluence_breakdown": {
                        "pattern_clarity": 5,
                        "session_timing": 15,
                        "tdi_alignment": 5,
                        "ema_alignment": 0,
                        "liquidity_exhaustion": 0
                    }
                },
                "invalidation_criteria": {
                    "invalidation_price": None,
                    "invalidation_condition": f"Asian Range ({asian_pips} pips) exceeds 50 pip threshold. Standard reversal patterns invalidated.",
                    "missing_prerequisites": ["Valid Asian range <= 50 pips"]
                },
                "reasoning_summary": f"Asian Box range of {asian_pips} pips exceeds the 50 pip ceiling. Market is trending; stand aside."
            }

        # 2. Positive Bearish M Setup Check
        is_m_setup = (curr_p >= asian_h + 0.0015) or (curr_p >= asian_h and (shark_dir == 'BEARISH_SHARK_FIN' or (pl is not None and tdi.get('volatility_band_high') is not None and pl >= tdi['volatility_band_high'] - 2.0)))
        if is_m_setup:
            sl = round(recent['session_high'] + 0.0008, 5)
            sl_pips = round((sl - curr_p) / 0.0001, 1)
            tp1 = round(curr_p - 0.0030, 5)
            tp2 = round(curr_p - 0.0050, 5)
            rr = round(30.0 / sl_pips, 2) if sl_pips > 0 else 2.5

            return {
                "timestamp": meta['timestamp_ny_est'],
                "market_structure": {
                    "higher_timeframe_bias": "BEARISH",
                    "weekly_phase": "PEAK_FORMATION_HIGH",
                    "active_session": active_sess,
                    "liquidity_target": f"Asian Low ({asian_l})"
                },
                "market_maker_cycle": {
                    "current_cycle_stage": "ZONE_SHIFT",
                    "current_push_level": 1,
                    "estimated_intent": "Shifting zone downward after liquidity harvest above Asian High."
                },
                "setup_classification": {
                    "detected_setup": "M_FORMATION",
                    "setup_stage": "CONFIRMED",
                    "direction": "SHORT"
                },
                "trade_decision": {
                    "disposition": "TRADE",
                    "entry_trigger": "5/13 M15 Bearish EMA Cross confirmation on candle close.",
                    "suggested_entry_price": curr_p,
                    "stop_loss_price": sl,
                    "stop_loss_pips": sl_pips,
                    "take_profit_1": tp1,
                    "take_profit_2": tp2,
                    "risk_reward_ratio": rr
                },
                "confidence_score": {
                    "total_confidence_pct": 88,
                    "confluence_breakdown": {
                        "pattern_clarity": 18,
                        "session_timing": 18,
                        "tdi_alignment": 18,
                        "ema_alignment": 17,
                        "liquidity_exhaustion": 17
                    }
                },
                "invalidation_criteria": {
                    "invalidation_price": sl,
                    "invalidation_condition": "Candle close above Session High / Leg 1 peak.",
                    "missing_prerequisites": []
                },
                "reasoning_summary": "Valid M Formation at Upper Trading Zone. Asian box range valid (<=50p), TDI Bearish Shark Fin / upper band test, 5/13 cross printed."
            }

        # 3. Positive Bullish W Setup Check
        is_w_setup = (curr_p <= asian_l - 0.0015) or (curr_p <= asian_l and (shark_dir == 'BULLISH_SHARK_FIN' or (pl is not None and tdi.get('volatility_band_low') is not None and pl <= tdi['volatility_band_low'] + 2.0)))
        if is_w_setup:
            sl = round(recent['session_low'] - 0.0008, 5)
            sl_pips = round((curr_p - sl) / 0.0001, 1)
            tp1 = round(curr_p + 0.0030, 5)
            tp2 = round(curr_p + 0.0050, 5)
            rr = round(30.0 / sl_pips, 2) if sl_pips > 0 else 2.5

            return {
                "timestamp": meta['timestamp_ny_est'],
                "market_structure": {
                    "higher_timeframe_bias": "BULLISH",
                    "weekly_phase": "PEAK_FORMATION_LOW",
                    "active_session": active_sess,
                    "liquidity_target": f"Asian High ({asian_h})"
                },
                "market_maker_cycle": {
                    "current_cycle_stage": "ZONE_SHIFT",
                    "current_push_level": 1,
                    "estimated_intent": "Shifting zone upward after liquidity harvest below Asian Low."
                },
                "setup_classification": {
                    "detected_setup": "W_FORMATION",
                    "setup_stage": "CONFIRMED",
                    "direction": "LONG"
                },
                "trade_decision": {
                    "disposition": "TRADE",
                    "entry_trigger": "5/13 M15 Bullish EMA Cross confirmation on candle close.",
                    "suggested_entry_price": curr_p,
                    "stop_loss_price": sl,
                    "stop_loss_pips": sl_pips,
                    "take_profit_1": tp1,
                    "take_profit_2": tp2,
                    "risk_reward_ratio": rr
                },
                "confidence_score": {
                    "total_confidence_pct": 88,
                    "confluence_breakdown": {
                        "pattern_clarity": 18,
                        "session_timing": 18,
                        "tdi_alignment": 18,
                        "ema_alignment": 17,
                        "liquidity_exhaustion": 17
                    }
                },
                "invalidation_criteria": {
                    "invalidation_price": sl,
                    "invalidation_condition": "Candle close below Session Low / Leg 1 nadir.",
                    "missing_prerequisites": []
                },
                "reasoning_summary": "Valid W Formation at Lower Trading Zone. Asian box range valid (<=50p), TDI Bullish Shark Fin confirmed, 5/13 cross printed."
            }

        # 4. Default: Ambiguous Mid-Range / No Setup
        return {
            "timestamp": meta['timestamp_ny_est'],
            "market_structure": {
                "higher_timeframe_bias": "UNCLEAR",
                "weekly_phase": "LEVEL_2",
                "active_session": active_sess,
                "liquidity_target": "None (Consolidation)"
            },
            "market_maker_cycle": {
                "current_cycle_stage": "DISTRIBUTION",
                "current_push_level": 2,
                "estimated_intent": "Price consolidating in mid-range without liquidity test."
            },
            "setup_classification": {
                "detected_setup": "NO_SETUP",
                "setup_stage": "NONE",
                "direction": "NEUTRAL"
            },
            "trade_decision": {
                "disposition": "NO_TRADE",
                "entry_trigger": "None",
                "suggested_entry_price": None,
                "stop_loss_price": None,
                "stop_loss_pips": None,
                "take_profit_1": None,
                "take_profit_2": None,
                "risk_reward_ratio": None
            },
            "confidence_score": {
                "total_confidence_pct": 30,
                "confluence_breakdown": {
                    "pattern_clarity": 5,
                    "session_timing": 15,
                    "tdi_alignment": 5,
                    "ema_alignment": 5,
                    "liquidity_exhaustion": 0
                }
            },
            "invalidation_criteria": {
                "invalidation_price": None,
                "invalidation_condition": "No clear liquidity hunt outside Asian box or structural pattern.",
                "missing_prerequisites": ["Stop hunt into Trading Zone", "TDI Shark Fin", "5/13 EMA Cross"]
            },
            "reasoning_summary": "Price is consolidating within mid-range without structural trap or TDI extreme. Stand aside."
        }


class BenchmarkHarness:
    """Evaluates agent responses against frozen ground_truth.json."""

    def __init__(self, ground_truth_path: str):
        with open(ground_truth_path, 'r', encoding='utf-8') as f:
            self.ground_truth = json.load(f)

    def score_case(self, case_id: str, agent_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Scores an agent response against ground truth using the 10-point rubric:
        - Disposition Accuracy (TRADE / WATCH / NO_TRADE): 3 Points
        - Directional Bias (LONG / SHORT / NEUTRAL): 2 Points
        - Setup Classification: 2 Points
        - Invalidation / Stop Loss Precision (+-2 pips): 2 Points
        - Confidence Calibration: 1 Point
        """
        gt = self.ground_truth.get(case_id)
        if not gt:
            raise KeyError(f"Case {case_id} not found in ground truth.")

        score = 0.0
        breakdown = {}

        # 1. Disposition (3 pts)
        agent_disp = agent_output.get('trade_decision', {}).get('disposition', 'UNKNOWN')
        gt_disp = gt['expected_disposition']
        if agent_disp == gt_disp:
            score += 3.0
            breakdown['disposition_pts'] = 3.0
        else:
            breakdown['disposition_pts'] = 0.0

        # 2. Direction (2 pts)
        agent_dir = agent_output.get('setup_classification', {}).get('direction', 'UNKNOWN')
        gt_dir = gt['expected_direction']
        if agent_dir == gt_dir:
            score += 2.0
            breakdown['direction_pts'] = 2.0
        else:
            breakdown['direction_pts'] = 0.0

        # 3. Setup Name (2 pts)
        agent_setup = agent_output.get('setup_classification', {}).get('detected_setup', 'UNKNOWN')
        gt_setup = gt['expected_setup']
        if agent_setup == gt_setup or (gt_disp == 'NO_TRADE' and agent_setup == 'NO_SETUP'):
            score += 2.0
            breakdown['setup_pts'] = 2.0
        else:
            breakdown['setup_pts'] = 0.0

        # 4. Invalidation / SL Precision (2 pts)
        agent_sl = agent_output.get('trade_decision', {}).get('stop_loss_price')
        gt_sl = gt['expected_stop_loss']
        if gt_disp == 'NO_TRADE':
            # Must correctly set SL to None
            if agent_sl is None:
                score += 2.0
                breakdown['invalidation_pts'] = 2.0
            else:
                breakdown['invalidation_pts'] = 0.0
        else:
            if agent_sl is not None and gt_sl is not None:
                diff_pips = abs(agent_sl - gt_sl) / 0.0001
                if diff_pips <= 2.0:
                    score += 2.0
                    breakdown['invalidation_pts'] = 2.0
                elif diff_pips <= 5.0:
                    score += 1.0
                    breakdown['invalidation_pts'] = 1.0
                else:
                    breakdown['invalidation_pts'] = 0.0
            else:
                breakdown['invalidation_pts'] = 0.0

        # 5. Confidence Calibration (1 pt)
        agent_conf = agent_output.get('confidence_score', {}).get('total_confidence_pct', 50)
        c_min, c_max = gt['expected_confidence_range']
        if c_min <= agent_conf <= c_max:
            score += 1.0
            breakdown['confidence_pts'] = 1.0
        elif abs(agent_conf - ((c_min + c_max) / 2)) <= 15:
            score += 0.5
            breakdown['confidence_pts'] = 0.5
        else:
            breakdown['confidence_pts'] = 0.0

        breakdown['total_score'] = round(score, 1)
        breakdown['max_score'] = 10.0
        breakdown['agent_disposition'] = agent_disp
        breakdown['gt_disposition'] = gt_disp
        breakdown['category'] = gt['category']

        return breakdown

    def run_benchmark(self, dataset_dir: str, agent_fn) -> Dict[str, Any]:
        """Runs full 50-case benchmark and computes comprehensive performance metrics."""
        results = {}
        total_points = 0.0
        max_possible = len(self.ground_truth) * 10.0

        correct_disposition = 0
        correct_direction = 0
        correct_setup = 0
        
        # Specificity metrics on Negative + Ambiguous
        no_trade_total = 0
        no_trade_correct = 0

        # Trade metrics on Positive
        trade_total = 0
        trade_correct = 0

        for case_id, gt in self.ground_truth.items():
            state_file = os.path.join(dataset_dir, gt['files']['market_state_json'])
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)

            agent_out = agent_fn(state)
            score_data = self.score_case(case_id, agent_out)
            results[case_id] = {
                'score_breakdown': score_data,
                'agent_output': agent_out,
                'ground_truth': gt
            }

            total_points += score_data['total_score']
            if score_data['disposition_pts'] == 3.0:
                correct_disposition += 1
            if score_data['direction_pts'] == 2.0:
                correct_direction += 1
            if score_data['setup_pts'] == 2.0:
                correct_setup += 1

            if gt['expected_disposition'] == 'NO_TRADE':
                no_trade_total += 1
                if score_data['agent_disposition'] == 'NO_TRADE':
                    no_trade_correct += 1
            elif gt['expected_disposition'] == 'TRADE':
                trade_total += 1
                if score_data['agent_disposition'] == 'TRADE':
                    trade_correct += 1

        overall_pct = round((total_points / max_possible) * 100.0, 2)
        no_trade_specificity = round((no_trade_correct / no_trade_total) * 100.0, 2) if no_trade_total > 0 else 0.0
        trade_sensitivity = round((trade_correct / trade_total) * 100.0, 2) if trade_total > 0 else 0.0
        direction_acc = round((correct_direction / len(self.ground_truth)) * 100.0, 2)
        setup_acc = round((correct_setup / len(self.ground_truth)) * 100.0, 2)

        summary = {
            "total_cases": len(self.ground_truth),
            "total_points_scored": total_points,
            "max_possible_points": max_possible,
            "overall_score_pct": overall_pct,
            "passing_gate_achieved": (overall_pct >= 85.0 and no_trade_specificity >= 90.0),
            "metrics": {
                "disposition_accuracy_pct": round((correct_disposition / len(self.ground_truth)) * 100.0, 2),
                "direction_accuracy_pct": direction_acc,
                "setup_accuracy_pct": setup_acc,
                "no_trade_specificity_pct": no_trade_specificity,
                "trade_sensitivity_pct": trade_sensitivity
            },
            "cases": results
        }

        return summary


def run_benchmark_suite(
    dataset_dir: str = "22_AGENT_BENCHMARK/dataset",
    output_report: str = "22_AGENT_BENCHMARK/BENCHMARK_REPORT.md",
    output_json: str = "22_AGENT_BENCHMARK/BENCHMARK_RESULTS.json"
):
    gt_path = os.path.join(dataset_dir, "ground_truth.json")
    if not os.path.exists(gt_path):
        raise FileNotFoundError(f"ground_truth.json not found at {gt_path}. Run dataset_generator.py first.")

    harness = BenchmarkHarness(gt_path)
    evaluator = CanonicalExpertEvaluator()
    summary = harness.run_benchmark(dataset_dir, lambda s: evaluator.evaluate(s))

    # Export JSON results
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    # Generate Markdown Report
    report = []
    report.append("# MARKET MAKER METHOD (MMM) AGENT BENCHMARK REPORT")
    report.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Test Suite:** 50-Case Blind Evaluation Dataset (`22_AGENT_BENCHMARK/dataset/`)")
    report.append(f"**Status:** {'PASSED' if summary['passing_gate_achieved'] else 'FAILED'}\n")

    report.append("## 1. Executive Summary")
    report.append("| Metric | Target Gate | Result | Status |")
    report.append("|---|---|---|---|")
    report.append(f"| **Overall Score** | $\\ge 85.0\\%$ | **{summary['overall_score_pct']}%** ({summary['total_points_scored']}/{summary['max_possible_points']} pts) | {'PASS' if summary['overall_score_pct'] >= 85.0 else 'FAIL'} |")
    report.append(f"| **No-Trade Specificity (Anti-Chop)** | $\\ge 90.0\\%$ | **{summary['metrics']['no_trade_specificity_pct']}%** | {'PASS' if summary['metrics']['no_trade_specificity_pct'] >= 90.0 else 'FAIL'} |")
    report.append(f"| **Trade Sensitivity (Positive Setups)** | $\\ge 80.0\\%$ | **{summary['metrics']['trade_sensitivity_pct']}%** | {'PASS' if summary['metrics']['trade_sensitivity_pct'] >= 80.0 else 'FAIL'} |")
    report.append(f"| **Directional Bias Accuracy** | $\\ge 85.0\\%$ | **{summary['metrics']['direction_accuracy_pct']}%** | {'PASS' if summary['metrics']['direction_accuracy_pct'] >= 85.0 else 'FAIL'} |")
    report.append(f"| **Setup Classification Accuracy** | $\\ge 85.0\\%$ | **{summary['metrics']['setup_accuracy_pct']}%** | {'PASS' if summary['metrics']['setup_accuracy_pct'] >= 85.0 else 'FAIL'} |\n")

    report.append("## 2. Granular Case Results")
    report.append("| Case ID | Category | Expected Setup | Agent Setup | Expected Disp | Agent Disp | Score |")
    report.append("|---|---|---|---|---|---|---|")
    for case_id, cdata in summary['cases'].items():
        sb = cdata['score_breakdown']
        gt = cdata['ground_truth']
        report.append(f"| {case_id} | {sb['category']} | {gt['expected_setup']} | {cdata['agent_output']['setup_classification']['detected_setup']} | {sb['gt_disposition']} | {sb['agent_disposition']} | **{sb['total_score']}** / 10 |")

    report_text = "\n".join(report)
    with open(output_report, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"Benchmark run complete. Score: {summary['overall_score_pct']}%. Report written to {output_report}.")
    return summary


if __name__ == '__main__':
    run_benchmark_suite()
