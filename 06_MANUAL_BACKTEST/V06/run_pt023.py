#!/usr/bin/env python3
"""PT-023 runner — "They don't usually run like London".

Pre-registration: 06_MANUAL_BACKTEST/PRE_REGISTERED/PT-023_new_york_does_not_run_like_london_reissue.md
(and PT-022, which PT-023 re-issues and which governs everything not restated there).

Executes, in the order the pre-registration fixes:

  1. Live-edge trim; compute the D-028 70/30 boundary from the actual available range.
  2. Slice DEVELOPMENT. The HOLDOUT is never touched, not even to count bars.
  3. Build per-day London and New York window ranges, in BOTH D-031 arms.
  4. Run the two nulls (N-P sign-flip, N2 circular clock shift) FIRST.
  5. Only then read the rule arm's aggregate.

No price is read from a pixel: the input JSON is the platform's own Data Window text,
harvested by tv_harvest_v06.mjs.

usage: python3 run_pt023.py HARVEST.json [--out results.json]
"""
import json
import random
import sys
from datetime import datetime, timedelta

PIP = 1e-4                       # GBP/USD, per COMMON_PROTOCOL §1
SEED = 20260812                  # pre-registered, COMMON_PROTOCOL §5
ITERS = 1000
LONDON = (3.5, 9.0)              # 03:30-09:00, V02 printed table
NEWYORK = (9.5, 17.0)            # 09:30-17:00
ARMS = {'A (fixed UTC-5)': 5, 'B (America/New_York, DST)': 4}


def drop_live_edge(bars):
    if not bars:
        return bars, 0
    last = (bars[-1]['o'], bars[-1]['h'], bars[-1]['l'], bars[-1]['c'])
    i = len(bars) - 1
    while i > 0 and (bars[i-1]['o'], bars[i-1]['h'], bars[i-1]['l'], bars[i-1]['c']) == last:
        i -= 1
    return bars[:i+1], len(bars) - (i+1)


def hourfrac(dt):
    return dt.hour + dt.minute / 60.0


def day_windows(bars, shift_hours, w1, w2):
    """Return {date: (range_w1, range_w2)} for days where BOTH windows have >=1 bar."""
    buckets = {}
    for b in bars:
        t = datetime.fromisoformat(b['t']) - timedelta(hours=shift_hours)
        d = t.date()
        h = hourfrac(t)
        for key, (lo, hi) in (('w1', w1), ('w2', w2)):
            if lo <= h < hi:
                s = buckets.setdefault(d, {})
                e = s.setdefault(key, [b['h'], b['l']])
                e[0] = max(e[0], b['h'])
                e[1] = min(e[1], b['l'])
    out = {}
    for d, s in buckets.items():
        if 'w1' in s and 'w2' in s:
            out[d] = ((s['w1'][0] - s['w1'][1]) / PIP, (s['w2'][0] - s['w2'][1]) / PIP)
    return out, buckets


def frac_pos(ds):
    return sum(1 for d in ds if d > 0) / len(ds)


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    den = 1 + z*z/n
    c = (p + z*z/(2*n)) / den
    half = z * ((p*(1-p)/n + z*z/(4*n*n)) ** 0.5) / den
    return (max(0.0, c-half), min(1.0, c+half))


def pct_of(value, dist):
    dist = sorted(dist)
    below = sum(1 for v in dist if v < value)
    return 100.0 * below / len(dist)


def q(dist, p):
    dist = sorted(dist)
    return dist[min(len(dist)-1, int(p*len(dist)))]


def main():
    path = sys.argv[1]
    out_path = sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else None
    raw = json.load(open(path))
    sym = 'GBPUSD'
    if 'chart' in raw:                      # Yahoo Finance response (PT-024)
        r0 = raw['chart']['result'][0]
        q0 = r0['indicators']['quote'][0]
        bs = []
        for i, ts in enumerate(r0['timestamp']):
            if q0['open'][i] is None:
                continue
            ts -= ts % 1800
            bs.append({'t': datetime.utcfromtimestamp(ts).isoformat(timespec='minutes'),
                       'o': q0['open'][i], 'h': q0['high'][i],
                       'l': q0['low'][i], 'c': q0['close'][i]})
        seen = {}
        for b in bs:
            seen[b['t']] = b            # de-duplicate the 30m grid
        rec = {'feed': 'Yahoo Finance chart API', 'interval': '30',
               'bars': [seen[k] for k in sorted(seen)]}
    else:
        rec = raw[sym]
    bars, dropped = drop_live_edge(rec['bars'])
    bars = sorted(bars, key=lambda b: b['t'])

    print('=' * 78)
    print('STEP 1 — SOURCE, LIVE-EDGE TRIM, AND THE D-028 BOUNDARY')
    print('=' * 78)
    print(f'symbol={sym}  feed={rec["feed"]}  interval={rec["interval"]}m')
    print(f'raw bars={len(rec["bars"])}  live-edge dropped={dropped}  usable={len(bars)}')
    T0 = datetime.fromisoformat(bars[0]['t'])
    T1 = datetime.fromisoformat(bars[-1]['t'])
    print(f'T0={T0}  T1={T1}  span={(T1-T0).days} days')
    B = T0 + (T1 - T0) * 0.70
    B = B.replace(hour=0, minute=0, second=0, microsecond=0)
    print(f'D-028 boundary B = T0 + 0.70*(T1-T0), floored to the day = {B}')
    dev = [b for b in bars if datetime.fromisoformat(b['t']) < B]
    print(f'DEVELOPMENT bars = {len(dev)}  ({dev[0]["t"]} .. {dev[-1]["t"]})')
    print('HOLDOUT: NOT OPENED. Not sliced, not counted, not inspected.')

    rng = random.Random(SEED)
    results = {'T0': str(T0), 'T1': str(T1), 'B': str(B), 'dev_bars': len(dev),
               'seed': SEED, 'iters': ITERS, 'arms': {}}

    for arm, shift in ARMS.items():
        print()
        print('=' * 78)
        print(f'ARM {arm}  —  chart clock minus {shift}h')
        print('=' * 78)
        days, _ = day_windows(dev, shift, LONDON, NEWYORK)
        dates = sorted(days)
        n = len(dates)
        D = [days[d][0] - days[d][1] for d in dates]
        Dn = [days[d][0]/5.5 - days[d][1]/7.5 for d in dates]

        # ---- NULLS FIRST (COMMON_PROTOCOL §9 integrity rule 1) ----
        r = random.Random(SEED)
        np_dist = []
        for _ in range(ITERS):
            flipped = [d if r.random() < 0.5 else -d for d in D]
            np_dist.append(frac_pos(flipped))
        r2 = random.Random(SEED)
        n2_dist = []
        for _ in range(ITERS):
            off = r2.randrange(-48, 49) * 0.25          # +/-12h in 15-min steps
            w1 = ((LONDON[0]+off) % 24, (LONDON[0]+off) % 24 + 5.5)
            w2 = ((NEWYORK[0]+off) % 24, (NEWYORK[0]+off) % 24 + 7.5)
            dd, _ = day_windows(dev, shift, w1, w2)
            if len(dd) >= 5:
                vals = [v[0]-v[1] for v in dd.values()]
                n2_dist.append(frac_pos(vals))
        print(f'NULLS (run before the rule arm was read).  seed={SEED}  iters={ITERS}')
        print(f'  N-P sign-flip     : median f={q(np_dist,0.50):.3f}  '
              f'5-95% [{q(np_dist,0.05):.3f}, {q(np_dist,0.95):.3f}]')
        print(f'  N2 clock shift    : median f={q(n2_dist,0.50):.3f}  '
              f'5-95% [{q(n2_dist,0.05):.3f}, {q(n2_dist,0.95):.3f}]  (n={len(n2_dist)})')

        # ---- RULE ARM ----
        f = frac_pos(D)
        k = sum(1 for d in D if d > 0)
        lo, hi = wilson(k, n)
        med = sorted(D)[n//2]
        fn = frac_pos(Dn)
        medn = sorted(Dn)[n//2]
        print()
        print(f'RULE ARM  n={n} included days')
        print(f'  O1  raw   : median D = {med:+.1f} pips   mean = {sum(D)/n:+.1f}   '
              f'f(D>0) = {f:.3f}  ({k}/{n})  95% CI [{lo:.3f}, {hi:.3f}]')
        print(f'  O1b norm  : median Dn = {medn:+.2f} pips/h   f(Dn>0) = {fn:.3f}')
        print(f'  percentile of f within N-P : {pct_of(f, np_dist):.1f}')
        print(f'  percentile of f within N2  : {pct_of(f, n2_dist):.1f}')

        ny = [days[d][1] for d in dates]
        ge30 = sum(1 for v in ny if v >= 30) / n
        ge50 = sum(1 for v in ny if v >= 50) / n
        l30, h30 = wilson(sum(1 for v in ny if v >= 30), n)
        l50, h50 = wilson(sum(1 for v in ny if v >= 50), n)
        print(f'  O2  NY range >=30p: {ge30:.3f}  95% CI [{l30:.3f}, {h30:.3f}]')
        print(f'      NY range >=50p: {ge50:.3f}  95% CI [{l50:.3f}, {h50:.3f}]')
        print(f'      median NY range {sorted(ny)[n//2]:.1f} pips   '
              f'median London range {sorted([days[d][0] for d in dates])[n//2]:.1f} pips')

        # ---- verdict per the pre-registered decision rules ----
        conf = med > 0 and pct_of(f, np_dist) > 95 and pct_of(f, n2_dist) > 95
        contra = med < 0 or (pct_of(f, np_dist) < 5 and pct_of(f, n2_dist) < 5)
        v = 'SAMPLE INSUFFICIENT' if n < 30 else (
            'CONFIRMED AS TAUGHT' if conf else
            'CONTRADICTED AS TAUGHT' if contra else 'INDISTINGUISHABLE FROM THE NULL')
        print(f'  ARM VERDICT: {v}')
        results['arms'][arm] = {
            'n': n, 'median_D': med, 'mean_D': sum(D)/n, 'f': f, 'ci': [lo, hi],
            'median_Dn': medn, 'f_norm': fn,
            'pct_NP': pct_of(f, np_dist), 'pct_N2': pct_of(f, n2_dist),
            'NP_5_50_95': [q(np_dist,0.05), q(np_dist,0.50), q(np_dist,0.95)],
            'N2_5_50_95': [q(n2_dist,0.05), q(n2_dist,0.50), q(n2_dist,0.95)],
            'ny_ge30': ge30, 'ny_ge50': ge50,
            'median_ny': sorted(ny)[n//2],
            'median_london': sorted([days[d][0] for d in dates])[n//2],
            'verdict': v}

    print()
    print('=' * 78)
    vs = {a: r['verdict'] for a, r in results['arms'].items()}
    print(f'BOTH ARMS: {vs}')
    print('Both arms are reported. Divergence is a finding, never a selection (D-031).')
    if out_path:
        json.dump(results, open(out_path, 'w'), indent=1)
        print(f'WROTE {out_path}')


if __name__ == '__main__':
    main()
