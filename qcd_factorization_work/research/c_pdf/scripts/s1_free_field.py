"""
s1_free_field.py -- item (1): free-field normalisation of the operator definitions.

Conventions (CONTEXT.md): metric (+,-,-,-); v^pm = (v^0 pm v^3)/sqrt2;
D_mu = d_mu - i g A_mu^a t^a; W[b,a] = P exp(i g int_a^b dz.A), later points (closer to b) to the left.

f_q(xi)  = int dw^-/(4 pi) e^{-i xi P^+ w^-} <P| psibar(w) gamma^+ W[w,0] psi(0) |P>
f_g(xi)  = sum_j int dw^-/(2 pi xi P^+) e^{-i xi P^+ w^-} <P| G^{+j}_a(w) W^{adj}_{ab}[w,0] G^{+j}_b(0) |P>
f_qbar(xi) = - f_q(-xi)

Checks
 (a) spinor bilinears ubar gamma^+ u = vbar gamma^+ v = 2 p^+  (each helicity)
 (b) f_{q/q}^{(0)} = delta(1-xi), f_{q/qbar}^{(0)} = -delta(1+xi) => f_{qbar/qbar}^{(0)} = delta(1-xi)
 (c) charge-conjugate field psi^c = C psibar^T reproduces f_{qbar/qbar} = delta(1-xi) directly
 (d) gluon: <0|G^{a,+j}(0)|k,lambda,b> = -i k^+ eps^j delta^{ab}; f_{g/g}^{(0)} = delta(1-xi) - delta(1+xi)
 (e) Wilson line: discretised SU(2) path-ordered exponential converges to U(b) W U(a)^dagger under a gauge
     transformation with D = d - i g A (orientation W[b,a]); and dW[z,a]/dz = i g A(z) W[z,a].
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

results = []


def report(name, ok, detail=''):
    results.append((name, ok))
    print('%-72s %s %s' % (name, 'PASS' if ok else 'FAIL', detail))


# ---------------------------------------------------------------- Dirac matrices (Dirac representation)
I2 = sp.eye(2)
Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


g0 = blk(I2, Z2, Z2, -I2)
gs = [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
gam = [g0] + gs
metric = sp.diag(1, -1, -1, -1)
# Clifford algebra check
ok = all(sp.simplify(gam[m] * gam[n] + gam[n] * gam[m] - 2 * metric[m, n] * sp.eye(4)) == sp.zeros(4)
         for m in range(4) for n in range(4))
report('Clifford algebra {g^m,g^n}=2g^{mn}', ok)
s2 = sp.sqrt(2)
gplus = (gam[0] + gam[3]) / s2
gminus = (gam[0] - gam[3]) / s2
report('(gamma^+)^2 = 0, {gamma^+,gamma^-} = 2', sp.simplify(gplus * gplus) == sp.zeros(4)
       and sp.simplify(gplus * gminus + gminus * gplus - 2 * sp.eye(4)) == sp.zeros(4))


def slash(v):  # v contravariant Cartesian components
    return v[0] * gam[0] - v[1] * gam[1] - v[2] * gam[2] - v[3] * gam[3]


# n^mu with n.v = v^+ : n^+ = 0, n^- = 1 -> n^0 = 1/sqrt2, n^3 = -1/sqrt2
nvec = [1 / s2, 0, 0, -1 / s2]
report('nslash = gamma^+  (n^mu = delta^mu_-)', sp.simplify(slash(nvec) - gplus) == sp.zeros(4))

# massless momentum along +z
E = sp.Symbol('E', positive=True)
p = [E, 0, 0, E]
pplus = (p[0] + p[3]) / s2
chi = [sp.Matrix([1, 0]), sp.Matrix([0, 1])]
u = [sp.sqrt(E) * sp.Matrix.vstack(c, sz * c) for c in chi]
v = [sp.sqrt(E) * sp.Matrix.vstack(sz * c, c) for c in chi]


def bar(x):
    return x.H * g0


ok = all(sp.simplify(slash(p) * ui) == sp.zeros(4, 1) for ui in u) and \
     all(sp.simplify(slash(p) * vi) == sp.zeros(4, 1) for vi in v)
report('Dirac equation pslash u = pslash v = 0 (massless)', ok)
ok = sp.simplify(sum((ui * bar(ui) for ui in u), sp.zeros(4)) - slash(p)) == sp.zeros(4) and \
     sp.simplify(sum((vi * bar(vi) for vi in v), sp.zeros(4)) - slash(p)) == sp.zeros(4)
report('spin sums  sum u ubar = sum v vbar = pslash', ok)
vals = [sp.simplify((bar(ui) * gplus * ui)[0]) for ui in u] + [sp.simplify((bar(vi) * gplus * vi)[0]) for vi in v]
report('ubar_s gamma^+ u_s = vbar_s gamma^+ v_s = 2 p^+ (each s)',
       all(sp.simplify(x - 2 * pplus) == 0 for x in vals), str(vals))

# ---------------------------------------------------------------- (b) quark PDFs of free (anti)quark targets
xi = sp.Symbol('xi', real=True)
Pp = sp.Symbol('P^+', positive=True)
wm = sp.Symbol('w^-', real=True)
# connected matrix elements (spin average, colour: target colour fixed, field colour summed -> 1)
#   quark target:     <p| psibar(w) g^+ psi(0) |p>     = ubar g^+ u e^{+i p^+ w^-}
#   antiquark target: <pbar| psibar(w) g^+ psi(0) |pbar> = - vbar g^+ v e^{-i p^+ w^-}
spin_avg_u = sp.Rational(1, 2) * sum(sp.simplify((bar(ui) * gplus * ui)[0]) for ui in u)
spin_avg_v = sp.Rational(1, 2) * sum(sp.simplify((bar(vi) * gplus * vi)[0]) for vi in v)


def ft(sign_k):
    """int dw^-/(4pi) e^{-i xi P^+ w^-} e^{i sign_k P^+ w^-} = (2pi/4pi) delta(P^+(sign_k - xi))."""
    return sp.Rational(1, 2) * sp.DiracDelta(Pp * (sign_k - xi))


f_qq = (ft(+1) * spin_avg_u).subs(E, Pp / s2)
f_qqbar = (ft(-1) * (-spin_avg_v)).subs(E, Pp / s2)
h = sp.exp(xi) * (2 + xi ** 2) + xi ** 3      # generic smooth test function


def pair(dist, fn=h):
    """<dist, fn> = int dxi dist(xi) fn(xi) over a range containing the support."""
    return sp.simplify(sp.integrate(sp.expand(dist * fn), (xi, -3, 3)))


report('f_{q/q}^{(0)}(xi) = delta(1-xi)   [<f,h> = h(1)]', sp.simplify(pair(f_qq) - h.subs(xi, 1)) == 0)
report('f_{q/qbar}^{(0)}(xi) = -delta(1+xi)   [<f,h> = -h(-1)]', sp.simplify(pair(f_qqbar) + h.subs(xi, -1)) == 0)
f_qbarqbar = -f_qqbar.subs(xi, -xi)
report('f_{qbar/qbar}^{(0)}(xi) = -f_{q/qbar}(-xi) = delta(1-xi)', sp.simplify(pair(f_qbarqbar) - h.subs(xi, 1)) == 0)

# ---------------------------------------------------------------- (c) charge conjugation
C = sp.I * gam[2] * gam[0]
Cinv = C.inv()
ok = all(sp.simplify(Cinv * gam[m] * C + gam[m].T) == sp.zeros(4) for m in range(4))
report('C^{-1} gamma^mu C = -(gamma^mu)^T  (C = i g^2 g^0)', ok)
# psi^c = C psibar^T maps b <-> d : C ubar^T = v (up to a phase per spin), C vbar^T = u
cu = [sp.simplify(C * bar(ui).T) for ui in u]
cv = [sp.simplify(C * bar(vi).T) for vi in v]
# compare as spin sums (phase independent)
ok = sp.simplify(sum((x * bar(x) for x in cu), sp.zeros(4)) - sum((vi * bar(vi) for vi in v), sp.zeros(4))) == sp.zeros(4) \
     and sp.simplify(sum((x * bar(x) for x in cv), sp.zeros(4)) - sum((ui * bar(ui) for ui in u), sp.zeros(4))) == sp.zeros(4)
report('C ubar^T spans v-spinors, C vbar^T spans u-spinors (spin sums)', ok)
# antiquark PDF through psi^c:  <pbar| psibar^c(w) g^+ psi^c(0) |pbar> connected = ubar_c g^+ u_c e^{i p^+ w}
# with u_c = C vbar^T  -> same as quark case
spin_avg_c = sp.Rational(1, 2) * sum(sp.simplify((bar(x) * gplus * x)[0]) for x in cv)
f_c = (ft(+1) * spin_avg_c).subs(E, Pp / s2)
report('f_{qbar/qbar}^{(0)} from psi^c = C psibar^T  equals delta(1-xi)', sp.simplify(pair(f_c) - h.subs(xi, 1)) == 0)
# operator identity used: psibar^c(w) g^mu psi^c(0) = + psi_b(w) (g^mu)_{ab} psibar_a(0)
#   = - psibar(0) g^mu psi(w) + (anticommutator)   [check the matrix identity C^{-1} g C = -g^T with C^T = -C]
report('C^T = -C, C^dagger C = 1', sp.simplify(C.T + C) == sp.zeros(4) and sp.simplify(C.H * C - sp.eye(4)) == sp.zeros(4))

# ---------------------------------------------------------------- (d) gluon
k = sp.Symbol('k^+', positive=True)
# A_mu^b(x) ~ eps_mu e^{-i k.x}:  G^{+j} = d^+ A^j - d^j A^+ ;  d^+ = d/dx^- -> -i k_- = -i k^+  ; k_T = 0
eps = [sp.Matrix([0, 1, 0, 0]), sp.Matrix([0, 0, 1, 0])]   # Cartesian, transverse (eps^+ = eps^- = 0)
# <0|G^{+j}|k,lam>  = -i (k^+ eps^j - k^j eps^+) = -i k^+ eps^j
amp = [[-sp.I * k * e[j] for j in (1, 2)] for e in eps]
# connected <k|G^{+j}(w) G^{+j}(0)|k>: term (i) creation at w, annihilation at 0: |amp|^2 e^{i k^+ w^-}
#                                      term (ii) annihilation at w, creation at 0:  |amp|^2 e^{-i k^+ w^-}
pol_avg = sp.Rational(1, 2) * sum(sum(sp.conjugate(a) * a for a in amp_l) for amp_l in amp)
pol_avg = sp.simplify(pol_avg)
report('sum_j |<0|G^{+j}|k,lam>|^2 averaged = (k^+)^2', sp.simplify(pol_avg - k ** 2) == 0)
fg = (sp.DiracDelta(k * (1 - xi)) + sp.DiracDelta(k * (-1 - xi))) * pol_avg / (xi * k)  # (2pi/(2pi xi P^+)) delta(..)
test = sp.exp(xi) * (3 + xi)
val = pair(fg, test)
report('f_{g/g}^{(0)}(xi) = delta(1-xi) - delta(1+xi)  (odd in xi)',
       sp.simplify(val - (test.subs(xi, 1) - test.subs(xi, -1))) == 0)

# energy-momentum normalisation: <k|T^{++}|k> = 2 (k^+)^2 with T^{++}_g = sum_j G^{+j}G^{+j}
Tpp = 2 * pol_avg   # two contractions
report('<k|sum_j G^{+j}G^{+j}|k> = 2(k^+)^2  (=> int_0^1 x f_g = 1)', sp.simplify(Tpp - 2 * k ** 2) == 0)

# ---------------------------------------------------------------- (e) Wilson line orientation, numerically (SU(2))
rng = np.random.default_rng(1)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
t = [s / 2 for s in sig]
gcpl = 0.9


def expm_herm(Hm):
    w, U = np.linalg.eigh(Hm)
    return U @ np.diag(np.exp(1j * w)) @ U.conj().T


# smooth A_z(z) and gauge function theta(z) along the path z in [0,1]
cA = rng.normal(size=(3, 4))
cT = rng.normal(size=(3, 4))


def A_of(z):
    return sum((cA[a, 0] + cA[a, 1] * np.sin(2 * z) + cA[a, 2] * np.cos(3 * z) + cA[a, 3] * z ** 2) * t[a] for a in range(3))


def th_of(z):
    return sum((cT[a, 0] + cT[a, 1] * np.sin(1.3 * z) + cT[a, 2] * z + cT[a, 3] * np.cos(z)) * t[a] for a in range(3))


def U_of(z):
    return expm_herm(th_of(z))  # U = exp(i theta)


def Aprime(z, h=1e-6):
    U = U_of(z)
    dU = (U_of(z + h) - U_of(z - h)) / (2 * h)
    return U @ A_of(z) @ U.conj().T - (1j / gcpl) * dU @ U.conj().T


def wilson(Af, a, b, N):
    zs = np.linspace(a, b, N + 1)
    W = np.eye(2, dtype=complex)
    for i in range(N):
        zm = 0.5 * (zs[i] + zs[i + 1])
        W = expm_herm(gcpl * Af(zm) * (zs[i + 1] - zs[i])) @ W   # later points multiply from the LEFT
    return W


errs = []
for N in (200, 400, 800):
    W = wilson(A_of, 0.0, 1.0, N)
    Wp = wilson(Aprime, 0.0, 1.0, N)
    errs.append(np.abs(Wp - U_of(1.0) @ W @ U_of(0.0).conj().T).max())
conv = errs[-1] < 1e-4 and errs[0] / errs[-1] > 3.0
report('W[b,a] -> U(b) W[b,a] U(a)^dag  (later points to the left, D=d-igA)', conv, 'errors=%s' % np.array2string(np.array(errs), precision=2))
# wrong orientation (later points to the right) fails:
def wilson_wrong(Af, a, b, N):
    zs = np.linspace(a, b, N + 1)
    W = np.eye(2, dtype=complex)
    for i in range(N):
        zm = 0.5 * (zs[i] + zs[i + 1])
        W = W @ expm_herm(gcpl * Af(zm) * (zs[i + 1] - zs[i]))
    return W
Ww, Wwp = wilson_wrong(A_of, 0, 1, 800), wilson_wrong(Aprime, 0, 1, 800)
bad = np.abs(Wwp - U_of(1.0) @ Ww @ U_of(0.0).conj().T).max()
report('control: reversed ordering is NOT covariant (error O(1))', bad > 1e-2, 'error=%.2e' % bad)
# dW[z,a]/dz = i g A(z) W[z,a]
z0, hh = 0.6, 1e-4
dW = (wilson(A_of, 0, z0 + hh, 4000) - wilson(A_of, 0, z0 - hh, 4000)) / (2 * hh)
rhs = 1j * gcpl * A_of(z0) @ wilson(A_of, 0, z0, 4000)
report('d W[z,a]/dz = + i g A(z) W[z,a]  (left multiplication)', np.abs(dW - rhs).max() < 1e-3,
       'err=%.1e' % np.abs(dW - rhs).max())
# composition W[w,inf] W[inf,0] = W[w,0] for collinear straight lines (here: W[c,b]W[b,a]=W[c,a], and
# retracing W[w,b]W[b,w] = 1)
Wab = wilson(A_of, 0, 0.7, 2000); Wbc = wilson(A_of, 0.7, 1.0, 900)
report('composition W[c,b] W[b,a] = W[c,a]', np.abs(Wbc @ Wab - wilson(A_of, 0, 1.0, 2900)).max() < 1e-6)
Wret = wilson(A_of, 1.0, 0.7, 900) @ Wbc
report('retracing W[b,c] W[c,b] = 1', np.abs(Wret - np.eye(2)).max() < 1e-6)

print()
print('SUMMARY s1: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
