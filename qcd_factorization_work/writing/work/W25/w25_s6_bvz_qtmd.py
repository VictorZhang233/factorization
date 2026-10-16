#!/usr/bin/env python3
"""W25 / Ch22 -- s6: renormalon model of the twist-4 term (prop:lamet-bvz) and one-loop quasi-TMD checks
(thm:lamet-quasi-tmd(b), ex:lamet-qtmd-oneloop, prop:lattice-cs-kernel, def:lamet-soft-offlc, def:lamet-reduced-soft),
and the Lorentzian smearing bound (lem:lamet-lorentzian).

B1  d^2/dx^2 int_{|x|}^1 dy/y (y + ybar ln ybar) q(x/y) = x^-2 { int dy/y y^2/[1-y]_+ q(x/y) + q(x) - x q'(x) }, [0,1] plus,
    for x > 0 AND x < 0 (test function with quark and antiquark parts, different from LAMET s4); the q ln(1-x) term
    appears when the plus integral is written over [|x|,1]; dropping it fails
B2  perp kernel y + ybar ln ybar + y ybar: same structure with the extra -2y term
B3  int_0^1 k = 1/4, int_0^1 (k + a abar) = 5/12;  |kappa| = pi e^{5/3+2gE}/(4 beta0) = 1.47 (nf=3), 1.58 (nf=4)
B4  Borel variable: BVZ e^{-w/(beta0 a_s)} with a_s = alpha_s/(4pi) equals our e^{-t/alpha_s} with u = beta0 t/(4pi) -> w = u
Q1  quasi-TMD one loop: c = 1/2, H^(1), momentum evolution G^(1) = (alpha_s C_F/pi)(1 - L_zeta), printed exponent fails
Q2  CS-kernel ratio returns K^(1) = -2 a L_b exactly
Q3  off-light-cone soft function: time-like sigma = 1 case of the one-loop soft factor -> a(2 - 2Y)L_b + O(Y e^{-2Y});
    D^(1) = 2 a L_b, S_r = e^{-D} = 1 - (alpha_s C_F/pi) L_b, mu^2 d ln S_r/d mu^2 = -alpha_s C_F/pi = gamma_HH^(1)
L1  Lorentzian smearing: e^{-delta|lam|} <-> (1/pi) delta/(delta^2+u^2); bound sup|q1-q2| <= (delta/pi)(||q2''|| + 4||q2||)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

mp.mp.dps = 25
# ---------------------------------------------------------------- B1/B2
def qf(x):
    x = mp.mpf(x)
    if 0 < x < 1: return x**mp.mpf(0.4) * (1 - x)**mp.mpf(2.5) * (1 + 2 * x)
    if -1 < x < 0: return -mp.mpf('0.5') * (-x)**mp.mpf(0.4) * (1 + x)**mp.mpf(4.5)
    return mp.mpf(0)
def dq(x): return mp.diff(qf, x)
k_par = lambda y: y + (1 - y) * mp.log(1 - y) if y < 1 else mp.mpf(1)
k_perp = lambda y: k_par(y) + y * (1 - y)
def F(x, k): return mp.quad(lambda y: k(y) * qf(x / y) / y, [abs(x), (abs(x) + 1) / 2, 1])
def F2(x, k, h=mp.mpf('1e-3')): return (F(x + h, k) - 2 * F(x, k) + F(x - h, k)) / h**2
def rhs(x, perp, withlog=True):
    X = abs(x)
    pv = mp.quad(lambda y: (y * qf(x / y) - qf(x)) / (1 - y), [X, (X + 1) / 2, 1])
    extra = mp.quad(lambda y: -2 * y * qf(x / y), [X, 1]) if perp else 0
    return (pv + extra + (qf(x) * mp.log(1 - X) if withlog else 0) + (2 if perp else 1) * qf(x) - x * dq(x)) / x**2
for perp in (False, True):
    for xv in (0.25, 0.6, -0.3, -0.7):
        l, r_, rn = F2(mp.mpf(xv), k_perp if perp else k_par), rhs(mp.mpf(xv), perp), rhs(mp.mpf(xv), perp, False)
        tag = 'perp' if perp else 'par'
        check("B1 %s identity at x=%+.2f with [0,1] plus distribution and -x q'(x)" % (tag, xv), abs(l - r_) < 2e-4 * max(1, abs(l)),
              "%s vs %s" % (mp.nstr(l, 9), mp.nstr(r_, 9)))
        check("B1 %s: dropping q(x) ln(1-|x|) fails at x=%+.2f" % (tag, xv), abs(l - rn) > 1e-3)
# -|x| q'(x) would be wrong for x < 0
xv = mp.mpf(-0.3)
wrong = rhs(xv, False) + (-abs(xv) * dq(xv) + xv * dq(xv)) / xv**2
check("B1 for x<0 the term is -x q'(x) (the form with -|x| q'(x) fails)", abs(F2(xv, k_par) - wrong) > 1e-3)

# ---------------------------------------------------------------- B3
a = sp.Symbol('alpha', positive=True)
kpar = a + (1 - a) * sp.log(1 - a)
check("B3 int_0^1 (alpha + abar ln abar) = 1/4", sp.simplify(sp.integrate(kpar, (a, 0, 1)) - sp.Rational(1, 4)) == 0)
check("B3 int_0^1 (alpha + abar ln abar + alpha abar) = 5/12",
      sp.simplify(sp.integrate(kpar + a * (1 - a), (a, 0, 1)) - sp.Rational(5, 12)) == 0)
for nf in (3, 4):
    beta0 = 11 - mp.mpf(2) / 3 * nf
    kap = mp.pi * mp.e**(mp.mpf(5) / 3 + 2 * mp.euler) / (4 * beta0)
    print("   |kappa| (nf=%d, beta0=%s) = %s" % (nf, mp.nstr(beta0, 4), mp.nstr(kap, 4)))
check("B3 |kappa| ~ 1.5", abs(mp.pi * mp.e**(mp.mpf(5) / 3 + 2 * mp.euler) / (4 * 9) - 1.466) < 0.01)

# ---------------------------------------------------------------- B4
w, t, als, b0 = sp.symbols('w t alpha_s beta0', positive=True)
check("B4 e^{-w/(beta0 a_s)}, a_s = alpha_s/(4 pi), equals e^{-t/alpha_s} iff w = beta0 t/(4 pi) = u",
      sp.simplify((w / (b0 * als / (4 * sp.pi))).subs(w, b0 * t / (4 * sp.pi)) - t / als) == 0)

# ---------------------------------------------------------------- Q1/Q2
Lb, Lz, Lze, c = sp.symbols('L_b L_zeta L_zetaS c', real=True)   # L_zeta = ln(zeta_z/mu^2), L_zetaS = ln(zeta/mu^2)
ft1 = -sp.Rational(1, 2) * Lb**2 + Lb * (sp.Rational(5, 2) - Lz) - sp.Rational(3, 2) - sp.Rational(1, 2) * Lz**2 + Lz
fT1 = -sp.Rational(1, 2) * Lb**2 + (sp.Rational(3, 2) - Lze) * Lb + sp.Rational(1, 2) - sp.pi**2 / 12
K1 = -2 * Lb; Sr1 = -2 * Lb
expr = sp.expand(ft1 + Sr1 / 2 - c * K1 * (Lz - Lze) - fT1)       # = H^(1) must be L_b independent
csol = sp.solve(sp.Poly(expr, Lb).coeff_monomial(Lb), c)
check("Q1 coefficient of K ln(zeta_z/zeta) fixed to c = 1/2", csol == [sp.Rational(1, 2)], csol)
H1 = sp.simplify(expr.subs(c, sp.Rational(1, 2)))
check("Q1 H^(1) = -2 + pi^2/12 - L_zeta^2/2 + L_zeta", sp.simplify(H1 - (-2 + sp.pi**2 / 12 - Lz**2 / 2 + Lz)) == 0, H1)
resid = sp.simplify(sp.Poly(sp.expand(ft1 + Sr1 / 2 - K1 * (Lz - Lze) - fT1), Lb).coeff_monomial(Lb))
check("Q1 printed exponent (c = 1) leaves a residual L_b (L_zeta - ln(zeta/mu^2))", sp.simplify(resid - (Lz - Lze)) == 0, resid)
check("Q1 2 zeta_z d ln f~/d zeta_z = K + G, G^(1) = 2a(1 - L_zeta)",
      sp.simplify(2 * sp.diff(ft1, Lz) - (K1 + 2 * (1 - Lz))) == 0)
check("Q1 G = 2 zeta_z d ln H/d zeta_z at one loop", sp.simplify(2 * sp.diff(H1, Lz) - 2 * (1 - Lz)) == 0)
check("Q1 constants: -3/2 - 1/2 = -2 (from f~ and f^TMD) gives the -2 of H^(1)", sp.Rational(-3, 2) - sp.Rational(1, 2) == -2)
# CS ratio: K = [ln(H(P2) f~(P1)) - ln(H(P1) f~(P2))]/ln(P1/P2), L_zeta,i = L0 + 2 ln P_i
l1, l2, L0 = sp.symbols('l1 l2 L0', real=True)
Hf = lambda L: -2 + sp.pi**2 / 12 - L**2 / 2 + L
fl = lambda L: ft1.subs(Lz, L)
num = (Hf(L0 + 2 * l2) + fl(L0 + 2 * l1)) - (Hf(L0 + 2 * l1) + fl(L0 + 2 * l2))
check("Q2 CS-kernel ratio formula returns K^(1) = -2 a L_b", sp.simplify(sp.expand(num) / (l1 - l2) - K1) == 0)
xx, P1, P2 = sp.symbols('x P1 P2', positive=True)
check("Q2 (zeta_z1/zeta_z2)^{K/2} = (P1/P2)^K at fixed x  (zeta_z = (2 x P^z)^2)",
      sp.simplify(sp.expand_log(sp.Rational(1, 2) * sp.log((2 * xx * P1)**2 / (2 * xx * P2)**2), force=True)
                  - sp.expand_log(sp.log(P1 / P2), force=True)) == 0)

# ---------------------------------------------------------------- Q3 soft function
Y = sp.Symbol('Y', positive=True)
one_loop_soft = -2 * (Y * sp.coth(Y) - 1) * Lb       # -(alpha_s C_F/pi)(Y coth Y - sigma) L_b with sigma = 1, in units of a
diffY = sp.simplify(one_loop_soft - (2 - 2 * Y) * Lb)
check("Q3 time-like (sigma=1) one-loop soft factor = a(2 - 2Y) L_b + O(Y e^{-2Y})",
      sp.limit(sp.simplify(diffY / Lb) * sp.exp(Y), Y, sp.oo) == 0)
check("Q3 Y coth Y - Y = 2Y/(e^{2Y}-1) (numerically at Y = 0.3, 2, 7)",
      all(abs(float(sp.N((Y * sp.coth(Y) - Y - 2 * Y / (sp.exp(2 * Y) - 1)).subs(Y, v)))) < 1e-12 for v in (0.3, 2, 7)))
D1 = 2 * Lb                                            # ln S = (Y+Y')K + D: K^(1) = -2 a L_b, D^(1) = 2 a L_b
check("Q3 S_r = e^{-D}: S_r^(1) = -2 a L_b = -(alpha_s C_F/pi) L_b", -D1 == Sr1)
check("Q3 mu^2 d ln S_r/d mu^2 = -2a = -alpha_s C_F/pi = gamma_HH^(1) (dL_b/d ln mu^2 = 1)", sp.diff(-D1, Lb) == -2)

# ---------------------------------------------------------------- L1 Lorentzian
uu, dl = sp.symbols('u delta', positive=True)
lam = sp.Symbol('lambda', real=True)
Lr = sp.integrate(2 * sp.exp(-dl * lam) * sp.cos(uu * lam), (lam, 0, sp.oo), conds='none') / (2 * sp.pi)
check("L1 int dlam/(2pi) e^{-iu lam} e^{-delta|lam|} = (1/pi) delta/(delta^2+u^2)", sp.simplify(Lr - dl / (sp.pi * (dl**2 + uu**2))) == 0)
# bound pieces: (delta/pi) int_{-1}^1 u^2/(delta^2+u^2) du <= 2 delta/pi ; int_{|u|>1} L = (2/pi) arctan(delta) <= 2 delta/pi
check("L1 int_{|u|>=1} (1/pi) delta/(delta^2+u^2) du = (2/pi) arctan(delta)",
      sp.simplify(2 * sp.integrate(dl / (sp.pi * (dl**2 + uu**2)), (uu, 1, sp.oo)) - 2 / sp.pi * sp.atan(dl)) == 0)
def q2f(y): return mp.e**(-y**2) * (1 + mp.mpf('0.3') * mp.sin(3 * y))
def q1f(y, d): return mp.quad(lambda u: d / (mp.pi * (d**2 + u**2)) * q2f(y - u), [-mp.inf, -1, 0, 1, mp.inf])
for d in (mp.mpf('0.05'), mp.mpf('0.2')):
    diffs = [abs(q1f(mp.mpf(y), d) - q2f(mp.mpf(y))) for y in (-1.2, -0.4, 0, 0.3, 0.9, 1.7)]
    q2pp = max(abs(mp.diff(q2f, mp.mpf(y), 2)) for y in mp.linspace(-4, 4, 161))
    q2max = max(abs(q2f(mp.mpf(y))) for y in mp.linspace(-4, 4, 161))
    bound = d / mp.pi * (q2pp + 4 * q2max)
    check("L1 sup|q1 - q2| <= (delta/pi)(||q2''|| + 4||q2||) at delta=%s (max diff %s <= bound %s)" % (mp.nstr(d, 3), mp.nstr(max(diffs), 4), mp.nstr(bound, 4)),
          max(diffs) <= bound)
    check("L1 the correction is linear in delta: max diff / delta = %s" % mp.nstr(max(diffs) / d, 4), max(diffs) / d < 10)

print("\nSUMMARY w25_s6_bvz_qtmd: %d PASS, %d FAIL" % (NP, NF))
