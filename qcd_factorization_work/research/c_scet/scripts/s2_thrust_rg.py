# -*- coding: utf-8 -*-
"""
s2_thrust_rg.py -- Part (2b): RG consistency of  dsigma/dtau = H J (x) J (x) S , fixed-order check
against full QCD at O(alpha_s) (matrix element derived here), the delta(tau) coefficient from the
total-rate sum rule, and the LL resummed exponent vs. the CTTW form.

Inputs (derived in s2_thrust_oneloop.py, a = C_F alpha_s/(4 pi)):
  H  = 1 + a[-2 L_Q^2 + 6 L_Q - 16 + 7pi^2/3],          L_Q = ln(Q^2/mu^2)
  jt = 1 + a[2 L_J^2 - 3 L_J + 7 - 2pi^2/3],              L_J = ln(s Q^2/mu^2),  s = 1/(e^gE nu)
  st = 1 + a[-8 L_S^2 - pi^2],                            L_S = ln(s Q/mu)
  momentum space (star distributions):  J = delta + a[(7-pi^2)delta - 3[1/p^2]_* + 4[ln(p^2/mu^2)/p^2]_*]
                                         S = delta + a[(pi^2/3)delta - 16[ln(k/mu)/k]_*]
Run:  python3 -I s2_thrust_rg.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import scipy.integrate as si

ck = Check('s2_thrust_rg: RG consistency, fixed-order QCD check, delta(tau) sum rule, LL exponent')
pi = sp.pi
LQ, ell, lnmu = sp.symbols('L_Q ell lnmu', real=True)
H1 = -2 * LQ ** 2 + 6 * LQ - 16 + 7 * pi ** 2 / 3
j1 = lambda L: 2 * L ** 2 - 3 * L + 7 - 2 * pi ** 2 / 3
s1 = lambda L: -8 * L ** 2 - pi ** 2
# ell = ln(1/s) = ln(nu e^gE):  L_J = L_Q - ell,  L_S = L_Q/2 - ell
LJ = LQ - ell
LS = LQ / 2 - ell
tot1 = sp.expand(H1 + 2 * j1(LJ) + s1(LS))
# mu dependence: L_Q = ln Q^2 - 2 lnmu
dtot = sp.diff(tot1.subs(LQ, sp.Symbol('lnQ2') - 2 * lnmu), lnmu)
ck('RG consistency at O(alpha_s): d/dln mu [H jt^2 st] = 0 (all L_Q dependence cancels)', sp.simplify(dtot) == 0, f'H+2j+s = {tot1}')
ck('Laplace-space thrust at O(alpha_s): t(nu) = 1 + a[-4 ell^2 + 6 ell - 2],  ell = ln(nu e^gE)',
   sp.simplify(tot1 - (-4 * ell ** 2 + 6 * ell - 2)) == 0)

# ---- all-order structure: d ln H = 2 Gamma L_Q + 2 gV ; d ln jt = -2 Gamma L_J - 2 gJ ; d ln st = 4 Gamma L_S - 2 gS
Gam, gV, gJ, gS = sp.symbols('Gamma gamma_V gamma_J gamma_S')
rge = sp.expand((2 * Gam * LQ + 2 * gV) + 2 * (-2 * Gam * LJ - 2 * gJ) + (4 * Gam * LS - 2 * gS))
ck('cusp terms cancel identically for any Gamma_cusp(alpha_s) (2L_Q - 4L_J + 4L_S = 0)', sp.expand(rge.coeff(Gam)) == 0)
ck('non-cusp terms cancel iff gamma^S = gamma^V - 2 gamma^J  [= Becher-Schwartz (gw): gamma^S = gamma^H - 2 gamma^J]',
   sp.solve(rge, gS)[0] == gV - 2 * gJ)
# one loop: gV0 = -6 CF, gJ0 = -3 CF  => gS0 = 0  (agrees with direct soft calculation)
CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
ck('one loop: gamma^S_0 = gamma^V_0 - 2 gamma^J_0 = -6C_F + 6C_F = 0 = direct soft result', (-6 * CF) - 2 * (-3 * CF) == 0)
# two loops (values read from Becher-Schwartz 2008, App. A): C_F^2 must cancel in gamma^S_1 (non-abelian exponentiation)
z3 = sp.zeta(3)
gV1 = CF ** 2 * (-3 + 4 * pi ** 2 - 48 * z3) + CF * CA * (-sp.Rational(961, 27) - 11 * pi ** 2 / 3 + 52 * z3) + CF * TF * nf * (sp.Rational(260, 27) + 4 * pi ** 2 / 3)
gJ1 = CF ** 2 * (-sp.Rational(3, 2) + 2 * pi ** 2 - 24 * z3) + CF * CA * (-sp.Rational(1769, 54) - 11 * pi ** 2 / 9 + 40 * z3) + CF * TF * nf * (sp.Rational(242, 27) + 4 * pi ** 2 / 9)
gS1 = sp.expand(gV1 - 2 * gJ1)
ck('two loops: C_F^2 terms cancel in gamma^S_1 = gamma^V_1 - 2 gamma^J_1 (soft function has maximally non-abelian colour factors)',
   sp.expand(gS1).coeff(CF, 2) == 0, f'gamma^S_1 = {sp.collect(gS1, [CA, TF])}')
ck('gamma^S_1 = C_F C_A (808/27 - 11pi^2/9 - 28 zeta3) + C_F T_F n_f (-224/27 + 4pi^2/9)',
   sp.simplify(gS1 - (CF * CA * (sp.Rational(808, 27) - 11 * pi ** 2 / 9 - 28 * z3) + CF * TF * nf * (-sp.Rational(224, 27) + 4 * pi ** 2 / 9))) == 0)

# ======================================================================================== fixed order in tau
# tau-space at mu = Q: J -> Q^2 J(Q^2 tau): [1/p^2]_*^{[Q^2]} -> [1/tau]_+, [ln(p^2/Q^2)/p^2]_* -> [ln tau/tau]_+ ;
#                       S -> Q S(Q tau):    [ln(k/Q)/k]_*^{[Q]}    -> [ln tau/tau]_+
c_delta = sp.expand((-16 + 7 * pi ** 2 / 3) + 2 * (7 - pi ** 2) + pi ** 2 / 3)   # units of a
c_plus0 = 2 * (-3)
c_plus1 = 2 * 4 - 16
ck('SCET at mu=Q: (1/sigma0) dsigma/dtau = delta + (C_F a_s/2pi){ (pi^2/3 - 1) delta(tau) - 3[1/tau]_+ - 4[ln tau/tau]_+ }',
   sp.simplify(c_delta / 2 - (pi ** 2 / 3 - 1)) == 0 and c_plus0 / 2 == -3 and c_plus1 / 2 == -4,
   f'(units C_F a_s/4pi: delta {c_delta}, [1/tau] {c_plus0}, [ln/tau] {c_plus1})')

# ---- derive the O(alpha_s) e+e- -> q qbar g matrix element with the trace engine (D = 4)
# M = -g t^a ubar(p1)[ g^nu (p1+p3) g^mu / s13 - g^mu (p2+p3) g^nu / s23 ] v(p2) eps*_nu ; photon/gluon pol sums -> -g
s, x1, x2 = sp.symbols('s x1 x2', positive=True)
x3 = 2 - x1 - x2
dsub = {dot('p1', 'p1'): 0, dot('p2', 'p2'): 0, dot('p3', 'p3'): 0,
        dot('p1', 'p2'): s * (1 - x3) / 2, dot('p1', 'p3'): s * (1 - x2) / 2, dot('p2', 'p3'): s * (1 - x1) / 2}
s13 = s * (1 - x2); s23 = s * (1 - x1)
def tr4(slots, idx):
    return dtrace(slots, idx).subs(D, 4)
T = sp.Integer(0)
# |A|^2 with A = A1 - A2 ; A1 = g^nu (p1+p3) g^mu / s13, A2 = g^mu (p2+p3) g^nu / s23 ; conj reverses order
for a_ in ('p1', 'p3'):
    for b_ in ('p1', 'p3'):
        T += tr4(('p1', 'nu', a_, 'mu', 'p2', 'mu', b_, 'nu'), ('mu', 'nu')) / s13 ** 2
for a_ in ('p2', 'p3'):
    for b_ in ('p2', 'p3'):
        T += tr4(('p1', 'mu', a_, 'nu', 'p2', 'nu', b_, 'mu'), ('mu', 'nu')) / s23 ** 2
for a_ in ('p1', 'p3'):
    for b_ in ('p2', 'p3'):
        T -= tr4(('p1', 'nu', a_, 'mu', 'p2', 'nu', b_, 'mu'), ('mu', 'nu')) / (s13 * s23)
        T -= tr4(('p1', 'mu', b_, 'nu', 'p2', 'mu', a_, 'nu'), ('mu', 'nu')) / (s13 * s23)
T = sp.simplify(sp.expand(T.subs(dsub)))      # (-g_mumu')(-g_nunu') signs: (+1) overall
T2 = sp.simplify(-tr4(('p1', 'mu', 'p2', 'mu'), ('mu',)).subs({dot('p1', 'p2'): s / 2}))   # 2-body (p1.p2 = s/2): -g Tr[p1 g^mu p2 g^mu'] = 4s
gs2 = sp.Symbol('g_s2', positive=True)
ratio = sp.simplify(gs2 * CF * T * (s / (128 * pi ** 3)) / (T2 * (1 / (8 * pi))))
ck('e+e- -> q qbar g:  (1/sigma0) dsigma/dx1 dx2 = (C_F alpha_s/2pi) (x1^2 + x2^2)/((1-x1)(1-x2))  [derived]',
   sp.simplify(ratio.subs(gs2, 4 * pi * sp.Symbol('alpha_s')) - CF * sp.Symbol('alpha_s') / (2 * pi) * (x1 ** 2 + x2 ** 2) / ((1 - x1) * (1 - x2))) == 0,
   f'T = {sp.factor(T)}')

# ---- LO thrust distribution by integrating the matrix element along T = const ; compare with closed form
f12 = lambda a, b: (a * a + b * b) / ((1 - a) * (1 - b))
def dsig_dT_num(Tv):
    lo, hi = 2 - 2 * Tv, Tv
    r1 = si.quad(lambda xb: f12(Tv, xb), lo, hi, limit=200)[0]                 # quark most energetic (x1 = T)
    r3 = si.quad(lambda xa: f12(xa, 2 - Tv - xa), lo, hi, limit=200)[0]        # gluon most energetic (x3 = T)
    return 2 * r1 + r3
def dsig_dT_closed(Tv):
    return 2 * (3 * Tv ** 2 - 3 * Tv + 2) / (Tv * (1 - Tv)) * np.log((2 * Tv - 1) / (1 - Tv)) - 3 * (3 * Tv - 2) * (2 - Tv) / (1 - Tv)
dev = max(abs(dsig_dT_num(Tv) / dsig_dT_closed(Tv) - 1) for Tv in (0.70, 0.75, 0.8, 0.9, 0.95, 0.99, 0.999))
ck('LO thrust distribution (units C_F a_s/2pi) = 2(3T^2-3T+2)/(T(1-T)) ln((2T-1)/(1-T)) - 3(3T-2)(2-T)/(1-T)  [De Rujula et al. 1978]',
   dev < 1e-9, f'max rel dev {dev:.1e}')
# singular expansion tau -> 0
tau = sp.Symbol('tau', positive=True)
Tt = 1 - tau
closed = 2 * (3 * Tt ** 2 - 3 * Tt + 2) / (Tt * (1 - Tt)) * sp.log((2 * Tt - 1) / (1 - Tt)) - 3 * (3 * Tt - 2) * (2 - Tt) / (1 - Tt)
sing = sp.limit(sp.expand(closed * tau - (-4 * sp.log(tau) - 3)), tau, 0)
ck('tau -> 0: LO thrust = -(4 ln tau + 3)/tau + O(ln tau) : matches SCET plus-distribution coefficients', sing == 0)
# delta(tau) coefficient from the total-rate sum rule: int_0^{1/2} dsigma/dtau = 1 + (3/2)(C_F a_s/2pi)
def dsig_dtau(t):
    # closed form written in tau = 1 - T (no cancellation in 1 - T)
    T_ = 1 - t
    return 2 * (3 * T_ ** 2 - 3 * T_ + 2) / (T_ * t) * np.log((1 - 2 * t) / t) - 3 * (1 - 3 * t) * (1 + t) / t
rfun = lambda t: dsig_dtau(t) + (4 * np.log(t) + 3) / t
I0 = si.quad(lambda u: rfun(np.exp(-u) / 3) * np.exp(-u) / 3, 0, 34, limit=400, epsabs=1e-14, epsrel=1e-13)[0]   # t = e^{-u}/3
I1 = 3 * np.log(3) - 2 * np.log(3) ** 2          # int_{1/3}^1 (4 ln t + 3)/t dt
cdel = 1.5 - I0 - I1
ck('delta(tau) coefficient from sum rule (QCD) = pi^2/3 - 1 (SCET: H + 2J + S constants)', abs(cdel - (np.pi ** 2 / 3 - 1)) < 1e-9,
   f'sum rule: {cdel:.12f}, SCET: {np.pi**2/3 - 1:.12f}')
# Laplace transform of the fixed-order cumulant R(tau) = 1 + a'(-2 ln^2 tau - 3 ln tau + pi^2/3 - 1):
#   <ln tau> = -ell, <ln^2 tau> = ell^2 + zeta_2   =>  t(nu) = 1 + 2a[-2(ell^2+zeta2) + 3 ell + pi^2/3 - 1]
lap = sp.expand(2 * (-2 * (ell ** 2 + pi ** 2 / 6) + 3 * ell + pi ** 2 / 3 - 1))
ck('Laplace transform of fixed-order cumulant equals SCET t(nu) = 1 + a[-4 ell^2 + 6 ell - 2]', sp.simplify(lap - tot1) == 0)
# check the Laplace moments numerically
nu_v = 37.0
m1 = si.quad(lambda t: nu_v * np.exp(-nu_v * t) * np.log(t), 0, np.inf, limit=400)[0]
m2 = si.quad(lambda t: nu_v * np.exp(-nu_v * t) * np.log(t) ** 2, 0, np.inf, limit=400)[0]
lv = np.log(nu_v * np.exp(np.euler_gamma))
ck('Laplace moments: nu int e^{-nu t} ln t = -ln(nu e^gE), nu int e^{-nu t} ln^2 t = ln^2(nu e^gE) + pi^2/6',
   abs(m1 + lv) < 1e-8 and abs(m2 - (lv ** 2 + np.pi ** 2 / 6)) < 1e-8)

# ======================================================================================== LL resummation
al, b, l = sp.symbols('alpha b ell', positive=True)     # alpha = alpha_s(Q), b = beta0/(4pi)
t = sp.Symbol('t', real=True)
IJ = sp.integrate((l + t) / (1 + b * al * t), (t, -l, 0))
IS = sp.integrate((2 * l + t) / (1 + b * al * t), (t, -2 * l, 0))
lnsig_LL = sp.simplify(CF * al / pi * (2 * IJ - IS))
lam = b * al * l
g1 = -(CF / (pi * b * lam)) * ((1 - 2 * lam) * sp.log(1 - 2 * lam) - 2 * (1 - lam) * sp.log(1 - lam))
diff_LL = sp.simplify(sp.expand_log(lnsig_LL - l * g1, force=True))
num_ok = all(abs(complex(sp.N((lnsig_LL - l * g1).subs({CF: sp.Rational(4, 3), b: sp.Rational(23, 12) / pi * sp.Rational(1, 1), al: 0.118, l: lv_}), 25))) < 1e-18
             for lv_ in (0.5, 1.7, 2.9))
ck('LL from SCET RG (one-loop cusp & beta): ln t = ell g1(lambda), g1 = -(C_F/(pi b lambda))[(1-2lambda)ln(1-2lambda) - 2(1-lambda)ln(1-lambda)]',
   diff_LL == 0 or num_ok, 'lambda = beta0 alpha_s(Q) ell/(4pi) ; CTTW (1993) form with their beta0 = beta0/(4pi)')
ser = sp.expand(sp.series(lnsig_LL, al, 0, 4).removeO())
ck('LL series: ln t = -(C_F a_s/pi) ell^2 - (C_F b/pi) a_s^2 ell^3 - (7/6)... ; leading term matches fixed order -(C_F a_s/pi) ell^2',
   sp.simplify(ser.coeff(al, 1) + CF / pi * l ** 2) == 0, f'series: {sp.collect(ser, al)}')
ck('O(alpha_s^2 ell^3) LL coefficient = -C_F beta0/(4 pi^2)', sp.simplify(ser.coeff(al, 2) - (-CF * b / pi * l ** 3)) == 0)

# ---------------------------------------------------------------- thrust vs hemisphere masses (massless particles)
# T = max_S 2|sum_{i in S} p_i|/sum|p_i| (thrust axis along a hemisphere momentum), tau = 1 - T.
# Exact identity: (M_L^2 + M_R^2)/Q^2 = tau - tau^2/2 + (M_R^2 - M_L^2)^2/(2 Q^4)  =>  tau = (M_L^2+M_R^2)/Q^2 + O(tau^2);
# for three partons M_L^2 + M_R^2 = Q^2 tau exactly.
import itertools
rng_t = np.random.default_rng(7)
def random_event(npart):
    # massless momenta in the c.m. frame (rescaled RAMBO-like: random directions, then boost/rescale to P=(Q,0))
    while True:
        ks = []
        for _ in range(npart):
            c = rng_t.uniform(-1, 1); ph = rng_t.uniform(0, 2 * np.pi); E = -np.log(rng_t.uniform() * rng_t.uniform())
            s_ = np.sqrt(1 - c * c); ks.append(E * np.array([1, s_ * np.cos(ph), s_ * np.sin(ph), c]))
        Ptot = sum(ks); M = np.sqrt(Ptot[0] ** 2 - Ptot[1:] @ Ptot[1:]); bvec = -Ptot[1:] / M
        gam = Ptot[0] / M; a_ = 1 / (1 + gam); x_ = 1.0 / M
        out = []
        for k in ks:
            bq = bvec @ k[1:]
            E = x_ * (gam * k[0] + bq); vec = x_ * (k[1:] + bvec * k[0] + a_ * bq * bvec)
            out.append(np.array([E, *vec]))
        Pout = sum(out)
        assert np.allclose(Pout, [1, 0, 0, 0], atol=1e-12) and all(abs(q[0] ** 2 - q[1:] @ q[1:]) < 1e-12 for q in out)
        return out                                            # total momentum (1,0,0,0): Q = 1
def thrust_and_masses(ps):
    best, bestS = -1, None
    idx = range(len(ps))
    for r in range(1, len(ps)):
        for S in itertools.combinations(idx, r):
            v = sum(ps[i][1:] for i in S); t = 2 * np.linalg.norm(v)
            if t > best: best, bestS = t, S
    Q = sum(p[0] for p in ps); T = best / Q
    PR = sum(ps[i] for i in bestS); PL = sum(ps[i] for i in idx if i not in bestS)
    m2 = lambda P: P[0] ** 2 - P[1:] @ P[1:]
    return 1 - T, m2(PR) / Q ** 2, m2(PL) / Q ** 2
dev3 = dev4 = 0.0
for _ in range(200):
    t3, mR, mL = thrust_and_masses(random_event(3)); dev3 = max(dev3, abs(mR + mL - t3))
    t4, mR, mL = thrust_and_masses(random_event(4)); dev4 = max(dev4, abs(mR + mL - (t4 - t4 ** 2 / 2 + (mR - mL) ** 2 / 2)))
ck('thrust vs hemisphere masses: (M_L^2+M_R^2)/Q^2 = tau - tau^2/2 + (M_R^2-M_L^2)^2/(2Q^4) (exact, 4 partons); = tau exactly for 3 partons',
   dev3 < 1e-12 and dev4 < 1e-12, f'max dev: 3 partons {dev3:.1e}, 4 partons {dev4:.1e}')

ok = ck.summary()
sys.exit(0 if ok else 1)
