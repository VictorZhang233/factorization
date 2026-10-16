# Unit tests for twoexch_model.py: (1) half-line log-residue integrator; (2) A-side quadrant formulas
# (exact k^- residues) against brute-force double quadrature (scipy) of the covariant colour-ordered jet function.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import numpy as np
from scipy import integrate
from twoexch_model import *
mp.mp.dps = 20

# (1) half-line integrator
C = mp.mpc(1.3, -0.4); facs = [(mp.mpc(2, 0.1), mp.mpc(1, 0.5)), (mp.mpc(-1, 0.2), mp.mpc(0.3, -0.7)), (1, mp.mpc(-2, 0.3))]
f = lambda x: C * x / ((facs[0][0]*x - facs[0][1]) * (facs[1][0]*x - facs[1][1]) * (facs[2][0]*x - facs[2][1]))
for s in (+1, -1):
    num = mp.quad(f, [0, 1, 10, mp.inf]) if s > 0 else mp.quad(f, [-mp.inf, -10, -1, 0])
    print("halfline sign", s, "formula", mp.nstr(int_halfline(C, 1, facs, s), 12), " quad", mp.nstr(num, 12), flush=True)

# (2) A-side quadrant formulas vs brute force (double precision)
lam = 1.0
sc = lambda v: (lam*v[0], lam*v[1])
k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
pa = jet_params(lam, 0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
eta = 0.05
p = {k: float(v) for k, v in pa.items()}
def JA(k1, k2, col):
    d0, beta, al0, al1, al2 = p['d0'], p['beta'], p['al0'], p['al1'], p['al2']
    den3 = (al1 - k2 + 1j*eta) if col == '12' else (al2 - k1 + 1j*eta)
    return (1j)**3 / ((k1 + k2 - beta + 1j*eta) * (al0 - k1 - k2 + 1j*eta) * den3)
def cquad(fun, a, b, pts=None):
    re = integrate.quad(lambda t: fun(t).real, a, b, points=pts, limit=400, epsabs=1e-11, epsrel=1e-10)[0]
    im = integrate.quad(lambda t: fun(t).imag, a, b, points=pts, limit=400, epsabs=1e-11, epsrel=1e-10)[0]
    return re + 1j*im
def fullline(fun):
    # map R -> (-pi/2, pi/2) via k = tan(th)
    g = lambda th: fun(np.tan(th)) / np.cos(th)**2
    return cquad(g, -np.pi/2 + 1e-12, np.pi/2 - 1e-12, pts=list(np.arctan(np.linspace(-3, 3, 25))))
def brute(y, x, col):
    R1 = lambda k: 1/(2*y*k - a1 + 1j*eta)
    R2 = lambda k: 1/(2*x*k - a2 + 1j*eta)
    inner = lambda k2: fullline(lambda k1: JA(k1, k2, col)*R1(k1)) * R2(k2)
    return fullline(inner) / (2*np.pi)**2
def formula(y, x, col):
    terms = F_A_terms(mp.mpf(y), pa, a1, a2, mp.mpf(eta), col)
    sx = 1 if x > 0 else -1
    tot = mp.mpc(0)
    for (C, m, facs) in terms[sx]:
        val = C * mp.mpf(x)**m
        for (g, h) in facs: val = val/(g*x - h)
        tot += val
    return complex(tot)
for (y, x) in [(0.7, 1.3), (0.7, -0.9), (-0.6, 1.1), (-0.8, -1.4)]:
    for col in ('12', '21'):
        b = brute(y, x, col); fo = formula(y, x, col)
        print(f"y={y:5}, x={x:5}, col={col}: brute={b:.8e}  formula={fo:.8e}  |diff|/|f|={abs(b-fo)/max(abs(fo),1e-30):.2e}", flush=True)
