# -*- coding: utf-8 -*-
"""
s3_erbl_eigen.py -- item (1): eigenfunctions/eigenvalues of the LO ERBL kernel, one-loop anomalous dimensions
of Gegenbauer moments, comparison with DGLAP moments and with the literature exponents, numerical checks.

Evolution equation (normalization derived in s2):
   mu^2 d/dmu^2 phi(x,mu) = (alpha_s(mu)/2pi) int_0^1 dy V(x,y) phi(y,mu),
   V(x,y) = C_F [ x/y (1 + 1/(y-x)) th(y-x) + xbar/ybar (1 + 1/(x-y)) th(x-y) ]_+ ,
   [V]_+(x,y) = V(x,y) - delta(x-y) int_0^1 dt V(t,y).
Run:  python3 -I s3_erbl_eigen.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np
import mpmath as mp

ck = Checker('s3_erbl_eigen')
x, y, z = sp.symbols('x y z', positive=True)
CF = sp.Rational(4, 3)
Cg = lambda n, t: sp.gegenbauer(n, sp.Rational(3, 2), t)


def Vconv(phi):
    """(V_+ (x) phi)(x)/C_F, exact, for polynomial phi(y) vanishing at y=0,1 (sympy expression in y)"""
    phix = phi.subs(y, x)
    # y > x : (1 + 1/(y-x)) [ x/y phi(y) - ybar/xbar phi(x) ]
    A = sp.cancel(x / y * phi - (1 - y) / (1 - x) * phix)
    A = sp.cancel(A * (1 + 1 / (y - x)))
    # y < x : (1 + 1/(x-y)) [ xbar/ybar phi(y) - y/x phi(x) ]
    Bq = sp.cancel((1 - x) / (1 - y) * phi - y / x * phix)
    Bq = sp.cancel(Bq * (1 + 1 / (x - y)))
    return sp.simplify(sp.integrate(sp.expand(A), (y, x, 1)) + sp.integrate(sp.expand(Bq), (y, 0, x)))


def H(n):
    return sum(sp.Rational(1, j) for j in range(1, n + 1))


lam_formula = lambda n: -sp.Rational(1, 2) + sp.Rational(1, (n + 1) * (n + 2)) - 2 * sum(sp.Rational(1, j) for j in range(2, n + 2))
gam = lambda n: 2 * CF * (1 - sp.Rational(2, (n + 1) * (n + 2)) + 4 * sum(sp.Rational(1, j) for j in range(2, n + 2)))

print('=== 1. Gegenbauer eigenfunctions: V (x) [y ybar C_n(2y-1)] = lambda_n x xbar C_n(2x-1) ===')
lams = {}
okall = True
for n in range(0, 11):
    phin = y * (1 - y) * Cg(n, 2 * y - 1)
    res = Vconv(phin)
    target = x * (1 - x) * Cg(n, 2 * x - 1)
    ratio = sp.simplify(res / target)
    lams[n] = ratio
    good = (ratio.free_symbols == set()) and sp.simplify(ratio - lam_formula(n)) == 0
    okall &= good
    print('   n=%2d  lambda_n/C_F = %-14s  formula: %s' % (n, str(ratio), str(lam_formula(n))))
ck.check('eigenvalues lambda_n/C_F = -1/2 + 1/((n+1)(n+2)) - 2 sum_{j=2}^{n+1} 1/j  (n = 0..10, exact)', okall)
ck.check('lambda_0 = 0  (axial current conserved: f_pi is scale independent)', lams[0] == 0)
ck.check('lambda_2 = -25/12 C_F', sp.simplify(lams[2] + sp.Rational(25, 12)) == 0)
ok = all(sp.simplify(gam(n) - 8 * CF * (H(n + 1) - sp.Rational(3, 4) - sp.Rational(1, 2 * (n + 1) * (n + 2)))) == 0 for n in range(0, 30))
ck.check('gamma_n = -4 C_F lambda_n = 2 C_F[1 - 2/((n+1)(n+2)) + 4 sum_{j=2}^{n+1} 1/j] = 8 C_F[H_{n+1} - 3/4 - 1/(2(n+1)(n+2))]', ok)
ck.check('gamma_n = -4 C_F lambda_n for n = 0..10', all(sp.simplify(gam(n) + 4 * CF * lams[n]) == 0 for n in range(0, 11)))

print('=== 2. triangularity (polynomial preservation) ===')
ok = True
for kdeg in range(0, 9):
    res = sp.simplify(Vconv(y * (1 - y) * y ** kdeg) / (x * (1 - x)))
    poly = sp.Poly(sp.expand(sp.cancel(res)), x)
    if not (res.is_polynomial(x) and poly.degree() <= kdeg):
        ok = False
        print('   not triangular at k=', kdeg, res)
ck.check('V maps x xbar * (polynomials of degree <= k) into itself (k = 0..8)', ok)
print('   [with the hermiticity V(x,y) y ybar = V(y,x) x xbar (s2), the eigenfunctions are the orthogonal')
print('    polynomials for the weight x(1-x) on [0,1], i.e. C_n^{3/2}(2x-1): a proof valid for all n]')

# moment-space triangularity: (V^T P)(x) = int dy V(y,x)[P(y) - P(x)] maps P_n into P_n
def VTconv(Pp):
    Px = Pp.subs(y, x)
    # y < x : V(y,x) = (y/x)(1 + 1/(x-y)) ;  y > x : V(y,x) = (ybar/xbar)(1 + 1/(y-x))
    A1 = sp.cancel(y / x * (1 + 1 / (x - y)) * (Pp - Px))
    A2 = sp.cancel((1 - y) / (1 - x) * (1 + 1 / (y - x)) * (Pp - Px))
    return sp.simplify(sp.integrate(sp.expand(A1), (y, 0, x)) + sp.integrate(sp.expand(A2), (y, x, 1)))
ok = True
for nd in range(0, 11):
    r = sp.cancel(VTconv(y ** nd))
    if not (r.is_polynomial(x) and sp.Poly(sp.expand(r), x).degree() <= nd):
        ok = False
        print('   V^T not degree preserving at n=', nd, r)
ck.check('V^T (moment space) maps polynomials of degree <= n into themselves (n = 0..10)', ok)
Ptest = y ** 3 + 2 * y - sp.Rational(1, 3)
ck.zero('exact identity V (x) [y ybar P(y)] = x xbar (V^T P)(x)  (plus prescriptions included; test polynomial)',
        sp.simplify(Vconv(y * (1 - y) * Ptest) - x * (1 - x) * VTconv(Ptest)))

print('=== 3. comparison with the DGLAP non-singlet moments ===')
zz = sp.symbols('zz', positive=True)
def Pqq_moment(N):
    # int_0^1 z^{N-1} C_F [(1+z^2)/(1-z)]_+ dz = C_F int_0^1 (z^{N-1}-1)(1+z^2)/(1-z) dz
    return sp.simplify(CF * sp.integrate(sp.cancel((zz ** (N - 1) - 1) * (1 + zz ** 2) / (1 - zz)), (zz, 0, 1)))
ok = all(sp.simplify(Pqq_moment(n + 1) - CF * lams[n]) == 0 for n in range(0, 11))
ck.check('C_F lambda_n = int_0^1 z^n P_qq(z) dz  (n = 0..10): ERBL eigenvalues = DGLAP moments at N = n+1', ok)
ck.check('closed form: int z^{N-1} P_qq = C_F[3/2 + 1/(N(N+1)) - 2 H_N]',
         all(sp.simplify(Pqq_moment(N) - CF * (sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * H(N))) == 0 for N in range(1, 12)))

print('=== 4. literature values of the exponents ===')
beta0 = lambda nf: 11 - sp.Rational(2, 3) * nf
expo = lambda n, nf: gam(n) / (2 * beta0(nf))
ck.check('gamma_0 = 0', gam(0) == 0)
ck.check('gamma_2 = 25 C_F/3 = 100/9', sp.simplify(gam(2) - sp.Rational(100, 9)) == 0)
ck.check('a_2 exponent gamma_2/(2 beta_0) = 50/81 for n_f = 3 (standard value)', expo(2, 3) == sp.Rational(50, 81), str(expo(2, 3)))
ck.check('a_2 exponent = 2/3 for n_f = 4', expo(2, 4) == sp.Rational(2, 3), str(expo(2, 4)))
ck.check('a_4 exponent = 364/405 for n_f = 3', expo(4, 3) == sp.Rational(364, 405), str(expo(4, 3)))
# Lepage-Brodsky form: (ln Q^2/Lambda^2)^{-gamma_n^{LB}}, gamma_n^{LB} = (C_F/beta0)[1 + 4 sum_{k=2}^{n+1} 1/k - 2/((n+1)(n+2))]
gLB = lambda n, nf: CF / beta0(nf) * (1 + 4 * sum(sp.Rational(1, k) for k in range(2, n + 2)) - sp.Rational(2, (n + 1) * (n + 2)))
ck.check('identical to the Lepage-Brodsky exponent (C_F/beta_0)[1 + 4 sum_{k=2}^{n+1} 1/k - 2/((n+1)(n+2))]',
         all(sp.simplify(gLB(n, nf) - expo(n, nf)) == 0 for n in range(0, 12) for nf in (3, 4, 5)))
gl = [float(gam(n)) for n in range(0, 61, 2)]
ck.check('gamma_n > 0 and increasing for even n = 2..60 (=> phi -> 6x(1-x) as mu -> infinity)',
         all(g > 0 for g in gl[1:]) and all(gl[i + 1] > gl[i] for i in range(len(gl) - 1)))
# H_{n+1} = ln(n+1) + gamma_E + 1/(2(n+1)) + O(n^-2)  =>  gamma_n = 8 C_F [ln(n+1) + gamma_E - 3/4 + 1/(2(n+1))] + O(n^-2)
nl = 400
ck.check('large-n behaviour gamma_n = 8 C_F [ln n + gamma_E - 3/4] + O(1/n)  (coefficient of ln n = 2 x 4 C_F, cusp)',
         abs(float(gam(nl)) / (8 * float(CF) * (np.log(nl + 1) + np.euler_gamma - 0.75 + 0.5 / (nl + 1))) - 1) < 1e-5)

print('=== 5. numerical plus-prescription check (direct quadrature, non-polynomial DA) ===')
mp.mp.dps = 30
def geg(n, t):
    # Gegenbauer C_n^{3/2}(t) by the stable three-term recurrence (mpmath's hypergeometric form fails near t=-1)
    lam_ = mp.mpf(3) / 2
    c0, c1 = mp.mpf(1), 2 * lam_ * t
    if n == 0:
        return c0
    for m in range(2, n + 1):
        c0, c1 = c1, (2 * t * (m + lam_ - 1) * c1 - (m + 2 * lam_ - 2) * c0) / m
    return c1
def Vnum(phifun, xv):
    xv = mp.mpf(xv)
    f1 = lambda yv: (1 + 1 / (yv - xv)) * (xv / yv * phifun(yv) - (1 - yv) / (1 - xv) * phifun(xv))
    f2 = lambda yv: (1 + 1 / (xv - yv)) * ((1 - xv) / (1 - yv) * phifun(yv) - yv / xv * phifun(xv))
    return mp.quad(f1, [xv, 1]) + mp.quad(f2, [0, xv])
# test function phi = x xbar e^{2x} (not a finite Gegenbauer sum, but analytic => fast-decaying a_n):
# compare the direct quadrature with the Gegenbauer series.  (For phi ~ sqrt(x xbar), which vanishes like
# sqrt(x) at the endpoints, the a_n decay slowly and a series truncated at n = 40 is not accurate pointwise.)
phis = lambda t: t * (1 - t) * mp.exp(2 * t)
an = {}
for n in range(0, 41):
    an[n] = 2 * (2 * n + 3) / mp.mpf(3 * (n + 1) * (n + 2)) * mp.quad(lambda t: geg(n, 2 * t - 1) * phis(t), [0, 1])
def series_V(xv, nmax=40):
    return sum(float(lam_formula(n)) * an[n] * 6 * xv * (1 - xv) * geg(n, 2 * mp.mpf(xv) - 1) for n in range(0, nmax + 1))
ok = True
for xv in (0.2, 0.5, 0.71):
    d = Vnum(phis, xv)
    sv = series_V(xv)
    print('   x=%.2f  direct %.8f   Gegenbauer series (n<=40) %.8f' % (xv, float(d), float(sv)))
    ok &= abs(d - sv) < 1e-12 * max(1, abs(d))
ck.check('V (x) phi by direct quadrature = sum_n lambda_n a_n phi_n (phi = x xbar e^{2x}, all n <= 40, 1e-12)', ok)
phiCZ = lambda t: 30 * t * (1 - t) * (1 - 2 * t) ** 2
ok = True
for xv in (0.13, 0.5, 0.8):
    d = Vnum(phiCZ, xv)
    pred = float(lam_formula(2)) * mp.mpf(2) / 3 * 6 * xv * (1 - xv) * geg(2, 2 * mp.mpf(xv) - 1)
    ok &= abs(d - pred) < 1e-12
ck.check('V (x) phi_CZ = (2/3) lambda_2 6x xbar C_2(2x-1)  (direct quadrature, 1e-12)', ok)

print('=== 6. evolution-equation normalization: analytic solution vs kernel ===')
# a_n(mu) = a_n(mu0) [alpha_s(mu)/alpha_s(mu0)]^{gamma_n/(2 beta0)}, one-loop running; check
# mu^2 d phi/d mu^2 = (alpha_s/2pi) C_F (V (x) phi) at a point, by finite differences
nf = 3
b0 = float(beta0(nf))
as0 = 0.5
def alpha(t):   # t = ln(mu^2/mu0^2)
    return as0 / (1 + b0 * as0 / (4 * np.pi) * t)
def phi_evolved(t, xv):
    # CZ initial condition a_2(mu0) = 2/3 ; C_2^{3/2}(xi) = (3/2)(5 xi^2 - 1)
    a2t = (2.0 / 3) * (alpha(t) / as0) ** float(expo(2, nf))
    return 6 * xv * (1 - xv) * (1 + a2t * 1.5 * (5 * (2 * xv - 1) ** 2 - 1))
t0, h, xv = 1.3, 1e-4, 0.3
lhs = (phi_evolved(t0 + h, xv) - phi_evolved(t0 - h, xv)) / (2 * h)
a2t0 = (2.0 / 3) * (alpha(t0) / as0) ** float(expo(2, nf))
phit = lambda tt: 6 * tt * (1 - tt) * (1 + a2t0 * 1.5 * (5 * (2 * tt - 1) ** 2 - 1))
rhs = alpha(t0) / (2 * np.pi) * float(CF) * float(Vnum(phit, xv))
ck.close('d phi/d ln mu^2 (analytic Gegenbauer solution, exponent gamma_n/(2 beta_0)) = (alpha_s/2pi) V (x) phi', lhs, rhs, tol=1e-7)

ck.summary()
