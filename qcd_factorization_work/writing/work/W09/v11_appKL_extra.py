"""W09 / v11: additional checks for the App K / App L texts (items not covered by v7, v8).
 (a) lem:appK-markov, elementary part: Chebyshev expansion coefficients satisfy |c_0| <= ||p||, |c_m| <= 2||p||;
     hence |a_k| <= c'_{N,k} ||p|| with c'_{N,k} = 2 sum_{m=k}^N |t_{m,k}| (and >= the sharp Markov constant);
     random tests; the table of sharp constants c_{N,k} for N = 4 (text example).
 (b) lem:appL-divided-differences: h_r(x_1..x_j) - h_r(x_0..x_{j-1}) = (x_j - x_0) h_{r-1}(x_0..x_j) (sympy);
     x^p[k_0..k_m] = h_{p-m}(k_0..k_m) for p <= 9, m <= 4 (sympy, distinct symbolic nodes);
     Hermite-Genocchi form of the path-ordered integral, i^m int_{0<s1<..<sm<w} e^{i k_m w - i sum q_j s_j}
     = e_w[k_0..k_m], for w > 0 AND w < 0 (oriented nested integrals), m = 1, 2, 3 (numerical quadrature);
     coinciding nodes (continuity): e_w[k,k] = i w e^{ikw}.
 (c) prop:appK-kernels (b): <D_k, z^{N-1}> = int_0^1 (z^{N-1}-1) ln^k(1-z)/(1-z) dz:
     exact generating function B(N,eta) - 1/eta; large-N form k! [eta^{k+1}] exp(-eta L + sum_{j>=2} (-1)^j zeta_j eta^j / j),
     L = ln N + gamma_E; leading term (-1)^{k+1} L^{k+1}/(k+1); remainder O(L^k/N) (k = 0..3).
 (d) rem:appK-counterexamples: |Q^2 int_0^1 x^n sin(Q^2 x) dx| <= 2 for n = 0..40 and Q^2 in [1, 1e6] (exact recursion
     from integration by parts, checked against quadrature); delta'(x) moments; Hilbert-matrix condition numbers
     (K = 5, 10, 20).
 (e) cor:appK-pdf: odd-moment difference of the explicit pair, 2/((N+1)(N+2)).
 (f) lem:appK-compact: Fourier-Laplace transform of a compactly supported distribution built from a function, a delta
     and a delta' term, equals its moment Taylor series (entire); a distribution with all moments zero gives 0.
 (g) prop:appL-bare (gluon sign bookkeeping): <[(D^+)^k G]_a [(D^+)^l G]_a> = -<[(D^+)^{k-1} G]_a [(D^+)^{l+1} G]_a>
     in forward matrix elements, so int xi^{n-1} f_g = (-i)^{n-2} M_g^{(n-2)}(0)/(P^+)^n = <G (iD^+)^{n-2} G>/(P^+)^n
     (abelian free-field model with a translation-invariant Gaussian state: total derivatives vanish).
"""
import sys, os, itertools, math, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# ---------------- (a) elementary Markov bound -----------------------------------------------------------
def cheb_poly_coeffs(m):
    c = np.polynomial.chebyshev.cheb2poly([0] * m + [1])
    out = np.zeros(m + 1); out[:len(c)] = c
    return out

def sharp(N, k):
    m = N if (N - k) % 2 == 0 else N - 1
    if m < k:
        return 0.0
    return abs(cheb_poly_coeffs(m)[k])

def elem(N, k):
    return 2.0 * sum(abs(cheb_poly_coeffs(m)[k]) for m in range(k, N + 1))

ok = True
for N in range(0, 13):
    for k in range(0, N + 1):
        if elem(N, k) + 1e-9 < sharp(N, k):
            ok = False
check('(a) elementary constant c\'_{N,k} = 2 sum_{m=k}^N |t_{m,k}| >= sharp Markov constant (N <= 12)', ok)

rng = np.random.default_rng(7)
th = np.linspace(0, np.pi, 20001)
ok_c = True; ok_a = True; worst = 0.0
for trial in range(400):
    N = int(rng.integers(1, 11))
    a = rng.normal(size=N + 1)
    p = np.polynomial.Polynomial(a)
    sup = np.max(np.abs(p(np.cos(th))))
    cheb = np.polynomial.chebyshev.poly2cheb(a)
    if abs(cheb[0]) > sup * (1 + 1e-6) or np.any(np.abs(cheb[1:]) > 2 * sup * (1 + 1e-6)):
        ok_c = False
    for k in range(N + 1):
        r = abs(a[k]) / (elem(N, k) * sup)
        worst = max(worst, r)
        if r > 1 + 1e-6:
            ok_a = False
check('(a) Chebyshev coefficients |c_0| <= sup|p|, |c_m| <= 2 sup|p| (400 random polynomials)', ok_c)
check('(a) |a_k| <= c\'_{N,k} sup|p| on [-1,1] (400 random polynomials; max ratio %.3f)' % worst, ok_a)
tab4 = [sharp(4, k) for k in range(5)]
check('(a) sharp constants for N = 4: (c_{4,0..4}) = (1, 3, 8, 4, 8): %s' % tab4, tab4 == [1.0, 3.0, 8.0, 4.0, 8.0])
check('(a) N = 4 elementary constants c\'_{4,k} = (6, 8, 20, 8, 16): %s' % [elem(4, k) for k in range(5)],
      [elem(4, k) for k in range(5)] == [6.0, 8.0, 20.0, 8.0, 16.0])
print('    elementary constants N=4:', [elem(4, k) for k in range(5)])

# ---------------- (b) divided differences ----------------------------------------------------------------
def hsym(r, xs):
    if r < 0:
        return sp.Integer(0)
    tot = sp.Integer(0)
    for comb in itertools.combinations_with_replacement(range(len(xs)), r):
        term = sp.Integer(1)
        for i in comb:
            term *= xs[i]
        tot += term
    return tot

X = sp.symbols('x0:6')
ok = True
for j in range(1, 5):
    for r in range(1, 6):
        lhs = hsym(r, X[1:j + 1]) - hsym(r, X[0:j])
        rhs = (X[j] - X[0]) * hsym(r - 1, X[0:j + 1])
        if sp.expand(lhs - rhs) != 0:
            ok = False
check('(b) h_r(x_1..x_j) - h_r(x_0..x_{j-1}) = (x_j - x_0) h_{r-1}(x_0..x_j)  (j <= 4, r <= 5)', ok)

def divdiff(f, nodes):
    if len(nodes) == 1:
        return f(nodes[0])
    return sp.simplify((divdiff(f, nodes[1:]) - divdiff(f, nodes[:-1])) / (nodes[-1] - nodes[0]))

ok = True
for m in range(0, 5):
    nodes = list(X[:m + 1])
    for p in range(0, 10):
        dd = sp.factor(divdiff(lambda t: t ** p, nodes))
        if sp.expand(dd - hsym(p - m, nodes)) != 0:
            ok = False
check('(b) x^p[k_0..k_m] = h_{p-m}(k_0..k_m) for m <= 4, p <= 9 (zero for p < m)', ok)

mp.mp.dps = 30
def e_dd(w, kap):
    """divided difference of x -> e^{i x w} at distinct nodes kap."""
    s = mp.mpc(0)
    for j, kj in enumerate(kap):
        den = mp.mpf(1)
        for l, kl in enumerate(kap):
            if l != j:
                den *= (kj - kl)
        s += mp.e ** (1j * kj * w) / den
    return s

def nested(w, kap):
    """i^m int_0^w ds_m int_0^{s_m} ds_{m-1} ... int_0^{s_2} ds_1 exp(i k_m w - i sum q_j s_j) (oriented)."""
    m = len(kap) - 1
    q = [kap[j] - kap[j - 1] for j in range(1, m + 1)]
    def inner(level, upper):
        # integrate s_level from 0 to upper of exp(-i q_level s) * inner(level-1, s)
        if level == 0:
            return mp.mpf(1)
        return mp.quad(lambda s: mp.e ** (-1j * q[level - 1] * s) * inner(level - 1, s), [0, upper])
    return (1j) ** m * mp.e ** (1j * kap[-1] * w) * inner(m, w)

ok = True; worst = 0
for m in (1, 2, 3):
    for w in (mp.mpf('1.7'), mp.mpf('-1.3')):
        kap = [mp.mpf('0.3'), mp.mpf('1.1'), mp.mpf('-0.4'), mp.mpf('2.2')][:m + 1]
        a = nested(w, kap); b = e_dd(w, kap)
        worst = max(worst, abs(a - b))
        if abs(a - b) > mp.mpf('1e-12'):
            ok = False
check('(b) Hermite-Genocchi: i^m nested int = e_w[k_0..k_m] for m = 1,2,3 and w = 1.7, -1.3 (max dev %.1e)' % float(worst), ok)
# coinciding nodes: e_w[k,k] = d/dk e^{ikw} = i w e^{ikw}
k0 = mp.mpf('0.8'); w = mp.mpf('1.9')
lim = e_dd(w, [k0, k0 + mp.mpf('1e-12')])
check('(b) coinciding nodes: e_w[k,k] = i w e^{ikw} (limit)', abs(lim - 1j * w * mp.e ** (1j * k0 * w)) < 1e-9)
# moment of (1/2) delta(x - xi P+) divided difference: int xi^{n-1} (1/2) delta(x - xi P) dxi = x^{n-1}/(2 P^n)
xs = sp.symbols('x', positive=True); Pp = sp.symbols('P', positive=True); xi = sp.symbols('xi')
nn = 5
mom = sp.integrate(xi ** (nn - 1) * sp.Rational(1, 2) * sp.DiracDelta(xs - xi * Pp), (xi, -sp.oo, sp.oo))
check('(b) int dxi xi^{n-1} (1/2) delta(x - xi P^+) = x^{n-1}/(2 (P^+)^n)  (n = 5)', sp.simplify(mom - xs ** (nn - 1) / (2 * Pp ** nn)) == 0)

# ---------------- (c) moments of D_k ----------------------------------------------------------------------
mp.mp.dps = 40
def Dk_moment_exact(k, N):
    # k! [eta^k] (B(N,eta) - 1/eta)
    f = lambda eta: mp.beta(N, eta) - 1 / eta
    return mp.diff(f, mp.mpf(0), k, method='step', h=mp.mpf('1e-6')) if False else None

def Dk_moment_quad(k, N):
    return mp.quad(lambda z: (z ** (N - 1) - 1) * mp.log(1 - z) ** k / (1 - z), [0, 1])

def Dk_moment_taylor(k, N):
    # coefficients of B(N, eta) - 1/eta in eta via mpmath taylor of the regular function
    g = lambda eta: mp.beta(N, eta) - 1 / eta if eta != 0 else mp.mpf(0)
    # regularized: use series of Gamma functions: B(N,eta) - 1/eta = (Gamma(N)Gamma(1+eta)/Gamma(N+eta) - 1)/eta
    h = lambda eta: (mp.gamma(N) * mp.gamma(1 + eta) / mp.gamma(N + eta) - 1)
    c = mp.taylor(h, 0, k + 1)
    return mp.factorial(k) * c[k + 1]

def Dk_asym(k, N):
    L = mp.log(N) + mp.euler
    # k! [eta^{k+1}] exp(-eta L + sum_{j>=2} (-1)^j zeta_j eta^j / j)
    def E(eta):
        s = -eta * L
        for j in range(2, k + 3):
            s += (-1) ** j * mp.zeta(j) * eta ** j / j
        return mp.e ** s
    c = mp.taylor(E, 0, k + 1)
    return mp.factorial(k) * c[k + 1]

ok_ex = True; ok_as = True; ok_lead = True
for k in range(0, 4):
    for N in (5, 12):
        a = Dk_moment_quad(k, N); b = Dk_moment_taylor(k, N)
        if abs(a - b) > mp.mpf('1e-15') * (1 + abs(a)):
            ok_ex = False
    rem = []
    for N in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
        ex = Dk_moment_taylor(k, N); asy = Dk_asym(k, N)
        L = mp.log(N) + mp.euler
        rem.append(abs(ex - asy) * N / max(1, L ** k))
        lead = (-1) ** (k + 1) * L ** (k + 1) / (k + 1)
        # the leading term dominates: (asy - lead)/L^{k+1} -> 0
    # remainder * N / L^k bounded
    if not all(r < 10 for r in rem):
        ok_as = False
    N = 10 ** 8; L = mp.log(N) + mp.euler
    if abs(Dk_asym(k, N) / ((-1) ** (k + 1) * L ** (k + 1) / (k + 1)) - 1) > 0.05 * (k + 1):
        ok_lead = False
    print('    k=%d: remainder*N/L^k = %s' % (k, [mp.nstr(r, 4) for r in rem]))
check('(c) <D_k, z^{N-1}> = k! [eta^{k+1}] Gamma(N)Gamma(1+eta)/Gamma(N+eta) (quadrature, k <= 3, N = 5, 12)', ok_ex)
check('(c) <D_k, z^{N-1}> = k! [eta^{k+1}] exp(-eta L + sum_j (-1)^j zeta_j eta^j/j) + O(L^k/N), L = ln N + gamma_E', ok_as)
check('(c) leading term (-1)^{k+1} L^{k+1}/(k+1) dominates at N = 1e8 (k <= 3)', ok_lead)
# explicit low k: k=0: -L + O(1/N); k=1: (L^2 + zeta2)/2
N = 10 ** 6; L = mp.log(N) + mp.euler
check('(c) k=0: <D_0, z^{N-1}> = -S_1(N-1) -> -(ln N + gamma_E)', abs(Dk_moment_taylor(0, N) + (mp.harmonic(N - 1))) < 1e-20 and abs(Dk_asym(0, N) + L) < 1e-30)
check('(c) k=1: asymptotic form (L^2 + zeta_2)/2', abs(Dk_asym(1, N) - (L ** 2 + mp.zeta(2)) / 2) < 1e-25)

# ---------------- (d) counterexamples ---------------------------------------------------------------------
mp.mp.dps = 30
def moment_sin(n, a):
    """I_n(a) = int_0^1 x^n sin(a x) dx via the integration-by-parts recursion with J_n = int x^n cos.
    The forward recursion amplifies round-off by ~ n!/a^n when n > a, so it is run with 250 digits."""
    olddps = mp.mp.dps; mp.mp.dps = 250
    a = mp.mpf(a)
    # I_0 = (1 - cos a)/a, J_0 = sin a / a; I_n = -cos a / a + (n/a) J_{n-1}; J_n = sin a / a - (n/a) I_{n-1}
    I = (1 - mp.cos(a)) / a; J = mp.sin(a) / a
    out = [I]
    for m in range(1, n + 1):
        I, J = -mp.cos(a) / a + (m / a) * J, mp.sin(a) / a - (m / a) * I
        out.append(I)
    mp.mp.dps = olddps
    return [+v for v in out]

ok_rec = True
for a in (mp.mpf(3), mp.mpf(50)):
    rec = moment_sin(6, a)
    for nn in range(7):
        qd = mp.quad(lambda x: x ** nn * mp.sin(a * x), mp.linspace(0, 1, 40))
        if abs(qd - rec[nn]) > 1e-15:
            ok_rec = False
check('(d) integration-by-parts recursion for int_0^1 x^n sin(a x) agrees with quadrature', ok_rec)
ok = True; worst = 0
for a in [mp.mpf(10) ** e for e in (0, 0.5, 1, 1.5, 2, 3, 4, 5, 6)] + [mp.mpf(7), mp.mpf(31.4), mp.mpf(1234.5)]:
    vals = moment_sin(40, a)
    for nn, v in enumerate(vals):
        worst = max(worst, abs(a * v))
        if abs(a * v) > 2 + 1e-20:
            ok = False
check('(d) |Q^2 int_0^1 x^n sin(Q^2 x) dx| <= 2 for n <= 40, Q^2 in [1, 1e6] (max %.4f)' % float(worst), ok)
# delta'(x): <delta', x^m> = -m 0^{m-1}
check('(d) delta\'(x): <delta\', x^{2k}> = 0 (k >= 0), <delta\', x> = -1', all((-(2 * k) * (0 ** (2 * k - 1) if 2 * k - 1 >= 0 else 0)) == 0 for k in range(8)))
for K in (5, 10, 20):
    H = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            H[i, j] = mp.mpf(1) / (i + j + 1)
    mp.mp.dps = 80
    ev = mp.eigsy(H)[0]
    cond = max(ev) / min(ev)
    print('    cond_2(H_%d) = %s' % (K, mp.nstr(cond, 6)))
    if K == 10:
        check('(d) cond_2(H_10) = 1.6025e13', abs(cond / mp.mpf('1.6025e13') - 1) < 1e-3)
    mp.mp.dps = 30

# ---------------- (e) explicit pair ------------------------------------------------------------------------
x = sp.symbols('x', positive=True)
ok = True
for N in range(1, 12):
    d = sp.integrate(x ** (N - 1) * 2 * x * (1 - x), (x, 0, 1))
    if sp.simplify(d - sp.Rational(2, (N + 1) * (N + 2))) != 0:
        ok = False
check('(e) odd-moment difference of the pair (q + x(1-x), qbar - x(1-x)): 2/((N+1)(N+2))', ok)

# ---------------- (f) compact support: Fourier-Laplace = moment series -------------------------------------
mp.mp.dps = 30
# T = f(xi) dxi on [-1,1] + c1 delta(xi - 0.4) + c2 delta'(xi + 0.2)
f = lambda s: (1 - s * s) ** 2 * (1 + s / 3)
c1, c2 = mp.mpf('0.7'), mp.mpf('-0.25')
def moment(m):
    val = mp.quad(lambda s: s ** m * f(s), [-1, 1]) + c1 * mp.mpf('0.4') ** m
    # <delta'(xi - b), phi> = -phi'(b) with b = -0.2
    val += c2 * (-(m * mp.mpf('-0.2') ** (m - 1) if m >= 1 else 0))
    return val
def FL(t):
    val = mp.quad(lambda s: mp.e ** (-1j * t * s) * f(s), [-1, 1]) + c1 * mp.e ** (-1j * t * mp.mpf('0.4'))
    val += c2 * (-(-1j * t) * mp.e ** (-1j * t * mp.mpf('-0.2')))
    return val
t = mp.mpf('2.3') + 0.7j
series = sum(((-1j * t) ** m / mp.factorial(m)) * moment(m) for m in range(0, 70))
check('(f) Fourier-Laplace transform of a compactly supported distribution = sum_m (-i t)^m/m! <T, xi^m> (t = 2.3+0.7i)', abs(series - FL(t)) < 1e-20)

# ---------------- (g) gluon moment bookkeeping (free abelian Gaussian model) -------------------------------
# In a translation-invariant state, <X(w) Y(0)> depends on w only; derivatives: d/dw <X(w)Y(0)> = <X'(w) Y(0)>,
# and <X'(0)Y(0)> = -<X(0)Y'(0)> (total derivative). Model: M_g(w) = int dxi e^{i xi P w} (P^2 xi f_g(xi)) with f_g odd.
P = mp.mpf('1.7')
fg = lambda s: s * (1 - s * s) ** 3 * (2 + s * s)          # odd test distribution on [-1,1] (xi f_g even)
Mg = lambda w: P ** 2 * mp.quad(lambda s: mp.e ** (1j * s * P * w) * s * fg(s), [-1, 1])
ok = True
for n in range(2, 8):
    lhs = mp.quad(lambda s: s ** (n - 1) * fg(s), [-1, 1])
    der = mp.diff(Mg, 0, n - 2)
    rhs = (-1j) ** (n - 2) * der / P ** n
    if abs(lhs - rhs) > 1e-12:
        ok = False
check('(g) int xi^{n-1} f_g = (-i)^{n-2} M_g^{(n-2)}(0)/(P^+)^n for n = 2..7 (odd f_g)', ok)

print('\nSUMMARY v11: %d PASS, %d FAIL' % (npass, nfail))
