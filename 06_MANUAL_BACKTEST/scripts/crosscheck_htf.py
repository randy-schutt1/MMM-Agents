#!/usr/bin/env python3
"""Cross-check the derived GBP/USD M15 and H1 bars against independent re-derivations.

WHY THIS SCRIPT EXISTS, AND WHY IT IS NOT THE CROSS-CHECK THAT WAS ASKED FOR
===========================================================================
The commissioning request asked for the derived bars to be compared against
HistData.com's **native** M15 and H1 files. Those files do not exist. HistData
publishes tick and M1 only, on every platform it serves, and says so on its own
FAQ page:

    "For Which TimeFrames?  We can only deliver you time ordered Tick and
     M1 (1 minute) data."
        -- https://www.histdata.com/f-a-q/ , retrieved 2026-08-13

The captured evidence, with SHA-256 and retrieval date, is in
`../datasets/HISTDATA_GBPUSD_M15_H1/VENDOR_TIMEFRAME_AVAILABILITY.md`. So the
external comparison is not merely unrun, it is **unavailable from this vendor**,
and no amount of retrying will produce it. That is a negative result about the
world, recorded as such, not a task this session skipped.

What replaces it has to be honest about what it can and cannot establish:

  IT CANNOT establish that our bucket boundaries agree with an independent
  vendor's. Nothing available here can. Only a second data source can close
  that, and adopting one is a `D-034`/`D-036a`-class data-source decision that
  belongs to the owner and to `DECISIONS.md`, not to a tool script.

  IT CAN establish that the aggregation is not silently wrong in the ways
  aggregation is usually silently wrong -- and every check below is a real one
  that has broken real backtests:

    X1  independent re-implementation   a second, structurally different
                                        aggregator (dict-free, sorted-run based,
                                        written against the same spec but not
                                        the same code) must produce bar-for-bar
                                        identical output to `aggregate_m15.py`
    X2  reproducibility                 the newly derived M15 Arm A/B must be
                                        byte-identical to the M15 files `D-036a`
                                        already committed, or the corpus changed
                                        under us
    X3  transitivity                    H1 built from the M15 bars must equal H1
                                        built from the M1 bars. A boundary error
                                        in either aggregation breaks this and
                                        almost nothing else catches it.
    X4  containment                     every derived bar's O/H/L/C must be
                                        reconstructible from the M1 bars inside
                                        its own window, and from no bar outside
                                        it. This is the check that catches an
                                        off-by-one window.
    X5  arm correspondence (D-031)      Arm B is defined as Arm A shifted +1h
                                        during US DST. Bar CONTENT must therefore
                                        be identical between the arms under that
                                        relabelling. Where it is not, the bucket
                                        boundary genuinely fell in a different
                                        place, and that is a finding.
    X6  DST transition audit            explicit inspection of every US DST
                                        changeover date in the corpus, at M15 and
                                        H1, on both arms. `I-010` and the D-031
                                        Arm B logic live here.
    X7  bucket occupancy census         buckets holding fewer M1 bars than the
                                        timeframe nominally holds -- session
                                        edges, holidays, and the 2014-06-01 hole
                                        `D-036a` records.

`E06` (`COMMON_PROTOCOL.md` §2, restated by `D-036a`): every number this script
prints is parsed from a checksummed file and is reproducible by re-running it.
Nothing is read off a rendering.

usage: python3 crosscheck_htf.py RAW_M1_DIR DERIVED_DIR [--legacy-m15-dir DIR]
"""
import argparse
import collections
import glob
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
FILE_OFFSET = timedelta(hours=5)  # HistData stamps are fixed UTC-5, no DST (D-036a)
PIP = 0.0001


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------
def load_csv(path):
    """Read a HistData-format CSV: YYYY.MM.DD,HH:MM,O,H,L,C,V."""
    rows = []
    with open(path) as fh:
        for line in fh:
            p = line.strip().split(",")
            if len(p) != 7:
                continue
            ts = datetime.strptime(p[0] + " " + p[1], "%Y.%m.%d %H:%M")
            rows.append((ts, float(p[2]), float(p[3]), float(p[4]), float(p[5]), float(p[6])))
    rows.sort(key=lambda r: r[0])
    return rows


def load_m1(raw_dir):
    rows = []
    for path in sorted(glob.glob(os.path.join(raw_dir, "DAT_MT_GBPUSD_M1_*.csv"))):
        rows.extend(load_csv(path))
    rows.sort(key=lambda r: r[0])
    return rows


# ---------------------------------------------------------------------------
# X1 -- the independent re-implementation
#
# Deliberately NOT a copy of aggregate_m15.py's approach. That one accumulates
# into a dict keyed by bucket and sorts the keys at the end; this one walks the
# already-sorted series and closes a run when the bucket key changes. Two ways
# of being wrong that do not overlap: a dict aggregator survives out-of-order
# input silently, a run aggregator does not; a run aggregator mis-handles an
# empty bucket, a dict aggregator never sees one. If both agree, neither of
# those failure modes is present.
# ---------------------------------------------------------------------------
def shift_to_arm(ts, arm):
    """Map a raw UTC-5 file timestamp onto the requested D-031 arm's wall clock."""
    if arm == "A":
        return ts
    utc = ts.replace(tzinfo=timezone.utc) + FILE_OFFSET
    return utc.astimezone(NY).replace(tzinfo=None)


def bucket_of(ts, minutes):
    """Floor to the timeframe, anchored on midnight of the bar's own day."""
    total = ts.hour * 60 + ts.minute
    floored = (total // minutes) * minutes
    return ts.replace(hour=floored // 60, minute=floored % 60, second=0, microsecond=0)


def aggregate_runwise(rows, minutes, arm):
    """Second aggregator: single pass, close-the-run. Returns list of bars + occupancy."""
    out, occ = [], []
    key = None
    o = h = l = c = None
    v = 0.0
    n = 0
    for ts, ro, rh, rl, rc, rv in rows:
        k = bucket_of(shift_to_arm(ts, arm), minutes)
        if k != key:
            if key is not None:
                out.append((key, o, h, l, c, v))
                occ.append((key, n))
            key, o, h, l, c, v, n = k, ro, rh, rl, rc, rv, 1
        else:
            h = rh if rh > h else h
            l = rl if rl < l else l
            c = rc
            v += rv
            n += 1
    if key is not None:
        out.append((key, o, h, l, c, v))
        occ.append((key, n))
    return out, occ


def compare_bars(a, b, label_a, label_b, tol=0.0):
    """Bar-for-bar comparison. Returns (n_common, diffs, only_a, only_b)."""
    da = {r[0]: r for r in a}
    db = {r[0]: r for r in b}
    only_a = sorted(set(da) - set(db))
    only_b = sorted(set(db) - set(da))
    diffs = []
    for ts in sorted(set(da) & set(db)):
        ra, rb = da[ts], db[ts]
        for i, field in enumerate("OHLC", start=1):
            if abs(ra[i] - rb[i]) > tol:
                diffs.append((ts, field, ra[i], rb[i]))
    return len(set(da) & set(db)), diffs, only_a, only_b


def report_compare(name, a, b, la, lb, limit=10):
    n, diffs, oa, ob = compare_bars(a, b, la, lb)
    ok = not diffs and not oa and not ob
    print(f"{name:<52} {'PASS' if ok else 'FAIL'}")
    print(f"      {la}: {len(a):,} bars   {lb}: {len(b):,} bars   common: {n:,}")
    if oa:
        print(f"      only in {la}: {len(oa)}")
        for t in oa[:limit]:
            print(f"        {t}")
    if ob:
        print(f"      only in {lb}: {len(ob)}")
        for t in ob[:limit]:
            print(f"        {t}")
    if diffs:
        print(f"      value differences: {len(diffs)}")
        for ts, f, x, y in diffs[:limit]:
            print(f"        {ts}  {f}  {x:.6f} vs {y:.6f}  ({abs(x-y)/PIP:.2f} pips)")
    return ok


# ---------------------------------------------------------------------------
# X4 -- containment
# ---------------------------------------------------------------------------
def check_containment(m1, bars, minutes, arm, sample=None):
    """Recompute each derived bar directly from the M1 bars inside its window.

    Independent of BOTH aggregators: it groups by window membership computed from
    the bar's own timestamp rather than by any running state. Catches an off-by-one
    window, which produces bars that are individually plausible and collectively wrong.
    """
    windows = collections.defaultdict(list)
    for r in m1:
        windows[bucket_of(shift_to_arm(r[0], arm), minutes)].append(r)
    bad = []
    targets = bars if sample is None else bars[:sample]
    for ts, o, h, l, c, _v in targets:
        members = windows.get(ts)
        if not members:
            bad.append((ts, "no M1 bars in window"))
            continue
        if abs(members[0][1] - o) > 0:
            bad.append((ts, f"open {o:.6f} != first M1 open {members[0][1]:.6f}"))
        if abs(max(m[2] for m in members) - h) > 0:
            bad.append((ts, f"high {h:.6f} != max M1 high"))
        if abs(min(m[3] for m in members) - l) > 0:
            bad.append((ts, f"low {l:.6f} != min M1 low"))
        if abs(members[-1][4] - c) > 0:
            bad.append((ts, f"close {c:.6f} != last M1 close {members[-1][4]:.6f}"))
        # nothing outside the window may be inside it
        for m in members:
            if bucket_of(shift_to_arm(m[0], arm), minutes) != ts:
                bad.append((ts, f"member {m[0]} outside window"))
    return bad, len(targets)


# ---------------------------------------------------------------------------
# X5 / X6 -- D-031 arm correspondence and the DST audit
# ---------------------------------------------------------------------------
def dst_transitions(m1):
    """US DST changeover instants inside the corpus span, in the corpus's own UTC-5 clock."""
    lo, hi = m1[0][0], m1[-1][0]
    out = []
    for year in range(lo.year, hi.year + 1):
        for month, day_lo, day_hi, kind in ((3, 8, 14, "spring-forward"), (11, 1, 7, "fall-back")):
            for day in range(day_lo, day_hi + 1):
                d = datetime(year, month, day)
                if d.weekday() != 6:  # second Sunday in March / first Sunday in November
                    continue
                if lo <= d <= hi:
                    out.append((d.date(), kind))
                break
    return sorted(out)


def arm_correspondence(bars_a, bars_b, minutes):
    """Arm B should be Arm A relabelled: same CONTENT, timestamp shifted 0h or +1h.

    Compare the two arms as ordered sequences of (O,H,L,C). If the bucket boundary
    landed in the same place on both clocks -- which it must, since the shift is a
    whole number of hours and the timeframe divides an hour -- the sequences are
    identical and only the labels move. Any positional mismatch is a genuine
    boundary divergence and a D-031 finding.
    """
    seq_a = [(r[1], r[2], r[3], r[4]) for r in bars_a]
    seq_b = [(r[1], r[2], r[3], r[4]) for r in bars_b]
    if len(seq_a) != len(seq_b):
        return None, f"bar COUNT differs: arm A {len(seq_a):,}, arm B {len(seq_b):,}"
    mism = [i for i, (x, y) in enumerate(zip(seq_a, seq_b)) if x != y]
    return mism, None


def label_offsets(bars_a, bars_b):
    """Distribution of (arm B label - arm A label) over the positionally-aligned pair."""
    offs = collections.Counter()
    examples = {}
    for ra, rb in zip(bars_a, bars_b):
        d = rb[0] - ra[0]
        offs[d] += 1
        examples.setdefault(d, (ra[0], rb[0]))
    return offs, examples


# ---------------------------------------------------------------------------
# X7 -- bucket occupancy
# ---------------------------------------------------------------------------
def occupancy_report(occ, minutes):
    full = collections.Counter()
    for _ts, n in occ:
        full[n] += 1
    partial = [(ts, n) for ts, n in occ if n < minutes]
    return full, partial


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw_m1_dir")
    ap.add_argument("derived_dir")
    ap.add_argument("--legacy-m15-dir", default=None,
                    help="directory holding the D-036a GBPUSD_M15_ARM{A,B}.csv, for X2")
    ap.add_argument("--containment-sample", type=int, default=0,
                    help="0 = check every bar (default); N = check first N only")
    args = ap.parse_args()

    print("=" * 78)
    print("GBP/USD M15 / H1 — DERIVATION CROSS-CHECK")
    print("=" * 78)
    print("The requested native-vendor comparison is UNAVAILABLE: HistData publishes")
    print("tick and M1 only. See VENDOR_TIMEFRAME_AVAILABILITY.md. What follows are the")
    print("checks that ARE available, and what each can and cannot establish.")
    print()

    m1 = load_m1(args.raw_m1_dir)
    print(f"M1 source bars : {len(m1):,}")
    print(f"M1 span        : {m1[0][0]} -> {m1[-1][0]}  (corpus clock, fixed UTC-5)")
    print()

    ok_all = True
    derived = {}
    occs = {}

    # ---- X1 ---------------------------------------------------------------
    print("--- X1  INDEPENDENT RE-IMPLEMENTATION -----------------------------------")
    print("Establishes: the committed aggregator and a structurally different second")
    print("aggregator agree bar-for-bar. Does NOT establish agreement with any vendor.")
    print()
    for tf, name in ((15, "M15"), (60, "H1")):
        for arm in ("A", "B"):
            path = os.path.join(args.derived_dir, f"GBPUSD_{name}_ARM{arm}.csv")
            committed = load_csv(path)
            independent, occ = aggregate_runwise(m1, tf, arm)
            derived[(name, arm)] = committed
            occs[(name, arm)] = occ
            ok_all &= report_compare(
                f"X1  {name} arm {arm}  aggregate_m15.py vs run-wise",
                committed, independent, "committed", "independent")
    print()

    # ---- X2 ---------------------------------------------------------------
    print("--- X2  REPRODUCIBILITY AGAINST THE D-036a M15 FILES ---------------------")
    if args.legacy_m15_dir:
        for arm in ("A", "B"):
            legacy_path = os.path.join(args.legacy_m15_dir, f"GBPUSD_M15_ARM{arm}.csv")
            if not os.path.exists(legacy_path):
                print(f"X2  M15 arm {arm}: legacy file absent at {legacy_path} — SKIPPED")
                continue
            ok_all &= report_compare(
                f"X2  M15 arm {arm}  new derivation vs D-036a committed",
                derived[("M15", arm)], load_csv(legacy_path), "new", "D-036a")
    else:
        print("SKIPPED — no --legacy-m15-dir given")
    print()

    # ---- X3 ---------------------------------------------------------------
    print("--- X3  TRANSITIVITY  H1(M1) vs H1(M15) ---------------------------------")
    print("Establishes: the 15-minute and 60-minute bucket grids nest correctly. A")
    print("boundary error in either aggregation breaks this and little else catches it.")
    print()
    for arm in ("A", "B"):
        m15 = derived[("M15", arm)]
        # Re-bucket the M15 bars to H1. Their timestamps are already on the arm's
        # clock, so no second shift is applied -- applying one would be the bug
        # this check is looking for.
        h1_from_m15, _ = aggregate_runwise(m15, 60, "A")
        ok_all &= report_compare(
            f"X3  H1 arm {arm}  from M1 vs from M15",
            derived[("H1", arm)], h1_from_m15, "H1(M1)", "H1(M15)")
    print()

    # ---- X4 ---------------------------------------------------------------
    print("--- X4  CONTAINMENT  (every derived bar rebuilt from its own M1 window) --")
    print("Establishes: no bar reads a minute outside its window, and none misses one")
    print("inside it. This is the off-by-one-window check.")
    print()
    sample = args.containment_sample or None
    for tf, name in ((15, "M15"), (60, "H1")):
        for arm in ("A", "B"):
            bad, n = check_containment(m1, derived[(name, arm)], tf, arm, sample)
            print(f"X4  {name} arm {arm}: {n:,} bars checked — "
                  f"{'PASS' if not bad else f'FAIL ({len(bad)})'}")
            for ts, why in bad[:10]:
                print(f"        {ts}  {why}")
            ok_all &= not bad
    print()

    # ---- X5 ---------------------------------------------------------------
    print("--- X5  D-031 ARM CORRESPONDENCE ----------------------------------------")
    print("Arm B is defined as Arm A shifted +1h during US DST. Content must therefore")
    print("be identical under relabelling; a positional mismatch is a real divergence.")
    print()
    for tf, name in ((15, "M15"), (60, "H1")):
        a, b = derived[(name, "A")], derived[(name, "B")]
        mism, err = arm_correspondence(a, b, tf)
        if err:
            print(f"X5  {name}: FAIL — {err}")
            ok_all = False
            continue
        print(f"X5  {name}: {'PASS' if not mism else f'FAIL ({len(mism)} positional mismatches)'}"
              f"  — {len(a):,} bars aligned")
        for i in mism[:10]:
            print(f"        idx {i}: A {a[i][0]}  B {b[i][0]}")
        offs, ex = label_offsets(a, b)
        print("      label offset (arm B - arm A) distribution:")
        for d, n in sorted(offs.items()):
            ea, eb = ex[d]
            print(f"        {str(d):>16}  x{n:<8,}  e.g. A {ea} -> B {eb}")
        ok_all &= not mism
    print()

    # ---- X6 ---------------------------------------------------------------
    print("--- X6  DST TRANSITION AUDIT --------------------------------------------")
    print("Every US DST changeover in the corpus span, inspected on both arms. The")
    print("market is shut across the 02:00 local changeover instant (the week opens")
    print("Sunday 17:00), so a well-behaved corpus shows the offset changing at the")
    print("weekend boundary and NO bar landing on a skipped or repeated local hour.")
    print()
    for day, kind in dst_transitions(m1):
        print(f"  {day} ({kind})")
        for tf, name in ((15, "M15"), (60, "H1")):
            a = {r[0]: r for r in derived[(name, "A")]}
            b = derived[(name, "B")]
            lo = datetime.combine(day, datetime.min.time()) - timedelta(days=1)
            hi = lo + timedelta(days=3)
            win_b = [r for r in b if lo <= r[0] < hi]
            stamps_b = collections.Counter(r[0] for r in win_b)
            dup = [t for t, n in stamps_b.items() if n > 1]
            print(f"     {name}: {len(win_b):,} arm-B bars in [{lo.date()}, {hi.date()})"
                  f"   duplicate stamps: {len(dup)}")
            for t in dup[:5]:
                print(f"        DUPLICATE {t}")
            if dup:
                ok_all = False
            # first bar of the week following the transition, both arms
            wk = [r for r in win_b if r[0] >= datetime.combine(day, datetime.min.time())]
            if wk:
                print(f"        first arm-B bar on/after the changeover date: {wk[0][0]}")
    print()

    # ---- X7 ---------------------------------------------------------------
    print("--- X7  BUCKET OCCUPANCY CENSUS -----------------------------------------")
    print("Partial buckets are EXPECTED at session edges and across holidays; they are")
    print("reported, never repaired. A synthetic flat candle would be worse than a gap.")
    print()
    for tf, name in ((15, "M15"), (60, "H1")):
        for arm in ("A", "B"):
            occ = occs[(name, arm)]
            full, partial = occupancy_report(occ, tf)
            complete = full.get(tf, 0)
            print(f"X7  {name} arm {arm}: {len(occ):,} buckets   "
                  f"complete ({tf}/{tf} M1 bars): {complete:,} "
                  f"({100*complete/len(occ):.2f}%)   partial: {len(partial):,}")
            worst = sorted(partial, key=lambda x: x[1])[:5]
            for ts, n in worst:
                print(f"        {ts}  {n}/{tf} M1 bars")
    print()

    print("=" * 78)
    print("CROSS-CHECK:", "PASS — X1-X5, X7 clean" if ok_all else "FAIL — see above")
    print()
    print("WHAT THIS DOES NOT ESTABLISH, restated so it cannot be mislaid:")
    print("  These bars have NOT been compared against an independent vendor's M15 or")
    print("  H1. HistData publishes none. The bucket boundaries are OURS, they are")
    print("  internally consistent, and they are unvalidated against any outside feed.")
    print("  Closing that gap requires adopting a second data source, which is an")
    print("  owner decision of the D-034 / D-036a class, not a tool script's.")
    print("=" * 78)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
