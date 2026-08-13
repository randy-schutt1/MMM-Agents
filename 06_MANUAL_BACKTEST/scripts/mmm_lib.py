#!/usr/bin/env python3
"""Shared machinery for running the PT-002...PT-021 pre-registered batch against the
HistData GBP/USD M1 corpus (`D-036a`).

WHAT THIS FILE IS FOR
---------------------
Twelve pre-registered tests share one instrument, one corpus, one pip, two `D-031`
timezone arms, one seed, and one definition of the Asian box. Re-implementing any of
those twelve times is how twelve tests silently stop being the same test. Everything
common lives here; everything a `PT-NNN` file pre-registered for itself lives in that
test's own runner script.

MEASUREMENT RULE — `COMMON_PROTOCOL.md` §2 as restated by `D-036a`
-----------------------------------------------------------------
Every number this module produces is parsed from a checksummed CSV. Nothing is read
from a rendering of any kind. Re-running a runner against the files whose SHA-256 is
in `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` reproduces every figure exactly,
seed included.

HOLDOUT — `D-035`
-----------------
DEVELOPMENT is 2013-01-06 -> 2016-06-30; HOLDOUT is 2016-07-01 -> 2017-12-29 and is
never opened. The corpus on disk stops at 2016-06-30 (`D-036a` truncated it on
arrival) and `assert_development()` re-checks every window a runner asks for rather
than trusting that. Arm B shifts file stamps +1h during US DST, so the last four Arm-B
bars carry the wall-clock label 2016-07-01 while being the same M1 bars as Arm A's
last four (`I-010` Q2). No test in this batch reaches them: W-A and W-B end 2015-12-31.

TIME REPRESENTATION
-------------------
Canonical time is **int64 minutes since the Unix epoch**, not `datetime64`. pandas
silently re-casts `datetime64[m]` to a coarser-or-finer unit on column assignment,
which turned a 15-minute bucket key into a nanosecond count on the first draft of
this file and produced 1,297,781 "M15 bars". Integers cannot do that.
`verify_against_committed()` exists so the same class of error cannot survive again.

DECLARED MEASUREMENT CONVENTIONS
--------------------------------
Conventions, not pre-registrations. Declared once here so every artifact points at the
same words instead of each inventing its own:

  C-1  SESSION DAY. The V02 printed table runs 5pm -> 5pm. Session day `D` is the
       half-open interval [ D-1 17:00, D 17:00 ) in the arm's own clock.

  C-2  THE BOX. Asian window 20:30 -> 03:00, exactly as the V02 slide prints it. For
       session day `D`: [ D-1 20:30, D 03:00 ). Box high/low are the extreme high/low
       of the M15 bars inside it.

  C-3  THE POST-BOX DAY. 03:00 -> 17:00 of session day `D`. This end is NOT stated by
       PT-014/015/016/017/018; it is stated by `PT-021` §3 Measure 1 ("to the 17:00
       close") and by the printed table's own 5pm boundary, and it is applied
       identically across every box test in this batch so their results compose.
       Declared, not invented, and disclosed in every artifact that uses it.

  C-4  INTRABAR STOP/TARGET ORDER. Resolved on M1 bars, not M15 — the corpus makes the
       finer series free. Only when a SINGLE M1 bar contains both the stop level and
       the target level is an order assumed, and then it is STOP FIRST (adverse to the
       rule). Every artifact reports how often that tie occurred.

  C-5  INCLUSION. A session day enters a box test if its box window holds >= 1 M15 bar
       and its post-box window holds >= 1 M15 bar. NOTHING IS EXCLUDED for being
       unrepresentative — no holiday filter, no news filter, no volatility filter
       (`COMMON_PROTOCOL.md` §3 disclosure 1).

  C-6  COMPLETENESS (added 2026-08-13, on completeness grounds only, and the rule was
       fixed before its effect on any result was looked at). A session day is EXCLUDED
       if any 15-minute bucket of its box window or of its post-box window is absent
       from the corpus — i.e. `box_n < 26` (6.5 h) or `post_n < 56` (14 h). Exclusions
       are COUNTED AND REPORTED beside n, never dropped quietly: the honest form is
       "n = 512 (3 excluded for incomplete sessions)".

       WHY THE RULE IS SET AT THE M15 BUCKET AND NOT AT THE MINUTE. The tests read
       15-minute bars, so a fully-covered measured window means every 15-minute slot
       the test reads exists. Requiring 100% M1 coverage instead would exclude most of
       the corpus for a reason that is not a defect: a bid feed legitimately prints no
       tick in a quiet minute. Measured floor among full-bucket days in W-B is 363/390
       M1 in the box and 741/840 in the post-box window, with 1st percentiles of
       372/390 and 828/840 — i.e. ordinary thin minutes, not holes.

       THE SAME RULE IS APPLIED TO THE N2 NULL. A clock-shifted sham window that runs
       off the end of the week is not measurable either, and scoring the null by a
       looser standard than the rule arm would flatter whichever one it favoured.

       This rule is applied identically whether the incompleteness is a data defect or
       a real market closure. A half-covered Christmas Eve is a real closure AND cannot
       support a full-window measurement.

`D-031` ARMS
------------
  Arm A — fixed UTC-5 year-round -> file timestamps verbatim.
  Arm B — America/New_York, DST-aware -> file stamp +1h during US DST.
Both are always computed and both are always reported (`D-031`, binding).

BASELINES — `D-026` / `D-029` / `COMMON_PROTOCOL.md` §5
------------------------------------------------------
  N1  matched random entry: holds instrument, window, session, eligible hours, stop,
      target, direction and n; randomizes the entry bar. 1,000 iterations, seed
      20260812. A secondary random-direction arm is run alongside (`D-029`).
  N2  circular clock shift: holds the entire price path; shifts every session and
      boundary label by an offset drawn uniformly from +/-12h in 15-minute steps.

usage: imported by the run_ptNNN.py scripts in this directory.
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

# ---------------------------------------------------------------- constants

PIP = 0.0001                      # `D-036a` / `COMMON_PROTOCOL.md` §1
SEED = 20260812                   # `COMMON_PROTOCOL.md` §5 — batch constant
ITERATIONS = 1000                 # `D-029`
STOP_PIPS = 18.0                  # V04 [00:04:43]
TARGET_PIPS = 50.0                # V04 [00:05:07]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
DATA_DIR = os.path.join(ROOT, "06_MANUAL_BACKTEST", "datasets", "HISTDATA_GBPUSD_M1")
RAW_DIR = os.path.join(DATA_DIR, "raw")
CACHE_DIR = os.path.join(DATA_DIR, "_cache")     # inside the gitignored bulk dir

QA_REPORT = os.path.join(DATA_DIR, "QA_REPORT.txt")
SHA_FILE = os.path.join(RAW_DIR, "SHA256SUMS.txt")

NY = ZoneInfo("America/New_York")

MIN = 1
HOUR = 60
DAY = 1440


def dt2m(s: str) -> int:
    """'YYYY-MM-DD[ HH:MM]' -> int64 minutes since epoch."""
    return int(np.datetime64(s, "m").astype("int64"))


def m2s(m) -> str:
    return str(np.datetime64(int(m), "m"))


DEV_START = dt2m("2013-01-06")
DEV_END = dt2m("2016-06-30 23:59")          # `D-035`
HOLDOUT_START = dt2m("2016-07-01")

# The pre-registered windows this batch uses (`COMMON_PROTOCOL.md` §3)
WINDOWS = {
    "W-A": (dt2m("2015-01-04"), dt2m("2015-12-31 23:59")),
    "W-B": (dt2m("2014-01-05"), dt2m("2015-12-31 23:59")),
}

BOX_START_MIN = 20 * 60 + 30      # 20:30
BOX_END_MIN = 3 * 60              # 03:00
DAY_END_MIN = 17 * 60             # 17:00


# ---------------------------------------------------------------- QA gate

def qa_gate():
    """`COMMON_PROTOCOL.md` §1 makes the QA report a PRECONDITION on every run.

    Returns (report, sha256 manifest) so a runner can cite both. Raises if C1-C4 did
    not pass: a silent wrong number is the failure mode a CSV corpus has and a chart
    does not (`D-036a`).
    """
    with open(QA_REPORT) as fh:
        txt = fh.read()
    if "GATE: PASS" not in txt:
        raise SystemExit("QA gate did not PASS — refusing to run (`D-036a`)")
    with open(SHA_FILE) as fh:
        sha = fh.read()
    return txt, sha


# ---------------------------------------------------------------- DST arms

def _dst_intervals():
    """UTC instants of the US DST transitions covering the corpus, in epoch minutes.

    Computed from `zoneinfo` rather than hard-coded, so a tzdata change is visible
    instead of silently wrong.
    """
    out = []
    for year in range(2012, 2018):
        start = end = None
        prev = None
        t = datetime(year, 1, 1, tzinfo=timezone.utc)
        while t.year == year:
            off = t.astimezone(NY).utcoffset()
            if prev is not None and off != prev:
                if off == timedelta(hours=-4):
                    start = t
                else:
                    end = t
            prev = off
            t += timedelta(hours=1)
        if start and end:
            out.append((dt2m(start.replace(tzinfo=None).strftime("%Y-%m-%d %H:%M")),
                        dt2m(end.replace(tzinfo=None).strftime("%Y-%m-%d %H:%M"))))
    return out


_DST = _dst_intervals()


def shift_to_arm(tm: np.ndarray, arm: str) -> np.ndarray:
    """Map raw file timestamps (fixed UTC-5, epoch minutes) onto a `D-031` arm's clock.

    Arm A: verbatim. Arm B: +1h while US DST is in force. Derivation is `D-036a`'s —
    a file stamp T denotes UTC = T+5h; New York under DST is UTC-4, so local = T+1h.
    """
    if arm == "A":
        return tm
    utc = tm + 5 * HOUR
    dst = np.zeros(utc.shape, dtype=bool)
    for s, e in _DST:
        dst |= (utc >= s) & (utc < e)
    return tm + np.where(dst, 60, 0).astype("int64")


# ---------------------------------------------------------------- loading

def _load_raw_m1():
    """Parse the four checksummed raw CSVs once; cache the parse, never the results."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache = os.path.join(CACHE_DIR, "m1_raw_v2.npz")
    if os.path.exists(cache):
        z = np.load(cache, allow_pickle=False)
        return z["tm"], z["o"], z["h"], z["l"], z["c"]
    tms, os_, hs, ls, cs = [], [], [], [], []
    for name in sorted(os.listdir(RAW_DIR)):
        if not name.startswith("DAT_MT_GBPUSD_M1_") or not name.endswith(".csv"):
            continue
        df = pd.read_csv(
            os.path.join(RAW_DIR, name), header=None,
            names=["d", "t", "o", "h", "l", "c", "v"],
            dtype={"d": str, "t": str, "o": np.float64, "h": np.float64,
                   "l": np.float64, "c": np.float64, "v": np.float64},
        )
        # Volume is structurally zero in this vendor's data and NO TEST MAY READ IT
        # (`D-036a`). Dropped here so it cannot be reached by accident.
        ts = pd.to_datetime(df["d"] + " " + df["t"], format="%Y.%m.%d %H:%M")
        tms.append(ts.values.astype("datetime64[m]").astype("int64"))
        os_.append(df["o"].values); hs.append(df["h"].values)
        ls.append(df["l"].values); cs.append(df["c"].values)
    tm = np.concatenate(tms)
    o = np.concatenate(os_); h = np.concatenate(hs)
    l = np.concatenate(ls); c = np.concatenate(cs)
    k = np.argsort(tm, kind="stable")
    tm, o, h, l, c = tm[k], o[k], h[k], l[k], c[k]
    np.savez(cache, tm=tm, o=o, h=h, l=l, c=c)
    return tm, o, h, l, c


class Bars:
    """A bar series on one `D-031` arm. `tm` is int64 epoch minutes."""

    __slots__ = ("tm", "o", "h", "l", "c", "arm", "tf")

    def __init__(self, tm, o, h, l, c, arm, tf):
        self.tm, self.o, self.h, self.l, self.c = tm, o, h, l, c
        self.arm, self.tf = arm, tf

    def __len__(self):
        return len(self.tm)

    def slice(self, lo, hi):
        m = (self.tm >= lo) & (self.tm <= hi)
        return Bars(self.tm[m], self.o[m], self.h[m], self.l[m], self.c[m],
                    self.arm, self.tf)

    @property
    def sd(self):
        return session_day(self.tm)

    @property
    def mod(self):
        return minute_of_day(self.tm)

    @property
    def tr_pips(self):
        return (self.h - self.l) / PIP


def load_m1(arm: str) -> Bars:
    tm, o, h, l, c = _load_raw_m1()
    tm2 = shift_to_arm(tm, arm)
    k = np.argsort(tm2, kind="stable")
    return Bars(tm2[k], o[k], h[k], l[k], c[k], arm, 1)


def resample(b: Bars, minutes: int) -> Bars:
    """Floor to `minutes`, anchored on midnight of the bar's own day.

    A bucket is emitted only if at least one M1 bar falls inside it, so holidays and
    the weekend stay absent rather than becoming flat synthetic candles — identical
    behaviour to the committed `aggregate_m15.py`.
    """
    day = (b.tm // DAY) * DAY
    key = day + ((b.tm - day) // minutes) * minutes
    df = pd.DataFrame({"key": key, "o": b.o, "h": b.h, "l": b.l, "c": b.c})
    g = df.groupby("key", sort=True).agg(o=("o", "first"), h=("h", "max"),
                                         l=("l", "min"), c=("c", "last"))
    return Bars(g.index.values.astype("int64"), g["o"].values, g["h"].values,
                g["l"].values, g["c"].values, b.arm, minutes)


def load_m15(arm: str) -> Bars:
    return resample(load_m1(arm), 15)


def verify_against_committed(arm: str):
    """Re-derive M15 and diff it against the committed `aggregate_m15.py` output.

    The check that keeps the batch honest about its own tooling: if this module's
    bucketing ever drifts from the committed aggregator, every result downstream is
    quietly measuring something else.
    """
    path = os.path.join(DATA_DIR, f"GBPUSD_M15_ARM{arm}.csv")
    ref = pd.read_csv(path, header=None, names=["d", "t", "o", "h", "l", "c", "v"])
    ref_tm = (pd.to_datetime(ref["d"] + " " + ref["t"], format="%Y.%m.%d %H:%M")
              .values.astype("datetime64[m]").astype("int64"))
    mine = load_m15(arm)
    if len(ref_tm) != len(mine):
        return False, len(ref_tm), len(mine), "row count"
    ts_ok = bool((ref_tm == mine.tm).all())
    px_ok = bool(np.allclose(ref[["o", "h", "l", "c"]].values,
                             np.column_stack([mine.o, mine.h, mine.l, mine.c]),
                             atol=1e-9))
    return (ts_ok and px_ok), len(ref_tm), len(mine), f"ts={ts_ok} px={px_ok}"


# ---------------------------------------------------------------- calendar

def session_day(tm: np.ndarray) -> np.ndarray:
    """Convention C-1: session day D = [ D-1 17:00, D 17:00 ). Returns day index."""
    day = tm // DAY
    minute = tm - day * DAY
    return day + (minute >= DAY_END_MIN).astype("int64")


def minute_of_day(tm: np.ndarray) -> np.ndarray:
    return tm - (tm // DAY) * DAY


def day2s(d) -> str:
    return str(np.datetime64(int(d), "D"))


def assert_development(tm: np.ndarray, label: str = ""):
    """`D-035`. Refuse to proceed if a single timestamp reaches the holdout."""
    if len(tm) == 0:
        return
    mx = int(np.max(tm))
    if mx >= HOLDOUT_START:
        raise SystemExit(
            f"HOLDOUT BREACH ({label}): max timestamp {m2s(mx)} >= "
            f"{m2s(HOLDOUT_START)}. Stopping, per `D-035` / `E23`."
        )


def window(b: Bars, name: str) -> Bars:
    lo, hi = WINDOWS[name]
    out = b.slice(lo, hi)
    assert_development(out.tm, f"{name} / arm {b.arm}")
    return out


# ---------------------------------------------------------------- the box

BOX_BUCKETS = 26      # 20:30 -> 03:00 is 6.5 h = 26 fifteen-minute buckets
POST_BUCKETS = 56     # 03:00 -> 17:00 is 14 h  = 56 fifteen-minute buckets


def build_days(m15: Bars, offset_min: int = 0, require_full: bool = True) -> pd.DataFrame:
    """Per-session-day frame: the box (C-2), the post-box day (C-3), inclusion (C-5),
    completeness (C-6).

    `offset_min` implements the **N2 circular clock shift**: every session and boundary
    label moves by that many minutes while the price path is untouched. Implemented by
    shifting the bar stamps by -offset, which is identical and cheaper.

    `require_full` applies C-6. The returned frame carries the exclusion accounting in
    `.attrs` so a runner can report it beside n rather than losing it:
        attrs["n_before_completeness"]   days passing C-5
        attrs["n_excluded_incomplete"]   days C-6 removed
        attrs["excluded_days"]           their dates and bucket counts
    """
    tm = m15.tm - int(offset_min)
    sd = session_day(tm)
    mod = minute_of_day(tm)

    in_box = (mod >= BOX_START_MIN) | (mod < BOX_END_MIN)
    in_post = (mod >= BOX_END_MIN) & (mod < DAY_END_MIN)

    def agg(mask, name):
        d = pd.DataFrame({"sd": sd[mask], "h": m15.h[mask], "l": m15.l[mask],
                          "c": m15.c[mask], "o": m15.o[mask], "tm": tm[mask]})
        g = d.groupby("sd", sort=True)
        return pd.DataFrame({
            f"{name}_hi": g["h"].max(), f"{name}_lo": g["l"].min(),
            f"{name}_n": g["h"].size(), f"{name}_o": g["o"].first(),
            f"{name}_c": g["c"].last(),
        })

    days = agg(in_box, "box").join(agg(in_post, "post"), how="inner")
    days = days[(days["box_n"] >= 1) & (days["post_n"] >= 1)]      # C-5
    days = days.reset_index()

    n_before = int(len(days))
    excluded = []
    if require_full:                                               # C-6
        bad = (days["box_n"] < BOX_BUCKETS) | (days["post_n"] < POST_BUCKETS)
        for r in days[bad].itertuples():
            excluded.append(dict(day=day2s(r.sd), box_n=int(r.box_n),
                                 post_n=int(r.post_n)))
        days = days[~bad].reset_index(drop=True)

    days["box_range_pips"] = (days["box_hi"] - days["box_lo"]) / PIP
    days["post_range_pips"] = (days["post_hi"] - days["post_lo"]) / PIP
    days.attrs["n_before_completeness"] = n_before
    days.attrs["n_excluded_incomplete"] = n_before - int(len(days))
    days.attrs["excluded_days"] = excluded
    return days


def completeness_line(days: pd.DataFrame) -> str:
    """The honest form `n` must take when C-6 removed anything."""
    k = days.attrs.get("n_excluded_incomplete", 0)
    if not k:
        return (f"n = {len(days)} (0 excluded for incomplete sessions; every included "
                f"day has all {BOX_BUCKETS} box and all {POST_BUCKETS} post-box buckets)")
    who = ", ".join(f"{d['day']} (box {d['box_n']}/{BOX_BUCKETS}, "
                    f"post {d['post_n']}/{POST_BUCKETS})"
                    for d in days.attrs.get("excluded_days", []))
    return f"n = {len(days)} ({k} excluded for incomplete sessions: {who})"


def first_close_beyond(m15: Bars, days: pd.DataFrame, lo=10.0, hi=np.inf):
    """The batch's ONE implementation of "first 15m close N pips beyond a box edge".

    PT-015, PT-017, PT-018, PT-020 and PT-021 all trigger on some version of this
    sentence, with different bands. Writing it five times is how five tests silently
    stop sharing a trigger, so it is written once.

    Scans the post-box day (C-3) in time order and returns, per session day, the FIRST
    M15 close whose excursion beyond either box edge lies in [lo, hi]:

      exc   pips beyond the edge at that close (nan if the day never qualifies)
      side  +1 the close was above the box high, -1 below the box low
      mod   minute-of-day of that M15 bar (its stamp, so it indexes a TradeGrid)
      idx   index into `m15` of that bar

    Only bars strictly inside the post-box window are scanned, so nothing before 03:00
    and nothing at or after 17:00 can trigger. No later bar is consulted for anything —
    the decision point is that close, as every one of those pre-registrations requires.
    """
    sd, mod = m15.sd, m15.mod
    inpost = (mod >= BOX_END_MIN) & (mod < DAY_END_MIN)
    rows_by_day = {}
    for i in np.where(inpost)[0]:
        rows_by_day.setdefault(int(sd[i]), []).append(i)
    exc, side, when, where = [], [], [], []
    for row in days.itertuples():
        rows = rows_by_day.get(int(row.sd))
        if not rows:
            exc.append(np.nan); side.append(0); when.append(np.nan); where.append(-1)
            continue
        rows = np.asarray(rows)
        C = m15.c[rows]
        up = (C - row.box_hi) / PIP
        dn = (row.box_lo - C) / PIP
        e = np.maximum(up, dn)
        q = np.where((e >= lo) & (e <= hi))[0]
        if len(q) == 0:
            exc.append(np.nan); side.append(0); when.append(np.nan); where.append(-1)
            continue
        j = int(q[0])
        exc.append(float(e[j]))
        side.append(1 if up[j] >= dn[j] else -1)
        when.append(int(mod[rows[j]]))
        where.append(int(rows[j]))
    return (np.array(exc), np.array(side), np.array(when, dtype=float),
            np.array(where))


# ---------------------------------------------------------------- trade grid

class TradeGrid:
    """Outcome of a stop/target trade entered at the close of every M15 bar in the
    eligible window, both directions, resolved on M1 bars (convention C-4).

    Precomputing the whole grid once is what makes the `D-029` 1,000-iteration N1
    baseline cheap: an iteration becomes an array lookup, not 500 fresh simulations.
    It also guarantees the rule arm and the null arm are scored by *identical* code,
    which a separately-written control would not be.

    Direction index: 0 = long, 1 = short.
    """

    def __init__(self, m1: Bars, m15: Bars, stop_pips=STOP_PIPS,
                 target_pips=TARGET_PIPS, elig_from=BOX_END_MIN, elig_to=DAY_END_MIN,
                 checkpoints=(15, 30, 45, 60, 120), horizon_end=DAY_END_MIN):
        self.stop_pips, self.target_pips = stop_pips, target_pips
        self.checkpoints = tuple(checkpoints)

        m15_sd, m15_mod = m15.sd, m15.mod
        elig = (m15_mod >= elig_from) & (m15_mod < elig_to)
        e = np.where(elig)[0]

        self.entry_tm = m15.tm[e]
        self.entry_px = m15.c[e]
        self.entry_sd = m15_sd[e]
        self.entry_mod = m15_mod[e]
        n = len(e)

        shape = (n, 2)
        self.outcome = np.zeros(shape, dtype=np.int8)     # +1 target, -1 stop, 0 open
        self.exit_min = np.full(shape, np.nan)
        self.pnl_pips = np.full(shape, np.nan)
        self.mae_pips = np.full(shape, np.nan)
        self.mfe_pips = np.full(shape, np.nan)
        self.t_profit0 = np.full(shape, np.nan)
        self.t_profit10 = np.full(shape, np.nan)
        self.mae_before_profit = np.full(shape, np.nan)
        self.tie = np.zeros(shape, dtype=bool)
        self.ck_pnl = np.full((n, 2, len(self.checkpoints)), np.nan)
        self.valid = np.zeros(shape, dtype=bool)

        m1_sd = m1.sd
        order = np.argsort(m1_sd, kind="stable")
        sd_sorted = m1_sd[order]
        uniq, start = np.unique(sd_sorted, return_index=True)
        stop_ = np.append(start[1:], len(sd_sorted))
        day_rows = {int(u): np.sort(order[start[i]:stop_[i]])
                    for i, u in enumerate(uniq)}

        by_day = {}
        for i, sd in enumerate(self.entry_sd):
            by_day.setdefault(int(sd), []).append(i)

        for sd, rows in by_day.items():
            idx = day_rows.get(sd)
            if idx is None or len(idx) == 0:
                continue
            H, L, C, M = m1.h[idx], m1.l[idx], m1.c[idx], m1.tm[idx]
            rows = np.asarray(rows)
            e_moment = self.entry_tm[rows] + 15        # close of the M15 bar
            px = self.entry_px[rows]
            day_end = sd * DAY + horizon_end
            fwd = (M[None, :] >= e_moment[:, None]) & (M[None, :] < day_end)
            has = fwd.any(1)
            if not has.any():
                continue
            held = (M[None, :] - e_moment[:, None]).astype(np.float64)
            W = fwd.shape[1]
            pos = np.arange(W)[None, :]
            BIG = W + 10

            for d, sign in ((0, +1.0), (1, -1.0)):
                stop_lvl = px - sign * stop_pips * PIP
                tgt_lvl = px + sign * target_pips * PIP
                if sign > 0:
                    hit_s = (L[None, :] <= stop_lvl[:, None]) & fwd
                    hit_t = (H[None, :] >= tgt_lvl[:, None]) & fwd
                    fav = (H[None, :] - px[:, None]) / PIP
                    adv = (px[:, None] - L[None, :]) / PIP
                    mtm = (C[None, :] - px[:, None]) / PIP
                else:
                    hit_s = (H[None, :] >= stop_lvl[:, None]) & fwd
                    hit_t = (L[None, :] <= tgt_lvl[:, None]) & fwd
                    fav = (px[:, None] - L[None, :]) / PIP
                    adv = (H[None, :] - px[:, None]) / PIP
                    mtm = (px[:, None] - C[None, :]) / PIP

                f_s = np.where(hit_s.any(1), hit_s.argmax(1), BIG)
                f_t = np.where(hit_t.any(1), hit_t.argmax(1), BIG)
                self.tie[rows, d] = (f_s == f_t) & (f_s < BIG)
                stopped = f_s <= f_t                       # C-4: stop first on a tie
                res_at = np.minimum(f_s, f_t)
                resolved = res_at < BIG

                self.outcome[rows, d] = np.where(resolved,
                                                 np.where(stopped, -1, 1), 0).astype(np.int8)
                self.valid[rows, d] = has

                live = fwd & (pos <= np.where(resolved, res_at, W)[:, None])
                last_live = np.where(has, W - 1 - fwd[:, ::-1].argmax(1), 0)

                self.exit_min[rows, d] = np.where(
                    resolved,
                    np.take_along_axis(held, np.clip(res_at, 0, W - 1)[:, None], 1).ravel(),
                    np.nan)
                realised = np.where(stopped, -stop_pips, target_pips)
                mtm_end = np.take_along_axis(mtm, last_live[:, None], 1).ravel()
                self.pnl_pips[rows, d] = np.where(resolved, realised,
                                                  np.where(has, mtm_end, np.nan))

                self.mae_pips[rows, d] = np.max(np.where(live, adv, -np.inf), axis=1)
                self.mfe_pips[rows, d] = np.max(np.where(live, fav, -np.inf), axis=1)

                p0 = live & (fav > 0)
                p10 = live & (fav >= 10.0)
                f0 = np.where(p0.any(1), p0.argmax(1), -1)
                f10 = np.where(p10.any(1), p10.argmax(1), -1)
                self.t_profit0[rows, d] = np.where(
                    f0 >= 0, np.take_along_axis(held, np.clip(f0, 0, None)[:, None], 1).ravel(), np.nan)
                self.t_profit10[rows, d] = np.where(
                    f10 >= 0, np.take_along_axis(held, np.clip(f10, 0, None)[:, None], 1).ravel(), np.nan)

                before = live & (pos <= np.where(f0 >= 0, f0, W)[:, None])
                self.mae_before_profit[rows, d] = np.max(
                    np.where(before, adv, -np.inf), axis=1)

                # How far forward the day actually extends from each entry. A trade
                # triggered at 16:45 has 15 minutes of runway, so its "P&L at 120
                # minutes" DOES NOT EXIST and must be nan, not the last bar it saw.
                # Getting this wrong silently converts a censored observation into a
                # measured one, which is the quiet way a time-to-profit curve lies.
                horizon = np.max(np.where(fwd, held, -np.inf), axis=1)
                for k, ck in enumerate(self.checkpoints):
                    at = live & (held <= ck)
                    reach = horizon >= ck
                    last = np.where(at.any(1), W - 1 - at[:, ::-1].argmax(1), 0)
                    v = np.take_along_axis(mtm, last[:, None], 1).ravel()
                    # after a resolution the position no longer exists: carry the
                    # realised result forward — that is what "in profit at T" means
                    done = resolved & (np.nan_to_num(self.exit_min[rows, d], nan=1e9) <= ck)
                    v = np.where(done, self.pnl_pips[rows, d], v)
                    self.ck_pnl[rows, d, k] = np.where((reach & at.any(1)) | done,
                                                       v, np.nan)

        self.index = {}
        for i in range(n):
            self.index[(int(self.entry_sd[i]), int(self.entry_mod[i]))] = i

    def lookup(self, sd, minute):
        return self.index.get((int(sd), int(minute)))

    def lookup_many(self, sds, minutes):
        return np.array([self.index.get((int(a), int(b)), -1)
                         for a, b in zip(sds, minutes)])


# ---------------------------------------------------------------- baselines

def n1_matched_random(grid: TradeGrid, dirs, metric, pool=None,
                      iterations=ITERATIONS, seed=SEED, random_direction=False,
                      agg="mean"):
    """N1 — matched random entry (`D-026` required form, `D-029` parameters).

    Holds instrument, window, session, eligible hours, stop, target, direction and n;
    randomizes the entry bar. `dirs` is the rule population's direction vector so the
    control carries the same direction mix (`D-029` primary arm); `random_direction`
    gives the `D-029` secondary arm.
    """
    rng = np.random.default_rng(seed)
    dirs = np.asarray(dirs)
    n = len(dirs)
    if pool is None:
        pool = np.where(grid.valid.any(1))[0]
    arr = getattr(grid, metric)
    out = np.full(iterations, np.nan)
    for it in range(iterations):
        pick = rng.choice(pool, size=n, replace=True)
        d = rng.integers(0, 2, size=n) if random_direction else dirs
        v = arr[pick, d]
        v = v[np.isfinite(v)]
        if len(v) == 0:
            continue
        if agg == "mean":
            out[it] = v.mean()
        elif agg == "median":
            out[it] = np.median(v)
        elif agg == "hitrate":
            out[it] = float((v > 0).mean())
        else:
            raise ValueError(agg)
    return out


def n1_outcome(grid: TradeGrid, dirs, pool=None, iterations=ITERATIONS, seed=SEED,
               random_direction=False):
    """N1 reporting target-hit rate and expectancy together, per iteration."""
    rng = np.random.default_rng(seed)
    dirs = np.asarray(dirs)
    n = len(dirs)
    if pool is None:
        pool = np.where(grid.valid.any(1))[0]
    tgt = np.full(iterations, np.nan)
    exp = np.full(iterations, np.nan)
    for it in range(iterations):
        pick = rng.choice(pool, size=n, replace=True)
        d = rng.integers(0, 2, size=n) if random_direction else dirs
        oc = grid.outcome[pick, d]
        pl = grid.pnl_pips[pick, d]
        res = oc != 0
        if res.any():
            tgt[it] = float((oc[res] == 1).mean())
        if np.isfinite(pl).any():
            exp[it] = float(np.nanmean(pl))
    return tgt, exp


def n2_offsets(iterations=ITERATIONS, seed=SEED):
    """N2 — circular clock shift. Offsets drawn uniformly from +/-12h in 15-min steps."""
    rng = np.random.default_rng(seed)
    steps = np.arange(-48, 49)
    return (rng.choice(steps, size=iterations) * 15).astype("int64")


# ---------------------------------------------------------------- statistics

def wilson_ci(k: int, n: int, z: float = 1.959963985):
    """`BACKTEST_EVIDENCE_STANDARD.md` §4.2 — every rate carries an interval."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((c - h) / d, (c + h) / d)


def boot_ci(x, iterations=2000, seed=SEED, stat=np.median):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(iterations, len(x)))
    s = stat(x[idx], axis=1)
    return (float(np.percentile(s, 2.5)), float(np.percentile(s, 97.5)))


def percentile_of(value, dist) -> float:
    d = np.asarray(dist, dtype=float)
    d = d[np.isfinite(d)]
    if len(d) == 0 or not np.isfinite(value):
        return float("nan")
    return float((d < value).mean() * 100.0)


def dist_line(dist) -> str:
    d = np.asarray(dist, dtype=float)
    d = d[np.isfinite(d)]
    if len(d) == 0:
        return "n/a"
    return (f"median {np.median(d):.4g}, 5-95% [{np.percentile(d, 5):.4g}, "
            f"{np.percentile(d, 95):.4g}]")


def perm_diff(a, b, iterations=ITERATIONS, seed=SEED, stat=np.median):
    """Label-shuffling permutation test on a two-group difference of `stat`.

    Used where a pre-registration asks whether two populations differ and names no
    parametric test. No distributional assumption enters, and scipy is not installed.
    """
    a = np.asarray(a, float); a = a[np.isfinite(a)]
    b = np.asarray(b, float); b = b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return float("nan"), float("nan"), np.array([])
    obs = float(stat(a) - stat(b))
    pool = np.concatenate([a, b])
    na = len(a)
    rng = np.random.default_rng(seed)
    null = np.empty(iterations)
    for i in range(iterations):
        p = rng.permutation(pool)
        null[i] = stat(p[:na]) - stat(p[na:])
    return obs, float((np.abs(null) >= abs(obs)).mean()), null


def fmt_rate(k: int, n: int) -> str:
    if n == 0:
        return "n/a (n = 0)"
    lo, hi = wilson_ci(k, n)
    s = f"{k/n:.3f} ({k}/{n}), 95% CI [{lo:.3f}, {hi:.3f}]"
    if n < 30:
        s += "  <<< SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only"
    return s


def nlabel(n: int) -> str:
    return (f"n = {n} <<< SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only"
            if n < 30 else f"n = {n}")


def header(test_id: str, title: str, arm_note: str = "") -> str:
    qa, sha = qa_gate()
    lines = [
        "=" * 78,
        f"{test_id} — {title}",
        "=" * 78,
        "corpus   : HistData GBP/USD M1 (`D-036a`), SHA-256 manifest:",
    ]
    lines += ["           " + l for l in sha.strip().splitlines()]
    lines += [
        "QA gate  : " + [l for l in qa.splitlines() if l.startswith("GATE:")][0],
        f"seed     : {SEED}   iterations: {ITERATIONS}   pip: {PIP}",
        "holdout  : `D-035` 2016-07-01 -> never opened; assert_development() enforced",
        "levels   : NOT comparable with the V02-V06 FXCM homework (`D-036a`).",
        "           Only shape and distance claims travel.",
    ]
    if arm_note:
        lines.append(arm_note)
    lines.append("=" * 78)
    return "\n".join(lines)
