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

HOLDOUT — `D-035`, AS AMENDED IN ITS USE BY `D-044`
---------------------------------------------------
DEVELOPMENT is 2013-01-06 -> 2016-06-30. `D-035`'s HOLDOUT was 2016-07-01 -> 2017-12-29;
`D-044` records the owner releasing **2017-01-01 -> 2017-12-29** of it for forward-testing
and backtesting, and leaves **2016-07-01 -> 2016-12-31 sealed and not on disk**.

THE CORPUS ON DISK NO LONGER STOPS AT THE BOUNDARY, and that is the one sentence in this
file most likely to be read from memory rather than from the code. `D-036a` truncated 2016
on arrival, so for a while "everything in `raw/`" and "DEVELOPMENT" were the same set and
ten runners quietly depended on it. `D-044` added 2017-2025. What protects the boundary now
is not the directory: it is `SCOPES` + the DEVELOPMENT default on `load_m1()`/`load_m15()`,
with `assert_development()` re-checking every window a runner asks for.

Arm B shifts file stamps +1h during US DST, so the last four Arm-B development bars carry
the wall-clock label 2016-07-01 while being the same M1 bars as Arm A's last four
(`I-010` Q2, STILL AN OPEN OWNER CALL — `load_m1()` clips on the raw clock precisely so
that this entry does not move it). No test in this batch reaches them: W-A and W-B end
2015-12-31.

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

import collections
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

QA_REPORT = os.path.join(DATA_DIR, "QA_REPORT.txt")          # `D-035` DEVELOPMENT
QA_REPORT_EXT = os.path.join(DATA_DIR, "QA_REPORT_EXT.txt")  # `D-044`, post-dedupe
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

# ---------------------------------------------------------------- corpus scope
#
# `D-044` EXTENDED THE CORPUS ON DISK to 2017-01-01 -> 2025-12-31, and that broke an
# assumption every runner in this directory silently relied on: that "load the corpus"
# and "load DEVELOPMENT" were the same act, because the only thing on disk WAS
# DEVELOPMENT (`D-036a` truncated 2016 on arrival). Ten scripts — `PT-025`...`PT-032`,
# `PT-036`, `PT-039` — derive their bar universe from the whole corpus and then call
# `assert_development()` on it. Left alone they would have raised HOLDOUT BREACH on the
# first run after the extension: loud, correct, and useless.
#
# So the coupling is made explicit instead of accidental. `load_m1()` and `load_m15()`
# take a SCOPE and DEFAULT TO DEVELOPMENT, which is exactly what every existing runner
# was already getting. Reaching the `D-044` years requires naming them.
#
# THIS IS NOT A REDEFINITION OF "DEVELOPMENT". `SCOPES["development"]` is `D-035`'s
# block, unchanged to the minute, and `assert_development()` is untouched. What changed
# is that a runner now gets it because it asked, not because the vendor's other years
# happened to be missing from a directory.

SCOPES = {
    # `D-035` DEVELOPMENT — the default, and the only scope any pre-`D-044` runner sees.
    "development": (None, DEV_END),
    # `D-044` — the extension the owner released for forward-testing and backtesting.
    # 2016-07-01 -> 2016-12-31 is NOT here: it is still sealed and is not on disk.
    "extended": (None, dt2m("2025-12-31 23:59")),
}
DEFAULT_SCOPE = "development"

# `D-044`: the years whose files are on disk. `_dst_intervals()` reads this rather than
# a literal, so extending the corpus again cannot leave Arm B's DST table short.
CORPUS_YEAR_MIN = 2013
CORPUS_YEAR_MAX = 2025

# The pre-registered windows this batch uses (`COMMON_PROTOCOL.md` §3)
WINDOWS = {
    "W-A": (dt2m("2015-01-04"), dt2m("2015-12-31 23:59")),
    "W-B": (dt2m("2014-01-05"), dt2m("2015-12-31 23:59")),
}

BOX_START_MIN = 20 * 60 + 30      # 20:30
BOX_END_MIN = 3 * 60              # 03:00
DAY_END_MIN = 17 * 60             # 17:00


# ---------------------------------------------------------------- QA gate

def qa_gate(scope: str = DEFAULT_SCOPE):
    """`COMMON_PROTOCOL.md` §1 makes the QA report a PRECONDITION on every run.

    Returns (report, sha256 manifest) so a runner can cite both. Raises if C1-C4 did
    not pass: a silent wrong number is the failure mode a CSV corpus has and a chart
    does not (`D-036a`).

    THE PRECONDITION IS PER-SCOPE, because after `D-044` the corpus has two of them and
    they do not pass or fail together. `QA_REPORT.txt` gates `D-035` DEVELOPMENT and is
    unchanged. `QA_REPORT_EXT.txt` gates the `D-044` years as the project consumes them
    — i.e. after the exact-duplicate removal that `_dedupe_exact()` applies at load.
    `QA_REPORT_EXT_RAW.txt` is committed beside it and DOES NOT PASS; it is the record
    of what the vendor actually served and is deliberately not the gate, because gating
    on it would block a corpus whose only defect is 420 rows the vendor sent twice.
    """
    path = QA_REPORT if scope == "development" else QA_REPORT_EXT
    with open(path) as fh:
        txt = fh.read()
    if "GATE: PASS" not in txt:
        raise SystemExit(
            f"QA gate did not PASS for scope {scope!r} ({os.path.basename(path)}) — "
            "refusing to run (`D-036a`, `D-044`)")
    return txt, scope_manifest(scope)


# ---------------------------------------------------------------- DST arms

def _dst_intervals():
    """UTC instants of the US DST transitions covering the corpus, in epoch minutes.

    Computed from `zoneinfo` rather than hard-coded, so a tzdata change is visible
    instead of silently wrong.

    THE YEAR RANGE IS DERIVED, NOT TYPED. It was `range(2012, 2018)` — correct for a
    corpus that stopped in 2016 and SILENTLY WRONG the moment `D-044` added 2017-2025:
    every Arm-B bar from 2018 on would have fallen through the loop below with `dst`
    False and been left on Arm A's clock. Not an exception, not a warning — Arm B would
    simply have become Arm A for eight years and reported itself as Arm B. It now spans
    the corpus with a year of margin either side.
    """
    out = []
    for year in range(CORPUS_YEAR_MIN - 1, CORPUS_YEAR_MAX + 2):
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

def _raw_files():
    return sorted(n for n in os.listdir(RAW_DIR)
                  if n.startswith("DAT_MT_GBPUSD_M1_") and n.endswith(".csv"))


def _fileset_fingerprint():
    """Identify the raw file set by (name, size, mtime_ns) for every file in it.

    THE CACHE USED TO BE KEYED ON NOTHING. `m1_raw_v2.npz` was reused whenever it
    existed, so adding, removing or re-downloading a raw CSV left every runner reading
    a stale parse of a corpus that no longer existed — and reading it SILENTLY, with
    correct-looking bar counts for the old file set. `D-044` adds nine files at once,
    which is exactly the event that would have triggered it.

    Cheap and honest beats cheap: this stats the files (microseconds) rather than
    hashing 400 MB, and a stat change is a superset of the content changes that matter
    here, because a raw file is only ever replaced wholesale by a re-download.
    `raw/SHA256SUMS.txt` remains the integrity record; this is a staleness check.
    """
    parts = []
    for n in _raw_files():
        st = os.stat(os.path.join(RAW_DIR, n))
        parts.append(f"{n}:{st.st_size}:{st.st_mtime_ns}")
    return "|".join(parts)


def _dedupe_exact(tm, o, h, l, c):
    """`D-044`. Remove re-emitted rows — and ONLY re-emitted rows — reporting the count.

    THE DEFECT THIS EXISTS FOR, MEASURED NOT ASSUMED. From 2019 onward the vendor emits
    the 60 minutes `19:00`-`19:59` TWICE on the EU fall-back Sunday (the last Sunday in
    October): 2019-10-27, 2020-10-25, 2021-10-31, 2022-10-30, 2023-10-29, 2024-10-27,
    2025-10-26 — 60 minutes each, 420 rows in total. The 2013-2018 files contain ZERO
    duplicate stamps, so this is a change in the vendor's pipeline, not a property of
    the product `D-036a` declared.

    THE REASON THIS IS SAFE TO REPAIR AT ALL, AND THE ONLY REASON: in all 420 cases the
    two rows are IDENTICAL in open, high, low and close. Nothing is being chosen
    between and no bar is ambiguous — one emission is a copy of the other. A repeated
    wall-clock hour folded onto itself would look completely different, and this
    function REFUSES to touch that case: a duplicated stamp whose bars DIFFER raises,
    because picking one of two genuinely different bars for the same minute is a
    modelling decision and it is not this function's to make.

    Nothing is normalised silently. The raw CSVs on disk are untouched and still match
    `raw/SHA256SUMS.txt`; the census below is carried in `DEDUPE_REPORT` and printed by
    the QA gate.
    """
    if len(tm) == 0:
        return tm, o, h, l, c, []
    dup = np.zeros(len(tm), dtype=bool)
    dup[1:] = tm[1:] == tm[:-1]
    if not dup.any():
        return tm, o, h, l, c, []
    same = (o[1:] == o[:-1]) & (h[1:] == h[:-1]) & \
           (l[1:] == l[:-1]) & (c[1:] == c[:-1])
    conflict = np.zeros(len(tm), dtype=bool)
    conflict[1:] = dup[1:] & ~same
    if conflict.any():
        bad = [m2s(t) for t in tm[conflict][:10]]
        raise SystemExit(
            f"DUPLICATE STAMPS CARRYING DIFFERENT BARS ({int(conflict.sum())}): {bad}. "
            "This is not a re-emission and `_dedupe_exact()` will not guess which bar "
            "is the minute. Record it and decide it explicitly (`D-044`)."
        )
    census = sorted(collections.Counter(
        str(np.datetime64(int(t), "m").astype("datetime64[D]")) for t in tm[dup]
    ).items())
    keep = ~dup
    return tm[keep], o[keep], h[keep], l[keep], c[keep], census


DEDUPE_REPORT = []       # [(date, n_removed)], filled by `_load_raw_m1()`


def _census_encode(census):
    """Serialise the de-dup census as one string.

    Deliberately a string and not two arrays: the first draft stored the dates as a
    numpy `U10` column, which SILENTLY TRUNCATED every entry and round-tripped a census
    of nonsense dates out of the cache while the fresh-parse path was correct. A cache
    that returns a plausible-looking wrong answer is worse than no cache.
    """
    return ";".join(f"{d}={n}" for d, n in census)


def _census_decode(s):
    if not s:
        return []
    return [(p.split("=")[0], int(p.split("=")[1])) for p in s.split(";")]


def _load_raw_m1():
    """Parse every checksummed raw CSV once; cache the parse, never the results."""
    global DEDUPE_REPORT
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache = os.path.join(CACHE_DIR, "m1_raw_v3.npz")
    fp = _fileset_fingerprint()
    if os.path.exists(cache):
        z = np.load(cache, allow_pickle=False)
        if str(z["fingerprint"]) == fp:
            DEDUPE_REPORT = _census_decode(str(z["dedupe"]))
            return z["tm"], z["o"], z["h"], z["l"], z["c"]
    tms, os_, hs, ls, cs = [], [], [], [], []
    for name in _raw_files():
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
    tm, o, h, l, c, census = _dedupe_exact(tm, o, h, l, c)
    DEDUPE_REPORT = census
    np.savez(cache, tm=tm, o=o, h=h, l=l, c=c, fingerprint=np.array(fp),
             dedupe=np.array(_census_encode(census)))
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


def load_m1(arm: str, scope: str = DEFAULT_SCOPE) -> Bars:
    """Load M1 on an arm's clock, clipped to `scope` (`SCOPES`, default DEVELOPMENT).

    THE CLIP IS APPLIED ON THE RAW FILE CLOCK, BEFORE THE ARM SHIFT, AND THE CHOICE IS
    LOAD-BEARING. Clipping on the arm's own clock instead looks more principled and is
    a silent redefinition: under Arm B the +1h DST shift relabels the last four
    development M15 bars to wall-clock 2016-07-01 (`I-010` Q2), so an arm-clock clip
    drops them and Arm-B DEVELOPMENT quietly becomes 86,820 M15 bars where `D-036a`
    committed 86,824. That is precisely the kind of change `D-044` must not make — it
    would move a boundary that an OPEN OWNER QUESTION governs, in the course of adding
    data that has nothing to do with it. `verify_against_committed("B")` catches it,
    and did: it failed on row count on the first draft of this function.

    So DEVELOPMENT stays exactly the set of raw stamps `D-035` names, on both arms, and
    `I-010` Q2 stays exactly as open as it was.
    """
    if scope not in SCOPES:
        raise SystemExit(f"unknown scope {scope!r}; known: {sorted(SCOPES)}")
    tm, o, h, l, c = _load_raw_m1()
    lo, hi = SCOPES[scope]
    if lo is not None or hi is not None:
        m = np.ones(len(tm), dtype=bool)
        if lo is not None:
            m &= tm >= lo
        if hi is not None:
            m &= tm <= hi
        tm, o, h, l, c = tm[m], o[m], h[m], l[m], c[m]
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


def load_m15(arm: str, scope: str = DEFAULT_SCOPE) -> Bars:
    """M15 on an arm's clock, clipped to `scope`.

    The clip happens at M1, BEFORE bucketing, so a bucket is never built from a
    partial set of the minutes that belong to it. Bucketing first and clipping after
    would silently hand back a 15-minute bar assembled from whichever minutes fell
    inside the scope — a different bar wearing the right timestamp.
    """
    return resample(load_m1(arm, scope), 15)


def verify_against_committed(arm: str, scope: str = DEFAULT_SCOPE):
    """Re-derive M15 and diff it against the committed `aggregate_m15.py` output.

    The check that keeps the batch honest about its own tooling: if this module's
    bucketing ever drifts from the committed aggregator, every result downstream is
    quietly measuring something else.

    `GBPUSD_M15_ARM{A,B}.csv` ARE AND REMAIN DEVELOPMENT-SCOPE FILES — 86,824 bars,
    2013 -> 2016-06-30, byte-identical to what `D-036a` committed. `D-044`'s extended
    bars are a SEPARATE artifact under `derived_ext/` and are deliberately not compared
    here. Rebuilding these two files over the extended corpus instead would have made
    the row-count arm of this check fail against every runner in the directory, and the
    honest reading of that failure is that the reference moved, not that the module
    drifted. So the reference does not move.
    """
    path = os.path.join(DATA_DIR, f"GBPUSD_M15_ARM{arm}.csv")
    ref = pd.read_csv(path, header=None, names=["d", "t", "o", "h", "l", "c", "v"])
    ref_tm = (pd.to_datetime(ref["d"] + " " + ref["t"], format="%Y.%m.%d %H:%M")
              .values.astype("datetime64[m]").astype("int64"))
    mine = load_m15(arm, scope)
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


# ---------------------------------------------------------------- C-6, general form
#
# ADDED 2026-08-13 for PT-003/004/005/006/007. PURE ADDITION: no existing function is
# changed, so PT-014/015/016/017/018/020/021 (committed df7eab6) are untouched and are
# not recomputed. `build_days()` keeps its own box/post-specific C-6; the functions
# below generalise the same rule to tests whose measured window is not the box.
#
# C-6 restated for an arbitrary window set: a session day is EXCLUDED if any 15-minute
# bucket of any window the test measures is absent from the corpus. Same rule, same
# rationale, same reporting obligation (count and name every exclusion beside n), and
# the same treatment for a real market closure as for a data hole — a half-covered
# Christmas Eve is a closure AND cannot support a full-window measurement.
#
# `QA_REPORT.txt` C8 requires that "any session flagged by C8 must have an explicit,
# PRE-REGISTERED disposition (include / exclude / report separately) in the test that
# spans it." These functions are that disposition, applied mechanically.

SESSION_ANCHOR = 17 * 60          # C-1: the session day starts at 17:00


def session_slot(mod):
    """Position of a minute-of-day within the session day: slot 0 = 17:00, 95 = 16:45."""
    return ((np.asarray(mod) - SESSION_ANCHOR) % DAY) // 15


def slot_presence(b: Bars, offset_min: int = 0):
    """Which of the 96 fifteen-minute slots of each session day exist in the corpus.

    Returns (session_days, presence[n_days, 96]). `offset_min` carries the N2 circular
    clock shift so the null is scored under the same completeness rule as the rule arm.
    """
    tm = b.tm - int(offset_min)
    sd = session_day(tm)
    slot = session_slot(minute_of_day(tm))
    uniq = np.unique(sd)
    pos = {int(d): i for i, d in enumerate(uniq)}
    P = np.zeros((len(uniq), 96), dtype=bool)
    P[np.array([pos[int(x)] for x in sd]), slot] = True
    return uniq, P


def required_slots(ranges):
    """Boolean mask over the 96 session slots covered by a list of (from, to) minutes.

    Ranges are half-open [from, to) in minute-of-day terms and may wrap midnight.
    """
    need = np.zeros(96, dtype=bool)
    for a, b_ in ranges:
        n = int(((b_ - a) % DAY) // 15)
        s0 = int(session_slot(a))
        for k in range(n):
            need[(s0 + k) % 96] = True
    return need


def complete_days(b: Bars, ranges, offset_min: int = 0):
    """C-6 for an arbitrary window set.

    Returns (session_days, keep_mask, excluded) where `excluded` names every day
    dropped, so a runner can report them beside n instead of losing them.
    """
    uniq, P = slot_presence(b, offset_min)
    need = required_slots(ranges)
    ok = P[:, need].all(axis=1)
    excluded = [dict(day=day2s(uniq[i]), missing=int((~P[i][need]).sum()))
                for i in np.where(~ok)[0]]
    return uniq, ok, excluded


def completeness_line_general(uniq, ok, excluded, max_named=8) -> str:
    """The honest form `n` must take when C-6 removed anything."""
    k = len(excluded)
    if not k:
        return (f"n = {int(ok.sum())} (0 excluded for incomplete sessions; every "
                f"included day has every 15-minute bucket the test measures)")
    named = ", ".join(f"{d['day']} ({d['missing']} slots missing)"
                      for d in excluded[:max_named])
    more = "" if k <= max_named else f", +{k - max_named} more"
    return (f"n = {int(ok.sum())} ({k} excluded for incomplete sessions: "
            f"{named}{more})")


def gini(x) -> float:
    """Gini-style concentration of a non-negative series (`PT-003` Metric 3)."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) == 0 or x.sum() <= 0:
        return float("nan")
    x = np.sort(np.clip(x, 0, None))
    n = len(x)
    i = np.arange(1, n + 1)
    return float((2.0 * np.sum(i * x) - (n + 1) * np.sum(x)) / (n * np.sum(x)))


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


def scope_manifest(scope: str = DEFAULT_SCOPE) -> str:
    """The `raw/SHA256SUMS.txt` lines for the files a `scope` can actually reach.

    A provenance header must describe the data the run READ, not every file that
    happens to sit in the directory. `D-044` put nine more years on disk; echoing the
    whole manifest into a DEVELOPMENT run would append nine hashes for years that run
    cannot see, and would have rewritten the header of all sixteen committed `PT`
    artifacts for no change in a single measured number.
    """
    with open(SHA_FILE) as fh:
        lines = [l for l in fh.read().strip().splitlines() if l.strip()]
    if scope != "development":
        return "\n".join(lines)
    keep = []
    for l in lines:
        name = l.split()[-1]
        year = os.path.basename(name)[len("DAT_MT_GBPUSD_M1_"):][:4]
        if year.isdigit() and int(year) <= 2016:
            keep.append(l)
    return "\n".join(keep)


def header(test_id: str, title: str, arm_note: str = "",
           scope: str = DEFAULT_SCOPE) -> str:
    qa, _sha = qa_gate(scope)
    lines = [
        "=" * 78,
        f"{test_id} — {title}",
        "=" * 78,
        "corpus   : HistData GBP/USD M1 (`D-036a`), SHA-256 manifest:",
    ]
    lines += ["           " + l for l in scope_manifest(scope).strip().splitlines()]
    holdout = (
        "holdout  : `D-035` 2016-07-01 -> never opened; assert_development() enforced"
        if scope == "development" else
        "holdout  : `D-044` released 2017-01-01 -> 2017-12-29 for use; "
        "2016-07-01 -> 2016-12-31 REMAINS SEALED and is not on disk"
    )
    lines += [
        "QA gate  : " + [l for l in qa.splitlines() if l.startswith("GATE:")][0],
        f"seed     : {SEED}   iterations: {ITERATIONS}   pip: {PIP}",
        holdout,
        "levels   : NOT comparable with the V02-V06 FXCM homework (`D-036a`).",
        "           Only shape and distance claims travel.",
    ]
    if arm_note:
        lines.append(arm_note)
    lines.append("=" * 78)
    return "\n".join(lines)
