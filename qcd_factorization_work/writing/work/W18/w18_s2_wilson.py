# -*- coding: utf-8 -*-
"""
w18_s2_wilson.py -- Ch15 sec:scet-lagrangian (prop:scet-wilson, ex:scet-wn-tree), sec:scet-decoupling
(thm:scet-decoupling key identity, ex:scet-decoupling-tree, rem:scet-y-direction), sec:scet-scet2 (prop:scet-scet2).
Own implementation. Checks:
  A one-gluon Wilson-line rules (absorption/emission) from the line integrals;
  B tree matching gamma* -> q(p1) qbar(p2) g(k), k || n: antiquark-emission graph -> W_n term; full amplitude QCD = SCET;
    Ward identity in QCD and in SCET (collinear vertex term + W_n term = 0 exactly);
  C two collinear gluons on the nbar line: LP product of eikonal factors = O(g^2) term of W_n (with colour order);
  D SCET_II: soft gluon on an outgoing collinear quark -> eikonal factor of S_n (rel. error O(lambda));
  E usoft gluons absorbed/emitted by an outgoing collinear quark (LO SCET rules) = future-pointing Wilson line;
  F key identity in.D_us (Y f) = Y in.d f, conjugation identity, gauge covariance, W_n[Y A Y^dag] = Y W_n Y^dag.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import *
import sympy as sp

ck = Check('W18 s2: Wilson lines W_n, Y_n, S_n; tree matching; key identity of the BPS decoupling')
rng = np.random.default_rng(1515)

# ---------------- A one-gluon rules
s, kb, dl = sp.symbols('s k delta', real=True)
I_abs = sp.integrate(sp.exp(-sp.I * s * kb + dl * s), (s, -sp.oo, 0), conds='none')
I_emi = sp.integrate(sp.exp(+sp.I * s * kb + dl * s), (s, -sp.oo, 0), conds='none')
ck('int_{-inf}^0 ds e^{-i s nbar.k + delta s} = i/(nbar.k + i delta)  => absorbed gluon: i g * i/(nbar.k+i0) = -g/(nbar.k+i0)',
   sp.simplify(I_abs - sp.I / (kb + sp.I * dl)) == 0, sp.simplify(I_abs))
ck('int_{-inf}^0 ds e^{+i s nbar.k + delta s} = -i/(nbar.k - i delta)  => emitted gluon: +g nbar.eps*/(nbar.k - i0)',
   sp.simplify(I_emi + sp.I / (kb - sp.I * dl)) == 0, sp.simplify(I_emi))

# ---------------- B tree matching for one collinear gluon
def kinematics(lam, Q=10.0, seed=7):
    r = np.random.default_rng(seed)
    # p1 (n-collinear quark), k (n-collinear gluon), p2 (nbar-collinear antiquark); all massless
    pt1 = np.array([0.6, -0.2]) * lam * Q; nb1 = 0.55 * Q
    ptk = np.array([-0.3, 0.45]) * lam * Q; nbk = 0.35 * Q
    pt2 = -(pt1 + ptk); n2 = 0.9 * Q
    p1 = lc_vec(nb1, pt1 @ pt1 / nb1, pt1)
    k = lc_vec(nbk, ptk @ ptk / nbk, ptk)
    p2 = lc_vec(pt2 @ pt2 / n2, n2, pt2)
    return p1, k, p2


def pol(k, r):
    """physical-like polarization: eps.k = 0 with a non-zero nbar.eps (eps = transverse vector + c k)."""
    kv = np.array(k[1:4]); kh = kv / np.linalg.norm(kv)
    a = np.array([1.0, 0.3, -0.2]); a = a - (a @ kh) * kh; a /= np.linalg.norm(a)
    eT = np.array([0.0, a[0], a[1], a[2]], dtype=complex)
    return eT + 0.8 / k[0] * np.asarray(k, dtype=complex)     # eps.k = 0, nbar.eps = O(1)


def gperp_mu(mu):
    return GAM[mu] - NV[mu] * NBSL / 2 - NBV[mu] * NSL / 2


chi1 = np.array([1.0, 0.2j, -0.4, 0.3]); chi2 = np.array([0.3, -0.7, 0.1j, 1.0])
mu_c = 1        # current index gamma^mu, mu = 1 (transverse component; gamma^1 = gamma_perp^1)
errs_W, errs_full, wards = [], [], []
for lam in (1e-1, 1e-2, 1e-3):
    p1, k, p2 = kinematics(lam)
    eps = pol(k, rng); epsc = np.conj(eps)
    u = massless_spinor(p1, chi1); ub = bar(u)
    v = massless_spinor(p2, chi2)
    G = GAM[mu_c]
    S = lambda q: 1j * slash(q) / dot(q, q)
    # QCD: emission from the quark p1 and from the antiquark p2 (colour t^a stripped, g = 1)
    M_q = ub @ (1j * slash(epsc)) @ S(p1 + k) @ G @ v
    M_a = ub @ G @ S(-p2 - k) @ (1j * slash(epsc)) @ v
    W_rule = (ub @ G @ v) * dot(NBV, epsc) / dot(NBV, k)
    errs_W.append(abs(M_a - W_rule) / abs(W_rule))
    # SCET: xibar_n W_n gamma_perp W_nbar^dag xi_nbar; collinear vertex on the quark line + W_n term
    ubn = ub @ PNB; vn = PNB @ v
    # SCET collinear vertex: incoming quark momentum p1+k (from the current), outgoing p1; propagator S_xi(p1+k)
    def Vdot(p_in, p_out, e):
        el = METRIC @ e
        out = np.zeros((4, 4), dtype=complex)
        pperp, poperp = slash(perp_part(p_in)), slash(perp_part(p_out))
        nbi, nbo = dot(NBV, p_in), dot(NBV, p_out)
        for m in range(4):
            out += el[m] * (NV[m] * ID4 + gperp_mu(m) @ pperp / nbi + poperp @ gperp_mu(m) / nbo
                            - poperp @ pperp * NBV[m] / (nbi * nbo))
        return 1j * out @ (NBSL / 2)
    Sxi = lambda q: 1j * (NSL / 2) * dot(NBV, q) / dot(q, q)
    Gp = gperp_mu(mu_c)
    M_scet_c = ubn @ Vdot(p1 + k, p1, epsc) @ Sxi(p1 + k) @ Gp @ vn
    M_scet_W = (ubn @ Gp @ vn) * dot(NBV, epsc) / dot(NBV, k)
    M_qcd = M_q + M_a
    errs_full.append(abs(M_qcd - (M_scet_c + M_scet_W)) / abs(M_qcd))
    # Ward identity eps* -> k
    Mq_k = ub @ (1j * slash(k)) @ S(p1 + k) @ G @ v
    Ma_k = ub @ G @ S(-p2 - k) @ (1j * slash(k)) @ v
    Sc_k = ubn @ Vdot(p1 + k, p1, k.astype(complex)) @ Sxi(p1 + k) @ Gp @ vn
    SW_k = (ubn @ Gp @ vn) * dot(NBV, k) / dot(NBV, k)
    wards.append((abs(Mq_k + Ma_k) / abs(Mq_k), abs(Sc_k + SW_k) / abs(SW_k)))
ck('antiquark-emission graph (off-shell ~Q^2) -> ubar gamma v * g nbar.eps*/nbar.k (W_n one-gluon term); rel. err O(lam)',
   errs_W[2] < 5e-3 and errs_W[0] / errs_W[2] > 50, ['%.1e' % e for e in errs_W])
ck('full tree amplitude QCD = SCET (L_xixi collinear vertex + W_n term) + O(lam)',
   errs_full[2] < 1e-3 and errs_full[0] / errs_full[2] > 50, ['%.1e' % e for e in errs_full])
ck('Ward identity eps*->k: QCD sum = 0 exactly; SCET: collinear-vertex term + W_n term = 0 exactly',
   all(a < 1e-10 and b < 1e-10 for a, b in wards), ['(%.0e, %.0e)' % w for w in wards])

# ---------------- C two collinear gluons on the nbar line: product of eikonal factors = O(g^2) term of W_n
# (i) leading field component: eps^mu = n^mu (only nbar.A_n ~ lam^0 is non-zero; A_perp ~ lam, n.A ~ lam^2 are power suppressed)
# (ii) transverse polarizations attached to the hard nbar line: suppressed by lam^2 relative to the collinear emissions
errs2, ratios = [], []
for lam in (1e-1, 1e-2, 1e-3):
    Q = 10.0
    pt1 = np.array([0.4, 0.1]) * lam * Q; nb1 = 0.4 * Q
    pk1 = np.array([-0.2, 0.3]) * lam * Q; nbk1 = 0.25 * Q
    pk2 = np.array([0.15, -0.35]) * lam * Q; nbk2 = 0.2 * Q
    pt2 = -(pt1 + pk1 + pk2); n2 = Q
    p1 = lc_vec(nb1, pt1 @ pt1 / nb1, pt1); k1 = lc_vec(nbk1, pk1 @ pk1 / nbk1, pk1); k2 = lc_vec(nbk2, pk2 @ pk2 / nbk2, pk2)
    p2 = lc_vec(pt2 @ pt2 / n2, n2, pt2)
    u = massless_spinor(p1, chi1); ub = bar(u); v = massless_spinor(p2, chi2)
    G = GAM[1]
    S = lambda q: 1j * slash(q) / dot(q, q)
    def nbar_line(e1, e2):
        A = ub @ G @ S(-p2 - k1 - k2) @ (1j * slash(e2)) @ S(-p2 - k1) @ (1j * slash(e1)) @ v   # colour t^{a2} t^{a1}
        B = ub @ G @ S(-p2 - k1 - k2) @ (1j * slash(e1)) @ S(-p2 - k2) @ (1j * slash(e2)) @ v   # colour t^{a1} t^{a2}
        return A, B
    e1 = NV.astype(complex); e2 = 0.7 * NV.astype(complex)
    A, B = nbar_line(e1, e2)
    base = ub @ G @ v
    eA = base * dot(NBV, e2) / dot(NBV, k1 + k2) * dot(NBV, e1) / dot(NBV, k1)
    eB = base * dot(NBV, e1) / dot(NBV, k1 + k2) * dot(NBV, e2) / dot(NBV, k2)
    errs2.append(max(abs(A - eA) / abs(eA), abs(B - eB) / abs(eB)))
    # transverse polarizations: hard-line attachments vs double collinear emission from the quark line
    t1 = np.array([0, 1.0, 0.4j, 0]); t1 = t1 - dot(t1, k1) / dot(NBV, k1) * NBV     # eps.k = 0, nbar.eps = 0
    t2 = np.array([0, -0.3, 1.0, 0]); t2 = t2 - dot(t2, k2) / dot(NBV, k2) * NBV
    At, Bt = nbar_line(np.conj(t1), np.conj(t2))
    Cq = ub @ (1j * slash(np.conj(t1))) @ S(p1 + k1) @ (1j * slash(np.conj(t2))) @ S(p1 + k1 + k2) @ G @ v
    ratios.append(abs(At + Bt) / abs(Cq))
ck('O(g^2): two nbar.A_n gluons on the nbar antiquark line: each ordering -> product of eikonal factors in the W_n colour order; rel. err O(lam)',
   errs2[2] < 5e-3 and errs2[0] / errs2[2] > 50, ['%.1e' % e for e in errs2])
ck('transverse collinear gluons attached to the hard nbar line are suppressed by ~lam^2 relative to the double collinear emission',
   ratios[1] / ratios[2] > 50 and ratios[2] < 1e-4, ['%.1e' % r for r in ratios])

# ---------------- D SCET_II: soft gluon emitted by an outgoing collinear quark -> eikonal factor (S_n)
def scet2_err(lam, ksoft_dir, eps):
    Q = 10.0
    nbp = 0.8 * Q; pt = np.array([0.5, -0.3]) * lam * Q
    p = lc_vec(nbp, pt @ pt / nbp, pt)
    ks = np.array(ksoft_dir) * lam * Q
    u = massless_spinor(p, chi1); ub = bar(u)
    G = GAM[2]
    exact = ub @ (1j * slash(eps)) @ (1j * slash(p + ks) / dot(p + ks, p + ks)) @ G
    eik = (ub @ G) * (-dot(NV, eps) / dot(NV, ks))
    return np.max(np.abs(exact - eik)) / np.max(np.abs(eik))

e_c = np.array([0.2, 0.5 + 0.3j, -0.1, 0.4])
errs_s = [scet2_err(l, [1.0, 0.3, -0.6, 0.2], e_c) for l in (1e-1, 1e-2, 1e-3)]
ck('SCET_II (c_scet kinematic point): (p+k_s)^2 ~ lam Q^2, exact emission vs eikonal -n.eps/n.k: rel. err O(lam)',
   errs_s[2] < 1e-2 and errs_s[0] / errs_s[1] > 5 and errs_s[1] / errs_s[2] > 9, ['%.2e' % e for e in errs_s])
errs_s2 = [scet2_err(l, [0.7, -0.2, 0.5, -0.1], np.array([0.1, -0.4j, 0.6, 0.3])) for l in (1e-1, 1e-2, 1e-3)]
ck('SCET_II, second kinematic point: rel. err O(lam)', errs_s2[1] / errs_s2[2] > 9, ['%.2e' % e for e in errs_s2])
lam_ = 0.01; Q = 10.0
p = lc_vec(0.8 * Q, 0, [0, 0]); ks = np.array([1.0, 0.3, -0.6, 0.2]) * lam_ * Q
ck('virtuality of the intermediate line: (p+k_s)^2/Q^2 ~ lam (hard-collinear), not lam^2',
   0.1 < dot(p + ks, p + ks) / (lam_ * Q * Q) < 10, '%.3f' % (dot(p + ks, p + ks) / (lam_ * Q * Q)))

# ---------------- E usoft gluons and an OUTGOING collinear quark (LO SCET rules are exact in SCET)
# vertex i g t^a n.eps nbarslash/2; propagator i (nslash/2) nbar.p/(p_int^2 + i0) with p_int^2 = -nbar.p n.K for on-shell p
ok1, ok2, ok3 = True, True, True
for _ in range(5):
    nbp = 3.0 + rng.random(); pt = rng.normal(size=2); p = lc_vec(nbp, pt @ pt / nbp, pt)
    u = massless_spinor(p, chi1); ubn = bar(u) @ PNB
    ta, tb = TGEN[2], TGEN[5]
    d0 = 0.0
    nk1, nk2 = rng.normal(), rng.normal()
    # one absorbed gluon (k into the line): internal momentum p - k1
    prop1 = 1j * (NSL / 2) * nbp / (-nbp * nk1 + 1j * d0)
    amp1 = np.kron(ta, ubn @ (1j * NBSL / 2) @ prop1)                 # colour x Dirac (row spinor)
    rule1 = np.kron(ta, ubn) / (nk1 - 1j * d0)                        # future-pointing: g t^a n.eps/(n.k - i0)
    ok1 &= np.allclose(amp1, rule1, atol=1e-6)
    # two absorbed gluons: sum over the two orderings along the outgoing quark line
    #   gluon b absorbed last (nearest the final quark): colour t^b t^a, denominators n.k_b, n.(k_a+k_b)
    def chain(first, second, nkf, nks):
        # first = absorbed nearest the hard vertex, second = absorbed nearest the final state
        pr_last = 1j * (NSL / 2) * nbp / (-nbp * nks + 1j * d0)              # momentum p - k_second
        pr_first = 1j * (NSL / 2) * nbp / (-nbp * (nks + nkf) + 1j * d0)     # momentum p - k_second - k_first
        return np.kron(second @ first, ubn @ (1j * NBSL / 2) @ pr_last @ (1j * NBSL / 2) @ pr_first)
    amp2 = chain(ta, tb, nk1, nk2) + chain(tb, ta, nk2, nk1)
    rule2 = (np.kron(tb @ ta, ubn) / ((nk2 - 1j * d0) * (nk1 + nk2 - 1j * d0))
             + np.kron(ta @ tb, ubn) / ((nk1 - 1j * d0) * (nk1 + nk2 - 1j * d0)))
    ok2 &= np.allclose(amp2, rule2, rtol=1e-10, atol=1e-12)
    # one EMITTED usoft gluon (outgoing k): internal momentum p + k, (p+k)^2 = nbar.p n.k
    prop_e = 1j * (NSL / 2) * nbp / (nbp * nk1 + 1j * d0)
    amp_e = np.kron(ta, ubn @ (1j * NBSL / 2) @ prop_e)
    rule_e = -np.kron(ta, ubn) / (nk1 + 1j * d0)                       # future-pointing rule with inflow -k
    ok3 &= np.allclose(amp_e, rule_e, atol=1e-6)
ck('one usoft gluon ABSORBED by an outgoing n-collinear quark: ubar_n g t^a n.eps/(n.k - i0)  (future-pointing line)', ok1)
ck('two absorbed usoft gluons: sum over orderings = g^2[t^b t^a/((n.k_b-i0)(n.(k_a+k_b)-i0)) + (a<->b)] = W[x+inf n, x] at O(g^2)', ok2)
ck('one usoft gluon EMITTED (outgoing k): ubar_n (-g t^a n.eps*/(n.k + i0)) = future-pointing rule with inflow -k', ok3)
# the future-pointing Feynman rule (prop:prelim-wilson-rules): W[inf n, 0]: prod_j (-i)/(n.(k_j+...+k_m) - i0), vertices i g t n
K1, K2 = sp.symbols('K1 K2')
fp = sp.simplify((sp.I) ** 2 * (-sp.I) / (K1 + K2) * (-sp.I) / K2)        # (ig)^2 with g=1, gluons ordered 1 then 2 outward
ck('future-pointing rule (ig)^2 (-i)^2/[n.(k1+k2) n.k2] = 1/[n.(k1+k2) n.k2] (matches the two-gluon chain)',
   sp.simplify(fp - 1 / ((K1 + K2) * K2)) == 0)

# ---------------- F key identity and related Wilson-line identities (numerical, random su(3) backgrounds)
class SmoothField:
    """a(s) = sum_j c_j exp(-(s-s_j)^2/w_j^2) T_j, hermitian su(3)-valued, negligible for s < -12."""
    def __init__(self, seed, nb=4, amp=0.8):
        r = np.random.default_rng(seed)
        self.T = [rand_su3_alg(r) for _ in range(nb)]
        self.s0 = r.uniform(-4, 1, size=nb); self.w = r.uniform(0.6, 1.4, size=nb); self.c = amp * r.normal(size=nb)
    def __call__(self, s):
        return sum(c * np.exp(-((s - s0) / w) ** 2) * T for c, s0, w, T in zip(self.c, self.s0, self.w, self.T))

a_us = SmoothField(11)
smin = -14.0
def Y_at(s, field=a_us, nstep=3000):
    return path_ordered(field, smin, s, nstep=nstep)
# (i d/ds + a(s)) [Y(s) f(s)] = Y(s) i f'(s)
fvec = lambda s: np.array([np.sin(s), np.cos(0.7 * s) + 0.2j, 0.3 * s * np.exp(-s * s / 9)], dtype=complex)
fder = lambda s: np.array([np.cos(s), -0.7 * np.sin(0.7 * s), 0.3 * np.exp(-s * s / 9) * (1 - 2 * s * s / 9)], dtype=complex)
errs = []
for s0 in (-2.0, -0.5, 0.7):
    h = 1e-4
    Yp, Ym, Y0 = Y_at(s0 + h), Y_at(s0 - h), Y_at(s0)
    dYf = (Yp @ fvec(s0 + h) - Ym @ fvec(s0 - h)) / (2 * h)
    lhs = 1j * dYf + a_us(s0) @ Y0 @ fvec(s0)
    rhs = Y0 @ (1j * fder(s0))
    errs.append(np.max(np.abs(lhs - rhs)))
ck('KEY IDENTITY: (i n.d + g n.A_us)(Y_n f) = Y_n i n.d f  (Y_n = W[x, x - inf n], random su(3) usoft field)',
   max(errs) < 1e-6, '%.1e' % max(errs))
# conjugation: Y^dag (i d + a_us + a_c) Y f = (i d + a_c0) f   with a_c = Y a_c0 Y^dag
a_c0 = SmoothField(23, amp=0.5)
errs = []
for s0 in (-1.0, 0.3):
    h = 1e-4
    Y0 = Y_at(s0)
    ac = lambda s: Y_at(s) @ a_c0(s) @ Y_at(s).conj().T
    g_ = lambda s: Y_at(s) @ fvec(s)
    lhs = Y0.conj().T @ (1j * (g_(s0 + h) - g_(s0 - h)) / (2 * h) + (a_us(s0) + ac(s0)) @ g_(s0))
    rhs = 1j * fder(s0) + a_c0(s0) @ fvec(s0)
    errs.append(np.max(np.abs(lhs - rhs)))
ck('Y^dag (in.d + g n.A_us + g n.A_n) Y = in.d + g n.A_n^(0) for A_n = Y A_n^(0) Y^dag', max(errs) < 1e-6, '%.1e' % max(errs))
# unitarity / determinant and composition
Ya = Y_at(0.5); Yb = Y_at(-0.7)
W_ba = path_ordered(a_us, -0.7, 0.5, nstep=3000)
ck('Y unitary, det Y = 1; composition W[b,c] W[c,a] = W[b,a] (later points to the left)',
   np.allclose(Ya.conj().T @ Ya, np.eye(3), atol=1e-9) and abs(np.linalg.det(Ya) - 1) < 1e-8
   and np.allclose(W_ba @ Yb, Ya, atol=1e-8))
# gauge covariance: A' = U A U^dag - (i/g)(dU)U^dag  ->  W' [b,a] = U(b) W[b,a] U^dag(a)  (here g=1, a = v.A)
Ugen = rand_su3_alg(np.random.default_rng(5))
wU, VU = np.linalg.eigh(Ugen)
theta = lambda s: 1.3 * np.tanh(s)             # smooth, U -> const at large |s|
dtheta = lambda s: 1.3 / np.cosh(s) ** 2
Uf = lambda s: VU @ np.diag(np.exp(1j * theta(s) * wU)) @ VU.conj().T
def a_prime(s):
    U0 = Uf(s); dU = 1j * dtheta(s) * Ugen @ U0
    return U0 @ a_us(s) @ U0.conj().T - 1j * dU @ U0.conj().T
Wp = path_ordered(a_prime, -1.0, 0.6, nstep=2000)
Wo = path_ordered(a_us, -1.0, 0.6, nstep=2000)
ck("gauge covariance W'[b,a] = U(b) W[b,a] U^dag(a) for A' = U A U^dag - (i/g)(dU)U^dag  (law of D = d - igA)",
   np.allclose(Wp, Uf(0.6) @ Wo @ Uf(-1.0).conj().T, atol=1e-6))
# W_n[Y A^(0) Y^dag] = Y W_n[A^(0)] Y^dag for Y constant along nbar
Yc = Y_at(0.2); a0 = SmoothField(31)
lhsW = path_ordered(lambda t: Yc @ a0(t) @ Yc.conj().T, smin, 0.0, nstep=3000)
rhsW = Yc @ path_ordered(a0, smin, 0.0, nstep=3000) @ Yc.conj().T
ck('W_n[Y A_n^(0) Y^dag] = Y W_n[A_n^(0)] Y^dag (Y independent of the position along nbar at LP)', np.allclose(lhsW, rhsW, atol=1e-10))

ok = ck.summary()
sys.exit(0 if ok else 1)
