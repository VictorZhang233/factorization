"""W02 / Ch2 check s2: gauge covariance, Bianchi, Chern-Simons current, Feynman rules derived from the
Lagrangian by plane waves, propagators.  Conventions: D = d - i g A, A = A^a t^a, G = dA - dA - i g [A,A].
Run: python3 -I s2_lagrangian.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = nfail = 0
def report(ok, name):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)

g = sp.Symbol('g')
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
tS = [s / 2 for s in sig]                      # SU(2) generators
fS = lambda a, b, c: sp.LeviCivita(a, b, c)    # SU(2): f^{abc} = epsilon^{abc}

# ---------------- (1) commutator [D_mu, D_nu] = -i g G_mu nu and finite gauge covariance (2D, SU(2)) -------------
x0, x1 = sp.symbols('x0 x1')
X = [x0, x1]
rng = np.random.default_rng(7)
def rpoly(deg=2):
    terms = [x0**i * x1**j for i in range(deg + 1) for j in range(deg + 1 - i)]
    return sum(sp.Rational(int(rng.integers(-3, 4)), int(rng.integers(1, 3))) * m for m in terms)
Acomp = [[rpoly() for a in range(3)] for mu in range(2)]          # A^a_mu(x0,x1)
A = [sum((Acomp[mu][a] * tS[a] for a in range(3)), sp.zeros(2)) for mu in range(2)]
def Gmat(A):
    return sp.diff(A[1], x0) - sp.diff(A[0], x1) - sp.I * g * (A[0] * A[1] - A[1] * A[0])
G01 = Gmat(A)
# component form G^a = dA^a - dA^a + g f^{abc} A^b A^c
Gc = [sp.diff(Acomp[1][a], x0) - sp.diff(Acomp[0][a], x1) + g * sum(fS(a, b, c) * Acomp[0][b] * Acomp[1][c] for b in range(3) for c in range(3)) for a in range(3)]
report(all(sp.simplify(sp.expand(G01 - sum((Gc[a] * tS[a] for a in range(3)), sp.zeros(2)))[i, j]) == 0 for i in range(2) for j in range(2)),
       'component form G^a = d A^a - d A^a + g f^abc A^b A^c  (SU(2), symbolic)')
# [D_0, D_1] psi = -i g G_01 psi for a test doublet psi(x)
psi = sp.Matrix([rpoly(), rpoly()])
D = lambda mu, v: sp.diff(v, X[mu]) - sp.I * g * A[mu] * v
lhs = D(0, D(1, psi)) - D(1, D(0, psi))
report(sp.simplify(sp.expand(lhs + sp.I * g * G01 * psi)) == sp.zeros(2, 1), '[D_mu,D_nu] psi = -i g G_mu nu psi  (symbolic)')
# finite gauge transformation with U = exp(i theta.sigma/2), theta(x) polynomial
th = [rpoly(1) for a in range(3)]
nrm = sp.sqrt(sum(t_**2 for t_ in th))
U = sp.cos(nrm / 2) * sp.eye(2) + sp.I * sp.sin(nrm / 2) * sum((th[a] / nrm * sig[a] for a in range(3)), sp.zeros(2))
Ui = sp.cos(nrm / 2) * sp.eye(2) - sp.I * sp.sin(nrm / 2) * sum((th[a] / nrm * sig[a] for a in range(3)), sp.zeros(2))
Ap = [U * A[mu] * Ui - sp.I / g * sp.diff(U, X[mu]) * Ui for mu in range(2)]
Gp = Gmat(Ap)
pt = {x0: sp.Rational(3, 7), x1: sp.Rational(-2, 5), g: sp.Rational(5, 4)}
diffm = (Gp - U * G01 * Ui).subs(pt).evalf(30)
report(max(abs(complex(v)) for v in diffm) < 1e-20, 'finite gauge covariance G -> U G U^{-1}  (SU(2), U = exp(i theta.sigma/2), at a point)')
Dp = lambda mu, v: sp.diff(v, X[mu]) - sp.I * g * Ap[mu] * v
dd = (Dp(0, U * psi) - U * D(0, psi)).subs(pt).evalf(30)
report(max(abs(complex(v)) for v in dd) < 1e-20, 'finite gauge covariance D psi -> U D psi')

# ---------------- (2) Bianchi identity and Chern-Simons current in 4D (SU(2), polynomial fields) -------------
xs = sp.symbols('y0:4')
def rpoly4(deg=1):
    mons = [sp.Integer(1)] + list(xs) + ([xs[i] * xs[j] for i in range(4) for j in range(i, 4)] if deg >= 2 else [])
    return sum(int(rng.integers(-2, 3)) * m for m in mons)
A4 = [[rpoly4(2) for a in range(3)] for mu in range(4)]
G4 = [[[sp.diff(A4[nu][a], xs[mu]) - sp.diff(A4[mu][a], xs[nu]) + g * sum(fS(a, b, c) * A4[mu][b] * A4[nu][c] for b in range(3) for c in range(3))
        for a in range(3)] for nu in range(4)] for mu in range(4)]
def DG(lam, mu, nu, a):   # adjoint covariant derivative of G
    return sp.diff(G4[mu][nu][a], xs[lam]) + g * sum(fS(a, b, c) * A4[lam][b] * G4[mu][nu][c] for b in range(3) for c in range(3))
ok = True
for (lam, mu, nu) in [(0, 1, 2), (1, 2, 3), (0, 2, 3)]:
    for a in range(3):
        ok &= sp.expand(DG(lam, mu, nu, a) + DG(mu, nu, lam, a) + DG(nu, lam, mu, a)) == 0
report(ok, 'Bianchi identity D_lam G_mu nu + cyclic = 0  (SU(2), symbolic)')
eps = lambda *i: sp.LeviCivita(*i)
GGt = sum(sp.Rational(1, 2) * eps(m, n, r, s) * G4[m][n][a] * G4[r][s][a]
          for m, n, r, s in itertools.permutations(range(4)) for a in range(3))
K = [2 * sum(eps(m, n, r, s) * (sum(A4[n][a] * sp.diff(A4[s][a], xs[r]) for a in range(3))
          + g / 3 * sum(fS(a, b, c) * A4[n][a] * A4[r][b] * A4[s][c] for a in range(3) for b in range(3) for c in range(3)))
          for n, r, s in itertools.permutations([i for i in range(4) if i != m])) for m in range(4)]
divK = sum(sp.diff(K[m], xs[m]) for m in range(4))
report(sp.expand(GGt - divK) == 0, 'G^a Gtilde^a = d_mu K^mu, K = 2 eps(A dA + g/3 f AAA)  (SU(2), symbolic)')

# ---------------- (3) Feynman rules from the Lagrangian by plane waves (SU(3) numerics) -------------
def su3():
    lam = np.zeros((8, 3, 3), complex)
    lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
    lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
    lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    t = lam / 2
    f = np.zeros((8, 8, 8))
    for a, b, c in itertools.product(range(8), repeat=3):
        f[a, b, c] = np.real(-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c]))
    return t, f
t3, f3 = su3()
eta = np.diag([1., -1, -1, -1])
gv = 0.9
# L_3 = -g f^{abc} (d_mu A^a_nu) A^{b mu} A^{c nu}; a field slot carrying incoming momentum k with polarization e and colour a:
#   A^a_nu(x) -> e_nu e^{-ikx}, d_mu -> -i k_mu.  Vertex = i * sum over assignments of the coefficient.
def V3_from_L(legs):
    # legs: list of (k (4,), e (4,), colour) ; returns i * sum over the 3! assignments
    tot = 0
    for perm in itertools.permutations(range(3)):
        (k1, e1, a1), (k2, e2, a2), (k3, e3, a3) = [legs[i] for i in perm]
        # slot1: (d_mu A^a_nu), slot2: A^{b mu}, slot3: A^{c nu}
        dmuA = -1j * np.outer(k1, e1)           # [mu, nu] lower indices: d_mu A_nu
        val = -gv * f3[a1, a2, a3] * np.einsum('mn,m,n->', dmuA, eta @ e2, eta @ e3)
        tot += val
    return 1j * tot
def V3_rule(legs):
    (k, e1, a), (p, e2, b), (q, e3, c) = legs
    up = lambda v: eta @ v
    val = gv * f3[a, b, c] * ((e1 @ eta @ e2) * ((k - p) @ eta @ e3) + (e2 @ eta @ e3) * ((p - q) @ eta @ e1) + (e3 @ eta @ e1) * ((q - k) @ eta @ e2))
    return val
ok = True
for trial in range(20):
    k = rng.normal(size=4); p = rng.normal(size=4); q = -k - p
    es = [rng.normal(size=4) for _ in range(3)]
    cols = rng.integers(0, 8, size=3)
    legs = [(k, es[0], cols[0]), (p, es[1], cols[1]), (q, es[2], cols[2])]
    ok &= np.isclose(V3_from_L(legs), V3_rule(legs))
report(ok, 'three-gluon vertex: i x (sum over 3! assignments of L_3) = g f^abc[g(k-p)+g(p-q)+g(q-k)], momenta incoming')
# four-gluon: L_4 = -(g^2/4) f^{eab} f^{ecd} A^a_mu A^b_nu A^{c mu} A^{d nu}
def V4_from_L(legs):
    tot = 0
    for perm in itertools.permutations(range(4)):
        (e1, a1), (e2, a2), (e3, a3), (e4, a4) = [legs[i] for i in perm]
        tot += -gv**2 / 4 * np.einsum('e,e->', f3[:, a1, a2], f3[:, a3, a4]) * (e1 @ eta @ e3) * (e2 @ eta @ e4)
    return 1j * tot
def V4_rule(legs):
    (e1, a), (e2, b), (e3, c), (e4, d) = legs
    G = lambda u, v: u @ eta @ v
    ff = lambda x, y, z, w: np.einsum('e,e->', f3[x, y, :], f3[z, w, :])
    return -1j * gv**2 * (ff(a, b, c, d) * (G(e1, e3) * G(e2, e4) - G(e1, e4) * G(e2, e3))
                          + ff(a, c, b, d) * (G(e1, e2) * G(e3, e4) - G(e1, e4) * G(e2, e3))
                          + ff(a, d, b, c) * (G(e1, e2) * G(e3, e4) - G(e1, e3) * G(e2, e4)))
ok = True
for trial in range(20):
    es = [rng.normal(size=4) for _ in range(4)]
    cols = rng.integers(0, 8, size=4)
    legs = list(zip(es, cols))
    ok &= np.isclose(V4_from_L(legs), V4_rule(legs))
report(ok, 'four-gluon vertex: i x (sum over 4! assignments of L_4) = -i g^2 [f f (gg-gg) + ...]')
# ghost vertex: L_gh = g f^{abc} (d^mu cbar^a) A^b_mu c^c ; outgoing ghost a with momentum p (cbar ~ e^{+ipx}: d -> +ip)
ok = True
for trial in range(10):
    p = rng.normal(size=4); e = rng.normal(size=4); a, b, c = rng.integers(0, 8, size=3)
    val = 1j * gv * f3[a, b, c] * ((1j * p) @ eta @ e)
    ok &= np.isclose(val, -gv * f3[a, b, c] * (p @ eta @ e))
report(ok, 'ghost-gluon vertex: i * g f^abc * (+i p.e) = -g f^abc p.e  (p = outgoing ghost momentum)')
# cubic and quartic terms of -1/4 G^a G^a (component check, symbolic, SU(2), constant 'fields')
Asym = [[sp.Symbol(f'A{a}_{m}') for m in range(4)] for a in range(3)]
dA = [[[sp.Symbol(f'dA{a}_{m}{n}') for n in range(4)] for m in range(4)] for a in range(3)]   # d_m A^a_n
gm = sp.diag(1, -1, -1, -1)
Gl = [[[dA[a][m][n] - dA[a][n][m] + g * sum(fS(a, b, c) * Asym[b][m] * Asym[c][n] for b in range(3) for c in range(3))
        for n in range(4)] for m in range(4)] for a in range(3)]
LYM = -sp.Rational(1, 4) * sum(Gl[a][m][n] * Gl[a][r][s] * gm[m, r] * gm[n, s] for a in range(3) for m in range(4) for n in range(4) for r in range(4) for s in range(4))
LYM = sp.expand(LYM)
L3 = -g * sum(fS(a, b, c) * dA[a][m][n] * Asym[b][r] * gm[r, m] * Asym[c][s] * gm[s, n]
              for a in range(3) for b in range(3) for c in range(3) for m in range(4) for n in range(4) for r in range(4) for s in range(4))
L4 = -g**2 / 4 * sum(fS(e, a, b) * fS(e, c, d) * Asym[a][m] * Asym[b][n] * Asym[c][r] * gm[r, m] * Asym[d][s] * gm[s, n]
                     for e in range(3) for a in range(3) for b in range(3) for c in range(3) for d in range(3)
                     for m in range(4) for n in range(4) for r in range(4) for s in range(4))
cub = sum(term for term in LYM.as_ordered_terms() if sp.Poly(term, g).degree() == 1)
qua = sum(term for term in LYM.as_ordered_terms() if sp.Poly(term, g).degree() == 2)
report(sp.expand(cub - L3) == 0 and sp.expand(qua - L4) == 0, '-1/4 G^a G^a: cubic term = L_3, quartic term = L_4 (SU(2), symbolic)')

# ---------------- (4) propagators -------------
k0, k1, k2, k3, xi = sp.symbols('k0 k1 k2 k3 xi')
kv = sp.Matrix([k0, k1, k2, k3]); kl = gm * kv; ksq = (kv.T * gm * kv)[0]
Mquad = -ksq * gm + (1 - 1 / xi) * kl * kl.T          # quadratic form (lower indices)
Dprop = sp.I * Mquad.inv()                              # upper indices
expected = -sp.I / ksq * (gm.inv() - (1 - xi) * kv * kv.T / ksq)
report(sp.simplify(Dprop - expected) == sp.zeros(4), 'gluon propagator: i [-k^2 g + (1-1/xi) k k]^{-1} = -i/k^2 [g - (1-xi) kk/k^2]')
M0 = -ksq * gm + kl * kl.T
report(sp.simplify(M0 * kv) == sp.zeros(4, 1), 'without gauge fixing the quadratic form -k^2 g + k k annihilates k (zero mode)')

print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
