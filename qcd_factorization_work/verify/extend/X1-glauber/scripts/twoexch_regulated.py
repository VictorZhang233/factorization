# [Fix round 1 label note] 'Thm T4' below = current T2' (analytic k^+ regulator, class X); the
# 'collinear end' wording is superseded by the near-shell diagnosis in REPORT T2'/P2.
# Two SS exchanges with an ANALYTIC rapidity regulator on the exchanged gluons' plus components,
# chi(u) = 1/(1 + |u|/Kc) per gluon (quadrant-wise analytic, real on the real axis), evaluated on the
# rotated contour (strip-adapted).  Prediction (REPORT Thm T4): Re p_opp -> 0 even when jet A has
# end poles (set 'apole'), because the regulator removes the collinear end where the
# Lemma-E.19 approximation of the jets is invalid.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoexch_rotated_fast import jet_params, sets, FA, JB
import twoexch_rotated_fast2 as R2

def chi_rot(k, q, Kc):
    # quadrant piece of 1/(1+|u|/Kc) continued: for real-u sign q, |u| = q*u
    return 1.0/(1.0 + q*k/Kc)

def Irot_reg(pa, pb, a1, a2, cA, cB, lamB, Kc, nt=3000, nphi=1500, ns=1500):
    ph = 1j; tot = 0
    t, wt = R2.gl(nt, -45, 25); phi, wp = R2.gl(nphi, 0, np.pi/2)
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp); r = np.exp(T)
    for q in ((1, 1), (-1, -1)):
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI)
        k1, k2 = ph*x1, ph*x2
        f = FA(k1, k2, pa, a1, a2, cA, q)*JB(-k1, -k2, pb, cB)*chi_rot(k1, q[0], Kc)*chi_rot(k2, q[1], Kc)*r*r
        tot += np.sum(W*f)
    for q in ((-1, 1), (1, -1)):
        t2, w2 = R2.gl(nt, -45, 25); s, ws = R2.gl(ns, -1, 1)
        X2 = q[1]*np.exp(t2)[:, None]; A = np.abs(X2)
        c1 = np.arcsinh(A/lamB); sp = s[None, :]*c1
        v1 = A + lamB*np.sinh(sp); dv1 = lamB*np.cosh(sp)*c1*ws[None, :]
        u, wu = R2.gl(ns, 0, 40); v2 = 2*A*np.exp(u)[None, :]; dv2 = v2*wu[None, :]
        res = 0
        for v, dv in ((v1, dv1), (v2, dv2)):
            U = X2 - q[1]*v; X1 = U - X2
            k1, k2 = ph*X1, ph*X2
            f = FA(k1, k2, pa, a1, a2, cA, q)*JB(-k1, -k2, pb, cB)*chi_rot(k1, q[0], Kc)*chi_rot(k2, q[1], Kc)
            res = res + np.sum(f*dv*(np.abs(X2)*w2[:, None]))
        tot += res
    return tot*ph**2/(2*np.pi)**2

if __name__ == '__main__':
    lam = float(sys.argv[1]); name = sys.argv[2]; Kfac = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[name]
    pa = jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    lamB = abs(pb['d0']); Kc = Kfac*lam
    res = {}
    for cA, cB in itertools.product(('12','21'), repeat=2):
        res[(cA, cB)] = Irot_reg(pa, pb, a1, a2, cA, cB, lamB, Kc)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    print(f"lam={lam} set={name} Kc={Kc:.3g} REGULATED: N/N0={N/N0:.8f}  p_opp={(res[('12','21')]+res[('21','12')])/N:.8f}", flush=True)
