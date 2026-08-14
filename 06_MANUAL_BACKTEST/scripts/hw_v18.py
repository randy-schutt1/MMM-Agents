#!/usr/bin/env python3
"""V18 HOMEWORK -- the one measurable item of the four V18 actually sets.

V18's assignment, `[00:45:31]`-`[00:46:04]`:
  1. "draw your line[s] on 24 hour chart[s]"            -- not measurable, a drawing task
  2. "look for peak formation"                          -- NOT measurable: V18 never
                                                           constructs a peak formation
  3. "Look for the dealer to make the high and low of   -- ** MEASURABLE **
      the week"
  4. "Look for clean, seeable flashcards setups"        -- not measurable here

This is HOMEWORK, not a pre-registered test. It states no hypothesis, scores no
prediction and produces no verdict. It exists to find out how far V18's own assignment
can be carried on real data before it stops.

Item 3 is measurable because "the high and low of the week" needs no formation
recognition -- only an extreme and a clock. WHEN in the week do they land?

Everything reads M1/M15 bars parsed from the checksummed HistData corpus. Nothing is
read from a rendering. No M, W, peak formation, level or entry is computed.

usage:  python3 hw_v18.py > ../../05_HOMEWORK/V18/data/hw_v18_output.txt
"""
from __future__ import annotations

import json
import numpy as np

import mmm_lib as L

ARMS = ["A", "B"]
BUCKETS_PER_DAY = 96
ANCHOR = L.SESSION_ANCHOR
SESSION_NAMES = {0: "S1 Asian 17:00-03:00", 1: "S2 London 03:00-09:00",
                 2: "S3 US 09:00-17:00"}
DOW = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def session_index(mod):
    off = (np.asarray(mod) - ANCHOR) % L.DAY
    idx = np.zeros(len(off), dtype="int64")
    idx[(off >= 600) & (off < 960)] = 1
    idx[off >= 960] = 2
    return idx


def trading_week(sd):
    """Week key: session days grouped Mon-Fri. Session day D starts at D-1 17:00, so
    the Sunday-evening open belongs to Monday's session day already."""
    return (np.asarray(sd) + 3) // 7          # arbitrary but contiguous Mon-anchored


def run(arm):
    m15 = L.load_m15(arm)                     # DEVELOPMENT scope by default
    sd, mod = m15.sd, m15.mod
    slot = L.session_slot(mod)

    present = {}
    for d, s in zip(sd, slot):
        present.setdefault(int(d), set()).add(int(s))
    ok_days = {d for d, s in present.items() if len(s) == BUCKETS_PER_DAY}
    keep = np.array([int(d) in ok_days for d in sd])
    excluded = len(present) - len(ok_days)

    tm, h, l, sd2, mod2 = m15.tm[keep], m15.h[keep], m15.l[keep], sd[keep], mod[keep]
    si = session_index(mod2)
    wk = trading_week(sd2)

    rows = []
    for w in np.unique(wk):
        m = wk == w
        if m.sum() < 96 * 3:                  # need at least ~3 complete days
            continue
        hi_i = np.argmax(h[m])
        lo_i = np.argmin(l[m])
        d_in_wk = sd2[m] - sd2[m].min()
        rows.append((int(d_in_wk[hi_i]), int(si[m][hi_i]),
                     int(d_in_wk[lo_i]), int(si[m][lo_i])))
    rows = np.array(rows)
    n = len(rows)

    def dist(col, k):
        c = np.bincount(rows[:, col], minlength=k)
        return {i: (int(c[i]), 100.0 * c[i] / n) for i in range(k)}

    return dict(arm=arm, n_weeks=n, n_days_excluded=int(excluded),
                hi_day=dist(0, 6), hi_sess=dist(1, 3),
                lo_day=dist(2, 6), lo_sess=dist(3, 3))


def main():
    print("=" * 78)
    print("V18 HOMEWORK -- item 3: WHEN does the dealer make the high and low of the week?")
    print('V18 [00:45:58]: "Look for the dealer to make the high and low of the week"')
    print("=" * 78)
    print("\nNOT a test. No hypothesis, no prediction, no verdict.")
    print("Session boundaries are the DECLARED convention of PT-046 s2a -- V18 states")
    print("no clock time for any session. Read the percentages with that in mind.\n")

    L.qa_gate()
    out = {}
    for arm in ARMS:
        r = run(arm)
        out[arm] = r
        print("-" * 78)
        print(f"ARM {arm}   complete weeks {r['n_weeks']}   "
              f"(incomplete session days excluded: {r['n_days_excluded']})")
        print("\n  WEEKLY HIGH lands on day-of-week (0 = first session day of the week):")
        for i, (c, p) in r["hi_day"].items():
            print(f"    day +{i}: {c:4d}  {p:5.1f}%  {'#' * int(p / 2)}")
        print("\n  WEEKLY HIGH lands in session:")
        for i, (c, p) in r["hi_sess"].items():
            print(f"    {SESSION_NAMES[i]:26s}: {c:4d}  {p:5.1f}%  {'#' * int(p / 2)}")
        print("\n  WEEKLY LOW lands on day-of-week:")
        for i, (c, p) in r["lo_day"].items():
            print(f"    day +{i}: {c:4d}  {p:5.1f}%  {'#' * int(p / 2)}")
        print("\n  WEEKLY LOW lands in session:")
        for i, (c, p) in r["lo_sess"].items():
            print(f"    {SESSION_NAMES[i]:26s}: {c:4d}  {p:5.1f}%  {'#' * int(p / 2)}")
        print()

    with open("../../05_HOMEWORK/V18/data/hw_v18_results.json", "w") as f:
        json.dump(out, f, indent=2, default=float)
    print("wrote ../../05_HOMEWORK/V18/data/hw_v18_results.json")


if __name__ == "__main__":
    main()
