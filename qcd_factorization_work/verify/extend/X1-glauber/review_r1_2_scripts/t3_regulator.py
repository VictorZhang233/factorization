# Reviewer-2 independent check of X1 claim T3 (half-coincident pattern) and of its regulator dependence.
# W12 = 1/2 + Phi,  Phi = (1/Jcal_B) int d^2u/(2pi)^2 [w12(z(u)) - 1/2] J_B(-u),  z_e = a_e/(2 u_e)
# (leading power in eps = lambda_A lambda_B / a: jet A replaced by its localized weights).
# w12: race weights of L1/L2 (no regulator)  or  weights with an analytic regulator chi(k^-)=K^2/(k^2+K^2)
# on the A-side k^- integrals (scale K).  Contour: u = e^{i theta} x, x real (rotation needs NF_B).
import sys, os, pickle
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

def model(lam=1.0, variant='author'):
    sc = lambda v: (lam*v[0], lam*v[1])
    if variant == 'author':      # halfcoinc.py parameters
        k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
        MB, mb, m1, m2 = 1.1*lam, 0.5*lam, 0.4*lam, 0.6*lam
        x1, x2 = 0.3, 0.35; s1T, s2T = sc((-0.2, 0.3)), sc((0.25, -0.15))
    elif variant == 'Basym':     # halfcoinc_sym.py 'B-asym'
        k1T = sc((0.8, 0.1)); k2T = sc((0.1, 0.8))
        MB, mb, m1, m2 = 1.1*lam, 0.5*lam, 0.4*lam, 0.4*lam
        x1, x2 = 0.3, 0.3; s1T, s2T = sc((-0.2, 0.3)), sc((0.5, -0.4))
    xb = 1 - x1 - x2
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    return dict(al1=al1, al2=al2, beta=beta, d0B=al1 + al2 - beta, a1=a1, a2=a2)

def JB(p1, p2, m):
    return (1j)**3/((p1 + p2 - m['beta'])*(m['al1'] - p1)*(m['al2'] - p2))

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

def integrate(fun, theta, nt=2400, nphi=900, tmin=-40.0, tmax=40.0):
    """int d^2u/(2pi)^2 fun(u1,u2,case) over the rotated real plane u = e^{i theta} x."""
    ph = np.exp(1j*theta)
    t, wt = gl(nt, tmin, tmax); phi, wp = gl(nphi, 0.0, np.pi/2)
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp); r = np.exp(T)
    tot = 0
    for q in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
        case = ('F' if q[0] > 0 else 'B') + ('F' if q[1] > 0 else 'B')
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI)
        tot += np.sum(W*r*r*fun(ph*x1, ph*x2, case))
    return tot*ph**2/(2*np.pi)**2

def Phi(m, theta, K=None, **kw):
    Jcal = 1j/m['d0B']
    def fun(u1, u2, case):
        z1 = m['a1']/(2*u1); z2 = m['a2']/(2*u2)
        w = wrace(case, z1, z2) if K is None else wreg[case](z1, z2, K)
        return (w - 0.5)*JB(-u1, -u2, m)
    return integrate(fun, theta, **kw)/Jcal

if __name__ == '__main__':
    for variant in ('author', 'Basym'):
        m = model(1.0, variant)
        print(f"[{variant}] B finals al1={m['al1']:.4f} al2={m['al2']:.4f} beta={m['beta']:.4f} d0B={m['d0B']:.4f}  a1={m['a1']:.3f} a2={m['a2']:.3f}")
        # normalization / rotation sanity: int J_B(-u) d^2u/(2pi)^2 = Jcal_B
        for th in (np.pi/4, np.pi/2):
            nrm = integrate(lambda u1, u2, c: JB(-u1, -u2, m), th)/(1j/m['d0B'])
            print(f"   theta/pi={th/np.pi:.2f}: int J_B / Jcal_B = {nrm:.10f}")
        for th in (np.pi/4, np.pi/2):
            print(f"   race (no regulator), theta/pi={th/np.pi:.2f}: W12 = {0.5 + Phi(m, th):.8f}")
        lamB = abs(m['d0B']); a = np.sqrt(m['a1']*m['a2'])
        for Kr in (1e4, 1e2, 10.0, 3.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
            K = Kr*a/lamB
            print(f"   regulator K = {Kr:g} * a/lambda_B : W12 = {0.5 + Phi(m, np.pi/4, K=K):.8f}", flush=True)
