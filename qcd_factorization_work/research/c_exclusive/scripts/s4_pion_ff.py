# -*- coding: utf-8 -*-
"""
s4_pion_ff.py -- item (2): LO hard kernel of the pion electromagnetic form factor.

  <pi+(p')| J^mu(0) |pi+(p)> = (p+p')^mu F_pi(Q^2),  J^mu = sum_q e_q qbar g^mu q,  q = p'-p, Q^2 = -q^2.
Breit frame, massless pions: p = (P,0,0_T), p' = (0,P,0_T) in light-front components, Q^2 = 2 P^2.
Leading-region approximation:
  M^mu = - sum_graphs int dx dy  Tr_D Tr_c [ A  M_in(x)  B  M_out(y) ] x (gluon propagator),
  M_in(x)  = (i f/4) g5 pslash  phi(x)   x  1_c/N_c      (<0|dbar_b u_a|pi+(p)>,  x = u-quark fraction)
  M_out(y) = (i f*/4) p'slash g5 phi*(y) x  1_c/N_c      (<pi+(p')|ubar_c d_d|0>)
  the overall (-1) comes from reordering  ubar_c u_a dbar_b d_d = - (ubar_c d_d)(dbar_b u_a).
A = Dirac string of the u line (from ubar to u), B = Dirac string of the d line (from dbar to d).
Run:  python3 -I s4_pion_ff.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np

ck = Checker('s4_pion_ff')
x, y, P, g, f = sp.symbols('x y P g f', positive=True)
eu, ed = sp.symbols('e_u e_d', real=True)
Nc = sp.symbols('N_c', positive=True)
CF = (Nc ** 2 - 1) / (2 * Nc)
xb, yb = 1 - x, 1 - y
Q2 = 2 * P ** 2

p = lc(P, 0)
pp = lc(0, P)
q = sub(pp, p)
ck.zero('Q^2 = -q^2 = 2 p.p\' = 2 P^2', -dot(q, q) - Q2)

Min = I * f / 4 * g5 * slash(p)
Mout = I * f / 4 * slash(pp) * g5
colour = CF / Nc          # Tr_c[t^a (1/Nc) t^a (1/Nc)] = Tr(t^a t^a)/Nc^2 = C_F/N_c


def S(k):
    return I * slash(k) / dot(k, k)


def graphs(mu):
    """returns dict graph -> amplitude M^mu (without the phi(x) phi*(y) factor)"""
    gmu = G[mu]
    out = {}
    lA = sub(scal(yb, pp), scal(xb, p))      # gluon momentum, graphs A,B
    lC = sub(scal(x, p), scal(y, pp))        # gluon momentum, graphs C,D
    tot = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for a in range(4):
        # graph A: photon on u line, gluon emitted after the photon vertex
        A_A = (I * g * G[a]) * S(add(scal(x, p), q)) * (eu * gmu)
        B_A = (I * g * GL[a])
        # graph B: photon on u line, gluon emitted before the photon vertex
        A_B = (eu * gmu) * S(sub(p, scal(yb, pp))) * (I * g * G[a])
        B_B = (I * g * GL[a])
        # graph C: photon on d line next to the incoming antiquark
        A_C = (I * g * G[a])
        B_C = (ed * gmu) * S(sub(scal(x, p), pp)) * (I * g * GL[a])
        # graph D: photon on d line next to the outgoing antiquark
        A_D = (I * g * G[a])
        B_D = (I * g * GL[a]) * S(sub(scal(y, pp), p)) * (ed * gmu)
        tot['A'] += tr(A_A * Min * B_A * Mout) * (-I / dot(lA, lA))
        tot['B'] += tr(A_B * Min * B_B * Mout) * (-I / dot(lA, lA))
        tot['C'] += tr(A_C * Min * B_C * Mout) * (-I / dot(lC, lC))
        tot['D'] += tr(A_D * Min * B_D * Mout) * (-I / dot(lC, lC))
    for k_ in tot:
        out[k_] = sp.simplify(-colour * tot[k_])
    return out


Mmu = [graphs(mu) for mu in range(4)]
tot = [sp.simplify(sum(Mmu[mu].values())) for mu in range(4)]

print('=== 1. current conservation, graph pair by graph pair ===')
qlow = [METRIC[i] * q[i] for i in range(4)]
ck.zero('q_mu (M_A + M_B)^mu = 0  (photon on the u line)', sum(qlow[mu] * (Mmu[mu]['A'] + Mmu[mu]['B']) for mu in range(4)))
ck.zero('q_mu (M_C + M_D)^mu = 0  (photon on the d line)', sum(qlow[mu] * (Mmu[mu]['C'] + Mmu[mu]['D']) for mu in range(4)))
ck.check('individual graphs are NOT conserved (q.M_A != 0): conservation needs both attachments',
         sp.simplify(sum(qlow[mu] * Mmu[mu]['A'] for mu in range(4))) != 0)

print('=== 2. Lorentz structure M^mu = (p+p\')^mu F ===')
ppp = add(p, pp)
ck.zero('transverse components M^1 = M^2 = 0', tot[1] ** 2 + tot[2] ** 2)
Mplus = sp.simplify((tot[0] + tot[3]) / sqrt2)
Mminus = sp.simplify((tot[0] - tot[3]) / sqrt2)
ck.zero('M^+/(p+p\')^+ = M^-/(p+p\')^-', sp.simplify(Mplus / plus(ppp) - Mminus / minus(ppp)))
TH = sp.factor(sp.simplify(Mplus / plus(ppp)))
print('   T_H(x,y) = ', TH)

print('=== 3. the hard kernel ===')
aS = sp.symbols('alpha_s', positive=True)
QQ = sp.symbols('Q', positive=True)
TH_expected = (g ** 2 * CF * f ** 2 / (2 * Nc * Q2)) * (eu / (xb * yb) - ed / (x * y))
ck.zero('T_H = (C_F g^2 f^2 /(2 N_c Q^2)) [ e_u/(xbar ybar) - e_d/(x y) ] = (2 pi C_F alpha_s f^2/(N_c Q^2)) [e_u/(xbar ybar) + e_dbar/(x y)]',
        sp.simplify(TH - TH_expected))
# individual graphs: decompose M_G^mu = alpha_G p^mu + beta_G p'^mu  (no transverse part)
coef = {}
for k_ in 'ABCD':
    Mp = sp.simplify((Mmu[0][k_] + Mmu[3][k_]) / sqrt2)   # M^+ = alpha P
    Mm = sp.simplify((Mmu[0][k_] - Mmu[3][k_]) / sqrt2)   # M^- = beta P
    al, be = sp.factor(sp.simplify(Mp / P)), sp.factor(sp.simplify(Mm / P))
    coef[k_] = (al, be)
    print('   graph %s :  M^mu = (%s) p^mu + (%s) p\'^mu' % (k_, al, be))
ck.check('graph A (photon absorbed first by the incoming u) is proportional to p^mu, graph B to p\'^mu, with equal '
         'coefficients; likewise C (prop. p\'^mu... ) and D: only the sums are conserved and proportional to (p+p\')^mu',
         sp.simplify(coef['A'][1]) == 0 and sp.simplify(coef['B'][0]) == 0 and sp.simplify(coef['A'][0] - coef['B'][1]) == 0
         and sp.simplify(coef['C'][0] * coef['C'][1]) == 0 and sp.simplify(coef['D'][0] * coef['D'][1]) == 0
         and sp.simplify(coef['C'][0] + coef['C'][1] - coef['D'][0] - coef['D'][1]) == 0)
ck.check('sign: T_H > 0 for e_u = 2/3, e_d = -1/3 (F_pi > 0 at large Q^2, same sign as F_pi(0) = 1)',
         sp.simplify(TH.subs({eu: sp.Rational(2, 3), ed: -sp.Rational(1, 3), Nc: 3, x: sp.Rational(1, 3), y: sp.Rational(1, 4)})) > 0)

print('=== 4. convolution formula and asymptotic limit ===')
phi_as = lambda t: 6 * t * (1 - t)
F_as = sp.integrate(sp.integrate(sp.expand(TH.subs({eu: sp.Rational(2, 3), ed: -sp.Rational(1, 3), Nc: 3}) * phi_as(x) * phi_as(y)), (x, 0, 1)), (y, 0, 1))
F_as = sp.simplify(F_as.subs(g, sp.sqrt(4 * sp.pi * aS)))
print('   Q^2 F_pi (asymptotic DA) =', sp.simplify(F_as * Q2))
ck.zero('Q^2 F_pi -> 8 pi alpha_s f_pi^2   (asymptotic DA, f_pi ~ 130 MeV normalization)', sp.simplify(F_as * Q2 - 8 * sp.pi * aS * f ** 2))
Fs = sp.symbols('F93', positive=True)
ck.zero('                = 16 pi alpha_s F_pi^2 with F_pi = f_pi/sqrt2 ~ 93 MeV', sp.simplify((F_as * Q2).subs(f, sp.sqrt(2) * Fs) - 16 * sp.pi * aS * Fs ** 2))
# general: Q^2 F = (2 pi C_F alpha_s f^2 / N_c) [ e_u I(1/xbar) I*(1/ybar) + e_dbar I(1/x) I*(1/y) ]
Ix, Ixb = sp.symbols('I_x I_xb')
a2, a4 = sp.symbols('a2 a4', real=True)
Cg = lambda n, t: sp.gegenbauer(n, sp.Rational(3, 2), t)
phi_g = lambda t: 6 * t * (1 - t) * (1 + a2 * Cg(2, 2 * t - 1) + a4 * Cg(4, 2 * t - 1))
F_g = sp.integrate(sp.integrate(sp.expand(TH.subs({eu: sp.Rational(2, 3), ed: -sp.Rational(1, 3), Nc: 3}) * phi_g(x) * phi_g(y)), (x, 0, 1)), (y, 0, 1))
F_g = sp.simplify((F_g * Q2).subs(g, sp.sqrt(4 * sp.pi * aS)))
ck.zero('Q^2 F_pi = 8 pi alpha_s f_pi^2 (1 + a_2 + a_4)^2  (Gegenbauer DA, symmetric)', sp.simplify(F_g - 8 * sp.pi * aS * f ** 2 * (1 + a2 + a4) ** 2))
ck.zero('equivalently (8 pi alpha_s f^2/9) [int phi/(1-x)]^2  with N_c = 3', sp.simplify(F_g - 8 * sp.pi * aS * f ** 2 / 9 * sp.integrate(sp.cancel(phi_g(x) / (1 - x)), (x, 0, 1)) ** 2))
# general N_c, asymptotic DA
F_Nc = sp.integrate(sp.integrate(sp.expand(TH.subs({eu: sp.Rational(2, 3), ed: -sp.Rational(1, 3)}) * phi_as(x) * phi_as(y)), (x, 0, 1)), (y, 0, 1))
F_Nc = sp.simplify((F_Nc * Q2).subs(g, sp.sqrt(4 * sp.pi * aS)))
ck.zero('general N_c: Q^2 F_pi = 18 pi C_F alpha_s f^2 / N_c (asymptotic DA; = 8 pi alpha_s f^2 at N_c = 3)', sp.simplify(F_Nc - 18 * sp.pi * CF * aS * f ** 2 / Nc))
CZ = lambda t: 30 * t * (1 - t) * (1 - 2 * t) ** 2
F_CZ = sp.integrate(sp.integrate(sp.expand(TH.subs({eu: sp.Rational(2, 3), ed: -sp.Rational(1, 3), Nc: 3}) * CZ(x) * CZ(y)), (x, 0, 1)), (y, 0, 1))
F_CZ = sp.simplify((F_CZ * Q2).subs(g, sp.sqrt(4 * sp.pi * aS)))
ck.zero('CZ DA: Q^2 F_pi = (25/9) x asymptotic', sp.simplify(F_CZ - sp.Rational(25, 9) * 8 * sp.pi * aS * f ** 2))
fpi, als = 0.1302, 0.3
print('   numbers (f_pi = 130.2 MeV, alpha_s = 0.3): Q^2F_as = %.4f GeV^2,  Q^2F_CZ = %.4f GeV^2' % (8 * np.pi * als * fpi ** 2, 25 / 9 * 8 * np.pi * als * fpi ** 2))

print('=== 5. endpoint behaviour ===')
aa = sp.symbols('a', positive=True)
# phi ~ (x xbar)^a : int phi/x = B(a, a+1)/B(a+1,a+1) -> diverges like 1/a as a -> 0
ratio = sp.simplify(sp.gamma(aa) * sp.gamma(aa + 1) / sp.gamma(2 * aa + 1) / (sp.gamma(aa + 1) ** 2 / sp.gamma(2 * aa + 2)))
ck.zero('phi = (x xbar)^a/B(a+1,a+1): int phi/x = (2a+1)/a  (finite iff a > 0)', sp.simplify(ratio - (2 * aa + 1) / aa))
ck.check('a = 1 (asymptotic) gives 3; a -> 0 (flat DA) diverges', sp.simplify(((2 * aa + 1) / aa).subs(aa, 1)) == 3 and sp.limit((2 * aa + 1) / aa, aa, 0) == sp.oo)
# fraction of the LO integral from gluon virtualities xbar ybar Q^2 < mu0^2  (asymptotic and CZ DAs)
def frac_soft(phifun, Q2v, mu02=1.0, n=1200):
    # Gauss-Legendre in u = xbar, v = ybar ; integrand phi(u) phi(v)/(u v)
    t, wts = np.polynomial.legendre.leggauss(n)
    u = 0.5 * (t + 1); wu = 0.5 * wts
    U, V = np.meshgrid(u, u, indexing='ij')
    W = np.outer(wu, wu)
    integrand = phifun(U) * phifun(V) / (U * V)
    total = np.sum(W * integrand)
    soft = np.sum(W * integrand * (U * V * Q2v < mu02))
    return soft / total
asf = lambda t: 6 * t * (1 - t)
czf = lambda t: 30 * t * (1 - t) * (1 - 2 * t) ** 2
print('   fraction of the LO u-line integral with gluon virtuality xbar*ybar*Q^2 < 1 GeV^2:')
for Q2v in (2.0, 4.0, 10.0, 100.0):
    print('     Q^2 = %6.1f GeV^2 :  asymptotic DA %.3f   CZ DA %.3f' % (Q2v, frac_soft(asf, Q2v), frac_soft(czf, Q2v)))
# exact value for the asymptotic DA, c = mu0^2/Q^2 <= 1: R(c) = 4 int int_{uv<c} (1-u)(1-v)
uu, vv, cc = sp.symbols('u v c', positive=True)
Rexact = 4 * (sp.integrate((1 - uu) * sp.integrate(1 - vv, (vv, 0, 1)), (uu, 0, cc)) + sp.integrate((1 - uu) * sp.integrate(1 - vv, (vv, 0, cc / uu)), (uu, cc, 1)))
Rexact = sp.simplify(Rexact)
print('   exact (asymptotic DA): R(c) =', Rexact, '   c = mu0^2/Q^2')
ck.close('analytic R(c=1/4) matches the numerical fraction (asymptotic DA, Q^2 = 4 GeV^2)', float(Rexact.subs(cc, sp.Rational(1, 4))), frac_soft(asf, 4.0), tol=2e-3)
# exact value for the CZ DA: integrand phi_CZ(u) phi_CZ(v)/(u v) = 900 (1-u)(1-2u)^2 (1-v)(1-2v)^2, total = 5^2 = 25
fcz = 30 * (1 - uu) * (1 - 2 * uu) ** 2
Rcz = sp.simplify((sp.integrate(fcz * sp.integrate(fcz.subs(uu, vv), (vv, 0, 1)), (uu, 0, cc))
                   + sp.integrate(fcz * sp.integrate(fcz.subs(uu, vv), (vv, 0, cc / uu)), (uu, cc, 1))) / 25)
Rcz_closed = cc * (456 * cc ** 3 + 352 * cc ** 2 - 675 * cc - 132 - (144 * cc ** 3 + 768 * cc ** 2 + 450 * cc + 36) * sp.log(cc))
ck.zero('exact (CZ DA): R_CZ(c) = c[456c^3 + 352c^2 - 675c - 132 - (144c^3 + 768c^2 + 450c + 36) ln c]  (R(1) = 1)',
        sp.expand(sp.expand_log(Rcz - Rcz_closed, force=True)) + (Rcz_closed.subs(cc, 1) - 1))
ck.close('analytic R_CZ(c=1/10) matches the numerical fraction (CZ DA, Q^2 = 10 GeV^2)', float(Rcz_closed.subs(cc, sp.Rational(1, 10))), frac_soft(czf, 10.0), tol=2e-3)

ck.summary()
