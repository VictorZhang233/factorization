# -*- coding: utf-8 -*-
"""
s1_wilson_decoupling.py -- Part (1b): collinear and ultrasoft Wilson lines, the BPS decoupling
identity, eikonal Feynman rules, and the tree-level QCD -> SCET matching that generates W_n.

Conventions: D = d - i g A (CONTEXT.md);  W[b,a] = P exp(i g int_a^b dz.A), later points to the left.
  W_n(x) = W[x, x - inf nbar] = P exp( i g int_{-inf}^0 ds nbar.A_n(x + s nbar) )
  Y_n(x) = W[x, x - inf n]    = P exp( i g int_{-inf}^0 ds n.A_us(x + s n) )
Along the line z(s) = x0 + s v these satisfy dW(s)/ds = i g v.A(z(s)) W(s), i.e. v.D W = 0.

Run:  python3 -I s1_wilson_decoupling.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

ck = Check('s1_wilson_decoupling: Wilson lines, key identity n.D_us Y_n = Y_n n.d, eikonal rules, W_n from QCD')
rng = np.random.default_rng(7)
T = T_SU3
g = 1.3

# ------------------------------------------------------------------ background su(3) field along a line
class Field:
    def __init__(self, seed, nb=4, amp=1.0):
        r = np.random.default_rng(seed)
        self.c = r.normal(size=(8, nb)) * amp
        self.s0 = r.uniform(-3, 3, size=(8, nb))
        self.w = r.uniform(0.6, 1.8, size=(8, nb))

    def coeffs(self, s):
        return np.sum(self.c * np.exp(-((s - self.s0) / self.w) ** 2), axis=1)

    def __call__(self, s):
        return np.einsum('a,aij->ij', self.coeffs(s), T)

    def deriv(self, s):
        d = np.sum(self.c * np.exp(-((s - self.s0) / self.w) ** 2) * (-2 * (s - self.s0) / self.w ** 2), axis=1)
        return np.einsum('a,aij->ij', d, T)


def wilson_path(field, s_start, s_end, h=2e-3, W0=None):
    """solve dW/ds = i g a(s) W, W(s_start) = W0 (default 1), RK4; returns grid and W(s) on grid"""
    N = int(round((s_end - s_start) / h))
    ss = np.linspace(s_start, s_end, N + 1)
    W = np.eye(3, dtype=complex) if W0 is None else W0.copy()
    out = np.empty((N + 1, 3, 3), dtype=complex)
    out[0] = W
    f = lambda s, W: 1j * g * field(s) @ W
    for i in range(N):
        s = ss[i]
        k1 = f(s, W); k2 = f(s + h / 2, W + h / 2 * k1); k3 = f(s + h / 2, W + h / 2 * k2); k4 = f(s + h, W + h * k3)
        W = W + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out[i + 1] = W
    return ss, out


A = Field(11)
s_inf = -14.0         # "minus infinity": field ~ exp(-(14-3)^2/1.8^2) ~ 1e-16
ss, Ws = wilson_path(A, s_inf, 4.0)
h = ss[1] - ss[0]
idx = lambda s: int(round((s - s_inf) / h))
def d5(F, i):
    # 5-point central difference, error O(h^4)
    return (-F(i + 2) + 8 * F(i + 1) - 8 * F(i - 1) + F(i - 2)) / (12 * h)

# A1 unitarity, det
uni = max(np.max(np.abs(W.conj().T @ W - np.eye(3))) for W in Ws[::500])
dets = max(abs(np.linalg.det(W) - 1) for W in Ws[::500])
ck('W unitary and unimodular along the path', uni < 1e-9 and dets < 1e-9, f'max|W^dag W - 1| = {uni:.1e}, max|det W - 1| = {dets:.1e}')

# A2 defining derivative: (d/ds - i g a(s)) W(s) = 0   <=>  v.D W = 0 with D = d - igA
err = 0
for s in np.linspace(-3, 3, 13):
    i = idx(s)
    dW = d5(lambda j: Ws[j], i)
    err = max(err, np.max(np.abs(dW - 1j * g * A(ss[i]) @ Ws[i])))
ck('v.D W = 0  [ dW/ds = + i g v.A W ]  (=> nbar.D W_n = 0, n.D_us Y_n = 0 as functions)', err < 1e-8, f'max err {err:.1e}')

# A3 composition / ordering: W[s2,s0] = W[s2,s1] W[s1,s0]  (later points to the left)
s1, s2 = -1.0, 2.5
_, W21 = wilson_path(A, s1, s2)
comp = np.max(np.abs(Ws[idx(s2)] - W21[-1] @ Ws[idx(s1)]))
comp_wrong = np.max(np.abs(Ws[idx(s2)] - Ws[idx(s1)] @ W21[-1]))
ck('composition W[s2,s0] = W[s2,s1] W[s1,s0] (later points to the LEFT); reversed order fails',
   comp < 1e-9 and comp_wrong > 1e-3, f'err {comp:.1e}, reversed {comp_wrong:.2f}')

# A4 perturbative expansion check of the ordering at O(g^2), small coupling
g_save = g
g = 1e-4
_, Wsmall = wilson_path(A, s_inf, 1.0)
gr = np.linspace(s_inf, 1.0, 6001)
dg = gr[1] - gr[0]
avals = np.array([A(s) for s in gr])
first = np.sum((avals[1:] + avals[:-1]) / 2, axis=0) * dg
# second order: sum_{s1 > s2} a(s1) a(s2)  (later to the left)
cum = np.cumsum(np.concatenate([np.zeros((1, 3, 3)), (avals[1:] + avals[:-1]) / 2 * dg]), axis=0)
second = np.zeros((3, 3), dtype=complex)
for i in range(1, len(gr)):
    amid = (avals[i] + avals[i - 1]) / 2
    second += amid @ ((cum[i] + cum[i - 1]) / 2) * dg
pert = np.eye(3) + 1j * g * first + (1j * g) ** 2 * second
pert_wrong = np.eye(3) + 1j * g * first + (1j * g) ** 2 * (first @ first - second)
e1 = np.max(np.abs(Wsmall[-1] - pert)); e2 = np.max(np.abs(Wsmall[-1] - pert_wrong))
ck('O(g^2) expansion: P exp = 1 + ig int a + (ig)^2 int_{s1>s2} a(s1) a(s2) + ...  (anti-ordering differs)',
   e1 < 1e-2 * e2, f'err {e1:.1e} vs anti-ordered {e2:.1e}')
g = g_save

# A5 KEY IDENTITY:  (i d/ds + g a(s)) [Y(s) f(s)] = Y(s) i f'(s)   i.e.  in.D_us Y_n = Y_n in.d
f = lambda s: np.array([np.sin(1.3 * s) + 0.2j, np.cos(0.7 * s) * np.exp(-0.1 * s * s), 0.5 * s + 1j * np.sin(s)])
fp = lambda s: np.array([1.3 * np.cos(1.3 * s), (-0.7 * np.sin(0.7 * s) - 0.2 * s * np.cos(0.7 * s)) * np.exp(-0.1 * s * s),
                         0.5 + 1j * np.cos(s)])
err = 0; err_inv = 0
for s in np.linspace(-2.5, 2.5, 11):
    i = idx(s)
    F = lambda j: Ws[j] @ f(ss[j])
    lhs = 1j * d5(F, i) + g * A(ss[i]) @ F(i)
    rhs = Ws[i] @ (1j * fp(ss[i]))
    err = max(err, np.max(np.abs(lhs - rhs)))
    err_inv = max(err_inv, np.max(np.abs(Ws[i].conj().T @ lhs - 1j * fp(ss[i]))))
ck('KEY IDENTITY  in.D_us (Y_n f) = Y_n in.d f   (operator form of n.D_us Y_n = Y_n n.d)', err < 1e-8, f'max err {err:.1e}')
ck('=> Y_n^dag in.D_us Y_n = in.d  (usoft gluons removed from the n.D term)', err_inv < 1e-8, f'max err {err_inv:.1e}')

# A6 conjugation of the collinear n.A_n term: with a_c = Y a_c0 Y^dag,
#     Y^dag (i d/ds + g a_us + g a_c) Y f = (i d/ds + g a_c0) f
Ac0 = Field(29, amp=0.7)
err = 0
for s in np.linspace(-2.5, 2.5, 11):
    i = idx(s)
    ac = Ws[i] @ Ac0(ss[i]) @ Ws[i].conj().T
    F = lambda j: Ws[j] @ f(ss[j])
    lhs = Ws[i].conj().T @ (1j * d5(F, i) + g * (A(ss[i]) + ac) @ F(i))
    rhs = 1j * fp(ss[i]) + g * Ac0(ss[i]) @ f(ss[i])
    err = max(err, np.max(np.abs(lhs - rhs)))
ck('Y^dag (in.d + g n.A_us + g n.A_n) Y = in.d + g n.A_n^(0)  for A_n = Y A_n^(0) Y^dag', err < 1e-8, f'max err {err:.1e}')

# A7 gauge covariance W[b,a] -> U(b) W[b,a] U^dag(a),  A' = U A U^dag - (i/g)(dU)U^dag  (for D = d - igA)
th = Field(41, amp=0.8)
def U(s):
    M = 1j * th(s)
    w, V = np.linalg.eig(M)
    return V @ np.diag(np.exp(w)) @ np.linalg.inv(V)
def dU(s, eps=1e-5):
    return (U(s + eps) - U(s - eps)) / (2 * eps)
class GaugeT:
    def __call__(self, s):
        return U(s) @ A(s) @ U(s).conj().T - (1j / g) * dU(s) @ U(s).conj().T
Ap = GaugeT()
sa, sb = -6.0, 2.0
_, Wab = wilson_path(A, sa, sb, h=4e-3)
_, Wpab = wilson_path(Ap, sa, sb, h=4e-3)
cov = np.max(np.abs(Wpab[-1] - U(sb) @ Wab[-1] @ U(sa).conj().T))
ck('gauge covariance W\'[b,a] = U(b) W[b,a] U^dag(a)  with A\' = U A U^dag - (i/g)(dU)U^dag', cov < 1e-7, f'err {cov:.1e}')
# Hermiticity of the transformed field (consistency of the transformation law)
herm = max(np.max(np.abs(Ap(s) - Ap(s).conj().T)) for s in (-1.0, 0.3, 1.7))
ck('transformed field is hermitian & traceless (su(3)-valued)', herm < 1e-8 and abs(np.trace(Ap(0.4))) < 1e-8)

# A8 W_n built from A_n = Y A^(0) Y^dag with Y constant along nbar:  W_n -> Y W_n^(0) Y^dag
Ycst = Ws[idx(1.0)]
class Conj:
    def __call__(self, s):
        return Ycst @ Ac0(s) @ Ycst.conj().T
_, W0 = wilson_path(Ac0, s_inf, 1.0, h=4e-3)
_, W1 = wilson_path(Conj(), s_inf, 1.0, h=4e-3)
ck('W_n[Y A^(0) Y^dag] = Y W_n[A^(0)] Y^dag  (Y usoft, constant along nbar at LO)',
   np.max(np.abs(W1[-1] - Ycst @ W0[-1] @ Ycst.conj().T)) < 1e-9)

# ------------------------------------------------------------------ B. eikonal Feynman rules
# One-gluon term of the past-pointing line W[x, x - inf v] (gluon field A(y) = int e^{-ik.y} At(k), k INTO the line):
#   i g int_{-inf}^0 ds e^{-i s v.k + 0 s} = i g * i/(v.k + i0) = -g/(v.k + i0)
# creation of an outgoing gluon (A contains e^{+ik.y} eps*):  i g int e^{+i s v.k + 0 s} = g/(v.k - i0)
s_ = sp.Symbol('s', real=True); vk = sp.Symbol('vk', real=True); d0 = sp.Symbol('delta', positive=True)
I1 = sp.integrate(sp.exp((-sp.I * vk + d0) * s_), (s_, -sp.oo, 0), conds='none')
ck('int_{-inf}^0 ds e^{-i s v.k + delta s} = i/(v.k + i delta)', sp.simplify(I1 - sp.I / (vk + sp.I * d0)) == 0, str(sp.simplify(I1)))
I2 = sp.integrate(sp.exp((sp.I * vk + d0) * s_), (s_, -sp.oo, 0), conds='none')
ck('int_{-inf}^0 ds e^{+i s v.k + delta s} = -i/(v.k - i delta)  => W_n creates gluon with +g nbar.eps*/(nbar.k - i0)',
   sp.simplify(I2 + sp.I / (vk - sp.I * d0)) == 0)

# B2: usoft gluons absorbed by an outgoing on-shell n-collinear quark, LO SCET rules:
#   vertex  i g t^a n^mu nbarslash/2 ;  propagator  i (nslash/2) nbar.p/(p^2 + i0) ;  (p-k)^2 -> -nbar.p n.k at LO
# expected (future-pointing line W[+inf, x] = Y_n^(out) dag):  one gluon g t^a n.eps/(n.k - i0);
#   two gluons, gluon 1 nearer the hard vertex: g^2 t^{a2} t^{a1} /((n.(k1+k2) - i0)(n.k2 - i0))
Pn = slash(NVEC) @ slash(NBVEC) / 4; Pnb = slash(NBVEC) @ slash(NVEC) / 4
ns, nbs = slash(NVEC), slash(NBVEC)
ok1 = True; ok2 = True
for trial in range(5):
    k3 = rng.normal(size=3) * 0.1 + np.array([0, 0, 5.0]); p = np.array([np.linalg.norm(k3), *k3])   # n-collinear
    nbp = mdot(NBVEC, p)
    u = u_spinor(p, trial % 2); ub = bar(u)
    k1, k2 = rng.normal(size=4) * 1e-3, rng.normal(size=4) * 1e-3     # usoft
    nk1, nk2 = mdot(NVEC, k1), mdot(NVEC, k2)
    Gam = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))    # arbitrary hard vertex (Dirac part)
    a1, a2 = 2, 5
    V = lambda a: 1j * g * np.kron(nbs / 2, T[a])           # n.eps = 1 stripped; Dirac x colour
    Sp = lambda nk: np.kron(1j * (ns / 2) * nbp / (-nbp * nk), np.eye(3))   # LO propagator, on-shell p
    ubC = np.kron(ub, np.eye(3))                             # colour left open (3x... matrix)
    GamC = np.kron(Gam, np.eye(3))
    # one gluon
    amp1 = ubC @ V(a1) @ Sp(nk1) @ GamC
    exp1 = ubC @ np.kron(Pnb, g * T[a1] / nk1) @ GamC        # ubar_n P_nbar = ubar_n (projector acts trivially)
    ok1 &= close(amp1, ubC @ np.kron(ID4, g * T[a1] / nk1) @ np.kron(Pnb, np.eye(3)) @ GamC, 1e-8)
    # two gluons: sum over the two orderings; gluon absorbed last is nearest to the final quark
    amp2 = (ubC @ V(a2) @ Sp(nk2) @ V(a1) @ Sp(nk1 + nk2) @ GamC
            + ubC @ V(a1) @ Sp(nk1) @ V(a2) @ Sp(nk1 + nk2) @ GamC)
    eik = g ** 2 * (T[a2] @ T[a1] / ((nk1 + nk2) * nk2) + T[a1] @ T[a2] / ((nk1 + nk2) * nk1))
    exp2 = ubC @ np.kron(Pnb, eik) @ GamC
    ok2 &= close(amp2, exp2, 1e-8)
ck('one usoft gluon ABSORBED (k into the line) by outgoing collinear quark: ubar_n [g t^a n.eps/(n.k - i0)]  (future-pointing Wilson line)', ok1)
ck('two usoft gluons: sum of orderings = g^2[t^b t^a/(n.(k1+k2) n.k2) + t^a t^b/(n.(k1+k2) n.k1)] = expansion of W[+inf,x]', ok2)
# B2': usoft gluon EMITTED (outgoing momentum k) by the outgoing collinear quark: line momentum p+k,
#   (p+k)^2 + i0 -> nbar.p (n.k + i0/nbar.p), nbar.p > 0  => expected  -g t^a n.eps*/(n.k + i0);
#   future-pointing rule with inflow K = -k:  (i g)(-i)/(n.K - i0) = -g/(n.k + i0)   (same thing)
ok3 = True
for trial in range(5):
    k3 = rng.normal(size=3) * 0.1 + np.array([0, 0, 5.0]); p = np.array([np.linalg.norm(k3), *k3])
    nbp = mdot(NBVEC, p); ub = bar(u_spinor(p, trial % 2)); ubC = np.kron(ub, np.eye(3))
    GamC = np.kron(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)), np.eye(3))
    ke = rng.normal(size=4) * 1e-3; nke = mdot(NVEC, ke)
    V = lambda a: 1j * g * np.kron(nbs / 2, T[a])
    Sp_e = np.kron(1j * (ns / 2) * nbp / (nbp * nke), np.eye(3))      # (p+k)^2 -> + nbar.p n.k
    ok3 &= close(ubC @ V(3) @ Sp_e @ GamC, ubC @ np.kron(Pnb, -g * T[3] / nke) @ GamC, 1e-8)
nks_ = sp.Symbol('nk', real=True); dl_ = sp.Symbol('delta', positive=True)
rule_emit = (sp.I) * (-sp.I) / (-nks_ - sp.I * dl_)          # (i)(-i)/(n.K - i delta), K = -k
ck("one usoft gluon EMITTED (outgoing k): ubar_n [-g t^a n.eps*/(n.k + i0)] = future-pointing rule with inflow -k",
   ok3 and sp.simplify(rule_emit + 1 / (nks_ + sp.I * dl_)) == 0)
# the same in terms of the blueprint rule (future-pointing line, gluons ordered from the vertex outward):
#   prod_j (i g n^mu)(-i)/(n.(k_j+...+k_m) - i0), colour t^{a_m}...t^{a_1}: identical (checked symbolically)
nk1s, nk2s = sp.symbols('nk1 nk2', positive=True)
rule = (sp.I * 1) * (-sp.I) / (nk1s + nk2s) * (sp.I) * (-sp.I) / nk2s
ck('blueprint future-pointing rule for (1 then 2) = 1/((n.k1+n.k2) n.k2)  (g^2 t^{a2} t^{a1} stripped)',
   sp.simplify(rule - 1 / ((nk1s + nk2s) * nk2s)) == 0)

# ------------------------------------------------------------------ C. tree-level matching QCD -> SCET: origin of W_n
# gamma*(q) -> q(p1) qbar(p2) g(k), p1, k n-collinear (along +z), p2 nbar-collinear.
def amps(lam, eps, color_stripped=True):
    Q = 10.0
    # n-collinear quark p1 and gluon k, nbar-collinear antiquark p2 (all massless, on-shell)
    def onshell(nbp, perp):
        np_ = (perp[0] ** 2 + perp[1] ** 2) / nbp
        return nbp * NVEC / 2 + np_ * NBVEC / 2 + np.array([0, perp[0], perp[1], 0])
    p1 = onshell(0.6 * Q, (0.7 * lam * Q, -0.2 * lam * Q))
    k = onshell(0.35 * Q, (-0.3 * lam * Q, 0.5 * lam * Q))
    # antiquark: (nbar.p2, n.p2, p2perp) ~ (lam^2, 1, lam) Q
    def onshell_nb(np_, perp):
        nbp = (perp[0] ** 2 + perp[1] ** 2) / np_
        return nbp * NVEC / 2 + np_ * NBVEC / 2 + np.array([0, perp[0], perp[1], 0])
    p2 = onshell_nb(0.9 * Q, (0.4 * lam * Q, 0.1 * lam * Q))
    u1 = u_spinor(p1, 0); v2 = v_spinor(p2, 1)
    ub1 = bar(u1)
    es = slash(eps)    # eps here is the (complex conjugated) polarization vector eps*
    mu = 1             # transverse current component gamma^1 (= gamma_perp^1)
    Gm = GAM[mu]
    S = lambda P: 1j * slash(P) / mdot(P, P)
    # QCD (colour t^a and coupling g stripped: vertex i gamma^nu)
    M_coll = ub1 @ (1j * es) @ S(p1 + k) @ Gm @ v2
    M_anti = ub1 @ Gm @ (1j * slash(-(p2 + k)) / mdot(p2 + k, p2 + k)) @ (1j * es) @ v2
    # SCET: collinear emission with LO vertex (BFPS) and xi propagator, plus W_n term g nbar.eps*/nbar.k
    P = p1 + k
    nbP, nP, Pperp = lc_components(P)
    nbp1, np1, p1perp = lc_components(p1)
    nbk = mdot(NBVEC, k)
    gp = lambda nu: GAM[nu] - NVEC[nu] * nbs / 2 - NBVEC[nu] * ns / 2
    epsl = lower(eps)
    Vc = sum(epsl[nu] * 1j * (NVEC[nu] * ID4 + gp(nu) @ slash(Pperp) / nbP + slash(p1perp) @ gp(nu) / nbp1
                               - slash(p1perp) @ slash(Pperp) * NBVEC[nu] / (nbP * nbp1)) @ nbs / 2 for nu in range(4))
    Sxi = 1j * ns / 2 * nbP / mdot(P, P)
    un1b = ub1 @ Pnb          # ubar_n = ubar P_nbar
    v2n = (slash(NVEC) @ slash(NBVEC) / 4 @ v2) * 0 + (slash(NBVEC) @ slash(NVEC) / 4) @ v2   # v_nbar = P_nbar-type projection
    S_coll = un1b @ Vc @ Sxi @ Gm @ v2n
    S_W = un1b @ Gm @ v2n * (mdot(NBVEC, eps) / nbk)
    M_W_expected = ub1 @ Gm @ v2 * (mdot(NBVEC, eps) / nbk)
    return M_coll, M_anti, S_coll, S_W, M_W_expected, k

# C1 Ward identity eps = k: QCD sum = 0 ; collinear part = -ubar gamma v ; W_n part = + ubar gamma v
for lam in (0.1, 0.01):
    _, _, _, _, _, kk = amps(lam, np.zeros(4))
    Mc, Ma, Sc, Sw, Mw, _ = amps(lam, kk.astype(complex))
    ck(f'Ward identity (eps* = k), lam={lam}: M_coll + M_anti = 0 in QCD', abs(Mc + Ma) < 1e-9 * max(1, abs(Mc)))
    ck(f'  SCET: collinear term + W_n term = 0  (W_n restores collinear gauge invariance), lam={lam}', abs(Sc + Sw) < 1e-9 * max(1, abs(Sc)),
       f'S_coll = {Sc:.4f}, S_W = {Sw:.4f}')
# C2 the antiquark-emission diagram (hard, off-shell ~ Q^2) -> W_n Feynman rule  g nbar.eps*/nbar.k, error O(lam)
eps_gen = np.array([0.3 + 0.1j, 1.0, 0.4j, -0.2]) + 0.7 * np.array([1, 0, 0, 1])   # generic incl. gauge-like part
errs = []
for lam in (1e-1, 1e-2, 1e-3):
    Mc, Ma, Sc, Sw, Mw, _ = amps(lam, eps_gen)
    errs.append(abs(Ma - Mw) / abs(Mw))
ck('hard antiquark-emission diagram -> ubar gamma v * g nbar.eps*/nbar.k  (W_n rule), rel. error O(lam)',
   errs[2] < 2e-2 and errs[1] / errs[2] > 5, f'rel errors {["%.1e" % e for e in errs]}')
# C3 full amplitude: QCD = SCET (collinear LO + W_n), relative error -> 0 linearly in lam
errs = []
for lam in (1e-1, 1e-2, 1e-3):
    Mc, Ma, Sc, Sw, Mw, _ = amps(lam, eps_gen)
    errs.append(abs((Mc + Ma) - (Sc + Sw)) / abs(Mc + Ma))
ck('full gamma* -> q qbar g (collinear gluon): QCD = SCET[xibar_n W_n gamma_perp W_nbar^dag xi_nbar] + O(lam)',
   errs[2] < 1e-2 and errs[1] / errs[2] > 5, f'rel errors {["%.1e" % e for e in errs]}')

# ------------------------------------------------------------------ D. SCET_II: soft gluon on a collinear quark -> S_n
errs = []
for lam in (1e-1, 1e-2, 1e-3):
    Q = 10.0
    nbp = 0.8 * Q; perp = np.array([0.5, -0.3]) * lam * Q
    p = nbp * NVEC / 2 + (perp @ perp / nbp) * NBVEC / 2 + np.array([0, perp[0], perp[1], 0])
    ksoft = np.array([1.0, 0.3, -0.6, 0.2]) * lam * Q          # soft (lam, lam, lam), off-shell ok
    eps = np.array([0.2, 0.5 + 0.3j, -0.1, 0.4])
    u = u_spinor(p, 0); ub = bar(u)
    Gam = GAM[2]
    exact = ub @ (1j * slash(eps)) @ (1j * slash(p + ksoft) / mdot(p + ksoft, p + ksoft)) @ Gam
    eik = ub @ Gam * (-mdot(NVEC, eps) / mdot(NVEC, ksoft))     # i*i*nbar.p n.eps/(nbar.p n.k) = - n.eps/n.k
    errs.append(np.max(np.abs(exact - eik)) / np.max(np.abs(eik)))
ck('SCET_II: soft gluon on collinear quark, (p+k)^2 ~ lam Q^2 -> eikonal n.eps/n.k (soft Wilson line S_n), rel. err O(lam)',
   errs[2] < 1e-2 and errs[1] / errs[2] > 5, f'rel errors {["%.1e" % e for e in errs]}')

ok = ck.summary()
sys.exit(0 if ok else 1)
