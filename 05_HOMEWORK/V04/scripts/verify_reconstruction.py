#!/usr/bin/env python3
"""Recompute V04 homework §1.2 validation 3 from the committed JSON alone.

Added 2026-08-11 while remediating V04 review R1 finding `M1` (`E19`).

WHAT THIS EXISTS FOR
--------------------
R1 found that USDCHF's committed 15-minute week slice was mis-aligned at the week-open
bar, and that the resulting 27/30 reconstruction had been reported as ±0.4 pip harvest
noise when bar 0's *open* differed by 28.1 pips. The slice is now corrected. This script
is the mechanical check that says so, and it is committed so the claim in §1.2 is
re-derivable by someone who was not here.

THE DEFECT, IN ONE PARAGRAPH
----------------------------
On this feed USDCHF's first 4-hour bar of the week is a PARTIAL bar of only twelve
15-minute bars — the pair's session opens an hour after the other three majors. The 15m
slice was cut with a fixed sixteen-bars-per-4h-bar assumption, so it began four bars too
early: the committed 480-bar window carried four PREVIOUS-week bars at its head, and the
weekend gap (a -12.7 pip discontinuity, the only 15m discontinuity in the whole dataset)
sat *inside* what the file called "the week". Dropping those four bars leaves 476 =
12 + 29x16, which is the complete week for this pair. Nothing was missing from the tail.

Run:  python3 verify_reconstruction.py
Exits non-zero if the committed data no longer reproduces the figures in §1.2.
"""

import json
import os
import sys

DATA = os.path.join(os.path.dirname(__file__), "..", "data",
                    "v04_week_2026-08-02_4h_and_15m.json")

# Expected, as stated in V04_HOMEWORK.md §1.2 validation 3 after the M1 correction.
EXPECTED = {
    "EURUSD": (30, 120),
    "GBPUSD": (28, 118),
    "USDJPY": (30, 120),
    "USDCHF": (28, 118),
}


def aggregate(seg):
    """Aggregate a run of 15m bars into one OHLC bar."""
    return [seg[0][0], max(b[1] for b in seg), min(b[2] for b in seg), seg[-1][3]]


def windows(n0, count=30):
    """15m index windows per 4h bar, honouring a partial first bar of n0 bars."""
    yield 0, n0
    for k in range(1, count):
        yield n0 + (k - 1) * 16, n0 + k * 16


def main():
    data = json.load(open(DATA))
    ok = True
    total_bars = total_fields = 0

    for pair, v in data.items():
        m, f, pip = v["bars_15m_week"], v["bars_4h"], v["pip"]
        n0 = v["bars_15m_in_4h_bar_0"]

        # (1) the week's 15m bar count must equal n0 + 29 full bars
        assert len(m) == n0 + 29 * 16, (pair, len(m), n0)

        # (2) no discontinuity may sit inside the week: each bar's open == prior close
        breaks = [i for i in range(len(m) - 1) if abs(m[i + 1][0] - m[i][3]) > 1e-9]

        # (3) the 15m series must reconstruct the 4h series
        bars = fields = 0
        detail = []
        for k, (a, b) in enumerate(windows(n0)):
            agg = aggregate(m[a:b])
            match = [abs(agg[j] - f[k][j]) < 1e-9 for j in range(4)]
            fields += sum(match)
            if all(match):
                bars += 1
            else:
                detail.append((k, [round((agg[j] - f[k][j]) / pip, 2) for j in range(4)]))

        exp_bars, exp_fields = EXPECTED[pair]
        good = (bars, fields) == (exp_bars, exp_fields) and not breaks
        ok &= good
        total_bars += bars
        total_fields += fields

        print("%-7s first-4h-bar %2d x 15m | %2d/30 bars %3d/120 fields | "
              "in-week 15m discontinuities: %d | %s"
              % (pair, n0, bars, fields, len(breaks), "OK" if good else "MISMATCH"))
        for k, diff in detail:
            print("            4h bar %2d differs by %s pips (O,H,L,C)" % (k, diff))

    print("\nTOTAL: %d/120 bars, %d/480 fields (%.2f%%)"
          % (total_bars, total_fields, 100.0 * total_fields / 480))
    print("Expected after the M1 correction: 116/120 bars, 476/480 fields (99.17%)")

    if not ok:
        print("\nFAIL — the committed data no longer matches V04_HOMEWORK.md §1.2.")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
