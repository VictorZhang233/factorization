# Check L1/L3: the report's quadrant formulas F_A (scripts/twoexch_rotated_fast.py: FA) against an
# independent exact evaluation of the k^- integrals of the COVARIANT jet function times exact propagators.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from resid import int2d
mp.mp.dps = 40
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
import numpy as np
from twoexch_rotated_fast import jet_params, FA
lam = 0.05
sc = lambda v: (lam*v[0], lam*v[1])
k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
pa = jet_params(0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
P = {k: mp.mpf(v) for k, v in pa.items()}
def FA_cov(kp1, kp2, col, eta):
    # J_A^[12] = i^3/[(k1+k2-beta+i e1)(al0-k1-k2+i e2)(al1-k2+i e3)];  [21]: (al2-k1+i e3)
    e = [eta*(1 + 0.137*j) for j in range(6)]
    facs = [(1, 1, -P['beta'] + 1j*e[0]), (-1, -1, P['al0'] + 1j*e[1])]
    facs.append((0, -1, P['al1'] + 1j*e[2]) if col == '12' else (-1, 0, P['al2'] + 1j*e[2]))
    facs.append((2*kp1, 0, -mp.mpf(a1) + 1j*e[3]))     # R1
    facs.append((0, 2*kp2, -mp.mpf(a2) + 1j*e[4]))     # R2
    return int2d((1j)**3, facs)
maxrel = 0
for q in itertools.product((1, -1), repeat=2):
    for (u1, u2) in ((0.3, 0.7), (2.0, 0.05), (0.01, 0.02), (5.0, 3.0)):
        kp1, kp2 = q[0]*u1*lam**2, q[1]*u2*lam**2
        for col in ('12', '21'):
            ref = complex(FA(np.array(kp1), np.array(kp2), pa, a1, a2, col, q))
            vals = [complex(FA_cov(mp.mpf(kp1), mp.mpf(kp2), col, mp.mpf(10)**(-k)*lam**2)) for k in (10, 14)]
            v = vals[-1]
            den = max(abs(ref), abs(v), 1e-300)
            rel = abs(v - ref)/den if den > 0 else 0
            if abs(ref) < 1e-12*abs(FA(np.array(abs(kp1)), np.array(abs(kp2)), pa, a1, a2, '12', (1,1))) and abs(v) < 1e-6*den:
                rel = 0
            maxrel = max(maxrel, rel if abs(ref) > 0 else abs(v))
            print(f"q={q} k+=({kp1:+.2e},{kp2:+.2e}) [{col}]  report FA = {ref:.10e}   covariant residues = {v:.10e}   rel.diff = {rel:.1e}")
print('max relative difference', maxrel)
