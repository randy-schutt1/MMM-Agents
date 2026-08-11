#!/usr/bin/env python3
"""Render the V05 homework charts FROM THE COMMITTED JSON. Not screenshots.

Applies only the DESCRIPTIVE half of V05's markup procedure:
  - day separators, placed at each day's first bar as read from that bar's own timestamp
  - the week high and the week low, which are INSTRUCTOR-sourced objects (V04 [00:18:24]),
    marked with the exact prices from the harvested legend data
  - body-to-body consolidation boxes at those extremes, per the guest's stated convention
    (wicks left outside, V05 [00:56:11]-[00:56:27])
  - the flashcard crop: cut at the decision candle, nothing to its right (V05 [00:31:04])

It deliberately does NOT assign Level 1/2/3, an anchor, or any entry. Those are guest
NORMATIVE material and D-025 excludes them.
"""
import json, datetime as dt, os
from PIL import Image, ImageDraw

W, H = 1600, 720
PADL, PADR, PADT, PADB = 70, 110, 46, 58
BG, GRID, TXT = (22, 24, 30), (44, 48, 58), (226, 230, 238)
UP, DN, WICK = (78, 190, 128), (222, 88, 88), (150, 158, 172)
HI, LO, BOX, SEP = (255, 196, 84), (120, 190, 255), (255, 150, 60), (70, 78, 92)

D = json.load(open('v05_week.json'))
os.makedirs('charts', exist_ok=True)


def digits(sym):
    return 3 if sym.endswith('JPY') else 5


def pip(sym):
    return 0.01 if sym.endswith('JPY') else 0.0001


def render(sym, bars, out, crop_to=None, title_extra=''):
    b = bars if crop_to is None else bars[:crop_to + 1]
    n = len(b)
    lo = min(x['l'] for x in b); hi = max(x['h'] for x in b)
    pad = (hi - lo) * 0.08 or 1e-4
    lo -= pad; hi += pad
    pw, ph = W - PADL - PADR, H - PADT - PADB
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    X = lambda i: PADL + (i + 0.5) * pw / n
    Y = lambda p: PADT + (hi - p) * ph / (hi - lo)

    # price grid
    for k in range(7):
        p = lo + (hi - lo) * k / 6
        y = Y(p)
        d.line([(PADL, y), (PADL + pw, y)], fill=GRID)
        d.text((6, y - 6), f'{p:.{digits(sym)}f}', fill=(140, 148, 162))

    # day separators, from each bar's own timestamp
    seen, dayno = set(), 0
    for i, x in enumerate(b):
        day = x['t'][:10]
        if day not in seen:
            seen.add(day); dayno += 1
            if i:
                d.line([(X(i), PADT), (X(i), PADT + ph)], fill=SEP)
            wd = dt.datetime.fromisoformat(x['t']).strftime('%a')
            # stagger so a short first day (Sunday open) cannot collide with Monday's label
            ly = PADT + 4 + 13 * (dayno % 2)
            d.text((X(i) + 4, ly), f'D{dayno} {wd} {day[5:]} open {x["t"][11:]}', fill=(150, 158, 172))

    cw = max(1.0, pw / n * 0.62)
    for i, x in enumerate(b):
        col = UP if x['c'] >= x['o'] else DN
        cx = X(i)
        d.line([(cx, Y(x['h'])), (cx, Y(x['l']))], fill=WICK)
        y0, y1 = Y(max(x['o'], x['c'])), Y(min(x['o'], x['c']))
        if y1 - y0 < 1: y1 = y0 + 1
        d.rectangle([cx - cw / 2, y0, cx + cw / 2, y1], fill=col)

    # week high / low -- instructor-sourced objects
    ih = max(range(n), key=lambda i: b[i]['h']); il = min(range(n), key=lambda i: b[i]['l'])
    for idx, price, col, lab in ((ih, b[ih]['h'], HI, 'WEEK HIGH'), (il, b[il]['l'], LO, 'WEEK LOW')):
        y = Y(price)
        d.line([(PADL, y), (PADL + pw, y)], fill=col)
        d.text((PADL + pw + 6, y - 6), f'{lab}\n{price:.{digits(sym)}f}\n{b[idx]["t"][5:]}', fill=col)
        # body-to-body box around the extreme: wicks left outside (guest convention)
        s, e = max(0, idx - 6), min(n - 1, idx + 6)
        bt = max(max(x['o'], x['c']) for x in b[s:e + 1])
        bb = min(min(x['o'], x['c']) for x in b[s:e + 1])
        d.rectangle([X(s) - cw, Y(bt), X(e) + cw, Y(bb)], outline=BOX)

    rng = (b[ih]['h'] - b[il]['l']) / pip(sym)
    d.text((PADL, 10), f'{sym}  15M  FXCM   {b[0]["t"]} -> {b[-1]["t"]} UTC   '
                       f'{n} bars   range {rng:.1f} pips{title_extra}', fill=TXT)
    d.text((PADL, H - 30), 'Rendered from committed JSON (TradingView Data Window text). '
                           'No Level/anchor/entry marked: guest-normative, excluded under D-025.',
           fill=(120, 128, 142))
    im.save(out)
    return ih, il, rng


summary = {}
for sym, s in D.items():
    bars = s['week_bars']
    ih, il, rng = render(sym, bars, f'charts/{sym}_15m_week_marked.png')
    # flashcard crops: cut AT the decision candle, nothing to its right
    render(sym, bars, f'charts/{sym}_15m_flashcard_week-high.png', crop_to=ih,
           title_extra='   FLASHCARD: cut at the week-high candle')
    render(sym, bars, f'charts/{sym}_15m_flashcard_week-low.png', crop_to=il,
           title_extra='   FLASHCARD: cut at the week-low candle')
    summary[sym] = {
        'bars': len(bars), 'first': bars[0]['t'], 'last': bars[-1]['t'],
        'week_high': bars[ih]['h'], 'week_high_at': bars[ih]['t'], 'week_high_idx': ih,
        'week_low': bars[il]['l'], 'week_low_at': bars[il]['t'], 'week_low_idx': il,
        'range_pips': round(rng, 1), 'breaks': len(s['breaks']),
    }
    print(f'{sym:8} {len(bars):4} bars  high {bars[ih]["h"]} @ {bars[ih]["t"]}  '
          f'low {bars[il]["l"]} @ {bars[il]["t"]}  range {rng:7.1f} pips')

json.dump(summary, open('charts/summary.json', 'w'), indent=1)
print('\nWROTE charts/ (12 images) + summary.json')
