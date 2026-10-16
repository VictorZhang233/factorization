"""
s6_i0_poles.py -- the i0 of the eikonal propagator agrees with the pole of the exact propagator it replaces.

(1) For the four external-line types (gluon momentum k flowing INTO the line, p^2 = M^2):
      incoming quark/antiquark : exact denominator (p+K)^2 - M^2 + i0 = 2 p.K + K^2 + i0
      outgoing quark/antiquark : exact denominator (p-K)^2 - M^2 + i0 = -2 p.K + K^2 + i0
    As a function of the eikonal variable a = p.K the pole lies at a = -K^2/2 - i0 (incoming) and
    a = K^2/2 + i0 (outgoing): same half plane as the eikonal pole of i/(a + i0) (past line) and
    -i/(a - i0) (future line).
(2) DIS seed: K-gluon k from the target-collinear subgraph (k^+ large) attaches to the struck quark p' (p'^- > 0,
    final state): (p'-k)^2 + i0 = -2 p'^- k^+ + (k-independent of k^+) + i0 -> pole in k^+ in the UPPER half plane
    == pole of 1/(nB.k - i0) = 1/(k^+ - i0): future-pointing Wilson line along nB (Collins 2011 eq. 11.6).
(3) Drell-Yan: K-gluon from hadron A attaches to the incoming antiquark from hadron B (pbar^- > 0, initial state):
    (pbar + k)^2 + i0 = 2 pbar^- k^+ + ... + i0 -> pole in k^+ in the LOWER half plane == 1/(k^+ + i0):
    past-pointing Wilson line along nB.
(4) the future/past difference is a delta function: 1/(a - i0) - 1/(a + i0) = 2 pi i delta(a) (numerical check with
    a test function).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *
import sympy as sp

R = Report('s6_i0_poles')
eps = sp.symbols('epsilon', positive=True)
a = sp.symbols('a')          # complex variable (pole positions)
K2 = sp.symbols('K2', real=True)

# (1) pole location in the eikonal variable a = p.K
pole_in = sp.solve(sp.Eq(2 * a + K2 + sp.I * eps, 0), a)[0]
pole_out = sp.solve(sp.Eq(-2 * a + K2 + sp.I * eps, 0), a)[0]
R.flag(f'(1) incoming line: pole at a = {pole_in}  (Im < 0, like i/(a+i0))', sp.im(pole_in) == -eps / 2)
R.flag(f'(1) outgoing line: pole at a = {pole_out} (Im > 0, like -i/(a-i0))', sp.im(pole_out) == eps / 2)

# (2) DIS: light-front variables, p' = (0, p'^-, 0_T) massless, k = (k^+, k^-, k_T)
kp = sp.symbols('k_p')      # complex k^+ (pole positions)
km, kt2, ppm = sp.symbols('k_m k_t2 pp_m', real=True)
den_dis = (-2 * ppm * kp) + (2 * kp * km - kt2) + sp.I * eps          # (p'-k)^2 + i0 with p'^+ = 0, p'_T = 0
den_dis = sp.expand(den_dis)
pole_dis = sp.solve(sp.Eq(den_dis, 0), kp)[0]
im_dis = sp.simplify(sp.im(pole_dis).subs({km: sp.Rational(1, 10)}))
R.flag(f'(2) DIS: pole of the struck-quark propagator in k^+ has Im = {sp.simplify(sp.im(pole_dis))} > 0 for p\'^- > k^-',
       sp.simplify(im_dis.subs(ppm, 3)) > 0)
# (3) DY
pbm = sp.symbols('pb_m', positive=True)
den_dy = sp.expand(2 * pbm * kp + (2 * kp * km - kt2) + sp.I * eps)  # (pbar + k)^2 + i0, pbar = (0, pbar^-, 0_T)
pole_dy = sp.solve(sp.Eq(den_dy, 0), kp)[0]
R.flag(f'(3) DY: pole of the incoming-antiquark propagator in k^+ has Im = {sp.simplify(sp.im(pole_dy))} < 0',
       sp.simplify(sp.im(pole_dy).subs({km: sp.Rational(1, 10), pbm: 3})) < 0)

# (4) 1/(a - i0) - 1/(a + i0) = 2 pi i delta(a)  (test function f(a) = exp(-a^2) (1 + a))
import mpmath as mpm
for e in [1e-2, 1e-3]:
    val = mpm.quad(lambda x: mpm.e**(-x**2) * (1 + x) * (1 / (x - 1j * e) - 1 / (x + 1j * e)), [-mpm.inf, -1, 0, 1, mpm.inf])
    R.check(f'(4) int f(a)[1/(a-i e) - 1/(a+i e)] da -> 2 pi i f(0)  (e={e})', float(abs(val - 2j * mpm.pi) / (2 * mpm.pi)), 3 * e)

# (5) blueprint E7.24: one-gluon exchange between two past-pointing eikonal lines (A along nA: i/(k^- + i0);
#     B along nB with momentum -k flowing in: i/(-k^+ + i0)); k^- integral of
#     1/((k^- + i0)(-k^+ + i0)(2 k^+ k^- - kT^2 + i0)) = 0 for k^+ > 0 and = -2 pi i/(kT^2 k^+) for k^+ < 0.
kT2 = 1.3
for kpv in [0.7, -0.7]:
    e = 1e-4
    f = lambda x: 1 / ((x + 1j * e) * (-kpv + 1j * e) * (2 * kpv * x - kT2 + 1j * e))
    pole = kT2 / (2 * kpv)
    pts = sorted([-mpm.inf, -50, min(0, pole) - 1, -1e-3, 0, 1e-3, max(0, pole) + 1, 50, mpm.inf] + [pole - 1e-3, pole, pole + 1e-3])
    val = complex(mpm.quad(f, pts, maxdegree=10))
    target = 0 if kpv > 0 else -2j * np.pi / (kT2 * kpv)
    scale = 2 * np.pi / (kT2 * abs(kpv))
    R.check(f'(5) blueprint E7.24: past-past exchange, int dk^- = {"0" if kpv > 0 else "-2 pi i/(kT^2 k^+)"} for k^+ = {kpv}',
            abs(val - target) / scale, 1e-3)

R.summary()
