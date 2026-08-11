# V05 homework scripts

Three scripts, run in this order. All are committed so every number in
`../V05_HOMEWORK.md` can be recomputed from the committed data.

```bash
# 1. harvest — TIMESTAMPED bars from TradingView's Data Window (DOM text, never pixels)
node tv_harvest_v05.mjs EURUSD,GBPUSD,USDJPY,USDCHF 15 v05_15m.json 2026-08-02 14

# 2. validate + slice one complete trading week, by timestamp
python3 slice_week.py            # reads v05_15m.json -> writes v05_week.json

# 3. render the marked charts and flashcard crops from the sliced data
python3 render_charts.py         # reads v05_week.json -> writes charts/
```

## Why this harvester exists rather than V04's

`05_HOMEWORK/V04/scripts/harvest_4h.mjs` and `harvest_15m.mjs` capture `O H L C` only.
Without timestamps a week boundary has to be **inferred** from bar cadence, and V04 review
R1 finding `M1` showed that inference failing on USDCHF, whose week opens with a partial
4-hour bar. Four previous-week bars were pushed onto the head of the committed slice and
the symptom was misread as harvest noise.

`tv_harvest_v05.mjs` opens TradingView's **Data Window** (`Alt+D`) and reads `Date`,
`Time`, `Open`, `High`, `Low`, `Close` together for every hovered bar. Week and day
boundaries become a lookup. Running it on the 2026-08-02 week reports USDCHF's 22:00 open
and its 476-bar week directly — the same condition, surfaced instead of silently absorbed.

## Two behaviours worth knowing before re-running

- **Live-edge artifact.** Hovering past the last real bar makes TradingView report the
  still-forming bar's OHLC for every projected future slot, so the harvest ends in a run of
  rows with distinct timestamps and identical OHLC. `slice_week.py` drops that trailing run.
  Harvest a *complete past* week and none of the analysed bars is affected.
- **Chart timezone.** Times are the chart's own, which was **UTC** for this harvest (the
  platform clock is visible in the legend probe). A chart set to another timezone would
  shift every timestamp and therefore the day slicing. `A-019` — the course never states a
  timezone — is still open, so this is a property of the harvest, not of the method.

`render_charts.py` marks only day separators, the week high/low and body-to-body boxes at
those extremes. It does **not** mark levels, an anchor or any entry: those are guest
normative material, excluded under `DECISIONS.md` D-025. See `../V05_HOMEWORK.md` header.
