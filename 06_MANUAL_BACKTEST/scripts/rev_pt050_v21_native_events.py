"""REVIEWER: does a V21-NATIVE stop-hunt definition move the median MFE into [40,60]?

V21's own stop-hunt material is frame 16:40:
  "Hunt Stops! (as a collective) / Vary the Levels that these stops are triggered at! /
   Spike Past Support & Resistance/Pivots/Breakout levels/ Fib numbers"
So a V21-native event keys on SPIKING PAST A LEVEL. Four definitions are compared, all
measuring PT-050's Outcome A identically (MFE above L over t+1..t+16).
"""
import numpy as np, sys
sys.path.insert(0,'06_MANUAL_BACKTEST/scripts')
import mmm_lib as M
PIP=M.PIP; HORIZON=16; BAND=(40.,60.); GRID=(0,20,40)

def boot(x,seed=20260812,iters=20000):
    x=np.asarray(x,float); rng=np.random.default_rng(seed)
    idx=rng.integers(0,len(x),size=(iters,len(x)))
    m=np.median(x[idx],axis=1); return float(np.percentile(m,2.5)),float(np.percentile(m,97.5))

def cells(arm,win):
    b=M.load_m15(arm,"development"); t0,t1=M.WINDOWS[win]; b=b.slice(t0,t1)
    M.assert_development(b.tm,f"REV PT-050 {win}/{arm}")
    sd=M.session_day(b.tm); mod=M.minute_of_day(b.tm)
    post=(mod>=M.BOX_END_MIN)&(mod<M.DAY_END_MIN)
    box=(mod>=M.BOX_START_MIN)|(mod<M.BOX_END_MIN)     # 20:30 -> 03:00 Asian box
    days=sorted(set(sd.tolist()))
    ev={k:[] for k in ("PT047_borrowed","prev_day_high","asian_box_high","spike_qualified")}
    prev_high=None
    for d in days:
        mday=(sd==d)
        hp,lp=b.h[mday&post],b.l[mday&post]
        hb=b.h[mday&box]
        n=len(hp)
        if n < 8+1+HORIZON:
            if len(b.h[mday])>0: prev_high=float(b.h[mday].max())
            continue
        def emit(key,t,L):
            if t+HORIZON>=n: return
            fwd=hp[t+1:t+1+HORIZON]
            ev[key].append(max(0.0,(float(fwd.max())-L)/PIP))
        # (1) PT-047 borrowed: exceed a running day-high aged 8-24 bars
        run=-np.inf; anchor=-1
        for t in range(n):
            if run>-np.inf:
                age=t-anchor
                if hp[t]>run and 8<=age<=24 and t+HORIZON<n:
                    emit("PT047_borrowed",t,float(run)); break
            if hp[t]>run: run=float(hp[t]); anchor=t
        # (2) V21-native: first post-box bar spiking past the PREVIOUS DAY'S high (a pivot level)
        if prev_high is not None:
            for t in range(n):
                if hp[t]>prev_high:
                    emit("prev_day_high",t,prev_high); break
        # (3) V21-native: first post-box bar spiking past the ASIAN BOX high
        if len(hb)>0:
            bh=float(hb.max())
            for t in range(n):
                if hp[t]>bh:
                    emit("asian_box_high",t,bh); break
        # (4) PT-047 event but requiring the bar to be a SPIKE (range >= 1.5x trailing median)
        run=-np.inf; anchor=-1
        rng_=hp-lp
        for t in range(n):
            if run>-np.inf:
                age=t-anchor
                if hp[t]>run and 8<=age<=24 and t+HORIZON<n:
                    med=float(np.median(rng_[max(0,t-20):t])) if t>=5 else 0.0
                    if med>0 and rng_[t]>=1.5*med:
                        emit("spike_qualified",t,float(run)); break
            if hp[t]>run: run=float(hp[t]); anchor=t
        prev_high=float(b.h[mday].max())
    return ev

print("Outcome A = median MFE above L over t+1..t+16.  Pre-registered band [40,60].\n")
for arm,win in (("A","W-A"),("A","W-B")):
    ev=cells(arm,win)
    print(f"### {win} / arm {arm}")
    for k,v in ev.items():
        if len(v)<5: print(f"   {k:18s} n={len(v):4d}  (too few)"); continue
        med=float(np.median(v)); lo,hi=boot(v)
        inb=BAND[0]<=med<=BAND[1]
        star=" <-- PT-050's choice" if k=="PT047_borrowed" else ""
        print(f"   {k:18s} n={len(v):4d}  median={med:6.2f}  boot95=[{lo:6.2f},{hi:6.2f}]"
              f"  median in [40,60]? {str(inb):5s}{star}")
    print()
