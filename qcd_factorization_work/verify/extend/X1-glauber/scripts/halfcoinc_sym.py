# Sanity test of halfcoinc.py: with a1 = a2 and a B jet symmetric under (line 1 <-> line 2) the
# half-coincident weight must be W12 = 1/2 exactly at leading power (Im W12 -> 0); with asymmetric
# parameters Im W12 = O(1).  Also scan the B asymmetry.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoexch_rotated_fast import jet_params, E
from halfcoinc import Irot
def run(lam, k1, k2, s1, s2, m1=0.4, m2=0.4, x1=0.3, x2=0.3, label=''):
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T, k2T = sc(k1), sc(k2)
    pa = jet_params(0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
    MB, mb = 1.1*lam, 0.5*lam; xb = 1 - x1 - x2
    s1T, s2T = sc(s1), sc(s2); m1, m2 = m1*lam, m2*lam
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    I12 = Irot(pa, (beta, al1, al2), a1, a2, '12'); I21 = Irot(pa, (beta, al1, al2), a1, a2, '21')
    N = I12 + I21
    print(f"{label} lam={lam}: a1/a2={a1/a2:.3f} al1,al2={al1/lam**2:.4f},{al2/lam**2:.4f}  W12={I12/N:.8f}", flush=True)
for lam in (0.01, 0.003):
    run(lam, (0.8, 0.1), (0.1, 0.8), (-0.2, 0.3), (0.3, -0.2), label='symmetric ')
    run(lam, (0.8, 0.1), (0.1, 0.8), (-0.2, 0.3), (0.5, -0.4), label='B-asym    ')
    run(lam, (0.8, 0.1), (-0.3, 0.9), (-0.2, 0.3), (0.3, -0.2), label='a-asym    ')
