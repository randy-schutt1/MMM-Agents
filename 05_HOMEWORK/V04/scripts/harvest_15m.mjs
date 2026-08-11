import { chromium } from 'playwright';
import fs from 'fs';
const SYMS=process.argv[2].split(','), OUT=process.argv[3], SCREENS=Number(process.argv[4]||8);
const b=await chromium.launch({channel:'chrome'});
const ctx=await b.newContext({viewport:{width:1600,height:900}});
const p=await ctx.newPage();
const res={};
for(const sym of SYMS){
  await p.goto(`https://www.tradingview.com/chart/?symbol=FX%3A${sym}&interval=15`,{waitUntil:'domcontentloaded',timeout:90000});
  await p.waitForTimeout(11000);
  const all=[];  // newest-first accumulation
  for(let s=0; s<SCREENS; s++){
    let last=null;
    for(let x=1180;x>=280;x-=2){
      await p.mouse.move(x,420); await p.waitForTimeout(22);
      const t=await p.evaluate(()=>{const e=[...document.querySelectorAll('[class*="legend"]')].map(e=>e.innerText||'').find(s=>s.includes('O')&&s.includes('H'));return e||'';});
      const m=t.replace(/\n/g,' ').match(/O\s+([\d.]+)\s+H\s+([\d.]+)\s+L\s+([\d.]+)\s+C\s+([\d.]+)/);
      if(!m) continue;
      const bar=[+m[1],+m[2],+m[3],+m[4]], k=bar.join(',');
      if(k!==last){ all.push(bar); last=k; }
    }
    // pan back: drag chart to the right
    await p.mouse.move(700,420); await p.mouse.down();
    await p.mouse.move(1300,420,{steps:20}); await p.mouse.up();
    await p.waitForTimeout(1400);
  }
  // dedupe overlap, keep order newest->oldest
  const seenK=new Set(); const uniq=[];
  for(const bar of all){ const k=bar.join(','); if(!seenK.has(k)){ seenK.add(k); uniq.push(bar);} }
  uniq.reverse();  // oldest -> newest
  res[sym]=uniq;
  console.log(sym,'15m bars:',uniq.length);
}
fs.writeFileSync(OUT, JSON.stringify(res));
console.log('WROTE',OUT);
await ctx.close(); await b.close();
