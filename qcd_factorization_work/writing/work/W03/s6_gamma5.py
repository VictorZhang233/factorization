"""W03 / Ch3 def:prelim-gamma5, App I (def:appI-hvbm, prop:appI-larin, rem:appI-anomaly).
Binding conventions: metric (+,-,-,-), gamma_5 = i g0 g1 g2 g3, eps^{0123} = +1 (so eps_{0123} = -1),
D_mu = d_mu - i g A_mu, vertex i g gamma^mu t^a, Tr(t^a t^b) = delta^{ab}/2.
  G1  Tr(g^m g^n g^r g^s g5) = -4 i eps^{mnrs}, all 256 index sets
  G2  Larin replacement in our convention: g^mu g5 = -(i/6) eps^{mu nu rho sigma} g_nu g_rho g_sigma (all mu);
      the literature form g_mu g5 = +(i/6) eps_{mu nu rho sigma} g^nu g^rho g^sigma holds iff eps_{0123} = +1
  G3  transverse tensors: eps_perp^{mu nu} = eps^{mu nu rho sigma} n_A,rho n_B,sigma has eps_perp^{12} = +1; g_perp
  G4  D-dim Clifford identities (explicit reps in D = 6, 8, Minkowski signature):
        g^rho G^{[n]} g_rho = (-1)^n (D - 2n) G^{[n]}   (n = 1, 2, 3; G^{[n]} antisymmetrised products)
        g_a g^m g^n g^r g^s g^a = 2[g^s g^m g^n g^r + g^r g^n g^m g^s] - (4-D) g^m g^n g^r g^s
  G5  HVBM in D = 6, 8: g5 := i gbar^0 gbar^1 gbar^2 gbar^3 anticommutes with gbar^mu (mu < 4), commutes with ghat^mu;
      g^rho (gbar^{[3]}) g_rho = (6 - D) gbar^{[3]} (rho summed over all D dims)
  G6  anticommuting g5 in D dims is inconsistent with Tr(g5 g^m g^n g^r g^s) != 0: algebraic steps
        Tr(g5) = 0, (2D-4) Tr(g5 g^a g^b) = 0, (2D-8) Tr(g5 g^m g^n g^r g^s) = 0   (symbolic in D)
  G7  one-loop finite renormalization of the non-singlet axial current in the Larin scheme:
        UV part of the vertex ~ (g^a g^r Gamma g_r g_a)/D * (1/eps + c);  X_V = (D-2)^2/D, X_L = (6-D)^2/D,
        X_L - X_V = 4 eps + O(eps^2)  ->  Z_5^ns = 1 - 4 C_F alpha_s/(4 pi) + O(alpha_s^2)  (VF-POL-1 coefficient)
      and the vector-current check Z_1 = Z_2 (Feynman gauge): UV pole of the vertex = + a_s C_F/eps
  G8  heavy-fermion (Pauli-Villars) bookkeeping, validated on the scalar density (SVZ low-energy theorem):
        lim_{M->inf} <g g| M psibar psi |0> = -(alpha_s/(12 pi)) <g g| G^a_{mu nu} G^{a mu nu} |0>
      then the axial anomaly: <g g|d_mu J5^mu|0> = - lim_{M->inf} <g g| 2 i M psibar g5 psi |0>_(normal loop)
        = c * (g^2/(32 pi^2)) <g g| eps^{mu nu rho sigma} G^a_{mu nu} G^a_{rho sigma} |0>,  c determined here.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok))
    print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

# ---------------- 4D Dirac matrices ----------------
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
def gi(s): return np.block([[Z2, s], [-s, Z2]]).astype(complex)
G = [g0, gi(sx), gi(sy), gi(sz)]
g5 = 1j * G[0] @ G[1] @ G[2] @ G[3]
eta = np.diag([1., -1., -1., -1.])
Glow = [eta[m, m] * G[m] for m in range(4)]        # gamma_mu
def levi(*idx):
    return float(sp.LeviCivita(*idx))               # LeviCivita(0,1,2,3) = +1  => eps^{0123} = +1
def slash(v):                                        # v^mu contravariant
    return sum(eta[m, m] * v[m] * G[m] for m in range(4))
def mdot(a, b): return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
def eps_contract(a, b, c, d):                        # eps_{mu nu rho sigma} a^mu b^nu c^rho d^sigma with eps_{0123} = -1
    tot = 0
    for p in itertools.permutations(range(4)):
        tot += levi(*p) * a[p[0]] * b[p[1]] * c[p[2]] * d[p[3]]
    return -tot                                      # lowering four indices: eps_{0123} = -eps^{0123}

# G1
ok = True
for m, n, r, s in itertools.product(range(4), repeat=4):
    ok &= np.isclose(np.trace(G[m] @ G[n] @ G[r] @ G[s] @ g5), -4j * levi(m, n, r, s))
check('G1 Tr(g^m g^n g^r g^s g5) = -4i eps^{mnrs} (eps^{0123}=+1), all 256 index sets', ok)
# G2
ok_ours = all(np.allclose(G[mu] @ g5, -1j / 6 * sum(levi(mu, n, r, s) * Glow[n] @ Glow[r] @ Glow[s]
                                                 for n in range(4) for r in range(4) for s in range(4))) for mu in range(4))
# literature form with eps_{0123} = +1 (i.e. eps_lit_{mnrs} = +LeviCivita), lower index mu on the left
ok_lit = all(np.allclose(Glow[mu] @ g5, 1j / 6 * sum(levi(mu, n, r, s) * G[n] @ G[r] @ G[s]
                                                  for n in range(4) for r in range(4) for s in range(4))) for mu in range(4))
# the literature form evaluated with OUR eps_{0123} = -1 has the wrong sign:
ok_wrong = all(np.allclose(Glow[mu] @ g5, -(1j / 6) * sum((-levi(mu, n, r, s)) * G[n] @ G[r] @ G[s]
                                                       for n in range(4) for r in range(4) for s in range(4))) for mu in range(4))
check('G2 Larin replacement (ours): g^mu g5 = -(i/6) eps^{mu nu rho sigma} g_nu g_rho g_sigma, all mu', ok_ours)
check('G2 literature form g_mu g5 = (i/6) eps_{mu nu rho sigma} g^nu g^rho g^sigma holds iff eps_{0123}=+1 (opposite to ours)',
      ok_lit and ok_wrong)
# G3
nA = np.array([1, 0, 0, 1]) / np.sqrt(2); nB = np.array([1, 0, 0, -1]) / np.sqrt(2)
nA_low = eta @ nA; nB_low = eta @ nB
eperp12 = sum(levi(1, 2, r, s) * nA_low[r] * nB_low[s] for r in range(4) for s in range(4))
gperp = np.linalg.inv(eta) - np.outer(nA, nB) - np.outer(nB, nA)    # g^{mu nu} - nA^mu nB^nu - nB^mu nA^nu
check('G3 eps_perp^{12} = eps^{12 rho sigma} n_A,rho n_B,sigma = +1; g_perp^{mu nu} = diag(0,-1,-1,0)',
      np.isclose(eperp12, 1.0) and np.allclose(gperp, np.diag([0, -1., -1., 0])), 'eps_perp^12 = %.3f' % eperp12)

# ---------------- D-dim Clifford algebras (D = 6, 8) ----------------
def clifford(Dd):
    n = Dd // 2
    def kron(*ms):
        out = np.array([[1]], dtype=complex)
        for m_ in ms: out = np.kron(out, m_)
        return out
    E = []
    for j in range(n):
        E.append(kron(*([sz] * j + [sx] + [I2] * (n - j - 1))))
        E.append(kron(*([sz] * j + [sy] + [I2] * (n - j - 1))))
    return [E[0]] + [1j * E[i] for i in range(1, Dd)]
def antisym(gam, idx):
    tot = 0
    for p in itertools.permutations(range(len(idx))):
        sgn = sp.combinatorics.Permutation(list(p)).signature()
        M_ = np.eye(gam[0].shape[0], dtype=complex)
        for k in p: M_ = M_ @ gam[idx[k]]
        tot = tot + sgn * M_
    return tot / len(list(itertools.permutations(range(len(idx)))))
import sympy.combinatorics
okG4 = True; okG4b = True; okG5 = True
for Dd in (6, 8):
    gam = clifford(Dd)
    met = np.diag([1.] + [-1.] * (Dd - 1))
    glow = [met[m, m] * gam[m] for m in range(Dd)]
    dim = gam[0].shape[0]
    okG4 &= all(np.allclose(gam[m] @ gam[n_] + gam[n_] @ gam[m], 2 * met[m, n_] * np.eye(dim)) for m in range(Dd) for n_ in range(Dd))
    rng = np.random.default_rng(Dd)
    for nn in (1, 2, 3):
        for trial in range(4):
            idx = list(rng.choice(Dd, size=nn, replace=False))
            A_ = antisym(gam, idx)
            lhs = sum(gam[r] @ A_ @ glow[r] for r in range(Dd))
            okG4 &= np.allclose(lhs, (-1)**nn * (Dd - 2 * nn) * A_)
    for trial in range(6):
        m, n_, r, s = rng.integers(0, Dd, size=4)
        X = gam[m] @ gam[n_] @ gam[r] @ gam[s]
        lhs = sum(glow[a] @ X @ gam[a] for a in range(Dd))
        rhs = 2 * (gam[s] @ gam[m] @ gam[n_] @ gam[r] + gam[r] @ gam[n_] @ gam[m] @ gam[s]) - (4 - Dd) * X
        okG4b &= np.allclose(lhs, rhs)
    # HVBM
    g5D = 1j * gam[0] @ gam[1] @ gam[2] @ gam[3]
    okG5 &= all(np.allclose(g5D @ gam[m] + gam[m] @ g5D, 0) for m in range(4))
    okG5 &= all(np.allclose(g5D @ gam[m] - gam[m] @ g5D, 0) for m in range(4, Dd))
    for trial in range(4):
        idx = list(rng.choice(4, size=3, replace=False))
        A_ = antisym(gam, idx)
        lhs = sum(gam[r] @ A_ @ glow[r] for r in range(Dd))
        okG5 &= np.allclose(lhs, (6 - Dd) * A_)
check('G4 g^rho G^[n] g_rho = (-1)^n (D-2n) G^[n], n=1,2,3, explicit D=6,8 representations', okG4)
check('G4 g_a g^m g^n g^r g^s g^a = 2[g^s g^m g^n g^r + g^r g^n g^m g^s] - (4-D) g^m g^n g^r g^s (D=6,8)', okG4b)
check('G5 HVBM: g5 anticommutes with gbar, commutes with ghat; g^rho gbar^[3] g_rho = (6-D) gbar^[3] (D=6,8)', okG5)

# G6 symbolic: with T2 = Tr(g5 g^a g^b), T4 = Tr(g5 g^m g^n g^r g^s) and an anticommuting g5 in D dims:
Dsym, T0, T2, T4 = sp.symbols('D T0 T2 T4')
# (i) Tr g5 = D^{-1} Tr(g5 g^l g_l); cyclic + anticommute: Tr(g5 g^l g_l) = -Tr(g5 g_l g^l)  =>  D T0 = -D T0
eq0 = sp.Eq(Dsym * T0, -Dsym * T0)
# (ii) D T2 = Tr(g5 g^a g^b g^l g_l) = -Tr(g5 g_l g^a g^b g^l) = -[4 g^{ab} T0 - (4-D) T2]
eq2 = sp.Eq(Dsym * T2, -(4 * 0 - (4 - Dsym) * T2))      # T0 = 0 used
# (iii) D T4 = -Tr(g5 g_a X g^a) = -[2(-T4) + 2(-T4) - (4-D) T4]  (total antisymmetry from (ii))
eq4 = sp.Eq(Dsym * T4, -(2 * (-T4) + 2 * (-T4) - (4 - Dsym) * T4))
s0 = sp.solve(eq0, T0); s2 = sp.solve(eq2, T2); s4 = sp.solve(eq4, T4)
red2 = sp.factor(eq2.lhs - eq2.rhs); red4 = sp.factor(eq4.lhs - eq4.rhs)
check('G6 anticommuting g5 in D dims: Tr g5 = 0, (2D-4)Tr(g5 g g) = 0, (2D-8)Tr(g5 gggg) = 0',
      s0 == [0] and sp.simplify(red2 - (2 * Dsym - 4) * T2) == 0 and sp.simplify(red4 - (2 * Dsym - 8) * T4) == 0,
      'factors: %s ; %s' % (red2, red4))

# G7 Larin finite renormalization at one loop
e = sp.Symbol('epsilon')
Dd = 4 - 2 * e
XV = (Dd - 2)**2 / Dd
XL = (6 - Dd)**2 / Dd
XA = (Dd - 2)**2 / Dd          # anticommuting g5: same as vector
ser = sp.series(XL - XV, e, 0, 2).removeO()
okL = sp.simplify(ser - 4 * e) == 0 and sp.simplify(sp.series(XV, e, 0, 1).removeO() - 1) == 0
# UV part of the one-loop vertex with insertion Gamma: -i g^2 C_F X int d^Dk/(2pi)^D 1/(k^2)^2, the integral = i/(16 pi^2 eps)
# => Gamma^(1)_UV = + alpha_s C_F/(4 pi) * X/eps.  For Gamma = gamma^mu: pole a_s C_F/eps = -delta Z_2 (Feynman gauge)
aS, CF = sp.symbols('a_s C_F', positive=True)      # a_s = alpha_s/(4 pi)
Z2 = 1 - aS * CF / e
vec_bare = 1 + aS * CF * sp.series(XV / e, e, 0, 1).removeO()
vec_ren = sp.expand(sp.series(Z2 * vec_bare, aS, 0, 2).removeO())
okV = sp.simplify(vec_ren.coeff(aS, 1).coeff(e, -1)) == 0
# Larin: MS-bar renormalized (pole removed) minus anticommuting: finite difference
lar_bare = 1 + aS * CF * sp.series(XL / e, e, 0, 1).removeO()
ac_bare = 1 + aS * CF * sp.series(XA / e, e, 0, 1).removeO()
diff = sp.simplify(sp.expand(lar_bare - ac_bare))
Z5 = sp.simplify(1 - diff)
check('G7 Larin vs anticommuting: X_L - X_V = 4 eps + O(eps^2); vertex difference = 4 C_F a_s; Z_5^ns = 1 - 4 C_F a_s',
      okL and sp.simplify(diff - 4 * aS * CF) == 0 and sp.simplify(Z5 - (1 - 4 * CF * aS)) == 0, 'Z5 = %s' % Z5)
check('G7 vector current: UV pole of the one-loop vertex (+a_s C_F/eps) cancels against Z_2 = 1 - a_s C_F/eps (Z_1 = Z_2)', okV)

# ---------------- G8 heavy-fermion bookkeeping ----------------
# Amplitude <k1 a e1, k2 b e2 | psibar Gamma psi (0) |0>, one loop, fermion of mass M:
#   direct diagram: (-1)_loop * Tr_c(t^b t^a) * (i g)^2 * i^3 * Int d^Dl/(2pi)^D Tr[Gamma (p3+M) e2slash (p2+M) e1slash (p1+M)]/(D1 D2 D3)
#   p1 = l, p2 = l-k1, p3 = l-k1-k2 (trace written against the fermion flow O -> v1 -> v2 -> O); crossed: (1 <-> 2).
#   Feynman parameters: 1/(D1D2D3) = 2 Int_simplex 1/((l'^2 - Delta)^3), l = l' + P, P = y k1 + z (k1+k2),
#   Delta = M^2 - x z q^2 (k_i^2 = 0);  Int d^4l' 1/(l'^2-Delta)^3 = -i/(32 pi^2 Delta);
#   Int d^Dl' l'^2/(l'^2-Delta)^3 = i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Delta^{-eps}.
rng = np.random.default_rng(11)
def rand_lightlike():
    v = rng.normal(size=3); v /= np.linalg.norm(v)
    E_ = abs(rng.normal()) + 0.5
    return np.array([E_, *(E_ * v)])
k1 = rand_lightlike(); k2 = rand_lightlike()
e1 = rng.normal(size=4); e2 = rng.normal(size=4)       # arbitrary (off-transverse allowed: test gauge invariance too)
gc = 1.0                                                # coupling g (overall g^2 factored)
q2 = mdot(k1 + k2, k1 + k2)
def simplex_avg(f, n=60):
    # Int_simplex f(x,y,z) dx dy dz delta(1-x-y-z), Gauss-Legendre on the triangle (x, z), y = 1-x-z
    xs, ws = np.polynomial.legendre.leggauss(n)
    tot = 0.0
    for xi, wi in zip(xs, ws):
        x = 0.5 * (xi + 1); wx = 0.5 * wi
        for zj, wj in zip(xs, ws):
            z = 0.5 * (zj + 1) * (1 - x); wz = 0.5 * wj * (1 - x)
            tot += wx * wz * f(x, 1 - x - z, z)
    return tot
def scalar_amp(ka, ea, kb, eb, M):
    """direct diagram, gluon a emitted first along the fermion flow; returns amplitude / delta^{ab}"""
    def integrand(x, y, z):
        P = y * ka + z * (ka + kb)
        Delta = M * M - x * z * q2
        N0 = M * np.trace((slash(P - ka - kb) + M * np.eye(4)) @ slash(eb) @ (slash(P - ka) + M * np.eye(4)) @ slash(ea)
                          @ (slash(P) + M * np.eye(4)))
        # D-dim l'l' term: M^2 * (l'^2/D) * 4(4-D) e1.e2 -> Int = M^2 e1.e2 * i/(16 pi^2) * 2 (at D -> 4)
        ll = M * M * mdot(ea, eb) * 1j / (16 * np.pi**2) * 2.0
        return 2 * (-1j * N0 / (32 * np.pi**2 * Delta) + ll)
    I = simplex_avg(integrand)
    pref = (-1) * 0.5 * (1j * gc)**2 * (1j)**3
    return pref * I
def axial_amp(ka, ea, kb, eb, M):
    def integrand(x, y, z):
        P = y * ka + z * (ka + kb)
        Delta = M * M - x * z * q2
        N5 = np.trace(2j * M * g5 @ (slash(P - ka - kb) + M * np.eye(4)) @ slash(eb) @ (slash(P - ka) + M * np.eye(4))
                      @ slash(ea) @ (slash(P) + M * np.eye(4)))
        return 2 * (-1j * N5 / (32 * np.pi**2 * Delta))
    I = simplex_avg(integrand)
    pref = (-1) * 0.5 * (1j * gc)**2 * (1j)**3
    return pref * I
alpha_s = gc**2 / (4 * np.pi)
GG = -4 * (mdot(k1, k2) * mdot(e1, e2) - mdot(k1, e2) * mdot(k2, e1))      # <gg|G^a G^a|0>/delta^{ab}
epsGG = -8 * eps_contract(k1, e1, k2, e2)                                   # <gg|eps G G|0>/delta^{ab}
res = []
for M in (30.0, 100.0, 300.0):
    Asc = scalar_amp(k1, e1, k2, e2, M) + scalar_amp(k2, e2, k1, e1, M)
    res.append(Asc)
target_sc = -(alpha_s / (12 * np.pi)) * GG
okS = abs(res[-1] - target_sc) < 2e-3 * abs(target_sc) and abs(res[-1] - target_sc) < abs(res[0] - target_sc) + 1e-12
# gauge invariance of the total: e1 -> k1 gives zero (up to O(q^2/M^2))
Agauge = scalar_amp(k1, k1, k2, e2, 300.0) + scalar_amp(k2, e2, k1, k1, 300.0)
check('G8 SVZ check: lim <gg|M psibar psi|0> = -(alpha_s/12pi)<gg|G^aG^a|0> (M = 30,100,300)', okS,
      'ratio(M=300) = %s; gauge test |A(e1->k1)| = %.1e' % (np.round(res[-1] / target_sc, 6), abs(Agauge)))
resA = []
for M in (30.0, 100.0, 300.0):
    A5 = axial_amp(k1, e1, k2, e2, M) + axial_amp(k2, e2, k1, e1, M)
    resA.append(-A5)                     # <gg| d.J5 |0> = - lim <gg| 2iM psibar g5 psi |0>_(normal loop)
cval = resA[-1] / ((gc**2 / (32 * np.pi**2)) * epsGG)
okA = abs(cval.imag) < 1e-6 and abs(abs(cval.real) - 1) < 1e-3
check('G8 ABJ anomaly: <gg|d.J5|0> = c (g^2/32 pi^2) <gg|eps^{mnrs} G^a_mn G^a_rs|0>, |c| = 1', okA,
      'c = %s (M=300); M-independence: %s' % (np.round(cval, 6), [np.round(r_ / resA[-1], 6) for r_ in resA]))
Agauge5 = axial_amp(k1, k1, k2, e2, 300.0) + axial_amp(k2, e2, k1, k1, 300.0)
check('G8 anomaly amplitude is gauge invariant (e1 -> k1 gives 0)', abs(Agauge5) < 1e-8 * max(1, abs(resA[-1])),
      '|A5(e1->k1)| = %.1e' % abs(Agauge5))
print('      => in our conventions: d_mu J5^mu = %+d * n_f * (alpha_s/(8 pi)) eps^{mu nu rho sigma} G^a_{mu nu} G^a_{rho sigma}'
      ' = %+d * n_f * (alpha_s/(4 pi)) G^a_{mu nu} Gtilde^{a mu nu},  Gtilde^{a mu nu} = (1/2) eps^{mu nu rho sigma} G^a_{rho sigma}'
      % (round(cval.real), round(cval.real)))
print('\nSUMMARY s6: %d/%d PASS' % (sum(PASS), len(PASS)))
