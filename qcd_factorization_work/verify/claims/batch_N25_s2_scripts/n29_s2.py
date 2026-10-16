#!/usr/bin/env python3
"""N29 (stage-2 verifier): YZLIU derived cross-checks of Liu-programme formulas.
 (i)   H = C+ C- with C+- = 1 + (a C_F/8pi)(-4 - 5pi^2/6 + 2L+- - L+-^2), L+- = L_z +- i pi  vs JLS (4.11), (4.2); ESZ C^(1); G^(1)
 (ii)  c_H closed form (JLS (5.11)) numerics vs (5.12); n_f parts vs Liu-Su (2.41),(2.42); (A.11) with (A.2)-(A.5) => (A.13)
 (iii) gamma~_J^(2) from (A.4),(A.5) via (A.10)  vs JLS (3.13) and vs -gamma_1 of Jain-Scimemi-Stewart (bHQET jet function)
 (iv)  N_m = C_F e^{5/6}/pi: Liu-Su residue (2.46)->(2.47)->(2.50), and an INDEPENDENT large-beta0 pole-mass computation
 (v)   D_1 = (D + D_2)/2 from JLL eqs. (19)-(21)
 (vi)  Liu 2312.05957 (C.1): middle (omega) representation and closed form, numerically (not the finite-eta E integral)
 (vii) GN inequalities (4.2)-(4.5) of Liu 2403.06787: factor-wise proofs of (4.4),(4.5); adversarial maximisation for (4.2),(4.3)
 (viii) one-loop threshold: IJJSZ MS-bar kernel near xi -> 1 vs JLS (4.10)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 25
NP = 0; NF = 0
def check(name, ok, info=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('   ' + info if info else ''))

aS, CF, CA, nf, TF, Lz = sp.symbols('alpha_s C_F C_A n_f T_F L_z', real=True)
z3 = sp.zeta(3); pi = sp.pi
# ------------------------------------------------------------------ (i)
Lp, Lm = Lz + sp.I * pi, Lz - sp.I * pi
Cp = 1 + aS * CF / (8 * pi) * (-4 - 5 * pi**2 / 6 + 2 * Lp - Lp**2)
Cm = 1 + aS * CF / (8 * pi) * (-4 - 5 * pi**2 / 6 + 2 * Lm - Lm**2)
H1 = sp.expand(sp.series(Cp * Cm, aS, 0, 2).removeO())
H_JLS = 1 + aS * CF / (2 * pi) * (-2 + pi**2 / 12 - Lz**2 / 2 + Lz)
check('(i-a) C+ C- = 1 + (a C_F/2pi)(-2 + pi^2/12 - L_z^2/2 + L_z) = JLS (4.11) at O(alpha_s)', sp.simplify(H1 - H_JLS) == 0)
check('(i-b) = ESZ C^TMD_ns: 1 + (a C_F/4pi)(-L^2 + 2L - 4 + pi^2/6) (ESZ eq. kernels_nlo)', sp.simplify(H_JLS - (1 + aS * CF / (4 * pi) * (-Lz**2 + 2 * Lz - 4 + pi**2 / 6))) == 0)
HLF = 1 + aS * CF / (4 * pi) * (-4 - 5 * pi**2 / 6 + 2 * Lp - Lp**2)
check('(i-c) (C+)^2 = H^+_LFWF of JLS (4.2) at O(alpha_s); its one-loop phase = (a C_F/2)(1 - L_z)',
      sp.simplify(sp.expand(sp.series(Cp**2, aS, 0, 2).removeO()) - HLF) == 0 and sp.simplify(sp.im(sp.expand(HLF.subs({aS: 1}) - 1)) * 1 - CF / 2 * (1 - Lz)) == 0,
      'Im = %s' % sp.simplify(sp.im(sp.expand(HLF - 1).subs(aS, 1))))
check('(i-d) G^(1) = 2 d/dL_z H^(1) = (a C_F/pi)(1 - L_z)', sp.simplify(2 * sp.diff(H_JLS, Lz) - aS * CF / pi * (1 - Lz)) == 0)
# ------------------------------------------------------------------ (ii)
cH_CA = 241 * z3 / (144 * pi**2) + 11 * pi**2 / 320 - sp.Rational(559, 1728) - 971 / (324 * pi**2)
cH_CF2 = (-45 * z3 - 2 * pi**4 + 30 * pi**2 - 30) / (24 * pi**2)
cH_nf = (36 * z3 + 51 * pi**2 + 1312) / (1296 * pi**2)
vals = [float(cH_CF2), float(cH_CA), float(cH_nf)]
check('(ii-a) c_H closed form (JLS (5.11)) = 0.0725 C_F^2 - 0.0840 C_F C_A + 0.1453 C_F n_f T_F (JLS (5.12))',
      abs(vals[0] - 0.0725) < 5e-5 and abs(vals[1] + 0.0840) < 5e-5 and abs(vals[2] - 0.1453) < 5e-5, 'values %.6f, %.6f, %.6f' % tuple(vals))
check('(ii-b) n_f part of c_H with T_F=1/2 equals Liu-Su (2.42): (36 zeta3 + 1312 + 51 pi^2)/(2592 pi^2)',
      sp.simplify(cH_nf / 2 - (36 * z3 + 1312 + 51 * pi**2) / (2592 * pi**2)) == 0)
# two-loop anomalous dimensions, JLS (A.1)-(A.5): coefficients of (alpha_s/4pi)^2
gF2 = (sp.Rational(49, 6) - 2 * pi**2 / 3) * CA * CF - (sp.Rational(5, 2) - 8 * pi**2 / 3) * CF**2 - sp.Rational(5, 3) * CF * nf
gV2 = CF * CA * (-sp.Rational(961, 27) - 11 * pi**2 / 3 + 52 * z3) + CF**2 * (-3 + 4 * pi**2 - 48 * z3) + CF * nf * (sp.Rational(130, 27) + 2 * pi**2 / 3)
gs2 = CF * CA * (sp.Rational(808, 27) - 11 * pi**2 / 9 - 28 * z3) + CF * nf * (-sp.Rational(112, 27) + 2 * pi**2 / 9)
gHL2 = CF * CA * (sp.Rational(110, 27) + pi**2 / 18 - 18 * z3) + CF * nf * (sp.Rational(4, 27) + pi**2 / 9)
gH2_A13 = (1188 * z3 - 99 * pi**2 - 1108) / (432 * pi**2) * CF * CA - (36 * z3 + 6 - 7 * pi**2) / (12 * pi**2) * CF**2 + (sp.Rational(1, 24) + 10 / (27 * pi**2)) * CF * nf
check('(ii-c) (A.11) gamma~_H = gamma_V + 2gamma_F + 2gamma_HL - gamma_s with (A.2)-(A.5) reproduces (A.13) (units alpha_s^2)',
      sp.simplify((gV2 + 2 * gF2 + 2 * gHL2 - gs2) / (16 * pi**2) - gH2_A13) == 0)
check('(ii-d) n_f part of gamma~_H^(2) = Liu-Su (2.41) large-beta0 value (80 + 9 pi^2)/(216 pi^2)',
      sp.simplify(sp.Rational(1, 24) + 10 / (27 * pi**2) - (80 + 9 * pi**2) / (216 * pi**2)) == 0)
gHH = (2 * gHL2 - gs2) / (16 * pi**2)
check('(ii-e) (A.6): 2gamma_HL - gamma_s two-loop = (1/pi^2)[C_F C_A(-49/36 + pi^2/12 - zeta3/2) + 5 C_F n_f/18]',
      sp.simplify(gHH - (CF * CA * (-sp.Rational(49, 36) + pi**2 / 12 - z3 / 2) + sp.Rational(5, 18) * CF * nf) / pi**2) == 0)
# ------------------------------------------------------------------ (iii)
gJ2 = 2 * gHL2 - 2 * gs2
target = CF * CA * (-sp.Rational(1396, 27) + 23 * pi**2 / 9 + 20 * z3) + CF * nf * (sp.Rational(232, 27) - 2 * pi**2 / 9)
check('(iii-a) gamma~_J^(2) = 2gamma_HL - 2gamma_s (A.10) with (A.4),(A.5) = C_F C_A(-1396/27 + 23pi^2/9 + 20zeta3) + C_F n_f(232/27 - 2pi^2/9) = JLS (3.13)',
      sp.simplify(gJ2 - target) == 0)
JSS_g1 = (sp.Rational(1396, 27) - 23 * pi**2 / 9 - 20 * z3) * CF * CA + (2 * pi**2 / 9 - sp.Rational(232, 27)) * CF * nf
check('(iii-b) = -gamma_1 of Jain-Scimemi-Stewart PRD 77 (2008) 094008 (bHQET jet function); one loop: -a C_F/pi = -gamma_0 (a/4pi), gamma_0 = 4C_F',
      sp.simplify(gJ2 + JSS_g1) == 0)
# ------------------------------------------------------------------ (iv) N_m
u = sp.symbols('u')
L_ = sp.symbols('L', real=True)
imB = CF / (4 * u) * (sp.exp((sp.Rational(5, 3) - L_) * u) / (u - 1) / sp.cos(pi * u) + 1)
res = sp.simplify(sp.limit((u - sp.Rational(1, 2)) * imB, u, sp.Rational(1, 2)))
mu_pz = sp.symbols('mu_over_pz', positive=True)
check('(iv-a) Liu-Su (2.46): residue of Im B at u=1/2 is (mu/p^z) C_F e^{5/6}/(2pi)  [e^{-L_z/2} = mu/(2p^z)]  (2.47)',
      sp.simplify(res.subs(L_, -2 * sp.log(mu_pz / 2)) - mu_pz * CF * sp.exp(sp.Rational(5, 6)) / (2 * pi)) == 0, 'residue = %s' % res)
Nm = float(sp.Rational(4, 3) * sp.exp(sp.Rational(5, 6)) / pi)
check('(iv-b) N_m = C_F e^{5/6}/pi = %.6f ~ 0.977 (C_F=4/3); this is Liu-Su eq. (2.50); eq. (2.52) lists the CONJECTURED values 0.622..0.524' % Nm, abs(Nm - 0.977) < 5e-4)
# independent: large-beta0 static self-energy dm = (C_F/pi) int_0^mu dk alpha_V(k), alpha_V(k) = a/(1 + beta0 a (ln(k/mu) - 5/6)),
# beta0 defined by d a/d ln mu = -beta0 a^2 (Liu-Su convention). Coefficient of a^{n+1}: (C_F/pi) mu beta0^n int_0^inf e^{-s}(s+5/6)^n ds
CFv = mp.mpf(4) / 3
ok = True
for n in [10, 20, 30]:
    coef = CFv / mp.pi * mp.quad(lambda s: mp.exp(-s) * (s + mp.mpf(5) / 6)**n, [0, mp.inf])
    ratio = coef / (CFv * mp.exp(mp.mpf(5) / 6) / mp.pi * mp.factorial(n))
    ok &= abs(ratio - 1) < 1e-5 * (10.0 / n)**2 + 1e-12
    last = ratio
check('(iv-c) independent: large-beta0 pole-mass/static self-energy coefficients -> (C_F e^{5/6}/pi) beta0^n n! mu (ratio -> 1)', ok, 'ratio at n=30: 1 - %.1e' % float(1 - last))
# ------------------------------------------------------------------ (v)
D, D1, D2, K, d, dp, Yp = sp.symbols('D D1 D2 K delta deltap Yp', real=True)
S1 = lambda dd, Y: sp.exp((Y - sp.log(dd)) * K + D1)
S2 = sp.exp(-(sp.log(d) + sp.log(dp)) * K + D2)
SI = sp.simplify(S2 / (S1(d, 0) * S1(dp, 0)))
check('(v) JLL (19)-(21): S_I = S2/(S1 S1) = e^{D2 - 2D1} = e^{-D}  =>  D = 2D1 - D2,  D1 = (D + D2)/2', sp.simplify(sp.log(SI) - (D2 - 2 * D1)) == 0)
# ------------------------------------------------------------------ (vi) (C.1)
c = mp.mpf('0.8')    # c = nu/sqrt2
for Es in [[mp.mpf('0.7'), mp.mpf('1.9')], [mp.mpf('0.4'), mp.mpf('1.1'), mp.mpf('2.6')], [mp.mpf('0.3'), mp.mpf('0.9'), mp.mpf('1.5'), mp.mpf('3.2')]]:
    n = len(Es)
    closed = sum(mp.exp(-c * Ek) * mp.fprod([1 / (Ek - Ej) for Ej in Es if Ej != Ek]) for Ek in Es)
    mid = 1j * mp.quadosc(lambda w: mp.sin(c * w) * mp.fprod([1 / (1j * w - Ek) for Ek in Es]), [-mp.inf, mp.inf], omega=c) / mp.pi
    check('(vi) Liu 2312.05957 (C.1), n=%d: i int dw/pi sin(c w) prod 1/(iw - E_k) = sum_k e^{-c E_k} prod_{j!=k} 1/(E_k-E_j) (real)' % n,
          abs(mid - closed) < 1e-12, 'middle=%s closed=%s' % (mp.nstr(mid, 12), mp.nstr(closed, 12)))
# ------------------------------------------------------------------ (vii) GN inequalities
# (4.4), (4.5): factor-wise proof from |Gamma(x+iy)/Gamma(x)|^2 = prod_n [1 + y^2/(x+n)^2]^{-1}
okf = True
for l in range(0, 9):
    for cc in [0.01, 0.2, 0.49]:
        for nn in range(0, 60):
            okf &= abs(nn - l + cc) <= nn + 1 + 2 * l - cc + 1e-15            # (4.4): |n-l+c| <= n+1+2l-c
            okf &= (nn + 2 * l + 2 + 2 * cc) <= 2 * (nn + 1 + 2 * l + cc) + 1e-15   # (4.5): x2 + n <= 2(x1 + n) with doubled y
check('(vii-a) (4.4),(4.5) hold factor by factor in the Weierstrass product (each factor <= 1): proof', okf)
ok44 = ok45 = True
rng = np.random.default_rng(5)
for _ in range(400):
    l = int(rng.integers(0, 9)); cc = mp.mpf(rng.uniform(0.001, 0.499)); yv = mp.mpf(rng.uniform(-40, 40))
    lhs44 = abs(mp.gamma(-l + cc + 1j * yv) / mp.gamma(1 + 2 * l - cc - 1j * yv)); rhs44 = abs(mp.gamma(-l + cc) / mp.gamma(1 + 2 * l - cc))
    lhs45 = abs(mp.gamma(2 * cc + 2j * yv + 2 * l + 2) / mp.gamma(1 + 2 * l + cc + 1j * yv)); rhs45 = abs(mp.gamma(2 * l + 2 + 2 * cc) / mp.gamma(1 + 2 * l + cc))
    ok44 &= lhs44 <= rhs44 * (1 + 1e-15); ok45 &= lhs45 <= rhs45 * (1 + 1e-15)
check('(vii-b) (4.4),(4.5) numerically on 400 random points', ok44 and ok45)
# (4.2), (4.3): adversarial search: coarse grid in lambda then local maximisation in (c, y, lambda)
from scipy.optimize import minimize
def F42(l, cc, yv, lam): return float(abs(mp.hyp1f1(2 + 2 * l + 2 * (cc + 1j * yv), 1 + 2 * l + (cc + 1j * yv), -lam)))
def F43(l, cc, yv, lam): return float(abs(mp.hyp1f1(2 + 2 * l, 1 + 2 * l - (cc + 1j * yv), -lam)))
worst = {'4.2': (0, None), '4.3': (0, None)}
mp.mp.dps = 15
for key, F in (('4.2', F42), ('4.3', F43)):
    for l in range(0, 9):
        best = (0, None)
        for cc in [0.01, 0.1, 0.25, 0.4, 0.49]:
            for yv in [0, 0.3, 1, 3, 10, 30]:
                for lam in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300]:
                    v = F(l, cc, yv, lam)
                    if v > best[0]: best = (v, (cc, yv, lam))
        # local refinement from the best grid point (bounded by clipping)
        cc0, y0, lam0 = best[1]
        def obj(p):
            cc_ = min(max(p[0], 1e-4), 0.4999); lam_ = min(max(p[2], 0.01), 400.0); y_ = min(max(p[1], -1000.0), 1000.0)
            return -F(l, cc_, y_, lam_)
        r = minimize(obj, [cc0, y0, lam0], method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-10, 'maxiter': 400})
        v = -r.fun
        xbest = [min(max(r.x[0], 1e-4), 0.4999), min(max(r.x[1], -1000.0), 1000.0), min(max(r.x[2], 0.01), 400.0)]
        if v > worst[key][0]: worst[key] = (v, (l, np.array(xbest)))
mp.mp.dps = 40
# large |y| (beyond the searched box |y|<=1000): |1F1(a,b,-lam)|^2 = 1 - [2a(1+2l-c) lam + a lam^2]/y^2 + O(y^-3) < 1 for (4.3), checked at high precision
okbig = True
for l in (0, 3, 8):
    for yv in (mp.mpf(10)**4, mp.mpf(10)**6):
        for lam in (mp.mpf('0.01'), mp.mpf(1), mp.mpf(50)):
            for cc in (mp.mpf('0.01'), mp.mpf('0.49')):
                v43 = abs(mp.hyp1f1(2 + 2 * l, 1 + 2 * l - (cc + 1j * yv), -lam)); v42 = abs(mp.hyp1f1(2 + 2 * l + 2 * (cc + 1j * yv), 1 + 2 * l + (cc + 1j * yv), -lam))
                okbig &= (v43 < 1) and (v42 <= 1)
check('(vii-e) large |y| (1e4, 1e6), 40-digit arithmetic: |F| < 1 for (4.3) (sup = 1 approached only as |y| -> inf) and <= 1 for (4.2)', okbig)
mp.mp.dps = 25
check('(vii-c) (4.2) |1F1(2+2l+2s, 1+2l+s, -lambda)| <= 1: adversarial grid + Nelder-Mead maximisation, l<=8, 0<c<1/2, lambda>=0.01 (=1 at lambda=0, decreasing there since Re(a/b)>0)',
      worst['4.2'][0] < 1, 'max found %.10f at l=%d, (c,y,lambda)=%s' % (worst['4.2'][0], worst['4.2'][1][0], np.round(worst['4.2'][1][1], 4)))
check('(vii-d) (4.3) |1F1(2+2l, 1+2l-s, -lambda)| <= 1: same search',
      worst['4.3'][0] < 1, 'max found %.10f at l=%d, (c,y,lambda)=%s' % (worst['4.3'][0], worst['4.3'][1][0], np.round(worst['4.3'][1][1], 4)))
# ------------------------------------------------------------------ (viii) one-loop threshold
y = sp.symbols('y', positive=True)
lp = sp.symbols('ell_p', real=True)   # ell_p = ln(mu^2/4p_z^2) = -L_z
g2 = (1 + y**2) / (1 - y) * (-lp + sp.log(y * (1 - y))) - y * (1 + y) / (1 - y)
lead_in = sp.limit(sp.simplify((1 - y) * (g2 - 2 / (1 - y) * (-lp + sp.log(1 - y) - 1))), y, 1)
g1 = (1 + y**2) / (1 - y) * sp.log(y / (y - 1)) + 1
lead_out = sp.limit(sp.simplify((y - 1) * (g1 - 2 * sp.log(y - 1) / (y - 1))), y, 1)
check('(viii) IJJSZ MS-bar kernel at threshold: 0<y<1 -> (2/(1-y))(L_z + ln(1-y) - 1), y>1 -> 2 ln(y-1)/(y-1), both = JLS (4.10) J_f^(1) at power (1-y)^-1',
      lead_in == 0 and lead_out == 0, 'remainders x (1-y): %s, %s' % (lead_in, lead_out))

print('\nSUMMARY n29_s2: %d PASS, %d FAIL' % (NP, NF))
