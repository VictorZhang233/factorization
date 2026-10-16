# Reviewer-2 check of X1 claim T2/T2' (fully coincident pattern) at leading power, and of its dependence on a
# regulator acting on the A-side k^- integrals.
#   p_opp = [I(12,21) + I(21,12)] / sum I,   I(pA,pB) = int d^2u/(2pi)^2 w^[pA](z(u)) J_B^[pB](-u) chi(u1) chi(u2)
#   w: localized A-side weights (race, or with chi_-(k^-) = K^2/(k^2+K^2));  chi(u) = 1/(1+|u|/Kc) as in X1's
#   twoexch_regulated.py (analytic cutoff of the A-collinear end, T2').  Jet B: scalar model, base set of X1.
import sys, os, pickle, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
here = os.path.dirname(os.path.abspath(__file__))
z1s, z2s, Ks = sp.symbols('z1 z2 K')
with open(os.path.join(here, 'regweights.pkl'), 'rb') as fh:
    ex = {c: eval(s_, dict(vars(sp))) for c, s_ in pickle.load(fh).items()}
wreg = {c: sp.lambdify((z1s, z2s, Ks), e, 'numpy') for c, e in ex.items()}

def wrace(case, z1, z2):
    if case == 'FF': return z1/(z1 + z2)
    if case == 'BB': return z2/(z1 + z2)
    if case == 'BF': return np.ones_like(z1)
    return np.zeros_like(z1)

def E(pT, m, pp): return (pT[0]**2 + pT[1]**2 + m**2)/(2*pp)
def jet_params(M, ma, ms, xs, sT, k1T, k2T):
    P = M**2/2
    sub = lambda u, v: (u[0]-v[0], u[1]-v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1-xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P-Ea-Es0, d10=P-Ea-Es1, d20=P-Ea-Es2, beta=Ea+Es-P, al0=Es-Es0, al1=Es-Es1, al2=Es-Es2)

def JB(p1, p2, pb, col, P=None):
    if P is None: P = p1 + p2
    den3 = (pb['al1'] - p2) if col == '12' else (pb['al2'] - p1)
    return (1j)**3/((P - pb['beta'])*(pb['al0'] - P)*den3)

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

def chi_q(u, q, Kc):          # quadrant-wise continuation of 1/(1+|u|/Kc) (real-axis sign q)
    return 1.0/(1.0 + q*u/Kc) if Kc is not None else 1.0

def I_all(pb, a1, a2, lamB, theta, K=None, Kc=None, nt=2000, nphi=1000, ns=1600):
    ph = np.exp(1j*theta)
    res = {c: 0 for c in itertools.product(('12', '21'), repeat=2)}
    def wts(u1, u2, case):
        z1 = a1/(2*u1); z2 = a2/(2*u2)
        w12 = wrace(case, z1, z2) if K is None else wreg[case](z1, z2, K)
        return {'12': w12, '21': 1 - w12}
    # diagonal quadrants: polar
    t, wt = gl(nt, -40, 40); phi, wp = gl(nphi, 0, np.pi/2)
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp); r = np.exp(T)
    for q in ((1, 1), (-1, -1)):
        case = 'FF' if q[0] > 0 else 'BB'
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI); u1, u2 = ph*x1, ph*x2
        w = wts(u1, u2, case); c = chi_q(u1, q[0], Kc)*chi_q(u2, q[1], Kc)
        for cA, cB in res:
            res[(cA, cB)] += np.sum(W*r*r*w[cA]*JB(-u1, -u2, pb, cB)*c)
    # off-diagonal quadrants: (x2, U = x1 + x2), strip-adapted in U (cf. X1's twoexch_rotated_fast2.py)
    for q in ((-1, 1), (1, -1)):
        case = 'BF' if q[0] < 0 else 'FB'
        t2, w2 = gl(nt, -40, 40); s, ws = gl(ns, -1, 1)
        X2 = q[1]*np.exp(t2)[:, None]; A = np.abs(X2)
        c1 = np.arcsinh(A/lamB); sp_ = s[None, :]*c1
        v1 = A + lamB*np.sinh(sp_); dv1 = lamB*np.cosh(sp_)*c1*ws[None, :]
        uu, wu = gl(ns, 0, 40); v2 = 2*A*np.exp(uu)[None, :]; dv2 = v2*wu[None, :]
        U1 = -q[1]*lamB*np.sinh(sp_); U2 = q[1]*A*(1 - 2*np.exp(uu)[None, :])
        for v, dv, U in ((v1, dv1, U1), (v2, dv2, U2)):
            X1 = U - X2
            u1, u2 = ph*X1, ph*X2
            w = wts(u1, u2, case); c = chi_q(u1, q[0], Kc)*chi_q(u2, q[1], Kc)
            meas = dv*(np.abs(X2)*w2[:, None])
            for cA, cB in res:
                res[(cA, cB)] += np.sum(meas*w[cA]*JB(-u1, -u2, pb, cB, P=-ph*U)*c)
    return {k_: v_*ph**2/(2*np.pi)**2 for k_, v_ in res.items()}

if __name__ == '__main__':
    lam = 1.0
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    pb = jet_params(0.8*lam, 0.6*lam, 0.5*lam, 0.55, sc((-0.25, 0.4)), (-k1T[0], -k1T[1]), (-k2T[0], -k2T[1]))
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    lamB = abs(pb['d0']); Jcal = 1j/pb['d0']
    print(f"jet B (base set): al0={pb['al0']:.4f} al1={pb['al1']:.4f} al2={pb['al2']:.4f} beta={pb['beta']:.4f} d0={pb['d0']:.4f}")
    a = np.sqrt(a1*a2)
    th = np.pi/4
    for Kc_r in (1e2, 1e4, 1e6):
        Kc = Kc_r*lamB
        r0 = I_all(pb, a1, a2, lamB, th, K=None, Kc=Kc)
        N0 = sum(r0.values()); p0 = (r0[('12', '21')] + r0[('21', '12')])/N0
        print(f"Kc = {Kc_r:g} lamB, no k^- regulator (race):  N/Jcal={N0/Jcal:.6f}  p_opp={p0:.6f}", flush=True)
        for Kr in (10.0, 1.0, 0.1, 0.01):
            K = Kr*a/lamB
            if K*Kc < 10*a1:   # keep the near-shell soft region inside both cutoffs (K*Kc >> a)
                pass
            r1 = I_all(pb, a1, a2, lamB, th, K=K, Kc=Kc)
            N1 = sum(r1.values()); p1 = (r1[('12', '21')] + r1[('21', '12')])/N1
            print(f"      + k^- regulator K = {Kr:g} a/lamB (K*Kc/a = {K*Kc/a:.3g}):  N/Jcal={N1/Jcal:.6f}  p_opp={p1:.6f}", flush=True)
