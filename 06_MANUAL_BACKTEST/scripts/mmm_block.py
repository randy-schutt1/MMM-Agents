#!/usr/bin/env python3
"""The week-opening block, shared by `PT-026` and `PT-027`.

`PT-027` §7 step 2: "Run `PT-026` first. This test consumes its block definition, and
running them in the other order would mean tuning the block against this test's
outcome." Writing the block twice is how two tests silently stop sharing it, so it is
written once, here, and both runners import it.

THE THREE BLOCK ARMS — `PT-026` §0c, and none of them is adopted as THE definition
---------------------------------------------------------------------------------
The instructor gives two phrasings in two lessons and they are the SAME span on
FXCM's 16:00 week open and DIFFERENT spans on this corpus's 17:00 one:

  headline   "the first eight hours"  — 8 h by clock from the REALISED week open.
             Chosen because it is what the slide prints, what both lessons say aloud,
             and the only reading that is the same length in both `D-031` arms.
  two-bars   "the first two 4-hour bars" — midnight-anchored buckets, per
             `aggregate_m15.py`. The week open at 17:00 falls inside the [16:00,20:00)
             bucket, so the first two buckets end at the NEXT MIDNIGHT: a realised
             7 h on Arm A and 6 h on Arm B during US DST.
  twelve     the 12-hour block, V03 `[00:29:51]` "Four, eight, twelve hours".

All three are reported every time. `D-030` forbids picking one and calling it the
definition, so the test measures both phrasings and adopts neither.

EVERYTHING IS VECTORISED ACROSS WEEKS
-------------------------------------
`PT-026` §4 runs N3 at 1,000 draws plus a 30-offset sweep plus a 4-width sweep, which
is ~200,000 week-blocks. Each measure below is computed with a scatter-reduce over the
whole bar array rather than a per-week Python loop, so the pre-registered baseline
counts are affordable and were not quietly reduced.
"""
from __future__ import annotations

import numpy as np

from mmm_lib import PIP, DAY, HOUR

BIG = np.iinfo("int64").max


def _grp_min(inv, vals, n, fill=BIG):
    out = np.full(n, fill, dtype=vals.dtype)
    np.minimum.at(out, inv, vals)
    return out


def _grp_max(inv, vals, n, fill=-BIG):
    out = np.full(n, fill, dtype=vals.dtype)
    np.maximum.at(out, inv, vals)
    return out


def week_index(anchors):
    uniq, inv = np.unique(anchors, return_inverse=True)
    return uniq, inv, len(uniq)


def block_measures(tm, h, l, c, inv, n, start_off=0, block_min=480,
                   outcome_cap_min=None):
    """`PT-026` Measures 1-4 for one block definition, across all weeks at once.

    `start_off` and `block_min` are measured from each week's REALISED open, in
    minutes -- "boundaries looked up from bar timestamps, never counted in bars", which
    is the V04 M1 defect the pre-registration names explicitly.

    Returns a dict of per-week arrays. A week whose block or outcome window holds no
    bars is marked not-measurable rather than being given a silent zero.
    """
    w_open = _grp_min(inv, tm, n)
    w_close = _grp_max(inv, tm, n, fill=-BIG)
    rel = tm - w_open[inv]

    # `block_min` may be a scalar (the 8h / 12h / sweep arms) OR a per-week array
    # (the "two bars" arm, whose realised span differs every week and between
    # `D-031` arms by construction — `PT-026` §0c). Both are broadcast per week here
    # so the two-bars arm is measured by the same code as the others rather than by
    # a parallel implementation that could drift from it.
    b0 = np.full(n, start_off, dtype="int64") if np.isscalar(start_off) \
        else np.asarray(start_off, dtype="int64")
    b1 = b0 + (np.full(n, block_min, dtype="int64") if np.isscalar(block_min)
               else np.asarray(block_min, dtype="int64"))
    in_block = (rel >= b0[inv]) & (rel < b1[inv])
    after = rel >= b1[inv]
    # `outcome_cap_min` truncates every week's outcome window to the SAME length.
    # Needed by PT-026's 30-offset sweep, where the uncapped window shrinks from
    # ~112 h at offset 0 to ~4 h at offset 108 — so an uncapped breach rate falls
    # with offset for a purely mechanical reason and would rank the week-open block
    # first no matter what the market did. See run_pt026.py's matched-basis sweep.
    if outcome_cap_min is not None:
        after &= rel < b1[inv] + int(outcome_cap_min)
        # a week with less than the full capped window left is NOT measurable on
        # this basis, and is dropped and counted rather than scored on a short one
        w_span = _grp_max(inv, rel, n, fill=-BIG)
        enough = w_span >= b1 + int(outcome_cap_min) - 15
    else:
        enough = np.ones(n, dtype=bool)

    nb = np.bincount(inv[in_block], minlength=n)
    na = np.bincount(inv[after], minlength=n)

    hi = _grp_max(inv[in_block], h[in_block], n, fill=-np.inf)
    lo = _grp_min(inv[in_block], l[in_block], n, fill=np.inf)

    # Measure 1 — is it cut? Max/min AFTER the block close decide it in one pass.
    a_hi = _grp_max(inv[after], h[after], n, fill=-np.inf)
    a_lo = _grp_min(inv[after], l[after], n, fill=np.inf)
    up = (a_hi > hi) & (nb > 0) & (na > 0)
    dn = (a_lo < lo) & (nb > 0) & (na > 0)

    # Measure 2 — when? First bar beyond each edge, in hours from the block close.
    bu = after & (h > hi[inv])
    bd = after & (l < lo[inv])
    t_up = _grp_min(inv[bu], tm[bu], n).astype(float)
    t_dn = _grp_min(inv[bd], tm[bd], n).astype(float)
    t_up[t_up == BIG] = np.nan
    t_dn[t_dn == BIG] = np.nan
    # A week whose block or outcome window holds no bars — a block running past its
    # own week close, or a sweep offset landing after it — is caught by `measurable`
    # below (nb > 0 and na > 0) and is excluded and counted, never given a zero.
    block_close = w_open + b1
    h_up = (t_up - block_close) / HOUR
    h_dn = (t_dn - block_close) / HOUR

    # Measure 3 — how far? Max excursion beyond each edge, in pips.
    exc_up = np.where(up, (a_hi - hi) / PIP, np.nan)
    exc_dn = np.where(dn, (lo - a_lo) / PIP, np.nan)

    # Measure 4 — which first, and does the week's extreme end up on that side?
    first_up = np.where(np.isnan(h_up), np.inf, h_up)
    first_dn = np.where(np.isnan(h_dn), np.inf, h_dn)
    first_side = np.where(np.isinf(first_up) & np.isinf(first_dn), 0,
                          np.where(first_up <= first_dn, 1, -1))
    wk_hi = _grp_max(inv, h, n, fill=-np.inf)
    wk_lo = _grp_min(inv, l, n, fill=np.inf)
    # which side the week's extreme sits on, relative to the block
    ext_side = np.where((wk_hi - hi) >= (lo - wk_lo), 1, -1)

    measurable = (nb > 0) & (na > 0) & enough
    return dict(
        w_open=w_open, w_close=w_close, block_hi=hi, block_lo=lo,
        block_n=nb, after_n=na, measurable=measurable,
        realised_block_h=np.where(nb > 0, nb * 0.25, np.nan),
        up=up, dn=dn, both=up & dn, neither=measurable & ~up & ~dn,
        h_up=h_up, h_dn=h_dn,
        t_first=np.nanmin(np.vstack([h_up, h_dn]), axis=0),
        exc_up=exc_up, exc_dn=exc_dn,
        first_side=first_side, ext_side=ext_side,
        agree=(first_side != 0) & (first_side == ext_side),
        outcome_h=(w_close - block_close) / HOUR,
    )


def two_bar_block_end(w_open):
    """End of the "first two 4-hour bars", midnight-anchored — `PT-026` §0c.

    The week open falls inside the [16:00, 20:00) bucket, so the second bucket is
    [20:00, 24:00) and the pair ends at the NEXT MIDNIGHT. Returned as an offset in
    minutes from the realised open, so it is a different length in each `D-031` arm
    BY CONSTRUCTION -- which is the whole point of §0c and is reported, not hidden.
    """
    nxt = (np.floor_divide(w_open, DAY) + 1) * DAY
    return (nxt - w_open).astype("int64")
