#!/usr/bin/env python3
"""s4: (A) one-loop consistency of the quasi-TMD factorization formula (Ji-Liu-Liu PLB 2020 / RMP 2021 / ESZ 2019 /
         ESSZ 2022): determine the coefficient c in  f~ sqrt(S_r) = H exp[c K ln(zeta_z/zeta)] f^TMD  from the one-loop
         expressions quoted in RMP 93 (2021) 035005, and check H, K, G and the ESZ Collins-Soper-kernel ratio formula.
     (B) Braun-Vladimirov-Zhang (PRD 99 014013) power-correction formula for the quasi-PDF: check the identity
         (d/dx)^2 int_x^1 dy/y (y + ybar ln ybar) q(x/y) = x^{-2}{ int_x^1 dy/y y^2/[1-y]_+ q(x/y) + q(x) - x q'(x) }
         and which reading of [1-y]_+ is correct; and the large-x behaviour of R_Q.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate

PASS = 0; FAIL = 0
def check(name, ok):
    global PASS, FAIL
    print(("PASS " if ok else "FAIL ") + name)
    if ok: PASS += 1
    else: FAIL += 1

# ---------------- (A) quasi-TMD at one loop ----------------
a, Lb, Lz, Lzeta, c = sp.symbols('a L_b L_z L_zeta c', real=True)   # Lz = ln(zeta_z/mu^2), Lzeta = ln(zeta/mu^2)
ftilde1 = -sp.Rational(1, 2) * Lb**2 + Lb * (sp.Rational(5, 2) - Lz) - sp.Rational(3, 2) - sp.Rational(1, 2) * Lz**2 + Lz
fTMD1 = -sp.Rational(1, 2) * Lb**2 + (sp.Rational(3, 2) - Lzeta) * Lb + sp.Rational(1, 2) - sp.pi**2 / 12
K1 = -2 * Lb             # K = -(alpha_s C_F/pi) L_b = -2 a L_b
Sr1 = -2 * Lb            # S_r = e^{-D}, D^(1) = 2 a L_b
# one-loop: ftilde1 + Sr1/2 = H1 + c K1 (Lz - Lzeta) + fTMD1  ; solve for c and H1 (must be L_b independent)
expr = sp.expand(ftilde1 + Sr1 / 2 - fTMD1 - c * K1 * (Lz - Lzeta))
coeff_Lb = sp.Poly(expr, Lb).coeff_monomial(Lb)
csol = sp.solve(sp.Eq(coeff_Lb, 0), c)
check("A exponent coefficient c = 1/2  (i.e. exp[ (1/2) K ln(zeta_z/zeta) ]), found c = %s" % csol, csol == [sp.Rational(1, 2)])
H1 = sp.simplify(expr.subs(c, sp.Rational(1, 2)))
check("A H^(1) = -2 + pi^2/12 - L_z^2/2 + L_z  (found %s)" % H1,
      sp.simplify(H1 - (-2 + sp.pi**2 / 12 - Lz**2 / 2 + Lz)) == 0)
# with c = 1 (as printed in RMP eq. quasiTMDmatch / PLB 811 eq. 13) the L_b dependence would not cancel:
res_c1 = sp.simplify(sp.Poly(sp.expand(ftilde1 + Sr1 / 2 - fTMD1 - 1 * K1 * (Lz - Lzeta)), Lb).coeff_monomial(Lb))
check("A with c=1 a residual L_b*(L_z - L_zeta) term survives (=%s): printed exponent is a factor-2 typo" % res_c1,
      sp.simplify(res_c1) != 0)
# momentum evolution: P^z d/dP^z ln f~ = 2 d/dLz ln f~ = K + G, G^(1) = (alpha_s C_F/pi)(1 - L_z) = 2a(1-L_z)
KG = sp.expand(2 * sp.diff(ftilde1, Lz))
check("A P^z d/dP^z ln f~ = K + G with K=-2aL_b, G=2a(1-L_z)", sp.simplify(KG - (K1 + 2 * (1 - Lz))) == 0)
check("A G = 2 dH/dLz (one loop)", sp.simplify(2 * sp.diff(H1, Lz) - 2 * (1 - Lz)) == 0)
# ESZ ratio: gamma_zeta = [ln(C(P2) f~(P1)) - ln(C(P1) f~(P2))]/ln(P1/P2), one loop, Lz_i = ln(4x^2 P_i^2/mu^2)
lP1, lP2 = sp.symbols('lP1 lP2', real=True)   # ln(P_i) shifts: Lz_i = Lz0 + 2 lP_i
Lz0 = sp.symbols('Lz0', real=True)
C1 = lambda L: 2 * (-sp.Rational(1, 2) * L**2 + L - 2 + sp.pi**2 / 12) / 2   # ESZ C^(1) * alpha_s C_F/(4pi) = a * (H1)
f1 = lambda L: ftilde1.subs(Lz, L)
num = (C1(Lz0 + 2 * lP2) + f1(Lz0 + 2 * lP1)) - (C1(Lz0 + 2 * lP1) + f1(Lz0 + 2 * lP2))
gz = sp.simplify(sp.expand(num) / (lP1 - lP2))
check("A ESZ ratio formula returns gamma_zeta^(1) = K^(1) = -2 a L_b (found %s)" % gz, sp.simplify(gz - K1) == 0)
# note: ESZ C(mu, xP^z) multiplies f^TMD to give f~, i.e. it is 1/H_RMP = e^{+h}: consistent with H1 sign conventions
# (here C1 = +H1 since f~ = C f).

# ---------------- (B) BVZ identity ----------------
qf = lambda x: x**-0.5 * (1 - x)**3
dq = lambda x: -0.5 * x**-1.5 * (1 - x)**3 - 3 * x**-0.5 * (1 - x)**2
def Fconv(x):
    k = lambda y: y + (1 - y) * np.log(1 - y) if y < 1 else 1.0
    return integrate.quad(lambda y: k(y) * qf(x / y) / y, x, 1, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2
def rhs(x, with_log):
    pv = integrate.quad(lambda y: (y * qf(x / y) - qf(x)) / (1 - y), x, 1, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
    return (pv + (qf(x) * np.log(1 - x) if with_log else 0.0) + qf(x) - x * dq(x)) / x**2
for x in (0.2, 0.5, 0.8):
    lhs = second_derivative(Fconv, x, 1e-3)
    r_log = rhs(x, True); r_nolog = rhs(x, False)
    print("   x=%.2f  F''(x)=%.6f   rhs([0,1]-plus incl. q ln(1-x))=%.6f   rhs(no log)=%.6f" % (x, lhs, r_log, r_nolog))
    check("B BVZ identity at x=%.2f with the [0,1] plus distribution" % x, abs(lhs - r_log) < 1e-3 * max(1, abs(lhs)))
    check("B (the R_Q formula of BVZ eq. (cR), which drops q(x) ln(1-x), differs) x=%.2f" % x, abs(lhs - r_nolog) > 1e-3)

# perpendicular (gamma^0) case: kernel y + ybar ln ybar + y ybar ; BVZ eq. (t4-Qperp) second line vs (cR) R_perp
def Fconv_perp(x):
    k = lambda y: y + (1 - y) * np.log(1 - y) + y * (1 - y) if y < 1 else 1.0
    return integrate.quad(lambda y: k(y) * qf(x / y) / y, x, 1, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
def rhs_perp(x, with_log):
    pv = integrate.quad(lambda y: (y * qf(x / y) - qf(x)) / (1 - y), x, 1, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
    m2 = integrate.quad(lambda y: -2 * y * qf(x / y), x, 1, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
    return (pv + m2 + (qf(x) * np.log(1 - x) if with_log else 0.0) + 2 * qf(x) - x * dq(x)) / x**2
for x in (0.2, 0.5, 0.8):
    lhs = second_derivative(Fconv_perp, x, 1e-3)
    r_log = rhs_perp(x, True); r_nolog = rhs_perp(x, False)
    print("   perp x=%.2f  F''(x)=%.6f   rhs(incl. q ln(1-x))=%.6f   rhs(no log, = eq. cR)=%.6f" % (x, lhs, r_log, r_nolog))
    check("B perp: BVZ (t4-Qperp) identity at x=%.2f with the [0,1] plus distribution" % x, abs(lhs - r_log) < 1e-3 * max(1, abs(lhs)))
    check("B perp: R_perp of eq. (cR) (drops q ln(1-x)) differs at x=%.2f" % x, abs(lhs - r_nolog) > 1e-3)

# large-x behaviour of R_Q (with the correct rhs): q ~ (1-x)^b -> x^2 xbar F''/q -> const
for b in (2.0, 3.0):
    qb = lambda x: (1 - x)**b
    dqb = lambda x: -b * (1 - x)**(b - 1)
    def Rq(x):
        pv = integrate.quad(lambda y: (y * qb(x / y) - qb(x)) / (1 - y), x, 1, limit=400)[0]
        return (1 - x) / qb(x) * (pv + qb(x) * np.log(1 - x) + qb(x) - x * dqb(x))
    vals = [Rq(x) for x in (0.9, 0.99, 0.999)]
    print("   b=%.0f: R_Q(0.9,0.99,0.999) = %s" % (b, ["%.4f" % v for v in vals]))
    check("B R_Q(x->1) tends to a constant (power correction ~ 1/(x^2 (1-x) P^2)) for b=%.0f" % b,
          abs(vals[2] - vals[1]) < 0.05 * abs(vals[2]) + 0.05)

print("\nSUMMARY s4: %d PASS, %d FAIL" % (PASS, FAIL))
