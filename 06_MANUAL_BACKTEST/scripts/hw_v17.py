#!/usr/bin/env python3
"""V17 HOMEWORK -- the measurable half of the seven-point safety-trade answer key,
plus the student flashcard's Asian-range size filter.

This is HOMEWORK, not a pre-registered test. It states no hypothesis, scores no
prediction and produces no verdict. It exists to find out how far V17's own
checklist can be carried on real data before it stops -- which is A-116/A-117
demonstrated rather than asserted.

Everything reads M1/M15 bars parsed from the checksummed HistData corpus. Nothing is
read from a rendering. No M, W, peak formation, TDI value or entry is computed (§1b of
PT-045 applies here too).

usage:  python3 hw_v17.py > ../../05_HOMEWORK/V17/data/hw_v17_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

FLASHCARD_FILTER = 50.0        # "Asian range less than 50pips" -- V17_00-14-15
HUNT_LO, HUNT_HI = 25.0, 50.0  # "25 to 50 pips as his normal stop hunt"  [00:28:59]
YLOD_LO, YLOD_HI = 25.0, 75.0  # "25 to 75 pips off Y-LOD"  -- answer key point 3
ARMS = ["A", "B"]


def run(arm):
    m15 = L.load_m15(arm)                      # DEVELOPMENT scope by default
    days = L.build_days(m15, require_full=True)

    box_hi = days["box_hi"].to_numpy()
    box_lo = days["box_lo"].to_numpy()
    post_hi = days["post_hi"].to_numpy()
    post_lo = days["post_lo"].to_numpy()
    day_lo = np.minimum(box_lo, post_lo)
    day_hi = np.maximum(box_hi, post_hi)
    n = len(days)

    # ---- HW1: the flashcard's Asian-range size filter
    box_rng = (box_hi - box_lo) / L.PIP
    under = float(np.mean(box_rng < FLASHCARD_FILTER))

    # ---- HW2: answer-key point 4 -- "Dealer Cuts the Asain Range as a visible stop hunt"
    #      Measured as the post-box excursion BEYOND each box edge, in pips.
    down_ext = np.maximum((box_lo - post_lo) / L.PIP, 0.0)
    up_ext = np.maximum((post_hi - box_hi) / L.PIP, 0.0)
    cut_either = float(np.mean((down_ext > 0) | (up_ext > 0)))
    in_band_down = float(np.mean((down_ext >= HUNT_LO) & (down_ext <= HUNT_HI)))
    in_band_up = float(np.mean((up_ext >= HUNT_LO) & (up_ext <= HUNT_HI)))
    in_band_either = float(np.mean(
        ((down_ext >= HUNT_LO) & (down_ext <= HUNT_HI)) |
        ((up_ext >= HUNT_LO) & (up_ext <= HUNT_HI))))

    # ---- HW3: answer-key point 3 -- "Dealer is Trading 25 to 75 pips off Y-LOD"
    #      Distance from TODAY's low to YESTERDAY's low, signed (positive = above).
    prev_lo = np.concatenate(([np.nan], day_lo[:-1]))
    prev_hi = np.concatenate(([np.nan], day_hi[:-1]))
    d_lo = (day_lo - prev_lo) / L.PIP
    d_hi = (prev_hi - day_hi) / L.PIP
    ok = ~np.isnan(d_lo)
    lo_in = float(np.mean((d_lo[ok] >= YLOD_LO) & (d_lo[ok] <= YLOD_HI)))
    hi_in = float(np.mean((d_hi[ok] >= YLOD_LO) & (d_hi[ok] <= YLOD_HI)))
    either_in = float(np.mean(
        ((d_lo[ok] >= YLOD_LO) & (d_lo[ok] <= YLOD_HI)) |
        ((d_hi[ok] >= YLOD_LO) & (d_hi[ok] <= YLOD_HI))))

    # ---- HW2 x HW1: does the flashcard's filter change the stop-hunt rate?
    small = box_rng < FLASHCARD_FILTER
    band = ((down_ext >= HUNT_LO) & (down_ext <= HUNT_HI)) | \
           ((up_ext >= HUNT_LO) & (up_ext <= HUNT_HI))
    band_small = float(np.mean(band[small])) if small.any() else float("nan")
    band_big = float(np.mean(band[~small])) if (~small).any() else float("nan")

    def ci(p, k_n):
        lo, hi = L.wilson_ci(int(round(p * k_n)), k_n)
        return [round(lo, 4), round(hi, 4)]

    return dict(
        arm=arm, n_days=int(n),
        completeness=L.completeness_line(days),
        HW1_box_range_median_pips=round(float(np.median(box_rng)), 1),
        HW1_box_range_p25_p75=[round(float(np.percentile(box_rng, 25)), 1),
                               round(float(np.percentile(box_rng, 75)), 1)],
        HW1_frac_under_50=round(under, 4),
        HW1_frac_under_50_ci=ci(under, n),
        HW2_frac_cuts_either_edge=round(cut_either, 4),
        HW2_median_down_ext=round(float(np.median(down_ext)), 1),
        HW2_median_up_ext=round(float(np.median(up_ext)), 1),
        HW2_frac_down_in_25_50=round(in_band_down, 4),
        HW2_frac_up_in_25_50=round(in_band_up, 4),
        HW2_frac_either_in_25_50=round(in_band_either, 4),
        HW2_frac_either_in_25_50_ci=ci(in_band_either, n),
        HW2_band_rate_small_box=round(band_small, 4),
        HW2_band_rate_big_box=round(band_big, 4),
        HW3_n=int(ok.sum()),
        HW3_median_low_vs_ylod=round(float(np.median(d_lo[ok])), 1),
        HW3_frac_low_25_75_above_ylod=round(lo_in, 4),
        HW3_frac_high_25_75_below_yhod=round(hi_in, 4),
        HW3_frac_either=round(either_in, 4),
        HW3_frac_either_ci=ci(either_in, int(ok.sum())),
    )


def main():
    print("V17 HOMEWORK -- the measurable half of the seven-point answer key")
    print("NOT a pre-registered test. No hypothesis, no prediction, no verdict.")
    print()
    rep, sha = L.qa_gate()
    print("QA GATE [development]: PASSED")
    print()
    out = []
    for arm in ARMS:
        r = run(arm)
        out.append(r)
        print(f"--- arm {arm} / D-035 DEVELOPMENT ---")
        for k, v in r.items():
            if k == "arm":
                continue
            print(f"    {k:34s} {v}")
        print()
    with open("../../05_HOMEWORK/V17/data/hw_v17_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print("wrote ../../05_HOMEWORK/V17/data/hw_v17_results.json")


if __name__ == "__main__":
    main()
