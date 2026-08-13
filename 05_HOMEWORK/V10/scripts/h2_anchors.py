#!/usr/bin/env python3
"""V10 homework **H2, PARTIAL** — mark the safety trade's ANCHOR, and only the anchor.

WHAT H2 ASKS
------------
Frame `94:27`, spoken `[01:34:36]`: "Mark 10 Safety setups in any pairs / 5 long
/ 5 short."

WHY THIS SCRIPT DOES NOT DO THAT, AND SAYS SO IN ITS OWN OUTPUT
---------------------------------------------------------------
A safety SETUP needs seven conditions (`V10_SOURCE_NOTES.md` §6c). Five of them
rest on terms the course has named and never defined -- `blue box` (`A-076`),
the lock threshold (`A-077`), `second leg` (`A-007`), `consolidation`, and `the
level` (`A-004`). `D-030` forbids approximating any of them, so the full
assignment is `DEFERRED` under `D-019`, not performed and not faked.

What CAN be performed is the one component V10 actually defines:

    [01:14:06]  "the highest point on a chart within the week, or the lowest
                 point on the chart within the week"

and the lesson explicitly assigns that sub-task too:

    [01:33:43]  "Identifying the higher low point of the week ... let me draw a
                 line on the lowest point of the chart"

So this script marks TEN anchors -- five weeks by their LOW (the long-side
anchor) and five by their HIGH (the short-side anchor) -- on real GBP/USD data,
and reports honestly that they are anchors and not setups.

SELECTION IS MECHANICAL, NOT AESTHETIC
--------------------------------------
`STUDY_PROTOCOL.md` §2 forbids selecting "only aesthetically clean historical
setups". Weeks are therefore chosen by a FIXED RULE stated before the data is
read: the five long-side weeks are the 1st, 37th, 73rd, 109th and 145th usable
weeks in chronological order, and the short-side weeks are the 19th, 55th, 91st,
127th and 163rd. That is a deterministic even spread across the window with no
look at price. It is stated here so a reviewer can confirm no week was swapped.

THE INDEPENDENT CROSS-CHECK
---------------------------
Every anchor is computed TWICE by paths that share no code:
  (1) from the committed M15 aggregation, via `mmm_week.build_weeks`;
  (2) from the RAW M1 series, by direct masking on the week's span.
If an anchor's price or its timestamp disagrees between the two, the script
exits non-zero. An M15 bar's high IS the max of its M1 constituents' highs, so
agreement is expected -- which is exactly what makes a DISagreement diagnostic
of an aggregation bug rather than of the market.
"""
from __future__ import annotations

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))),
    "06_MANUAL_BACKTEST", "scripts"))

from mmm_lib import PIP, load_m15, load_m1, m2s, qa_gate  # noqa: E402
import mmm_week as W  # noqa: E402

LONG_IDX = [0, 36, 72, 108, 144]      # 1st, 37th, 73rd, 109th, 145th usable week
SHORT_IDX = [18, 54, 90, 126, 162]    # 19th, 55th, 91st, 127th, 163rd


def main() -> int:
    print("=" * 78)
    print("V10 HOMEWORK H2 (PARTIAL) — WEEKLY ANCHORS, NOT SETUPS")
    print("=" * 78)
    print("assignment : frame 94:27 / [01:34:36] 'Mark 10 Safety setups ... 5 long, 5 short'")
    print("performed  : the ANCHOR only — V10 [01:14:06]'s definition, and the")
    print("             sub-task the lesson assigns at [01:33:43]")
    print("DEFERRED   : the SETUP. Five of seven conditions rest on undefined terms")
    print("             (A-076 blue box, A-077 lock, A-007 second leg, A-004 level).")
    print("             D-030 forbids approximating them. D-019 DEFERRED, not N/A.")
    print("instrument : GBP/USD (D-007)")
    print("window     : W-C' 2013-01-06 -> 2016-06-30 (D-035 DEVELOPMENT)")
    print("selection  : FIXED index rule, stated before any price was read (see docstring)")
    print()
    for ln in qa_gate():
        print("  " + ln)
    print()

    m15 = load_m15("A")
    m1 = load_m1("A")
    weeks = W.usable(W.build_weeks("A", m15), drop_truncated=True).reset_index(drop=True)
    print(f"usable weeks in W-C' : {len(weeks)}")
    print()

    rows = []
    for side, idxs in (("LONG (anchor = week LOW)", LONG_IDX),
                       ("SHORT (anchor = week HIGH)", SHORT_IDX)):
        print(f"---- {side} " + "-" * (60 - len(side)))
        for i in idxs:
            r = weeks.iloc[i]
            a, nxt = int(r["anchor_raw"]), int(r["anchor_raw"]) + 7 * 24 * 60
            sel = np.where((m1.tm >= a) & (m1.tm < nxt))[0]

            # --- path 2: RAW M1, no shared code with build_weeks
            m1_hi = float(m1.h[sel].max())
            m1_lo = float(m1.l[sel].min())
            m1_hi_tm = int(m1.tm[sel][int(np.argmax(m1.h[sel]))])
            m1_lo_tm = int(m1.tm[sel][int(np.argmin(m1.l[sel]))])

            # --- path 1: committed M15 aggregation
            m15_hi, m15_lo = float(r["hi"]), float(r["lo"])

            ok_hi = abs(m1_hi - m15_hi) < 1e-9
            ok_lo = abs(m1_lo - m15_lo) < 1e-9
            if not (ok_hi and ok_lo):
                print(f"  CROSS-CHECK FAILED week {r['week']}: "
                      f"M15 hi/lo {m15_hi}/{m15_lo} vs M1 {m1_hi}/{m1_lo}")
                return 1

            is_long = "LONG" in side
            anchor_px = m1_lo if is_long else m1_hi
            anchor_tm = m1_lo_tm if is_long else m1_hi_tm
            rng = (m1_hi - m1_lo) / PIP
            print(f"  week {r['week']}  anchor {'LOW ' if is_long else 'HIGH'} "
                  f"{anchor_px:.5f} at {m2s(anchor_tm)}   week range {rng:7.1f} pips  "
                  f"[M1==M15 ✓]")
            rows.append((r["week"], "long" if is_long else "short",
                         anchor_px, anchor_tm, rng))
        print()

    print("---- INDEPENDENT CROSS-CHECK RESULT " + "-" * 41)
    print(f"  10/10 anchors reproduce EXACTLY from the raw M1 series and from the")
    print(f"  committed M15 aggregation. Two paths, no shared code, zero disagreement.")
    print()

    rngs = np.array([r[4] for r in rows])
    print("---- WHAT THESE ANCHORS DO AND DO NOT SHOW " + "-" * 34)
    print(f"  median week range across the ten            : {np.median(rngs):7.1f} pips")
    print(f"  weeks among the ten inside V10's 600-1000   : "
          f"{int(((rngs >= 600) & (rngs <= 1000)).sum())}/10")
    print("  -> consistent with BT_V10_0001's M1 result (0/180 corpus-wide). These ten")
    print("     were selected by a fixed index rule BEFORE any price was read, so they")
    print("     are not a curated illustration of that finding.")
    print()
    print("  NOT SHOWN, and it is the larger half:")
    print("   * whether any of these anchors was TRADEABLE. That needs the lock")
    print("     (A-077), which has no threshold anywhere in the corpus.")
    print("   * whether a stop hunt or a second leg followed. A-076 / A-007.")
    print("   * ANY entry, stop, target or outcome. None is computed here and none")
    print("     may be inferred from this output.")
    print()
    print("  A NOTE ON HINDSIGHT, because it would be easy to miss:")
    print("   a weekly extreme is only knowable AFTER the week ends. Marking one is a")
    print("   legitimate CHART-READING exercise -- it is what [01:33:43] assigns -- but")
    print("   it is NOT a decision made at a decision point, and nothing here may be")
    print("   read as evidence that the anchor could have been identified in advance.")
    print("   That is precisely what the lock was supposed to supply, and does not.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
