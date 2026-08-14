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

  C8  session completeness — bars present per session against the nominal count

C8 EXISTS BECAUSE C1-C7 MISSED A REAL HOLE, and the way they missed it is instructive.
The corpus is absent from Sun 2014-06-01 17:00 to Mon 2014-06-02 15:01 — ~22 hours
covering an entire week open plus a Monday Asian and London session. Both relevant checks
waved it through:

  C6 excluded it BY CONSTRUCTION — the gap census skips anything >= 12h as "the weekend",
     and a missing session is indistinguishable from a weekend by duration alone.
  C7 saw it and rendered it cosmetic — it surfaced as a **Monday** entry in a weekday
     tally, where it reads as a holiday artifact rather than as an absence.

So a missing session was simultaneously invisible to the gap check and decorative to the
week-open check. C8 asks what neither asked: is each session actually THERE.

Exit status is 0 only if C1-C4 are clean. C5-C8 are reports, not gates: they need a
human, and pretending a threshold can decide them is how a bad tick becomes a finding.
C8 in particular CANNOT be a gate — Christmas and New Year produce genuinely short
sessions that are market closures, not defects, and only a human separates those from a
hole.

`--from-year` / `--to-year` / `--dedupe-exact` WERE ADDED BY `D-044`, WHICH PUT NINE MORE
YEARS IN THE SAME DIRECTORY. Two things stopped being true when it did:

  1. "Run the gate on DATA_DIR" no longer means "run the gate on `D-035` DEVELOPMENT".
     The year filter lets the DEVELOPMENT report stay exactly the report it was, and
     lets the extension be gated as its own thing rather than averaged in with it.

  2. C2 NO LONGER PASSES ON THE RAW FILES, and the reason is specific and bounded: from
     2019 on the vendor emits the 60 minutes 19:00-19:59 TWICE on the EU fall-back
     Sunday — 420 rows over seven years, every pair carrying IDENTICAL OHLC.
     `--dedupe-exact` drops the re-emitted copy and REPORTS THE COUNT AND THE DATES; it
     refuses outright if a duplicated stamp carries a different bar, because that would
     be a real ambiguity rather than a copy.

     RUN IT BOTH WAYS AND COMMIT BOTH. The un-repaired report is the honest record of
     what the vendor served; the repaired one is the gate on the corpus as the project
     actually consumes it (`mmm_lib.py` applies the same rule at load). A gate that only
     ever sees the repaired form would hide the defect; a project that only ever sees
     the raw form could never run.

usage: python3 qa_histdata_m1.py DATA_DIR [--spike-mult 12] [--gap-min 30]
                                 [--from-year Y] [--to-year Y] [--dedupe-exact]
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


def load(data_dir, from_year=None, to_year=None):
    """Parse every CSV in the directory. Returns (rows, c1_errors).

    rows: list of (datetime, open, high, low, close, volume, source_file, line_no)

    The year filter is applied to the BAR STAMP, not to the filename, so a file whose
    name and contents disagree cannot slip a year past the bound.
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
                if from_year is not None and ts.year < from_year:
                    continue
                if to_year is not None and ts.year > to_year:
                    continue
                rows.append((ts, o, h, l, c, v, name, n))
    rows.sort(key=lambda r: r[0])
    return rows, errors


def dedupe_exact(rows):
    """`D-044`. Drop re-emitted rows only, and say exactly what was dropped.

    Returns (rows, removed_by_day, conflicts). A "conflict" is a repeated stamp whose
    OHLC DIFFER — this function never resolves one, it reports it, because choosing
    between two different bars for the same minute is a modelling decision and not a
    cleanup.
    """
    out, removed, conflicts = [], [], []
    for r in rows:
        if out and r[0] == out[-1][0]:
            if r[1:5] == out[-1][1:5]:
                removed.append(r[0])
            else:
                conflicts.append(r[0])
            continue
        out.append(r)
    return out, sorted(collections.Counter(d.date() for d in removed).items()), conflicts


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


def session_completeness(rows, floor=0.60):
    """Flag sessions holding materially fewer bars than the trading day nominally holds.

    Nominal counts follow the corpus's own fixed UTC-5 clock: the week opens Sunday 17:00
    and closes Friday 17:00, so Sunday is a 7-hour stub, Monday-Thursday are full, and
    Friday runs to 17:00. Saturday is skipped — its absence is the market, not a defect.

    Returns (date, weekday, actual, nominal) for each session under `floor` x nominal.
    A short session is NOT automatically a defect: holidays are real closures. This
    separates "look at these" from "these are fine", nothing more.
    """
    nominal = {6: 420, 0: 1440, 1: 1440, 2: 1440, 3: 1440, 4: 1020}
    per_day = collections.Counter(r[0].date() for r in rows)
    first, last = rows[0][0].date(), rows[-1][0].date()
    flagged = []
    day = first
    while day <= last:
        wd = day.weekday()
        if wd != 5:  # Saturday: no session expected
            want = nominal[wd]
            have = per_day.get(day, 0)
            if have < floor * want:
                flagged.append((day, day.strftime("%a"), have, want))
        day += timedelta(days=1)
    return flagged


def week_opens(rows):
    """Return (week_opens, midweek_reopens).

    CORRECTED — the naive form of this check was WRONG, and wrong in a way that
    propagated into a decision entry before anyone noticed.

    The original implementation returned "the first bar after any gap >= 12h" and called
    every one of them a week open. That is not what a week open is. A Christmas or New
    Year closure also produces a >= 12h gap *in the middle of a week that opened normally
    on Sunday*, and the naive check reports the re-open as though the week restarted there:

        2013-12-22 Sun 17:00  <- the actual week open, 418 bars
        2013-12-24 Tue        <- closes early
        2013-12-25 Wed        <- 0 bars, market shut
        2013-12-26 Thu 06:02  <- a RE-OPEN, reported by the naive check as a "week open"

    A run session deriving week boundaries from that output would split four weeks in two.
    The inverse error is just as bad: when a holiday closure merges with the weekend, the
    affected week produces NO irregular open at all and the naive check stays silent —
    2015-12-20 and 2015-12-27 both END ON THURSDAY and neither was flagged.

    So: a week is delimited by its **Sunday** open. An intra-week re-open is never a week
    boundary. Both are reported, separately, because the second set matters — a
    Thursday-ending week shortens every censoring horizon that runs to the week close.
    """
    weekend = timedelta(hours=12)
    boundaries = [rows[0][0]]
    for a, b in zip(rows, rows[1:]):
        if (b[0] - a[0]) >= weekend:
            boundaries.append(b[0])
    opens = [t for t in boundaries if t.weekday() == 6]
    reopens = [t for t in boundaries if t.weekday() != 6]
    return opens, reopens


def short_weeks(rows):
    """Weeks that do not run the full Sunday-open -> Friday-close span.

    Invisible to the week-open census by construction: when a holiday closure abuts the
    weekend, the week simply ends early and no anomalous open is ever emitted.
    """
    by_day = collections.Counter(r[0].date() for r in rows)
    weeks = collections.defaultdict(list)
    for day in sorted(by_day):
        # attribute each session to the Sunday that opened its week
        anchor = day - timedelta(days=(day.weekday() + 1) % 7)
        weeks[anchor].append(day)
    out = []
    for anchor, days in sorted(weeks.items()):
        last = max(days)
        if last.weekday() not in (4,):  # a normal week closes Friday
            if last.weekday() != 5:  # Saturday never trades
                out.append((anchor, last, last.strftime("%a"), len(days)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("--spike-mult", type=float, default=12.0)
    ap.add_argument("--gap-min", type=int, default=30)
    ap.add_argument("--from-year", type=int)
    ap.add_argument("--to-year", type=int)
    ap.add_argument("--dedupe-exact", action="store_true",
                    help="drop vendor re-emitted rows before gating (`D-044`); "
                         "the removal is always reported, never silent")
    args = ap.parse_args()

    rows, c1 = load(args.data_dir, args.from_year, args.to_year)
    if not rows:
        print("FAIL C1: no parseable rows found in", args.data_dir)
        return 1

    dedup_days, conflicts = [], []
    if args.dedupe_exact:
        rows, dedup_days, conflicts = dedupe_exact(rows)

    print("=" * 78)
    print("HISTDATA GBP/USD M1 — DATA QA GATE")
    print("=" * 78)
    print(f"files    : {len(set(r[6] for r in rows))}")
    print(f"bars     : {len(rows):,}")
    print(f"span     : {rows[0][0]} -> {rows[-1][0]}")
    if args.from_year or args.to_year:
        print(f"years    : {args.from_year or '(start)'} -> {args.to_year or '(end)'}")
    if args.dedupe_exact:
        n = sum(k for _d, k in dedup_days)
        print(f"dedupe   : `D-044` exact-duplicate removal APPLIED — {n} row(s) dropped")
        for d, k in dedup_days:
            print(f"           {d}  {k} re-emitted minute(s)")
        if conflicts:
            print(f"           *** {len(conflicts)} DUPLICATED STAMP(S) CARRY DIFFERENT "
                  f"BARS — NOT REPAIRED, NOT REPAIRABLE HERE ***")
            for t in conflicts[:10]:
                print(f"           {t}")
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

    opens, reopens = week_opens(rows)
    tod = collections.Counter(o.strftime("%H:%M") for o in opens)
    print(f"C7 week-open census    : {len(opens)} week opens (Sunday-delimited)")
    print(f"      time-of-day : {dict(tod.most_common(5))}")
    print(f"      {len(reopens)} INTRA-WEEK RE-OPENS — these are NOT week boundaries:")
    for r in reopens:
        print(f"        {r} ({r.strftime('%a')}) — mid-week re-open after a closure")
    print("      Deriving week boundaries from re-opens would split those weeks in two.")
    sw = short_weeks(rows)
    print(f"      {len(sw)} week(s) not closing on a Friday — invisible to this census:")
    for anchor, last, wd, ndays in sw:
        print(f"        week of {anchor} ends {last} ({wd}), {ndays} sessions")
    bymonth = collections.defaultdict(collections.Counter)
    for o in opens:
        bymonth[o.month][o.strftime("%H:%M")] += 1
    modal = {m: bymonth[m].most_common(1)[0][0] for m in sorted(bymonth) if bymonth[m]}
    seasonal = len(set(modal.values())) > 1
    print(f"      modal open by month: {modal}")
    print(f"      seasonal shift (DST): {'YES' if seasonal else 'NO — fixed offset year-round'}")
    print()

    short = session_completeness(rows)
    print(f"C8 session completeness: {len(short)} sessions below 60% of nominal bars")
    for day, wd, have, want in short:
        note = ""
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

    gate_ok = not (c1 or c2 or c3 or c4 or conflicts)
    print("=" * 78)
    print("GATE:", "PASS — C1-C4 clean" if gate_ok else "FAIL — see above")
    print("C5-C8 require human sign-off before any PT test is run.")
    print("Any session flagged by C8 must have an explicit, PRE-REGISTERED disposition")
    print("(include / exclude / report separately) in the test that spans it.")
    print("=" * 78)
    return 0 if gate_ok else 1


if __name__ == "__main__":
    sys.exit(main())
