// tv_harvest_v05.mjs — harvest TIMESTAMPED OHLC bars from TradingView.
//
// Difference from V04's harvesters, and the reason this one exists:
// V04 captured OHLC only, so week and day boundaries had to be INFERRED from bar
// cadence. That inference is what broke on USDCHF (review R1, finding M1: its week
// opens with a partial 4h bar of twelve 15m bars, not sixteen). Here every bar is
// read together with its own Date and Time from TradingView's Data Window, so
// slicing by day or week is a lookup, not an assumption.
//
// Prices come from the Data Window's DOM text — the platform's own report of the bar.
// Nothing is read from a pixel or a colour.
//
// usage: node tv_harvest_v05.mjs SYMS INTERVAL OUT STOP_BEFORE_ISO [MAX_SCREENS]
import { chromium } from 'playwright';
import fs from 'fs';

const SYMS = process.argv[2].split(',');
const INTERVAL = process.argv[3];
const OUT = process.argv[4];
const STOP_BEFORE = process.argv[5];              // e.g. 2026-08-02
const MAX_SCREENS = Number(process.argv[6] || 14);

const MONTHS = { Jan: 1, Feb: 2, Mar: 3, Apr: 4, May: 5, Jun: 6, Jul: 7, Aug: 8, Sep: 9, Oct: 10, Nov: 11, Dec: 12 };

// "Mon 10 Aug '26" + "21:45"  ->  "2026-08-10T21:45"
function toIso(dateStr, timeStr) {
  const m = dateStr.match(/(\d{1,2})\s+([A-Za-z]{3})\s+'(\d{2})/);
  if (!m) return null;
  const [, d, mon, yy] = m;
  if (!MONTHS[mon]) return null;
  const t = (timeStr && /^\d{1,2}:\d{2}$/.test(timeStr.trim())) ? timeStr.trim().padStart(5, '0') : '00:00';
  return `20${yy}-${String(MONTHS[mon]).padStart(2, '0')}-${String(d).padStart(2, '0')}T${t}`;
}

const readDataWindow = () => {
  const el = [...document.querySelectorAll('.widgetbar-page')]
    .map(e => e.innerText || '').find(s => s.includes('Data window') && s.includes('Open'));
  return el || '';
};

const b = await chromium.launch({ channel: 'chrome' });
const ctx = await b.newContext({ viewport: { width: 1600, height: 900 } });
const p = await ctx.newPage();
const res = {};

for (const sym of SYMS) {
  await p.goto(`https://www.tradingview.com/chart/?symbol=FX%3A${sym}&interval=${INTERVAL}`,
    { waitUntil: 'domcontentloaded', timeout: 90000 });
  await p.waitForTimeout(13000);
  await p.keyboard.press('Alt+KeyD');            // open Data Window
  await p.waitForTimeout(2500);

  const bars = new Map();                        // iso -> [o,h,l,c]
  let feed = null, reachedStop = false;

  for (let s = 0; s < MAX_SCREENS && !reachedStop; s++) {
    for (let x = 1180; x >= 300; x -= 2) {
      await p.mouse.move(x, 420);
      await p.waitForTimeout(20);
      const txt = await p.evaluate(readDataWindow);
      if (!txt) continue;
      const t = txt.replace(/\n/g, ' ');
      const dm = t.match(/Date\s+(\w{3}\s+\d{1,2}\s+\w{3}\s+'\d{2})/);
      const tm = t.match(/Time\s+(\d{1,2}:\d{2})/);
      const om = t.match(/Open\s+([\d.]+)\s+High\s+([\d.]+)\s+Low\s+([\d.]+)\s+Close\s+([\d.]+)/);
      if (!dm || !om) continue;
      if (!feed) { const f = t.match(/·\s*[\w.]+\s*·\s*(\w+)/); if (f) feed = f[1]; }
      const iso = toIso(dm[1], tm ? tm[1] : null);
      if (!iso) continue;
      if (!bars.has(iso)) bars.set(iso, [+om[1], +om[2], +om[3], +om[4]]);
      if (iso < STOP_BEFORE) reachedStop = true;
    }
    if (reachedStop) break;
    await p.mouse.move(700, 420); await p.mouse.down();
    await p.mouse.move(1300, 420, { steps: 20 }); await p.mouse.up();
    await p.waitForTimeout(1600);
  }

  const sorted = [...bars.entries()].sort((a, b2) => a[0] < b2[0] ? -1 : 1);
  res[sym] = { feed, interval: INTERVAL, bars: sorted.map(([iso, o]) => ({ t: iso, o: o[0], h: o[1], l: o[2], c: o[3] })) };
  console.log(sym, 'bars:', sorted.length, 'feed:', feed,
    'range:', sorted.length ? `${sorted[0][0]} .. ${sorted[sorted.length - 1][0]}` : '-');
}

fs.writeFileSync(OUT, JSON.stringify(res, null, 1));
console.log('WROTE', OUT);
await ctx.close(); await b.close();
