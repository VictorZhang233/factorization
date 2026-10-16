"""
s6_uniqueness.py -- item (6): uniqueness of a function from its even moments; Muntz-Szasz; Carlson-type continuation.

 (a) substitution t = x^2:  int_0^1 x^{2k} g(x) dx = int_0^1 t^{k-1} h(t) dt,  h(t) = sqrt(t) g(sqrt t)/2,
     int_0^1 |h| dt = int_0^1 x^2 |g| dx  (so h in L^1 whenever x^2 g in L^1)
 (b) constructive illustration: h (hence g) recovered in L^2 from the even moments alone (shifted-Legendre
     expansion, exact rational arithmetic); Parseval error -> 0
 (c) ill-posedness: condition number of the Hilbert (moment Gram) matrix grows exponentially
 (d) Muntz-Szasz in L^2[0,1] made explicit: dist(x^lam, span{x^lam_k}) = (2lam+1)^{-1/2} prod |lam-lam_k|/(lam+lam_k+1)
     (Gram/Cauchy determinant, verified exactly); -> 0 for lam_k = 2k (sum 1/lam_k = oo), stays > 0 for
     lam_k = k^2+1 (sum 1/lam_k < oo)
 (e) Jensen's formula (numerical check) and divergence of the Blaschke sum for zeros at the even integers
 (f) Carlson sharpness: sin(pi N/2) vanishes at all even N and has exponential type exactly pi/2 along Im N;
     Mellin transforms of L^1 functions are bounded on Re N >= N0 (cannot differ by such a term)
 (g) LO DGLAP kernels: a kernel r(x) + a[1/(1-x)]_+ + b delta(1-x) with |r| <= C/x is fixed by its even moments
 (h) even moments of f_q on [-1,1] fix q + qbar only; odd moments fix q - qbar
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from fractions import Fraction as Fr
from math import comb
import sympy as sp
import mpmath as mp

results = []


def report(name, ok, detail=''):
    results.append((name, bool(ok)))
    print('%-86s %s %s' % (name, 'PASS' if ok else 'FAIL', detail), flush=True)


x, tt = sp.symbols('x t', positive=True)

# ---------------------------------------------------------------- (a) substitution identity
# one exact case (sympy) + three cases at 40 digits (mpmath tanh-sinh quadrature; integrable endpoint singularities)
g_ex = (1 - x) ** 3 * (1 + 2 * x)
h_ex = sp.sqrt(tt) * g_ex.subs(x, sp.sqrt(tt)) / 2
ok = all(sp.simplify(sp.integrate(sp.expand(x ** (2 * kk) * g_ex), (x, 0, 1))
                     - sp.integrate(sp.expand(tt ** (kk - 1) * h_ex), (tt, 0, 1))) == 0 for kk in range(1, 5))
mp.mp.dps = 40
gs = [lambda u: u ** mp.mpf(-0.5) * (1 - u) ** 3 * (1 + 2 * u), lambda u: u ** mp.mpf('0.3') * (1 - u) ** 5,
      lambda u: mp.log(1 / u) * (1 - u) / u ** mp.mpf('0.9')]
for gf in gs:
    hf = lambda s_, gf=gf: mp.sqrt(s_) * gf(mp.sqrt(s_)) / 2
    for kk in range(1, 5):
        lhs = mp.quad(lambda u: u ** (2 * kk) * gf(u), [0, 1])
        rhs = mp.quad(lambda s_: s_ ** (kk - 1) * hf(s_), [0, 1])
        ok &= abs(lhs - rhs) < mp.mpf(10) ** (-30) * abs(lhs)
    n1 = mp.quad(lambda s_: abs(hf(s_)), [0, 1])
    n2 = mp.quad(lambda u: u * u * abs(gf(u)), [0, 1])
    ok &= abs(n1 - n2) < mp.mpf(10) ** (-30) * n2
mp.mp.dps = 30
report('(a) int x^{2k} g = int t^{k-1} h(t), h = sqrt(t) g(sqrt t)/2;  ||h||_1 = ||x^2 g||_1 (4 test g, k=1..4)', ok)


# ---------------------------------------------------------------- (b) reconstruction from even moments (exact)
# g(x) = x^{1/2}(1-x)^3(1+4x);  m_k = int x^{2k} g = B(2k+3/2,4) + 4 B(2k+5/2,4),  B(a,4) = 6/(a(a+1)(a+2)(a+3))
def B4(a):
    return Fr(6) / (a * (a + 1) * (a + 2) * (a + 3))


def m_even(kk):
    a = Fr(4 * kk + 3, 2)
    return B4(a) + 4 * B4(a + 1)


# check m_k against sympy integration
okm = all(sp.Rational(m_even(kk).numerator, m_even(kk).denominator) ==
          sp.integrate(x ** (2 * kk) * sp.sqrt(x) * (1 - x) ** 3 * (1 + 4 * x), (x, 0, 1)) for kk in (1, 2, 5))
mu = [m_even(m + 1) for m in range(60)]                 # mu_m = int t^m h(t) dt = m_{m+1}
# ||h||^2 = (1/2) int x^3 g^2 = (1/2) int x^4 (1-x)^6 (1+4x)^2
hnorm2 = Fr(sp.Rational(sp.integrate(x ** 4 * (1 - x) ** 6 * (1 + 4 * x) ** 2, (x, 0, 1)) / 2).p,
            sp.Rational(sp.integrate(x ** 4 * (1 - x) ** 6 * (1 + 4 * x) ** 2, (x, 0, 1)) / 2).q)
errs = {}
acc = Fr(0)
for j in range(48):
    cj = (2 * j + 1) * sum(((-1) ** (j + m)) * comb(j, m) * comb(j + m, m) * mu[m] for m in range(j + 1))
    acc += cj * cj / (2 * j + 1)
    if j + 1 in (2, 4, 8, 16, 32, 48):
        errs[j + 1] = float(hnorm2 - acc) ** 0.5 / float(hnorm2) ** 0.5
mono = all(errs[a] >= errs[b] for a, b in zip(sorted(errs)[:-1], sorted(errs)[1:]))
report('(b) exact even moments of g = x^{1/2}(1-x)^3(1+4x) reproduce sympy integrals', okm)
report('(b) L^2 recovery of h from even moments: relative Parseval error -> 0 (K=2..48 Legendre terms)',
       mono and errs[48] < 2e-3, '; '.join('K=%d: %.1e' % (k_, v) for k_, v in sorted(errs.items())))

# ---------------------------------------------------------------- (c) ill-posedness: Hilbert matrix condition numbers
mp.mp.dps = 120
conds = {}
for K in (5, 10, 15, 20):
    H = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            H[i, j] = mp.mpf(1) / (i + j + 1)
    ev = mp.eigsy(H)[0]
    conds[K] = max(ev) / min(ev)
rate = float(mp.log(conds[20] / conds[10]) / 10)
report('(c) cond_2 of the KxK moment Gram (Hilbert) matrix grows ~ e^{3.5 K}: uniqueness, not stability',
       3.0 < rate < 3.8, ' '.join('K=%d:%.1e' % (k_, float(v)) for k_, v in conds.items()) + '  rate=%.2f' % rate)
mp.mp.dps = 30


# ---------------------------------------------------------------- (d) Muntz-Szasz in L^2: exact distance formula
def gram(lams):
    return sp.Matrix(len(lams), len(lams), lambda i, j: sp.Rational(1) / (lams[i] + lams[j] + 1))


okd = True
for lam, lks in [(sp.Integer(1), [2, 4, 6, 8, 10]), (sp.Rational(1, 2), [1, 3, 7]), (sp.Integer(1), [2, 5, 10, 17])]:
    for K in range(1, len(lks) + 1):
        L = [sp.Integer(v) for v in lks[:K]]
        d2 = gram([lam] + L).det() / gram(L).det()
        formula = sp.Rational(1) / (2 * lam + 1)
        for lk in L:
            formula *= (lam - lk) ** 2 / (lam + lk + 1) ** 2
        okd &= sp.simplify(d2 - formula) == 0
report('(d) dist^2(x^lam, span{x^lam_k}) = Gram-det ratio = (2lam+1)^{-1} prod (lam-lam_k)^2/(lam+lam_k+1)^2', okd)


def dist(lam, lks):
    v = mp.mpf(1) / mp.sqrt(2 * lam + 1)
    for lk in lks:
        v *= abs(lam - lk) / (lam + lk + 1)
    return v


d_even = {K: dist(1, [2 * k for k in range(1, K + 1)]) for K in (10, 100, 1000, 10000)}
d_sq = {K: dist(1, [k * k + 1 for k in range(1, K + 1)]) for K in (10, 100, 1000, 10000)}
# d_even ~ c K^{-3/2}
slope = float(mp.log(d_even[10000] / d_even[1000]) / mp.log(10))
report('(d) x^1 vs even powers x^{2k} (sum 1/lam_k = oo): dist -> 0 ~ K^{-3/2}', abs(slope + 1.5) < 0.01,
       ' '.join('K=%d:%.2e' % (k_, float(v)) for k_, v in d_even.items()) + ' slope=%.3f' % slope)
# exact limit: (1/sqrt3) prod_k k^2/(k^2+3) = (1/sqrt3) * pi sqrt3 / sinh(pi sqrt3) = pi / sinh(sqrt3 pi)   (Euler product for sinh)
d_inf = mp.pi / mp.sinh(mp.sqrt(3) * mp.pi)
report('(d) x^1 vs x^{k^2+1} (sum 1/lam_k < oo): dist -> pi/sinh(sqrt3 pi) = 0.02722 > 0 (no density)',
       all(0 < d_sq[K] - d_inf < 4 * d_inf / K for K in d_sq),
       ' '.join('K=%d:%.6f' % (k_, float(v)) for k_, v in d_sq.items()) + ' limit=%.6f' % float(d_inf))

# ---------------------------------------------------------------- (e) Jensen's formula & Blaschke divergence
f = lambda w: (w - mp.mpf('0.3')) * (w + mp.mpc(0, '0.5')) * (w - mp.mpc('0.9', '0.2')) * mp.exp(w + w * w / 3)
r = mp.mpf('0.8')
lhs = mp.log(abs(f(0)))
zeros_in = [mp.mpf('0.3'), mp.mpc(0, '-0.5')]
rhs = sum(mp.log(abs(a) / r) for a in zeros_in) + mp.quad(lambda th: mp.log(abs(f(r * mp.exp(1j * th)))), [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi)
report('(e) Jensen: log|f(0)| = sum_{|a|<r} log(|a|/r) + (1/2pi) int log|f(re^{i th})| d th (test f, r=0.8)',
       abs(lhs - rhs) < 1e-20, 'diff=%.1e' % float(abs(lhs - rhs)))
part = {K: sum(2.0 / (2 * k + 1) for k in range(1, K + 1)) for K in (10, 1000, 100000)}
report('(e) zeros z_k = 2k mapped by w=(z-1)/(z+1): sum (1-|w_k|) = sum 2/(2k+1) diverges (~ ln K)',
       part[100000] - part[1000] > 4.5, ' '.join('K=%d:%.2f' % (k_, v) for k_, v in part.items()))

# ---------------------------------------------------------------- (f) Carlson sharpness & boundedness of Mellin transforms
ok = True
for y in (1, 5, 20, 40):
    val = abs(mp.sin(mp.pi * (2 + 1j * y) / 2))
    ok &= abs(val - mp.sinh(mp.pi * y / 2)) < 1e-20 * val
typ = float(mp.log(abs(mp.sin(mp.pi * (2 + 80j) / 2))) / 80)
report('(f) |sin(pi N/2)| on N = 2+iy equals sinh(pi|y|/2): zeros at all even N, type exactly pi/2', ok and abs(typ - mp.pi / 2) < 0.01,
       'type(y=80)=%.4f' % typ)


def mellin_g(N):
    a = N + mp.mpf(1) / 2
    return mp.beta(a, 4) + 4 * mp.beta(a + 1, 4)


Ms = [abs(mellin_g(3 + 1j * y)) for y in (0, 2, 10, 50, 200)]
report('(f) Mellin transform of g bounded on Re N = 3: |M(3+iy)| <= M(3), decaying in |y|',
       all(Ms[i] >= Ms[i + 1] for i in range(len(Ms) - 1)) and abs(Ms[0] - mellin_g(3)) < 1e-25,
       ' '.join('%.2e' % float(v) for v in Ms))
# exact even-moment agreement of g's Mellin transform with m_even
report('(f) M(2k+1) = m_k (even powers x^{2k}) for k=1..6', all(abs(mellin_g(2 * k_ + 1) - mp.mpf(m_even(k_).numerator) / m_even(k_).denominator) < 1e-25 for k_ in range(1, 7)))

# ---------------------------------------------------------------- (g) LO kernels determined by even moments
# moments of D = r(x) + a[1/(1-x)]_+ + b delta(1-x):  M_D(N) = int x^{N-1} r - a (psi(N)+gamma_E) + b
# For P_qq/C_F: r = -(1+x), a = 2, b = 3/2
ok = True
for N in (2, 4, 6, 10):
    lhs_ = -sp.integrate(x ** (N - 1) * (1 + x), (x, 0, 1)) - 2 * (sp.harmonic(N - 1)) + sp.Rational(3, 2)
    rhs_ = sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * sp.harmonic(N)
    ok &= sp.simplify(lhs_ - rhs_) == 0
report('(g) decomposition r + a[1/(1-x)]_+ + b delta: P_qq/C_F (r=-(1+x), a=2, b=3/2) moments reproduce gamma_qq', ok)
# the ln N growth isolates a; then b from the constant; then r from the remaining even moments
Nbig = mp.mpf(10) ** 8
gq = lambda N: 1.5 + 1 / (N * (N + 1)) - 2 * (mp.digamma(N + 1) + mp.euler)
a_est = -(gq(Nbig) - gq(Nbig / 10)) / mp.log(10)
b_est = gq(Nbig) + a_est * (mp.digamma(Nbig) + mp.euler)
report('(g) recover a = 2, b = 3/2 from the large-N behaviour of the even moments of P_qq/C_F',
       abs(a_est - 2) < 1e-6 and abs(b_est - 1.5) < 1e-6, 'a=%.8f b=%.8f' % (float(a_est), float(b_est)))

# ---------------------------------------------------------------- (h) even vs odd moments: q + qbar vs q - qbar
xi = sp.Symbol('xi', real=True)
q1, qb1 = (1 - x) ** 3, x * (1 - x) ** 5
d_ = x ** 2 * (1 - x) ** 2
q2, qb2 = q1 + d_, qb1 + d_       # same q - qbar? no: same q + qbar requires qb2 = qb1 - d ; here we test both
q3, qb3 = q1 + d_, qb1 - d_       # same q + qbar, different q - qbar


def mom(q_, qb_, N):
    # int_{-1}^1 xi^{N-1} f_q(xi), f_q(xi) = q(xi) (xi>0), -qbar(-xi) (xi<0)
    return sp.integrate(x ** (N - 1) * q_, (x, 0, 1)) + sp.integrate(xi ** (N - 1) * (-(qb_.subs(x, -xi))), (xi, -1, 0))


ok_even = all(sp.simplify(mom(q1, qb1, N) - mom(q3, qb3, N)) == 0 for N in (2, 4, 6))
ok_odd = all(sp.simplify(mom(q1, qb1, N) - mom(q3, qb3, N)) != 0 for N in (1, 3, 5))
report('(h) same q+qbar, different q-qbar: identical even-N moments, different odd-N moments', ok_even and ok_odd)

print()
print('SUMMARY s6: %d/%d PASS' % (sum(1 for _, o in results if o), len(results)))
