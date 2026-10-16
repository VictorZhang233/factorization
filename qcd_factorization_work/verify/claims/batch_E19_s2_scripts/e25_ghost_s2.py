#!/usr/bin/env python3
"""E25 (stage 2): BPS 2002 eq. (24) [label Lcg], arXiv:hep-ph/0109045 v1 = v2:
   L = 1/(2g^2) tr{[iD+gA, iD+gA]}^2 + 2 tr{ cbar [iD_mu, [iD^mu + g A^mu, c]] } + 1/alpha tr{[iD_mu, A^mu]}^2
   text: "The first two terms in Eq. (24) are invariant under collinear gauge transformations".
Collinear transformation (BPS Table I): iD + gA -> U (iD + gA) U^dagger, iD (usoft/label background) fixed.
Method (independent of stage 1, which used random SU(2) jets in a continuum model):
 Part 1 - exact field-theory counterexample: SU(2), A = 0, A_us = 0, infinitesimal U = 1 + i omega;
          closed-form variations derived by hand (Jacobi identity) are checked against brute-force variation
          with symbolic functions, and the ACTION variation is evaluated EXACTLY on Gaussian test functions
          in 4D Minkowski space: non-zero for both ghost assignments (adjoint / inert).
 Part 2 - dimensionally reduced matrix model with the same commutator structure (iD_mu -> fixed matrices
          X_mu, trace cyclicity = integration by parts): FINITE collinear and usoft transformations, and BRST
          with an explicit Grassmann algebra (hand-written; ghosts c = th1 C1 + th2 C2, cbar = th3 Cb, lambda = th4).
Run: python3 -I e25_ghost_s2.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + info if info else ''))

# ===================================================================== Part 1: field theory, exact
X = sp.symbols('x0:4', real=True)
metric = [1, -1, -1, -1]
Tg = [sp.Matrix([[0, 1], [1, 0]])/2, sp.Matrix([[0, -sp.I], [sp.I, 0]])/2, sp.Matrix([[1, 0], [0, -1]])/2]
def adj(fs):  return sum((fs[a]*Tg[a] for a in range(3)), sp.zeros(2, 2))
def comm(A, B): return A*B - B*A
def d(M, mu): return M.applyfunc(lambda e: sp.diff(e, X[mu]))
def tr(M): return sp.expand(M.trace())
# generic symbolic component functions (for the brute-force vs closed-form identity)
cb = [sp.Function(f'cb{a}')(*X) for a in range(3)]
cc = [sp.Function(f'c{a}')(*X) for a in range(3)]
om = [sp.Function(f'w{a}')(*X) for a in range(3)]
CB, C, W = adj(cb), adj(cc), adj(om)
eps = sp.symbols('epsilon')
# A = 0, A_us = 0:  Pi^mu = i d^mu,  [i D_mu, Y] = i d_mu Y ; g delta A^mu = -i[Pi^mu, omega] = d^mu omega
def L_gh(Abar_list, Cfield, CBfield):       # 2 tr{ cbar [i d_mu, [i d^mu + g A^mu, c]] }, A given as g*A^mu list (upper index)
    tot = sp.zeros(2, 2)
    for mu in range(4):
        inner = sp.I*metric[mu]*d(Cfield, mu) + comm(Abar_list[mu], Cfield)       # [Pi^mu, c], Pi^mu = i d^mu + gA^mu
        tot += sp.I*d(inner, mu)                                                  # [i d_mu, inner]
    return 2*(CBfield*tot).trace()
gA_var = [eps*metric[mu]*d(W, mu) for mu in range(4)]       # g delta A^mu = d^mu omega (upper index)
zeroA = [sp.zeros(2, 2)]*4
# (i) adjoint ghosts: c -> c + i eps [omega, c], cbar -> cbar + i eps [omega, cbar]
Lp = L_gh(gA_var, C + sp.I*eps*comm(W, C), CB + sp.I*eps*comm(W, CB))
dL_adj = sp.expand(sp.diff(Lp, eps).subs(eps, 0))
closed_adj = sp.expand(sum((-2*sp.I*metric[mu]*(CB*comm(d(W, mu), d(C, mu))).trace() for mu in range(4))))
check('(1a) adjoint ghosts, A=0: delta L_gh = -2i tr{cbar [d_mu omega, d^mu c]} (brute force = closed form)',
      sp.simplify(dL_adj - closed_adj) == 0)
# (ii) inert ghosts
Lp2 = L_gh(gA_var, C, CB)
dL_inert = sp.expand(sp.diff(Lp2, eps).subs(eps, 0))
closed_inert = sp.expand(sum((2*(CB*sp.I*d(comm(d(W, mu)*metric[mu], C), mu)).trace() for mu in range(4))))
check('(1b) inert ghosts, A=0: delta L_gh = 2 tr{cbar [i d_mu, [d^mu omega, c]]} (brute force = closed form)',
      sp.simplify(dL_inert - closed_inert) == 0)
# exact action variation on Gaussian test functions (ghosts Grassmann: cbar^a = thb f^a, c^a = th h^a; the
# variation is bilinear, so delta S = thb th * (integral below)); Euclidean-norm Gaussians, Minkowski metric
r2 = sum(xx**2 for xx in X)
test = {cb[0]: 0, cb[1]: 0, cb[2]: sp.exp(-r2),
        om[0]: (1 + X[0])*sp.exp(-2*r2), om[1]: 0, om[2]: 0,
        cc[0]: 0, cc[1]: sp.exp(-3*r2)*(1 + X[1]), cc[2]: 0}
def integrate4(expr):
    expr = sp.expand(sp.simplify(expr.doit()))
    res = expr
    for xx in X:
        res = sp.integrate(res, (xx, -sp.oo, sp.oo))
    return sp.simplify(res)
dS_adj = integrate4(dL_adj.subs(test))
dS_inert = integrate4(dL_inert.subs(test))
print('   delta S (adjoint ghosts) =', dS_adj, '=', sp.N(dS_adj))
print('   delta S (inert ghosts)   =', dS_inert, '=', sp.N(dS_inert))
check('(1c) the ghost ACTION is not collinear-gauge invariant (adjoint ghosts): delta S != 0', dS_adj != 0)
check('(1d) ... nor with inert ghosts: delta S != 0', dS_inert != 0)
# abelian control: with commuting generators the variation vanishes identically
check('(1e) abelian control: [d omega, d c] = 0 for commuting fields, so the non-invariance is purely non-abelian',
      sp.simplify(closed_adj.subs({cb[0]: 0, cb[1]: 0, om[0]: 0, om[1]: 0, cc[0]: 0, cc[1]: 0})) == 0)

# ===================================================================== Part 2: reduced matrix model + Grassmann
rng = np.random.default_rng(2024)
N = 3
eta = np.diag([1., -1., -1., -1.])
def herm(): M = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)); return (M + M.conj().T)/2
def cm(A, B): return A @ B - B @ A
def U_of(H):                                   # U = exp(iH), H Hermitian (eigen-decomposition; no scipy needed)
    w, V = np.linalg.eigh(H); return V @ np.diag(np.exp(1j*w)) @ V.conj().T
g, alpha = 0.7, 1.3
Xs = [herm() for _ in range(4)]                 # background "i D_mu" (lower index); fixed under collinear transf.
As = [herm() for _ in range(4)]                 # collinear gluon A_mu (lower index)
up = lambda L: [eta[m, m]*L[m] for m in range(4)]
def LF(Xl, Al):
    Pi = [Xl[m] + g*Al[m] for m in range(4)]; Pu = up(Pi)
    return sum(np.trace(cm(Pi[m], Pi[n]) @ cm(Pu[m], Pu[n])) for m in range(4) for n in range(4))/(2*g**2)
def Gfix(Xl, Al):
    return sum(cm(Xl[m], up(Al)[m]) for m in range(4))
def Lgf(Xl, Al): G = Gfix(Xl, Al); return np.trace(G @ G)/alpha
def Lgh(Xl, Al, Cb, Cg):                        # bilinear in (cbar, c): ordinary matrices suffice for gauge variance
    Pu = up([Xl[m] + g*Al[m] for m in range(4)])
    return 2*np.trace(Cb @ sum(cm(Xl[m], cm(Pu[m], Cg)) for m in range(4)))
Cb0, Cg0 = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)), rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
U = U_of(0.8*herm()); Ud = U.conj().T
# collinear: Pi -> U Pi U^dag with X fixed  <=>  A -> (U (X + gA) U^dag - X)/g
Acol = [(U @ (Xs[m] + g*As[m]) @ Ud - Xs[m])/g for m in range(4)]
base = dict(F=LF(Xs, As), gf=Lgf(Xs, As), gh=Lgh(Xs, As, Cb0, Cg0))
rel = lambda a, b: abs(a - b)/max(abs(b), 1e-300)
check('(2a) matrix model, finite collinear transf.: field-strength term invariant', rel(LF(Xs, Acol), base['F']) < 1e-10)
check('(2b) ... ghost term NOT invariant (ghosts adjoint: c -> U c U^dag, cbar -> U cbar U^dag)',
      rel(Lgh(Xs, Acol, U @ Cb0 @ Ud, U @ Cg0 @ Ud), base['gh']) > 1e-3,
      f'rel. change {rel(Lgh(Xs, Acol, U @ Cb0 @ Ud, U @ Cg0 @ Ud), base["gh"]):.2f}')
check('(2c) ... ghost term NOT invariant (ghosts inert)', rel(Lgh(Xs, Acol, Cb0, Cg0), base['gh']) > 1e-3,
      f'rel. change {rel(Lgh(Xs, Acol, Cb0, Cg0), base["gh"]):.2f}')
check('(2d) ... gauge-fixing term NOT invariant (as expected)', rel(Lgf(Xs, Acol), base['gf']) > 1e-3)
# usoft: everything conjugated, including the background X
V = U_of(0.6*herm()); Vd = V.conj().T
Xu = [V @ Xs[m] @ Vd for m in range(4)]; Au = [V @ As[m] @ Vd for m in range(4)]
check('(2e) usoft (background) transf. with c, cbar -> V(.)V^dag: all three terms invariant',
      rel(LF(Xu, Au), base['F']) < 1e-10 and rel(Lgf(Xu, Au), base['gf']) < 1e-10 and
      rel(Lgh(Xu, Au, V @ Cb0 @ Vd, V @ Cg0 @ Vd), base['gh']) < 1e-10)

# (2f) Faddeev-Popov operator M(A): c -> [X_mu, [Pi^mu, c]] as an N^2 x N^2 matrix; if |det M| changes under the
# collinear transformation, NO ghost transformation with unit Jacobian (c -> R c, cbar -> cbar R', |det R det R'| = 1,
# e.g. any adjoint/unitary or inert assignment) can make the ghost term invariant.
def FP_matrix(Xl, Al):
    Pu = up([Xl[m] + g*Al[m] for m in range(4)])
    cols = []
    for k in range(N*N):
        E = np.zeros(N*N, complex); E[k] = 1; Cm = E.reshape(N, N)
        cols.append(sum(cm(Xl[m], cm(Pu[m], Cm)) for m in range(4)).reshape(-1))
    return np.array(cols).T
# restrict to the traceless (su(N)) part to remove the trivial zero mode c ~ 1
basis = []
for i in range(N):
    for j in range(N):
        if i != j:
            B = np.zeros((N, N), complex); B[i, j] = 1; basis.append(B)
for i in range(N - 1):
    B = np.zeros((N, N), complex); B[i, i] = 1; B[i + 1, i + 1] = -1; basis.append(B)
Bm = np.array([b.reshape(-1) for b in basis]).T                     # N^2 x (N^2-1)
Bp = np.linalg.pinv(Bm)
def detFP(Xl, Al): return np.linalg.det(Bp @ FP_matrix(Xl, Al) @ Bm)
d0, d1 = detFP(Xs, As), detFP(Xs, Acol)
dU = detFP(Xu, Au)
print(f'   |det M| before = {abs(d0):.6g}, after collinear transf. = {abs(d1):.6g}, after usoft transf. = {abs(dU):.6g}')
check('(2f) |det M_FP| changes under the collinear transformation (no unit-Jacobian ghost assignment can rescue invariance)',
      abs(abs(d1)/abs(d0) - 1) > 1e-3)
check('(2g) |det M_FP| is invariant under the usoft (background) transformation', abs(abs(dU)/abs(d0) - 1) < 1e-9)

# ---------------- Grassmann algebra: element = {sorted tuple of generator indices: complex N x N matrix}
class Gr:
    def __init__(self, d=None): self.d = {k: v for k, v in (d or {}).items()}
    @staticmethod
    def bos(M): return Gr({(): np.array(M, complex)})
    def __add__(self, o):
        r = dict(self.d)
        for k, v in o.d.items(): r[k] = r.get(k, 0) + v
        return Gr(r)
    def __sub__(self, o): return self + o.scale(-1)
    def scale(self, z): return Gr({k: z*v for k, v in self.d.items()})
    def __matmul__(self, o):
        r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                if set(k1) & set(k2): continue
                seq = list(k1 + k2); sign = 1
                for i in range(len(seq)):                      # bubble sort, count transpositions
                    for j in range(len(seq) - 1 - i):
                        if seq[j] > seq[j + 1]: seq[j], seq[j + 1] = seq[j + 1], seq[j]; sign = -sign
                key = tuple(seq); r[key] = r.get(key, 0) + sign*(v1 @ v2)
        return Gr(r)
    def tr(self): return {k: complex(np.trace(v)) for k, v in self.d.items()}
    def coeff(self, key): return self.d.get(key, np.zeros((N, N), complex))
def gcm(A, B): return A @ B - B @ A
def theta(i): return Gr({(i,): np.eye(N, dtype=complex)})
def odd(i, M): return Gr({(i,): np.array(M, complex)})
C1, C2, Cbm = (rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)) for _ in range(3))
c = odd(1, C1) + odd(2, C2)                     # Grassmann-odd ghost with c c != 0
cbar = odd(3, Cbm)
lam = theta(4); lam2 = theta(5)
Xg = [Gr.bos(M) for M in Xs]; Ag = [Gr.bos(M) for M in As]
def upg(L): return [L[m].scale(eta[m, m]) for m in range(4)]
def LF_g(Al):
    Pi = [Xg[m] + Al[m].scale(g) for m in range(4)]; Pu = upg(Pi); tot = Gr()
    for m in range(4):
        for n in range(4): tot = tot + gcm(Pi[m], Pi[n]) @ gcm(Pu[m], Pu[n])
    return tot.scale(1/(2*g**2))
def G_g(Al): return sum((gcm(Xg[m], upg(Al)[m]) for m in range(4)), Gr())
def Lgf_g(Al): G = G_g(Al); return (G @ G).scale(1/alpha)
def Lgh_g(Al, cb_, c_):
    Pu = upg([Xg[m] + Al[m].scale(g) for m in range(4)])
    return (cb_ @ sum((gcm(Xg[m], gcm(Pu[m], c_)) for m in range(4)), Gr())).scale(2)
def trace_part(gr, key): return gr.tr().get(key, 0)
def brst(Al, c_, cb_, lam_, kc, kb):
    """delta_lam fields: A_mu -> A_mu - (i/g) lam [Pi_mu, c];  c -> c + kc lam c c;  cbar -> cbar + kb lam G"""
    Pi = [Xg[m] + Al[m].scale(g) for m in range(4)]
    dA = [(lam_ @ gcm(Pi[m], c_)).scale(-1j/g) for m in range(4)]
    dc = (lam_ @ c_ @ c_).scale(kc)
    dcb = (lam_ @ G_g(Al)).scale(kb)
    return dA, dc, dcb
# nilpotency on A and c fixes kc
def second_variation(kc):
    dA1, dc1, _ = brst(Ag, c, cbar, lam, kc, 0)
    A1 = [Ag[m] + dA1[m] for m in range(4)]; c1 = c + dc1
    dA2, dc2, _ = brst(A1, c1, cbar, lam2, kc, 0)       # vary again with an independent parameter
    dA2_0, dc2_0, _ = brst(Ag, c, cbar, lam2, kc, 0)
    # part bilinear in (lam, lam2): d2 = delta_2(delta_1 X)
    key_res_A = max(max(np.abs(v).max() for k, v in (dA2[m] - dA2_0[m]).d.items() if 4 in k and 5 in k) if any(4 in k and 5 in k for k in (dA2[m] - dA2_0[m]).d) else 0 for m in range(4))
    dd = dc2 - dc2_0
    key_res_c = max((np.abs(v).max() for k, v in dd.d.items() if 4 in k and 5 in k), default=0)
    return key_res_A, key_res_c
for kc in (1j, -1j):
    ra, rc = second_variation(kc)
    print(f'   kc = {kc}: |s^2 A| = {ra:.2e}, |s^2 c| = {rc:.2e}')
raP, rcP = second_variation(1j); raM, rcM = second_variation(-1j)
check('(3a) BRST nilpotency on A and c holds for s c = i c c (in this normalization), fails for s c = -i c c',
      raP < 1e-10 and rcP < 1e-10 and raM > 1e-3)
kc = 1j
def var_of(Lfun, kb):
    dA, dc, dcb = brst(Ag, c, cbar, lam, kc, kb)
    A1 = [Ag[m] + dA[m] for m in range(4)]
    L0 = Lfun(Ag, c, cbar); L1 = Lfun(A1, c + dc, cbar + dcb)
    D = L1 - L0
    return max((abs(v) for k, v in D.tr().items() if 4 in k), default=0.0)
LFw = lambda A, c_, cb_: LF_g(A); Lgfw = lambda A, c_, cb_: Lgf_g(A); Lghw = lambda A, c_, cb_: Lgh_g(A, cb_, c_)
sumw = lambda A, c_, cb_: Lgf_g(A) + Lgh_g(A, cb_, c_)
# fix kb by requiring s(Lgf + Lgh) = 0: scan the natural candidates +-1/(alpha g), +-i/(alpha g)
cands = [s_*z/(alpha*g) for s_ in (1, -1) for z in (1, 1j)]
res = {kb: var_of(sumw, kb) for kb in cands}
for kb, r in res.items(): print(f'   s cbar = {kb:.4f} G : |s(L_gf + L_gh)| = {r:.3e}')
kb = min(res, key=res.get)
check('(3b) BRST: s L_F = 0', var_of(LFw, kb) < 1e-9, f'{var_of(LFw, kb):.1e}')
check('(3c) BRST: s(L_gf + L_gh) = 0 for s cbar = kb G with a unique kb among the candidates',
      res[kb] < 1e-9 and sorted(res.values())[1] > 1e-3, f'kb = {kb:.4f}')
check('(3d) BRST: s L_gf != 0 and s L_gh != 0 separately (only the SUM is invariant)',
      var_of(Lgfw, kb) > 1e-3 and var_of(Lghw, kb) > 1e-3, f'{var_of(Lgfw, kb):.3g}, {var_of(Lghw, kb):.3g}')
print(f'\nSUMMARY: {sum(PASS)}/{len(PASS)} PASS')
