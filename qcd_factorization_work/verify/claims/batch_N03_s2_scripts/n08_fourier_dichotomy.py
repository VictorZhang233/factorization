#!/usr/bin/env python3
"""
N08 (stage-2 verifier): LaMET Lemma 5.2 (z^2 <-> d^2/dx^2), endpoint factors, Cor. 5.3 (endpoint dichotomy),
and the P=0-normalization terms -1/4 and -5/12 (BVZ eq. (bR)).

Conventions: r(lambda) = int dalpha e^{i alpha lambda} rho(alpha);  FT[f](x) = int dlambda/(2pi) e^{-i x lambda} f(lambda);
z^2 = -lambda^2/P_z^2 (4-vector square, z along e_z, lambda = P.z = -P^z z).
Checks (method differs from stage 1: closed-form 1F1 transform of a beta-type rho, Fourier inversion by
contour-free direct quadrature on a symmetric window with Fejer (Cesaro) smoothing; symbolic endpoint asymptotics
of the BVZ renormalon model):
Run: python3 -I n08_fourier_dichotomy.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np
from scipy import integrate

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

# ---------------- Lemma 5.2: sign and form ----------------
lam, x, Lam, Pz = sp.symbols('lambda x Lambda P_z', real=True)
# lambda^2 e^{-i x lambda} = -d^2/dx^2 e^{-i x lambda}
check("lambda^2 e^{-i x lambda} = -d_x^2 e^{-i x lambda}", sp.simplify(lam**2 * sp.exp(-sp.I * x * lam) + sp.diff(sp.exp(-sp.I * x * lam), x, 2)) == 0)
# hence FT[z^2 Lambda^2 r] = -(Lambda^2/Pz^2) FT[lambda^2 r] = -(Lambda^2/Pz^2)(-rho'') = +(Lambda^2/Pz^2) rho''
# numerical: rho(alpha) = alpha^4 (1-alpha)^5 on [0,1]  -> r = B(5,6) 1F1(5;11; i lambda)  (closed form)
mp.mp.dps = 30
B56 = mp.beta(5, 6)
def r_of(l): return B56 * mp.hyp1f1(5, 11, mp.mpc(0, l))
def rho(a): return a**4 * (1 - a)**5 if 0 <= a <= 1 else 0.0
def rho2(a):
    if not (0 < a < 1): return 0.0
    return 12 * a**2 * (1 - a)**5 - 40 * a**3 * (1 - a)**4 + 20 * a**4 * (1 - a)**3
# closed form check of r against quadrature
for l in [3.0, -17.0]:
    rq = mp.quad(lambda a: a**4 * (1 - a)**5 * mp.exp(mp.mpc(0, a * l)), [0, 0.5, 1])
    check(f"closed form r(lambda) = B(5,6) 1F1(5;11;i lambda) at lambda={l}", abs(rq - r_of(l)) < 1e-25)
# FT[lambda^2 r](x) = (1/pi) Re int_0^inf dl e^{-i x l} l^2 r(l)   (r(-l) = conj r(l));  lambda^2 r ~ lambda^{-3}: abs. convergent
lgrid = np.linspace(0, 400, 400001)
rvals = np.array([complex(r_of(l)) for l in lgrid[::100]])
# interpolate r on fine grid via direct evaluation at coarse points is too crude; evaluate exactly on a moderate grid instead
def FT_l2r(xv, Lmax=300.0, n=60001):
    ls = np.linspace(0, Lmax, n)
    vals = np.array([complex(r_of(l)) for l in ls]) * ls**2 * np.exp(-1j * xv * ls)
    w = np.ones(n); w[0] = w[-1] = 0.5
    dl = ls[1] - ls[0]
    return (np.sum(w * vals) * dl).real / np.pi
for xv in [0.25, 0.5, 0.8]:
    v = FT_l2r(xv)
    check(f"FT[lambda^2 r](x={xv}) = {v:.6e} vs -rho''(x) = {-rho2(xv):.6e}", abs(v + rho2(xv)) < 2e-5, f"|diff| = {abs(v + rho2(xv)):.1e}")
v = FT_l2r(1.3)
check(f"FT[lambda^2 r](x=1.3) = {v:.2e} ~ 0 outside the support", abs(v) < 2e-5)

# ---------------- endpoint factors ----------------
a_, b_, y = sp.symbols('a b y', positive=True)
f = x**a_
check("rho ~ x^a  =>  rho''/rho = a(a-1)/x^2", sp.simplify(sp.diff(f, x, 2) / f - a_ * (a_ - 1) / x**2) == 0)
f = (1 - x)**b_
check("rho ~ (1-x)^b  =>  rho''/rho = b(b-1)/(1-x)^2", sp.simplify(sp.diff(f, x, 2) / f - b_ * (b_ - 1) / (1 - x)**2) == 0)

# ---------------- Cor. 5.3 with the BVZ renormalon kernels ----------------
# rho_4(x) = int_x^1 dy/y k(y) q(x/y);  k_par = y + (1-y)ln(1-y), k_perp = k_par + y(1-y)
k_par = lambda t: t + (1 - t) * np.log1p(-t) if t < 1 else 1.0
k_perp = lambda t: k_par(t) + t * (1 - t)
def rho4(xv, q, k):
    return integrate.quad(lambda t: k(t) * q(xv / t) / t, xv, 1, limit=400)[0]
for bexp in [2.0, 3.0, 4.5]:
    q = lambda t, bb=bexp: t**0.5 * (1 - t)**bb if 0 < t < 1 else 0.0
    xs = [1 - 1e-2, 1 - 1e-3, 1 - 1e-4]
    loc = []
    for k in (k_par, k_perp):
        r1, r2 = rho4(xs[1], q, k) / q(xs[1]), rho4(xs[2], q, k) / q(xs[2])
        loc.append(np.log(r2 / r1) / np.log((1 - xs[2]) / (1 - xs[1])))
    check(f"BVZ model, q~(1-x)^{bexp}: local exponent delta of rho_4/q at x->1 = {loc[0]:.4f} (par), {loc[1]:.4f} (perp)  -> 1",
          abs(loc[0] - 1) < 2e-3 and abs(loc[1] - 1) < 2e-3)
    # relative correction (Lambda^2/Pz^2) rho_4''/q ~ (b+1) b /(1-x): second derivative by finite differences
    def rel(xv, k=k_par, h=None):
        h = h or (1 - xv) * 1e-2
        d2 = (rho4(xv + h, q, k) - 2 * rho4(xv, q, k) + rho4(xv - h, q, k)) / h**2
        return d2 / q(xv)
    vals = [rel(xx) * (1 - xx) for xx in [1 - 1e-2, 1 - 1e-3]]
    # rho_4/q -> C (1-x) with C = k(1)/(b+1) = 1/(b+1), so (1-x) rho_4''/q -> C (b+1) b = b  (BVZ R -> b)
    check(f"q~(1-x)^{bexp}: (1-x) rho_4''/q -> C(b+1)b with C=1/(b+1), i.e. b = {bexp:.3f}: {vals[0]:.3f}, {vals[1]:.3f}",
          abs(vals[1] - bexp) < 0.01 * bexp)
# small-x: rho_4 ~ x^a for q ~ x^a (a<2) -> Lambda^2/(x^2 Pz^2)
q = lambda t: t**0.5 * (1 - t)**3 if 0 < t < 1 else 0.0
r1, r2 = rho4(1e-4, q, k_par) / q(1e-4), rho4(1e-6, q, k_par) / q(1e-6)
check(f"small x: rho_4/q -> const (delta_0 = 0): {r1:.6f}, {r2:.6f}", abs(r1 - r2) < 1e-2 * abs(r2))

# ---------------- P=0 normalization: [k]_+ = k - delta(1-y) int_0^1 k ----------------
t = sp.symbols('t', positive=True)
Ipar = sp.integrate(t + (1 - t) * sp.log(1 - t), (t, 0, 1))
Iperp = sp.integrate(t + (1 - t) * sp.log(1 - t) + t * (1 - t), (t, 0, 1))
check("int_0^1 (y + ybar ln ybar) dy = 1/4", sp.simplify(Ipar - sp.Rational(1, 4)) == 0, str(Ipar))
check("int_0^1 (y + ybar ln ybar + y ybar) dy = 5/12", sp.simplify(Iperp - sp.Rational(5, 12)) == 0, str(Iperp))
# normalized model: rho_4^norm = rho_4 - (1/4) q  =>  delta R = x^2 xbar (rho_4^norm - rho_4)''/q = -(1/4) x^2 xbar q''/q  (BVZ (bR))
qs = sp.Function('q')
xbar = 1 - x
dR = sp.simplify(x**2 * xbar * sp.diff(-sp.Rational(1, 4) * qs(x), x, 2) / qs(x))
check("normalization shift of R^par = -(1/4) xbar x^2 q''/q", sp.simplify(dR + sp.Rational(1, 4) * xbar * x**2 * sp.diff(qs(x), x, 2) / qs(x)) == 0)
# its endpoint behaviour: q ~ (1-x)^b => -(1/4) x^2 b(b-1)/(1-x)  in R, i.e. relative correction ~ 1/(1-x)^2 (delta = 0)
qb = (1 - x)**b_
shift = sp.simplify(-sp.Rational(1, 4) * sp.diff(qb, x, 2) / qb)
check("normalization term relative correction = -(1/4) b(b-1)/(1-x)^2  (Cor. 5.3 with delta=0)",
      sp.simplify(shift + sp.Rational(1, 4) * b_ * (b_ - 1) / (1 - x)**2) == 0)

print(f"\nSUMMARY n08: {PASS} PASS, {FAIL} FAIL")
