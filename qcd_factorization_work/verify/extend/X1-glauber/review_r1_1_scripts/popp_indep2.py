# Independent, vectorized evaluation of the T2/T3 model integrals on a rotated contour k+ = e^{i theta} x.
# Diagonal quadrants: log-Cartesian coordinates (u = log|x1|, v = log|x2|), Gauss-Legendre.
# Off-diagonal quadrants: (t = log|x2|, U = x1 + x2) with U pieces: sinh-map on scale lamB near U = 0 and
# exponential tails; truncation at U = x2 (quadrant boundary).  Convergence checked by refinement.
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
REP = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts'
sys.path.insert(0, REP)
from twoexch_rotated_fast import jet_params, sets, FA, JB

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

def make(lam, name):
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[name]
    pa = jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    return pa, pb, a1, a2

def quad_rot(f, ph, lamB, lo=-55.0, hi=35.0, n=1600, nU=500):
    """ Int_{R^2} d^2x f(ph*x1, ph*x2, q) * ph^2 ; f(k1, k2, q) vectorized. """
    tot = 0j
    u, wu = gl(n, lo, hi)
    U1, U2 = np.meshgrid(u, u, indexing='ij'); W = np.outer(wu, wu)
    for q in ((1, 1), (-1, -1)):
        x1 = q[0]*np.exp(U1); x2 = q[1]*np.exp(U2)
        tot += np.sum(W*np.exp(U1 + U2)*f(ph*x1, ph*x2, q))
    t, wt = gl(n, lo, hi)
    C = 40*lamB
    wc = np.arcsinh(C/lamB)
    for q in ((-1, 1), (1, -1)):
        s = q[1]
        acc = 0j
        # process in chunks over t to limit memory
        for i0 in range(0, n, 200):
            tt = t[i0:i0+200]; ww = wt[i0:i0+200]
            A = np.exp(tt)[:, None]; X2 = s*A
            pieces = []
            # side: s=+1 -> U in (-inf, X2);  s=-1 -> U in (X2, +inf).  Write U = s*V, V in (-inf, A).
            # central V in (-C, min(C, A)) via V = lamB sinh(w)
            wmax = np.arcsinh(np.minimum(C, A)/lamB)
            g, gw = np.polynomial.legendre.leggauss(nU)
            wgrid = 0.5*(wmax + wc)*g[None, :] + 0.5*(wmax - wc)        # from -wc to wmax
            wwt = 0.5*(wmax + wc)*gw[None, :]
            V = lamB*np.sinh(wgrid); dV = lamB*np.cosh(wgrid)*wwt
            pieces.append((V, dV))
            # left tail V in (-inf, -C): V = -C e^z, z in (0, 70)
            z, zw = gl(nU, 0.0, 70.0)
            V = -C*np.exp(z)[None, :]*np.ones_like(A); dV = C*np.exp(z)[None, :]*zw[None, :]*np.ones_like(A)
            pieces.append((V, dV))
            # right piece V in (C, A) if A > C: V = C e^z, z in (0, log(A/C))
            Lz = np.log(np.maximum(A, C)/C)
            z0, zw0 = np.polynomial.legendre.leggauss(nU)
            zz = 0.5*Lz*(z0[None, :] + 1); zwt = 0.5*Lz*zw0[None, :]
            V = C*np.exp(zz); dV = C*np.exp(zz)*zwt
            pieces.append((V, dV))
            for (V, dV) in pieces:
                Uv = s*V
                x1 = Uv - X2
                val = f(ph*x1, ph*np.broadcast_to(X2, x1.shape), q)
                val = np.where(np.isfinite(val), val, 0)
                acc += np.sum(val*dV*(A*ww[:, None]))
        tot += acc
    return tot*ph*ph

def run_T2(lam, name, theta, n=1600, nU=500):
    pa, pb, a1, a2 = make(lam, name)
    ph = np.exp(1j*theta); lamB = abs(pb['d0'])
    res = {}
    for cA, cB in itertools.product(('12', '21'), repeat=2):
        f = lambda k1, k2, q: FA(k1, k2, pa, a1, a2, cA, q)*JB(-k1, -k2, pb, cB)/(2*np.pi)**2
        res[(cA, cB)] = quad_rot(f, ph, lamB, n=n, nU=nU)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    return N/N0, (res[('12', '21')] + res[('21', '12')])/N, {k: v/N for k, v in res.items()}

if __name__ == '__main__':
    lam = float(sys.argv[1]); name = sys.argv[2]; th = float(sys.argv[3])
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 1600; nU = int(sys.argv[5]) if len(sys.argv) > 5 else 500
    t0 = time.time()
    nn, popp, W = run_T2(lam, name, th*np.pi, n, nU)
    print(f"[indep2] lam={lam} set={name} theta/pi={th} n={n},{nU}: N/N0={nn:.10f}  p_opp={popp:.10f}  ({time.time()-t0:.0f}s)", flush=True)
    for k, v in W.items(): print(f"      W{k} = {v:.10f}")
