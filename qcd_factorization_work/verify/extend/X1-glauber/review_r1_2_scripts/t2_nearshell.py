# Does an ANALYTIC pair of cutoffs that removes the near-shell region (K*Kc << a) give the strict-window value?
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import t2_regulator as T
k1T = (0.8, 0.1); k2T = (-0.3, 0.9)
pb = T.jet_params(0.8, 0.6, 0.5, 0.55, (-0.25, 0.4), (-0.8, -0.1), (0.3, -0.9))
a1 = 0.65; a2 = 0.9; lamB = abs(pb['d0']); Jcal = 1j/pb['d0']; a = np.sqrt(a1*a2)
for Kc_r, Ks in ((1e2, (1e-3, 1e-4, 1e-5)), (1e4, (1e-5, 1e-6, 1e-7))):
    Kc = Kc_r*lamB
    for Kr in Ks:
        K = Kr*a/lamB
        r1 = T.I_all(pb, a1, a2, lamB, np.pi/4, K=K, Kc=Kc)
        N1 = sum(r1.values()); p1 = (r1[('12', '21')] + r1[('21', '12')])/N1
        print(f"Kc = {Kc_r:g} lamB, K = {Kr:g} a/lamB  (K*Kc/a = {K*Kc/a:.3g}):  N/Jcal={N1/Jcal:.6f}  p_opp={p1:.6f}", flush=True)
