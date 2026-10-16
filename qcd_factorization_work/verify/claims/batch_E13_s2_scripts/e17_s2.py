#!/usr/bin/env python3
"""E17 stage-2: Aybat-Rogers 2011 zeta normalization.
(1) kinematics in their convention V^pm=(V0 pm Vz)/sqrt2: sqrt(zeta_F zeta_D) vs Q^2 for printed eqs (3),(4)
    and for the factor-free forms (ACQR 2012 eqs. (zetaF),(zetaD)).
(2) RG invariance with the authors' OWN one-loop SIDIS hard factor (Aybat-Rogers arXiv:1107.3973):
    |H|^2 = 1 + (CF as/pi)[3/2 ln(Q^2/mu^2) - 1/2 ln^2(Q^2/mu^2) - 4], and their (B1)
    gamma_F = gamma_D = (as CF/pi)(3/2 - ln(zeta/mu^2)).
(3) rapidity-cutoff derivation of the delta(1-x) coefficient ln(zeta/kT^2): the Collins soft-factor
    ratio removes gluons with rapidity below y_s; gluon rapidity y = ln(sqrt2 l^+/l_T).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
ok = []
def check(n, c):
    ok.append(bool(c)); print(('PASS ' if c else 'FAIL ') + n)

M, Mh, Pp, Phm, x, z, ys = sp.symbols('M M_h Pplus Phminus x z y_s', positive=True)
# hadron P along +z: P^- = M^2/(2P^+) ; hadron h along -z: Ph^+ = Mh^2/(2 Ph^-)
yP = sp.log(Pp/(M**2/(2*Pp)))/2
yh = sp.log((Mh**2/(2*Phm))/Phm)/2
check('M^2 e^{2 y_P} = 2 (P^+)^2', sp.simplify(M**2*sp.exp(2*yP) - 2*Pp**2) == 0)
check('M_h^2 e^{-2 y_h} = 2 (P_h^-)^2', sp.simplify(Mh**2*sp.exp(-2*yh) - 2*Phm**2) == 0)
Q2 = 2*x*Pp*Phm/z          # Q^2 = -2 q^+ q^-, q^+ = -x P^+, q^- = P_h^-/z (hadron frame, leading power)
zF_pr = 2*M**2*x**2*sp.exp(2*(yP - ys)); zD_pr = 2*(Mh**2/z**2)*sp.exp(2*(ys - yh))
zF_ok = M**2*x**2*sp.exp(2*(yP - ys));   zD_ok = (Mh**2/z**2)*sp.exp(2*(ys - yh))
r_pr = sp.simplify(sp.sqrt(zF_pr*zD_pr)/Q2); r_ok = sp.simplify(sp.sqrt(zF_ok*zD_ok)/Q2)
print('   printed (3),(4): sqrt(zF zD)/Q^2 =', r_pr, ' ; factor-free: ', r_ok)
check('printed eqs (3),(4) give sqrt(zeta_F zeta_D) = 2 Q^2 (contradicting their own "~ Q^2")', r_pr == 2)
check('factor-free forms give sqrt(zeta_F zeta_D) = Q^2', r_ok == 1)
check('factor-free zeta_F = 2 (x P^+)^2 e^{-2 y_s} (Collins-Rogers 2013 eq. (zeta.A) form)', sp.simplify(zF_ok - 2*(x*Pp)**2*sp.exp(-2*ys)) == 0)

# (2) RG
a, Q, mu, zF, zD = sp.symbols('a Q mu zeta_F zeta_D', positive=True)   # a = as CF/pi
H = 1 + a*(sp.Rational(3, 2)*sp.log(Q**2/mu**2) - sp.Rational(1, 2)*sp.log(Q**2/mu**2)**2 - 4)
gH = sp.expand(sp.diff(H, mu)*mu)     # exact O(a): H is linear in a
gF = a*(sp.Rational(3, 2) - sp.log(zF/mu**2)); gD = a*(sp.Rational(3, 2) - sp.log(zD/mu**2))
tot = sp.simplify(sp.expand_log(gH + gF + gD, force=True))
print('   gamma_H =', sp.simplify(gH), ';  gamma_H+gamma_F+gamma_D =', tot)
check('gamma_H + gamma_F + gamma_D = a ln(Q^4/(zeta_F zeta_D)) -> RG invariance iff zeta_F zeta_D = Q^4',
      sp.simplify(tot - a*sp.log(Q**4/(zF*zD))) == 0)
check('with printed normalization (zeta_F zeta_D = 4 Q^4) the sum is -a ln 4 != 0',
      sp.simplify(tot.subs(zD, 4*Q**4/zF) + a*sp.log(4)) == 0)

# (3) rapidity cutoff -> delta(1-x) coefficient
p, kT, om = sp.symbols('p_plus k_T one_minus_x', positive=True)
ylow = ys
# gluon: l^+ = (1-x) p^+, |l_T| = kT, y_l = ln(sqrt2 l^+/kT) ; keep y_l > y_s  <=> (1-x) > kT e^{y_s}/(sqrt2 p^+)
delta0 = sp.solve(sp.Eq(sp.log(sp.sqrt(2)*om*p/kT), ys), om)[0]
# int_0^1 dx 2/(1-x) Theta(1-x > delta0) g(x) = int 2[1/(1-x)]_+ g + 2 ln(1/delta0) g(1)
coef = sp.simplify(sp.expand_log(2*sp.log(1/delta0), force=True))
zeta_std = 2*p**2*sp.exp(-2*ys)
print('   delta(1-x) coefficient =', coef)
check('delta(1-x) coefficient = ln(zeta/kT^2) with zeta = 2 (p^+)^2 e^{-2 y_s}',
      sp.simplify(coef - sp.log(zeta_std/kT**2)) == 0)
print(f'\nSUMMARY: {sum(ok)}/{len(ok)} checks passed')
