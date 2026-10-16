# Regulator (scheme) dependence of the in-window residual: rapidity regulators on k^+ of the two SS lines.
#  chiX : 1/(1+|k|/Kc)          (in the report's analytic class X; T2' predicts Re p_opp -> 0)
#  chiL : Kc^2/(k^2+Kc^2)       (smooth, even, real; NOT in class X: poles at +-i Kc on the rotated axis)
#  chiG : exp(-k^2/Kc^2)        (smooth, even, entire, real; not in X: grows along the imaginary axis)
#         NOTE: on the rotated contour exp(-(e^{i pi/4} x/Kc)^2) is a pure, wildly oscillating phase; the
#         quadrature returns NaN for 'G' -- that column of logs/popp_kplus_reg.log is NOT a result.
# Real-axis integrals evaluated on the contour rotated by theta = pi/4 (no regulator singularity crossed).
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popp_indep2 import quad_rot, make
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
from twoexch_rotated_fast import FA, JB

def chi(k, q_e, Kc, kind):
    if kind == 'X':
        return 1/(1 + q_e*k/Kc)          # |k| = q_e*k continued from the half line of sign q_e
    if kind == 'L':
        return Kc**2/(k**2 + Kc**2)
    if kind == 'G':
        return np.exp(-(k/Kc)**2)
    return 1.0

def run(lam, name, kind, theta=0.25, n=2000, nU=600):
    pa, pb, a1, a2 = make(lam, name)
    ph = np.exp(1j*theta*np.pi); lamB = abs(pb['d0']); Kc = lam
    res = {}
    for cA, cB in itertools.product(('12', '21'), repeat=2):
        f = lambda k1, k2, q: FA(k1, k2, pa, a1, a2, cA, q)*JB(-k1, -k2, pb, cB)*chi(k1, q[0], Kc, kind)*chi(k2, q[1], Kc, kind)/(2*np.pi)**2
        res[(cA, cB)] = quad_rot(f, ph, lamB, n=n, nU=nU)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    return N/N0, (res[('12', '21')] + res[('21', '12')])/N

if __name__ == '__main__':
    for lam in (0.01, 0.003, 0.001):
        for kind in ('X', 'L', 'G'):
            t0 = time.time()
            nn, popp = run(lam, 'base', kind)
            print(f"lam={lam} base Kc=lam regulator {kind}: N/N0={nn:.6f}  p_opp={popp:.6f}  ({time.time()-t0:.0f}s)", flush=True)
