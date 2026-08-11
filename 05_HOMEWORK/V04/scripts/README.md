# V04 homework — measurement scripts

Committed so the numbers in `V04_HOMEWORK.md` are reproducible by someone who was not
here. This discharges for V04 the promise `REVIEW_INDEX.md` open item 13 records against
V02 (*"§1.1 promises a reproducible method and commits no script"*).

| File | What it does |
|---|---|
| `harvest_4h.mjs` | Drives a public TradingView chart with Playwright, hovers across the price pane, and parses the platform's own **OHLC legend as DOM text**. No login, no account, no paywalled feature. |
| `harvest_15m.mjs` | Same, at the 15-minute interval, panning the chart back by drag to accumulate ~860 bars per pair. |
| `verify_reconstruction.py` | Recomputes `V04_HOMEWORK.md` §1.2 validation 3 from the committed JSON alone — the 15m → 4h reconstruction (116/120 bars, 476/480 fields), the per-pair partial-first-bar length, and the absence of any in-week 15m discontinuity. Added 2026-08-11 while remediating review R1 `M1`. Exits non-zero on mismatch. |

```bash
node harvest_4h.mjs  EURUSD,GBPUSD,USDJPY,USDCHF 240 out_4h.json
node harvest_15m.mjs EURUSD,GBPUSD,USDJPY,USDCHF     out_15m.json 9
```

**No price is read from a pixel.** Every number is the platform's own text report of the
hovered bar. This is the V02 `E06`/`MAJOR` lesson applied (a price line rendered in the
same colour as bullish candles corrupted a pixel-based read).

**Known limitation, measured rather than assumed.** The legend updates asynchronously, so
a short hover dwell can occasionally latch a stale high/low. `harvest_4h.mjs` was run at a
28 ms dwell and again at 75 ms; the two runs disagreed on **5 of 480** OHLC fields, all in
highs/lows, never in opens or closes. The 75 ms run is the committed one and it is the one
that agrees with V03's independently committed dataset on 476/480 fields. See
`V04_HOMEWORK.md` §1.3.

**A second limitation, found by review R1 (`M1`, `E19`) and corrected 2026-08-11.**
`harvest_15m.mjs` slices a calendar week by a fixed **sixteen 15m bars per 4h bar**. That
assumption is **false for USDCHF on this feed**, whose first 4h bar of the week holds only
**twelve** — the pair quotes an hour later than the other majors. The committed slice
therefore carried four previous-week bars at its head, putting the weekend gap inside the
"week". The data is re-sliced and every pair now carries an explicit
`bars_15m_in_4h_bar_0` field. **A future session reusing this harvester must not assume 16**;
derive the first-bar length per pair and assert zero in-week discontinuities before
trusting the slice. `verify_reconstruction.py` performs both checks.
