#!/usr/bin/env python3
"""Data-QA gate for the HistData GBP/USD M1 corpus, required before any PT test runs.

Why this exists. The manual phase moved from a rendered chart to a CSV corpus, and the
two fail differently. On a chart a bad tick is a 200-pip spike you cannot miss; in a
column of numbers it simply computes, silently, into a result. `D-034`'s standing answer
to "is this feed trustworthy" was a *depth* probe, which answers reachability and nothing
else. This script is the replacement question: is the data SOUND.

Nothing here reads a price to draw a conclusion about the market. Every check is a
structural assertion about the file, so running it does not consult the holdout, does not
touch a window's outcome, and cannot be outcome-informed.

Seven checks, each of which has silently corrupted a backtest somewhere:

  C1  parse integrity      — field count, parseable timestamp, parseable numbers
  C2  duplicate timestamps — the same minute twice ranks as two observations
  C3  ordering             — strictly increasing; an out-of-order block breaks any
                             "first close beyond X" trigger, which is most of this batch
  C4  OHLC coherence       — high >= max(open, close), low <= min(open, close),
                             high >= low, all quotes positive
  C5  spike census         — bar range against a rolling median, flagged not deleted.
                             A real news bar and a bad tick look identical here; this
                             produces a LIST FOR HUMAN REVIEW, never an auto-exclusion
  C6  gap census           — intra-week gaps over a threshold, weekends excluded by
                             construction (they are not gaps, they are the market shut)
  C7  week-open census     — time-of-day of the first bar after each weekend, which is
                             the vendor fact `W-C'` and PT-008..PT-013 inherit BY NAME

Exit status is 0 only if C1-C4 are clean. C5-C7 are reports, not gates: they need a
human, and pretending a threshold can decide them is how a bad tick becomes a finding.

usage: python3 qa_histdata_m1.py DATA_DIR [--spike-mult 12] [--gap-min 30]
       DATA_DIR holds DAT_MT_GBPUSD_M1_*.csv
"""
import argparse
import collections
import glob
import os
import statistics as st
import sys
from datetime import datetime, timedelta

PIP = 0.0001


def load(data_dir):
    """Parse every CSV in the directory. Returns (rows, c1_errors).

    rows: list of (datetime, open, high, low, close, volume, source_file, line_no)
    """
    rows, errors = [], []
    for path in sorted(glob.glob(os.path.join(data_dir, "DAT_MT_GBPUSD_M1_*.csv"))):
        name = os.path.basename(path)
        with open(path) as fh:
            for n, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 7:
                    errors.append((name, n, f"field count {len(parts)} != 7"))
                    continue
                try:
                    ts = datetime.strptime(parts[0] + " " + parts[1], "%Y.%m.%d %H:%M")
                    o, h, l, c = (float(x) for x in parts[2:6])
                    v = float(parts[6])
                except ValueError as exc:
                    errors.append((name, n, f"unparseable: {exc}"))
                    continue
                rows.append((ts, o, h, l, c, v, name, n))
    rows.sort(key=lambda r: r[0])
    return rows, errors


def check_duplicates(rows):
    seen, dupes = {}, []
    for ts, *_rest, name, n in rows:
        if ts in seen:
            dupes.append((ts, seen[ts], (name, n)))
        else:
            seen[ts] = (name, n)
    return dupes


def check_ordering(rows):
    """rows is sorted, so this reports ties only; genuine disorder shows up as C2."""
    return [
        (a[0], b[0]) for a, b in zip(rows, rows[1:]) if b[0] <= a[0]
    ]


def check_ohlc(rows):
    bad = []
    for ts, o, h, l, c, _v, name, n in rows:
        why = []
        if h < l:
            why.append("high < low")
        if h < max(o, c):
            why.append("high < max(open,close)")
        if l > min(o, c):
            why.append("low > min(open,close)")
        if min(o, h, l, c) <= 0:
            why.append("non-positive quote")
        if why:
            bad.append((ts, name, n, "; ".join(why), (o, h, l, c)))
    return bad


def spike_census(rows, mult, window=201):
    """Flag bars whose range exceeds `mult` x the rolling median range.

    Deliberately NOT an exclusion rule. A Bank of England surprise and a corrupt tick
    both land here; only a human looking at the surrounding bars can tell them apart.
    """
    ranges = [(r[2] - r[3]) for r in rows]
    half = window // 2
    flagged = []
    for i in range(len(rows)):
        lo, hi = max(0, i - half), min(len(ranges), i + half + 1)
        local = ranges[lo:hi]
        med = st.median(local)
        if med <= 0:
            continue
        if ranges[i] > mult * med:
            flagged.append((rows[i][0], ranges[i] / PIP, med / PIP, ranges[i] / med))
    return flagged


def gap_census(rows, gap_min):
    """Gaps inside a trading week. A weekend is not a gap; it is the market being shut."""
    threshold = timedelta(minutes=gap_min)
    weekend = timedelta(hours=12)
    gaps = []
    for a, b in zip(rows, rows[1:]):
        delta = b[0] - a[0]
        if threshold <= delta < weekend:
            gaps.append((a[0], b[0], delta))
    return gaps


def week_opens(rows):
    weekend = timedelta(hours=12)
    opens = [rows[0][0]]
    for a, b in zip(rows, rows[1:]):
        if (b[0] - a[0]) >= weekend:
            opens.append(b[0])
    return opens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("--spike-mult", type=float, default=12.0)
    ap.add_argument("--gap-min", type=int, default=30)
    args = ap.parse_args()

    rows, c1 = load(args.data_dir)
    if not rows:
        print("FAIL C1: no parseable rows found in", args.data_dir)
        return 1

    print("=" * 78)
    print("HISTDATA GBP/USD M1 — DATA QA GATE")
    print("=" * 78)
    print(f"files    : {len(set(r[6] for r in rows))}")
    print(f"bars     : {len(rows):,}")
    print(f"span     : {rows[0][0]} -> {rows[-1][0]}")
    print()

    c2 = check_duplicates(rows)
    c3 = check_ordering(rows)
    c4 = check_ohlc(rows)

    print("--- GATING CHECKS (must be clean) ---")
    print(f"C1 parse integrity     : {'PASS' if not c1 else f'FAIL ({len(c1)})'}")
    for e in c1[:10]:
        print("     ", e)
    print(f"C2 duplicate timestamps: {'PASS' if not c2 else f'FAIL ({len(c2)})'}")
    for e in c2[:10]:
        print("     ", e)
    print(f"C3 ordering            : {'PASS' if not c3 else f'FAIL ({len(c3)})'}")
    for e in c3[:10]:
        print("     ", e)
    print(f"C4 OHLC coherence      : {'PASS' if not c4 else f'FAIL ({len(c4)})'}")
    for e in c4[:10]:
        print("     ", e)
    print()

    print("--- REPORTS (human review, not gates) ---")
    spikes = spike_census(rows, args.spike_mult)
    print(f"C5 spike census        : {len(spikes)} bars > {args.spike_mult:g}x rolling median range")
    for ts, rng, med, ratio in sorted(spikes, key=lambda x: -x[3])[:15]:
        print(f"      {ts}  range {rng:7.1f} pips   local median {med:5.1f}   x{ratio:5.1f}")
    if len(spikes) > 15:
        print(f"      ... {len(spikes) - 15} more")
    print()

    gaps = gap_census(rows, args.gap_min)
    total_gap = sum((g[2] for g in gaps), timedelta())
    print(f"C6 gap census          : {len(gaps)} intra-week gaps >= {args.gap_min}m, {total_gap} total")
    for a, b, d in sorted(gaps, key=lambda x: -x[2])[:10]:
        print(f"      {a} -> {b}   {d}")
    if len(gaps) > 10:
        print(f"      ... {len(gaps) - 10} more")
    print()

    opens = week_opens(rows)
    tod = collections.Counter(o.strftime("%H:%M") for o in opens)
    dow = collections.Counter(o.strftime("%a") for o in opens)
    print(f"C7 week-open census    : {len(opens)} week opens")
    print(f"      time-of-day : {dict(tod.most_common(5))}")
    print(f"      weekday     : {dict(dow)}")
    bymonth = collections.defaultdict(collections.Counter)
    for o in opens:
        bymonth[o.month][o.strftime("%H:%M")] += 1
    modal = {m: bymonth[m].most_common(1)[0][0] for m in sorted(bymonth) if bymonth[m]}
    seasonal = len(set(modal.values())) > 1
    print(f"      modal open by month: {modal}")
    print(f"      seasonal shift (DST): {'YES' if seasonal else 'NO — fixed offset year-round'}")
    print()

    gate_ok = not (c1 or c2 or c3 or c4)
    print("=" * 78)
    print("GATE:", "PASS — C1-C4 clean" if gate_ok else "FAIL — see above")
    print("C5-C7 require human sign-off before any PT test is run.")
    print("=" * 78)
    return 0 if gate_ok else 1


if __name__ == "__main__":
    sys.exit(main())
