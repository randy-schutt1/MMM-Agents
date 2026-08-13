#!/usr/bin/env python3
"""PT-033 — POST-HOC SENSITIVITY. NOT PART OF THE PRE-REGISTERED RESULT.

PT-033 §7 fixed a mechanical drop rule: days with fewer than 4 bars are dropped. Running
the test surfaced a consequence of that rule interacting with D-031 Arm B that the
pre-registration did not anticipate, and this script measures it.

WHY IT EXISTS. The corpus's week CLOSES at 17:00 fixed EST (D-036a). Under Arm B the same
instant is stamped 18:00 during US DST, so the last hour of each DST Friday falls PAST the
17:00 day boundary and forms a 4-bar stub 'day'. Those stubs are legitimate under the
pre-registered rule -- they have exactly 4 bars -- and they are why cell B|D-SESSION holds
1,021 days where cell A|D-SESSION holds 904.

WHAT THIS SCRIPT DOES NOT DO. It does not replace, correct or supersede the headline
result. The pre-registered numbers stand exactly as run. This is a disclosed sensitivity,
reported alongside them, per BACKTEST_EVIDENCE_STANDARD.md's requirement that every test
performed is reported.

Usage:  python3 06_MANUAL_BACKTEST/V07/sensitivity_pt033.py
"""
import os, sys, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_pt033 as R

MIN_BARS_SENSITIVITY = 8          # 2 hours; post hoc, and labelled as such

def main():
    print("=" * 78)
    print("PT-033 POST-HOC SENSITIVITY — stub days under D-031 Arm B")
    print("  PRE-REGISTERED rule: drop days with < 4 bars   (headline result)")
    print(f"  SENSITIVITY  rule: drop days with < {MIN_BARS_SENSITIVITY} bars  (this script only)")
    print("=" * 78)
    for arm in ("A", "B"):
        bars = R.load(os.path.join(R.DATA, f"GBPUSD_M15_ARM{arm}.csv"))
        for daydef in ("D-SESSION", "D-MIDNIGHT"):
            days, dropped4 = R.group_days(bars, daydef)
            stubs = {k: v for k, v in days.items() if len(v) < MIN_BARS_SENSITIVITY}
            kept = {k: v for k, v in days.items() if len(v) >= MIN_BARS_SENSITIVITY}
            obs = R.rule_arm(kept, 0)
            byday = {}
            for k, d, h in obs:
                byday[k] = byday.get(k, False) or h
            f_day = sum(1 for v in byday.values() if v) / len(byday)
            rng = sorted(((max(b[2] for b in v) - min(b[3] for b in v)) / R.PIP) for v in kept.values())
            stub_rng = sorted(((max(b[2] for b in v) - min(b[3] for b in v)) / R.PIP) for v in stubs.values()) or [float('nan')]
            print(f"\n  cell {arm}|{daydef}")
            print(f"    days at >=4 bars (pre-registered) : {len(days)}")
            print(f"    stub days (4..{MIN_BARS_SENSITIVITY-1} bars)          : {len(stubs)}"
                  f"   median range {statistics.median(stub_rng):.1f} pips")
            print(f"    days at >={MIN_BARS_SENSITIVITY} bars (sensitivity)  : {len(kept)}"
                  f"   median range {statistics.median(rng):.1f} pips")
            print(f"    f50_day  sensitivity              : {f_day:.4f}")

if __name__ == "__main__":
    main()
