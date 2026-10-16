# Half-coincident weight W12 with a rapidity regulator on the A-side k^- of each SS line placed inside the
# Glauber region (Lam_- = c*lam, so lambda_A ~ lam^2 << Lam_- << z ~ a/lambda_B = O(1)), exact F_A
# (generalized L1 with multi-pole external factors).  Also the fully coincident p_opp with the same regulator.
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popp_indep2 import quad_rot, make
from halfcoinc_indep import setup, JB2
from popp_kminus import FA_reg
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
from twoexch_rotated_fast import JB

def W12_reg(lam, Lam, theta=0.25, n=2000, nU=600):
    pa, beta, al1, al2, a1, a2 = setup(lam)
    ph = np.exp(1j*theta*np.pi); lamB = max(abs(beta), abs(al1), abs(al2))
    I = {}
    for c in ('12', '21'):
        f = lambda k1, k2, q: FA_reg(k1, k2, pa, a1, a2, c, q, Lam)*JB2(-k1, -k2, beta, al1, al2)
        I[c] = quad_rot(f, ph, lamB, n=n, nU=nU)
    return I['12']/(I['12'] + I['21'])

def popp_reg(lam, Lam, theta=0.25, n=2000, nU=600):
    pa, pb, a1, a2 = make(lam, 'base')
    ph = np.exp(1j*theta*np.pi); lamB = abs(pb['d0'])
    res = {}
    for cA, cB in itertools.product(('12', '21'), repeat=2):
        f = lambda k1, k2, q: FA_reg(k1, k2, pa, a1, a2, cA, q, Lam)*JB(-k1, -k2, pb, cB)
        res[(cA, cB)] = quad_rot(f, ph, lamB, n=n, nU=nU)
    N = sum(res.values())
    return (res[('12', '21')] + res[('21', '12')])/N

if __name__ == '__main__':
    for lam in (0.01, 0.003, 0.001):
        t0 = time.time()
        w0 = W12_reg(lam, None); w1 = W12_reg(lam, lam); w2 = W12_reg(lam, 3*lam)
        p1 = popp_reg(lam, lam)
        print(f"lam={lam}: half-coincident W12: no k^- regulator {w0:.6f} | Lam_-=lam {w1:.6f} | Lam_-=3lam {w2:.6f};   fully coincident p_opp(Lam_-=lam) = {p1:.6f}  ({time.time()-t0:.0f}s)", flush=True)
