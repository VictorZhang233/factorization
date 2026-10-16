# -*- coding: utf-8 -*-
"""
scale_check.py -- mu_F independence of the Drell-Yan cross section at O(alpha_s).

  dsigma/dQ^2 = (sigma_0/s) sum_q e_q^2 int dx1 dx2 dz delta(x1 x2 z - tau) {
        [q(x1) qb(x2) + qb(x1) q(x2)] Delta_qqbar(z, mu_F)
      + [g(x1)(q(x2)+qb(x2)) + (q(x1)+qb(x1)) g(x2)] Delta_qg(z, mu_F) },
  Delta_qqbar = delta(1-z) + a [Delta^(1)_qqbar(z) + 2 P_qq(z) ln(Q^2/mu_F^2)],
  Delta_qg    =              a [Delta^(1)_qg(z)    +   P_qg(z) ln(Q^2/mu_F^2)],   a = alpha_s/(2 pi).
DGLAP (CONTEXT): d f_i/d ln mu^2 = a sum_j P_ij (x) f_j.

(A) Mellin space, exact symbolic algebra:  d sigma_N/d ln mu_F^2 = O(a^2).
(B) x space, numerically with toy PDFs: the O(a) terms of d sigma/d ln mu_F^2 cancel
    [Born x (d f/d ln mu^2) from DGLAP  vs  f x f x d Delta/d ln mu_F^2], using the CONTEXT convolution
    (P (x) f)(x) = int_x^1 dxi/xi P(x/xi) f(xi) and the plus prescription of CONTEXT.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate

RES = []
def report(name, ok, extra=''):
    RES.append((name, bool(ok)))
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)

# ------------------------------------------------------------------ (A) Mellin space
a, lF = sp.symbols('a ell_F')          # ell_F = ln(mu_F^2/Q^2)
qA, qbA, gA, qB, qbB, gB = sp.symbols('q_A qb_A g_A q_B qb_B g_B')
gqq, gqg, ggq, ggg = sp.symbols('gamma_qq gamma_qg gamma_gq gamma_gg')
D1qq, D1qg = sp.symbols('Delta1_qq Delta1_qg')
Dqq = 1 + a * (D1qq - 2 * gqq * lF)          # ln(Q^2/mu_F^2) = -ell_F
Dqg = a * (D1qg - gqg * lF)
sigma = (qA * qbB + qbA * qB) * Dqq + (gA * (qB + qbB) + (qA + qbA) * gB) * Dqg
# d/d ell_F: explicit + via PDFs (DGLAP in Mellin space; gamma_ij = int z^{N-1} P_ij); flavour-singlet mixing
# enters g only, which multiplies O(a) terms.  Sigma_N = sum over flavours of (q+qbar) -> symbol for brevity
Sig = sp.Symbol('Sigma')
dq = lambda q, g: a * (gqq * q + gqg * g)
dg = lambda g: a * (ggq * Sig + ggg * g)
deriv = sp.diff(sigma, lF) + sum(sp.diff(sigma, f) * df for f, df in [(qA, dq(qA, gA)), (qbA, dq(qbA, gA)), (qB, dq(qB, gB)), (qbB, dq(qbB, gB)), (gA, dg(gA)), (gB, dg(gB))])
deriv = sp.expand(deriv)
order1 = deriv.coeff(a, 1)
report('(A) Mellin space: O(a) part of d sigma_N / d ln mu_F^2 vanishes identically', sp.simplify(order1) == 0, '   [O(a^2) remainder: %d terms]' % len(sp.Add.make_args(deriv.coeff(a, 2))))
# show which terms cancel against which
print('      cancellation: gamma_qq terms (q qbar channel) and gamma_qg terms (q g channel) separately:',
      sp.simplify(order1.coeff(gqq)) == 0, sp.simplify(order1.coeff(gqg)) == 0)

# ------------------------------------------------------------------ (B) x space numerically
CF, TF = 4.0 / 3.0, 0.5
def q(x):  return 1.9 * x**-0.35 * (1 - x)**3.1 * (1 + 2.0 * x)
def qb(x): return 0.35 * x**-1.15 * (1 - x)**6.5
def g(x):  return 2.4 * x**-1.25 * (1 - x)**5.0
tau = 0.02

def conv_Pqq(f, x):
    """(P_qq (x) f)(x), P_qq = C_F[2 D_0 - (1+z) + 3/2 delta(1-z)];
    D_0 (x) f = int_x^1 dz [f(x/z)/z - f(x)]/(1-z) + f(x) ln(1-x)."""
    i1, _ = integrate.quad(lambda zz: (f(x / zz) / zz - f(x)) / (1 - zz), x, 1, epsabs=0, epsrel=1e-12, limit=400)
    i2, _ = integrate.quad(lambda zz: (1 + zz) * f(x / zz) / zz, x, 1, epsabs=0, epsrel=1e-12, limit=400)
    return CF * (2 * (i1 + f(x) * np.log(1 - x)) - i2 + 1.5 * f(x))

def conv_Pqg(f, x):
    i, _ = integrate.quad(lambda zz: TF * (zz**2 + (1 - zz)**2) * f(x / zz) / zz, x, 1, epsabs=0, epsrel=1e-12, limit=400)
    return i

# Born-type double convolution  B[F1,F2] = int dx1 dx2 delta(x1 x2 - tau) F1(x1) F2(x2) = int_tau^1 dx1/x1 F1(x1) F2(tau/x1)
def born(F1, F2):
    val, _ = integrate.quad(lambda x1: F1(x1) * F2(tau / x1) / x1, tau, 1, epsabs=0, epsrel=1e-10, limit=400)
    return val

# triple convolution with a distribution in z:  T[F1,F2;P] = int dx1 dx2 dz delta(x1 x2 z - tau) F1 F2 P(z)
def triple_reg(F1, F2, Preg):
    # int dx1 dz /(x1 z) F1(x1) F2(tau/(x1 z)) P(z),  tau/(x1 z) <= 1
    def inner(x1):
        zmin = tau / x1
        val, _ = integrate.quad(lambda zz: Preg(zz) * F2(tau / (x1 * zz)) / zz, zmin, 1, epsabs=0, epsrel=1e-11, limit=400)
        return F1(x1) * val / x1
    val, _ = integrate.quad(inner, tau, 1, epsabs=0, epsrel=1e-9, limit=400)
    return val

def triple_D0(F1, F2):
    # <D_0, phi>, phi(z) = F1(x1) F2(tau/(x1 z))/(x1 z) theta(z > tau/x1);  = int_{zmin}^1 (phi-phi(1))/(1-z) + phi(1) ln(1-zmin)
    def inner(x1):
        zmin = tau / x1
        phi = lambda zz: F2(tau / (x1 * zz)) / zz
        p1 = phi(1.0)
        val, _ = integrate.quad(lambda zz: (phi(zz) - p1) / (1 - zz), zmin, 1, epsabs=0, epsrel=1e-11, limit=400)
        return F1(x1) * (val + p1 * np.log(1 - zmin)) / x1
    val, _ = integrate.quad(inner, tau, 1, epsabs=0, epsrel=1e-9, limit=400)
    return val

# DGLAP-evolved pieces at O(a): dq = a (P_qq x q + P_qg x g), same for qbar
Pq = lambda x: conv_Pqq(q, x); Pqb = lambda x: conv_Pqq(qb, x); Pgq = lambda x: conv_Pqg(g, x)
# (i) Born x (d f/d ln mu^2)  [q qbar channel, both orderings]
term_pdf_qq = born(Pq, qb) + born(q, Pqb) + born(Pqb, q) + born(qb, Pq)
term_pdf_qg = born(Pgq, qb) + born(q, Pgq) + born(Pgq, q) + born(qb, Pgq)   # P_qg x g enters both q and qbar
# (ii) f x f x dDelta/d ln mu_F^2 :  d/d ln mu_F^2 [2 P_qq ln(Q^2/mu_F^2)] = -2 P_qq ; d/d ln mu_F^2 [P_qg ln] = -P_qg
def triple_Pqq(F1, F2):
    return CF * (2 * triple_D0(F1, F2) - triple_reg(F1, F2, lambda zz: 1 + zz) + 1.5 * born(F1, F2))
term_coef_qq = -2 * (triple_Pqq(q, qb) + triple_Pqq(qb, q))
Pqg_reg = lambda zz: TF * (zz**2 + (1 - zz)**2)
term_coef_qg = -(triple_reg(g, lambda x: q(x) + qb(x), Pqg_reg) + triple_reg(lambda x: q(x) + qb(x), g, Pqg_reg))
print('      q qbar: Born x dPDF = %.12e ; PDFs x dDelta = %.12e' % (term_pdf_qq, term_coef_qq))
print('      q g   : Born x dPDF = %.12e ; PDFs x dDelta = %.12e' % (term_pdf_qg, term_coef_qg))
r_qq = abs(term_pdf_qq + term_coef_qq) / abs(term_pdf_qq)
r_qg = abs(term_pdf_qg + term_coef_qg) / abs(term_pdf_qg)
report('(B) x space, q qbar sector: Born x P_qq-evolution + PDFs x d(2 P_qq ln)/dln mu_F^2 = 0', r_qq < 1e-7, '(rel. residual %.1e)' % r_qq)
report('(B) x space, q g sector:    Born x P_qg-evolution + PDFs x d(P_qg ln)/dln mu_F^2 = 0', r_qg < 1e-7, '(rel. residual %.1e)' % r_qg)
# sanity: with a WRONG factor (1 instead of 2 in front of P_qq ln) the cancellation fails
r_wrong = abs(term_pdf_qq + term_coef_qq / 2) / abs(term_pdf_qq)
report('(B) control: coefficient 1 instead of 2 for P_qq ln(Q^2/mu_F^2) would leave O(1) residual', r_wrong > 0.1, '(rel. residual %.2f)' % r_wrong)

print()
print('SUMMARY scale_check: %d/%d PASS' % (sum(ok for _, ok in RES), len(RES)))
