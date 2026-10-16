"""
s5_grammer_yennie.py -- item (5): K/G (Grammer-Yennie-type) decompositions and their power counting.

Light-front conventions of CONTEXT.md:  v.w = v^+w^- + v^-w^+ - v_T.w_T ;  hadron A along +z.
  nA = (1,0,0_T)  [nA.v = v^-],     nB = w2 = (0,1,0_T)  [nB.v = v^+]   (Collins' w_2)

COLLINEAR (A-collinear gluon k between the A-collinear subgraph C (index nu) and the hard part H (index mu),
k flowing into H) -- Collins (2011) eqs. (11.5)-(11.6) as corrected in his errata:
    g_{mu nu} = K_{mu nu} + G_{mu nu},   K_{mu nu} = k_mu w2_nu/(k.w2 - i0),   G = g - K.
  Exact properties: G^{mu nu} k_nu = 0 (G kills the scalar polarization on the C side);
                    k_mu K^{mu nu} C_nu feeds the Ward identity on H.
  Power counting: C^nu = (C^+/k^+) k^nu + O(lambda) => H.G.C / H.C = O(lambda) (unless H.k = 0, see below).
SOFT (soft gluon k between an A-collinear (jet) line (index mu) and the soft subgraph S (index nu)):
    K_s^{mu nu} = k^mu nA^nu/(nA.k +- i0),  G_s = g - K_s.
  Power counting: J^mu ~ J^+ nA^mu + O(lambda) => J.G_s.S / J.S = O(lambda * |k_T|/|k^-|):
  O(lambda) for soft k (k^+ ~ k^- ~ k_T), O(1) in the Glauber region |k^-| << |k_T|.
GLUON PDF: if the only collinear parton entering H is a gluon, H.k = 0 (Ward identity) so the K term vanishes and
  H.C = H.G.C = -H_T.(C_T - (k_T/k^+) C^+) + H^+ (C^- - (k^-/k^+) C^+)   (field-strength combination k^+A^j - k^jA^+).
Checks: sympy algebra; one-loop DIS vertex integrand (collinear region) with explicit spinors; soft/Glauber scan;
photon-gluon fusion hard part for the gluon-PDF case.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *
import sympy as sp

R = Report('s5_grammer_yennie')
g = 1.0
rng = np.random.default_rng(1618)

# ======================================================================== (1) algebra (sympy, light-front components)
print('--- (1) algebraic properties ---')
kp, km, k1, k2 = sp.symbols('k_p k_m k_1 k_2', real=True)
Hp, Hm, H1, H2, Cp, Cm, C1, C2 = sp.symbols('H_p H_m H_1 H_2 C_p C_m C_1 C_2')


def dot(a, b):   # a, b = (plus, minus, T1, T2)
    return a[0] * b[1] + a[1] * b[0] - a[2] * b[2] - a[3] * b[3]


kv = (kp, km, k1, k2); Hv = (Hp, Hm, H1, H2); Cv = (Cp, Cm, C1, C2)
w2 = (0, 1, 0, 0)        # nB: w2.v = v^+
nA = (1, 0, 0, 0)        # nA.v = v^-
HKC = dot(Hv, kv) * dot(w2, Cv) / dot(kv, w2)
HGC = dot(Hv, Cv) - HKC
R.flag('(1) w2.v = v^+ and nA.v = v^-', sp.simplify(dot(w2, Cv) - Cp) == 0 and sp.simplify(dot(nA, Cv) - Cm) == 0)
# G^{mu nu} k_nu = 0 : replace C by k
R.flag('(1) collinear: H.G.k = 0 for any H (G annihilates the scalar polarization on the C side)',
       sp.simplify(HGC.subs({Cp: kp, Cm: km, C1: k1, C2: k2})) == 0)
# H.G.C = H.(C - (C^+/k^+) k) - 0  (identity)
X = tuple(Cv[i] - Cp / kp * kv[i] for i in range(4))
R.flag('(1) collinear: H.G.C = H.(C - (C^+/k^+) k) - [H.k] [w2.(C-(C^+/k^+)k)]/k^+ = H.(C - (C^+/k^+) k)',
       sp.simplify(HGC - dot(Hv, X)) == 0)
# soft: J.G_s.S with K_s = k^mu nA^nu/(nA.k)
Jp, Jm, J1, J2, Sp, Sm, S1, S2 = sp.symbols('J_p J_m J_1 J_2 S_p S_m S_1 S_2')
Jv = (Jp, Jm, J1, J2); Sv = (Sp, Sm, S1, S2)
JGS = dot(Jv, Sv) - dot(Jv, kv) * dot(nA, Sv) / dot(nA, kv)
R.flag('(1) soft: (J^+ nA).G_s.S = 0 exactly (pure eikonal current along nA decouples from G_s)',
       sp.simplify(JGS.subs({Jm: 0, J1: 0, J2: 0})) == 0)
R.flag('(1) soft: J.G_s.S = J^- S^+ - J_T.S_T - (J^- k^+ - J_T.k_T) S^-/k^-  (remainder involves J_T k_T/k^-)',
       sp.simplify(JGS - (Jm * Sp - J1 * S1 - J2 * S2 - (Jm * kp - J1 * k1 - J2 * k2) * Sm / km)) == 0)
# gluon-PDF identity: if H.k = 0 then H.C = H^+(C^- - k^- C^+/k^+) - H_T.(C_T - k_T C^+/k^+)
sol_Hm = sp.solve(sp.Eq(dot(Hv, kv), 0), Hm)[0]
lhs = dot(Hv, Cv).subs(Hm, sol_Hm)
rhs = Hp * (Cm - km * Cp / kp) - H1 * (C1 - k1 * Cp / kp) - H2 * (C2 - k2 * Cp / kp)
R.flag('(1) gluon PDF: H.k = 0 => H.C = H^+(C^- - k^-C^+/k^+) - H_T.(C_T - k_T C^+/k^+)', sp.simplify(lhs - rhs) == 0)
# original Grammer-Yennie form (as reproduced by Sen-Indumathi-Choudhury 2019, eq. 9): K = b_k k_mu k_nu,
# b_k = 1/2 [ (2pf-k).(2pi-k)/(((pf-k)^2-m^2)((pi-k)^2-m^2)) + (k -> -k) ] ; property: contracted with the two
# convection currents it reproduces their eikonal (IR) product at small k (checked numerically below)

# ======================================================================== (2) collinear region: one-loop DIS vertex
print('--- (2) collinear region: one-loop DIS vertex integrand, K/G split ---')
Qv = 3.0
Pp = 2.0                                   # P^+
P = lc(Pp, 0.0)                            # massless target quark along +z
q = lc(-Pp, Qv**2 / (2 * Pp))              # x = 1 kinematics (Breit frame): p' = P + q on shell along -z
pp = P + q
R.check('(2) p\' = P + q on shell (x = 1)', abs(mdot(pp, pp)), 1e-12)
w = NB
nu = 1
Gam = GAM[nu]
xi = 0.37
kap_m, kap_t = rng.normal(size=1)[0], rng.normal(size=2)


def k_coll(lam):
    return lc(xi * Pp, lam**2 * Qv * kap_m, lam * Qv * kap_t[0], lam * Qv * kap_t[1])


lams = [1e-1, 1e-2, 1e-3, 1e-4]
ratios = []; kexact = []
for lam in lams:
    k = k_coll(lam)
    fulls = []; Gs = []; kes = []
    for s1 in range(2):
        for s2 in range(2):
            ub = bar(u_spinor(pp, s1)); u = u_spinor(P, s2)
            full = sum(METRIC[al, al] * ub @ (1j * g * GAM[al]) @ S_quark(pp - k) @ Gam @ S_quark(P - k) @ (1j * g * GAM[al]) @ u
                       for al in range(4))
            Kt = ub @ (1j * g * slash(k)) @ S_quark(pp - k) @ Gam @ S_quark(P - k) @ (1j * g * slash(w)) @ u / mdot(k, w)
            # Ward identity: K term == Wilson-line graph of the PDF times the Born vertex
            wl = (g * ub @ Gam) @ S_quark(P - k) @ (1j * g * slash(w)) @ u / mdot(k, w)
            fulls.append(abs(full)); Gs.append(abs(full - Kt)); kes.append(abs(Kt - wl))
    # normalize by the largest (helicity-allowed) amplitude; helicity-forbidden ones vanish identically
    ratios.append(max(Gs) / max(fulls)); kexact.append(max(kes) / max(fulls))
slope = np.polyfit(np.log10(lams[1:]), np.log10(ratios[1:]), 1)[0]
R.check(f'(2) on-shell massless parent quark: |G|/|full| at lambda=1e-4 (slope {slope:.2f})', ratios[-1], 1e-2)
R.flag('(2) on-shell massless parent: G suppressed by lambda^2 (bad components of u(P) vanish: Pslash u(P)=0)',
       1.85 < slope < 2.15)
R.check('(2) K term == g * Born x [PDF Wilson-line vertex graph] exactly (Ward identity), normalized', max(kexact), 1e-12)

# generic off-shell collinear parent: C^beta = S(l-k) i g gamma^beta chi, chi = lslash eta, l collinear off shell;
# generic hard row spinor etap. Here the bad spinor components are O(lambda), so G is suppressed by lambda^1.
eta = rng.normal(size=4) + 1j * rng.normal(size=4)
etap = rng.normal(size=4) + 1j * rng.normal(size=4)
lam_list = [1e-2, 1e-3, 1e-4, 1e-5]
rg = []
for lam in lam_list:
    k = k_coll(lam)
    l = lc(Pp, lam**2 * Qv * 0.7, lam * Qv * 0.4, -lam * Qv * 0.9)
    chi = slash(l) @ eta
    Hd = [etap @ GAM[al] @ S_quark(l + q - k) @ Gam for al in range(4)]      # hard part (row spinors), index up
    Cd = [S_quark(l - k) @ (1j * g * GAM[be]) @ chi for be in range(4)]        # collinear part (column spinors)
    full = sum(METRIC[al, al] * Hd[al] @ Cd[al] for al in range(4))
    kH = sum(lower(k)[al] * Hd[al] for al in range(4))
    wC = sum(lower(w)[be] * Cd[be] for be in range(4))
    Kt = kH @ wC / mdot(k, w)
    rg.append(abs(full - Kt) / abs(full))
slope_g = np.polyfit(np.log10(lam_list), np.log10(rg), 1)[0]
R.check(f'(2) generic off-shell collinear parent: |G|/|full| at lambda=1e-5 (slope {slope_g:.2f})', rg[-1], 1e-3)
R.flag('(2) generic collinear parent: G suppressed by lambda^1 (Collins 11.5-11.6 power counting)', 0.85 < slope_g < 1.15)

# ======================================================================== (3) soft region vs Glauber region
print('--- (3) soft attachment to an A-collinear line: soft vs Glauber ---')
QA = 2.5


def pA_of(lam):                 # energetic A-collinear on-shell quark with p_T ~ lam Q
    t = lam * QA * np.array([0.6, -0.3])
    return lc(QA, (t @ t) / (2 * QA), t[0], t[1])


lams = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
for trial in range(3):
    Svec = rand_vec(rng, 1.0, cplx=True)     # soft-subgraph vertex (generic)
    Xsp = rng.normal(size=4) + 1j * rng.normal(size=4)
    cs = rng.normal(size=4)
    res = {}
    for kind in ['soft', 'glauber']:
        rr = []
        for lam in lams:
            pA = pA_of(lam)
            k = lam * QA * lc(*cs) if kind == 'soft' else QA * lc(lam**2 * cs[0], lam**2 * cs[1], lam * cs[2], lam * cs[3])
            num = 0; den = 0
            for s_ in range(2):
                ub = bar(u_spinor(pA, s_))
                # jet side J^mu: soft gluon (k flowing in) absorbed by the outgoing A-collinear quark
                J = np.array([ub @ (1j * g * GAM[mu]) @ S_quark(pA - k) @ Xsp for mu in range(4)])
                full = mdot(J, Svec)
                Kpart = mdot(J, k) * mdot(NA, Svec) / mdot(NA, k)
                num = max(num, abs(full - Kpart)); den = max(den, abs(full))
            rr.append(num / den)
        res[kind] = rr
    s_soft = np.polyfit(np.log10(lams[1:]), np.log10(res['soft'][1:]), 1)[0]
    plateau = abs(res['glauber'][-1] / res['glauber'][-2] - 1)
    R.check(f'(3) trial {trial} soft region: |J.G_s.S|/|J.S| at lambda=1e-5 (slope {s_soft:.2f})', res['soft'][-1], 1e-3)
    R.flag(f'(3) trial {trial} soft region: G_s suppressed by lambda^1', 0.85 < s_soft < 1.15)
    R.flag(f'(3) trial {trial} Glauber region: G_s NOT suppressed: ratio plateaus at {res["glauber"][-1]:.3f} '
           f'(change {plateau:.1e} between lambda=1e-4 and 1e-5)', plateau < 1e-2 and res['glauber'][-1] > 1e-2)

# ======================================================================== (4) gluon-PDF case: photon-gluon fusion
print('--- (4) gluon entering H: K term vanishes, transverse (field-strength) term is leading ---')
# H^mu = amplitude gamma*(q) + g*(k, mu) -> q(p1) qbar(p2) (two diagrams), on-shell quarks, k off shell (collinear)
P2 = lc(Pp, 0.0)
for lam in [1e-1, 1e-2]:
    k = lc(xi * Pp, lam**2 * Qv * kap_m, lam * Qv * kap_t[0], lam * Qv * kap_t[1])
    qv = lc(-xi * Pp * 0.6, Qv**2 / (2 * xi * Pp * 0.6))      # some hard photon momentum
    tot = qv + k
    # final state q qbar with total momentum tot (timelike?)
    if mdot(tot, tot) <= 0:
        qv = lc(-xi * Pp * 0.3, Qv**2 / (2 * xi * Pp * 0.3)); tot = qv + k
    M = np.sqrt(mdot(tot, tot)); beta = tot[1:] / tot[0]
    # two-body decay of 'tot' into massless p1, p2
    n_ = rng.normal(size=3); n_ /= np.linalg.norm(n_)
    a_ = np.concatenate([[M / 2], M / 2 * n_]); b_ = np.concatenate([[M / 2], -M / 2 * n_])

    def boost(v):
        gam = tot[0] / M; b2 = beta @ beta; bp = beta @ v[1:]
        return np.concatenate([[gam * (v[0] + bp)], v[1:] + ((gam - 1) * bp / b2 + gam * v[0]) * beta])
    p1, p2 = boost(a_), boost(b_)
    ub = bar(u_spinor(p1, 0)); vv = v_spinor(p2, 1)
    epsph = slash(rand_vec(rng, cplx=True))
    H = np.array([ub @ (1j * g * GAM[mu]) @ S_quark(p1 - k) @ epsph @ vv + ub @ epsph @ S_quark(-p2 + k) @ (1j * g * GAM[mu]) @ vv
                  for mu in range(4)])
    C = rand_vec(rng, 1.0, cplx=True)
    # make C collinear-like: C ~ (C^+, lam^2, lam) scaling
    Cc = lc(1.0 + 0.3j, lam**2 * (0.5 - 0.2j), lam * (0.7 + 0.1j), lam * (-0.4 + 0.3j))
    kH = mdot(k, H)
    R.check(f'(4) lambda={lam}: k.H = 0 (gluon-initiated hard part, on-shell quarks)', abs(kH) / np.abs(H).max(), 1e-12)
    HC = mdot(H, Cc)
    lcH = lc_comp(H); lcC = lc_comp(Cc); lck = lc_comp(k)
    trans = lcH[0] * (lcC[1] - lck[1] * lcC[0] / lck[0]) - (lcH[2] * (lcC[2] - lck[2] * lcC[0] / lck[0]) + lcH[3] * (lcC[3] - lck[3] * lcC[0] / lck[0]))
    R.check(f'(4) lambda={lam}: H.C == H^+(C^- - k^-C^+/k^+) - H_T.(C_T - k_T C^+/k^+)', abs(HC - trans) / abs(HC), 1e-10)
    Kterm = kH * mdot(w, Cc) / mdot(k, w)
    R.check(f'(4) lambda={lam}: K term = 0, so H.C = H.G.C (G gluon is the leading parton)', abs(Kterm) / abs(HC), 1e-10)

# ======================================================================== (5) original GY K-photon (QED, symmetric form)
print('--- (5) original Grammer-Yennie K photon (QED form) ---')
# e(p_i) -> e(p_f) + virtual photon k exchanged between the final and initial lines; check that
#   b_k (2pf-k)^mu (2pi-k)^nu k_mu k_nu / denominators  reproduces the eikonal convection-current product as k -> 0
mE = 0.5
pi_ = rand_massive(rng, mE, 1.0); pf_ = rand_massive(rng, mE, 1.0)
khat = rand_vec(rng, 1.0)
errs = []
lamsGY = [1e-2, 1e-3, 1e-4, 1e-5]
for lam in lamsGY:
    k = lam * khat
    Df = mdot(pf_ - k, pf_ - k) - mE**2; Di = mdot(pi_ - k, pi_ - k) - mE**2
    Dfm = mdot(pf_ + k, pf_ + k) - mE**2; Dim = mdot(pi_ + k, pi_ + k) - mE**2
    bk = 0.5 * (mdot(2 * pf_ - k, 2 * pi_ - k) / (Df * Di) + mdot(2 * pf_ + k, 2 * pi_ + k) / (Dfm * Dim))
    # K-photon contribution between scalar-like convection vertices (2p - k): (2pf-k).K.(2pi-k)/(Df Di)
    jf = (2 * pf_ - k) / Df; ji = (2 * pi_ - k) / Di
    Kc = bk * mdot(jf, k) * mdot(k, ji)
    full = mdot(jf, ji)
    errs.append(abs(Kc - full) / abs(full))
slopeGY = np.polyfit(np.log10(lamsGY), np.log10(errs), 1)[0]
R.flag(f'(5) GY K photon = full eikonal product + O(k): rel. err {errs[-1]:.1e} at lambda=1e-5, slope {slopeGY:.2f}',
       0.85 < slopeGY < 1.15 and errs[-1] < 1e-3)

R.summary()
