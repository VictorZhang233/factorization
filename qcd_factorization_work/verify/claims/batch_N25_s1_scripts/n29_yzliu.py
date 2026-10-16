# -*- coding: utf-8 -*-
"""
n29_yzliu.py -- independent checks for claim N29 (YZLIU derived cross-checks).
Run: python3 -I n29_yzliu.py
Inputs READ from arXiv sources: Ji-Liu-Su 2305.04416 (eqs. (3.13), (4.2), (4.10), (4.11), (5.7), (5.11)-(5.12), (A.1)-(A.13));
Liu-Su 2311.06907 (eqs. (2.41)-(2.52)); Ebert-Stewart-Zhao 1811.00026 (eq. kernels_nlo); Ji-Liu-Liu 1910.11415 (S_I, D_1, D_2);
Liu 2312.05957 (C.1); Liu 2403.06787 (4.2)-(4.5); Jain-Scimemi-Stewart 0801.0743 (two-loop gamma_1 of the heavy-quark jet function).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools, random
import numpy as np, sympy as sp, mpmath as mp

RES = []
def rep(name, ok, extra=''):
    RES.append(bool(ok)); print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)
mp.mp.dps = 30
pi = sp.pi; z3 = sp.zeta(3)

# ---------------------------------------------------------------- (i) H = C+ C-, ESZ form, G^(1), LFWF pair
Lz = sp.Symbol('L_z', real=True); aCF = sp.Symbol('a', positive=True)   # a = alpha_s C_F
Cpm = lambda s: 1 + aCF/(8*pi)*(-4 - 5*pi**2/6 + 2*(Lz + s*sp.I*pi) - (Lz + s*sp.I*pi)**2)
H1 = sp.expand(Cpm(+1)*Cpm(-1)).coeff(aCF, 1)
ESZ = (-Lz**2 + 2*Lz - 4 + pi**2/6)/(4*pi)                              # ESZ: C^TMD = 1 + (as CF/4pi)(-L^2 + 2L - 4 + pi^2/6)
JLS411 = (-2 + pi**2/12 - Lz**2/2 + Lz)/(2*pi)                          # JLS (4.11)
rep('(i-a) C_HL^+ C_HL^- = 1 + (as CF/2pi)(-2 + pi^2/12 - L_z^2/2 + L_z) = ESZ C^TMD_ns (1811.00026) = JLS (4.11)  [one loop]',
    sp.simplify(H1 - ESZ) == 0 and sp.simplify(H1 - JLS411) == 0)
G1 = sp.simplify(2*sp.diff(H1, Lz))                                    # 2 zeta_z d/dzeta_z = 2 d/dL_z
rep('(i-b) G^(1) = 2 d/dL_z H^(1) = (as CF/pi)(1 - L_z)', sp.simplify(G1 - (1 - Lz)/pi) == 0, '[%s]' % G1)
pair = sp.expand(Cpm(+1)**2).coeff(aCF, 1)
JLS42 = (-4 - 5*pi**2/6 + 2*(Lz + sp.I*pi) - (Lz + sp.I*pi)**2)/(4*pi)
rep('(i-c) (C_HL^+)^2 = H^+_LFWF of JLS (4.2) at one loop, with phase (as CF/2)(1 - L_z)',
    sp.simplify(pair - JLS42) == 0 and sp.simplify(sp.im(sp.expand(pair))*4*pi - 2*pi*(1 - Lz)) == 0)

# ---------------------------------------------------------------- (ii) c_H: numerics and n_f cross-check
cH_CA = 241*z3/(144*pi**2) + 11*pi**2/320 - sp.Rational(559, 1728) - 971/(324*pi**2)
cH_CF2 = (-45*z3 - 2*pi**4 + 30*pi**2 - 30)/(24*pi**2)
cH_nf = (36*z3 + 51*pi**2 + 1312)/(1296*pi**2)
vals = [float(cH_CF2), float(cH_CA), float(cH_nf)]
rep('(ii-a) c_H (JLS (5.11)) = 0.0725 CF^2 - 0.0840 CF CA + 0.1453 CF nf TF  (JLS (5.12))',
    abs(vals[0] - 0.0725) < 5e-5 and abs(vals[1] + 0.0840) < 5e-5 and abs(vals[2] - 0.1453) < 5e-5, '(%.6f, %.6f, %.6f)' % tuple(vals))
LS242 = (36*z3 + 1312 + 51*pi**2)/(2592*pi**2)                          # Liu-Su (2.42): alpha^2 CF nf coefficient of H(L_z=0)
rep('(ii-b) n_f part: c_H CF nf TF coefficient with TF=1/2 equals the large-beta0 result of Liu-Su (2.42) (H^(2) n_f part = c_H n_f part at L_z=0)',
    sp.simplify(cH_nf/2 - LS242) == 0)
# gamma_H^(2) from (A.11) with (A.2)-(A.5), units alpha_s^2
CF, CA, nf = sp.symbols('C_F C_A n_f')
u = 1/(16*pi**2)
gV = u*(CF*CA*(-sp.Rational(961, 27) - 11*pi**2/3 + 52*z3) + CF**2*(-3 + 4*pi**2 - 48*z3) + CF*nf*(sp.Rational(130, 27) + 2*pi**2/3))
gF = u*(CA*CF*(sp.Rational(49, 6) - 2*pi**2/3) - CF**2*(sp.Rational(5, 2) - 8*pi**2/3) - sp.Rational(5, 3)*CF*nf)
gs = u*(CF*CA*(sp.Rational(808, 27) - 11*pi**2/9 - 28*z3) + CF*nf*(-sp.Rational(112, 27) + 2*pi**2/9))        # (A.4)
gHL = u*(CF*CA*(sp.Rational(110, 27) + pi**2/18 - 18*z3) + CF*nf*(sp.Rational(4, 27) + pi**2/9))             # (A.5)
gH = sp.expand(gV + 2*gF + 2*gHL - gs)
A13 = (1188*z3 - 99*pi**2 - 1108)/(432*pi**2)*CF*CA - (36*z3 + 6 - 7*pi**2)/(12*pi**2)*CF**2 + (sp.Rational(1, 24) + 10/(27*pi**2))*CF*nf
rep('(ii-c) (A.11) with (A.2)-(A.5) reproduces (A.13) gamma~_H^(2)', sp.simplify(gH - A13) == 0)
rep('(ii-d) its n_f part (1/24 + 10/(27pi^2)) CF nf = (80 + 9pi^2)/(216 pi^2) CF nf = large-beta0 Liu-Su (2.41)',
    sp.simplify(sp.Rational(1, 24) + 10/(27*pi**2) - (80 + 9*pi**2)/(216*pi**2)) == 0)
# gamma_V and gamma_J cross-checks against Becher-Neubert-Pecjak, JHEP 01 (2007) 076 [hep-ph/0607228], App. (READ): TF nf -> nf/2
gV_BN = u*(CF**2*(-3 + 4*pi**2 - 48*z3) + CF*CA*(-sp.Rational(961, 27) - 11*pi**2/3 + 52*z3) + CF*(nf/2)*(sp.Rational(260, 27) + 4*pi**2/3))
rep('(ii-e) gamma_V (JLS A.3) = gamma_1^V of Becher-Neubert-Pecjak hep-ph/0607228 (read)', sp.simplify(gV - gV_BN) == 0)
gJ_BN = u*(CF**2*(-sp.Rational(3, 2) + 2*pi**2 - 24*z3) + CF*CA*(-sp.Rational(1769, 54) - 11*pi**2/9 + 40*z3) + CF*(nf/2)*(sp.Rational(242, 27) + 4*pi**2/9))
rep('(ii-e2) gamma_J = gamma_V/2 - gamma_s/2 (JLS A.9) equals gamma_1^J of BNP hep-ph/0607228 => gamma_s (JLS A.4) independently confirmed',
    sp.simplify(sp.expand(gV/2 - gs/2) - gJ_BN) == 0)
# 2 gamma_HL - gamma_s = gamma_HH (A.6), checked independently from the large-angle limit of the two-loop velocity-dependent cusp AD
rep('(ii-f) 2 gamma_HL - gamma_s = (as/pi)^2 CF[CA(-49/36 + pi^2/12 - zeta3/2) + (5/18) nf]  (A.6)',
    sp.simplify(sp.expand(2*gHL - gs) - (CF*CA*(-sp.Rational(49, 36) + pi**2/12 - z3/2) + sp.Rational(5, 18)*CF*nf)/pi**2) == 0)
# independent: large-angle constant of the two-loop cusp AD, Korchemsky-Radyushkin form, CA part:
#   Gamma(theta) -> theta Gamma_cusp + const ; two-loop CA constant (in (as/pi)^2 CF CA units) from Kilian-Mannel-Ohl / Becher-Neubert function
def B_BN(b):
    e = mp.e**(-2*b); c = mp.coth(b)
    return c**2*(mp.polylog(3, e) + b*mp.polylog(2, e) - mp.zeta(3) + mp.pi**2/6*b + b**3/3) \
        + c*(mp.polylog(2, e) - 2*b*mp.log(1 - e) - mp.pi**2/6*(1 + b) - b**2 - b**3/3) + mp.pi**2/6 + mp.zeta(3) + b**2
gQ2_CA = (2*mp.pi**2/3 - mp.mpf(98)/9 - 4*mp.zeta(3))/16
const_CA = B_BN(mp.mpf(70))/2 + 2*gQ2_CA
lin_CA = (mp.mpf(67)/36 - mp.pi**2/12)          # coefficient of theta at two loops (CA part), subtract theta*Gamma_cusp
theta = mp.mpf(70)
rep('(ii-g) cross-check: large-angle limit (B(beta->inf)->0) of the BN two-loop cusp function + 2 gamma^Q gives the gamma_HH CA coefficient -49/36+pi^2/12-zeta3/2',
    abs(-(const_CA) - (-(-mp.mpf(49)/36 + mp.pi**2/12 - mp.zeta(3)/2))) < 1e-10 or abs(const_CA - (-mp.mpf(49)/36 + mp.pi**2/12 - mp.zeta(3)/2)) < 1e-10,
    '(const = %s, target %s)' % (mp.nstr(const_CA, 12), mp.nstr(-mp.mpf(49)/36 + mp.pi**2/12 - mp.zeta(3)/2, 12)))

# ---------------------------------------------------------------- (iii) gamma~_J^(2)
gJ = sp.expand((2*gHL - 2*gs)/u)
target = CF*CA*(-sp.Rational(1396, 27) + 23*pi**2/9 + 20*z3) + CF*nf*(sp.Rational(232, 27) - 2*pi**2/9)
rep('(iii-a) gamma~_J^(2) = 2 gamma_HL - 2 gamma_s (JLS (A.10), (A.4), (A.5)) = CF CA(-1396/27 + 23pi^2/9 + 20 zeta3) + CF nf(232/27 - 2pi^2/9) [(as/4pi)^2]',
    sp.simplify(gJ - target) == 0)
JSS_gamma1 = (sp.Rational(1396, 27) - 23*pi**2/9 - 20*z3)*CF*CA + (2*pi**2/9 - sp.Rational(232, 27))*CF*nf
rep('(iii-b) = -gamma_1 of the heavy-quark (bHQET) jet function, Jain-Scimemi-Stewart PRD 77 (2008) 094008 (gamma_0 = 4CF <-> gamma~_J^(1) = -as CF/pi)',
    sp.simplify(gJ + JSS_gamma1) == 0)

# ---------------------------------------------------------------- (iv) N_m
uu = sp.Symbol('u'); LzS = sp.Symbol('L_z', real=True)
# Liu-Su (2.46): Im B(u) = Im R + (CF/(4u)) [ e^{(5/3 - L_z) u}/(u-1) * 1/cos(pi u) + 1 ] sign(z)
ImB = sp.Rational(1, 4)/uu*(sp.exp((sp.Rational(5, 3) - LzS)*uu)/(uu - 1)/sp.cos(pi*uu) + 1)     # per C_F, sign(z)=1
resid = sp.simplify(sp.limit((uu - sp.Rational(1, 2))*ImB, uu, sp.Rational(1, 2)))
# with L_z = ln(4 p_z^2/mu^2): e^{-L_z/2} = mu/(2 p_z)
target_res = sp.exp(sp.Rational(5, 6))/(2*pi)*sp.exp(-LzS/2)*2      # (mu/p_z) e^{5/6}/(2 pi) = 2 e^{-L_z/2} e^{5/6}/(2pi)
rep('(iv-a) residue of Im B at u=1/2 = (mu/p^z) CF e^{5/6}/(2 pi) (Liu-Su (2.47)), from their (2.46)', sp.simplify(resid - target_res) == 0, '[%s]' % resid)
# Borel: coefficient of alpha^{n+1} = n! [t^n] B(beta0 t/2); pole -> -(mu/p^z)(CF e^{5/6}/pi) sum (beta0 t)^n ; phase of the PAIR = 2 x single
Nm = sp.exp(sp.Rational(5, 6))*sp.Rational(4, 3)/pi
rep('(iv-b) => r_n = N_m beta0^n n! with N_m = CF e^{5/6}/pi = 0.9766 (CF=4/3), beta0 in d alpha/d ln mu = -beta0 alpha^2 (Liu-Su (2.49)-(2.50))',
    abs(float(Nm) - 0.977) < 5e-4, '(%.6f)' % float(Nm))
# independent large-beta0 pole-mass normalisation: static self-energy  delta m = (CF/pi) int_0^mu dk alpha_V(k),
# alpha_V(k) = alpha/(1 + beta0 alpha (ln(k/mu) - 5/6))  (MSbar large-beta0, C = -5/3); coefficient of alpha^{n+1}:
# (CF/pi) mu int_0^inf ds e^{-s} (s + 5/6)^n beta0^n  -> ratio to (CF e^{5/6}/pi) beta0^n n! mu
ratios = []
for n in (5, 10, 20, 40):
    cn = mp.quad(lambda s: mp.e**(-s)*(s + mp.mpf(5)/6)**n, [0, mp.inf])
    ratios.append(cn/(mp.e**(mp.mpf(5)/6)*mp.factorial(n)))
rep('(iv-c) independent: large-beta0 static self-energy (pole mass) coefficients r_n/(beta0^n n! mu) -> CF e^{5/6}/pi (ratio -> 1)',
    abs(ratios[-1] - 1) < 1e-10 and abs(ratios[0] - 1) > abs(ratios[-1] - 1), '(ratios n=5,10,20,40: %s)' % ', '.join(mp.nstr(r, 10) for r in ratios))

# ---------------------------------------------------------------- (v) D_1 = (D + D_2)/2
Kb, dl, dlp, D1, D2, Dd, Yp = sp.symbols('K delta delta_p D_1 D_2 D Yprime')
lnS1 = lambda d, Y: (Y - sp.log(d))*Kb + D1
lnS2 = -sp.log(dl*dlp)*Kb + D2
lnSI = sp.expand(lnS2 - lnS1(dl, 0) - lnS1(dlp, 0))       # S_I = S_2/(S_1(delta, Y'=0) S_1(Y=0, delta'))  [Ji-Liu-Liu 2019]
rep('(v) S_I = S_2/(S_1 S_1) = e^{-D}: K cancels, D = 2D_1 - D_2, i.e. D_1 = (D + D_2)/2',
    sp.simplify(sp.expand_log(lnSI, force=True) - (D2 - 2*D1)) == 0)

# ---------------------------------------------------------------- (vi) (C.1) of Liu 2312.05957: analytic + numeric
def rhsC1(E, nu): return sum(mp.e**(-nu*Ek/mp.sqrt(2))*mp.fprod([1/(Ek - Ej) for Ej in E if Ej != Ek]) for Ek in E)
def lhsC1_numeric(E, nu, eta):
    # direct E-integral at finite eta of the difference of products (no contour manipulation)
    f = lambda x: mp.e**(-nu*abs(x)/mp.sqrt(2))*(mp.fprod([1/(x - Ek - 1j*eta) for Ek in E]) - mp.fprod([1/(x - Ek + 1j*eta) for Ek in E]))/(2j*mp.pi)
    pts = sorted(set([-mp.inf, 0] + [Ek + s*d for Ek in E for s in (-1, 1) for d in (0, eta, 10*eta, 100*eta)] + list(E) + [mp.inf]))
    return mp.quad(f, pts)
okc = True; txt = []
for E, nu in [([1.3, 2.1], 0.7), ([0.5, 1.7, 2.9], 1.1), ([0.9, 1.0, 3.3, 4.0], 0.4)]:
    r = rhsC1(E, nu); l = lhsC1_numeric(E, nu, mp.mpf('1e-6'))
    okc = okc and abs(l - r) < 1e-4*max(1, abs(r)); txt.append('n=%d: lhs(eta=1e-6)=%s rhs=%s' % (len(E), mp.nstr(l.real, 9), mp.nstr(r, 9)))
rep('(vi) Liu (C.1): int dE/(2 pi i) e^{-nu|E|/sqrt2}[prod 1/(E-E_k-i eta) - prod 1/(E-E_k+i eta)] = sum_k e^{-nu E_k/sqrt2} prod_{j!=k} 1/(E_k-E_j)', okc, '; '.join(txt))

# ---------------------------------------------------------------- (vii) GN inequalities (4.2)-(4.5) of Liu 2403.06787
random.seed(20261010)
worst = [0, 0, 0, 0]
for trial in range(6000):
    l = random.randint(0, 10); c = random.choice([random.uniform(1e-4, 0.02), random.uniform(0.02, 0.48), random.uniform(0.48, 0.4999)])
    y = random.choice([random.uniform(-3, 3), random.uniform(-80, 80)]); lam = 10**random.uniform(-4, 3)
    s = mp.mpc(c, y)
    r1 = abs(mp.hyp1f1(2 + 2*l + 2*s, 1 + 2*l + s, -lam))
    r2 = abs(mp.hyp1f1(2 + 2*l, 1 + 2*l - s, -lam))
    r3 = abs(mp.gamma(-l + s)/mp.gamma(1 + 2*l - s))/abs(mp.gamma(-l + c)/mp.gamma(1 + 2*l - c))
    r4 = abs(mp.gamma(2*s + 2*l + 2)/mp.gamma(1 + 2*l + s))/abs(mp.gamma(2*l + 2 + 2*c)/mp.gamma(1 + 2*l + c))
    for i, r in enumerate([r1, r2, r3, r4]): worst[i] = max(worst[i], float(r))
rep('(vii-a) GN inequalities (4.2)-(4.5): max ratios over 6000 random points incl. c near 0 and 1/2, |y|<=80, 1e-4<=lambda<=1e3, l<=10 are <= 1',
    all(wv <= 1 + 1e-12 for wv in worst), '(%s)' % ', '.join('%.6f' % wv for wv in worst))
# analytic proof of (4.4),(4.5) via |Gamma(x+iy)/Gamma(x)|^2 = prod_n [1 + y^2/(x+n)^2]^{-1}: termwise comparison
okp = True
for l in range(0, 6):
    for c in (0.01, 0.25, 0.49):
        x, xp = -l + c, 1 + 2*l - c
        okp = okp and all(abs(x + n) < xp + n for n in range(0, 2000))           # (4.4): each factor <= 1
        a_ = 1 + 2*l + c
        okp = okp and all(4*(a_ + n)**2 >= (2*a_ + n)**2 for n in range(0, 2000))   # (4.5): 4/(2a+n)^2 >= 1/(a+n)^2
rep('(vii-b) (4.4) and (4.5) follow analytically from the Weierstrass product: termwise |x+n| < x\'+n and 4/(2a+n)^2 >= 1/(a+n)^2', okp)

# ---------------------------------------------------------------- (viii) one-loop threshold structure
y = sp.Symbol('y', positive=True); ell = sp.Symbol('ell', real=True)
g2 = (1 + y**2)/(1 - y)*(-ell + sp.log(y*(1 - y))) - y*(1 + y)/(1 - y)       # IJJSZ MSbar kernel, 0<y<1 (units as CF/2pi)
lead = sp.simplify(sp.limit((g2 - 2/(1 - y)*(-ell + sp.log(1 - y) - 1))*(1 - y), y, 1))
rep('(viii-a) 0<y<1: MSbar kernel -> (as CF/2pi) 2/(1-y) (L_z + ln(1-y) - 1) + O((1-y)^0), L_z = -ell = ln(4p_z^2/mu^2)', lead == 0, '[residual x(1-y) -> %s]' % lead)
g1 = (1 + y**2)/(1 - y)*sp.log(y/(y - 1)) + 1
lead1 = sp.simplify(sp.limit((g1 - 2*sp.log(y - 1)/(y - 1))*(y - 1), y, 1, '+'))
rep('(viii-b) y>1: kernel -> (as CF/2pi) 2 ln(y-1)/(y-1); JLS (4.10): P(ln(1-y)^2/|1-y|) + (L_z-1)[P(1/(1-y)) + P(1/|1-y|)] gives the same on both sides', lead1 == 0)

print('\nSUMMARY n29: %d/%d PASS' % (sum(RES), len(RES)))
