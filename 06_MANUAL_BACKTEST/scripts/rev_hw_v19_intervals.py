#!/usr/bin/env python3
"""Wilson 95% intervals for every rate in V19_HOMEWORK.md §§4-6.

Added 2026-08-15 discharging REVIEW_INDEX.md item 302, whose secondary instance is
that the homework quotes rates without intervals (BACKTEST_EVIDENCE_STANDARD.md §4.2).

This does NOT re-run the homework and does NOT touch hw_v19.py or its JSON. It mirrors
hw_v19.blocks()'s definitions exactly and reports the COUNTS behind each rate, which the
committed JSON stores only as fractions, so a Wilson interval can be formed.
"""
import os, sys
import numpy as np
from math import sqrt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mmm_lib as M
import hw_v19 as H


def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)


def row(label, k, n):
    lo, hi = wilson(k, n)
    print(f"  {label:26s} {k:4d}/{n:4d} = {100*k/n:5.1f}%   Wilson95 [{lo:4.1f}%, {hi:4.1f}%]")


M.qa_gate()
for arm in ("A", "B"):
    for win in ("W-A", "W-B"):
        m15 = M.window(M.load_m15(arm), win)
        days = M.build_days(m15, offset_min=0, require_full=True)
        hi = days["post_hi"].to_numpy(); lo = days["post_lo"].to_numpy()
        rng = (hi - lo) / M.PIP
        print(f"\n=== arm {arm} / {win} ===")
        for p in H.ADR_PERIODS:
            adr = np.convolve(rng, np.ones(p) / p, mode="valid")[:-1]
            ex = rng[p:] > adr
            row(f"next day exceeds ADR{p}", int(ex.sum()), len(ex))
        h1, l1 = hi[1:] >= hi[:-1], lo[1:] <= lo[:-1]
        row("prev high touched", int(h1.sum()), len(h1))
        row("prev low touched", int(l1.sum()), len(l1))
        row("both touched", int((h1 & l1).sum()), len(h1))
        row("neither touched", int((~h1 & ~l1).sum()), len(h1))
        pulls = []
        sd, mod = m15.sd, m15.mod
        post = (mod >= M.BOX_END_MIN) & (mod < M.DAY_END_MIN)
        for day in sorted(set(days["sd"].tolist())):
            m = post & (sd == day)
            hh, ll = m15.h[m], m15.l[m]
            if len(hh) < H.PULLBACK_BARS + 2:
                continue
            k = int(np.argmax(hh))
            if k + H.PULLBACK_BARS >= len(hh):
                continue
            pulls.append((float(hh[k]) - float(ll[k+1:k+1+H.PULLBACK_BARS].min())) / M.PIP)
        pulls = np.array(pulls); n = len(pulls)
        row("pullback in 15-25", int(((pulls >= 15) & (pulls <= 25)).sum()), n)
        row("pullback < 15", int((pulls < 15).sum()), n)
        row("pullback > 50", int((pulls > 50).sum()), n)
