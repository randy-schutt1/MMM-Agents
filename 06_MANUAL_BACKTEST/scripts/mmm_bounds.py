#!/usr/bin/env python3
"""The six printed boundaries of `PT-002` / `PT-025`, and the clustering machinery.

THE SIX BOUNDARIES ARE THE SLIDE'S SIX AND ONLY THE SLIDE'S SIX
--------------------------------------------------------------
V01 `[00:30:35]` prints a CLOSED list:

    Beginning Of The Week (Sun / Mon)   Beginning Of The Day
    Beginning Of The Session            End Of The Session
    End Of The Day                      End Of The Week

`PT-002` §1 records that this session's predecessor over-generalised the spoken
enumeration into "every session boundary" and that the slide REFUTED it (`G5`).
Both tests therefore pre-register the slide's six, and the placement rule is
`PT-002`/`PT-025` §3 verbatim:

    "placed from the V02 printed table. London and New York opens/closes are the
     'session' boundaries; the Asian open at 8:30pm is included as a session
     boundary"

and the V02 printed table (`COMMON_PROTOCOL.md` §4, slide at `[00:45:55]`) is:

    5pm            High / Low Reset
    5pm - 8pm      Dead Gap
    Asian Session  8:30pm - 3:00am     Gap 3:00-3:30
    London Session 3:30am - 9:00am     Gap 9:00-9:30
    New York       9:30am - 5pm

THE TRADING-WEEK COORDINATE
---------------------------
Everything here is expressed as MINUTES FROM THE WEEK OPEN (`mfwo`), where the week
open is Sunday 17:00 local and the trading week is 120 h = 7,200 minutes. This is the
coordinate both files' §3a demands the covered fraction be computed in:

    "The covered-fraction denominator is the 120-hour trading week, and the
     per-boundary expected shares are exposure-weighted, never per-weekday-uniform.
     Getting this wrong would manufacture a Sunday clustering result out of
     arithmetic."

THE OVERLAP IS REAL AND IS NOT SWEPT UP
---------------------------------------
17:00 is simultaneously a day close, a day open, a New York session close, and — on
Sunday and Friday — a week open or week close. Six categories x a +/-30 min band would
be 6 h of a 24 h day BEFORE overlaps are removed, which is why §3a requires the
OVERLAP-CORRECTED covered fraction be reported in the same table as the observed
share. `covered_fraction()` returns the union, computed against realised bars rather
than against nominal clock arithmetic, so a closure reduces the denominator honestly.
"""
from __future__ import annotations

import numpy as np

from mmm_week import week_anchor, DAY

WEEK_MINUTES = 5 * DAY                      # Sun 17:00 -> Fri 17:00 = 7,200
SESSION_DAYS = 5                            # session days 0..4 inside a trading week

# offsets WITHIN a session day, measured from that day's own 17:00 start
_ASIAN_OPEN = 3 * 60 + 30                   # 20:30  -> +210
_ASIAN_CLOSE = 10 * 60                      # 03:00  -> +600
_LONDON_OPEN = 10 * 60 + 30                 # 03:30  -> +630
_LONDON_CLOSE = 16 * 60                     # 09:00  -> +960
_NY_OPEN = 16 * 60 + 30                     # 09:30  -> +990
_NY_CLOSE = 24 * 60                         # 17:00  -> +1440


def _day_starts():
    return np.arange(SESSION_DAYS, dtype="int64") * DAY


def boundary_sets() -> dict[str, np.ndarray]:
    """The six categories, in minutes-from-week-open. Order is the slide's order."""
    d = _day_starts()
    return {
        "week_open": np.array([0], dtype="int64"),
        "day_open": d.copy(),                                   # each 17:00 that opens a day
        "session_open": np.concatenate([d + _ASIAN_OPEN,
                                        d + _LONDON_OPEN,
                                        d + _NY_OPEN]),
        "session_close": np.concatenate([d + _ASIAN_CLOSE,
                                         d + _LONDON_CLOSE,
                                         d + _NY_CLOSE]),
        "day_close": d + DAY,                                   # each 17:00 that closes a day
        "week_close": np.array([WEEK_MINUTES], dtype="int64"),
    }


def all_boundaries() -> np.ndarray:
    return np.unique(np.concatenate(list(boundary_sets().values())))


def mfwo(tm: np.ndarray) -> np.ndarray:
    """Minutes from the week open (Sunday 17:00) for raw-clock timestamps."""
    return np.asarray(tm, dtype="int64") - week_anchor(tm)


def min_distance(pos: np.ndarray, bounds: np.ndarray) -> np.ndarray:
    """Distance in minutes from each `mfwo` position to the nearest boundary instant.

    Linear, not circular: the bands used are <= 60 minutes and the week open and week
    close are both present as explicit instants (0 and 7,200), so the 48-hour weekend
    is never crossed by a band and no wrap term is needed.
    """
    pos = np.asarray(pos, dtype="int64")
    b = np.sort(np.asarray(bounds, dtype="int64"))
    i = np.searchsorted(b, pos)
    lo = b[np.clip(i - 1, 0, len(b) - 1)]
    hi = b[np.clip(i, 0, len(b) - 1)]
    return np.minimum(np.abs(pos - lo), np.abs(pos - hi))


def covered_fraction(bar_mfwo: np.ndarray, bounds: np.ndarray, band: int) -> float:
    """Overlap-corrected share of REALISED trading time inside any boundary band.

    `PT-002` §3a / `PT-025` §3a: "A clustering result is meaningless unless the
    expected share under the null is stated in the same table as the observed share.
    Report the overlap-corrected covered fraction of the trading week explicitly."

    Computed over realised bars, so a market closure removes its minutes from the
    denominator rather than being counted as uncovered trading time.
    """
    if len(bar_mfwo) == 0:
        return float("nan")
    return float((min_distance(bar_mfwo, bounds) <= band).mean())


def per_category_covered(bar_mfwo: np.ndarray, band: int) -> dict[str, float]:
    return {k: covered_fraction(bar_mfwo, v, band) for k, v in boundary_sets().items()}


def group_extremes(sd: np.ndarray, h: np.ndarray, l: np.ndarray):
    """Per-group argmax of `h` and argmin of `l`, vectorised.

    Returns (group_ids, idx_of_high, idx_of_low) as indices into the input arrays.
    `lexsort` puts each group's extreme last within its block, which is ~200x faster
    than a pandas groupby-apply and matters because the nulls call this 1,000 times.
    """
    order_h = np.lexsort((h, sd))
    order_l = np.lexsort((-l, sd))
    sd_h = sd[order_h]
    last = np.r_[sd_h[1:] != sd_h[:-1], True]
    return sd_h[last], order_h[last], order_l[last]
