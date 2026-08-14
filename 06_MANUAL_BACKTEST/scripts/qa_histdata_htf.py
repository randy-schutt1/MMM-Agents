#!/usr/bin/env python3
"""Data-QA gate for the DERIVED GBP/USD M15 and H1 bars, analogous to `qa_histdata_m1.py`.

RELATIONSHIP TO `qa_histdata_m1.py`
===================================
That script gates the M1 corpus. This one gates the coarser bars built from it. It is a
deliberate adaptation, not a copy, because two of the M1 checks change meaning once the
bars are aggregated and one becomes actively misleading if carried over unchanged:

  C1-C4  UNCHANGED IN INTENT. Parse integrity, duplicate timestamps, ordering and OHLC
         coherence are exactly as load-bearing on a derived file as on a raw one -- more
         so, because a derived file is the output of code this project wrote, and the M1
         file at least had a vendor checking it.

  C5     SPIKE CENSUS -- RESCALED, NOT REUSED. `qa_histdata_m1.py` flags a bar whose
         range exceeds 12x the rolling median range. A 15-minute bar aggregates fifteen
         minutes of movement, so its ranges are larger and its distribution is different;
         running the M1 threshold against it would flag noise. The multiple is a CLI knob
         and its default is stated per timeframe below. It remains a LIST FOR HUMAN
         REVIEW and never an exclusion, for the same reason as in M1: a Bank of England
         surprise and a corrupt tick are indistinguishable to a threshold.

  C6     GAP CENSUS -- MEANING CHANGES. At M1 a gap is a missing minute. At M15 and H1 a
         gap can only be a missing bucket, and a missing bucket means every minute inside
         it was absent. So C6 here is strictly coarser than C6 there and CANNOT replace
         it: a 20-minute hole is invisible at H1 and was already caught at M1. The M1
         gate is still the authority on gaps. This one reports bucket-level absence only.

  C7     WEEK-OPEN CENSUS -- CARRIED, and it is the check most worth re-running, because
         the week open is the fact `W-C'` and `PT-008`..`PT-013` inherit BY NAME
         (`D-036a`). An aggregation that moved the week open by one bucket would be a
         serious defect and would show here.

         The corrected M1 definition is carried verbatim: A WEEK IS DELIMITED BY ITS
         SUNDAY OPEN; AN INTRA-WEEK HOLIDAY RE-OPEN IS NEVER A WEEK BOUNDARY. The M1
         script got this wrong on first writing and it propagated into a decision entry
         before anyone caught it (`D-036a`, second correction block). It is not
         re-derived here; it is copied deliberately.

  C8     SESSION COMPLETENESS -- RESCALED. Nominal bars per session divide by the
         timeframe. The 2014-06-01/02 hole `D-036a` records must still appear, and if it
         does not, this script is wrong rather than the corpus being clean. That is
         asserted explicitly by C9.

  C9     NEW -- KNOWN-DEFECT REGRESSION. The M1 corpus has one documented unexplained
         absence (Sun 2014-06-01 17:00 -> Mon 2014-06-02 15:01, ~22 trading hours). A QA
         gate that reports a clean corpus is only trustworthy if it still reports the
         defects that are known to be there. C9 asserts the hole is visible at this
         timeframe. IT IS A GATING CHECK: if a known hole has become invisible, the
         aggregation has filled it in, which is far worse than the hole.

         This exists because of the failure `D-036a` records at length -- the M1 corpus
         "passed four gating checks and three reports while missing a full trading
         session". The compensating control for that is not a better threshold, it is a
         check that fails when a known-bad input starts looking good.

Exit status is 0 only if C1-C4 and C9 are clean. C5-C8 are reports, not gates: they need
a human, and pretending a threshold can decide them is how a real news bar becomes an
exclusion.

usage: python3 qa_histdata_htf.py CSV_FILE --timeframe {15,60} [--spike-mult N] [--arm {A,B}]
"""
import argparse
import collections
import statistics as st
import sys
from datetime import datetime, timedelta

PIP = 0.0001

# The documented hole in the M1 corpus (D-036a, first correction block). C9 asserts it is
# still visible after aggregation. Expressed in the corpus's own fixed UTC-5 clock (Arm A);
# under Arm B the same absence sits +1h, which is June and therefore inside US DST.
KNOWN_HOLE_ARM_A = (datetime(2014, 6, 1, 17, 0), datetime(2014, 6, 2, 15, 1))

# Default spike multiples. Lower than M1's 12x because aggregation shrinks the ratio
# between an eventful bar and its neighbours -- fifteen minutes of quiet still moves.
# These are TUNING CHOICES OF THIS SCRIPT, not source-derived, and C5 is not a gate.
DEFAULT_SPIKE_MULT = {15: 8.0, 60: 6.0}


def load(path):
    """Parse a HistData-format CSV. Returns (rows, c1_errors)."""
    rows, errors = [], []
    with open(path) as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 7:
                errors.append((n, f"field count {len(parts)} != 7"))
                continue
            try:
                ts = datetime.strptime(parts[0] + " " + parts[1], "%Y.%m.%d %H:%M")
                o, h, l, c = (float(x) for x in parts[2:6])
                v = float(parts[6])
            except ValueError as exc:
                errors.append((n, f"unparseable: {exc}"))
                continue
            rows.append((ts, o, h, l, c, v, n))
    rows.sort(key=lambda r: r[0])
    return rows, errors


def check_grid(rows, minutes):
    """Every timestamp must sit exactly on the timeframe grid.

    Has no M1 analogue -- at M1 the grid is every minute and the check is vacuous. Here
    it is the cheapest possible detector of a mis-floored bucket, which is the single
    most likely aggregation bug and the one that would silently shift a session boundary.
    """
    off = []
    for ts, *_rest, n in rows:
        if (ts.hour * 60 + ts.minute) % minutes != 0 or ts.second or ts.microsecond:
            off.append((ts, n))
    return off


def check_duplicates(rows):
    seen, dupes = {}, []
    for ts, *_rest, n in rows:
        if ts in seen:
            dupes.append((ts, seen[ts], n))
        else:
            seen[ts] = n
    return dupes


def check_ordering(rows):
    return [(a[0], b[0]) for a, b in zip(rows, rows[1:]) if b[0] <= a[0]]


def check_ohlc(rows):
    bad = []
    for ts, o, h, l, c, _v, n in rows:
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
            bad.append((ts, n, "; ".join(why), (o, h, l, c)))
    return bad


def spike_census(rows, mult, window=201):
    """Bars whose range exceeds `mult` x the rolling median range. A LIST, not a rule."""
    ranges = [(r[2] - r[3]) for r in rows]
    half = window // 2
    flagged = []
    for i in range(len(rows)):
        lo, hi = max(0, i - half), min(len(ranges), i + half + 1)
        med = st.median(ranges[lo:hi])
        if med <= 0:
            continue
        if ranges[i] > mult * med:
            flagged.append((rows[i][0], ranges[i] / PIP, med / PIP, ranges[i] / med))
    return flagged


def gap_census(rows, minutes):
    """Missing buckets inside a trading week. Weekends excluded by construction.

    STRICTLY COARSER THAN THE M1 GAP CHECK and not a substitute for it: an absence
    shorter than one bucket cannot appear here at all. `qa_histdata_m1.py` remains the
    authority on gaps; this reports only which buckets never got built.
    """
    step = timedelta(minutes=minutes)
    weekend = timedelta(hours=12)
    gaps = []
    for a, b in zip(rows, rows[1:]):
        delta = b[0] - a[0]
        if step < delta < weekend:
            gaps.append((a[0], b[0], delta, int(delta / step) - 1))
    return gaps


def week_opens(rows):
    """(week_opens, midweek_reopens). Definition copied from qa_histdata_m1.py.

    A week is delimited by its SUNDAY open. An intra-week holiday re-open is never a
    week boundary. The naive "first bar after any >= 12h gap" form of this check was
    WRONG in the M1 script and the error reached a decision entry before it was caught
    (D-036a, second correction block). Do not re-derive it; it is correct as written.
    """
    weekend = timedelta(hours=12)
    boundaries = [rows[0][0]]
    for a, b in zip(rows, rows[1:]):
        if (b[0] - a[0]) >= weekend:
            boundaries.append(b[0])
    return ([t for t in boundaries if t.weekday() == 6],
            [t for t in boundaries if t.weekday() != 6])


def short_weeks(rows):
    """Weeks that do not run Sunday-open -> Friday-close. Invisible to the week-open census."""
    by_day = collections.Counter(r[0].date() for r in rows)
    weeks = collections.defaultdict(list)
    for day in sorted(by_day):
        anchor = day - timedelta(days=(day.weekday() + 1) % 7)
        weeks[anchor].append(day)
    out = []
    for anchor, days in sorted(weeks.items()):
        last = max(days)
        if last.weekday() not in (4, 5):
            out.append((anchor, last, last.strftime("%a"), len(days)))
    return out


def session_completeness(rows, minutes, floor=0.60):
    """Bars present per session against the nominal count, scaled to the timeframe.

    Nominal M1 counts from qa_histdata_m1.py, divided by the timeframe: the week opens
    Sunday 17:00 and closes Friday 17:00, so Sunday is a 7-hour stub (420 minutes),
    Mon-Thu are full days, Friday runs to 17:00 (1020 minutes). Saturday is skipped --
    its absence is the market, not a defect.

    A short session is NOT automatically a defect. Holidays are real closures.
    """
    nominal_m1 = {6: 420, 0: 1440, 1: 1440, 2: 1440, 3: 1440, 4: 1020}
    per_day = collections.Counter(r[0].date() for r in rows)
    first, last = rows[0][0].date(), rows[-1][0].date()
    flagged = []
    day = first
    while day <= last:
        wd = day.weekday()
        if wd != 5:
            want = max(1, nominal_m1[wd] // minutes)
            have = per_day.get(day, 0)
            if have < floor * want:
                flagged.append((day, day.strftime("%a"), have, want))
        day += timedelta(days=1)
    return flagged


def known_defect_regression(rows, minutes, arm):
    """C9 -- assert the documented 2014-06-01/02 hole is STILL VISIBLE after aggregation.

    A gate that only reports absence of trouble is untrustworthy. This one fails if a
    known-bad stretch of input has come out looking clean, which is what an aggregator
    that invents bars would produce. It is a gate, deliberately.

    THE ASSERTION MUST BE GRID-ALIGNED, AND ON FIRST WRITING IT WAS NOT.
    The M1 corpus resumes at 2014-06-02 **15:01**. At M15 that minute falls inside the
    15:00-15:15 bucket, so a 15:00 bar legitimately exists, built from the fourteen
    surviving minutes. The first version of this check asserted emptiness over the raw
    [17:00, 15:01) interval and duly FAILED on a bar that is correct -- the defect was
    in the assertion, not in the data.

    Recorded rather than quietly corrected, because it is the same failure shape
    `D-036a` records twice: a check that treats a boundary as an absence. Here it cost
    one false alarm and nothing else, precisely because it fired loudly.

    The correct statement of the regression is therefore in two parts:
      (a) NO bar exists in the buckets wholly inside the hole, and
      (b) the bucket containing the resumption minute DOES exist -- if it were missing
          too, the hole would be longer than the record says and the record is wrong.
    """
    lo, hi = KNOWN_HOLE_ARM_A
    if arm == "B":
        lo, hi = lo + timedelta(hours=1), hi + timedelta(hours=1)  # June -> inside US DST

    def floor_grid(ts):
        total = (ts.hour * 60 + ts.minute) // minutes * minutes
        return ts.replace(hour=total // 60, minute=total % 60, second=0, microsecond=0)

    lo_b, hi_b = floor_grid(lo), floor_grid(hi)          # hi_b = the resumption bucket
    intruders = [r for r in rows if lo_b <= r[0] < hi_b]  # must be empty
    resume = [r for r in rows if r[0] == hi_b]            # must be present
    return intruders, resume, (lo_b, hi_b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--timeframe", type=int, required=True, choices=[15, 60])
    ap.add_argument("--arm", choices=["A", "B"], default="A")
    ap.add_argument("--spike-mult", type=float, default=None)
    args = ap.parse_args()
    tf = args.timeframe
    mult = args.spike_mult if args.spike_mult is not None else DEFAULT_SPIKE_MULT[tf]

    rows, c1 = load(args.csv_file)
    if not rows:
        print("FAIL C1: no parseable rows in", args.csv_file)
        return 1

    name = "M15" if tf == 15 else "H1"
    print("=" * 78)
    print(f"HISTDATA GBP/USD {name} (DERIVED) — DATA QA GATE — D-031 ARM {args.arm}")
    print("=" * 78)
    print(f"file     : {args.csv_file}")
    print(f"bars     : {len(rows):,}")
    print(f"span     : {rows[0][0]} -> {rows[-1][0]}")
    print(f"clock    : {'fixed UTC-5, no DST (corpus native)' if args.arm == 'A' else 'America/New_York, DST-tracking (file stamp +1h during US DST)'}")
    print()
    print("PROVENANCE: these bars are DERIVED from the D-036a M1 corpus by")
    print("aggregate_m15.py. HistData publishes no native M15 or H1 — see the dataset's")
    print("VENDOR_TIMEFRAME_AVAILABILITY.md. The bucket boundaries are OURS.")
    print("This gate does not, and cannot, validate them against an outside feed.")
    print()

    c0 = check_grid(rows, tf)
    c2 = check_duplicates(rows)
    c3 = check_ordering(rows)
    c4 = check_ohlc(rows)

    print("--- GATING CHECKS (must be clean) ---")
    print(f"C0 timeframe grid      : {'PASS' if not c0 else f'FAIL ({len(c0)})'}"
          f"   — every stamp on the {tf}-minute grid")
    for e in c0[:10]:
        print("     ", e)
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

    intruders, resume, (hlo, hhi) = known_defect_regression(rows, tf, args.arm)
    c9_ok = not intruders and bool(resume)
    print(f"C9 known-defect regr.  : {'PASS' if c9_ok else 'FAIL'}"
          f"   — the D-036a 2014-06-01/02 hole must STILL be visible")
    print(f"      asserted-empty buckets (arm {args.arm}): {hlo} -> {hhi}  "
          f"— {len(intruders)} bar(s) found, expected 0")
    print(f"      resumption bucket {hhi}: {'present' if resume else 'ABSENT'}, expected present")
    if intruders:
        print("      *** BARS EXIST INSIDE A WINDOW THE M1 CORPUS DOES NOT COVER. ***")
        print("      *** The aggregation is inventing bars. Do not use this file.  ***")
        for r in intruders[:10]:
            print(f"        {r[0]}  O{r[1]:.5f} H{r[2]:.5f} L{r[3]:.5f} C{r[4]:.5f}")
    if not resume:
        print("      *** The hole extends FURTHER than D-036a records. The record is")
        print("      *** wrong, or this file is truncated. Investigate before using it.")
    print()

    print("--- REPORTS (human review, not gates) ---")
    spikes = spike_census(rows, mult)
    print(f"C5 spike census        : {len(spikes)} bars > {mult:g}x rolling median range")
    print(f"      threshold is a TUNING CHOICE of this script, rescaled from M1's 12x")
    print(f"      because a {tf}-minute bar aggregates more movement. Not source-derived.")
    for ts, rng, med, ratio in sorted(spikes, key=lambda x: -x[3])[:15]:
        print(f"      {ts}  range {rng:7.1f} pips   local median {med:6.1f}   x{ratio:5.1f}")
    if len(spikes) > 15:
        print(f"      ... {len(spikes) - 15} more")
    print()

    gaps = gap_census(rows, tf)
    missing = sum(g[3] for g in gaps)
    print(f"C6 missing-bucket census: {len(gaps)} intra-week runs, {missing:,} buckets absent")
    print("      COARSER THAN THE M1 GAP CHECK AND NOT A SUBSTITUTE FOR IT — an absence")
    print("      shorter than one bucket cannot appear here. qa_histdata_m1.py is the")
    print("      authority on gaps.")
    for a, b, d, k in sorted(gaps, key=lambda x: -x[2])[:10]:
        print(f"      {a} -> {b}   {d}  ({k} buckets)")
    if len(gaps) > 10:
        print(f"      ... {len(gaps) - 10} more")
    print()

    opens, reopens = week_opens(rows)
    tod = collections.Counter(o.strftime("%H:%M") for o in opens)
    print(f"C7 week-open census    : {len(opens)} week opens (Sunday-delimited)")
    print(f"      time-of-day : {dict(tod.most_common(5))}")
    print(f"      {len(reopens)} INTRA-WEEK RE-OPENS — these are NOT week boundaries:")
    for r in reopens:
        print(f"        {r} ({r.strftime('%a')}) — mid-week re-open after a closure")
    sw = short_weeks(rows)
    print(f"      {len(sw)} week(s) not closing on a Friday — invisible to this census:")
    for anchor, last, wd, ndays in sw:
        print(f"        week of {anchor} ends {last} ({wd}), {ndays} sessions")
    bymonth = collections.defaultdict(collections.Counter)
    for o in opens:
        bymonth[o.month][o.strftime("%H:%M")] += 1
    modal = {m: bymonth[m].most_common(1)[0][0] for m in sorted(bymonth) if bymonth[m]}
    print(f"      modal open by month: {modal}")
    seasonal = len(set(modal.values())) > 1
    if args.arm == "A":
        print(f"      seasonal shift (DST): {'YES' if seasonal else 'NO — fixed offset year-round'}")
    else:
        print(f"      seasonal shift (DST): {'YES — EXPECTED on arm B' if seasonal else 'NO — UNEXPECTED on arm B, investigate'}")
    print()

    short = session_completeness(rows, tf)
    print(f"C8 session completeness: {len(short)} sessions below 60% of nominal bars")
    for day, wd, have, want in short:
        if (day.month == 12 and day.day >= 24) or (day.month == 1 and day.day <= 2):
            note = "  <- Dec/Jan holiday, a real market closure"
        elif have == 0:
            note = "  <- *** ABSENT AND UNEXPLAINED ***"
        else:
            note = "  <- *** SHORT AND UNEXPLAINED ***"
        print(f"      {day} {wd}  {have:5d} bars  (nominal ~{want:4d}, {100*have/want:5.1f}%){note}")
    print("      A short session is not automatically a defect. Holidays are closures;")
    print("      an unexplained absence is a hole. Only a human tells them apart.")
    print()

    gate_ok = not (c0 or c1 or c2 or c3 or c4) and c9_ok
    print("=" * 78)
    print("GATE:", "PASS — C0-C4 and C9 clean" if gate_ok else "FAIL — see above")
    print("C5-C8 require human sign-off before any study window is drawn from this file.")
    print("Any session flagged by C8 that falls inside a rendered window must be named in")
    print("the rendering's caption, so a hole is never mistaken for a quiet market.")
    print("=" * 78)
    return 0 if gate_ok else 1


if __name__ == "__main__":
    sys.exit(main())
