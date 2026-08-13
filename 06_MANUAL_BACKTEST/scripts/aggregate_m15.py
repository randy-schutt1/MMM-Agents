#!/usr/bin/env python3
"""Aggregate the HistData GBP/USD M1 corpus up to a coarser timeframe, per `D-031` arm.

Why an aggregator instead of downloading M15 directly. The vendor's own M1 file is the
finest thing it publishes; every coarser bar is a derived object. Deriving it here rather
than trusting a vendor's aggregation means the bucket boundaries are OURS and auditable,
which matters because `D-031` makes the boundary itself the tested variable.

The `D-031` arms, and why this file is unusually cheap to run both ways:

  HistData stamps every bar in **fixed UTC-5, no DST** (vendor spec, corroborated here by
  187 week opens sitting at 17:00 in all twelve months). That is *exactly* `D-031` Arm A.
  So:

    Arm A  — fixed offset UTC-5 year-round        -> file timestamps VERBATIM, no shift
    Arm B  — America/New_York, DST active         -> file timestamp + 1h during US DST,
                                                     unchanged during standard time

  Derivation for Arm B: a file stamp `T` denotes `UTC = T + 5h`. New York local is UTC-4
  under DST, so local `= (T + 5h) - 4h = T + 1h`; under standard time it is UTC-5 `= T`.

  On a rendered chart, running both arms meant harvesting the same window twice by hand.
  Here it is one flag. `D-031`'s binding rule — **both arms always reported** — stops
  being expensive, which is the point.

No bar is invented. A bucket is emitted only if at least one M1 bar falls inside it, so
holidays and the weekend stay absent rather than becoming flat synthetic candles. Volume
is summed and is structurally zero in this vendor's data; it is carried for format
compatibility and must not be read as traded volume.

usage: python3 aggregate_m15.py RAW_DIR --arm {A,B} [--timeframe 15] [--out FILE]
"""
import argparse
import glob
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
FILE_OFFSET = timedelta(hours=5)  # file stamps are UTC-5


def shift_to_arm(ts, arm):
    """Map a raw file timestamp onto the requested D-031 arm's wall clock."""
    if arm == "A":
        return ts
    utc = ts.replace(tzinfo=timezone.utc) + FILE_OFFSET
    return utc.astimezone(NY).replace(tzinfo=None)


def load_m1(raw_dir):
    rows = []
    for path in sorted(glob.glob(os.path.join(raw_dir, "DAT_MT_GBPUSD_M1_*.csv"))):
        with open(path) as fh:
            for line in fh:
                p = line.strip().split(",")
                if len(p) != 7:
                    continue
                ts = datetime.strptime(p[0] + " " + p[1], "%Y.%m.%d %H:%M")
                rows.append((ts, float(p[2]), float(p[3]), float(p[4]), float(p[5]), float(p[6])))
    rows.sort(key=lambda r: r[0])
    return rows


def bucket(ts, minutes):
    """Floor to the timeframe, anchored on midnight of the bar's own day."""
    total = ts.hour * 60 + ts.minute
    floored = (total // minutes) * minutes
    return ts.replace(hour=floored // 60, minute=floored % 60, second=0, microsecond=0)


def aggregate(rows, minutes, arm):
    out = {}
    order = []
    for ts, o, h, l, c, v in rows:
        key = bucket(shift_to_arm(ts, arm), minutes)
        if key not in out:
            out[key] = [o, h, l, c, v]
            order.append(key)
        else:
            b = out[key]
            b[1] = max(b[1], h)
            b[2] = min(b[2], l)
            b[3] = c
            b[4] += v
    order.sort()
    return [(k, *out[k]) for k in order]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw_dir")
    ap.add_argument("--arm", choices=["A", "B"], required=True)
    ap.add_argument("--timeframe", type=int, default=15)
    ap.add_argument("--out")
    args = ap.parse_args()

    m1 = load_m1(args.raw_dir)
    if not m1:
        print("no M1 rows found in", args.raw_dir, file=sys.stderr)
        return 1
    bars = aggregate(m1, args.timeframe, args.arm)

    dest = args.out or os.path.join(
        args.raw_dir, "..", f"GBPUSD_M{args.timeframe}_ARM{args.arm}.csv"
    )
    dest = os.path.normpath(dest)
    with open(dest, "w") as fh:
        for ts, o, h, l, c, v in bars:
            fh.write(
                f"{ts:%Y.%m.%d},{ts:%H:%M},{o:.6f},{h:.6f},{l:.6f},{c:.6f},{v:.0f}\n"
            )

    print(f"arm {args.arm}  M{args.timeframe}")
    print(f"  source M1 bars : {len(m1):,}")
    print(f"  emitted bars   : {len(bars):,}")
    print(f"  span           : {bars[0][0]} -> {bars[-1][0]}")
    print(f"  written        : {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
