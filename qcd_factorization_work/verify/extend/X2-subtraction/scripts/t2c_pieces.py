import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, warnings
warnings.filterwarnings('ignore')
from t2b_norm_fast import run
for (P, Pp) in [(1/np.sqrt(2), 1/np.sqrt(2)), (0.8, 1/(2*0.8))]:
    print(f"P={P:.4f} P'={Pp:.4f}  (Qt^2=2PP'={2*P*Pp:.3f})")
    for k in [4, 6, 8]:
        lam2 = 10.0**(-k); L = np.log(1/lam2)
        tot, nrm, ex, sl, sla, slG, pcs = run(P, Pp, lam2)
        print(f" lam2=1e-{k}: total {tot/lam2:+.6f} lam2 (exact {ex/lam2:+.6f}); norm/lam2 {nrm/lam2:.4f} = {nrm/(lam2*L):.4f} L; sliver {sl/lam2:+.5f}, |.| {sla/lam2:.5f}, int rhoG(sliver)={slG:.6f}")
        for key, (v, a_) in pcs.items():
            xa, xb, ya, yb = key
            if a_/lam2 > 1e-3:
                print(f"     x in ({xa:.1e},{xb:.1e}) y in ({ya:.1e},{yb:.1e}):  int r/lam2 = {v/lam2:+.5f}   int|r|/lam2 = {a_/lam2:.5f}  ({a_/(lam2*L):.4f} L)")
