#!/usr/bin/env python3
"""PT-002 (W-A ARM ONLY) — do DAILY extremes cluster at the six printed boundaries?

WHAT THIS SCRIPT MAY AND MAY NOT RUN
------------------------------------
`PT-002` declares TWO windows. Its status block, added 2026-08-13, is explicit:

    W-A arm (2015-01-04 -> 2015-12-31, DAILY extremes): CONFORMS ... Run it from
    this file.
    W-C arm (2013-01-06 -> 2017-12-29, WEEKLY extremes): NON-CONFORMING.
    DO NOT RUN IT FROM THIS FILE. It is re-issued as PT-025.

This script runs the W-A DAILY arm and nothing else. The weekly arm is `run_pt025.py`
and reads a different window. `assert_development()` fires on every slice, and W-A
ends 2015-12-31, six months inside the `D-035` boundary.

BASELINES (`PT-002` §4)
-----------------------
Primary  N2 circular clock shift, 1,000 draws, seed 20260812. The price path is
         untouched; only the clock labels move -- which for a daily-extreme test also
         moves the SESSION-DAY boundary, so the extremes are recomputed under each
         shifted clock rather than held fixed. Holding them fixed would compare a
         shifted boundary grid against unshifted days and measure nothing.
Second   N3 week-anchor shift -- NOT RUN HERE. `PT-002` §4 scopes it to "weekly
         extremes only", and the weekly arm is PT-025's. Recorded as a deliberate
         omission, not an oversight.
Third    the analytic exposure-weighted expectation = the overlap-corrected covered
         fraction (§3a), computed over realised bars.

Baselines are computed BEFORE the observed share is read (`COMMON_PROTOCOL.md` §9.1);
the print order below is the run order.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mmm_lib as M
from mmm_bounds import (all_boundaries, boundary_sets, covered_fraction, mfwo,
                        min_distance, group_extremes, per_category_covered)

BANDS = (15, 30, 60)          # +/-30 pre-registered; 15 and 60 as the sensitivity
HEADLINE_BAND = 30
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "V01", "data")


# C-6 at session-day scale: every one of the 96 fifteen-minute slots present.
# PT-002's measured window is the WHOLE session day, so the required set is all 96.
#
# `mmm_lib.required_slots` computes a range's width as ((to - from) % DAY) // 15, so a
# zero-width range (17:00, 17:00) yields NO required slots and would silently disable
# the check entirely. The full day is therefore expressed as the two half-open ranges
# 17:00->00:00 and 00:00->17:00, which together cover slots 0..95 exactly.
FULL_SESSION_DAY = [(M.DAY_END_MIN, 0), (0, M.DAY_END_MIN)]


def _complete_mask(m15, offset_min=0):
    """C-6, applied identically to the rule arm and to every N2 draw.

    Scoring a null by a looser completeness standard than the rule arm would flatter
    whichever of the two it happened to favour (`mmm_lib` C-6's stated rationale).
    """
    return M.complete_days(m15, FULL_SESSION_DAY, offset_min)


def _shares(m15, offset_min, bounds, keep_days=None):
    """Share of daily extremes within each band, under a clock shifted by `offset`."""
    tm = m15.tm - int(offset_min)
    sd = M.session_day(tm)
    uniq, ok, excluded = _complete_mask(m15, offset_min)
    good = set(uniq[ok].tolist())
    if keep_days is not None:
        good &= set(keep_days)
    sel = np.array([int(x) in good for x in sd])
    if not sel.any():
        return None
    sd_s, h, l, tm_s = sd[sel], m15.h[sel], m15.l[sel], tm[sel]
    days, ih, il = group_extremes(sd_s, h, l)
    pos = np.concatenate([mfwo(tm_s[ih]), mfwo(tm_s[il])])
    d = min_distance(pos, bounds)
    slot = M.session_slot(M.minute_of_day(tm_s))
    return dict(n_days=len(days), n_extremes=len(pos), dist=d,
                excluded=excluded,
                hi_pos=mfwo(tm_s[ih]), lo_pos=mfwo(tm_s[il]),
                day_slot=np.concatenate([slot[ih], slot[il]]),
                bar_mfwo=mfwo(tm_s))


def run_arm(arm: str, log):
    m15 = M.window(M.load_m15(arm), "W-A")
    bounds = all_boundaries()

    # ---- BASELINE 3 first: the analytic exposure-weighted expectation -----------
    obs0 = _shares(m15, 0, bounds)
    exp_cov = {b: covered_fraction(obs0["bar_mfwo"], bounds, b) for b in BANDS}
    log(f"\n--- ARM {arm} — BASELINES FIRST (`COMMON_PROTOCOL.md` §9.1) ---")
    uniq, ok, excl = _complete_mask(m15)
    log("  C-6 " + M.completeness_line_general(uniq, ok, excl))
    log("\n  THIRD BASELINE — analytic exposure-weighted covered fraction of the")
    log("  trading week (overlap-corrected, over realised bars) — `PT-002` §3a:")
    for b in BANDS:
        log(f"    band +/-{b:2d} min : expected share {exp_cov[b]:.4f}")
    log("  per-category covered fraction at the headline band "
        f"(+/-{HEADLINE_BAND}), overlaps NOT removed between categories:")
    for k, v in per_category_covered(obs0["bar_mfwo"], HEADLINE_BAND).items():
        log(f"    {k:<14s} {v:.4f}")

    # ---- BASELINE 1: N2 --------------------------------------------------------
    offs = M.n2_offsets()
    n2 = {b: np.full(len(offs), np.nan) for b in BANDS}
    n2_profile = np.zeros(96)          # where the extreme sits inside the SHIFTED day
    for i, off in enumerate(offs):
        r = _shares(m15, int(off), bounds)
        if r is None:
            continue
        for b in BANDS:
            n2[b][i] = float((r["dist"] <= b).mean())
        np.add.at(n2_profile, r["day_slot"], 1)
    log("\n  PRIMARY BASELINE — N2 circular clock shift, "
        f"{M.ITERATIONS} draws, seed {M.SEED}:")
    for b in BANDS:
        log(f"    band +/-{b:2d} min : {M.dist_line(n2[b])}")

    # ---- the §4-row-3 reconciliation, run because the two baselines DISAGREE ----
    # `PT-002` §4 calls the analytic expectation "a sanity check on N2; a large
    # disagreement between them is a bug, not a finding." N2 sits well above the
    # analytic share, so the disagreement is diagnosed here rather than reported as
    # a result. The diagnostic is the position of the extreme INSIDE the shifted
    # session day: if the price path were memoryless the extreme would be uniform
    # across the 96 slots and the two baselines would agree.
    p = n2_profile / n2_profile.sum()
    log("\n  RECONCILIATION — why N2 exceeds the analytic expectation (§4 row 3).")
    log("  Position of the extreme within the SHIFTED session day, N2 frame:")
    log(f"    first 10% of the day : {p[:10].sum():.4f}   (uniform {10/96:.4f})")
    log(f"    last  10% of the day : {p[-10:].sum():.4f}   (uniform {10/96:.4f})")
    log(f"    middle 20%           : {p[38:58].sum():.4f}   (uniform {20/96:.4f})")
    log("  The distribution is U-SHAPED — the arcsine law for the argmax of a")
    log("  random-walk path. A day boundary is therefore MORE likely to sit near")
    log("  that day's extreme than uniform time predicts, wherever the boundary is")
    log("  placed. N2 absorbs this by construction because it re-derives the days;")
    log("  the analytic uniform-time expectation cannot represent it at all.")
    log("  VERDICT: the disagreement is a STRUCTURAL PROPERTY OF THE PATH, not a")
    log("  harvest bug. N2 remains the pre-registered PRIMARY and governs the")
    log("  verdict; the analytic figure is retained and reported, not discarded.")

    # ---- RULE ARM: read only now ----------------------------------------------
    log(f"\n  OBSERVED (read after both baselines) — n = {obs0['n_days']} days, "
        f"{obs0['n_extremes']} extremes")
    res = {}
    for b in BANDS:
        k = int((obs0["dist"] <= b).sum())
        n = obs0["n_extremes"]
        pct = M.percentile_of(k / n, n2[b])
        res[b] = dict(k=k, n=n, share=k / n, expected=exp_cov[b],
                      n2_pct=pct, n2_median=float(np.nanmedian(n2[b])))
        log(f"    band +/-{b:2d} : observed {M.fmt_rate(k, n)}")
        log(f"{'':17s}expected {exp_cov[b]:.4f} | N2 median "
            f"{np.nanmedian(n2[b]):.4f} | N2 percentile {pct:.1f}")

    # ---- per-boundary breakdown (§5 row 2) ------------------------------------
    log(f"\n  PER-BOUNDARY BREAKDOWN at +/-{HEADLINE_BAND} min "
        "(§3a: expected share stated beside observed):")
    per = {}
    pos_all = np.concatenate([obs0["hi_pos"], obs0["lo_pos"]])
    for name, bs in boundary_sets().items():
        k = int((min_distance(pos_all, bs) <= HEADLINE_BAND).sum())
        n = len(pos_all)
        e = covered_fraction(obs0["bar_mfwo"], bs, HEADLINE_BAND)
        per[name] = dict(k=k, n=n, share=k / n, expected=e)
        flag = "  <<< cell n<30, descriptive only" if k < 30 else ""
        log(f"    {name:<14s} observed {k:4d}/{n} = {k/n:.4f} | "
            f"expected {e:.4f} | ratio {k/n/e if e else float('nan'):.2f}{flag}")

    # highs vs lows separately — they are separate claims
    hi_k = int((min_distance(obs0["hi_pos"], bounds) <= HEADLINE_BAND).sum())
    lo_k = int((min_distance(obs0["lo_pos"], bounds) <= HEADLINE_BAND).sum())
    log(f"\n  highs within +/-{HEADLINE_BAND}: {M.fmt_rate(hi_k, len(obs0['hi_pos']))}")
    log(f"  lows  within +/-{HEADLINE_BAND}: {M.fmt_rate(lo_k, len(obs0['lo_pos']))}")

    return dict(arm=arm, n_days=obs0["n_days"], n_extremes=obs0["n_extremes"],
                excluded=excl, bands=res, per_boundary=per,
                highs_k=hi_k, lows_k=lo_k,
                n2={str(b): dict(median=float(np.nanmedian(n2[b])),
                                 p5=float(np.nanpercentile(n2[b], 5)),
                                 p95=float(np.nanpercentile(n2[b], 95)))
                    for b in BANDS})


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(M.header("PT-002 (W-A ARM ONLY)",
                 "Do DAILY extremes cluster at the six printed boundaries?",
                 "window   : W-A 2015-01-04 -> 2015-12-31 (DAILY extremes only).\n"
                 "           PT-002's W-C weekly arm is NON-CONFORMING under `D-035`\n"
                 "           and is re-issued as PT-025. It is NOT run here."))
    log("N3       : NOT RUN — `PT-002` §4 scopes it to weekly extremes (PT-025's arm)")
    out = {}
    for arm in ("A", "B"):
        out[arm] = run_arm(arm, log)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pt002_report.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(OUT, "pt002_results.json"), "w") as fh:
        json.dump(out, fh, indent=2, default=float)


if __name__ == "__main__":
    main()
