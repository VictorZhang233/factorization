# -*- coding: utf-8 -*-
"""
s1_da.py -- item (1): pion distribution amplitude: conventions, normalization, projector,
Gegenbauer expansion, moments, f_pi normalization.
Run:  python3 -I s1_da.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import math

ck = Checker('s1_da')
x, y, xi, lam, P, a2, a4 = sp.symbols('x y xi lambda P a2 a4', real=True)
f = sp.symbols('f')  # possibly complex decay constant

print('=== 1. Dirac-matrix and epsilon conventions ===')
G5_expected = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
ck.check('gamma5 = i g0 g1 g2 g3 is the off-diagonal unit block (Dirac rep.)', sp.simplify(g5 - G5_expected) == sp.zeros(4))
ck.check('gamma5^2 = 1', sp.simplify(g5 * g5 - E4) == sp.zeros(4))
ck.check('{gamma5, gamma^mu} = 0 for all mu', all(sp.simplify(g5 * G[m] + G[m] * g5) == sp.zeros(4) for m in range(4)))
ok = True
for mu, nu, rho, sig in itertools.product(range(4), repeat=4):
    t = tr(G[mu] * G[nu] * G[rho] * G[sig] * g5)
    if sp.simplify(t - (-4 * I * levi(mu, nu, rho, sig))) != 0:
        ok = False
ck.check('Tr(g^mu g^nu g^rho g^sigma g5) = -4 i eps^{mu nu rho sigma} with eps^{0123}=+1 (all 256 index sets)', ok)
ck.check('(gamma^+)^2 = (gamma^-)^2 = 0', sp.simplify(gp * gp) == sp.zeros(4) and sp.simplify(gm * gm) == sp.zeros(4))
ck.check('{gamma^+, gamma^-} = 2', sp.simplify(gp * gm + gm * gp - 2 * E4) == sp.zeros(4))
v = sp.symbols('vp vm v1 v2')
ck.check('vslash = v^+ g^- + v^- g^+ - v^1 g^1 - v^2 g^2', sp.simplify(slash(lc(*v)) - (v[0] * gm + v[1] * gp - v[2] * g1 - v[3] * g2)) == sp.zeros(4))

print('=== 2. leading-twist Fierz projection (used for DA and GPD projectors) ===')
Pu = sp.Rational(1, 2) * gm * gp     # projects on spinors with gamma^- u = 0 (quark moving along +z)
Pv = sp.Rational(1, 2) * gp * gm     # vbar Pv = vbar for vbar gamma^- = 0
ck.check('Pu, Pv are projectors; gamma^- Pu = 0, Pv gamma^- = 0',
         sp.simplify(Pu * Pu - Pu) == sp.zeros(4) and sp.simplify(Pv * Pv - Pv) == sp.zeros(4)
         and sp.simplify(gm * Pu) == sp.zeros(4) and sp.simplify(Pv * gm) == sp.zeros(4))
Msym = sp.Matrix(4, 4, lambda i, j: sp.Symbol('m%d%d' % (i, j)))
D = [gp, gp * g5, gp * g1, gp * g2]
B = [gm, g5 * gm, gm * g1, gm * g2]
fierz = sp.zeros(4)
for Da, Ba in zip(D, B):
    fierz += sp.Rational(1, 4) * tr(Da * Msym) * Ba
ck.check('Pu M Pv = 1/4 [Tr(g+ M) g- + Tr(g+ g5 M) g5 g- + sum_j Tr(g+ g^j M) g- g^j]  for arbitrary M',
         sp.simplify(Pu * Msym * Pv - fierz) == sp.zeros(4))

print('=== 3. pion projector ===')
p = lc(P, 0)            # pion along +z, massless
Min = I * f / 4 * g5 * slash(p)
ok = all(sp.simplify(tr(G[m] * g5 * Min) - I * f * p[m]) == 0 for m in range(4))
ck.check('Tr[gamma^mu gamma5 M_in] = i f p^mu  with M_in = (i f/4) gamma5 pslash  (=> <0|dbar g^mu g5 u|pi+> = i f p^mu)', ok)
ck.check('Tr[M_in] = Tr[gamma5 M_in] = Tr[gamma^mu M_in] = 0',
         sp.simplify(tr(Min)) == 0 and sp.simplify(tr(g5 * Min)) == 0 and all(sp.simplify(tr(G[m] * Min)) == 0 for m in range(4)))
ck.check('M_in is of leading twist: Pu M_in Pv = M_in', sp.simplify(Pu * Min * Pv - Min) == sp.zeros(4))
# outgoing projector from hermitian conjugation: C = gamma0 A^dagger gamma0
Cout = g0 * Min.H * g0
ck.check('<pi+(p)| ubar_a d_b |0> projector = gamma0 M_in^dagger gamma0 = (i f*/4) pslash gamma5',
         sp.simplify(Cout - I * sp.conjugate(f) / 4 * slash(p) * g5) == sp.zeros(4))

print('=== 4. Fourier conventions of the DA ===')
# <0| dbar(z) g+ g5 W u(-z) |pi(p)> = i f p^+ int dx e^{i(2x-1) p.z} phi(x): with x the momentum fraction of u.
# free-field: u(-z) annihilating u(x0 p) gives e^{-i x0 p.(-z)}, dbar(z) annihilating dbar(xbar0 p) gives e^{-i xbar0 p.z}
x0 = sp.symbols('x0', positive=True)
phase = sp.exp(-I * x0 * (-lam)) * sp.exp(-I * (1 - x0) * lam)     # lam = p.z
ck.zero('free q qbar state: phase = e^{i(2x0-1) p.z}  => phi(x) = delta(x-x0), x = u-quark fraction',
        sp.simplify(phase - sp.exp(I * (2 * x0 - 1) * lam)))
# translation: <0|O(2z,0)|pi> = e^{-i p.z} <0|O(z,-z)|pi>  => asymmetric form e^{-i xbar p.w}, w=2z
ck.zero('symmetric <-> asymmetric form: e^{-i p.z} e^{i(2x-1)p.z} = e^{-i (1-x) p.(2z)}',
        sp.simplify(sp.exp(-I * lam) * sp.exp(I * (2 * x - 1) * lam) - sp.exp(-I * (1 - x) * 2 * lam)))
# Fourier inversion with a regulated delta: int dz e^{-i(2y-1)P z} e^{i(2x-1) P z} e^{-eps z^2} -> (pi/P) delta(x-y)
# check: int dy [regulated kernel] g(y) -> (pi/P) g(x) numerically for smooth g
import numpy as np
def inv_check(xv, Pv=1.3, eps=1e-3):
    # int dz e^{2 i (x-y) P z - eps z^2} = sqrt(pi/eps) exp(-(x-y)^2 P^2/eps)
    ys = np.linspace(0, 1, 200001)
    g = 6 * ys * (1 - ys) * (1 + 0.3 * 1.5 * (5 * (2 * ys - 1) ** 2 - 1))
    ker = np.sqrt(np.pi / eps) * np.exp(-(xv - ys) ** 2 * Pv ** 2 / eps)
    val = np.trapezoid(ker * g, ys)
    gx = 6 * xv * (1 - xv) * (1 + 0.3 * 1.5 * (5 * (2 * xv - 1) ** 2 - 1))
    return val, np.pi / Pv * gx
val, exp_ = inv_check(0.37)
ck.close('inversion: int dz^- e^{-i(2x-1)p^+z^-}[i f p^+ int dy e^{i(2y-1)p^+z^-}phi(y)] = i pi f phi(x)  (numerical, regulated)', val, exp_, tol=2e-3)

print('=== 5. Gegenbauer expansion ===')
C = lambda n, t: sp.gegenbauer(n, sp.Rational(3, 2), t)
ok = True
for n in range(0, 9):
    for m in range(0, 9):
        val = sp.integrate(x * (1 - x) * C(n, 2 * x - 1) * C(m, 2 * x - 1), (x, 0, 1))
        exp_ = sp.Rational((n + 1) * (n + 2), 4 * (2 * n + 3)) if n == m else 0
        if sp.simplify(val - exp_) != 0:
            ok = False
ck.check('int_0^1 x(1-x) C_n C_m dx = delta_nm (n+1)(n+2)/(4(2n+3))   (n,m <= 8)', ok)
# projection formula a_n = 2(2n+3)/(3(n+1)(n+2)) int dx C_n(2x-1) phi(x)
coef = {2: sp.Rational(3, 10), 4: -sp.Rational(1, 7), 6: sp.Rational(2, 9)}
phi_test = 6 * x * (1 - x) * (1 + sum(c * C(n, 2 * x - 1) for n, c in coef.items()))
ok = all(sp.simplify(sp.Rational(2 * (2 * n + 3), 3 * (n + 1) * (n + 2)) * sp.integrate(C(n, 2 * x - 1) * phi_test, (x, 0, 1)) - coef.get(n, 1 if n == 0 else 0)) == 0 for n in range(0, 9))
ck.check('a_n = 2(2n+3)/[3(n+1)(n+2)] int_0^1 dx C_n^{3/2}(2x-1) phi(x)  (recovers a test DA, n<=8)', ok)
ck.zero('int_0^1 phi = a_0 = 1 for any a_{n>=1} (normalization fixed by a_0)', sp.integrate(phi_test, (x, 0, 1)) - 1)
ok = all(sp.simplify(sp.integrate(6 * (1 - x) * C(n, 2 * x - 1), (x, 0, 1)) - 3 * (-1) ** n) == 0 for n in range(0, 13))
ck.check('int_0^1 6 x(1-x) C_n(2x-1)/x dx = 3 (-1)^n  (n<=12)  => int phi/x = 3 sum_n (-1)^n a_n', ok)
ok = all(sp.simplify(sp.integrate(6 * x * C(n, 2 * x - 1), (x, 0, 1)) - 3) == 0 for n in range(0, 13))
ck.check('int_0^1 6 x(1-x) C_n(2x-1)/(1-x) dx = 3        (n<=12)  => int phi/(1-x) = 3 sum_n a_n', ok)
ok = all(sp.simplify(sp.diff(sp.legendre(n + 1, xi), xi) - C(n, xi)) == 0 for n in range(0, 12))
ck.check('C_n^{3/2}(xi) = d/dxi P_{n+1}(xi)  (n<=11)', ok)
ok = all(sp.simplify(C(n, 1) - sp.Rational((n + 1) * (n + 2), 2)) == 0 for n in range(0, 12))
ck.check('C_n^{3/2}(1) = (n+1)(n+2)/2', ok)
phiCZ = 30 * x * (1 - x) * (1 - 2 * x) ** 2
ck.zero('CZ DA 30x(1-x)(1-2x)^2 = 6x(1-x)[1 + (2/3) C_2^{3/2}(2x-1)]  (a_2 = 2/3, a_{n>2}=0)',
        sp.expand(phiCZ - 6 * x * (1 - x) * (1 + sp.Rational(2, 3) * C(2, 2 * x - 1))))
ck.zero('int phi_CZ/x = 5', sp.integrate(sp.cancel(phiCZ / x), (x, 0, 1)) - 5)
phi2 = 6 * x * (1 - x) * (1 + a2 * C(2, 2 * x - 1) + a4 * C(4, 2 * x - 1))
ck.zero('<xi^2> = int (2x-1)^2 phi = (1/5)(1 + 12 a_2/7)  (a_4 drops out)',
        sp.integrate((2 * x - 1) ** 2 * phi2, (x, 0, 1)) - sp.Rational(1, 5) * (1 + sp.Rational(12, 7) * a2))
ck.zero('<xi^4> = int (2x-1)^4 phi = 3/35 + 8 a_2/35 + 8 a_4/77',
        sp.integrate((2 * x - 1) ** 4 * phi2, (x, 0, 1)) - (sp.Rational(3, 35) + sp.Rational(8, 35) * a2 + sp.Rational(8, 77) * a4))
# local expansion: int dx e^{i(2x-1)lam} phi = sum (i lam)^n/n! <xi^n>
Mlam = sp.integrate(sp.exp(I * (2 * x - 1) * lam) * 6 * x * (1 - x), (x, 0, 1))
ser = sp.series(sp.simplify(Mlam), lam, 0, 6).removeO()
target = sum((I * lam) ** n / sp.factorial(n) * sp.integrate((2 * x - 1) ** n * 6 * x * (1 - x), (x, 0, 1)) for n in range(6))
ck.zero('int dx e^{i(2x-1)lam} phi_as(x) = sum_n (i lam)^n <xi^n>/n!  (local OPE, through lam^5)', sp.expand(ser - target))
lp = sp.symbols('lambda_p', positive=True)   # lambda != 0 (avoids a sympy Piecewise branch at lambda = 0)
Mlp = sp.integrate(sp.exp(I * (2 * x - 1) * lp) * 6 * x * (1 - x), (x, 0, 1))
ck.zero('closed form: int_0^1 dx e^{i(2x-1)lam} 6x(1-x) = 3 (sin lam - lam cos lam)/lam^3  (lam != 0; -> 1 as lam -> 0)',
        sp.simplify(sp.expand_complex(Mlp.rewrite(sp.sin)) - 3 * (sp.sin(lp) - lp * sp.cos(lp)) / lp ** 3)
        + sp.limit(3 * (sp.sin(lp) - lp * sp.cos(lp)) / lp ** 3, lp, 0) - 1)

print('=== 6. f_pi normalization from pi -> mu nu (tree level, no radiative corrections) ===')
# Gamma = G_F^2 |V_ud|^2 f^2 m_pi m_mu^2 (1 - m_mu^2/m_pi^2)^2 / (8 pi), with <0|A^mu|pi> = i f p^mu
GF = 1.1663788e-5        # GeV^-2
Vud = 0.97373
mpi = 0.13957039         # GeV
mmu = 0.1056583755       # GeV
tau = 2.6033e-8          # s
hbar = 6.582119569e-25   # GeV s
BR = 0.999877
Gam = hbar / tau * BR
fpi = math.sqrt(8 * math.pi * Gam / (GF ** 2 * Vud ** 2 * mpi * mmu ** 2 * (1 - mmu ** 2 / mpi ** 2) ** 2))
print('   f_pi (tree level, from tau_pi and |V_ud|) = %.2f MeV ;  f_pi/sqrt2 = %.2f MeV' % (fpi * 1e3, fpi * 1e3 / math.sqrt(2)))
ck.check('tree-level f_pi from Gamma(pi->mu nu) is ~130 MeV (not ~93): the normalization <0|dbar g^mu g5 u|pi+> = i f_pi p^mu', 125e-3 < fpi < 135e-3,
         '%.1f MeV' % (fpi * 1e3))
ck.check('F_pi = f_pi/sqrt2 ~ 92-93 MeV (chiral-perturbation-theory / Lepage-Brodsky normalization)', 90e-3 < fpi / math.sqrt(2) < 95e-3)

print('=== 7. dictionary to the Lepage-Brodsky normalization ===')
Nc = 3
fpi131, fpi93 = sp.symbols('f131 f93', positive=True)
# phi_LB = f_pi^{(131)}/(2 sqrt(2 Nc)) phi ; int phi_LB = f93/(2 sqrt Nc) with f93 = f131/sqrt2
ck.zero('int phi_LB = f131/(2 sqrt(2 Nc)) = f93/(2 sqrt(Nc))', (fpi131 / (2 * sp.sqrt(2 * Nc))).subs(fpi131, sp.sqrt(2) * fpi93) - fpi93 / (2 * sp.sqrt(Nc)))

ck.summary()
