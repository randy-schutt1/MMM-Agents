#!/usr/bin/env python3
"""Render the V06 homework charts FROM THE COMMITTED JSON. Not screenshots.

Applies only the DESCRIPTIVE half of what V06 shows:
  - day separators, placed at each day's first bar as read from that bar's own timestamp
  - each DAY's high and low, marked with the exact price from the harvested legend data
  - nothing else

It deliberately does NOT mark an anchor, a push, a level, a pattern, or an entry. Those
are guest NORMATIVE material and D-025 excludes them. The footer of every image says so
in the image itself, so a frame that escapes this directory carries its own provenance.

Also renders two measurement figures that ARE the V06 result:
  - the ADR family (5/10/14/20/30) per pair, showing how far the undefined lookback
    moves the answer (A-038)
  - the lesson's own two numbers on one scale: ADR/3 against the 25-50 pip band

usage: python3 render_v06.py M15.json DAILY.json OUTDIR WEEK_START WEEK_END
"""
import json
import os
import sys
from PIL import Image, ImageDraw

W, H = 1700, 760
PADL, PADR, PADT, PADB = 76, 132, 52, 66
BG, GRID, TXT = (22, 24, 30), (44, 48, 58), (226, 230, 238)
UP, DN, WICK = (78, 190, 128), (222, 88, 88), (150, 158, 172)
HI, LO, SEP, DIM = (255, 196, 84), (120, 190, 255), (70, 78, 92), (140, 146, 158)
LOOKBACKS = [5, 10, 14, 20, 30]
FOOTER = ('No anchor / push / level / pattern / entry marked: guest-normative, '
          'excluded under D-025.  Prices are TradingView FXCM Data Window text, '
          'never a pixel read.')


def dg(sym):
    return 3 if sym.endswith('JPY') else 5


def pip(sym):
    return 0.01 if sym.endswith('JPY') else 0.0001


def render_week(sym, bars, out):
    n = len(bars)
    lo = min(x['l'] for x in bars)
    hi = max(x['h'] for x in bars)
    pad = (hi - lo) * 0.08 or 1e-4
    lo -= pad
    hi += pad
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    pw = W - PADL - PADR
    ph = H - PADT - PADB

    def X(i):
        return PADL + (i + 0.5) * pw / n

    def Y(p):
        return PADT + ph * (hi - p) / (hi - lo)

    for k in range(7):
        p = lo + (hi - lo) * k / 6
        d.line([(PADL, Y(p)), (W - PADR, Y(p))], fill=GRID)
        d.text((6, Y(p) - 6), f'{p:.{dg(sym)}f}', fill=DIM)

    bw = max(1.0, pw / n * 0.62)
    byday = {}
    for i, b in enumerate(bars):
        byday.setdefault(b['t'][:10], []).append(i)
        col = UP if b['c'] >= b['o'] else DN
        x = X(i)
        d.line([(x, Y(b['h'])), (x, Y(b['l']))], fill=WICK)
        y0, y1 = Y(max(b['o'], b['c'])), Y(min(b['o'], b['c']))
        d.rectangle([x - bw / 2, y0, x + bw / 2, max(y1, y0 + 1)], fill=col)

    for day, idxs in sorted(byday.items()):
        i0 = idxs[0]
        d.line([(X(i0) - bw, PADT), (X(i0) - bw, H - PADB)], fill=SEP)
        # a partial session (the Sunday-open stub) is too narrow for a label on the
        # baseline, so stagger it down rather than let it collide with the next day's
        dy = 2 if len(idxs) >= 40 else 16
        d.text((X(i0) + 2, PADT + dy), f'{day}  {bars[i0]["t"][11:]}  n={len(idxs)}', fill=DIM)
        dh = max(idxs, key=lambda i: bars[i]['h'])
        dl = min(idxs, key=lambda i: bars[i]['l'])
        for i, key, col, tag in ((dh, 'h', HI, 'day high'), (dl, 'l', LO, 'day low')):
            p = bars[i][key]
            d.line([(X(idxs[0]) - bw, Y(p)), (X(idxs[-1]), Y(p))], fill=col)
            d.text((X(idxs[-1]) + 4, Y(p) - 6), f'{tag} {p:.{dg(sym)}f}', fill=col)

    rng = (max(x['h'] for x in bars) - min(x['l'] for x in bars)) / pip(sym)
    d.text((PADL, 12), f'{sym}  15m  {bars[0]["t"]} .. {bars[-1]["t"]}   '
                       f'{n} bars   week range {rng:.1f} pips', fill=TXT)
    d.text((PADL, H - 44), FOOTER, fill=DIM)
    d.text((PADL, H - 28), 'Marked: day separators (each day\'s own first bar) and each '
                           'day\'s high and low. Nothing else.', fill=DIM)
    im.save(out)
    return out


def bars_fig(title, rows, out, unit='pips', bands=None):
    """rows: list of (label, [(sublabel, value), ...])"""
    im = Image.new('RGB', (1500, 700), BG)
    d = ImageDraw.Draw(im)
    d.text((30, 18), title, fill=TXT)
    top, left = 74, 130
    colw = 250
    maxv = max(v for _, sub in rows for _, v in sub) * 1.15
    ph = 500
    for gi, (label, sub) in enumerate(rows):
        x0 = left + gi * colw
        d.text((x0, top + ph + 16), label, fill=TXT)
        bw = colw / (len(sub) + 1)
        for bi, (sl, v) in enumerate(sub):
            x = x0 + bi * bw
            y = top + ph - ph * v / maxv
            d.rectangle([x, y, x + bw * 0.78, top + ph], fill=(70, 120, 190))
            d.text((x, y - 14), f'{v:.0f}', fill=TXT)
            d.text((x, top + ph + 2), sl, fill=DIM)
    for k in range(6):
        v = maxv * k / 5
        y = top + ph - ph * k / 5
        d.line([(left - 10, y), (1470, y)], fill=GRID)
        d.text((30, y - 6), f'{v:.0f} {unit}', fill=DIM)
    if bands:
        for v, col, lab in bands:
            y = top + ph - ph * v / maxv
            d.line([(left - 10, y), (1470, y)], fill=col)
            d.text((1300, y - 14), lab, fill=col)
    d.text((30, 660), FOOTER, fill=DIM)
    im.save(out)
    return out


def main():
    m15_path, daily_path, outdir, wstart, wend = sys.argv[1:6]
    m15 = json.load(open(m15_path))
    daily = json.load(open(daily_path))
    os.makedirs(outdir, exist_ok=True)

    for sym, rec in m15.items():
        bars = [b for b in rec['bars'] if wstart <= b['t'][:10] <= wend]
        print(render_week(sym, bars, os.path.join(outdir, f'{sym}_15m_week_days_marked.png')),
              len(bars))

    # ADR family
    adr = {}
    for sym, rec in daily.items():
        bs = rec['bars']
        last = (bs[-1]['o'], bs[-1]['h'], bs[-1]['l'], bs[-1]['c'])
        i = len(bs) - 1
        while i > 0 and (bs[i-1]['o'], bs[i-1]['h'], bs[i-1]['l'], bs[i-1]['c']) == last:
            i -= 1
        bs = [b for b in bs[:i+1] if b['h'] > b['l']]
        adr[sym] = {n: sum((b['h']-b['l'])/pip(sym) for b in bs[-n:]) / n for n in LOOKBACKS}

    print(bars_fig('ADR by lookback window — the lookback the course has never defined (A-038)',
                   [(s, [(f'{n}d', adr[s][n]) for n in LOOKBACKS]) for s in adr],
                   os.path.join(outdir, 'adr_family.png')))

    print(bars_fig('"Each push is approximately ADR divided by 3" vs "pullbacks are usually '
                   '25 to 50 pips" — ARITHMETIC ONLY, not a test of a rule',
                   [(s, [(f'{n}d/3', adr[s][n]/3) for n in LOOKBACKS]) for s in adr],
                   os.path.join(outdir, 'push_size_vs_pullback_band.png'),
                   bands=[(25, (255, 196, 84), '25 pips'), (50, (222, 88, 88), '50 pips')]))


if __name__ == '__main__':
    main()
