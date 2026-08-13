#!/usr/bin/env python3
"""Measure per-bar highs and lows off the committed USD/CHF 1H screenshot.

Written for the V02 R1 remediation (see 18_REVIEW/V02/V02_REVIEW_R1.md, MAJOR 1).
The first-pass 11a markup read prices off the axis by eye and got several of them
wrong. This script exists so that every price in the corrected markup is
reproducible by someone who was not in the session that produced it.

    python3 05_HOMEWORK/V02/measure_usdchf_week.py

Requires Pillow and numpy. It reads only the committed PNG; it does not touch the
network and does not need a TradingView account.

Method
------
1. Price axis calibration. The axis labels printed on the right of the image are
   located by their text rows and fitted linearly against their known values.
   The fit residual is reported; it is well under a tenth of a pip.
2. Bar grid. Candle bodies are 5 px wide on a 6 px pitch, with the wick on the
   centre column. Centres therefore sit at x = 3 (mod 6).
3. Day boundaries. Taken from the chart's own date-axis labels, not from eyeballed
   ticks. The single-character labels (4, 5, 6, 7, 9) are exactly 144 px = 24 bars
   apart, which fixes the grid; Friday's 21 bars and Sunday's 3 bars fall out of
   the same chain and are cross-checked against it.
4. Bar extremes. For each bar the *contiguous* run of candle-coloured pixels in
   its centre column is taken. Using one contiguous run rather than the column's
   min/max is what excludes the dotted last-price line and the header text, both
   of which are drawn in the candle colours and corrupted an earlier attempt.

Timebase check
--------------
The footer clock reads 19:21:20 UTC and the last-price countdown reads 38:40,
so the rightmost bar is the 19:00 UTC hour of Mon 10 Aug 2026. Its measured centre
is x = 1119, which is exactly where the day grid above puts it. That is the
independent confirmation that the grid is aligned and that the hour indices below
are UTC.

Known uncertainty
-----------------
The Sunday/Monday boundary for 2-3 Aug is uncertain by one bar. Counting Monday's
24 bars back from the label-verified Tue 4 Aug tick leaves Sunday 2 Aug with two
bars; the "Aug" month label sits on the first of them. Sun 9 Aug carries three.
Nothing in the markup turns on it: the two candidate lows, 0.80551 and 0.80559,
both sit in the Sunday-open / Monday-first-hour window either way.
"""

from pathlib import Path

import numpy as np
from PIL import Image

CHART = Path(__file__).with_name("charts") / "USDCHF_1H_2026-08-10_tradingview-fxcm.png"

# Right-hand price-axis labels: text-row centre (y px) -> printed price.
AXIS_LABELS = {
    81: 0.817, 133: 0.816, 185: 0.815, 237: 0.814, 290: 0.813, 342: 0.812,
    394: 0.811, 499: 0.809, 551: 0.808, 603: 0.807, 656: 0.806, 708: 0.805,
    760: 0.804,
}
# 0.81000 is omitted: the last-price badge covers it.

GREEN = (8, 153, 129)
RED = (242, 54, 69)

# (label, x of the day's first bar centre, bar count, UTC hour of that first bar).
# Sundays open partway through the day, so their first bar is not 00:00.
DAYS = [
    ("Thu 30 Jul", 3, 24, 0),
    ("Fri 31 Jul", 147, 21, 0),
    ("Sun 2 Aug", 273, 2, 22),
    ("Mon 3 Aug", 285, 24, 0),
    ("Tue 4 Aug", 429, 24, 0),
    ("Wed 5 Aug", 573, 24, 0),
    ("Thu 6 Aug", 717, 24, 0),
    ("Fri 7 Aug", 861, 21, 0),
    ("Sun 9 Aug", 987, 3, 21),
    ("Mon 10 Aug", 1005, 20, 0),
]

PLOT_X = (51, 1121)   # candle area; the last-price badge starts at 1183
PLOT_Y = (66, 840)    # below the symbol header, above the date axis


def contiguous_runs(mask_column):
    ys = np.flatnonzero(mask_column)
    if len(ys) == 0:
        return []
    runs, start, prev = [], ys[0], ys[0]
    for y in ys[1:]:
        if y == prev + 1:
            prev = y
        else:
            runs.append((start, prev))
            start = prev = y
    runs.append((start, prev))
    return runs


def main():
    img = np.array(Image.open(CHART).convert("RGB")).astype(int)

    ys = np.array(sorted(AXIS_LABELS))
    ps = np.array([AXIS_LABELS[y] for y in ys])
    fit = np.polyfit(ys, ps, 1)
    resid = np.abs(ps - np.polyval(fit, ys)).max()
    print(f"axis fit: {1e-3 / abs(fit[0]):.2f} px per 10 pips; "
          f"max residual {resid * 1e4:.2f} pip")

    def price(y):
        return float(np.polyval(fit, y))

    candle = (np.all(np.abs(img - np.array(GREEN)) <= 8, axis=2)
              | np.all(np.abs(img - np.array(RED)) <= 8, axis=2))
    candle[: PLOT_Y[0], :] = False
    candle[PLOT_Y[1]:, :] = False

    def bar(x):
        runs = contiguous_runs(candle[:, x])
        if not runs:
            return None
        top, bottom = max(runs, key=lambda r: r[1] - r[0])
        return price(top), price(bottom)

    print()
    print(f"{'day':12s} {'bars':>5s}  {'high':>9s} {'at':>6s}  {'low':>9s} {'at':>6s}  {'range':>7s}")
    detail = {}
    for name, x0, count, hour0 in DAYS:
        rows = []
        for i in range(count):
            x = x0 + 6 * i
            if not (PLOT_X[0] <= x <= PLOT_X[1]):
                continue
            got = bar(x)
            if got:
                rows.append((hour0 + i, got[0], got[1]))
        if not rows:
            continue
        detail[name] = rows
        hi = max(r[1] for r in rows)
        lo = min(r[2] for r in rows)
        hi_at = next(r[0] for r in rows if r[1] == hi)
        lo_at = next(r[0] for r in rows if r[2] == lo)
        print(f"{name:12s} {len(rows):5d}  {hi:9.5f} {hi_at:02d}:00  "
              f"{lo:9.5f} {lo_at:02d}:00  {(hi - lo) * 1e4:6.1f}p")

    # When did price first trade back above the Monday high? This is the only
    # number in the markup that bears on C-001, so it is computed rather than eyeballed.
    monday_high = max(r[1] for r in detail["Mon 3 Aug"])
    monday_high_at = next(r[0] for r in detail["Mon 3 Aug"] if r[1] == monday_high)
    print()
    print(f"Monday high {monday_high:.5f} set at Mon 3 Aug {monday_high_at:02d}:00 UTC")
    hours = 0
    order = ["Mon 3 Aug", "Tue 4 Aug", "Wed 5 Aug", "Thu 6 Aug", "Fri 7 Aug"]
    for day in order:
        for i, hi, _lo in detail[day]:
            if day == "Mon 3 Aug" and i <= monday_high_at:
                continue
            hours += 1
            if hi > monday_high:
                print(f"first bar back above it: {day} {i:02d}:00 UTC "
                      f"(high {hi:.5f}) — {hours} hours later")
                return


if __name__ == "__main__":
    main()
