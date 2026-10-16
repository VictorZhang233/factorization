# -*- coding: utf-8 -*-
"""
w18_s3_gauge_brst.py -- Ch15 prop:scet-gauge (incl. the corrected statement of App Q item 3) and the algebra behind
thm:scet-decoupling (gluon/ghost part).  Finite-dimensional operator model:
  space = 2D periodic lattice (N x N sites) (x) colour C^3;  i Dcal^mu (background, usoft) = i d_lat^mu + g a_bg^mu;
  collinear gauge field A^mu and ghosts c, cbar as operators;  i D_full^mu = i Dcal^mu + g A^mu.
Checks:
  (a) field-strength term (1/2g^2) Tr [iD_full^1, iD_full^2]^2 invariant under collinear U (iD_full -> U iD_full U^dag);
  (b) gauge-fixing term Tr [iDcal_mu, A^mu]^2 NOT collinear invariant; (c) ghost term Tr cbar [iDcal_mu,[iD_full^mu, c]]
      NOT collinear invariant, for adjoint ghosts (c -> U c U^dag) and for inert ghosts;
  (d) every term invariant under usoft (background) transformations V (iDcal -> V iDcal V^dag, A, c, cbar conjugated);
  (e) Faddeev-Popov structure: delta_theta G = -(eps/g)[iDcal_mu,[iD_full^mu, theta]] for G = -i[iDcal_mu, A^mu];
  (f) nilpotency identity {s(iD_full), c} + [iD_full, s c] = 0 with s(iD_full) = -i g [iD_full, c], s c = i g c c,
      c Grassmann odd (two-generator Grassmann algebra with matrix coefficients);
  (g) normalizations in the free limit (symbolic): -1/4 G^a G^a, -1/(2 alpha)(d.A^a)^2, -cbar^a d^2 c^a.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import *
import sympy as sp

ck = Check('W18 s3: gauge symmetries of the LO collinear gluon Lagrangian, BRST structure, normalizations')
rng = np.random.default_rng(301)
N = 4; nc = 3; dim = N * N * nc
g = 0.9


def site_index(i, j):
    return (i % N) * N + (j % N)


def shift_op(direction):
    """(T f)(x) = f(x + e_direction) on the periodic N x N lattice, tensored with colour identity."""
    T = np.zeros((N * N, N * N))
    for i in range(N):
        for j in range(N):
            a = site_index(i, j)
            b = site_index(i + (direction == 0), j + (direction == 1))
            T[a, b] = 1.0
    return np.kron(T, np.eye(nc))


def local_op(mats):
    """block-diagonal operator from site-local colour matrices mats[site]."""
    M = np.zeros((dim, dim), dtype=complex)
    for a in range(N * N):
        M[a * nc:(a + 1) * nc, a * nc:(a + 1) * nc] = mats[a]
    return M


# i d_lat: hermitian symmetric difference (i/2)(T - T^dag)
iD_lat = [1j * 0.5 * (shift_op(d) - shift_op(d).T) for d in (0, 1)]
abg = [local_op([rand_su3_alg(rng, 0.5) for _ in range(N * N)]) for _ in range(2)]
iDcal = [iD_lat[m] + g * abg[m] for m in range(2)]          # background (usoft) covariant derivative
A = [local_op([rand_su3_alg(rng, 0.7) for _ in range(N * N)]) for _ in range(2)]
c = local_op([rand_su3_alg(rng) for _ in range(N * N)])      # bosonic stand-ins (the terms are linear in c and cbar)
cb = local_op([rand_su3_alg(rng) for _ in range(N * N)])
Tr = lambda M: np.trace(M)
com = lambda X, Y: X @ Y - Y @ X


def terms(iDc, A_, c_, cb_):
    iDf = [iDc[m] + g * A_[m] for m in range(2)]
    F = com(iDf[0], iDf[1])
    L_F = Tr(F @ F) / (2 * g * g)
    Gm = sum(com(iDc[m], A_[m]) for m in range(2))           # [iDcal_mu, A^mu] (Euclidean contraction suffices here)
    L_gf = Tr(Gm @ Gm)
    L_gh = 2 * Tr(cb_ @ sum(com(iDc[m], com(iDf[m], c_)) for m in range(2)))
    return L_F, L_gf, L_gh


L0 = terms(iDcal, A, c, cb)
# collinear transformation U (site-local SU(3)): iD_full -> U iD_full U^dag  <=>  A -> U A U^dag + (1/g) U [iDcal, U^dag]
def rand_SU3_local(r, scale):
    mats = []
    for _ in range(N * N):
        H = rand_su3_alg(r, scale); w, V = np.linalg.eigh(H)
        mats.append(V @ np.diag(np.exp(1j * w)) @ V.conj().T)
    return local_op(mats)
U = rand_SU3_local(rng, 1.0); Ud = U.conj().T
A_U = [U @ A[m] @ Ud + (1 / g) * U @ com(iDcal[m], Ud) for m in range(2)]
iDf_U = [iDcal[m] + g * A_U[m] for m in range(2)]
ck('check of the transformation law: iD_full -> U iD_full U^dag for A -> U A U^dag + (1/g) U[iDcal, U^dag]',
   all(np.allclose(iDf_U[m], U @ (iDcal[m] + g * A[m]) @ Ud) for m in range(2)))
L_adj = terms(iDcal, A_U, U @ c @ Ud, U @ cb @ Ud)          # adjoint ghosts
L_inert = terms(iDcal, A_U, c, cb)                          # inert ghosts
rel = lambda a, b: abs(a - b) / max(abs(a), abs(b))
ck('(a) field-strength term invariant under collinear gauge transformations', rel(L_adj[0], L0[0]) < 1e-12, '%.1e' % rel(L_adj[0], L0[0]))
ck('(b) gauge-fixing term NOT invariant under collinear gauge transformations', rel(L_adj[1], L0[1]) > 1e-3, '%.2e' % rel(L_adj[1], L0[1]))
ck('(c) ghost term NOT invariant under collinear transformations: adjoint ghosts / inert ghosts',
   rel(L_adj[2], L0[2]) > 1e-3 and rel(L_inert[2], L0[2]) > 1e-3, '%.2e / %.2e' % (rel(L_adj[2], L0[2]), rel(L_inert[2], L0[2])))
# usoft (background) transformation V: everything conjugated, background transforms as a background field
V = rand_SU3_local(rng, 1.0); Vd = V.conj().T
iDcal_V = [V @ iDcal[m] @ Vd for m in range(2)]
L_V = terms(iDcal_V, [V @ A[m] @ Vd for m in range(2)], V @ c @ Vd, V @ cb @ Vd)
ck('(d) field-strength, gauge-fixing and ghost terms each invariant under usoft transformations (A_us as background)',
   all(rel(L_V[i], L0[i]) < 1e-12 for i in range(3)), ['%.1e' % rel(L_V[i], L0[i]) for i in range(3)])
# usoft transformation = background gauge transformation of a_bg: check iDcal_V = i d + g a_bg' with a_bg' = V a V^dag + (1/g) V[i d, V^dag]
abg_V = [V @ abg[m] @ Vd + (1 / g) * V @ com(iD_lat[m], Vd) for m in range(2)]
ck('    (usoft law A_us -> V A_us V^dag + (1/g) V[i d, V^dag]  <=>  iDcal -> V iDcal V^dag)',
   all(np.allclose(iDcal_V[m], iD_lat[m] + g * abg_V[m]) for m in range(2)))
# (e) Faddeev-Popov: G(A) = -i [iDcal_mu, A^mu];  delta G under U = exp(i eps theta)
theta = local_op([rand_su3_alg(rng) for _ in range(N * N)])
epsl = 1e-6
w, Vt = np.linalg.eigh(theta)
Ue = Vt @ np.diag(np.exp(1j * epsl * w)) @ Vt.conj().T; Ued = Ue.conj().T
A_e = [Ue @ A[m] @ Ued + (1 / g) * Ue @ com(iDcal[m], Ued) for m in range(2)]
Gf = lambda A_: -1j * sum(com(iDcal[m], A_[m]) for m in range(2))
dG = (Gf(A_e) - Gf(A)) / epsl
pred = -(1 / g) * sum(com(iDcal[m], com(iDcal[m] + g * A[m], theta)) for m in range(2))
ck('(e) delta_theta G = -(eps/g) [iDcal_mu, [iD_full^mu, theta]]: the FP operator of the background gauge (=> ghost term = -2Tr cbar sG)',
   np.allclose(dG, pred, atol=1e-5), '%.1e' % np.max(np.abs(dG - pred)))

# (f) Grassmann algebra with two generators th1, th2; elements stored as dict {(): M, (1,): M, (2,): M, (1,2): M}
def gmul(X, Y):
    out = {}
    for kx, Mx in X.items():
        for ky, My in Y.items():
            if set(kx) & set(ky):
                continue
            seq = list(kx) + list(ky)
            # sign of sorting the generator sequence
            sgn = 1; s_ = seq[:]
            for i in range(len(s_)):
                for j in range(len(s_) - 1 - i):
                    if s_[j] > s_[j + 1]:
                        s_[j], s_[j + 1] = s_[j + 1], s_[j]; sgn = -sgn
            key = tuple(s_)
            out[key] = out.get(key, 0) + sgn * (Mx @ My)
    return out

def gadd(*Xs):
    out = {}
    for X in Xs:
        for k, M in X.items():
            out[k] = out.get(k, 0) + M
    return out

def gscale(a, X):
    return {k: a * M for k, M in X.items()}

def gnorm(X):
    return max([np.max(np.abs(M)) for M in X.values()] + [0.0])

C1 = local_op([rand_su3_alg(rng) for _ in range(N * N)]); C2 = local_op([rand_su3_alg(rng) for _ in range(N * N)])
cG = {(1,): C1, (2,): C2}                       # c = th1 C1 + th2 C2  (Grassmann odd)
iDf0 = {(): iDcal[0] + g * A[0]}                # one component suffices (the identity holds component by component)
sA_full = gscale(-1j * g, gadd(gmul(iDf0, cG), gscale(-1, gmul(cG, iDf0))))      # s(iD_full) = -i g [iD_full, c]   (odd)
sc = gscale(1j * g, gmul(cG, cG))                                                 # s c = i g c c                  (even)
anticomm = gadd(gmul(sA_full, cG), gmul(cG, sA_full))                             # {s(iD), c}
comm = gadd(gmul(iDf0, sc), gscale(-1, gmul(sc, iDf0)))                           # [iD, s c]
ck('(f) s^2 A = 0:  {s(iD_full), c} + [iD_full, s c] = 0 with s(iD_full) = -ig[iD_full, c], s c = ig cc (c Grassmann odd)',
   gnorm(gadd(anticomm, comm)) < 1e-12, '%.1e' % gnorm(gadd(anticomm, comm)))
ck('    (and the opposite sign of s c fails)', gnorm(gadd(anticomm, gscale(-1, comm))) > 1e-3)

# (g) normalizations in the free limit (abelian-like single colour component, plane-wave symbols)
gs, al = sp.symbols('g alpha', positive=True)
# [iD_mu, iD_nu] = i g G_{mu nu}  =>  (1/2g^2) Tr{(igG)^2} = -(1/2) Tr(GG) = -(1/4) G^a G^a  (Tr t^a t^b = delta/2)
Ga = sp.symbols('G_a')
ck('(g) field-strength term: (1/2g^2) Tr{[iD,iD]^2} = -(1/4) G^a G^a',
   sp.simplify((1 / (2 * gs ** 2)) * (sp.I * gs * Ga) ** 2 * sp.Rational(1, 2) + Ga ** 2 / 4) == 0)
dA = sp.symbols('dA')            # (d.A)^a for one colour component
ck('    gauge fixing: (1/alpha) Tr{[i d_mu, A^mu]^2} = (1/alpha)(i dA)^2/2 = -(1/(2 alpha)) (d.A^a)^2',
   sp.simplify((1 / al) * (sp.I * dA) ** 2 * sp.Rational(1, 2) + dA ** 2 / (2 * al)) == 0)
d2c, cbs = sp.symbols('d2c cbar')
ck('    ghost: 2 Tr{cbar [i d_mu,[i d^mu, c]]} = 2 * (1/2) cbar^a (i*i d^2 c^a) = -cbar^a d^2 c^a',
   sp.simplify(2 * sp.Rational(1, 2) * cbs * (sp.I * sp.I * d2c) + cbs * d2c) == 0)

# (h) matrix form <-> component form of the BRST transformations of def:prelim-brst (our convention D = d - igA)
fabc = np.zeros((8, 8, 8))
for a_ in range(8):
    for b_ in range(8):
        for c_ in range(8):
            fabc[a_, b_, c_] = np.real(-2j * np.trace(com(TGEN[a_], TGEN[b_]) @ TGEN[c_]))
# s c = i g c c  with c = th1 C1 + th2 C2, C_i = c_i^a t^a:  coefficient of th1 th2 is i g [C1, C2]
c1 = rng.normal(size=8); c2 = rng.normal(size=8)
Cm1 = np.einsum('a,aij->ij', c1, TGEN); Cm2 = np.einsum('a,aij->ij', c2, TGEN)
lhs = 1j * g * com(Cm1, Cm2)
# component form -(g/2) f^{abc} c^b c^c  with c^b c^c -> (th1 c1^b + th2 c2^b)(th1 c1^c + th2 c2^c) = th1th2 (c1^b c2^c - c2^b c1^c)
comp = -(g / 2) * np.einsum('abc,b,c->a', fabc, c1, c2) * 2   # antisymmetric f: (c1^b c2^c - c2^b c1^c) f^{abc} = 2 f^{abc} c1^b c2^c
rhs = np.einsum('a,aij->ij', comp, TGEN)
ck('(h) s c = i g c c  <=>  s c^a = -(g/2) f^{abc} c^b c^c  (def:prelim-brst)', np.allclose(lhs, rhs))
# s A = -i [iD, c] = D c with (D c)^a = d c^a + g f^{abc} A^b c^c : the field-dependent part -i[g A, c]
Av = rng.normal(size=8); cv = rng.normal(size=8)
Am = np.einsum('a,aij->ij', Av, TGEN); cm = np.einsum('a,aij->ij', cv, TGEN)
lhs = -1j * com(g * Am, cm)
rhs = np.einsum('a,aij->ij', g * np.einsum('abc,b,c->a', fabc, Av, cv), TGEN)
ck('    s A_mu = -i[iD_mu, c] = (D_mu c)^a t^a with (D c)^a = d c^a + g f^{abc} A^b c^c', np.allclose(lhs, rhs))

ok = ck.summary()
sys.exit(0 if ok else 1)
