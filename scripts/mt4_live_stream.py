#!/usr/bin/env python3
"""
scripts/mt4_live_stream.py — Real-Time MT4 Market Streamer & Intelligence Pipeline
================================================================================
Monitors MetaTrader 4 in real time during London and New York sessions:
- Ingests live M15 candlestick closes
- Extracts Market Maker Method state vector via scripts/mmm_engine.py
- Cross-validates against MT4 custom DLL indicator buffers
- Auto-renders synchronized visual SVG charts
- Runs prospective setup evaluation without lookahead bias
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime
from typing import Dict, Any, Optional

from scripts.mt4_client import MT4BridgeClient
from scripts.mmm_engine import MMMEngine, MMMBar
from scripts.mmm_chart_generator import render_mmm_chart
from 22_AGENT_BENCHMARK.agent_harness import CanonicalExpertEvaluator


def run_live_stream(
    symbol: str = "GBPUSD",
    poll_interval_sec: float = 10.0,
    host: str = "127.0.0.1",
    port: int = 5555,
    custom_indicator: Optional[str] = None,
    output_chart: str = "live_chart.svg",
    log_file: str = "live_stream_log.jsonl"
):
    """Continuously monitors MT4 and runs live MMM analysis."""
    client = MT4BridgeClient(host=host, port=port)
    engine = MMMEngine()
    evaluator = CanonicalExpertEvaluator()

    print(f"Connecting to MT4 Bridge at {host}:{port}...")
    if not client.connect():
        print(f"ERROR: Could not connect to MT4 Bridge on {host}:{port}. Is MMM_MT4_Bridge.mq4 running in MT4?")
        return

    print(f"Connected to MT4 successfully. Monitoring {symbol} M15...")
    last_bar_time = None

    try:
        while True:
            try:
                # 1. Fetch recent M15 bars
                bars = client.get_candlesticks(symbol, timeframe=15, count=250)
                if not bars:
                    time.sleep(poll_interval_sec)
                    continue

                latest_bar = bars[-1]
                curr_bar_time = latest_bar.dt

                # 2. Check if new bar arrived or updated
                if curr_bar_time != last_bar_time:
                    last_bar_time = curr_bar_time
                    target_idx = len(bars) - 1

                    # 3. Extract MMM deterministic state
                    state = render_mmm_chart(bars, target_idx, engine, output_chart, lookback_bars=192, title=f"Live MMM Stream — {symbol} M15")

                    # 4. Optional: Read custom DLL indicator buffer
                    custom_val = None
                    if custom_indicator:
                        try:
                            custom_val = client.get_custom_indicator(custom_indicator, buffer_idx=0, shift=0, symbol=symbol, timeframe=15)
                        except Exception as e:
                            custom_val = f"Read Error: {e}"

                    # 5. Run Expert Evaluator
                    decision = evaluator.evaluate(state)

                    # 6. Format console alert
                    sess = state['session_metrics']
                    tdi = state['indicators']['tdi']
                    disp = decision['trade_decision']['disposition']
                    dir_bias = decision['setup_classification']['direction']
                    setup_name = decision['setup_classification']['detected_setup']

                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {symbol} M15 Close: {latest_bar.close:.5f} | Session: {state['metadata']['active_session']}")
                    print(f"  └─ Asian Box: {sess['asian_box']['range_pips']}p [{sess['asian_box']['status']}] | ADR Used: {sess['adr']['adr_percentage_used']}%")
                    print(f"  └─ TDI Shark Fin: {tdi['shark_fin_direction']} | 5/13 Cross: {state['indicators']['ema_crosses']['5_13_cross_direction']}")
                    print(f"  └─ DECISION: [{disp}] Bias: {dir_bias} | Setup: {setup_name} | Confidence: {decision['confidence_score']['total_confidence_pct']}%")
                    if custom_val is not None:
                        print(f"  └─ Custom DLL ({custom_indicator}): {custom_val}")
                    print(f"  └─ Chart updated: {output_chart}\n")

                    # 7. Append to JSONL log
                    log_entry = {
                        "timestamp": datetime.now().isoformat(),
                        "symbol": symbol,
                        "bar_time": curr_bar_time.isoformat(),
                        "close": latest_bar.close,
                        "state": state,
                        "decision": decision,
                        "custom_indicator_value": custom_val
                    }
                    with open(log_file, "a", encoding="utf-8") as f:
                        f.write(json.dumps(log_entry) + "\n")

            except Exception as loop_err:
                print(f"Stream iteration warning: {loop_err}")

            time.sleep(poll_interval_sec)

    except KeyboardInterrupt:
        print("\nStopping MT4 live stream.")
    finally:
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Live MT4 Market Streamer")
    parser.add_argument("--symbol", default="GBPUSD", help="Symbol (default: GBPUSD)")
    parser.add_argument("--host", default="127.0.0.1", help="Bridge Host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5555, help="Bridge Port (default: 5555)")
    parser.add_argument("--interval", type=float, default=10.0, help="Poll interval in seconds (default: 10.0)")
    parser.add_argument("--custom-ind", default=None, help="Name of custom DLL indicator in MT4")
    parser.add_argument("--output-chart", default="live_chart.svg", help="Output chart path")
    parser.add_argument("--log-file", default="live_stream_log.jsonl", help="JSONL log file")
    args = parser.parse_args()

    run_live_stream(
        symbol=args.symbol,
        poll_interval_sec=args.interval,
        host=args.host,
        port=args.port,
        custom_indicator=args.custom_ind,
        output_chart=args.output_chart,
        log_file=args.log_file
    )
