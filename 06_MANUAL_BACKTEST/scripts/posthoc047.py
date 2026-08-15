"""POST-HOC, NOT PRE-REGISTERED. Disjoint-window re-measurement of PT-047.

The objection: HELD_ABOVE is DEFINED as "price did not close back below L in the
2 bars after t", and O1 is measured from t+1. The classifier's own bars are inside
the outcome window, so part of the observed gap is mechanical rather than predictive.

This re-measures O1 over t+3 .. t+16 ONLY -- strictly AFTER the 30-minute decision
is complete -- so the classifier window and the outcome window are disjoint.
"""
import sys, numpy as np
sys.path.insert(0,'.')
import mmm_lib as M
import run_pt047 as R

def cell(arm, win, cap, start_off):
    m15 = M.window(M.load_m15(arm), win)
    days = M.build_days(m15, offset_min=0, require_full=True)
    sd, mod = m15.sd, m15.mod
    post = (mod >= M.BOX_END_MIN) & (mod < M.DAY_END_MIN)
    held, back = [], []
    for day in sorted(set(days["sd"].tolist())):
        m = post & (sd == day)
        h,l,c = m15.h[m], m15.l[m], m15.c[m]
        n=len(h)
        if n < R.MIN_AGE+1+R.HORIZON: continue
        run_hi=-np.inf; anchor=-1
        for t in range(n):
            if run_hi>-np.inf:
                age=t-anchor
                if h[t]>run_hi and R.MIN_AGE<=age<=R.MAX_AGE and t+R.HORIZON<n:
                    L=float(run_hi)
                    cb=bool(np.any(c[t+1:t+1+cap]<L))
                    fwd=h[t+start_off:t+1+R.HORIZON]     # DISJOINT window
                    o1=max(0.0,(float(fwd.max())-L)/M.PIP)
                    (back if cb else held).append(o1)
                    break
            if h[t]>run_hi: run_hi=float(h[t]); anchor=t
    return np.array(held), np.array(back)

print("POST-HOC disjoint-window check: O1 measured over t+3..t+16 only (cap=2 bars)\n")
for arm in ("A","B"):
    for win in ("W-A","W-B"):
        held,back=cell(arm,win,2,3)
        d,p=R.perm_p(held,back)
        print(f"{arm}|{win}  nH={len(held):>3} nB={len(back):>3}  "
              f"medH={np.median(held):6.2f} medB={np.median(back):6.2f}  "
              f"Δ={d:6.2f}  p={p:.4f}")
