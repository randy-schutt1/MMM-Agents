#!/usr/bin/env python3
"""Week-horizon stop/target resolution, for `PT-027` Outcome 3.

WHY NOT `mmm_lib.TradeGrid`
--------------------------
That grid resolves every trade against a DAY horizon (`horizon_end=DAY_END_MIN`) and
keys its index on the session day, because the twelve day-scale tests need exactly
that. `PT-027` Outcome 3 holds a position from the first breach of the week's opening
block until the WEEK closes. Reusing the day grid would silently truncate every trade
at 17:00 and quietly convert a week-long hold into a few hours.

WHAT IS PRESERVED FROM IT
-------------------------
Every convention, so the two are comparable:

  C-4  INTRABAR STOP/TARGET ORDER. Resolved on M1 bars, not M15. Only when a SINGLE
       M1 bar contains both levels is an order assumed, and it is STOP FIRST, adverse
       to the rule. The tie count is returned and must be reported.
  stop / target  18 and 50 pips — V04 `[00:04:43]`, `[00:05:07]`, the instructor's own
       numbers, not fitted.
  Entry is at the CLOSE of the triggering M15 bar, so the trade begins at that bar's
       end (`tm + 15`) and no part of the triggering bar is traded through.

`PT-027` §0c — WHAT THIS CANNOT PRICE
-------------------------------------
The corpus is bid-only with structurally zero volume. There is NO SPREAD in the data,
so every figure this module produces is an UPPER BOUND on what the trade would have
returned. V04's own stop language elsewhere is "7 pips plus spread"; the "plus spread"
half cannot be honoured by this corpus and inventing one would be `D-030`'s exact
prohibition. Every caller must label the result an upper bound.
"""
from __future__ import annotations

import numpy as np

from mmm_lib import PIP, STOP_PIPS, TARGET_PIPS


def resolve_week(m1_tm, m1_h, m1_l, m1_c, entry_tm, entry_px, week_end,
                 stop_pips=STOP_PIPS, target_pips=TARGET_PIPS):
    """Resolve stop/target trades held to `week_end`, both directions.

    All arrays are for ONE week. `entry_tm` are M15 bar stamps; the position opens at
    that bar's close, i.e. `entry_tm + 15`.

    Returns arrays indexed [entry, direction] with 0 = long, 1 = short:
      outcome  +1 target, -1 stop, 0 still open at the week close
      pnl      realised pips, or mark-to-market at the week close if unresolved
      hours    hours held to resolution (nan if unresolved)
      tie      the C-4 same-bar tie occurred
    """
    n = len(entry_tm)
    out = np.zeros((n, 2), dtype=np.int8)
    pnl = np.full((n, 2), np.nan)
    hrs = np.full((n, 2), np.nan)
    tie = np.zeros((n, 2), dtype=bool)
    if n == 0 or len(m1_tm) == 0:
        return out, pnl, hrs, tie

    start = entry_tm + 15
    fwd = (m1_tm[None, :] >= start[:, None]) & (m1_tm[None, :] <= week_end)
    W = fwd.shape[1]
    BIG = W + 10
    held = (m1_tm[None, :] - start[:, None]).astype(np.float64)
    has = fwd.any(1)

    for d, sign in ((0, +1.0), (1, -1.0)):
        stop_lvl = entry_px - sign * stop_pips * PIP
        tgt_lvl = entry_px + sign * target_pips * PIP
        if sign > 0:
            hit_s = (m1_l[None, :] <= stop_lvl[:, None]) & fwd
            hit_t = (m1_h[None, :] >= tgt_lvl[:, None]) & fwd
            mtm = (m1_c[None, :] - entry_px[:, None]) / PIP
        else:
            hit_s = (m1_h[None, :] >= stop_lvl[:, None]) & fwd
            hit_t = (m1_l[None, :] <= tgt_lvl[:, None]) & fwd
            mtm = (entry_px[:, None] - m1_c[None, :]) / PIP

        f_s = np.where(hit_s.any(1), hit_s.argmax(1), BIG)
        f_t = np.where(hit_t.any(1), hit_t.argmax(1), BIG)
        tie[:, d] = (f_s == f_t) & (f_s < BIG)
        stopped = f_s <= f_t                      # C-4: stop first on a tie
        at = np.minimum(f_s, f_t)
        resolved = at < BIG

        out[:, d] = np.where(resolved, np.where(stopped, -1, 1), 0).astype(np.int8)
        hrs[:, d] = np.where(
            resolved,
            np.take_along_axis(held, np.clip(at, 0, W - 1)[:, None], 1).ravel() / 60.0,
            np.nan)
        last = np.where(has, W - 1 - fwd[:, ::-1].argmax(1), 0)
        mtm_end = np.take_along_axis(mtm, last[:, None], 1).ravel()
        pnl[:, d] = np.where(resolved,
                             np.where(stopped, -stop_pips, target_pips),
                             np.where(has, mtm_end, np.nan))
    return out, pnl, hrs, tie
