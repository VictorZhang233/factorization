"""
e27_wilson_vertices.py -- stage-2 verifier (batch E26_s2), claim E27 (Collins 2011 errata).

Independent checks (explicit SU(3) matrices, light-cone algebra), not relying on the errata text:
 (1) Collins' conventions: D = d + i g0 t A (his eq. (2.2)), quark-gluon vertex -i g t gamma (Fig. 3.1);
     our convention (Peskin-Schroeder) D = d - i g t A, vertex +i g t gamma  =>  g_Collins = -g.
     Gauge covariance then requires the Wilson line W = P exp(-i g0 int dz.A^a R_a) (R = rep. matrices);
     checked numerically for an abelian-free path-ordered product in a random background (finite-difference
     version of dW/ds = -i g A W and W -> U(b) W U(a)^dagger).
 (2) First-order Wilson-line vertex on the left of the cut: -i g0 n^mu (R_a)_{kj}; on the right of the cut
     (hermitian conjugate line, SAME index labels k, j as drawn in Fig. 7.10): +i g0 n^mu (R_a)_{kj}.
     Fundamental: -i g0 n (t_a)_kj | +i g0 n (t_a)_kj  (as printed and as in the errata).
     Adjoint with Collins' (T_a)_kj = i f_{k a j}:  g0 n f_{kaj} | -g0 n f_{kaj}  (errata; the printing has
     +g0 n f_{kaj} on the right).
 (3) Index placement in (11.4)-(11.6): H^mu g_{mu nu} C^nu = H_mu g^{mu nu} C_nu (the same scalar), but
     the statement "the largest term has mu_j = -, nu_j = +" holds for UPPER-index H^mu, C^nu (corrected
     version), not for lower-index H_mu, C_nu (printed version).  K_{mu nu} = k_mu w2_nu/(k.w2) has
     K_{-+} = 1, while the printed K^{mu nu} = k^mu w2^nu/(k.w2) has K^{-+} = 0.
 (4) i0: attaching a collinear gluon (momentum k into H) to the outgoing struck quark p_f = (0,p^-,0_T)
     gives 1/((p_f-k)^2 + i0) = -1/(2p^-) * 1/(k^+ - k^2/(2p^-) - i0): the eikonal denominator is
     k.w2 - i0 (w2 = (0,1,0_T), k.w2 = k^+), i.e. the -i0 of a future-pointing Wilson line with momentum
     flowing INTO the line (Collins (7.50): int_0^inf dy e^{iky} = i/(k + i0) for k flowing out).
Run: python3 -I e27_wilson_vertices.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

ok_all = []


def ok(name, cond):
    ok_all.append(bool(cond))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# ---------- SU(3) generators ----------
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = l / 2
# structure constants [t_a, t_b] = i f_abc t_c  ->  f_abc = -2 i tr([t_a,t_b] t_c)
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = t[a] @ t[b] - t[b] @ t[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j * np.trace(comm @ t[c]))
ok('f_abc totally antisymmetric', np.allclose(f, -np.transpose(f, (1, 0, 2))) and np.allclose(f, -np.transpose(f, (0, 2, 1))))
# Collins' adjoint generators (T_a)_{kj} = i f_{k a j}
T = np.array([[[1j * f[k, a, j] for j in range(8)] for k in range(8)] for a in range(8)])
ok('Collins (T_a)_kj = i f_kaj are hermitian', all(np.allclose(T[a], T[a].conj().T) for a in range(8)))
ok('(T_a)_kj = i f_kaj = -i f_akj (standard adjoint)', np.allclose(T, np.array([[[-1j * f[a, k, j] for j in range(8)] for k in range(8)] for a in range(8)])))
ok('[T_a,T_b] = i f_abc T_c', all(np.allclose(T[a] @ T[b] - T[b] @ T[a], sum(1j * f[a, b, c] * T[c] for c in range(8))) for a in range(8) for b in range(8)))

# ---------- (1) Wilson line sign for D = d + i g A ----------
rng = np.random.default_rng(3)
g = 0.7
N = 4000
s_grid = np.linspace(0, 1, N + 1)
coef = rng.normal(size=(8, 3))
def Apath(s):          # n.A^a(z(s)) along a path, smooth random
    return np.array([coef[a, 0] + coef[a, 1] * np.sin(3 * s) + coef[a, 2] * s ** 2 for a in range(8)])
def wline(Afun, R, sign):
    W = np.eye(R.shape[1], dtype=complex)
    for i in range(N):
        sm = 0.5 * (s_grid[i] + s_grid[i + 1]); ds = s_grid[i + 1] - s_grid[i]
        Am = np.tensordot(Afun(sm), R, axes=(0, 0))
        # exact exponential of a small step (later points to the LEFT)
        w, V = np.linalg.eigh(Am)
        W = (V @ np.diag(np.exp(sign * 1j * g * w * ds)) @ V.conj().T) @ W
    return W
# gauge transformation along the path: U(s) = exp(i g0 omega(s).t) as in Collins (2.4a) with sign: psi -> exp(-i g0 omega t) psi
om = rng.normal(size=(8, 2))
def omega(s):
    return np.array([om[a, 0] * np.cos(2 * s) + om[a, 1] * s for a in range(8)])
def Umat(s):
    M = np.tensordot(omega(s), t, axes=(0, 0)); w, V = np.linalg.eigh(M)
    return V @ np.diag(np.exp(-1j * g * w)) @ V.conj().T      # psi -> U psi, U = exp(-i g0 omega.t)
def A_transformed(s, h=1e-6):
    # Collins (2.4b): A.t -> (-i/g0) U D U^dagger with D = d + i g0 A.t, i.e. A' = U A U^dag + (-i/g) U dU^dag/ds ... along path
    U = Umat(s)
    dUd = (Umat(s + h).conj().T - Umat(s - h).conj().T) / (2 * h)
    At = np.tensordot(Apath(s), t, axes=(0, 0))
    Ap = U @ At @ U.conj().T + (-1j / g) * U @ dUd
    return np.array([2 * np.real(np.trace(Ap @ t[a])) for a in range(8)])
W_minus = wline(Apath, t, -1.0)        # P exp(-i g int A)
W_minus_tr = wline(A_transformed, t, -1.0)
cov_minus = np.max(np.abs(W_minus_tr - Umat(1.0) @ W_minus @ Umat(0.0).conj().T))
W_plus = wline(Apath, t, +1.0)
W_plus_tr = wline(A_transformed, t, +1.0)
cov_plus = np.max(np.abs(W_plus_tr - Umat(1.0) @ W_plus @ Umat(0.0).conj().T))
print('   covariance defect: P exp(-i g int A): %.2e ; P exp(+i g int A): %.2e' % (cov_minus, cov_plus))
ok('with D = d + i g A, the covariant Wilson line is P exp(-i g int dz.A) (W -> U(b) W U(a)^dag)', cov_minus < 1e-5 and cov_plus > 1e-2)

# ---------- (2) first-order vertices, left and right of the cut ----------
for name, R in [('quark (fundamental)', t), ('gluon (adjoint, Collins T)', T)]:
    nA = rng.normal(size=8)
    first_left = -1j * g * np.tensordot(nA, R, axes=(0, 0))               # O(g) part of W
    first_right = first_left.conj().T                                       # O(g) part of W^dagger
    pred_right = +1j * g * np.tensordot(nA, R, axes=(0, 0))
    ok('%s: right-of-cut vertex = +i g n (R_a)_kj with the same labels' % name, np.allclose(first_right, pred_right))
nA = rng.normal(size=8)
left_adj = -1j * g * np.tensordot(nA, T, axes=(0, 0))
right_adj = left_adj.conj().T
fk = np.tensordot(nA, np.transpose(f, (1, 0, 2)), axes=(0, 0))           # sum_a nA_a f_{k a j}
ok('adjoint: left vertex = +g0 n f_kaj', np.allclose(left_adj, g * fk))
ok('adjoint: right vertex = -g0 n f_kaj (errata), not +g0 n f_kaj (printing)', np.allclose(right_adj, -g * fk) and not np.allclose(right_adj, g * fk))

# ---------- (3) index placement in (11.4)-(11.6) ----------
# light-cone components (v^+, v^-, v^1, v^2); metric v.w = v+ w- + v- w+ - vT.wT
G_up = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=float)   # g_{mu nu} in LC basis
def lower(v):
    return G_up @ v
kplus, kT, kminus = 50.0, np.array([0.7, -0.4]), 0.01
k_up = np.array([kplus, kminus, *kT])
w2_up = np.array([0.0, 1.0, 0.0, 0.0])         # w2 = (0,1,0_T): w2.k = k^+
kw = k_up @ G_up @ w2_up
ok('k.w2 = k^+', np.isclose(kw, kplus))
K_low = np.outer(lower(k_up), lower(w2_up)) / kw     # corrected K_{mu nu}
K_up = np.outer(k_up, w2_up) / kw                    # printed  K^{mu nu}
Hu = rng.normal(size=4); Cu = rng.normal(size=4)
s_corr = Hu @ K_low @ Cu                             # H^mu K_{mu nu} C^nu
s_print = lower(Hu) @ K_up @ lower(Cu)               # H_mu K^{mu nu} C_nu
ok('printed and corrected K-contractions give the same scalar', np.isclose(s_corr, s_print))
ip, im = 0, 1
ok('corrected: K_{-+} = 1 (largest component at mu = -, nu = +)', np.isclose(K_low[im, ip], 1.0))
ok('printed:   K^{-+} = 0 (the sentence "mu=-, nu=+" does not fit upper-index K)', np.isclose(K_up[im, ip], 0.0))
# boosted collinear field C: C^+ large; hard vertex H: H^- large  -> leading term g_{-+} H^- C^+
lam = 0.01
C_up = np.array([1.0, lam ** 2, lam, lam]); H_up = np.array([lam ** 2, 1.0, lam, lam])
terms = {(m, n): H_up[m] * G_up[m, n] * C_up[n] for m in range(4) for n in range(4) if G_up[m, n] != 0}
lead = max(terms, key=lambda kk: abs(terms[kk]))
ok('largest term of H^mu g_{mu nu} C^nu is (mu,nu) = (-,+)  [upper-index H, C]', lead == (im, ip))
termsL = {(m, n): lower(H_up)[m] * np.linalg.inv(G_up)[m, n] * lower(C_up)[n] for m in range(4) for n in range(4) if G_up[m, n] != 0}
leadL = max(termsL, key=lambda kk: abs(termsL[kk]))
ok('in lower-index notation H_mu g^{mu nu} C_nu the largest term is (mu,nu) = (+,-)', leadL == (ip, im))

# ---------- (4) the -i0 ----------
kp, km, kt2, pm, eps0 = sp.symbols('k_p k_m k_T2 p_m epsilon0', positive=True)
den = -2 * pm * kp + (2 * kp * km - kt2) + sp.I * eps0        # (p_f - k)^2 + i0, p_f = (0,p^-,0)
eik = sp.simplify(den / (-2 * pm))
ok('(p_f-k)^2 + i0 = -2p^- (k^+ - k^2/(2p^-) - i0/(2p^-))', sp.simplify(eik - (kp - (2 * kp * km - kt2) / (2 * pm) - sp.I * eps0 / (2 * pm))) == 0)
y, kk = sp.symbols('y k', real=True)
I_out = sp.integrate(sp.exp(sp.I * (kk + sp.I * eps0) * y), (y, 0, sp.oo), conds='none')
ok('Collins (7.50): int_0^inf dy e^{i(k+i0)y} = i/(k+i0)', sp.simplify(I_out - sp.I / (kk + sp.I * eps0)) == 0)
I_in = I_out.subs(kk, -kk)
ok('momentum flowing INTO the future-pointing line: -i/(k - i0)', sp.simplify(I_in - (-sp.I) / (kk - sp.I * eps0)) == 0)

print('\nALL PASS' if all(ok_all) else '\nSOME CHECKS FAILED')
