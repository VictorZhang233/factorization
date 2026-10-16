"""W03 / Ch3 sec:prelim-wilson.  Binding conventions: W[b,a] = P exp(i g int_a^b dz.A), later points to the left,
A(x) = int d^4k/(2pi)^4 e^{-ik.x} At(k) (k flows INTO the line), adiabatic factor e^{-eps s} (s >= 0 distance from the
finite end; eps is the adiabatic parameter, unrelated to the DR epsilon).
  R1  iterated integrals, m = 1,2,3, all four semi-infinite lines (sympy, exact at finite eps):
        W[0,-inf n]: prod_j i/(n.(k_1+..+k_j) + i j eps)          (k_1 nearest -inf)
        W[inf n,0]:  prod_j -i/(n.(k_j+..+k_m) - i (m-j+1) eps)    (k_1 nearest 0)
        W[-inf n,0]: vertex -ig, prod_j i/(n.(k_j+..+k_m) + i(m-j+1) eps)  (k_1 nearest 0)
        W[0,inf n]:  vertex -ig, prod_j -i/(n.(k_1+..+k_j) - i j eps)     (k_1 nearest +inf)
  R2  one-gluon terms: W[inf n,0] -> g n.A/(n.k - i0), W[-inf n,0] -> g n.A/(n.k + i0); future - past = 2 pi i g n.A delta(n.k)
      (numerical test of 1/(x-i e) - 1/(x+i e) -> 2 pi i delta(x) on a Gaussian test function)
  R3  real-gluon rule in a cut graph: emitted on W[inf n,0] (k=-l): -g n/(n.l + i0); absorbed on W[w, inf n] (k=+l):
      -g n/(n.l - i0): complex conjugates
  E1  abelian eikonal identity sum_{pi in S_m} prod_j 1/(a_pi(1)+..+a_pi(j)) = prod 1/a_j, m <= 5 (exact rationals) and
      symbolic m <= 4
  E2  exact at finite eps with the adiabatic (cumulative) regulator, past and future forms, m <= 4 symbolic
  E3  uniform +i eps: m=2 defect = -i eps/[(a1+ie)(a2+ie)(a1+a2+ie)] (with the factors i^2); pairing with
      1/((1+a1^2)(1+a2^2)) equals pi^2 eps/((1+eps)^2 (2+eps))  (claim N26 printable) -- numerical + residues
  E4  non-abelian m=2 decomposition: T_b T_a E12 + T_a T_b E21 = 1/2{T_a,T_b} * (abelian product) + 1/2[T_b,T_a](E12-E21)
  S1  finite light-like segment, w = (0^+, w^-, 0_T): W^(1)[w,0] = g At^+(k) (1 - e^{-i k^+ w^-})/k^+ ; limits w^- -> +inf,
      -inf with the adiabatic factor give g At^+/(k^+ -+ i eps); the two decompositions through +inf and -inf agree
  C1  covariance (numerical, SU(2) and SU(3)): discretized path-ordered exponential, random smooth fields and gauge
      functions: W'[b,a] = U(b) W[b,a] U^dag(a); reversed ordering fails at O(1); composition, retracing, unitarity;
      adjoint line W^(A)_{ab} = 2 Tr[t^a W t^b W^dag] is the adjoint path-ordered exponential with (T^c)_{ab} = -i f^{cab}
  C2  infinitesimal argument: delta W = i(theta(b) W - W theta(a)); for the reversed ordering an extra term
      2 g int ds V(s,a)[a(s),theta(s)]V(b,s) remains (checked numerically to first order in theta)
"""
import sys, os, itertools, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from fractions import Fraction

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok))
    print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

# ---------------- R1 iterated integrals ----------------
eps = sp.Symbol('epsilon', positive=True)
a = sp.symbols('a1:5', real=True)   # a_j = n.k_j
import mpmath as mp

# exact integrator for integrands exp(sum_i c_i l_i) over ordered simplices: the integral over l_j of exp(C l_j) from
# -inf to U (Re C > 0) is exp(C U)/C, from L to +inf (Re C < 0) is -exp(C L)/C.  We track the exponent as a linear
# form in the remaining variables and the prefactor; this is the iterated integration done by hand, step by step.
def nested(coeffs, order, lower_inf):
    """coeffs[j] = coefficient C_j of l_j in the exponent; order = list of variable indices in integration order;
    lower_inf=True: l_{order[0]} from -inf to l_{order[1]}, ..., last up to 0.
    lower_inf=False: l_{order[0]} from l_{order[1]} to +inf, ..., last from 0 to +inf."""
    expo = {j: coeffs[j] for j in range(len(coeffs))}
    pref = sp.Integer(1)
    for idx, j in enumerate(order):
        C = expo.pop(j)
        nxt = order[idx + 1] if idx + 1 < len(order) else None
        if lower_inf:
            pref = pref / C
        else:
            pref = -pref / C
        if nxt is not None:
            expo[nxt] = expo[nxt] + C      # exp(C l_j) evaluated at l_j = l_next
        # at the last step the boundary is 0: exp(0) = 1
    return sp.simplify(pref)

def num_nested(coeffs, order, lower_inf, vals):
    """independent numerical check by mpmath quadrature (m <= 2)"""
    C = [complex(sp.N(c.subs(vals))) for c in coeffs]
    m = len(C)
    if m == 1:
        if lower_inf:
            return mp.quad(lambda x: mp.exp(C[0] * x), [-mp.inf, 0])
        return mp.quad(lambda x: mp.exp(C[0] * x), [0, mp.inf])
    j0, j1 = order
    if lower_inf:   # l_j0 from -inf to l_j1, l_j1 from -inf to 0
        return mp.quad(lambda x1: mp.quad(lambda x0: mp.exp(C[j0] * x0 + C[j1] * x1), [-mp.inf, x1]), [-mp.inf, 0])
    return mp.quad(lambda x1: mp.quad(lambda x0: mp.exp(C[j0] * x0 + C[j1] * x1), [x1, mp.inf]), [0, mp.inf])

vals = {a[0]: 0.83, a[1]: -0.41, a[2]: 1.37, eps: 0.37}
for m in (1, 2, 3):
    # past-pointing W[0,-inf n]: field at z = l n (l<0): e^{-i l a_j}, damping e^{+eps l}: exponent l(-i a_j + eps)
    coeffs = [-sp.I * a[j] + eps for j in range(m)]
    exact = nested(coeffs, list(range(m)), True)            # l_1 < l_2 < ... < l_m < 0 (gluon 1 nearest -inf)
    closed = sp.Integer(1)
    for j in range(m):
        closed *= sp.I / (sum(a[:j + 1]) + sp.I * (j + 1) * eps)
    ok = sp.simplify(exact - closed) == 0
    info = ''
    if m <= 2:
        nv = num_nested(coeffs, list(range(m)), True, vals); cv = complex(sp.N(closed.subs(vals)))
        ok = ok and abs(nv - cv) < 1e-9; info = 'num=%s closed=%s' % (mp.nstr(nv, 10), mp.nstr(cv, 10))
    check('R1 past W[0,-inf n], m=%d: prod i/(n.(k1+..+kj) + i j eps)' % m, ok, info)
    # future-pointing W[inf n,0]: field at z = l n (l>0): e^{-i l a_j}, damping e^{-eps l}; 0 < l_1 < ... < l_m
    coeffs = [-sp.I * a[j] - eps for j in range(m)]
    exact = nested(coeffs, list(reversed(range(m))), False)  # integrate l_m first from l_{m-1} to inf
    closed = sp.Integer(1)
    for j in range(m):
        closed *= -sp.I / (sum(a[j:m]) - sp.I * (m - j) * eps)
    ok = sp.simplify(exact - closed) == 0
    info = ''
    if m <= 2:
        nv = num_nested(coeffs, list(reversed(range(m))), False, vals); cv = complex(sp.N(closed.subs(vals)))
        ok = ok and abs(nv - cv) < 1e-9; info = 'num=%s closed=%s' % (mp.nstr(nv, 10), mp.nstr(cv, 10))
    check('R1 future W[inf n,0], m=%d: prod -i/(n.(kj+..+km) - i(m-j+1) eps)' % m, ok, info)
    # conjugate W[-inf n,0]: path 0 -> -inf, z = -s n (s>0), field e^{+i s a_j}, damping e^{-eps s}; 0 < s_1 < ... < s_m
    coeffs = [sp.I * a[j] - eps for j in range(m)]
    exact = nested(coeffs, list(reversed(range(m))), False)
    closed = sp.Integer(1)
    for j in range(m):
        closed *= sp.I / (sum(a[j:m]) + sp.I * (m - j) * eps)
    check('R1 conjugate W[-inf n,0], m=%d: prod i/(n.(kj+..+km) + i(m-j+1) eps) [vertices -ig]' % m, sp.simplify(exact - closed) == 0)
    # conjugate W[0,inf n]: path +inf -> 0, z = t n, gluon 1 nearest +inf: t_1 > t_2 > ... > t_m > 0, field e^{-i t a_j},
    # damping e^{-eps t}; integrate t_1 from t_2 to inf first
    coeffs = [-sp.I * a[j] - eps for j in range(m)]
    exact = nested(coeffs, list(range(m)), False)
    closed = sp.Integer(1)
    for j in range(m):
        closed *= -sp.I / (sum(a[:j + 1]) - sp.I * (j + 1) * eps)
    check('R1 conjugate W[0,inf n], m=%d: prod -i/(n.(k1+..+kj) - i j eps) [vertices -ig]' % m, sp.simplify(exact - closed) == 0)

# ---------------- R2 future - past ----------------
gsym = sp.Symbol('g', positive=True)
one_future = (sp.I * gsym) * (-sp.I) / (a[0] - sp.I * eps)
one_past = (sp.I * gsym) * (sp.I) / (a[0] + sp.I * eps)
check('R2 one-gluon: W[inf n,0] -> g/(n.k - i0); W[0,-inf n] -> -g/(n.k + i0)',
      sp.simplify(one_future - gsym / (a[0] - sp.I * eps)) == 0 and sp.simplify(one_past + gsym / (a[0] + sp.I * eps)) == 0)
one_conj_past = (-sp.I * gsym) * sp.I / (a[0] + sp.I * eps)
check('R2 one-gluon: W[-inf n,0] -> g/(n.k + i0)', sp.simplify(one_conj_past - gsym / (a[0] + sp.I * eps)) == 0)
# future minus past at the same point (W[inf n,0] - W[-inf n,0]): g[1/(x-ie) - 1/(x+ie)] -> 2 pi i g delta(x)
for e in (1e-2, 1e-3):
    f = lambda x: mp.e**(-(x - 0.3)**2)
    val = mp.quad(lambda x: (1 / (x - 1j * e) - 1 / (x + 1j * e)) * f(x), [-mp.inf, -1, 0, 0.3, 1, mp.inf])
    target = 2j * mp.pi * f(0)
    print('      e=%g: int[1/(x-ie)-1/(x+ie)] f = %s ; 2 pi i f(0) = %s' % (e, mp.nstr(val, 10), mp.nstr(target, 10)))
e = 1e-5
val = mp.quad(lambda x: (1 / (x - 1j * e) - 1 / (x + 1j * e)) * mp.e**(-(x - 0.3)**2), [-mp.inf, -1, -1e-3, 0, 1e-3, 0.3, 1, mp.inf])
print('      e=%g: int[1/(x-ie)-1/(x+ie)] f = %s (error is O(e))' % (e, mp.nstr(val, 10)))
check('R2 1/(x-i0) - 1/(x+i0) = 2 pi i delta(x) (Gaussian test function; error linear in e)', abs(val - target) < 1e-4)
# ---------------- R3 cut-graph real gluon ----------------
l = sp.Symbol('l', real=True)
emit = (sp.I * gsym) * (-sp.I) / (-l - sp.I * eps)        # W[inf n,0], k = -l
absorb = (-sp.I * gsym) * (-sp.I) / (l - sp.I * eps)       # W[w,inf n] = conjugate line, k = +l (phase e^{-ik.w} aside)
check('R3 emitted: -g/(n.l + i0); absorbed on the conjugate line: -g/(n.l - i0); complex conjugates',
      sp.simplify(emit + gsym / (l + sp.I * eps)) == 0 and sp.simplify(absorb + gsym / (l - sp.I * eps)) == 0
      and sp.simplify(sp.conjugate(emit) - absorb) == 0)

# ---------------- E1-E4 eikonal identity ----------------
def eik_sum(vals):
    tot = 0
    for perm in itertools.permutations(range(len(vals))):
        prod = 1
        s = 0
        for j in perm:
            s += vals[j]
            prod *= 1 / s
        tot += prod
    return tot
ok = True
rng = np.random.default_rng(11)
for m in range(1, 6):
    for trial in range(5):
        vals = [Fraction(int(rng.integers(1, 40)), int(rng.integers(1, 9))) * (1 if rng.random() < 0.6 else -1) for _ in range(m)]
        # reject vanishing partial sums
        bad = any(sum(c) == 0 for r in range(1, m + 1) for c in itertools.combinations(vals, r))
        if bad:
            continue
        lhs = eik_sum(vals)
        rhs = 1
        for v_ in vals:
            rhs *= 1 / v_
        ok &= (lhs == rhs)
check('E1 abelian eikonal identity, exact rationals, m = 1..5', ok)
ok = True
for m in range(1, 5):
    lhs = 0
    for perm in itertools.permutations(range(m)):
        prod = 1; s = 0
        for j in perm:
            s += a[j]; prod *= 1 / s
        lhs += prod
    rhs = 1
    for j in range(m): rhs *= 1 / a[j]
    ok &= sp.simplify(sp.together(lhs - rhs)) == 0
check('E1 abelian eikonal identity, symbolic m = 1..4', ok)
ok_p = ok_f = True
for m in range(1, 5):
    lp = 0; lf = 0
    for perm in itertools.permutations(range(m)):
        prod = 1; s = 0
        for jj, j in enumerate(perm):
            s += a[j]; prod *= sp.I / (s + sp.I * (jj + 1) * eps)
        lp += prod
        prodf = 1
        for jj in range(m):
            Kj = sum(a[perm[i]] for i in range(jj, m))
            prodf *= -sp.I / (Kj - sp.I * (m - jj) * eps)
        lf += prodf
    rp = 1; rf = 1
    for j in range(m):
        rp *= sp.I / (a[j] + sp.I * eps); rf *= -sp.I / (a[j] - sp.I * eps)
    ok_p &= sp.simplify(sp.together(lp - rp)) == 0
    ok_f &= sp.simplify(sp.together(lf - rf)) == 0
check('E2 exact at finite eps with cumulative regulator (past form), m = 1..4', ok_p)
check('E2 exact at finite eps with cumulative regulator (future form), m = 1..4', ok_f)
# E3 uniform regulator
lu = sum(sp.I / (a[p0] + sp.I * eps) * sp.I / (a[0] + a[1] + sp.I * eps) for p0 in (0, 1))
ru = sp.I / (a[0] + sp.I * eps) * sp.I / (a[1] + sp.I * eps)
defect = sp.simplify(lu - ru)
target = -sp.I * eps / ((a[0] + sp.I * eps) * (a[1] + sp.I * eps) * (a[0] + a[1] + sp.I * eps))
check('E3 uniform +i eps, m=2: defect = -i eps/[(a1+ie)(a2+ie)(a1+a2+ie)]', sp.simplify(defect - target) == 0)
# pairing with 1/((1+a1^2)(1+a2^2)): do the a2 integral by residues (close in the upper half plane: poles of
# 1/(a2+ie) and 1/(a1+a2+ie) are in the LHP; only a2 = i from 1/(1+a2^2))
a1s, a2s = sp.symbols('a1 a2')
f2 = target.subs({a[0]: a1s, a[1]: a2s}) / ((1 + a1s**2) * (1 + a2s**2))
r2 = sp.residue(f2, a2s, sp.I)
inner = sp.simplify(2 * sp.pi * sp.I * r2)
r1 = sp.residue(inner, a1s, sp.I)      # inner as a function of a1: poles at a1 = -ie (LHP), a1 = -i - ie (LHP), a1 = +-i
pair = sp.simplify(2 * sp.pi * sp.I * r1)
check('E3 pairing of the defect with 1/((1+a1^2)(1+a2^2)) = pi^2 eps/((1+eps)^2(2+eps))',
      sp.simplify(pair - sp.pi**2 * eps / ((1 + eps)**2 * (2 + eps))) == 0, 'pairing = %s' % sp.factor(pair))
# numerical confirmation at eps = 0.3
e0 = 0.3
mp.mp.dps = 30
num = mp.quad(lambda x, y: complex(-1j * e0 / ((x + 1j * e0) * (y + 1j * e0) * (x + y + 1j * e0)) / ((1 + x * x) * (1 + y * y))),
              [-mp.inf, -2, -0.5, 0, 0.5, 2, mp.inf], [-mp.inf, -2, -0.5, 0, 0.5, 2, mp.inf])
mp.mp.dps = 15
check('E3 numerical pairing at eps=0.3', abs(num - mp.pi**2 * e0 / ((1 + e0)**2 * (2 + e0))) < 1e-6, 'num=%s' % mp.nstr(num, 12))
# E4 non-abelian decomposition with generic noncommuting matrices
Ta = sp.MatrixSymbol('Ta', 3, 3); Tb = sp.MatrixSymbol('Tb', 3, 3)
E12 = sp.I / (a[0] + sp.I * eps) * sp.I / (a[0] + a[1] + 2 * sp.I * eps)   # cumulative (adiabatic) regulator
E21 = sp.I / (a[1] + sp.I * eps) * sp.I / (a[0] + a[1] + 2 * sp.I * eps)
Aeik = sp.I / (a[0] + sp.I * eps) * sp.I / (a[1] + sp.I * eps)
rngm = np.random.default_rng(3)
TA = rngm.normal(size=(3, 3)) + 1j * rngm.normal(size=(3, 3)); TB = rngm.normal(size=(3, 3)) + 1j * rngm.normal(size=(3, 3))
vals = {a[0]: 0.37, a[1]: -1.21, eps: 0.05}
e12, e21, aa = [complex(sp.N(x.subs(vals))) for x in (E12, E21, Aeik)]
lhs = TB @ TA * e12 + TA @ TB * e21
rhs = 0.5 * (TA @ TB + TB @ TA) * aa + 0.5 * (TB @ TA - TA @ TB) * (e12 - e21)
check('E4 non-abelian m=2: path order = 1/2{Ta,Tb} x abelian + 1/2[Tb,Ta](E12-E21) (exact, adiabatic eps)', np.allclose(lhs, rhs))

# ---------------- S1 finite light-like segment ----------------
kp, wm = sp.symbols('k_p w_m', real=True)
s_ = sp.Symbol('s', real=True)
# W^(1)[w,0] = i g int_0^1 ds w.A(s w), w.A = w^- A^+, k.(s w) = s k^+ w^-
W1 = sp.I * gsym * wm * sp.integrate(sp.exp(-sp.I * s_ * kp * wm), (s_, 0, 1))
W1 = sp.simplify(W1)
target = gsym * (1 - sp.exp(-sp.I * kp * wm)) / kp
check('S1 W^(1)[w,0] = g At^+ (1 - e^{-i k^+ w^-})/k^+', sp.simplify(sp.piecewise_fold(W1) - target) == 0 or
      sp.simplify((W1 - target).subs({kp: 0.37, wm: 2.1})) == 0, 'sympy: %s' % W1)
check('S1 removable pole: limit k^+ -> 0 equals i g w^-', sp.simplify(sp.limit(target, kp, 0) - sp.I * gsym * wm) == 0)
# limits with the adiabatic factor
z = sp.Symbol('z', real=True)
Wplus = sp.I * gsym * sp.integrate(sp.exp(-sp.I * kp * z - eps * z), (z, 0, sp.oo), conds='none')
Wminus = sp.I * gsym * (-sp.integrate(sp.exp(-sp.I * kp * z + eps * z), (z, -sp.oo, 0), conds='none'))
check('S1 w^- -> +inf (damped): g At^+/(k^+ - i eps) = W^(1)[inf n_B,0]', sp.simplify(Wplus - gsym / (kp - sp.I * eps)) == 0)
check('S1 w^- -> -inf (damped): g At^+/(k^+ + i eps) = W^(1)[-inf n_B,0]', sp.simplify(Wminus - gsym / (kp + sp.I * eps)) == 0)
# decompositions W[w,0] = W[w, inf n]W[inf n,0] = W[w,-inf n]W[-inf n,0] at first order (endpoint w: phase e^{-ik^+w^-})
via_future = gsym / (kp - sp.I * eps) + (-gsym / (kp - sp.I * eps)) * sp.exp(-sp.I * kp * wm)
via_past = gsym / (kp + sp.I * eps) + (-gsym / (kp + sp.I * eps)) * sp.exp(-sp.I * kp * wm)
check('S1 via +inf and via -inf both -> g At^+(1-e^{-ik^+w^-})/k^+ as eps -> 0',
      sp.simplify(sp.limit(via_future - target, eps, 0)) == 0 and sp.simplify(sp.limit(via_past - target, eps, 0)) == 0)
# the future-segment first-order term of W[w, inf n_B]: conjugate line with endpoint at w: vertex -ig, prop -i/(n.k - i0)
check('S1 W^(1)[w,inf n_B] = -g At^+ e^{-ik^+w^-}/(k^+ - i0) from the conjugate-line rule',
      sp.simplify((-sp.I * gsym) * (-sp.I) / (kp - sp.I * eps) + gsym / (kp - sp.I * eps)) == 0)

# ---------------- C1 covariance (numerical) ----------------
def su2_gens():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    return [s1 / 2, s2 / 2, s3 / 2]
def su3_gens():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return [x / 2 for x in l]
from scipy.linalg import expm
def structure_consts(T):
    n = len(T); f = np.zeros((n, n, n))
    for a_ in range(n):
        for b_ in range(n):
            com = T[a_] @ T[b_] - T[b_] @ T[a_]
            for c_ in range(n):
                f[a_, b_, c_] = (np.trace(com @ T[c_]) * 2 / 1j).real   # [t^a,t^b] = i f^{abc} t^c, Tr(t t)=1/2
    return f
def run_cov(T, gcoup=0.9, N=4000, seed=5):
    rng = np.random.default_rng(seed)
    n = len(T); dim = T[0].shape[0]
    # path z(s) in a 4D Minkowski space, s in [0,1]; components of A along the path: a(s) = zdot.A(z(s)) = sum_c a_c(s) T^c
    coef = rng.normal(size=(n, 3)); ph = rng.uniform(0, 2 * np.pi, size=(n, 3))
    def acomp(s):
        return np.array([sum(coef[c, j] * np.cos((j + 1) * 2.1 * s + ph[c, j]) for j in range(3)) for c in range(n)])
    cth = rng.normal(size=(n, 3)) * 0.7; pth = rng.uniform(0, 2 * np.pi, size=(n, 3))
    def theta(s):   # gauge function U(s) = exp(i theta^c(s) T^c)
        return np.array([sum(cth[c, j] * np.sin((j + 1) * 1.7 * s + pth[c, j]) for j in range(3)) for c in range(n)])
    def U(s):
        th = theta(s); return expm(1j * sum(th[c] * T[c] for c in range(n)))
    def dUds(s, h=1e-6):
        return (U(s + h) - U(s - h)) / (2 * h)
    ss = np.linspace(0, 1, N + 1); ds = 1 / N
    mid = 0.5 * (ss[:-1] + ss[1:])
    amat = [sum(acomp(s)[c] * T[c] for c in range(n)) for s in mid]
    # transformed connection along the path: zdot.A' = U zdot.A U^-1 - (i/g)(dU/ds) U^-1
    aprime = []
    for s, am in zip(mid, amat):
        Us = U(s); Ui = np.linalg.inv(Us)
        aprime.append(Us @ am @ Ui - (1j / gcoup) * dUds(s) @ Ui)
    def ordered(mats, later_left=True):
        W = np.eye(dim, dtype=complex)
        for am in mats:
            step = expm(1j * gcoup * am * ds)
            W = step @ W if later_left else W @ step
        return W
    W = ordered(amat); Wp = ordered(aprime)
    err_cov = np.max(np.abs(Wp - U(1.0) @ W @ np.linalg.inv(U(0.0))))
    V = ordered(amat, later_left=False); Vp = ordered(aprime, later_left=False)
    err_rev1 = np.max(np.abs(Vp - U(1.0) @ V @ np.linalg.inv(U(0.0))))
    err_rev2 = np.max(np.abs(Vp - np.linalg.inv(U(0.0)) @ V @ U(1.0)))
    # composition and retracing
    half = N // 2
    W1 = ordered(amat[:half]); W2 = ordered(amat[half:])
    err_comp = np.max(np.abs(W2 @ W1 - W))
    Wrev = ordered([-am for am in amat[::-1]])   # path reversed: zdot -> -zdot, order reversed
    err_retr = np.max(np.abs(Wrev @ W - np.eye(dim)))
    err_unit = np.max(np.abs(W.conj().T @ W - np.eye(dim)))
    # adjoint line: W^(A)_{ab} = 2 Tr[t^a W t^b W^dag] vs adjoint path-ordered exponential with (T^c)_{ab} = -i f^{cab}
    f = structure_consts(T)
    TA = [np.array([[-1j * f[c, a_, b_] for b_ in range(n)] for a_ in range(n)]) for c in range(n)]
    WA_def = np.array([[2 * np.trace(T[a_] @ W @ T[b_] @ W.conj().T) for b_ in range(n)] for a_ in range(n)])
    WA_po = np.eye(n, dtype=complex)
    for s in mid:
        ac = acomp(s); amA = sum(ac[c] * TA[c] for c in range(n))
        WA_po = expm(1j * gcoup * amA * ds) @ WA_po
    err_adj = np.max(np.abs(WA_def - WA_po))
    return err_cov, err_rev1, err_rev2, err_comp, err_retr, err_unit, err_adj
for name, T in (('SU(2)', su2_gens()), ('SU(3)', su3_gens())):
    ec, er1, er2, ecomp, eretr, eunit, eadj = run_cov(T)
    check('C1 %s covariance W -> U(b) W U^dag(a)' % name, ec < 1e-5, 'err=%.2e' % ec)
    check('C1 %s reversed ordering is not covariant (either law)' % name, min(er1, er2) > 1e-2, 'err=%.2e, %.2e' % (er1, er2))
    check('C1 %s composition W[c,b]W[b,a]=W[c,a], retracing, unitarity' % name, max(ecomp, eretr, eunit) < 1e-9,
          'errs=%.1e %.1e %.1e' % (ecomp, eretr, eunit))
    check('C1 %s adjoint line 2Tr[t^a W t^b W^dag] = adjoint P-exp with (T^c)_ab = -i f^cab' % name, eadj < 1e-5, 'err=%.2e' % eadj)

# ---------------- C2 infinitesimal gauge variation of the reversed ordering ----------------
def first_order_variation(T, gcoup=0.8, N=3000, seed=9, h=1e-6):
    rng = np.random.default_rng(seed); n = len(T); dim = T[0].shape[0]
    coef = rng.normal(size=(n, 2)); ph = rng.uniform(0, 6, size=(n, 2))
    cth = rng.normal(size=(n, 2)); pth = rng.uniform(0, 6, size=(n, 2))
    ss = np.linspace(0, 1, N + 1); mid = 0.5 * (ss[:-1] + ss[1:]); ds = 1 / N
    def a_of(s): return sum(sum(coef[c, j] * np.cos((j + 1) * 2 * s + ph[c, j]) for j in range(2)) * T[c] for c in range(n))
    def th_of(s): return sum(sum(cth[c, j] * np.sin((j + 1) * 1.3 * s + pth[c, j]) for j in range(2)) * T[c] for c in range(n))
    def dth(s, hh=1e-6): return (th_of(s + hh) - th_of(s - hh)) / (2 * hh)
    A = [a_of(s) for s in mid]
    dA = [(dth(s) - 1j * gcoup * (a_of(s) @ th_of(s) - th_of(s) @ a_of(s))) / gcoup for s in mid]   # delta a = (1/g)(d theta - i g [a,theta])
    def ordered(mats, later_left):
        W = np.eye(dim, dtype=complex)
        for am in mats:
            step = expm(1j * gcoup * am * ds); W = step @ W if later_left else W @ step
        return W
    W0 = ordered(A, True); W1 = ordered([x + h * y for x, y in zip(A, dA)], True)
    dW = (W1 - W0) / h
    pred = 1j * (th_of(1.0) @ W0 - W0 @ th_of(0.0))
    V0 = ordered(A, False); V1 = ordered([x + h * y for x, y in zip(A, dA)], False)
    dV = (V1 - V0) / h
    predV_naive = 1j * (V0 @ th_of(1.0) - th_of(0.0) @ V0)
    # extra term 2 g int ds V(s,a)[a,theta]V(b,s): V(s,a) = ordered(A[:i], False), V(b,s) = ordered(A[i:], False)
    extra = np.zeros((dim, dim), dtype=complex)
    pref = [np.eye(dim, dtype=complex)]
    for am in A:
        pref.append(pref[-1] @ expm(1j * gcoup * am * ds))
    suf = [np.eye(dim, dtype=complex)]
    for am in reversed(A):
        suf.append(expm(1j * gcoup * am * ds) @ suf[-1])
    suf = suf[::-1]
    for i, s in enumerate(mid):
        com = a_of(s) @ th_of(s) - th_of(s) @ a_of(s)
        extra += pref[i] @ com @ suf[i + 1] * ds
    predV = predV_naive + 2 * gcoup * extra
    return np.max(np.abs(dW - pred)), np.max(np.abs(dV - predV)), np.max(np.abs(2 * gcoup * extra))
e_W, e_V, sz_extra = first_order_variation(su2_gens())
check('C2 delta W = i(theta(b) W - W theta(a)) (path order, later left)', e_W < 1e-3, 'err=%.1e' % e_W)
check('C2 reversed order: delta V = i(V theta(b) - theta(a) V) + 2g int V[a,theta]V, extra term nonzero',
      e_V < 1e-3 and sz_extra > 1e-2, 'err=%.1e, |extra|=%.2f' % (e_V, sz_extra))
print('\nSUMMARY s2: %d/%d PASS' % (sum(PASS), len(PASS)))
