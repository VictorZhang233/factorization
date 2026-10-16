# Independent check of T3 numbers: half-coincident weight W12 in the scalar model, (a) with the exact F_A
# (report's quadrant formula, verified by check_L3.py), (b) with F_A replaced by its localized limit
# (J_A/(a1 a2)) * race weight w^[12](k+), to show that Im W12 comes entirely from the race weights.
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popp_indep2 import quad_rot
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
from twoexch_rotated_fast import jet_params, FA, E

def JB2(p1, p2, beta, al1, al2):
    return (1j)**3/((p1 + p2 - beta)*(al1 - p1)*(al2 - p2))

def wrace(k1, k2, a1, a2, col, q):
    # localized limit of F_A^[col] / (J_A/(a1 a2)):  L2 two-line formulas
    if q == (1, 1):
        w12 = a1*k2/(a1*k2 + a2*k1)
    elif q == (-1, -1):
        w12 = a2*k1/(a2*k1 + a1*k2)
    elif q == (-1, 1):
        w12 = np.ones_like(k1)
    else:
        w12 = np.zeros_like(k1)
    return w12 if col == '12' else 1 - w12

def setup(lam, k1=(0.8, 0.1), k2=(-0.3, 0.9), s1=(-0.2, 0.3), s2=(0.25, -0.15), m1=0.4, m2=0.6, x1=0.3, x2=0.35):
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc(k1); k2T = sc(k2)
    pa = jet_params(0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
    MB, mb = 1.1*lam, 0.5*lam; m1, m2 = m1*lam, m2*lam
    xb = 1 - x1 - x2
    s1T, s2T = sc(s1), sc(s2)
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    return pa, beta, al1, al2, a1, a2

def W12(lam, n=2000, nU=700, theta=0.5, **kw):
    pa, beta, al1, al2, a1, a2 = setup(lam, **kw)
    ph = np.exp(1j*theta*np.pi); lamB = max(abs(beta), abs(al1), abs(al2))
    res = {}; resl = {}
    for c in ('12', '21'):
        f = lambda k1, k2, q: FA(k1, k2, pa, a1, a2, c, q)*JB2(-k1, -k2, beta, al1, al2)
        res[c] = quad_rot(f, ph, lamB, n=n, nU=nU)
        g = lambda k1, k2, q: wrace(k1, k2, a1, a2, c, q)*JB2(-k1, -k2, beta, al1, al2)
        resl[c] = quad_rot(g, ph, lamB, n=n, nU=nU)
    N = res['12'] + res['21']; Nl = resl['12'] + resl['21']
    d0B = al1 + al2 - beta
    JBeq = 1j/d0B          # equal-time value expected for int J_B d^2u/(2pi)^2 with this normalization
    return res['12']/N, resl['12']/Nl, Nl/(2*np.pi)**2/JBeq, (al1/lam**2, al2/lam**2, beta/lam**2)

if __name__ == '__main__':
    for lam in (0.03, 0.01, 0.003, 0.001):
        t0 = time.time()
        w, wl, nrm, al = W12(lam)
        print(f"lam={lam}: B (al1,al2,beta)/lam^2={tuple(round(x,4) for x in al)}  W12(exact F_A)={w:.8f}   W12(race-weight limit)={wl:.8f}   [int J_B/J_B(eq) = {nrm:.6f}]  ({time.time()-t0:.0f}s)", flush=True)
    for lam in (0.003,):
        w, wl, nrm, al = W12(lam, theta=0.25)
        print(f"lam={lam} theta=pi/4: W12(exact)={w:.8f}  W12(race)={wl:.8f}")
        w, wl, nrm, al = W12(lam, k2=(0.1, 0.8), s2=(0.3, -0.2), m2=0.4, x2=0.3)
        print(f"lam={lam} symmetric config: W12(exact)={w:.8f}  W12(race)={wl:.8f}")
