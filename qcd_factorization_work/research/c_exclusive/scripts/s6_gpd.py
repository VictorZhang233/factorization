# -*- coding: utf-8 -*-
"""
s6_gpd.py -- item (3): GPD definitions, kinematics, forward limits, polynomiality.

Definitions (Ji's H, E in the light-front normalization of Diehl, Phys. Rep. 388 (2003) 41):
  F^q = 1/2 int dz^-/(2pi) e^{i x Pbar^+ z^-} <p'| qbar(-z/2) g^+ W q(z/2) |p>|_{z^+=0, z_T=0}
      = 1/(2 Pbar^+) [ H^q ubar(p') g^+ u(p) + E^q ubar(p') i sigma^{+a} Delta_a/(2M) u(p) ],
  Ft^q (g^+ g5)  = 1/(2 Pbar^+) [ Ht^q ubar(p') g^+ g5 u(p) + Et^q Delta^+/(2M) ubar(p') g5 u(p) ],
  Pbar = (p+p')/2, Delta = p'-p, t = Delta^2, xi = -Delta^+/(2 Pbar^+) = (p^+ - p'^+)/(p^+ + p'^+).
Run:  python3 -I s6_gpd.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np

ck = Checker('s6_gpd')
xi, M, Pb, DT, xB, x, t = sp.symbols('xi M Pbar Delta_T x_B x t', positive=True)

print('=== 1. kinematics ===')
pm = (M ** 2 + DT ** 2 / 4) / (2 * Pb)
p = lc((1 + xi) * Pb, pm / (1 + xi), -DT / 2, 0)
pp = lc((1 - xi) * Pb, pm / (1 - xi), DT / 2, 0)
ck.zero('p^2 = p\'^2 = M^2', (dot(p, p) - M ** 2) ** 2 + (dot(pp, pp) - M ** 2) ** 2)
Pbar = scal(sp.Rational(1, 2), add(p, pp))
Delta = sub(pp, p)
ck.zero('xi = -Delta^+/(2 Pbar^+) = (p^+ - p\'^+)/(p^+ + p\'^+)', sp.simplify(-plus(Delta) / (2 * plus(Pbar)) - xi) + sp.simplify((plus(p) - plus(pp)) / (plus(p) + plus(pp)) - xi))
tt = sp.simplify(dot(Delta, Delta))
ck.zero('t = -(4 xi^2 M^2 + Delta_T^2)/(1 - xi^2)', sp.simplify(tt + (4 * xi ** 2 * M ** 2 + DT ** 2) / (1 - xi ** 2)))
ck.zero('t_0 = t(Delta_T=0) = -4 xi^2 M^2/(1-xi^2)  (so -t >= -t_0 >= 0)', sp.simplify(tt.subs(DT, 0) + 4 * xi ** 2 * M ** 2 / (1 - xi ** 2)))
# DVCS at leading power: q'^+ = 0 => q^+ = Delta^+, Q^2 = 4 xi Pbar^+ q^-, x_B = Q^2/(2 p.q) = 2 xi/(1+xi)
qm = sp.symbols('q_m', positive=True)
q = lc(-2 * xi * Pb, qm)
pL = lc((1 + xi) * Pb, 0)   # leading-power proton (M, t neglected)
Q2 = -dot(q, q)
xBv = sp.simplify(Q2 / (2 * dot(pL, q)))
ck.zero('leading power: x_B = 2 xi/(1+xi)  <=>  xi = x_B/(2 - x_B)', sp.simplify(xBv - 2 * xi / (1 + xi)) + sp.simplify(sp.solve(sp.Eq(xB, 2 * xi / (1 + xi)), xi)[0] - xB / (2 - xB)))
ck.zero('Q^2 = 4 xi Pbar^+ q^-', sp.simplify(Q2 - 4 * xi * Pb * qm))

print('=== 2. forward limits with explicit nucleon spinors ===')
# massive Dirac spinors u(p, s) for momentum along z (Dirac representation), spin along z (= helicity for p^3>0)
E_, pz = sp.symbols('E p_z', positive=True)
def u_spinor(Ev, pzv, s):
    chi = sp.Matrix([1, 0]) if s > 0 else sp.Matrix([0, 1])
    sig_p = pzv * SIG3
    up = sp.sqrt(Ev + M) * chi
    lo = sig_p * chi / sp.sqrt(Ev + M)
    return sp.Matrix([up[0], up[1], lo[0], lo[1]])
Ev = sp.sqrt(pz ** 2 + M ** 2)
pplus = (Ev + pz) / sqrt2
ok = True
okA = True
for s1 in (1, -1):
    for s2 in (1, -1):
        u1, u2 = u_spinor(Ev, pz, s1), u_spinor(Ev, pz, s2)
        ub1 = u1.H * g0
        vV = sp.simplify((ub1 * gp * u2)[0])
        vA = sp.simplify((ub1 * gp * g5 * u2)[0])
        ok &= sp.simplify(vV - (2 * pplus if s1 == s2 else 0)) == 0
        okA &= sp.simplify(vA - (2 * pplus * s1 if s1 == s2 else 0)) == 0
ck.check('ubar(p,s) g^+ u(p,s\') = 2 p^+ delta_{ss\'}  => F^q(forward) = H^q(x,0,0) = q(x) (x>0), -qbar(-x) (x<0)', ok)
ck.check('ubar(p,s) g^+ g5 u(p,s\') = 2 p^+ (2 lambda) delta_{ss\'}  => Ht^q(x,0,0) = Delta q(x) (x>0), +Delta qbar(-x) (x<0)', okA)
print('   (E, Et multiply structures proportional to Delta and have no forward PDF limit; E(x,0,0) exists but is not a density)')

print('=== 3. Gordon identity behind polynomiality (D-term enters H and E with opposite signs) ===')
# ubar(p') u(p) = (M/Pbar^+)[ ubar(p') g^+ u(p) - ubar(p') i sigma^{+a} Delta_a/(2M) u(p) ]
# verify numerically with explicit spinors for generic momenta (general frame: boosted spinors)
def u_general(pvec, s):
    # u(p,s) = (pslash + M) u(0,s)/sqrt(2M(E+M)) ... standard: u = sqrt(E+M) (chi, sigma.p chi/(E+M))
    Evv = pvec[0]
    chi = sp.Matrix([1, 0]) if s > 0 else sp.Matrix([0, 1])
    sig = pvec[1] * SIG1 + pvec[2] * SIG2 + pvec[3] * SIG3
    up = sp.sqrt(Evv + M) * chi
    lo = sig * chi / sp.sqrt(Evv + M)
    return sp.Matrix([up[0], up[1], lo[0], lo[1]])
Mv = sp.Rational(938, 1000)
vals = {M: Mv, xi: sp.Rational(1, 5), Pb: sp.Rational(7, 2), DT: sp.Rational(3, 10)}
pn = [sp.N(c_.subs(vals), 40) for c_ in p]
ppn = [sp.N(c_.subs(vals), 40) for c_ in pp]
Dn = sub(ppn, pn)
Pbp = plus(scal(sp.Rational(1, 2), add(pn, ppn)))
Mv = sp.N(Mv, 40)
def sigma(mu, nu):
    return I / 2 * (G[mu] * G[nu] - G[nu] * G[mu])
sig_plusD = sp.zeros(4)
Dlow = [METRIC[i] * Dn[i] for i in range(4)]
for a_ in range(4):
    sig_plusD += (sigma(0, a_) + sigma(3, a_)) / sqrt2 * Dlow[a_]     # sigma^{+ a} Delta_a
ok = True
for s1 in (1, -1):
    for s2 in (1, -1):
        uo = u_general(ppn, s1).subs(M, Mv)
        ui = u_general(pn, s2).subs(M, Mv)
        ubo = uo.H * g0
        lhs = (ubo * ui)[0]
        rhs = Mv / Pbp * ((ubo * gp * ui)[0] - (ubo * I * sig_plusD * ui)[0] / (2 * Mv))
        ok &= abs(complex(sp.N(lhs - rhs, 30))) < 1e-25
        ok &= abs(complex(sp.N((u_general(pn, s2).subs(M, Mv).H * g0 * u_general(pn, s2).subs(M, Mv))[0] - 2 * Mv, 30))) < 1e-25
ck.check('ubar(p\')u(p) = (M/Pbar^+)[ubar g^+ u - ubar i sigma^{+a} Delta_a u/(2M)]  (explicit spinors, all helicities)', ok)

print('=== 4. polynomiality in a closed-form double-distribution model with a D-term ===')
b, a, z = sp.symbols('beta alpha z', real=True)
X = sp.symbols('X', real=True)
xs = sp.symbols('xs', positive=True)
# DD: F(beta, alpha) = h(beta, alpha) q(beta), profile h = (3/4)[(1-beta)^2 - alpha^2]/(1-beta)^3, q(beta) = (1-beta)^3 (beta>0)
# H_DD(x,xi) = (1/xi) int dbeta F(beta, (x-beta)/xi) over max(0,(x-xi)/(1-xi)) <= beta <= (x+xi)/(1+xi)
Fba = sp.Rational(3, 4) * ((1 - b) ** 2 - ((X - b) / xi) ** 2)
H_dglap = sp.simplify(sp.integrate(Fba, (b, (X - xi) / (1 - xi), (X + xi) / (1 + xi))) / xi)   # xi < x < 1
H_erbl = sp.simplify(sp.integrate(Fba, (b, 0, (X + xi) / (1 + xi))) / xi)                     # -xi < x < xi
ck.zero('continuity of H_DD at x = xi', sp.simplify(H_dglap.subs(X, xi) - H_erbl.subs(X, xi)))
ck.zero('H_DD(x = -xi) = 0  (no antiquarks in this model) and H_DD(x=1) = 0', sp.simplify(H_erbl.subs(X, -xi)) ** 2 + sp.simplify(H_dglap.subs(X, 1)) ** 2)
ck.zero('forward limit H_DD(x, xi -> 0) = q(x) = (1-x)^3', sp.simplify(sp.limit(H_dglap, xi, 0) - (1 - X) ** 3))
# D-term: D(z) = (1-z^2) [d1 C_1^{3/2}(z) + d3 C_3^{3/2}(z)]  (odd in z), added as +D(x/xi) to H and -D(x/xi) to E
d1, d3 = sp.symbols('d1 d3', real=True)
Dz = (1 - z ** 2) * (d1 * sp.gegenbauer(1, sp.Rational(3, 2), z) + d3 * sp.gegenbauer(3, sp.Rational(3, 2), z))
okpoly = True
details = []
for n in range(0, 7):
    mom_dd = sp.integrate(sp.expand(X ** n * H_erbl), (X, -xi, xi)) + sp.integrate(sp.expand(X ** n * H_dglap), (X, xi, 1))
    mom_D = sp.integrate(sp.expand((X ** n * Dz.subs(z, X / xi))), (X, -xi, xi))
    momH = sp.simplify(sp.expand(mom_dd + mom_D))
    momE_D = -mom_D
    polyH = sp.Poly(sp.expand(momH), xi) if sp.expand(momH).is_polynomial(xi) else None
    if polyH is None:
        okpoly = False
        details.append('n=%d not polynomial: %s' % (n, momH))
        continue
    degs = [m_[0] for m_ in polyH.monoms()]
    if max(degs) > n + 1 or any(dg % 2 for dg in degs):
        okpoly = False
        details.append('n=%d bad degrees %s' % (n, degs))
    # xi^0 coefficient = forward moment int_0^1 x^n q(x)
    if sp.simplify(polyH.coeff_monomial(1) - sp.integrate(X ** n * (1 - X) ** 3, (X, 0, 1))) != 0:
        okpoly = False
        details.append('n=%d forward moment wrong' % n)
    # the xi^{n+1} term comes only from the D-term and cancels in H + E
    if n % 2 == 1:
        top_H = polyH.coeff_monomial(xi ** (n + 1))
        if sp.simplify(top_H - sp.expand(mom_D).coeff(xi, n + 1)) != 0:
            okpoly = False
    print('   n=%d: int x^n H dx = %s' % (n, sp.factor(momH)))
ck.check('int_{-1}^1 x^n H dx is an even polynomial in xi of degree <= n+1, xi^0 term = forward moment (n = 0..6)', okpoly, '; '.join(details))
mom1 = sp.integrate(sp.expand(X * Dz.subs(z, X / xi)), (X, -xi, xi))
C2 = sp.simplify(mom1 / (2 * xi) ** 2)
ck.zero('n=1: int x H = A_{2,0} + (2 xi)^2 C_2 with C_2 = (1/4) int_{-1}^{1} z D(z) dz; int x E has -(2 xi)^2 C_2',
        sp.simplify(C2 - sp.Rational(1, 4) * sp.integrate(z * Dz, (z, -1, 1))))
ck.zero('n=0: the D-term does not contribute to int H = F_1 (xi independent)', sp.integrate(Dz, (z, -1, 1)))
ck.zero('int_{-1}^1 z D(z) dz = (4/5) d1 for D = (1-z^2) sum_odd d_n C_n^{3/2}(z): only d1 enters C_2 = d1/5',
        sp.integrate(z * Dz, (z, -1, 1)) - sp.Rational(4, 5) * d1)

ck.summary()
