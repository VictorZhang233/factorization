# Does Re p_opp -> 0 (T2) survive an O(1) modification of the A-side integrand at k^- ~ z = O(1)
# (B-collinear region of the connecting gluon, where E.19(b) fails)?  Exact F_A generalized to external factors
# R_e(k^-) rho(k^-), rho = Lam^2/(k^2 + Lam^2), via the exact sector functions (generalized Lemma L1).
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popp_indep2 import quad_rot, make
from kminus_sensitivity import poles_res
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
from twoexch_rotated_fast import FA, JB

def sector_J(pa, col, split, z1, z2):
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    i3 = (1j)**3
    f1, f2 = split
    if col == '12':
        if f1 and f2:        return i3/(d0*(al0 - z1 - z2)*(al1 - z2))
        if (not f1) and (not f2): return i3/(d0*(d10 + z1)*(z1 + z2 - beta))
        if (not f1) and f2:  return i3/(d0*(d10 + z1)*(al1 - z2))
        return 0*z1
    else:
        if f1 and f2:        return i3/(d0*(al0 - z1 - z2)*(al2 - z1))
        if (not f1) and (not f2): return i3/(d0*(d20 + z2)*(z1 + z2 - beta))
        if f1 and (not f2):  return i3/(d0*(d20 + z2)*(al2 - z1))
        return 0*z1

def FA_reg(k1, k2, pa, a1, a2, col, q, Lam):
    P1 = poles_res(k1, a1, Lam); P2 = poles_res(k2, a2, Lam)
    tot = 0
    for j1, (z1, r1) in enumerate(P1):
        for j2, (z2, r2) in enumerate(P2):
            f1 = (q[0] > 0) if j1 == 0 else (np.imag(z1) < 0)
            f2 = (q[1] > 0) if j2 == 0 else (np.imag(z2) < 0)
            c1 = -1j*r1 if f1 else 1j*r1
            c2 = -1j*r2 if f2 else 1j*r2
            tot = tot + c1*c2*sector_J(pa, col, (f1, f2), z1, z2)
    return tot

def run(lam, name, Lam, theta=0.25, n=2000, nU=600):
    pa, pb, a1, a2 = make(lam, name)
    ph = np.exp(1j*theta*np.pi); lamB = abs(pb['d0'])
    res = {}
    for cA, cB in itertools.product(('12', '21'), repeat=2):
        f = lambda k1, k2, q: FA_reg(k1, k2, pa, a1, a2, cA, q, Lam)*JB(-k1, -k2, pb, cB)/(2*np.pi)**2
        res[(cA, cB)] = quad_rot(f, ph, lamB, n=n, nU=nU)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    return N/N0, (res[('12', '21')] + res[('21', '12')])/N

if __name__ == '__main__':
    lam = float(sys.argv[1]) if len(sys.argv) > 1 else 0.003
    pa, pb, a1, a2 = make(lam, 'base')
    # sanity: FA_reg with Lam=None equals the report's FA
    k1 = np.array([0.4*lam**2*np.exp(0.7j)]); k2 = np.array([-1.3*lam**2*np.exp(0.7j)])
    print('sanity FA_reg(None) vs FA:', FA_reg(k1, k2, pa, a1, a2, '21', (1, -1), None), FA(k1, k2, pa, a1, a2, '21', (1, -1)))
    for Lam in (None, 10.0, 1.0, 0.3, 0.1, 0.03):
        t0 = time.time()
        nn, popp = run(lam, 'base', Lam)
        print(f"lam={lam} base, A-side k^- form factor Lam={Lam}: N/N0={nn:.6f}  p_opp={popp:.6f}  ({time.time()-t0:.0f}s)", flush=True)
