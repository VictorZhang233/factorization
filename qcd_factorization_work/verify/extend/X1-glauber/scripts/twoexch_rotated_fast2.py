# Rotated-contour evaluation with resolution adapted to the antidiagonal strip of jet B:
# quadrants (+,+),(-,-): polar (log r, phi) Gauss-Legendre;  quadrants (+,-),(-,+): variables
# (x2, U = x1 + x2) with U mapped by an asinh transform of scale lamB (strip width) and truncated
# at the quadrant boundary.  (Rotation k^+ = i*kappa; valid when B has no positive final energies.)
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoexch_rotated_fast import jet_params, sets, FA, JB

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

def Irot2(pa, pb, a1, a2, cA, cB, lamB, nt=3000, nphi=1500, ns=1500):
    ph = 1j
    tot = 0
    # diagonal quadrants
    t, wt = gl(nt, -45, 25); phi, wp = gl(nphi, 0, np.pi/2)
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp); r = np.exp(T)
    for q in ((1, 1), (-1, -1)):
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI)
        f = FA(ph*x1, ph*x2, pa, a1, a2, cA, q)*JB(-ph*x1, -ph*x2, pb, cB)*r*r
        tot += np.sum(W*f)
    # off-diagonal quadrants: (-,+): x2 = e^t > 0, x1 = U - x2 < 0  <=>  U < x2 ;  (+,-): x2 < 0, U > x2
    for q in ((-1, 1), (1, -1)):
        t2, w2 = gl(nt, -45, 25)
        s, ws = gl(ns, -1, 1)
        X2 = q[1]*np.exp(t2)[:, None]                                  # (nt,1)
        # U from -inf..x2 (q=(-1,1)) or x2..+inf (q=(1,-1)): write U = x2 - q[1]*v, v in (0, inf),
        # v = |x2| * g(s) with a mapping concentrating near v = |x2| (U = 0) on scale lamB
        A = np.abs(X2)
        # v-grid: v = A + lamB*sinh(c*s') piece + tail; use two pieces: v in (0, 2A) and (2A, inf)
        c1 = np.arcsinh(A/lamB)                                         # s' in (-c1, c1) -> v in (0, 2A)
        sp = s[None, :]*c1                                              # (nt, ns)
        v1 = A + lamB*np.sinh(sp); dv1 = lamB*np.cosh(sp)*c1*ws[None, :]
        # tail v in (2A, inf): v = 2A*exp(u), u in (0, 40)
        u, wu = gl(ns, 0, 40)
        v2 = 2*A*np.exp(u)[None, :]; dv2 = v2*wu[None, :]
        res = 0
        for v, dv in ((v1, dv1), (v2, dv2)):
            U = X2 - q[1]*v
            X1 = U - X2
            f = FA(ph*X1, ph*X2, pa, a1, a2, cA, q)*JB(-ph*X1, -ph*X2, pb, cB)
            res = res + np.sum(f*dv*(np.abs(X2)*w2[:, None]))
        tot += res
    return tot*ph**2/(2*np.pi)**2

if __name__ == '__main__':
    lam = float(sys.argv[1]); name = sys.argv[2]
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[name]
    pa = jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    lamB = abs(pb['d0'])
    res = {}
    for cA, cB in itertools.product(('12','21'), repeat=2):
        res[(cA, cB)] = Irot2(pa, pb, a1, a2, cA, cB, lamB)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    print(f"lam={lam} set={name} ROTATED(strip-adapted): N/N0={N/N0:.10f}")
    for k, v in res.items(): print(f"   W{k} = {v/N:.10f}")
    print(f"   p_opp = {(res[('12','21')]+res[('21','12')])/N:.10f}", flush=True)
