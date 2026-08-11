#!/usr/bin/env python3
"""Validate the harvest and slice one complete trading week, using the bars' OWN
timestamps rather than a bar-count cadence.

This is the V04 review-R1 M1 defect fixed at the source: there, 15m bars carried no
timestamps, the week boundary was inferred from a fixed 16-bars-per-4h-bar assumption,
and USDCHF's partial first bar (12, not 16) silently put four previous-week bars at the
head of the slice. Here the boundary is read.
"""
import json, datetime as dt, collections

D = json.load(open('v05_15m.json'))
WEEK_START = dt.datetime(2026, 8, 2, 21, 0)     # Sun 21:00 UTC — FX week open on this feed
WEEK_END = dt.datetime(2026, 8, 7, 21, 0)       # Fri 21:00 UTC

out = {}
print(f'{"pair":8} {"raw":>5} {"dedup":>6} {"week":>5}  first_bar          last_bar           gaps')
for sym, d in D.items():
    bars = d['bars']
    ts = [dt.datetime.fromisoformat(b['t']) for b in bars]

    # 1. strictly increasing, no duplicate timestamps
    assert all(ts[i] < ts[i + 1] for i in range(len(ts) - 1)), f'{sym} not strictly increasing'

    # 2. drop the live-edge artifact: TradingView reports the still-forming bar's OHLC for
    #    every projected future slot, so trailing bars repeat identical OHLC.
    trimmed = list(bars)
    while len(trimmed) >= 2 and (trimmed[-1]['o'], trimmed[-1]['h'], trimmed[-1]['l'], trimmed[-1]['c']) == \
                                (trimmed[-2]['o'], trimmed[-2]['h'], trimmed[-2]['l'], trimmed[-2]['c']):
        trimmed.pop()

    # 3. slice the week by timestamp
    wk = [b for b in trimmed if WEEK_START <= dt.datetime.fromisoformat(b['t']) < WEEK_END]

    # 4. continuity: within a week each bar's open should equal the prior bar's close
    breaks = []
    for i in range(1, len(wk)):
        if abs(wk[i]['o'] - wk[i - 1]['c']) > 1e-9:
            breaks.append((i, wk[i - 1]['t'], wk[i]['t'], round(wk[i]['o'] - wk[i - 1]['c'], 6)))

    # 5. bars per calendar day, from the timestamps themselves
    byday = collections.Counter(b['t'][:10] for b in wk)

    out[sym] = {'feed': d['feed'], 'interval': d['interval'], 'week_bars': wk,
                'breaks': breaks, 'by_day': dict(sorted(byday.items()))}
    print(f'{sym:8} {len(bars):5} {len(trimmed):6} {len(wk):5}  {wk[0]["t"]}   {wk[-1]["t"]}   {len(breaks)}')

print('\nbars per calendar day (UTC), read from timestamps:')
days = sorted({d for s in out.values() for d in s['by_day']})
print(f'{"pair":8} ' + ' '.join(f'{d[5:]:>6}' for d in days) + '   total')
for sym, s in out.items():
    row = ' '.join(f'{s["by_day"].get(d, 0):6d}' for d in days)
    print(f'{sym:8} {row}   {sum(s["by_day"].values()):5d}')

print('\ncontinuity breaks inside the week (open != previous close):')
for sym, s in out.items():
    if not s['breaks']:
        print(f'  {sym}: none')
    for b in s['breaks']:
        print(f'  {sym}: idx {b[0]}  {b[1]} -> {b[2]}  delta {b[3]}')

json.dump(out, open('v05_week.json', 'w'), indent=1)
print('\nWROTE v05_week.json')
