#!/usr/bin/env python3
"""V07 HOMEWORK — the assignment the lesson actually gives, performed.

V07's assignment, in the presenter's own words, [00:12:03]-[00:12:09]:

    "They have to go back to looking charts so you can see how many times it occurred.
     How many times over a year is what I am looking for actually occurred, where I am
     looking to get it."

Three items, plus a second measurement method:

  H1  the frequency count, over one full year, of the only mechanical object V07 supplies:
      a 50-pip run from the day's extreme. Counted per day definition and per session
      window. This is the assignment applied literally.

  H3  a BASE-RATE CENSUS of a declared, NON-COURSE shape family, run to check the
      presenter's own qualitative claim at [00:06:32] that "M's and W's are everywhere".
      See the fence in the header of item H3 below and in V07_HOMEWORK.md §3 -- the shapes
      counted here are NOT the course's M and W and are not offered as a definition of one.

  H4  the same H1 counts recomputed from the M1 corpus directly, bypassing the M15
      aggregate entirely. A second measurement method on the same underlying data, which
      is what catches an aggregation bug.

E06 as restated by D-036a: every number is parsed from a checksummed CSV. Nothing is
measured off a rendering.

Usage:  python3 05_HOMEWORK/V07/scripts/v07_homework.py
"""
import csv, hashlib, json, os, statistics
from datetime import datetime, timedelta, date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA = os.path.join(ROOT, "06_MANUAL_BACKTEST", "datasets", "HISTDATA_GBPUSD_M1")
OUT = os.path.join(ROOT, "05_HOMEWORK", "V07", "data")

YEAR_START = date(2015, 1, 1)          # one full calendar year, inside DEVELOPMENT (D-035)
YEAR_END = date(2015, 12, 31)
TARGET_PIPS = 50.0                     # the lesson's own exit
PIP = 0.0001

# H3 grid — declared, NON-COURSE, and swept rather than chosen (D-010)
H3_SWING_N = [2, 3, 4, 5]              # bars either side that define a local extreme
H3_TOL_PIPS = [3, 5, 10, 20]           # how close the two peaks must be to count as "level"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def load_m15(path):
    bars = []
    with open(path, newline="") as f:
        for r in csv.reader(f):
            if len(r) < 6:
                continue
            d, t = r[0], r[1]
            bars.append((datetime(int(d[0:4]), int(d[5:7]), int(d[8:10]), int(t[0:2]), int(t[3:5])),
                         float(r[2]), float(r[3]), float(r[4]), float(r[5])))
    return bars


def load_m1_year(paths):
    """Only the target year, to keep memory sane."""
    bars = []
    for p in paths:
        with open(p, newline="") as f:
            for r in csv.reader(f):
                if len(r) < 6:
                    continue
                d = r[0]
                y = int(d[0:4])
                if y != YEAR_START.year:
                    continue
                t = r[1]
                bars.append((datetime(y, int(d[5:7]), int(d[8:10]), int(t[0:2]), int(t[3:5])),
                             float(r[2]), float(r[3]), float(r[4]), float(r[5])))
    bars.sort(key=lambda x: x[0])
    return bars


def day_key(dt, daydef):
    return dt.date() if daydef == "D-MIDNIGHT" else (dt + timedelta(hours=7)).date()


def group(bars, daydef, lo=YEAR_START, hi=YEAR_END, min_bars=4):
    days = {}
    for b in bars:
        if not (lo <= b[0].date() <= hi):
            continue
        days.setdefault(day_key(b[0], daydef), []).append(b)
    return {k: sorted(v, key=lambda x: x[0]) for k, v in days.items() if len(v) >= min_bars}


def h1_count(days):
    """How many days offered a 50-pip run from the day extreme, and in which window."""
    hit_days, miss_days = [], []
    window = {"asian": 0, "london": 0, "newyork": 0, "other": 0}
    for k in sorted(days):
        bars = days[k]
        hod = max(b[2] for b in bars)
        lod = min(b[3] for b in bars)
        i_s = next(i for i, b in enumerate(bars) if b[2] >= hod)
        i_l = next(i for i, b in enumerate(bars) if b[3] <= lod)
        ok = False
        for i, d in ((i_s, "SHORT"), (i_l, "LONG")):
            entry = bars[i][2] if d == "SHORT" else bars[i][3]
            goal = entry - TARGET_PIPS * PIP if d == "SHORT" else entry + TARGET_PIPS * PIP
            reached = any((b[3] <= goal) if d == "SHORT" else (b[2] >= goal) for b in bars[i + 1:])
            if reached:
                ok = True
                h = bars[i][0].hour
                # V02's printed table, in the corpus's own fixed UTC-5 clock
                if 19 <= h or h < 3:
                    window["asian"] += 1
                elif 3 <= h < 9:
                    window["london"] += 1
                elif 9 <= h < 17:
                    window["newyork"] += 1
                else:
                    window["other"] += 1
        (hit_days if ok else miss_days).append(str(k))
    return {"n_days": len(days), "hit_days": len(hit_days), "miss_days": len(miss_days),
            "frac": len(hit_days) / len(days), "entry_window_counts": window,
            "hit_sample": hit_days[:5], "miss_sample": miss_days[:5], "misses": miss_days}


def h3_census(bars, n, tol):
    """Count DECLARED, NON-COURSE double-top / double-bottom shapes in the year.

    A 'shape' here is: two local extremes, each higher/lower than the n bars on both sides,
    separated by at least n bars and at most 40 bars, whose extreme prices are within tol
    pips of one another. THIS IS NOT THE COURSE'S M OR W and is not offered as one -- it is
    a deliberately crude, fully-stated stand-in used ONLY to ask whether shapes of roughly
    this kind are common, which is the presenter's own qualitative claim.
    """
    yr = [b for b in bars if YEAR_START <= b[0].date() <= YEAR_END]
    highs, lows = [], []
    for i in range(n, len(yr) - n):
        h = yr[i][2]
        l = yr[i][3]
        if all(h >= yr[j][2] for j in range(i - n, i + n + 1)):
            highs.append((i, h))
        if all(l <= yr[j][3] for j in range(i - n, i + n + 1)):
            lows.append((i, l))
    def pairs(pts):
        c = 0
        for a in range(len(pts)):
            for b in range(a + 1, len(pts)):
                gap = pts[b][0] - pts[a][0]
                if gap < n:
                    continue
                if gap > 40:
                    break
                if abs(pts[b][1] - pts[a][1]) <= tol * PIP:
                    c += 1
        return c
    return {"bars_in_year": len(yr), "local_highs": len(highs), "local_lows": len(lows),
            "M_like": pairs(highs), "W_like": pairs(lows)}


def main():
    os.makedirs(OUT, exist_ok=True)
    m15 = {a: os.path.join(DATA, f"GBPUSD_M15_ARM{a}.csv") for a in ("A", "B")}
    raw = [os.path.join(DATA, "raw", f"DAT_MT_GBPUSD_M1_{y}.csv") for y in (2015,)]

    print("=" * 78)
    print("V07 HOMEWORK — 'How many times over a year ... actually occurred'  [00:12:09]")
    print("=" * 78)
    print(f"\n  year   : {YEAR_START} -> {YEAR_END}  (inside DEVELOPMENT, D-035)")
    print(f"  target : {TARGET_PIPS:.0f} pips — the lesson's own exit")
    print("\n--- INPUT INTEGRITY (E06 / D-036a) ---")
    digests = {}
    for k, p in list(m15.items()) + [("M1-2015", raw[0])]:
        digests[k] = sha256(p)
        print(f"  {k:8} {os.path.basename(p):26} sha256={digests[k]}")

    res = {"year": [str(YEAR_START), str(YEAR_END)], "target_pips": TARGET_PIPS,
           "digests": digests, "H1": {}, "H3": {}, "H4": {}}

    # ---------------- H1 ----------------
    print("\n" + "=" * 78)
    print("H1 — THE FREQUENCY COUNT, AS ASSIGNED (M15 aggregate)")
    print("=" * 78)
    barsA = load_m15(m15["A"])
    barsB = load_m15(m15["B"])
    for arm, bars in (("A", barsA), ("B", barsB)):
        for dd in ("D-SESSION", "D-MIDNIGHT"):
            days = group(bars, dd)
            r = h1_count(days)
            res["H1"][f"{arm}|{dd}"] = r
            print(f"\n  {arm}|{dd}:  days={r['n_days']}  offered a 50-pip run from the extreme "
                  f"on {r['hit_days']} of them  ({r['frac']:.3f})")
            print(f"    days it did NOT: {r['miss_days']}")
            print(f"    entry-bar window of the successful entries "
                  f"(V02's printed table, corpus clock): {r['entry_window_counts']}")

    # ---------------- H4 : second measurement method ----------------
    print("\n" + "=" * 78)
    print("H4 — SECOND MEASUREMENT METHOD: the same count from M1 directly")
    print("=" * 78)
    m1 = load_m1_year(raw)
    print(f"  M1 bars loaded for {YEAR_START.year}: {len(m1):,}")
    for dd in ("D-SESSION", "D-MIDNIGHT"):
        days = group(m1, dd, min_bars=60)
        r = h1_count(days)
        res["H4"][f"M1|{dd}"] = r
        a = res["H1"][f"A|{dd}"]
        print(f"\n  M1|{dd}: days={r['n_days']} (M15 said {a['n_days']})   "
              f"hits={r['hit_days']} ({r['frac']:.3f})  vs M15 {a['hit_days']} ({a['frac']:.3f})")
        sm, sa = set(r["misses"]), set(a["misses"])
        print(f"    miss-day sets: M1 {len(sm)}, M15 {len(sa)}, agree on {len(sm & sa)}, "
              f"M1-only {sorted(sm - sa)}, M15-only {sorted(sa - sm)}")
        res["H4"][f"M1|{dd}"]["agreement"] = {
            "m1_only": sorted(sm - sa), "m15_only": sorted(sa - sm), "both": len(sm & sa)}

    # ---------------- H3 ----------------
    print("\n" + "=" * 78)
    print("H3 — BASE-RATE CENSUS OF A DECLARED, NON-COURSE SHAPE FAMILY")
    print("     THESE ARE NOT THE COURSE'S M AND W. See V07_HOMEWORK.md §3.")
    print("=" * 78)
    for n in H3_SWING_N:
        for tol in H3_TOL_PIPS:
            r = h3_census(barsA, n, tol)
            res["H3"][f"n={n},tol={tol}"] = r
            print(f"  swing={n:2}  tol={tol:2}p :  local highs {r['local_highs']:5}  "
                  f"lows {r['local_lows']:5}  |  M-like {r['M_like']:6}   W-like {r['W_like']:6}")
    res["H3"]["bars_in_year"] = h3_census(barsA, 2, 3)["bars_in_year"]

    with open(os.path.join(OUT, "v07_homework_results.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    print(f"\nwrote {os.path.join(OUT, 'v07_homework_results.json')}")


if __name__ == "__main__":
    main()
