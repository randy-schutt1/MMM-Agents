#!/usr/bin/env python3
"""V06 homework measurements — the ADMISSIBLE half only.

Everything here is arithmetic over TradingView's own reported OHLC (harvested from the
platform's Data Window DOM text by tv_harvest_v06.mjs — no pixel is read, no colour is
detected). Nothing here applies a guest construct: no anchor, no push, no level, no
pattern, no entry. See V06_HOMEWORK.md for why.

Outputs, all to stdout as a report plus a JSON summary:

  1. Live-edge trim and continuity/bar-count verification, per pair.
  2. ADR over a FAMILY of lookbacks (5/10/14/20/30) and ADR/3, per pair.
     A family, not a value: the course has never defined ADR's lookback (A-038) and
     D-030 forbids inventing one to make a blocked measurement runnable.
  3. Realised daily range vs each ADR estimate.
  4. The lesson's two numbers put on one scale: is "ADR/3" the same size as
     "25 to 50 pips"? Arithmetic on the lesson's own figures; NOT a test of a rule.
  5. Per-day intraday extremes and their clock times under BOTH D-031 timezone arms.

usage: python3 measure_v06.py DAILY.json M15.json WEEK_START WEEK_END [--json OUT]
       dates are inclusive ISO dates bounding the 15m week, e.g. 2026-08-02 2026-08-07
"""
import json
import sys
from datetime import datetime, timedelta

PIP = {'EURUSD': 0.0001, 'GBPUSD': 0.0001, 'USDCHF': 0.0001, 'USDJPY': 0.01,
       'AUDUSD': 0.0001, 'USDCAD': 0.0001, 'EURJPY': 0.01}
LOOKBACKS = [5, 10, 14, 20, 30]


def drop_live_edge(bars):
    """Trailing rows with distinct timestamps and identical OHLC are the platform
    reporting the still-forming bar for every projected future slot. V05 documented
    this; the same trim is applied here."""
    if not bars:
        return bars, 0
    n = len(bars)
    last = (bars[-1]['o'], bars[-1]['h'], bars[-1]['l'], bars[-1]['c'])
    i = n - 1
    while i > 0 and (bars[i - 1]['o'], bars[i - 1]['h'],
                     bars[i - 1]['l'], bars[i - 1]['c']) == last:
        i -= 1
    return bars[:i + 1], n - (i + 1)


def pips(sym, x):
    return x / PIP[sym]


def main():
    daily_path, m15_path, wstart, wend = sys.argv[1:5]
    out_json = None
    if '--json' in sys.argv:
        out_json = sys.argv[sys.argv.index('--json') + 1]

    daily = json.load(open(daily_path))
    m15 = json.load(open(m15_path))
    summary = {}

    print('=' * 78)
    print('SECTION 1 — LIVE-EDGE TRIM AND VERIFICATION')
    print('=' * 78)
    dcl = {}
    for sym, rec in daily.items():
        bars, dropped = drop_live_edge(rec['bars'])
        # a daily bar with zero range is not a traded day on this feed
        bars = [b for b in bars if b['h'] > b['l']]
        dcl[sym] = bars
        print(f'{sym:8s} feed={rec["feed"]:6s} raw={len(rec["bars"]):4d} '
              f'live-edge dropped={dropped:3d} usable={len(bars):4d} '
              f'range {bars[0]["t"][:10]} .. {bars[-1]["t"][:10]}')

    print()
    print('=' * 78)
    print('SECTION 2 — ADR FAMILY (no single value is adopted: A-038, D-030)')
    print('=' * 78)
    print(f'{"pair":8s} ' + ' '.join(f'ADR{n:<3d}' for n in LOOKBACKS)
          + '   | ' + ' '.join(f'/3@{n:<3d}' for n in LOOKBACKS))
    adr = {}
    for sym, bars in dcl.items():
        adr[sym] = {}
        for n in LOOKBACKS:
            window = bars[-n:]
            v = sum(pips(sym, b['h'] - b['l']) for b in window) / len(window)
            adr[sym][n] = v
        print(f'{sym:8s} ' + ' '.join(f'{adr[sym][n]:6.1f}' for n in LOOKBACKS)
              + '   | ' + ' '.join(f'{adr[sym][n]/3:6.1f}' for n in LOOKBACKS))
    summary['adr'] = adr

    print()
    print('SPREAD OF THE FAMILY — how much the undefined lookback moves the answer:')
    for sym in dcl:
        vs = [adr[sym][n] for n in LOOKBACKS]
        lo, hi = min(vs), max(vs)
        print(f'  {sym:8s} ADR {lo:6.1f} .. {hi:6.1f} pips  (spread {hi-lo:5.1f}, '
              f'{100*(hi-lo)/lo:4.1f}% of the smallest)   ADR/3 {lo/3:5.1f} .. {hi/3:5.1f}')

    print()
    print('=' * 78)
    print("SECTION 3 — THE LESSON'S TWO NUMBERS ON ONE SCALE")
    print('=' * 78)
    print('V06 [00:05:45]  "Each push is approximately ADR divided by 3."')
    print('V06 [00:06:04]  "The pull marks [pullbacks] are usually 25 to 50 pips."')
    print('V06 [00:06:19]  a 10-15 pip channel is "not really pulling it back".')
    print()
    print('ARITHMETIC ONLY. This is the lesson\'s own two figures compared to each')
    print('other on measured data. It is NOT a test of a rule and NOT evidence for or')
    print('against one (D-025 excludes the rule; D-030 forbids substituting a')
    print('definition to make a blocked test runnable).')
    print()
    print(f'{"pair":8s} {"ADR20":>7s} {"ADR20/3":>8s} {"pullback band as % of ADR20/3":>34s}')
    ratio = {}
    for sym in dcl:
        a = adr[sym][20]
        ratio[sym] = {'adr20': a, 'push': a / 3,
                      'pb_lo_pct': 100 * 25 / (a / 3), 'pb_hi_pct': 100 * 50 / (a / 3)}
        print(f'{sym:8s} {a:7.1f} {a/3:8.1f} '
              f'{"25 pips = " + format(100*25/(a/3), ".0f") + "%":>17s}'
              f'{"  50 pips = " + format(100*50/(a/3), ".0f") + "%":>17s}')
    summary['scale'] = ratio

    print()
    print('=' * 78)
    print('SECTION 4 — THE 15-MINUTE WEEK: BAR COUNTS AND CONTINUITY')
    print('=' * 78)
    print('Bar counts are VERIFIED against expectation rather than assumed. V04 review R1')
    print('and V05 both found USDCHF short by exactly one hour at the week open.')
    wk = {}
    for sym, rec in m15.items():
        bars, dropped = drop_live_edge(rec['bars'])
        sel = [b for b in bars if wstart <= b['t'][:10] <= wend]
        wk[sym] = sel
        breaks = sum(1 for a, b in zip(sel, sel[1:]) if abs(a['c'] - b['o']) > 1e-9)
        byday = {}
        for b in sel:
            byday[b['t'][:10]] = byday.get(b['t'][:10], 0) + 1
        print(f'{sym:8s} bars={len(sel):4d}  first={sel[0]["t"]}  last={sel[-1]["t"]}  '
              f'continuity breaks={breaks}/{max(0,len(sel)-1)}')
        print(f'{"":8s} per-day: ' + '  '.join(f'{d[5:]}={c}' for d, c in sorted(byday.items())))
    summary['week_bars'] = {s: len(b) for s, b in wk.items()}

    print()
    print('=' * 78)
    print('SECTION 5 — DAILY EXTREMES AND THEIR CLOCK TIMES, BOTH D-031 ARMS')
    print('=' * 78)
    print('Arm A = fixed UTC-5 ("EST", no DST).  Arm B = America/New_York with DST')
    print('(UTC-4 in August).  BOTH are reported, always; divergence is a finding and')
    print('never a selection criterion (D-031).')
    print('Feed timestamps are treated as the chart\'s own clock; the two arms differ by')
    print('exactly one hour, so Arm B = Arm A + 1h.')
    print()
    extremes = {}
    for sym, sel in wk.items():
        extremes[sym] = []
        byday = {}
        for b in sel:
            byday.setdefault(b['t'][:10], []).append(b)
        print(f'-- {sym}')
        for d, bs in sorted(byday.items()):
            hi = max(bs, key=lambda b: b['h'])
            lo = min(bs, key=lambda b: b['l'])
            rng = pips(sym, hi['h'] - lo['l'])
            def arms(t):
                dt = datetime.fromisoformat(t)
                return (dt - timedelta(hours=5)).strftime('%H:%M'), \
                       (dt - timedelta(hours=4)).strftime('%H:%M')
            ha, hb = arms(hi['t'])
            la, lb = arms(lo['t'])
            n = len(bs)
            print(f'   {d}  bars={n:3d}  range={rng:6.1f}p   '
                  f'high {hi["h"]:>9} at {hi["t"][11:]} (A {ha} / B {hb})   '
                  f'low {lo["l"]:>9} at {lo["t"][11:]} (A {la} / B {lb})')
            extremes[sym].append({'date': d, 'bars': n, 'range_pips': round(rng, 1),
                                  'high': hi['h'], 'high_t': hi['t'],
                                  'low': lo['l'], 'low_t': lo['t']})
    summary['extremes'] = extremes

    print()
    print('=' * 78)
    print('SECTION 6 — REALISED DAILY RANGE vs ADR')
    print('=' * 78)
    print('Descriptive. How the week\'s actual ranges sit against each ADR estimate.')
    for sym, days in extremes.items():
        # skip partial boundary days (a Sunday open stub or a Friday close stub)
        full = [d for d in days if d['bars'] >= 90]
        if not full:
            continue
        avg = sum(d['range_pips'] for d in full) / len(full)
        print(f'{sym:8s} full days n={len(full)}  mean realised range={avg:6.1f}p   '
              + '  '.join(f'ADR{n}={adr[sym][n]:5.1f}' for n in LOOKBACKS))
    if out_json:
        json.dump(summary, open(out_json, 'w'), indent=1)
        print(f'\nWROTE {out_json}')


if __name__ == '__main__':
    main()
