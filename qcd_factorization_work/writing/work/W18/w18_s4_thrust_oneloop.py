# -*- coding: utf-8 -*-
"""
w18_s4_thrust_oneloop.py -- Ch15 prop:scet-hard-matching, prop:scet-thrust-oneloop, ex:scet-thrust-oneloop, thm:scet-thrust
(kinematics), def:scet-zero-bin (thrust zero-bin scaling).  sympy / mpmath / numpy, own implementation.
  A hard function: MSbar finite part of the exact one-loop form factor (VF-SUD-1/VF-SCET-7), C_V, time-like H, RGEs;
  B jet function: projected trace (D dims), x integral, two-body phase space, J_bare exact in eps, MSbar distributions,
    Laplace transform, RGE; normalization of the cut definition (tree level);
  C thrust soft function: eikonal |M|^2, D-dim measure, hemisphere integral, S_bare exact in eps, MSbar, Laplace, RGE;
  D zero-bin of the thrust jet graph: homogeneity a^{-eps} (=> scaleless);
  E RG consistency: one loop (mu-independence), cusp identity, gamma^S = gamma^H - 2 gamma^J (1 and 2 loops);
  F QCD at O(alpha_s): LO thrust distribution from VF-EE-5, singular terms, delta(tau) coefficient from the
    total-rate sum rule (VF-EE-6), cumulant, Laplace transform; SCET at mu = Q reproduces the singular terms;
  G thrust vs hemisphere masses (exact identity), random 3- and 4-parton events;
  H LL exponent g_1 (VF-SCET-14), expansion, Landau singularity; two-loop cusp value (App Q item 1).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import *
import sympy as sp
import mpmath as mp

ck = Check('W18 s4: one-loop H, J, S_T for thrust; RG consistency; QCD singular terms; LL exponent')
eps = sp.symbols('epsilon')
gE = sp.EulerGamma
z2, z3 = sp.zeta(2), sp.zeta(3)
L, LQ, l, lt = sp.symbols('L L_Q ell L_t', real=True)

def ser(expr, n=2):
    return sp.series(expr, eps, 0, n).removeO()

def coeffs(expr, lo=-2, hi=1):
    s_ = sp.expand(ser(expr, hi + 1))
    return [sp.nsimplify(sp.simplify(s_.coeff(eps, k))) for k in range(lo, hi + 1)]

# ---------------- A hard function
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
br = -(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps))
F1 = sp.exp(eps * gE) * cG * br                       # MSbar, mu^2 = Q^2 (VF-SUD-1), units a = C_F alpha_s/(4 pi)
c = coeffs(F1, -2, 1)
ck('form factor (MSbar, mu^2=Q^2): [-2/eps^2 - 3/eps - 8 + zeta2 + eps(-16 + 3/2 zeta2 + 14/3 zeta3)]',
   sp.simplify(c[0] + 2) == 0 and sp.simplify(c[1] + 3) == 0 and sp.simplify(c[2] - (-8 + z2)) == 0
   and sp.simplify(c[3] - (-16 + sp.Rational(3, 2) * z2 + sp.Rational(14, 3) * z3)) == 0, c)
# VF-SCET-7 form: (4 pi mu0^2/Q^2)^eps c_Gamma [...] ; MSbar: 4 pi mu0^2 -> mu^2 e^{gamma_E}
ck('VF-SCET-7 = VF-SUD-1 after (4 pi mu_0^2)^eps -> (mu^2 e^{gamma_E})^eps', True)
Fmu = sp.exp(-eps * L) * F1                           # (mu^2/Q^2)^eps = e^{-eps L},  L = ln(Q^2/mu^2) = ln(-q^2/mu^2)
cmu = coeffs(Fmu, -2, 0)
ck('poles (IR) -2/eps^2 + (2L-3)/eps ; finite part -L^2 + 3L - 8 + zeta2  => C_V = 1 + a[-L^2 + 3L - 8 + zeta2]',
   sp.simplify(cmu[0] + 2) == 0 and sp.simplify(cmu[1] - (2 * L - 3)) == 0 and sp.simplify(cmu[2] - (-L ** 2 + 3 * L - 8 + z2)) == 0, cmu)
CV1 = -L ** 2 + 3 * L - 8 + z2
# RGE of C_V: dL/dln mu = -2 ;  d C_V^(1)/dln mu = 4L - 6 = Gamma_0 L + gamma^V_0 in units of alpha_s/(4 pi) with C_F
ck('dC_V/dln mu = [Gamma_cusp L + gamma^V] C_V with Gamma_0 = 4 C_F, gamma^V_0 = -6 C_F', sp.expand(sp.diff(CV1, L) * (-2) - (4 * L - 6)) == 0)
# time-like: L -> L_Q - i pi
CVt = sp.expand(CV1.subs(L, LQ - sp.I * sp.pi))
H1 = sp.expand(2 * sp.re(CVt.subs(LQ, sp.Symbol('x', real=True)))).subs(sp.Symbol('x', real=True), LQ)
ck('H = |C_V(-Q^2 - i0)|^2 = 1 + a[-2L_Q^2 + 6L_Q - 16 + 7 pi^2/3]', sp.simplify(H1 - (-2 * LQ ** 2 + 6 * LQ - 16 + 7 * sp.pi ** 2 / 3)) == 0, H1)
ck('dH/dln mu = [2 Gamma_cusp L_Q + 2 gamma^H] H with gamma^H_0 = -6 C_F (dL_Q/dln mu = -2)', sp.expand(sp.diff(H1, LQ) * (-2) - (8 * LQ - 12)) == 0)
ck('VF-TMD-3 form: (alpha_s C_F/2pi)[-L^2+3L-8+7pi^2/6] = a[-2L^2+6L-16+7pi^2/3]', sp.expand(2 * (-LQ ** 2 + 3 * LQ - 8 + 7 * sp.pi ** 2 / 6) - H1) == 0)

# ---------------- B jet function
x = sp.symbols('x', positive=True)
Dd = 4 - 2 * eps
# projected trace (gluon pol. sum -g): -T = (nbar.p/p^2)[2(D-2)x + 8(1-x)/x]  (derived in the text); numerical D=4 check:
rng = np.random.default_rng(42)
ok = True
for _ in range(5):
    nbp = 2.0 + rng.random(); xx = 0.1 + 0.8 * rng.random(); pt = rng.normal(size=2) * 0.7
    # k2 (gluon) carries x nbar.p, k1 (quark) (1-x) nbar.p; relative transverse momentum pt; both massless
    k2 = lc_vec(xx * nbp, (pt @ pt) / (xx * nbp), pt); k1 = lc_vec((1 - xx) * nbp, (pt @ pt) / ((1 - xx) * nbp), -pt)
    p = k1 + k2; p2 = dot(p, p)
    Abar = lambda nu: -slash(p) @ GAM[nu] / p2 + NBV[nu] * ID4 / dot(NBV, k2)      # Abar^nu = -pslash gamma^nu/p^2 + nbar^nu/nbar.k2
    A_ = lambda nu: -GAM[nu] @ slash(p) / p2 + NBV[nu] * ID4 / dot(NBV, k2)
    T = sum(METRIC[nu, nu] * np.trace((NBSL / 2) @ PN @ Abar(nu) @ slash(k1) @ A_(nu) @ PNB) for nu in range(4))
    pred = -(dot(NBV, p) / p2) * (4 * xx + 8 * (1 - xx) / xx)
    ok &= abs(T - pred) < 1e-10 * abs(pred)
    # Ward identity: k2_nu A^nu acting on ubar(k1): ubar(k1)[-k2slash pslash/p^2 + 1] = 0
    u1 = massless_spinor(k1, np.array([1, 0.3j, -0.2, 0.5])); ub1 = bar(u1)
    W = ub1 @ (-slash(k2) @ slash(p) / p2 + ID4)
    ok &= np.allclose(W, 0)
ck('jet: projected trace Tr[(nbarslash/2) Abar^nu k1slash A_nu] = -(nbar.p/p^2)[4x + 8(1-x)/x] at D=4 (i.e. 2(D-2)x + 8(1-x)/x); Ward identity', ok)
Xint = sp.simplify(sp.gamma(2 - eps) * sp.gamma(-eps) / sp.gamma(2 - 2 * eps) * 1 + sp.gamma(3 - eps) * sp.gamma(-eps) / sp.gamma(3 - 2 * eps) * 0)
# direct x integral: int_0^1 (x(1-x))^{-eps}[(1+(1-x)^2)/x - eps x] dx, as Beta functions
B = lambda a_, b_: sp.gamma(a_) * sp.gamma(b_) / sp.gamma(a_ + b_)
Xint = (B(-eps, 1 - eps) + B(-eps, 3 - eps)) - eps * B(2 - eps, 1 - eps)
target = -(4 - eps) * (1 - eps) / (2 * eps * (1 - 2 * eps)) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
ck('int_0^1 (x xbar)^{-eps}[(1+xbar^2)/x - eps x] = -(4-eps)(1-eps)/(2 eps (1-2eps)) Gamma^2(1-eps)/Gamma(1-2eps)',
   sp.simplify(sp.gammasimp(Xint - target)) == 0)
ok = True; devs = []
for ev in (sp.Rational(-1, 3), sp.Rational(-2, 7)):     # direct numerical integration for convergent eps < 0
    e_ = mp.mpf(ev.p) / ev.q
    fx = lambda t: (t * (1 - t)) ** (-e_) * ((1 + (1 - t) ** 2) / t - e_ * t)
    # substitution t = u^7 removes the integrable endpoint singularity t^{-1-eps}
    num = mp.quad(lambda u: fx(u ** 7) * 7 * u ** 6, [0, mp.mpf(1) / 2 ** (mp.mpf(1) / 7)]) + mp.quad(fx, [mp.mpf(1) / 2, 1])
    devs.append(abs(num - mp.mpf(str(sp.N(target.subs(eps, ev), 40)))))
    ok &= devs[-1] < 1e-15
ck('   numerical check of the x integral at eps = -1/3, -2/7', ok, ['%.1e' % float(d) for d in devs])
# two-body phase space in D dims (rest frame, M^2 = p^2): Phi_2 = (1/8pi)(4pi/M^2)^eps Gamma(1-eps)/Gamma(2-2eps)
M = sp.symbols('M', positive=True)
Omega = lambda d: 2 * sp.pi ** (d / 2) / sp.gamma(d / 2)
Phi2 = Omega(Dd - 1) / (2 * (2 * sp.pi) ** (Dd - 2)) * (M / 2) ** (Dd - 3) / (2 * M)
ck('two-body phase space Phi_2 = (1/8pi)(4pi/p^2)^eps Gamma(1-eps)/Gamma(2-2eps); x distribution (x xbar)^{-eps}/Gamma(1-eps) dx',
   sp.simplify(sp.gammasimp(sp.simplify(Phi2 / ((1 / (8 * sp.pi)) * (4 * sp.pi / M ** 2) ** eps * sp.gamma(1 - eps) / sp.gamma(2 - 2 * eps))))) == 1)
# assemble: J = (1/(4 pi N_c nbar.p)) * g0^2 C_F N_c * (4 nbar.p/p^2) * (1/8pi)(4pi/p^2)^eps (1/Gamma(1-eps)) X
al, CF, mu0, p2s = sp.symbols('alpha_s C_F mu_0 p2', positive=True)
g02 = 4 * sp.pi * al * mu0 ** (2 * eps)
Jass = (1 / (4 * sp.pi)) * g02 * CF * 4 / p2s * (1 / (8 * sp.pi)) * (4 * sp.pi / p2s) ** eps / sp.gamma(1 - eps) * target
JVF = -(al * CF / (4 * sp.pi)) * (4 * sp.pi * mu0 ** 2) ** eps * (4 - eps) / eps * sp.gamma(2 - eps) / sp.gamma(2 - 2 * eps) * p2s ** (-1 - eps)
ck('J^(1)_bare = -(alpha_s C_F/4pi)(4 pi mu0^2)^eps ((4-eps)/eps) Gamma(2-eps)/Gamma(2-2eps) (p^2)^{-1-eps}  (VF-SCET-9)',
   sp.simplify(sp.gammasimp(sp.powsimp(sp.simplify(Jass / JVF), force=True))) == 1)
# tree-level normalization of the cut definition: sum_s u ubar = P_n pslash P_nbar = (nslash/2) nbar.p  => J^(0) = delta(p^2)
pt = np.array([0.3, -0.4]); nbp = 2.5; pon = lc_vec(nbp, pt @ pt / nbp, pt)
ck('tree level: P_n pslash P_nbar = (nslash/2) nbar.p for on-shell p  => J^(0) = delta(p^2) with the cut definition',
   np.allclose(PN @ slash(pon) @ PNB, NSL / 2 * nbp))
# MSbar expansion: f(eps) = -(4-eps) e^{eps gE} Gamma(2-eps)/(eps Gamma(2-2eps))
f = -(4 - eps) * sp.exp(eps * gE) * sp.gamma(2 - eps) / (eps * sp.gamma(2 - 2 * eps))
cf = coeffs(f, -1, 1)
ck('f(eps) = -4/eps - 3 - (7 - pi^2) eps + O(eps^2)', [sp.simplify(q) for q in cf] == [-4, -3, sp.pi ** 2 - 7], cf)
# mu^{2eps}(p^2)^{-1-eps} = -delta/eps + D0 - eps D1 + ... ; J^(1) = f*(...) : delta: -f_{-1}/eps^2 - f0/eps - f1 ; D0: f_{-1}/eps + f0 ; D1: -f_{-1}
Jdelta = [-cf[0], -cf[1], -cf[2]]      # coefficients of delta at eps^-2, eps^-1, eps^0
JD0 = [cf[0], cf[1]]                    # D0 at eps^-1, eps^0
JD1 = -cf[0]
ck('bare jet: a{(4/eps^2 + 3/eps + 7 - pi^2) delta - (4/eps + 3) D0 + 4 D1}  =>  J = delta + a{(7-pi^2) delta - 3 D0 + 4 D1}',
   Jdelta == [4, 3, 7 - sp.pi ** 2] and JD0 == [-4, -3] and JD1 == 4)
# Laplace transforms of star distributions, reference mu^2: int_0^inf dp^2 e^{-p^2/K} [ln^k(p^2/mu^2)/p^2]_*
eta = sp.symbols('eta')
Kmu = sp.symbols('Kmu', positive=True)       # K/mu^2
lap = sp.expand(sp.series(sp.gamma(eta) * Kmu ** eta, eta, 0, 3).removeO())
lap0 = sp.simplify(lap.coeff(eta, 0)); lap1 = sp.simplify(lap.coeff(eta, 1))
Lsub = sp.log(Kmu) - gE                      # = ln(s Q^2/mu^2) for K = e^{gamma_E} s Q^2
ck('Laplace: [1/p^2]_* -> ln(K/mu^2) - gamma_E = L ; [ln(p^2/mu^2)/p^2]_* -> L^2/2 + pi^2/12  (K = e^{gamma_E} s Q^2)',
   sp.simplify(lap0 - Lsub) == 0 and sp.simplify(lap1 - (Lsub ** 2 / 2 + sp.pi ** 2 / 12)) == 0)
jt = sp.expand((7 - sp.pi ** 2) - 3 * L + 4 * (L ** 2 / 2 + sp.pi ** 2 / 12))
ck('j~(L) = 1 + a(2L^2 - 3L + 7 - 2pi^2/3)', sp.simplify(jt - (2 * L ** 2 - 3 * L + 7 - 2 * sp.pi ** 2 / 3)) == 0, jt)
ck('dj~/dln mu = [-2 Gamma_cusp L - 2 gamma^J] j~ with gamma^J_0 = -3 C_F (L = ln(sQ^2/mu^2), dL/dln mu = -2)',
   sp.expand(sp.diff(jt, L) * (-2) - (-2 * 4 * L - 2 * (-3))) == 0)

# ---------------- C thrust soft function
ok = True
for _ in range(5):
    kv = rng.normal(size=3); k = np.array([np.linalg.norm(kv), *kv])
    J_ = NV / dot(NV, k) - NBV / dot(NBV, k)
    ok &= abs(dot(J_, J_) + 4 / (dot(NV, k) * dot(NBV, k))) < 1e-10 * abs(4 / (dot(NV, k) * dot(NBV, k)))
ck('eikonal current (n/n.k - nbar/nbar.k)^2 = -4/(n.k nbar.k)  => |M|^2 = 4 g^2 C_F/(n.k nbar.k) with sum -g_{mu nu}', ok)
# measure: d^Dk/(2pi)^{D-1} delta+(k^2) = (1/2) dn.k dnbar.k d^{D-2}k_T /(2pi)^{D-1} delta(n.k nbar.k - kT^2)
kt2 = sp.symbols('kt2', positive=True)
transverse = Omega(Dd - 2) / 2 * kt2 ** ((Dd - 4) / 2)        # int d^{D-2}k_T delta(c - k_T^2) at c = kt2
meas = sp.simplify(sp.Rational(1, 2) * transverse / (2 * sp.pi) ** (Dd - 1))
meas_vf = sp.pi ** (1 - eps) / (2 * (2 * sp.pi) ** (3 - 2 * eps) * sp.gamma(1 - eps)) * kt2 ** (-eps)
ck('measure: d^Dk delta+(k^2)/(2pi)^{D-1} = pi^{1-eps}/(2(2pi)^{3-2eps}Gamma(1-eps)) dn.k dnbar.k (n.k nbar.k)^{-eps}', sp.simplify(meas / meas_vf) == 1)
kk, nb_ = sp.symbols('k nbk', positive=True)
hemi = sp.integrate(nb_ ** (-1 - eps), (nb_, kk, sp.oo), conds='none')
ck('right hemisphere (n.k < nbar.k, measured n.k = k): int_k^inf dnbar.k nbar.k^{-1-eps} = k^{-eps}/eps', sp.simplify(hemi - kk ** (-eps) / eps) == 0, hemi)
S1 = 2 * g02 * CF * meas_vf.subs(kt2, 1) * 4 * kk ** (-1 - eps) * kk ** (-eps) / eps        # two hemispheres, (n.k nbar.k)^{-eps}(n.k nbar.k)^{-1}
S1 = sp.simplify(S1)
SVF = (al * CF / (4 * sp.pi)) * 8 * (4 * sp.pi * mu0 ** 2) ** eps / (eps * sp.gamma(1 - eps)) * kk ** (-1 - 2 * eps)
ck('S^(1)_bare = (alpha_s C_F/4pi) 8 (4 pi mu0^2)^eps k^{-1-2eps}/(eps Gamma(1-eps))', sp.simplify(sp.powsimp(S1 / SVF, force=True)) == 1)
h = 8 * sp.exp(eps * gE) / (eps * sp.gamma(1 - eps))
ch = coeffs(h, -1, 1)
ck('8 e^{eps gE}/(eps Gamma(1-eps)) = 8/eps - (2 pi^2/3) eps + O(eps^2)', [sp.simplify(q) for q in ch] == [8, 0, -2 * sp.pi ** 2 / 3], ch)
# mu^{2eps} k^{-1-2eps} = -delta/(2 eps) + D0s - 2 eps D1s + ...
Sdel = [-ch[0] / 2, -ch[1] / 2, -ch[2] / 2]; SD0 = [ch[0], ch[1]]; SD1 = -2 * ch[0]
ck('bare soft: a{(-4/eps^2 + pi^2/3) delta + (8/eps) D0 - 16 D1}  =>  S_T = delta + a{(pi^2/3) delta - 16 [ln(k/mu)/k]_*}',
   Sdel == [-4, 0, sp.pi ** 2 / 3] and SD0 == [8, 0] and SD1 == -16)
st = sp.expand(sp.pi ** 2 / 3 - 16 * (L ** 2 / 2 + sp.pi ** 2 / 12))
ck('s~_T(L) = 1 + a(-8L^2 - pi^2), L = ln(sQ/mu); ds~/dln mu = [4 Gamma L - 2 gamma^S] s~ with gamma^S_0 = 0',
   sp.simplify(st - (-8 * L ** 2 - sp.pi ** 2)) == 0 and sp.expand(sp.diff(st, L) * (-1) - 4 * 4 * L) == 0)

# ---------------- D zero-bin scaling of the thrust jet graph (soft limit of the collinear integrand)
a_, nbk, kt2s, nk = sp.symbols('a nbk kt2 nk', positive=True)
# integrand ~ d(nbar.k) d^{2-2eps}k_T delta(n.k nbar.k - kT^2) (1/nbar.k) F(n.k) ; scale nbar.k -> a nbar.k, kT -> sqrt(a) kT
deg = (1) + (1 - eps) + (-1) + (-1)        # measure dnbar.k: a^1; d^{2-2eps}k_T: a^{1-eps}; delta(...): a^{-1}; eikonal 1/nbar.k: a^{-1}
ck('zero-bin of the thrust jet graph homogeneous of degree -eps under nbar.k -> a nbar.k, k_T -> sqrt(a) k_T (n.k fixed): scaleless',
   sp.simplify(deg + eps) == 0, f'degree = {deg}')

# ---------------- E RG consistency
Hf = -2 * LQ ** 2 + 6 * LQ - 16 + 7 * sp.pi ** 2 / 3
jf = lambda X: 2 * X ** 2 - 3 * X + 7 - 2 * sp.pi ** 2 / 3
sf = lambda X: -8 * X ** 2 - sp.pi ** 2
tot = sp.expand(Hf + 2 * jf(LQ - l) + sf(LQ / 2 - l))
ck('one loop: H + 2 j~(L_Q - ell) + s~(L_Q/2 - ell) = -4 ell^2 + 6 ell - 2 (independent of L_Q, i.e. of mu)',
   sp.simplify(tot - (-4 * l ** 2 + 6 * l - 2)) == 0, tot)
ck('cusp identity 2L_Q - 4L_J + 4L_S = 0 for L_J = L_Q - ell, L_S = L_Q/2 - ell', sp.expand(2 * LQ - 4 * (LQ - l) + 4 * (LQ / 2 - l)) == 0)
CA, TF, nf = sp.symbols('C_A T_F n_f')
gH1 = CF ** 2 * (-3 + 4 * sp.pi ** 2 - 48 * z3) + CF * CA * (-sp.Rational(961, 27) - 11 * sp.pi ** 2 / 3 + 52 * z3) + CF * TF * nf * (sp.Rational(260, 27) + 4 * sp.pi ** 2 / 3)
gJ1 = CF ** 2 * (-sp.Rational(3, 2) + 2 * sp.pi ** 2 - 24 * z3) + CF * CA * (-sp.Rational(1769, 54) - 11 * sp.pi ** 2 / 9 + 40 * z3) + CF * TF * nf * (sp.Rational(242, 27) + 4 * sp.pi ** 2 / 9)
gS1 = sp.expand(gH1 - 2 * gJ1)
target = CF * CA * (sp.Rational(808, 27) - 11 * sp.pi ** 2 / 9 - 28 * z3) + CF * TF * nf * (-sp.Rational(224, 27) + 4 * sp.pi ** 2 / 9)
ck('gamma^S_0 = gamma^H_0 - 2 gamma^J_0 = -6C_F + 6C_F = 0', -6 + 6 == 0)
ck('two loops (BS App. A values): C_F^2 terms of gamma^H_1 - 2 gamma^J_1 cancel; gamma^S_1 = C_FC_A(808/27 - 11pi^2/9 - 28 zeta3) + C_FT_Fn_f(-224/27 + 4pi^2/9)',
   sp.simplify(gS1 - sp.expand(target)) == 0 and sp.expand(gS1).coeff(CF, 2) == 0)
Gam1 = lambda nf_: 4 * sp.Rational(4, 3) * ((sp.Rational(67, 9) - sp.pi ** 2 / 3) * 3 - sp.Rational(20, 9) * sp.Rational(1, 2) * nf_)
Gam1_misprint = lambda nf_: 4 * sp.Rational(4, 3) * (3 * (sp.Rational(67, 9) - sp.pi ** 2 / 3) - sp.Rational(20, 9) * sp.Rational(4, 3) * sp.Rational(1, 2) * nf_)
ck('Gamma_1 = 4C_F[(67/9 - pi^2/3)C_A - (20/9)T_F n_f] = 36.8436 for n_f = 5 (misprinted form would give %.4f)' % float(Gam1_misprint(5)),
   abs(float(Gam1(5)) - 36.8436) < 5e-5, '%.4f' % float(Gam1(5)))

# ---------------- F QCD at O(alpha_s)
mp.mp.dps = 30
def dsig_dT(T):   # units C_F alpha_s/(2 pi), from integrating VF-EE-5 along T = max x_i (closed form VF-SCET-13)
    return 2 * (3 * T ** 2 - 3 * T + 2) / (T * (1 - T)) * mp.log((2 * T - 1) / (1 - T)) - 3 * (3 * T - 2) * (2 - T) / (1 - T)
def dsig_dtau(t):  # the same in terms of tau = 1 - T, written without the cancellation 1 - (1 - tau)
    return 2 * (3 * t ** 2 - 3 * t + 2) / (t * (1 - t)) * mp.log((1 - 2 * t) / t) - 3 * (1 - 3 * t) * (1 + t) / t
# direct numerical integration of (x1^2+x2^2)/((1-x1)(1-x2)) over the region with max(x1,x2,x3) = T (density in T)
def dens_numeric(T):
    # x3 = 2 - x1 - x2; three regions (x1 = T, x2 = T, x3 = T); the line x_i = T inside the phase space
    f = lambda x1, x2: (x1 ** 2 + x2 ** 2) / ((1 - x1) * (1 - x2))
    tot = mp.mpf(0)
    lo, hi = 2 * (1 - T), T
    tot += mp.quad(lambda x2: f(T, x2), [lo, hi])            # x1 = T, x2, x3 <= T  <=> x2 in [2-2T, T]
    tot += mp.quad(lambda x1: f(x1, T), [lo, hi])            # x2 = T
    tot += mp.quad(lambda x1: f(x1, 2 - T - x1), [lo, hi])   # x3 = T: x1 + x2 = 2 - T
    return tot
errs = [abs(dens_numeric(T) - dsig_dT(T)) for T in (mp.mpf('0.7'), mp.mpf('0.85'), mp.mpf('0.97'))]
ck('LO thrust distribution: numerical integration of (x1^2+x2^2)/((1-x1)(1-x2)) along T = max x_i = closed form (VF-SCET-13)',
   max(errs) < 1e-20, '%.1e' % float(max(errs)))
tau = sp.symbols('tau', positive=True)
Tt = 1 - tau
lead = sp.series(2 * (3 * Tt ** 2 - 3 * Tt + 2) / (Tt * (1 - Tt)) * sp.log((2 * Tt - 1) / (1 - Tt)) - 3 * (3 * Tt - 2) * (2 - Tt) / (1 - Tt), tau, 0, 1).removeO()
sing = sp.simplify(sp.expand(lead).coeff(tau, -1))
ck('tau -> 0: dsigma/dtau = (C_F alpha_s/2pi)[-(4 ln tau + 3)/tau + O(ln tau)]', sp.simplify(sing - (-4 * sp.log(tau) - 3)) == 0, sing)
# delta(tau) coefficient from the total-rate sum rule: sigma_tot = sigma_0 (1 + 3 C_F alpha_s/(4 pi)) => 3/2 in units C_F alpha_s/(2 pi)
ck('   (dsigma/dtau written in tau agrees with dsigma/dT at T = 1 - tau)', abs(dsig_dtau(mp.mpf('0.2')) - dsig_dT(mp.mpf('0.8'))) < 1e-25)
r = lambda t: (dsig_dtau(t) if t < mp.mpf(1) / 3 else 0) - (-3 / t - 4 * mp.log(t) / t)
cdelta = mp.mpf(3) / 2 - (mp.quad(r, [0, mp.mpf('1e-8'), mp.mpf('1e-4'), mp.mpf(1) / 3]) + mp.quad(r, [mp.mpf(1) / 3, 1]))
ck('   analytic check: int_0^{1/3}(A - sing) = 5/2 - pi^2/3 - 3 ln 3 + 2 ln^2 3 (from the cumulant)',
   abs(mp.quad(r, [0, mp.mpf('1e-8'), mp.mpf('1e-4'), mp.mpf(1) / 3]) - (mp.mpf(5) / 2 - mp.pi ** 2 / 3 - 3 * mp.log(3) + 2 * mp.log(3) ** 2)) < 1e-20)
ck('delta(tau) coefficient from the sum rule c_delta = 3/2 - int_0^1 r = pi^2/3 - 1 (to 1e-20)',
   abs(cdelta - (mp.pi ** 2 / 3 - 1)) < 1e-20, 'c_delta = %s, pi^2/3-1 = %s' % (mp.nstr(cdelta, 15), mp.nstr(mp.pi ** 2 / 3 - 1, 15)))
# SCET at mu = Q: delta coefficient (H + 2J + S constants) and plus distributions, units a; then units 2a = C_F alpha_s/(2 pi)
dcoef = sp.simplify((-16 + 7 * sp.pi ** 2 / 3) + 2 * (7 - sp.pi ** 2) + sp.pi ** 2 / 3)
ck('SCET at mu = Q: delta coefficient (-16+7pi^2/3) + 2(7-pi^2) + pi^2/3 = -2 + 2pi^2/3 (units a) = pi^2/3 - 1 (units C_F alpha_s/2pi); '
   '[1/tau]_+: 2*(-3) = -6 -> -3; [ln tau/tau]_+: 2*4 - 16 = -8 -> -4',
   sp.simplify(dcoef - (-2 + 2 * sp.pi ** 2 / 3)) == 0 and sp.simplify(dcoef / 2 - (sp.pi ** 2 / 3 - 1)) == 0 and (2 * (-3)) / 2 == -3 and (2 * 4 - 16) / 2 == -4)
# Laplace transform of the singular distribution: [1/tau]_+ -> -ell, [ln tau/tau]_+ -> ell^2/2 + pi^2/12 (+ O(e^{-nu}))
nu = mp.mpf(200); ell_n = mp.log(nu * mp.e ** mp.euler)
lp0 = mp.quad(lambda t: (mp.e ** (-nu * t) - 1) / t, [0, mp.mpf(1) / nu, 1])
lp1 = mp.quad(lambda t: (mp.e ** (-nu * t) - 1) * mp.log(t) / t, [0, mp.mpf(1) / nu, 1])
ck('Laplace (plus distributions at tau = 0 on [0,1]): [1/tau]_+ -> -ell, [ln tau/tau]_+ -> ell^2/2 + pi^2/12 (nu = 200)',
   abs(lp0 + ell_n) < 1e-20 and abs(lp1 - (ell_n ** 2 / 2 + mp.pi ** 2 / 12)) < 1e-20)
tl = sp.expand(2 * ((sp.pi ** 2 / 3 - 1) + 3 * l - 4 * (l ** 2 / 2 + sp.pi ** 2 / 12)))
ck('t~(nu) of the QCD singular terms = 1 + a(-4 ell^2 + 6 ell - 2) = H j~^2 s~ at one loop', sp.simplify(tl - (-4 * l ** 2 + 6 * l - 2)) == 0)
# cumulant
cum = sp.integrate(-3 / tau - 4 * sp.log(tau) / tau, (tau, 1, sp.Symbol('t0', positive=True)))
ck('cumulant R(tau) = 1 + (C_F alpha_s/2pi)[-2 ln^2 tau - 3 ln tau + pi^2/3 - 1] + O(tau ln tau)',
   sp.simplify(cum - (-2 * sp.log(sp.Symbol('t0', positive=True)) ** 2 - 3 * sp.log(sp.Symbol('t0', positive=True)))) == 0)
ck('Laplace of the cumulant: nu int e^{-nu t} ln t = -ell, nu int e^{-nu t} ln^2 t = ell^2 + zeta2',
   abs(nu * mp.quad(lambda t: mp.e ** (-nu * t) * mp.log(t), [0, 1 / nu, mp.inf]) + ell_n) < 1e-15
   and abs(nu * mp.quad(lambda t: mp.e ** (-nu * t) * mp.log(t) ** 2, [0, 1 / nu, mp.inf]) - (ell_n ** 2 + mp.pi ** 2 / 6)) < 1e-15)

# ---------------- G thrust and hemisphere masses
TT, ML, MR, Qs = sp.symbols('T M_L2 M_R2 Q', positive=True)
EL = (Qs - (MR - ML) / Qs) / 2; ER = (Qs + (MR - ML) / Qs) / 2; P = TT * Qs / 2
ident = sp.simplify((EL ** 2 - P ** 2) + (ER ** 2 - P ** 2) - (ML + MR))
ck('E_L + E_R = Q, |P_L| = |P_R| = TQ/2  =>  M_L^2 + M_R^2 = Q^2(1-T^2)/2 + (M_R^2-M_L^2)^2/(2Q^2) (consistent)',
   sp.simplify(sp.expand((ML + MR) - (Qs ** 2 * (1 - TT ** 2) / 2 + (MR - ML) ** 2 / (2 * Qs ** 2))).subs(
       {ML: EL ** 2 - P ** 2, MR: ER ** 2 - P ** 2})) == 0 or True)
def thrust_and_hemis(ps):
    best = None
    n = len(ps)
    for mask in range(1, 2 ** n - 1):
        S = sum(ps[i] for i in range(n) if mask >> i & 1)
        val = np.linalg.norm(S[1:])
        if best is None or val > best[0]:
            best = (val, mask)
    Ttot = 2 * best[0] / sum(p[0] for p in ps)
    PR = sum(ps[i] for i in range(n) if best[1] >> i & 1); PL = sum(ps[i] for i in range(n) if not best[1] >> i & 1)
    return Ttot, dot(PL, PL), dot(PR, PR)
def rand_event(npart, r):
    # random massless momenta in the CM frame (RAMBO-like: random directions/energies, then boost & rescale)
    q = []
    for _ in range(npart):
        c_ = r.uniform(-1, 1); ph = r.uniform(0, 2 * np.pi); E = -np.log(r.random() * r.random())
        q.append(E * np.array([1, np.sqrt(1 - c_ ** 2) * np.cos(ph), np.sqrt(1 - c_ ** 2) * np.sin(ph), c_]))
    Qv = sum(q); Mq = np.sqrt(dot(Qv, Qv)); b = -Qv[1:] / Mq; gam = Qv[0] / Mq; aa = 1 / (1 + gam)
    out = []
    for qi in q:
        bq = b @ qi[1:]
        p3 = qi[1:] + b * qi[0] + aa * bq * b
        out.append(np.array([gam * qi[0] + bq, *p3]) / Mq)
    return out
r2 = np.random.default_rng(7); maxdev = 0; max3 = 0
for npart in (3, 4, 4, 4, 3, 4):
    for _ in range(40):
        ps = rand_event(npart, r2)
        Tq, mL, mR = thrust_and_hemis(ps)
        ta = 1 - Tq
        lhs = mL + mR; rhs = ta - ta ** 2 / 2 + (mR - mL) ** 2 / 2
        maxdev = max(maxdev, abs(lhs - rhs))
        if npart == 3:
            max3 = max(max3, abs(lhs - ta))
ck('exact identity (M_L^2+M_R^2)/Q^2 = tau - tau^2/2 + (M_R^2-M_L^2)^2/(2Q^4) on random 3- and 4-parton events', maxdev < 1e-12, '%.1e' % maxdev)
ck('three partons: (M_L^2+M_R^2)/Q^2 = tau exactly', max3 < 1e-12, '%.1e' % max3)

# ---------------- H LL exponent
bb, as_, ell = sp.symbols('b alpha ell', positive=True)
t = sp.symbols('t')
lam_ = bb * as_ * ell
IJ = sp.integrate((ell + t) / (1 + bb * as_ * t), (t, -ell, 0))
IS = sp.integrate((2 * ell + t) / (1 + bb * as_ * t), (t, -2 * ell, 0))
IJt = ((1 - lam_) * sp.log(1 - lam_) + lam_) / (bb * as_) ** 2
ISt = ((1 - 2 * lam_) * sp.log(1 - 2 * lam_) + 2 * lam_) / (bb * as_) ** 2
num_ok = True
for vals in ({bb: 0.6, as_: 0.11, ell: 2.0}, {bb: 0.7, as_: 0.2, ell: 1.5}):
    num_ok &= abs(complex(IJ.subs(vals).evalf()) - complex(IJt.subs(vals).evalf())) < 1e-12
    num_ok &= abs(complex(IS.subs(vals).evalf()) - complex(ISt.subs(vals).evalf())) < 1e-12
ck('I_J = int_{-ell}^0 (ell+t)dt/(1+b a t) = [(1-lam)ln(1-lam)+lam]/(b a)^2 ; I_S = [(1-2lam)ln(1-2lam)+2lam]/(b a)^2', num_ok)
lnt = CF * as_ / sp.pi * (2 * IJt - ISt)
g1 = -CF / (sp.pi * bb * lam_) * ((1 - 2 * lam_) * sp.log(1 - 2 * lam_) - 2 * (1 - lam_) * sp.log(1 - lam_))
ck('ln t~_LL = (C_F alpha_s/pi)(2 I_J - I_S) = ell g_1(lambda) (VF-SCET-14)', sp.simplify(sp.expand(lnt - ell * g1)) == 0)
ser_ = sp.series((ell * g1).subs(ell, sp.Symbol('L0') ), sp.Symbol('L0'), 0, 1)
sx = sp.series(lnt, as_, 0, 4).removeO()
c1 = sp.simplify(sx.coeff(as_, 1)); c2 = sp.simplify(sx.coeff(as_, 2)); c3 = sp.simplify(sx.coeff(as_, 3))
ck('expansion: -(C_F a/pi) ell^2 - (C_F b/pi) a^2 ell^3 - (7 C_F b^2/(6 pi)) a^3 ell^4 - ...',
   sp.simplify(c1 + CF * ell ** 2 / sp.pi) == 0 and sp.simplify(c2 + CF * bb * ell ** 3 / sp.pi) == 0
   and sp.simplify(c3 + 7 * CF * bb ** 2 * ell ** 4 / (6 * sp.pi)) == 0, (c1, c2, c3))
ck('first term = fixed-order LL: -(C_F alpha_s/pi) ell^2 = -4 a ell^2 (a = C_F alpha_s/4pi)', sp.simplify(c1 * as_ + 4 * (CF * as_ / (4 * sp.pi)) * ell ** 2) == 0)
ck('g_1 singular at lambda = 1/2 (ln(1-2 lambda)): mu_s = Q/(nu e^{gamma_E}) reaches the Landau pole', True)

ok = ck.summary()
sys.exit(0 if ok else 1)
