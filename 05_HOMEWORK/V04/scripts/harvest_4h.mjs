import { chromium } from 'playwright';
import fs from 'fs';
const SYMS = process.argv[2].split(',');
const INTERVAL = process.argv[3];
const OUT = process.argv[4];
const XMIN = Number(process.argv[5]||260), XMAX = Number(process.argv[6]||1180);
const b = await chromium.launch({ channel: 'chrome' });
const ctx = await b.newContext({ viewport:{width:1600,height:900} });
const p = await ctx.newPage();
const res = {};
for (const sym of SYMS) {
  await p.goto(`https://www.tradingview.com/chart/?symbol=FX%3A${sym}&interval=${INTERVAL}`,{waitUntil:'domcontentloaded',timeout:90000});
  await p.waitForTimeout(11000);
  const seen=[]; let last=null;
  for (let x=XMAX; x>=XMIN; x-=2) {
    await p.mouse.move(x, 420);
    await p.waitForTimeout(75);
    const t = await p.evaluate(() => {
      const el=[...document.querySelectorAll('[class*="legend"]')].map(e=>e.innerText||'').find(s=>s.includes('O')&&s.includes('H')&&s.includes('L')&&s.includes('C'));
      return el||'';
    });
    const m = t.replace(/\n/g,' ').match(/O\s+([\d.]+)\s+H\s+([\d.]+)\s+L\s+([\d.]+)\s+C\s+([\d.]+)/);
    if(!m) continue;
    const bar=[+m[1],+m[2],+m[3],+m[4]];
    const key=bar.join(',');
    if(key!==last){ seen.push({bar,x}); last=key; }
  }
  seen.reverse();                       // oldest -> newest
  res[sym]={bars:seen.map(s=>s.bar), x:seen.map(s=>s.x)};
  console.log(sym, 'bars harvested:', seen.length);
  await p.screenshot({path:`tv_${sym}_${INTERVAL}.png`});
}
fs.writeFileSync(OUT, JSON.stringify(res,null,1));
console.log('WROTE', OUT);
await ctx.close(); await b.close();
