"""W09 / v7: App K (moment problems, continuation, entire functions, Markov inequality, counterexamples).
 (a) lem:appK-markov: for every N <= 9 and k <= N, max |a_k| over real polynomials of degree <= N with |p| <= 1 on [-1,1]
     (linear programme on a fine grid incl. the Chebyshev extrema) = |t_{N,k}| (N-k even) or |t_{N-1,k}| (N-k odd);
     the maximiser is T_N resp. T_{N-1}; complex version: extra factor sqrt(2) bound holds;
 (b) lem:appK-entire: J(y) = (1/2pi) int log|y + 2 sin th| d th = log max(1, (|y| + sqrt(y^2-4))/2) >= 0 (= sum log max(1,|w_k|));
     the roots of w^2 + i y w - 1; the bound |f(z)| <= C (3+|z|)^A on an example;
 (c) thm:appK-carlson sharpness: sin(pi z) (type pi), sin(pi z/2) vanishes on even integers with |sin(pi(2+iy)/2)| = sinh(pi|y|/2);
     sin^2(pi z/2) = (1-cos pi z)/2 has type pi;
 (d) prop:appK-continuation: zeros at z_k = z0 + k d -> w_k = (x_k-1)/(x_k+1), sum (1-|w_k|) = sum 2/(x_k+1) diverges;
     Jensen's formula numerically for a Blaschke-type example;
 (e) VF-MISC-2: cond_2 of the K x K Hilbert (moment Gram) matrix: 4.8e5 (K=5), 2.5e28 (K=20), ~ e^{3.5K};
 (f) thm:appK-muntz: L^2 distance formula via Gram determinants (Cauchy matrix); dist(x, span{x^{k^2+1}}) = pi/sinh(sqrt3 pi);
 (g) rem:appK-counterexamples: delta'(x) has vanishing even moments; Q^2 * moments of sin(Q^2 x) bounded while sup = 1;
 (h) cor:appK-pdf: explicit pair with equal even and different odd moments; prop:appK-kernels: recovery of a, b from large N;
 (i) thm:appK-even-moments: substitution t = x^2 check.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.optimize import linprog

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

# ---------------- (a) Markov coefficient inequality ---------------------------------------------------
def cheb_coeffs(m):
    c = np.polynomial.chebyshev.cheb2poly([0] * m + [1])
    out = np.zeros(m + 1); out[:len(c)] = c
    return out
grid = np.unique(np.concatenate([np.cos(np.pi * np.arange(0, 4001) / 4000), np.linspace(-1, 1, 4001)]))
for N in range(1, 10):
    V = np.vander(grid, N + 1, increasing=True)
    for k in range(0, N + 1):
        c = np.zeros(N + 1); c[k] = -1.0             # maximise a_k
        A_ub = np.vstack([V, -V]); b_ub = np.ones(2 * len(grid))
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * (N + 1), method='highs')
        best = -res.fun
        m = N if (N - k) % 2 == 0 else N - 1
        tk = abs(cheb_coeffs(m)[k]) if k <= m else 0.0
        ok = abs(best - tk) < 2e-3 * max(1, tk)
        check('(a) N=%d k=%d: max a_k = %.5f vs |t_{%d,%d}| = %.5f' % (N, k, best, m, k, tk), ok)
# complex coefficients on the imaginary segment: |h(iy)| <= 1 for |y| <= 1 => |h_k| <= sqrt2 c_{N,k}
rng = np.random.default_rng(11)
worst = 0
for trial in range(200):
    N = rng.integers(2, 8)
    coef = rng.normal(size=N + 1) + 1j * rng.normal(size=N + 1)
    ys = np.linspace(-1, 1, 2001)
    vals = np.array([sum(coef[j] * (1j * y) ** j for j in range(N + 1)) for y in ys])
    coef = coef / np.max(np.abs(vals))
    for k in range(N + 1):
        m = N if (N - k) % 2 == 0 else N - 1
        bound = np.sqrt(2) * abs(cheb_coeffs(m)[k]) if k <= m else 0
        if bound > 0:
            worst = max(worst, abs(coef[k]) / bound)
check('(a) complex version: |h_k| <= sqrt2 c_{N,k} on 200 random polynomials (max ratio %.3f)' % worst, worst <= 1 + 1e-6)

# ---------------- (b) entire functions: J(y) --------------------------------------------------------------
for y in (0.0, 0.7, 1.99, 2.0, 2.5, 7.3, -4.0):
    pts = [mp.mpf(0), mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]
    if abs(y) <= 2:   # interior logarithmic singularities where sin th = -y/2: use them as break points
        t1 = mp.asin(-mp.mpf(y) / 2)
        for tt in (t1 % (2 * mp.pi), (mp.pi - t1) % (2 * mp.pi)):
            pts.append(tt)
    pts = sorted(set([mp.mpf(x) for x in pts]))
    J = mp.quad(lambda t: mp.log(abs(y + 2 * mp.sin(t))) if abs(y + 2 * mp.sin(t)) > 0 else mp.mpf(0), pts) / (2 * mp.pi)
    closed = mp.log(max(1, (abs(y) + mp.sqrt(max(0, y * y - 4))) / 2))
    roots = np.roots([1, 1j * y, -1])
    jensen = sum(np.log(max(1, abs(r))) for r in roots)
    check('(b) y=%.2f: J(y) = %.10f = log max(1,(|y|+sqrt(y^2-4))/2) = %.10f = Jensen %.10f >= 0'
          % (y, J, closed, jensen), abs(J - closed) < 1e-8 and abs(closed - jensen) < 1e-8 and J > -1e-10)
# |y + 2 sin th| = |w^2 + i y w - 1| on |w| = 1
th = 0.83; y = 1.37; w = np.exp(1j * th)
check('(b) |y + 2 sin th| = |w^2 + i y w - 1| for w = e^{i th}', abs(abs(y + 2 * np.sin(th)) - abs(w * w + 1j * y * w - 1)) < 1e-13)
# example: f(z) = (z^2+1) satisfies |f| <= C(1+|z|)^2 |Im z|^0; subharmonic bound log|f(z)| <= mean over circle radius 2
f = lambda z: z * z + 1
for z0 in (0.3 + 0.0j, 2.0 + 0.1j, -5 + 3j):
    mean = mp.quad(lambda t: mp.log(abs(f(z0 + 2 * mp.e ** (1j * t)))), [0, 2 * mp.pi]) / (2 * mp.pi)
    check('(b) subharmonic mean inequality log|f(z0)| <= mean_{|z-z0|=2} log|f| at z0=%s' % z0, mp.log(abs(f(z0))) <= mean + 1e-12)

# ---------------- (c) Carlson sharpness ------------------------------------------------------------------
for yv in (0.5, 3.0, 10.0):
    v = abs(mp.sin(mp.pi * (2 + 1j * yv) / 2))
    check('(c) |sin(pi(2+iy)/2)| = sinh(pi|y|/2) at y=%.1f' % yv, abs(v - mp.sinh(mp.pi * yv / 2)) < 1e-20 * max(1, v))
check('(c) sin(pi z/2) = 0 at even integers', all(abs(mp.sin(mp.pi * k / 2)) < 1e-12 for k in range(0, 20, 2)))
# type of sin^2(pi z/2) on the imaginary axis: log|.|/|y| -> pi
yv = mp.mpf(40)
check('(c) sin^2(pi z/2) has type pi along i R: log|sin^2(pi i y/2)|/y = %.4f -> pi' % (mp.log(abs(mp.sin(mp.pi * 1j * yv / 2) ** 2)) / yv),
      abs(mp.log(abs(mp.sin(mp.pi * 1j * yv / 2) ** 2)) / yv - mp.pi) < 0.05)

# ---------------- (d) continuation: Blaschke divergence ----------------------------------------------------
xs = [2 * k for k in range(1, 20001)]
partial = sum(2 / (x + 1) for x in xs)
check('(d) zeros at even integers: sum_k (1-|w_k|) = sum 2/(2k+1) ~ ln K diverges (K=20000: %.3f vs ln K = %.3f)' % (partial, np.log(20000)),
      abs(partial - (np.log(20000) + np.euler_gamma + 2 * np.log(2) - 2)) < 0.01)
# Jensen's formula check for Phi(w) = (w - 0.3)(w + 0.5i) on r = 0.9
Phi = lambda w: (w - 0.3) * (w + 0.5j)
r = 0.9
lhs = np.log(abs(Phi(0)))
rhs = np.log(0.3 / r) + np.log(0.5 / r) + float(mp.quad(lambda t: mp.log(abs(Phi(r * mp.e ** (1j * t)))), [0, 2 * mp.pi])) / (2 * np.pi)
check('(d) Jensen formula log|Phi(0)| = sum log(|w_k|/r) + mean log|Phi| (%.10f vs %.10f)' % (lhs, rhs), abs(lhs - rhs) < 1e-10)

# ---------------- (e) Hilbert matrix condition numbers ------------------------------------------------------
mp.mp.dps = 80
def cond_hilbert(K):
    H = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            H[i, j] = mp.mpf(1) / (i + j + 1)
    ev = mp.eigsy(H)[0]
    evs = [ev[i] for i in range(K)]
    return max(evs) / min(evs)
c5, c20 = cond_hilbert(5), cond_hilbert(20)
check('(e) cond_2(H_5) = %.3e (VF-MISC-2: 4.8e5)' % c5, abs(c5 / mp.mpf('4.8e5') - 1) < 0.02)
check('(e) cond_2(H_20) = %.3e (VF-MISC-2: 2.5e28)' % c20, abs(c20 / mp.mpf('2.5e28') - 1) < 0.05)
check('(e) growth ~ e^{3.5K}: log(cond(H_20)/cond(H_5))/15 = %.3f' % (mp.log(c20 / c5) / 15), abs(mp.log(c20 / c5) / 15 - 3.5) < 0.1)
mp.mp.dps = 30

# ---------------- (f) Muntz-Szasz distance formula --------------------------------------------------------
def gram(exps):
    return mp.matrix([[mp.mpf(1) / (a + b + 1) for b in exps] for a in exps])
lam = mp.mpf('1.0'); lks = [mp.mpf(2), mp.mpf(4), mp.mpf('5.5'), mp.mpf(9)]
d2 = mp.det(gram([lam] + lks)) / mp.det(gram(lks))
formula = (1 / mp.sqrt(2 * lam + 1)) * mp.fprod([abs(lam - lk) / (lam + lk + 1) for lk in lks])
check('(f) dist^2 = det G(lam,lk)/det G(lk) equals the squared product formula (%.12e vs %.12e)' % (d2, formula ** 2), abs(d2 - formula ** 2) < 1e-25)
prod = mp.nprod(lambda k: k ** 2 / (k ** 2 + 3), [1, mp.inf]) / mp.sqrt(3)
check('(f) dist(x, span{x^{k^2+1}}) = (1/sqrt3) prod k^2/(k^2+3) = pi/sinh(sqrt3 pi) = %.6f' % prod,
      abs(prod - mp.pi / mp.sinh(mp.sqrt(3) * mp.pi)) < 1e-15)

# ---------------- (g) counterexamples ------------------------------------------------------------------------
xsym = sp.symbols('x')
k_ = sp.symbols('k', integer=True, nonnegative=True)
ok = all(sp.diff(xsym ** (2 * kk), xsym).subs(xsym, 0) == 0 for kk in range(0, 8))
check("(g) delta'(x): int x^{2k} delta'(x) dx = -(d/dx x^{2k})(0) = 0 for k = 0..7", ok)
check("(g) delta'(x): first moment int x delta' = -1 (not zero), so it is not the zero distribution", -sp.diff(xsym, xsym).subs(xsym, 0) == -1)
# exact recursion: I_n = int_0^1 x^n sin(a x), J_n = int_0^1 x^n cos(a x):
#   I_0 = (1-cos a)/a, J_0 = sin a/a, I_n = -cos a/a + (n/a) J_{n-1}, J_n = sin a/a - (n/a) I_{n-1}
# integration by parts gives |a I_n| <= 2 for all n >= 0 and all a > 0 (uniform bound c_n = 2), while sup|sin(a x)| = 1
def IJ(a, nmax):
    a = mp.mpf(a); I = [(1 - mp.cos(a)) / a]; J = [mp.sin(a) / a]
    for n in range(1, nmax + 1):
        I.append(-mp.cos(a) / a + n / a * J[n - 1]); J.append(mp.sin(a) / a - n / a * I[n - 1])
    return I, J
I, J = IJ(37, 3)
check('(g) recursion vs quadrature at a = 37, n = 3', abs(I[3] - mp.quad(lambda x: x ** 3 * mp.sin(37 * x), mp.linspace(0, 1, 30))) < 1e-15)
for Q2 in (10, 100, 1000, 10 ** 4, 10 ** 6):
    I, J = IJ(Q2, 8)
    vals = [Q2 * I[n] for n in range(0, 9)]
    check('(g) Q^2=%d: max_n<=8 |Q^2 int x^n sin(Q^2 x)| = %.4f <= 2, sup|sin(Q^2 x)| = 1' % (Q2, max(abs(v) for v in vals)),
          all(abs(v) <= 2 + 1e-12 for v in vals))

# ---------------- (h) explicit pair; kernel recovery ----------------------------------------------------------
q = lambda x: 3 * (1 - x) ** 2; qb = lambda x: (1 - x) ** 3; hfun = lambda x: x * (1 - x)
q2 = lambda x: q(x) + hfun(x); qb2 = lambda x: qb(x) - hfun(x) + x ** 2 * (1 - x) ** 2 * 0
def moment_fq(qq, qqb, n):   # int_{-1}^1 xi^{n-1} f_q = int_0^1 x^{n-1} [q + (-1)^n qbar]
    return mp.quad(lambda x: x ** (n - 1) * (qq(x) + (-1) ** n * qqb(x)), [0, 1])
evens = all(abs(moment_fq(q, qb, n) - moment_fq(q2, qb2, n)) < 1e-20 for n in (2, 4, 6, 8))
odds = all(abs(moment_fq(q, qb, n) - moment_fq(q2, qb2, n)) > 1e-3 for n in (1, 3, 5))
check('(h) pair (q, qbar) and (q + x(1-x), qbar - x(1-x)): equal even moments, different odd moments', evens and odds)
# kernel recovery from large-N behaviour: M(N) = int x^{N-1} r - a(psi(N)+gE) + b ; P_qq/C_F: a = 2, b = 3/2, r = -(1+x)
def MP(N):
    return mp.quad(lambda x: x ** (N - 1) * (-(1 + x)), [0, 1]) - 2 * (mp.psi(0, N) + mp.euler) + mp.mpf(3) / 2
for N in (2, 4, 10):
    gqq = mp.mpf(3) / 2 + mp.mpf(1) / (N * (N + 1)) - 2 * (mp.psi(0, N + 1) + mp.euler)
    check('(h) Mellin of (1+x^2)[1/(1-x)]_+ + 3/2 delta at N=%d equals gamma_qq/C_F' % N, abs(MP(N) - gqq) < 1e-20)
Nbig = mp.mpf(10) ** 6
a_rec = -(MP(2 * Nbig) - MP(Nbig)) / mp.log(2)
b_rec = MP(Nbig) + a_rec * (mp.log(Nbig) + mp.euler)
check('(h) large-N recovery: a = %.5f (2), b = %.5f (3/2)' % (a_rec, b_rec), abs(a_rec - 2) < 1e-4 and abs(b_rec - 1.5) < 1e-4)

# ---------------- (i) substitution t = x^2 -------------------------------------------------------------------
g = lambda x: x ** (-1.5) * (1 - x) ** 0.3          # x^{2k0} g in L^1 for k0 = 1
k0 = 1
for m_ in range(0, 4):
    lhs = mp.quad(lambda t: t ** m_ * 0.5 * t ** (k0 - 0.5) * g(mp.sqrt(t)), [0, 1])
    rhs = mp.quad(lambda x: x ** (2 * (m_ + k0)) * g(x), [0, 1])
    check('(i) int t^m h(t) dt = int x^{2(m+k0)} g dx with h(t) = t^{k0-1/2} g(sqrt t)/2 (m=%d)' % m_, abs(lhs - rhs) < 1e-12)

print('\nSUMMARY v7: %d PASS, %d FAIL' % (npass, nfail))
