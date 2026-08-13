#!/usr/bin/env python3
"""Week-scale machinery for the `D-035` re-issue batch — `PT-025` ... `PT-032`.

WHY THIS IS A SEPARATE FILE FROM `mmm_lib.py`
---------------------------------------------
`mmm_lib.py` is day-scale: session days, the Asian box, the post-box day, a trade
grid keyed on session day. Twelve tests are committed against it (`df7eab6`,
`9eb2d0c`) and every one of their numbers must stay reproducible bit-for-bit. This
module is a PURE ADDITION in a NEW FILE: it imports `mmm_lib` and changes nothing in
it, so no committed result can move.

THE ONE DEFINITION EVERY RE-ISSUE DEPENDS ON
--------------------------------------------
All eight re-issues pre-register the same week rule, in the same words:

    "a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open is
     never a week boundary."

and all eight forbid the obvious shortcut:

    "never from `C7`'s open list, which counts intra-week holiday re-opens as opens."

`C7`'s detector emits the first bar after any gap >= 12 h. Four mid-week holiday
re-opens — 2013-12-26 Thu, 2014-01-01 Wed, 2014-12-25 Thu, 2015-01-01 Thu — are
indistinguishable from week opens to that detector. Deriving boundaries from it would
split four weeks in two, and every test in the batch says so explicitly and says what
it would corrupt. `week_anchor()` below is therefore CALENDAR arithmetic on the
Sunday-17:00 instant, and the corpus is then consulted only for what it REALISED
inside that span.

ARM A / ARM B AND WHY THE WEEK SPANS ARE THE SAME PHYSICAL INSTANTS IN BOTH
--------------------------------------------------------------------------
`D-031` Arm A reads the corpus stamps verbatim (fixed UTC-5). Arm B adds 1h during US
DST. The week open is one physical instant — Sunday 22:00 UTC — and the arms disagree
only about what to CALL it: 17:00 local on Arm A year-round, 18:00 local on Arm B in
summer.

So week boundaries are computed ONCE on the raw clock and then relabelled per arm.
`PT-028` §3a is the check on this reading: it states that under Arm B "Sunday is 6
hours in DST weeks and 7 in standard-time weeks, and Friday is correspondingly
18/17" — which is true only if the boundary instant is shared and the label moves.
Recomputing a fresh Sunday-17:00 anchor in Arm B's own clock would instead slide the
week by an hour and make Sunday 7 hours in both arms, contradicting the
pre-registration.

THE WINDOW
----------
`W-C'` = 2013-01-06 -> 2016-06-30, which IS `D-035`'s DEVELOPMENT block. It cannot
straddle the boundary because it is the boundary. `mmm_lib.assert_development()` is
re-asserted on every slice anyway.

EXCLUSIONS ARE PRE-REGISTERED BY NAME AND ARE NEVER DECIDED HERE
----------------------------------------------------------------
This module SUPPLIES the roster and the flags. It does not decide dispositions — each
test's own pre-registration does, and they are NOT uniform:

  * the week of 2014-06-01 (the C8 data hole) is excluded by name by all eight;
  * PT-030 additionally excludes 2014-06-08, whose barrier is drawn from that week;
  * the six Dec/Jan closure weeks are INCLUDED and reported separately by all eight;
  * the truncated final week 2016-06-26 is excluded by some tests and, in PT-032,
    supplies a gap that IS retained.

`week_flags()` returns the facts; each runner applies its own file's table.

usage: imported by the run_ptNNN.py scripts in this directory.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from mmm_lib import (  # noqa: F401  (re-exported for the runners' convenience)
    DAY, HOUR, PIP, SEED, ITERATIONS,
    dt2m, m2s, day2s, load_m1, load_m15, resample, shift_to_arm,
    assert_development, qa_gate, wilson_ci, boot_ci, percentile_of, dist_line,
    fmt_rate, nlabel, header, Bars,
)

# ---------------------------------------------------------------- the window

WC_PRIME_START = dt2m("2013-01-06")            # first week open in W-C'
WC_PRIME_END = dt2m("2016-06-30 23:59")        # `D-035` DEVELOPMENT end

WEEK_OPEN_MIN = 17 * 60                        # Sunday 17:00 local, raw clock

# Pre-registered by name in every file of the batch. Named here as constants so a
# runner cannot typo one and silently include it.
DATA_HOLE_WEEK = "2014-06-01"                  # C8: Sun 0 bars, Mon 521/1440
DATA_HOLE_HEIR_WEEK = "2014-06-08"             # PT-030 only: its barrier week is holed
TRUNCATED_FINAL_WEEK = "2016-06-26"            # cut by the DEVELOPMENT boundary
CLOSURE_WEEKS = (                              # the six Dec/Jan market closures
    "2013-12-22", "2013-12-29", "2014-12-21",
    "2014-12-28", "2015-12-20", "2015-12-27",
)
# The four mid-week holiday RE-OPENS that C7 miscounts as week opens. Carried so a
# runner can assert they never appear in the roster.
HOLIDAY_REOPENS = ("2013-12-26", "2014-01-01", "2014-12-25", "2015-01-01")


# ---------------------------------------------------------------- week anchors

def week_anchor(tm_raw) -> np.ndarray:
    """The Sunday-17:00 instant at or before each raw timestamp, in epoch minutes.

    Calendar arithmetic, not gap detection — see the module docstring. Epoch day 0 is
    1970-01-01, a Thursday, so `(day + 3) % 7` puts Monday at 0 and Sunday at 6.
    """
    tm = np.asarray(tm_raw, dtype="int64")
    s = tm - WEEK_OPEN_MIN                     # slide Sunday 17:00 -> Sunday 00:00
    d = np.floor_divide(s, DAY)
    dow = (d + 3) % 7                          # Mon=0 ... Sun=6
    back = (dow - 6) % 7
    return (d - back) * DAY + WEEK_OPEN_MIN


def _weekday(tm) -> np.ndarray:
    """Mon=0 ... Sun=6 for a timestamp in whatever clock it is expressed in."""
    return (np.floor_divide(np.asarray(tm, dtype="int64"), DAY) + 3) % 7


WEEKDAY_NAMES = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


# ---------------------------------------------------------------- the roster

def build_weeks(arm: str, m15: Bars | None = None) -> pd.DataFrame:
    """The `W-C'` week roster for one `D-031` arm.

    Week SPANS are the same physical instants on both arms; only the labels move
    (module docstring). The frame is indexed by the week's Sunday date in the RAW
    clock, which is the stable key every pre-registration names its weeks by
    ("the week of 2014-06-01").

    Columns
    -------
    week           Sunday date of the week open, raw clock — the pre-registrations' key
    anchor_raw     nominal Sunday 17:00 instant, raw clock (epoch minutes)
    anchor         the same instant relabelled into this arm's clock
    open_tm        REALISED first M15 stamp at or after the anchor (arm clock)
    close_tm       REALISED last M15 stamp before the next anchor (arm clock)
    open_px        open of that first bar          close_px  close of that last bar
    hi, lo         the week's extremes             hi_tm, lo_tm  their stamps
    n_bars         M15 bars realised in the week
    open_lag_min   open_tm - anchor, in minutes — the C7 "late open" fact, measured
    span_h         realised open->close span in hours
    ends_weekday   weekday name of the realised close (Thu for the two closure weeks)
    is_closure     one of the six Dec/Jan closure weeks (INCLUDE, report separately)
    is_data_hole   the 2014-06-01 week (EXCLUDE by name, everywhere)
    is_truncated   the 2016-06-26 week, cut by the DEVELOPMENT boundary

    `.attrs` carries the census each pre-registration requires be reported.
    """
    if m15 is None:
        m15 = load_m15(arm)

    # Work in the raw clock for anchoring, then relabel. `shift_to_arm` is a pure
    # function of the raw stamp, so inverting it per-bar is unnecessary: recompute
    # the raw stamps once instead.
    raw = load_m15("A") if arm != "A" else m15
    assert len(raw) == len(m15), "arm aggregation changed the bar count"

    anchors_raw = week_anchor(raw.tm)

    # W-C' weeks: every distinct Sunday-17:00 anchor whose week open lies in window.
    uniq = np.unique(anchors_raw)
    uniq = uniq[(uniq >= WC_PRIME_START) & (uniq <= WC_PRIME_END)]

    rows = []
    for a in uniq:
        m = anchors_raw == a
        if not m.any():
            continue
        idx = np.where(m)[0]
        tm_arm = m15.tm[idx]
        h, l, o, c = m15.h[idx], m15.l[idx], m15.o[idx], m15.c[idx]
        assert_development(raw.tm[idx], f"week {day2s(a // DAY)} / arm {arm}")

        jh, jl = int(np.argmax(h)), int(np.argmin(l))
        j0, j1 = int(np.argmin(tm_arm)), int(np.argmax(tm_arm))
        anchor_arm = int(shift_to_arm(np.array([a], dtype="int64"), arm)[0])
        week = day2s(a // DAY)

        rows.append(dict(
            week=week,
            anchor_raw=int(a),
            anchor=anchor_arm,
            open_tm=int(tm_arm[j0]),
            close_tm=int(tm_arm[j1]),
            open_px=float(o[j0]),
            close_px=float(c[j1]),
            hi=float(h[jh]), lo=float(l[jl]),
            hi_tm=int(tm_arm[jh]), lo_tm=int(tm_arm[jl]),
            n_bars=int(len(idx)),
            open_lag_min=int(tm_arm[j0] - anchor_arm),
            span_h=float((tm_arm[j1] - tm_arm[j0]) / 60.0),
            ends_weekday=WEEKDAY_NAMES[int(_weekday(tm_arm[j1]))],
            is_closure=week in CLOSURE_WEEKS,
            is_data_hole=week == DATA_HOLE_WEEK,
            is_truncated=week == TRUNCATED_FINAL_WEEK,
        ))

    df = pd.DataFrame(rows)
    df["range_pips"] = (df["hi"] - df["lo"]) / PIP

    # The assertion the batch's §3b.1 exists to force: no holiday re-open may ever
    # have become a week boundary. If this fires, the roster was built by gap
    # detection somewhere and every downstream number is wrong.
    bad = sorted(set(df["week"]) & set(HOLIDAY_REOPENS))
    assert not bad, f"holiday re-open leaked into the week roster: {bad}"

    df.attrs["arm"] = arm
    df.attrs["n_anchors"] = int(len(df))
    df.attrs["n_closure"] = int(df["is_closure"].sum())
    df.attrs["n_data_hole"] = int(df["is_data_hole"].sum())
    df.attrs["n_truncated"] = int(df["is_truncated"].sum())
    return df


def census_lines(df: pd.DataFrame) -> list[str]:
    """The week census every re-issue requires be printed before any result."""
    late = df[df["open_lag_min"] > 0]
    thu = df[df["ends_weekday"] == "Thu"]
    return [
        f"week roster (arm {df.attrs['arm']}) — derived from the Sunday 17:00 anchor,",
        "  NOT from C7's open list (which counts 4 holiday re-opens as opens)",
        f"  Sunday week anchors in W-C'            : {df.attrs['n_anchors']}",
        f"  of which Dec/Jan closure weeks         : {df.attrs['n_closure']}"
        f"  (INCLUDE, report separately)",
        f"  of which the 2014-06-01 data hole      : {df.attrs['n_data_hole']}"
        f"  (EXCLUDE by name)",
        f"  of which truncated by the DEV boundary : {df.attrs['n_truncated']}"
        f"  ({TRUNCATED_FINAL_WEEK})",
        f"  weeks whose realised open is late      : {len(late)}"
        f"  (max lag {int(late['open_lag_min'].max()) if len(late) else 0} min)",
        f"  weeks whose realised close is a Thu    : {len(thu)}"
        f"  ({', '.join(thu['week']) if len(thu) else 'none'})",
        "  holiday re-opens asserted absent from the roster: "
        + ", ".join(HOLIDAY_REOPENS),
    ]


def usable(df: pd.DataFrame, drop_truncated: bool = True,
           drop_heir: bool = False) -> pd.DataFrame:
    """Apply the exclusions that are common to the batch, per each file's table.

    `drop_truncated` — the 2016-06-26 week is cut by the DEVELOPMENT boundary. Most
    tests exclude it (no Friday, no remaining week, survival censored for a
    non-market reason). `PT-032` keeps the GAP INTO it while excluding it as a week,
    which that runner handles itself.

    `drop_heir` — `PT-030` only: 2014-06-08's barrier is the holed week's extremes.
    """
    keep = ~df["is_data_hole"]
    if drop_truncated:
        keep &= ~df["is_truncated"]
    if drop_heir:
        keep &= df["week"] != DATA_HOLE_HEIR_WEEK
    out = df[keep].reset_index(drop=True)
    out.attrs.update(df.attrs)
    out.attrs["excluded_data_hole"] = [DATA_HOLE_WEEK]
    out.attrs["excluded_truncated"] = [TRUNCATED_FINAL_WEEK] if drop_truncated else []
    out.attrs["excluded_heir"] = [DATA_HOLE_HEIR_WEEK] if drop_heir else []
    return out


# ---------------------------------------------------------------- exposure

def week_exposure_hours(df: pd.DataFrame, m15: Bars) -> pd.DataFrame:
    """Per-week, per-weekday REALISED exposure in hours, in the arm's own clock.

    `PT-028` §3a and `PT-025` §3a both require the null be exposure-weighted by the
    hours actually present in each week, never per-weekday-uniform: the trading week
    is 120 hours and is not five equal days (Sunday 7 h, Mon-Thu 24 h, Friday 17 h),
    and a closed Wednesday contributes zero Wednesday exposure.

    Computed from realised bars — one M15 bar = 0.25 h — so a closure and a data hole
    both reduce exposure honestly, which is why the data-hole week must be excluded
    BEFORE this is used as a denominator (`PT-028` §3c).
    """
    raw = load_m15("A")
    anchors = week_anchor(raw.tm)
    key = {int(a): i for i, a in enumerate(df["anchor_raw"])}
    out = np.zeros((len(df), 7), dtype=float)
    dow = _weekday(m15.tm)
    for i in range(len(m15.tm)):
        r = key.get(int(anchors[i]))
        if r is not None:
            out[r, dow[i]] += 0.25
    e = pd.DataFrame(out, columns=list(WEEKDAY_NAMES))
    e.insert(0, "week", df["week"].values)
    e["total_h"] = e[list(WEEKDAY_NAMES)].sum(axis=1)
    return e


# ---------------------------------------------------------------- N3

def n3_week_shifts(iterations: int = ITERATIONS, seed: int = SEED) -> np.ndarray:
    """N3 — week-anchor shift (`COMMON_PROTOCOL.md` §5).

    "the week boundary: shifted by `k` days, `k` drawn uniformly from 1...4, plus a
    random 15-minute intraday offset." Returned in minutes, ready to subtract from
    bar stamps the way `mmm_lib.build_days` implements N2's circular shift.
    """
    rng = np.random.default_rng(seed)
    k = rng.integers(1, 5, size=iterations)                 # 1..4 days
    intraday = rng.integers(0, 96, size=iterations) * 15    # 0..23:45
    return (k * DAY + intraday).astype("int64")


def weeks_from_offset(m15: Bars, offset_min: int) -> pd.DataFrame:
    """A sham week roster with the anchor moved by `offset_min` — the N3 null.

    The price path is untouched; only the boundary labels move. Returns the minimum a
    null needs: extremes, open/close and range per sham week. Sham weeks that run off
    either end of the corpus are dropped, because a partially-covered sham week is not
    measurable either and scoring the null by a looser standard than the rule arm
    would flatter whichever it favoured (`mmm_lib` C-6's rationale, at week scale).
    """
    raw = load_m15("A")
    a = week_anchor(raw.tm - int(offset_min)) + int(offset_min)
    uniq, inv = np.unique(a, return_inverse=True)
    n = len(uniq)
    hi = np.full(n, -np.inf); lo = np.full(n, np.inf)
    np.maximum.at(hi, inv, m15.h)
    np.minimum.at(lo, inv, m15.l)
    first = np.full(n, np.iinfo("int64").max, dtype="int64")
    last = np.full(n, np.iinfo("int64").min, dtype="int64")
    np.minimum.at(first, inv, m15.tm)
    np.maximum.at(last, inv, m15.tm)
    cnt = np.bincount(inv, minlength=n)
    df = pd.DataFrame(dict(anchor=uniq, hi=hi, lo=lo, first_tm=first,
                           last_tm=last, n_bars=cnt))
    # drop the two partial sham weeks at the corpus edges
    df = df[(df["anchor"] >= raw.tm.min()) & (df["anchor"] <= raw.tm.max() - 5 * DAY)]
    df["range_pips"] = (df["hi"] - df["lo"]) / PIP
    return df.reset_index(drop=True)


def largest_range_weeks(df: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    """The pre-registered sensitivity appendix — `COMMON_PROTOCOL.md` §3 disclosure 1.

    An APPENDIX, never a headline, and NEVER a filtered re-run. Every re-issue
    requires the five largest-range weeks be listed with their contribution; the EU
    referendum week (2016-06-20) is disclosed in advance as expected to appear.
    """
    return df.nlargest(k, "range_pips")[["week", "range_pips", "hi", "lo",
                                         "ends_weekday", "is_closure"]]
