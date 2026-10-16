r"""
s4_wilson.py  (writer W05; App B prop:appB-rules, lem:appB-shuffle, lem:appB-wilson-ward, prop:appB-webs,
Ch5 prop:sudakov-webs(b); Ch3 prop:prelim-wilson-covariance (proof in App B); VF-WL-1/2/3/4/13)

Conventions: W[b,a] = P exp(i g Int_a^b dz.A), later points to the left; A(x) = Int dk/(2pi)^4 e^{-ik.x} Atilde(k)
(k flows INTO the line); adiabatic damping e^{-eps |lambda|} on semi-infinite lines.
 (a) iterated integrals -> nested eikonal denominators (symbolic, m<=3, all four line types);
 (b) path-ordered exponential solved as an ODE in an SU(3) plane-wave background vs. the momentum-space rules
     (sum of terms up to g^4; residual ~ g^5);
 (c) future minus past: 1/(x-i0) - 1/(x+i0) = 2 pi i delta(x) (test function);
 (d) gauge covariance of the ODE solution (finite gauge transformation, SU(3), numerically);
 (e) shuffle/eikonal identity: symbolic m<=4, exact rationals (complex) m=5..7, finite-eps cumulative regulator,
     uniform-regulator defect for m=2 and its pairing with 1/((1+a1^2)(1+a2^2)) = pi^2 eps/((1+eps)^2(2+eps));
     general shuffle product of two ordered sequences (p,q<=3);
 (f) Ward identity of a semi-infinite Wilson line (VF-WL-13), SU(3) random matrices, finite eps;
 (g) O(g^2) non-abelian exponentiation: W2 - W1^2/2 = 1/4 sum [T_s,T_r](E(r,s)-E(s,r)) (VF-WL-3);
 (h) two-loop cusp colour factors: uncrossed C_F^2, crossed C_F(C_F - C_A/2); web colour factor -C_F C_A/2.
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, numpy as np, mpmath as mp
from fractions import Fraction
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# ---------------------------------------------------------------- (a) iterated integrals
e = sp.Symbol('epsilon', positive=True)
lam = sp.symbols('l1:5', real=True)
aa = sp.symbols('a1:5', real=True)      # a_j = n.k_j
def past_iter(m):
    """Int_{-inf<l1<...<lm<0} prod_j exp(-i l_j (a_j + i e))  done innermost-first (l1 first)"""
    expr = 1
    cur = sp.Integer(0)  # accumulated exponent coefficient
    res = sp.Integer(1)
    # analytic induction: Int_{-inf}^{l_{j+1}} dl_j exp(-i l_j (A_j + i j e)) = i/(A_j + i j e) exp(-i l_{j+1}(A_j + i j e))
    for j in range(1, m + 1):
        Aj = sum(aa[:j])
        integrand = sp.exp(-sp.I * lam[j - 1] * (Aj + sp.I * j * e))
        upper = lam[j] if j < m else 0
        val = sp.integrate(integrand, (lam[j - 1], -sp.oo, upper), conds='none')
        # val = i/(Aj + i j e) * exp(-i upper (Aj + i j e))
        res *= sp.simplify(val * sp.exp(sp.I * upper * (Aj + sp.I * j * e)))
    return sp.simplify(res)
for m in [1, 2, 3]:
    lhs = past_iter(m)
    rhs = sp.prod([sp.I / (sum(aa[:j]) + sp.I * j * e) for j in range(1, m + 1)])
    check('(a) past-pointing line, m=%d: nested denominators i/(n.(k1+..+kj) + i j eps)' % m, sp.simplify(lhs - rhs) == 0)
def future_iter(m):
    res = sp.Integer(1)
    for j in range(m, 0, -1):            # do l_m first: Int_{l_{j-1}}^{inf}
        Aj = sum(aa[j - 1:m])
        c = m - j + 1
        integrand = sp.exp(-sp.I * lam[j - 1] * (Aj - sp.I * c * e))
        lower = lam[j - 2] if j > 1 else 0
        val = sp.integrate(integrand, (lam[j - 1], lower, sp.oo), conds='none')
        res *= sp.simplify(val * sp.exp(sp.I * lower * (Aj - sp.I * c * e)))
    return sp.simplify(res)
for m in [1, 2, 3]:
    lhs = future_iter(m)
    rhs = sp.prod([-sp.I / (sum(aa[j - 1:m]) - sp.I * (m - j + 1) * e) for j in range(1, m + 1)])
    check('(a) future-pointing line, m=%d: -i/(n.(kj+..+km) - i(m-j+1)eps)' % m, sp.simplify(lhs - rhs) == 0)

def pastc_iter(m):
    """W[-inf n,0]: path 0 -> -inf (orientation -n), gluon 1 nearest 0 (points lambda_1 > ... > lambda_m, lambda<0)"""
    res = sp.Integer(1)
    for j in range(m, 0, -1):            # innermost: lambda_m in (-inf, lambda_{m-1})
        Aj = sum(aa[j - 1:m]); c = m - j + 1
        upper = lam[j - 2] if j > 1 else 0
        val = sp.integrate(sp.exp(-sp.I * lam[j - 1] * (Aj + sp.I * c * e)), (lam[j - 1], -sp.oo, upper), conds='none')
        res *= sp.simplify(val * sp.exp(sp.I * upper * (Aj + sp.I * c * e)))
    return sp.simplify((-1) ** m * res)  # each dz = -n dlambda
for m in [1, 2, 3]:
    lhs = pastc_iter(m)
    rhs = sp.prod([sp.I / (sum(aa[j - 1:m]) + sp.I * (m - j + 1) * e) for j in range(1, m + 1)]) * (-1) ** m
    check('(a) conjugate line W[-inf n,0], m=%d: (-1)^m prod_j i/(n.(k_j+..+k_m) + i(m-j+1)eps)  [vertex -i g t n]' % m, sp.simplify(lhs - rhs) == 0)
def futc_iter(m):
    """W[0,inf n]: path inf -> 0 (orientation -n), gluon 1 nearest +inf (lambda_1 > lambda_2 > ... > lambda_m > 0)"""
    res = sp.Integer(1)
    for j in range(1, m + 1):            # lambda_1 innermost: (lambda_2, inf)
        Aj = sum(aa[:j]); c = j
        lower = lam[j] if j < m else 0
        val = sp.integrate(sp.exp(-sp.I * lam[j - 1] * (Aj - sp.I * c * e)), (lam[j - 1], lower, sp.oo), conds='none')
        res *= sp.simplify(val * sp.exp(sp.I * lower * (Aj - sp.I * c * e)))
    return sp.simplify((-1) ** m * res)
for m in [1, 2, 3]:
    lhs = futc_iter(m)
    rhs = sp.prod([-sp.I / (sum(aa[:j]) - sp.I * j * e) for j in range(1, m + 1)]) * (-1) ** m
    check('(a) conjugate line W[0,inf n], m=%d: (-1)^m prod_j (-i)/(n.(k_1+..+k_j) - i j eps)  [vertex -i g t n]' % m, sp.simplify(lhs - rhs) == 0)
# one-gluon terms of all four lines (coefficient of g n.Atilde)
one = {}
l = sp.Symbol('l', real=True); a1 = aa[0]
one['W[inf n,0]'] = sp.I * sp.integrate(sp.exp(-sp.I * l * (a1 - sp.I * e)), (l, 0, sp.oo), conds='none')
one['W[-inf n,0]'] = sp.I * (-1) * sp.integrate(sp.exp(-sp.I * l * (a1 + sp.I * e)), (l, -sp.oo, 0), conds='none')   # path 0 -> -inf
one['W[0,-inf n]'] = sp.I * sp.integrate(sp.exp(-sp.I * l * (a1 + sp.I * e)), (l, -sp.oo, 0), conds='none')
one['W[0,inf n]'] = sp.I * (-1) * sp.integrate(sp.exp(-sp.I * l * (a1 - sp.I * e)), (l, 0, sp.oo), conds='none')     # path inf -> 0
ref = {'W[inf n,0]': 1 / (a1 - sp.I * e), 'W[-inf n,0]': 1 / (a1 + sp.I * e), 'W[0,-inf n]': -1 / (a1 + sp.I * e), 'W[0,inf n]': -1 / (a1 - sp.I * e)}
for k in one:
    check('(a) one-gluon term of %s = %s' % (k, ref[k]), sp.simplify(one[k] - ref[k]) == 0)

# ---------------------------------------------------------------- SU(3) generators
lam8 = np.zeros((8, 3, 3), dtype=complex)
lam8[0][0, 1] = lam8[0][1, 0] = 1
lam8[1][0, 1] = -1j; lam8[1][1, 0] = 1j
lam8[2][0, 0] = 1; lam8[2][1, 1] = -1
lam8[3][0, 2] = lam8[3][2, 0] = 1
lam8[4][0, 2] = -1j; lam8[4][2, 0] = 1j
lam8[5][1, 2] = lam8[5][2, 1] = 1
lam8[6][1, 2] = -1j; lam8[6][2, 1] = 1j
lam8[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam8 / 2
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- (b) ODE solution vs rules (past-pointing line)
# background along the line z = lambda n:  n.A(lambda n) = sum_r M_r exp(-i lambda a_r) ,  M_r = random su(3)-matrix
R = 3
Mr = [sum(rng.normal() * T[a] for a in range(8)) for _ in range(R)]
ar = rng.uniform(-1.5, 1.5, size=R)
epsv = 0.35
def nA(lmb):   # with adiabatic damping e^{eps lambda} (lambda<0)
    return sum(Mr[r] * np.exp(-1j * lmb * ar[r]) for r in range(R)) * np.exp(epsv * lmb)
def W_ode(g, L=60.0, N=60000):
    # dW/dlambda = i g nA(lambda) W, W(-L)=1, integrate to 0 (RK4)
    h = L / N; Wm = np.eye(3, dtype=complex); lm = -L
    f = lambda lm_, W_: 1j * g * nA(lm_) @ W_
    for _ in range(N):
        k1 = f(lm, Wm); k2 = f(lm + h / 2, Wm + h / 2 * k1); k3 = f(lm + h / 2, Wm + h / 2 * k2); k4 = f(lm + h, Wm + h * k3)
        Wm = Wm + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); lm += h
    return Wm
def W_rules(g, mmax=4):
    tot = np.eye(3, dtype=complex)
    for m in range(1, mmax + 1):
        for seq in itertools.product(range(R), repeat=m):     # seq[0] nearest -inf
            col = np.eye(3, dtype=complex)
            for r in seq:
                col = Mr[r] @ col                               # later (closer to 0) to the left
            den = 1.0 + 0j
            for j in range(1, m + 1):
                den *= 1j / (sum(ar[s] for s in seq[:j]) + 1j * j * epsv)
            tot = tot + (1j * g) ** m * col * den
    return tot
res = []
for g in [0.02, 0.04]:
    d = np.abs(W_ode(g) - W_rules(g)).max()
    res.append(d)
check('(b) ODE path-ordered exponential = momentum-space rules through g^4: residual small and scaling like g^5 (ratio ~ 2^5 when g doubles)',
      res[0] < 1e-6 and 26 < res[1] / res[0] < 38, ['%.2e' % r for r in res] + ['ratio %.2f' % (res[1] / res[0])])

# ---------------------------------------------------------------- (c) future minus past
f_test = lambda xx: mp.exp(-xx ** 2) * (1 + xx / 3)
for eta in [mp.mpf('1e-3'), mp.mpf('1e-4')]:
    val = mp.quad(lambda xx: f_test(xx) * (1 / (xx - 1j * eta) - 1 / (xx + 1j * eta)), [-mp.inf, -1, 0, 1, mp.inf])
    check('(c) Int f(x)[1/(x-i eta)-1/(x+i eta)] -> 2 pi i f(0)  (eta=%s)' % mp.nstr(eta, 1), abs(val - 2j * mp.pi * f_test(0)) < 10 * eta, complex(val))

# ---------------------------------------------------------------- (d) gauge covariance along a finite path
# path z(s), s in [0,1]; A_s(s) := zdot.A(z(s)) random smooth su(3)-valued function; U(s) = exp(i theta(s)) random
def rand_su3_fun(nmodes=3):
    coef = [(sum(rng.normal() * T[a] for a in range(8)), rng.normal(), rng.normal()) for _ in range(nmodes)]
    return lambda s: sum(C * (np.cos(w * s + ph)) for (C, w, ph) in coef)
As = rand_su3_fun(); Th = rand_su3_fun()
from scipy.linalg import expm
def U(s): return expm(1j * Th(s))
def dU(s, h=1e-6): return (U(s + h) - U(s - h)) / (2 * h)
gq = 0.8
def solve(Afun, N=4000):
    h = 1.0 / N; Wm = np.eye(3, dtype=complex); s = 0.0
    f = lambda s_, W_: 1j * gq * Afun(s_) @ W_
    for _ in range(N):
        k1 = f(s, Wm); k2 = f(s + h / 2, Wm + h / 2 * k1); k3 = f(s + h / 2, Wm + h / 2 * k2); k4 = f(s + h, Wm + h * k3)
        Wm = Wm + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); s += h
    return Wm
Aprime = lambda s: U(s) @ As(s) @ np.linalg.inv(U(s)) - (1j / gq) * dU(s) @ np.linalg.inv(U(s))
W0 = solve(As); W1 = solve(Aprime)
check('(d) W[b,a] -> U(b) W U^dagger(a) under A -> U A U^-1 - (i/g)(dU)U^-1  (D = d - i g A)',
      np.abs(W1 - U(1.0) @ W0 @ U(0.0).conj().T).max() < 1e-7, np.abs(W1 - U(1.0) @ W0 @ U(0.0).conj().T).max())
Aprime_wrong = lambda s: U(s) @ As(s) @ np.linalg.inv(U(s)) + (1j / gq) * dU(s) @ np.linalg.inv(U(s))
W2 = solve(Aprime_wrong)
check('(d) negative control: the opposite sign of the inhomogeneous term is not covariant', np.abs(W2 - U(1.0) @ W0 @ U(0.0).conj().T).max() > 1e-3)
check('(d) unitarity W^dagger W = 1 (hermitian A)', np.abs(W0.conj().T @ W0 - np.eye(3)).max() < 1e-9)

# ---------------------------------------------------------------- (e) shuffle / eikonal identity
ys = sp.symbols('y1:5')
def lhs_sym(vals):
    m = len(vals); tot = 0
    for perm in itertools.permutations(range(m)):
        term = 1
        for j in range(1, m + 1):
            term *= 1 / sum(vals[perm[i]] for i in range(j))
        tot += term
    return tot
for m in [2, 3, 4]:
    check('(e) shuffle identity, symbolic m=%d' % m, sp.simplify(sp.together(lhs_sym(list(ys[:m])) - sp.prod([1 / y for y in ys[:m]]))) == 0)
random.seed(11)
def rand_gauss_rat():
    return sp.Rational(random.randint(-50, 50), random.randint(1, 30)) + sp.I * sp.Rational(random.randint(-50, 50), random.randint(1, 30))
for m in [5, 6, 7]:
    ok = True
    for trial in range(2):
        while True:
            vals = [rand_gauss_rat() for _ in range(m)]
            if all(sum(vals[i] for i in S) != 0 for r in range(1, m + 1) for S in itertools.combinations(range(m), r)):
                break
        ok &= sp.simplify(lhs_sym(vals) - sp.prod([1 / v for v in vals])) == 0
    check('(e) shuffle identity, exact complex rationals, m=%d' % m, ok)
# finite eps: y_j = a_j + i eps  <=> cumulative denominators + i j eps
m = 3
cum = lhs_sym([aa[j] + sp.I * e for j in range(m)])
check('(e) y_j = n.k_j + i eps gives exactly the cumulative regulator (+ i j eps) and the identity holds', sp.simplify(cum - sp.prod([1 / (aa[j] + sp.I * e) for j in range(m)])) == 0)
unif = 1 / (aa[0] + sp.I * e) / (aa[0] + aa[1] + sp.I * e) + 1 / (aa[1] + sp.I * e) / (aa[0] + aa[1] + sp.I * e)
defect = sp.simplify(unif - 1 / ((aa[0] + sp.I * e) * (aa[1] + sp.I * e)))
check('(e) uniform +i eps, m=2: Prod - Sum = -i eps/[(a1+i eps)(a2+i eps)(a1+a2+i eps)]  (the N26 defect; Sum - Prod = +i eps/[...])',
      sp.simplify(-defect - (-sp.I * e / ((aa[0] + sp.I * e) * (aa[1] + sp.I * e) * (aa[0] + aa[1] + sp.I * e)))) == 0)
# pairing of the defect (Prod - Sum) with 1/((1+a1^2)(1+a2^2)): residues (close in the upper half planes) give
#   int da1 1/((a1+ie)(a1+a2+ie)(1+a1^2)) = -i pi/((1+e)(a2+i(1+e))) ; then int da2 ... = -pi/((2+e)(1+e))
#   => pairing of Sum - Prod = -pi^2 e/((1+e)^2(2+e)), of Prod - Sum = +pi^2 e/((1+e)^2(2+e))
a1s, a2s = sp.symbols('a1s a2s', real=True); es = sp.Symbol('es', positive=True)
inner = sp.residue(1 / ((a1s + sp.I * es) * (a1s + a2s + sp.I * es) * (1 + a1s ** 2)), a1s, sp.I) * 2 * sp.pi * sp.I
check('(e) residue step: int da1 1/((a1+ie)(a1+a2+ie)(1+a1^2)) = -i pi/((1+e)(a2+i(1+e)))',
      sp.simplify(inner - (-sp.I * sp.pi / ((1 + es) * (a2s + sp.I * (1 + es))))) == 0)
outer = sp.residue(inner / ((a2s + sp.I * es) * (1 + a2s ** 2)), a2s, sp.I) * 2 * sp.pi * sp.I
pairing_sum_minus_prod = sp.simplify(sp.I * es * outer)
check('(e) pairing of (Prod - Sum) with 1/((1+a1^2)(1+a2^2)) = +pi^2 e/((1+e)^2(2+e)) (residues)',
      sp.simplify(-pairing_sum_minus_prod - sp.pi ** 2 * es / ((1 + es) ** 2 * (2 + es))) == 0)
for ev in [mp.mpf('0.3'), mp.mpf('0.1')]:
    f2 = lambda x1, x2: (-1j * ev / ((x1 + 1j * ev) * (x2 + 1j * ev) * (x1 + x2 + 1j * ev))) / ((1 + x1 ** 2) * (1 + x2 ** 2))
    pts = [-mp.inf, -10, -3, -1, -0.3, -0.1, 0, 0.1, 0.3, 1, 3, 10, mp.inf]
    pair = mp.quad(lambda x1: mp.quad(lambda x2: f2(x1, x2), pts), pts)
    refp = mp.pi ** 2 * ev / ((1 + ev) ** 2 * (2 + ev))
    check('(e) numerical pairing (Prod - Sum) = pi^2 e/((1+e)^2(2+e)), e=%s' % mp.nstr(ev, 2), abs(pair - refp) < 1e-6 * refp, (complex(pair), float(refp)))
# general shuffle product of two ordered sequences
def Eword(vals):
    r = 1
    for j in range(1, len(vals) + 1):
        r *= 1 / sum(vals[:j])
    return r
def shuffles(A, B):
    if not A: yield list(B); return
    if not B: yield list(A); return
    for s in shuffles(A[1:], B): yield [A[0]] + s
    for s in shuffles(A, B[1:]): yield [B[0]] + s
ks = sp.symbols('k1:4'); ls_ = sp.symbols('m1:4')
ok = True
for p in range(1, 4):
    for q in range(1, 4):
        A, B = list(ks[:p]), list(ls_[:q])
        ok &= sp.simplify(sum(Eword(s) for s in shuffles(A, B)) - Eword(A) * Eword(B)) == 0
check('(e) shuffle product: sum over shuffles of E = E(k_1..k_p) E(l_1..l_q), p,q<=3', ok)

# ---------------------------------------------------------------- (f) Ward identity of W[0,-inf n]
def ward_check(m, eps_v, nonabelian=True):
    ks_ = rng.uniform(-2, 2, size=m); q_ = rng.uniform(-2, 2)
    if nonabelian:
        Ts = [sum(rng.normal() * T[a] for a in range(8)) for _ in range(m)]
        Tq = sum(rng.normal() * T[a] for a in range(8))
    else:
        Ts = [np.eye(3) * rng.normal() for _ in range(m)]; Tq = np.eye(3) * rng.normal()
    g = 0.7
    def props(moms):     # moms in path order (nearest -inf first); cumulative with i j eps
        r = 1 + 0j; c = 0.0
        for j, kk in enumerate(moms, start=1):
            c += kk; r *= 1j / (c + 1j * j * eps_v)
        return r
    def colour(seq):
        Cm = np.eye(3, dtype=complex)
        for X in seq: Cm = X @ Cm
        return Cm
    total = np.zeros((3, 3), dtype=complex)
    for p in range(m + 1):
        moms = list(ks_[:p]) + [q_] + list(ks_[p:])
        seq = Ts[:p] + [Tq] + Ts[p:]
        total += (1j * g) ** (m + 1) * (q_ + 1j * eps_v) * colour(seq) * props(moms)   # polarization n.q -> n.q + i eps
    Y = (1j * g) ** m * colour(Ts) * props(list(ks_))
    rhs = -g * Tq @ Y
    def props_shift(moms, p):   # chain where gluon p+1 carries k_{p+1}+q: segments j>p have regulator (j+1) eps
        r = 1 + 0j; c = 0.0
        for j, kk in enumerate(moms, start=1):
            c += kk; r *= 1j / (c + 1j * (j + (1 if j > p else 0)) * eps_v)
        return r
    for p in range(m):
        moms = list(ks_); moms[p] = moms[p] + q_          # gluon p+1 carries k_{p+1}+q
        Zp = (1j * g) ** m * props_shift(moms, p)
        seq_left = Ts[p + 1:]; seq_right = Ts[:p]
        comm = Tq @ Ts[p] - Ts[p] @ Tq
        rhs += g * Zp * colour(seq_left) @ comm @ colour(seq_right)
    return np.abs(total - rhs).max()
for m in [1, 2, 3, 4]:
    check('(f) Wilson-line Ward identity, SU(3), m=%d, finite eps (VF-WL-13)' % m, ward_check(m, 0.3) < 1e-12, '%.1e' % ward_check(m, 0.3))
check('(f) abelian case: sum = -g Y', ward_check(3, 0.2, nonabelian=False) < 1e-12)

# ---------------------------------------------------------------- (g) O(g^2) exponentiation / webs
Rm = 3
Tr_ = [sum(rng.normal() * T[a] for a in range(8)) for _ in range(Rm)]
kr = rng.uniform(-2, 2, size=Rm); ev = 0.4
E1 = lambda r: 1j / (kr[r] + 1j * ev)
E2 = lambda r, s: 1j / (kr[r] + 1j * ev) * 1j / (kr[r] + kr[s] + 2j * ev)
W1 = sum(Tr_[r] * E1(r) for r in range(Rm))
W2 = sum(Tr_[s] @ Tr_[r] * E2(r, s) for r in range(Rm) for s in range(Rm))
web = sum(0.25 * (Tr_[s] @ Tr_[r] - Tr_[r] @ Tr_[s]) * (E2(r, s) - E2(s, r)) for r in range(Rm) for s in range(Rm))
check('(g) W^(2) - (W^(1))^2/2 = 1/4 sum_{r,s} [T_s,T_r](E(r,s)-E(s,r))  exactly at finite eps (VF-WL-3)', np.abs(W2 - 0.5 * W1 @ W1 - web).max() < 1e-12)
check('(g) the O(g^2) part of ln W is traceless (in the span of the generators)', abs(np.trace(W2 - 0.5 * W1 @ W1)) < 1e-12)
Wab1 = sum(np.eye(3) * rng.normal() * E1(r) for r in range(Rm))
# abelian: commuting colour factors -> W2 = W1^2/2
cs = [rng.normal() for _ in range(Rm)]
W1a = sum(cs[r] * E1(r) for r in range(Rm)); W2a = sum(cs[s] * cs[r] * E2(r, s) for r in range(Rm) for s in range(Rm))
check('(g) abelian: W^(2) = (W^(1))^2/2 exactly at finite eps', abs(W2a - 0.5 * W1a ** 2) < 1e-12)

# ---------------------------------------------------------------- (h) two-loop cusp colour factors
CF = 4 / 3; CA = 3
unc = sum(np.trace(T[a] @ T[b] @ T[b] @ T[a]) for a in range(8) for b in range(8)) / 3
crs = sum(np.trace(T[a] @ T[b] @ T[a] @ T[b]) for a in range(8) for b in range(8)) / 3
check('(h) uncrossed ladder colour factor = C_F^2', abs(unc - CF ** 2) < 1e-12, unc.real)
check('(h) crossed ladder colour factor = C_F(C_F - C_A/2)', abs(crs - CF * (CF - CA / 2)) < 1e-12, crs.real)
check('(h) web colour factor of the crossed ladder = -C_F C_A/2', abs((crs - unc) - (-CF * CA / 2)) < 1e-12, (crs - unc).real)

print('\n=== s4_wilson (v2): %d/%d PASS ===' % (sum(PASS), len(PASS)))
