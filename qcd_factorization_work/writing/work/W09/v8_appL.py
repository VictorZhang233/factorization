"""W09 / v8: App L (lem:appL-divided-differences, prop:appL-bare, prop:appL-renormalized).
 (a) the m-gluon vertex of the LOCAL operator psibar g+ (iD^+)^{n-1} psi (iD^+ = i d^+ + g A^+; plane waves, all momenta
     incoming, fixed colour order t^{a_m}...t^{a_1}): sum over words with m letters A and n-1-m letters P of prod kappa
     = h_{n-1-m}(kappa_0..kappa_m), kappa_i = k^+ + q_1^+ + ... + q_i^+  (m <= 4, n <= 9);
 (b) Hermite-Genocchi for m = 4 (light-ray vertex in w space) and the divided-difference recursion;
 (c) gluon: int xi^{n-1} f_g = (-i)^{n-2} M_g^{(n-2)}(0)/(P^+)^n with M_g(w) = (P^+)^2 int dxi e^{i xi P^+ w} xi f_g(xi),
     odd f_g; consequence int_0^1 x^{n-1} g = <O_g^(n)>/(2 (P^+)^n) for even n, odd moments vanish;
 (d) SU(2) and SU(3) lattice check of d/dw W^{(A)}_{ab}[w,0] = -g f^{acd} A^c(w) W^{(A)}_{db}[w,0]  (so that
     d/dw[G_a(w) W^{(A)}_{ab}] = [(D^+G)_a](w) W^{(A)}_{ab}), and of the adjoint Leibniz rule;
 (e) one loop (VF-PDF-13): the 1/eps pole of the n-th moment of the bare PDF is gamma_qq(n)/C_F for n = 1..14, hence
     Z_f(n) = 1 - (alpha_s/2pi)(1/eps) gamma_qq(n) = Z_O(n) (VF-PDF-14), i.e. Z(x) = delta - (alpha_s/2pi)(1/eps) P_qq;
 (f) a compactly supported distribution with all moments zero vanishes: its Fourier-Laplace transform is entire with zero
     Taylor coefficients (illustrated: an entire function determined by its Taylor coefficients at 0).
"""
import sys, os, itertools, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import expm

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

def hcomp(r, ks):
    if r < 0: return sp.Integer(0)
    tot = sp.Integer(0)
    for comb in itertools.combinations_with_replacement(range(len(ks)), r):
        term = sp.Integer(1)
        for c in comb: term *= ks[c]
        tot += term
    return sp.expand(tot)

# ---------------- (a) local vertex from the word expansion --------------------------------------------
for m in range(0, 5):
    kp, *qs = sp.symbols('k q1:%d' % (m + 1)) if m > 0 else (sp.symbols('k'),)
    kap = [kp]
    for j in range(m):
        kap.append(kap[-1] + qs[j])
    for n in range(m + 1, 10):
        L = n - 1
        total = sp.Integer(0)
        # positions of the m A-letters among L letters (left to right = position 0..L-1); the gluon inserted rightmost is q_1
        for pos in itertools.combinations(range(L), m):
            term = sp.Integer(1)
            # momentum seen by a P-letter at position p = k + sum of q's of A-letters to its right
            for p in range(L):
                if p in pos: continue
                nright = sum(1 for a in pos if a > p)      # number of gluons inserted to the right of p
                term *= kap[nright]
            total += term
        ok = sp.simplify(sp.expand(total) - hcomp(n - 1 - m, kap)) == 0
        check('(a) m=%d n=%d: local m-gluon vertex of psibar g+ (iD+)^{n-1} psi = g^m h_{n-1-m}(kappa)' % (m, n), ok)

# ---------------- (b) Hermite-Genocchi m = 4, recursion ----------------------------------------------------
def divdiff(fun, nodes):
    if len(nodes) == 1:
        return fun(nodes[0])
    return (divdiff(fun, nodes[1:]) - divdiff(fun, nodes[:-1])) / (nodes[-1] - nodes[0])
rng = np.random.default_rng(5)
q = rng.uniform(-1.0, 1.3, size=4); k1 = 0.42
kap = [k1] + list(k1 + np.cumsum(q)); w = 0.9
# Monte Carlo-free: nested Gauss-Legendre on the simplex 0 < s1 < s2 < s3 < s4 < w
xg, wg = np.polynomial.legendre.leggauss(24)
def nested(level, upper, acc_phase):
    if level < 0:
        return np.exp(-1j * acc_phase)
    s = 0.5 * upper * (xg + 1); ws = 0.5 * upper * wg
    return sum(ws[i] * nested(level - 1, s[i], acc_phase + q[level] * s[i]) for i in range(len(s)))
val = nested(3, w, 0.0)
lhs = (1j) ** 4 * np.exp(1j * kap[-1] * w) * val
rhs = complex(divdiff(lambda x: mp.e ** (1j * x * w), kap))
check('(b) m=4: (i)^4 int_{0<s1<..<s4<w} e^{i kappa_4 w - i sum q_j s_j} = E_w[kappa_0..kappa_4] (|diff| = %.1e)' % abs(lhs - rhs), abs(lhs - rhs) < 1e-10)
# recursion f[k0..km] = (f[k1..km] - f[k0..k(m-1)])/(km - k0) for f = x^7 against h_{7-m}
ks = sp.symbols('c0:5')
for m in range(1, 5):
    dd = sp.cancel(divdiff(lambda x: x ** 7, list(ks[:m + 1])))
    check('(b) x^7[c0..c%d] = h_%d(c0..c%d)' % (m, 7 - m, m), sp.simplify(sp.expand(dd) - hcomp(7 - m, list(ks[:m + 1]))) == 0)

# ---------------- (c) gluon derivative formula ------------------------------------------------------------
Pp = mp.mpf('1.6')
fg = lambda t: t * (1 - t ** 2) ** 3 * (1 + 0.4 * t ** 2) * (1 if t >= 0 else 1)   # odd? t (1-t^2)^3 (1+0.4 t^2) is odd
check('(c) test f_g is odd', abs(fg(0.3) + fg(-0.3)) < 1e-15)
Mg = lambda w: Pp ** 2 * mp.quad(lambda t: mp.e ** (1j * t * Pp * w) * t * fg(t), [-1, 0, 1])
for n in range(2, 8):
    mom = mp.quad(lambda t: t ** (n - 1) * fg(t), [-1, 0, 1])
    der = mp.diff(Mg, 0, n - 2)
    rhs = (-1j) ** (n - 2) * der / Pp ** n
    check('(c) n=%d: int xi^{n-1} f_g = (-i)^{n-2} M_g^{(n-2)}(0)/(P+)^n  (%.10f vs %s)' % (n, mom, mp.nstr(rhs, 10)), abs(mom - rhs) < 1e-8)
    if n % 2 == 1:
        check('(c) n=%d odd: int xi^{n-1} f_g = 0' % n, abs(mom) < 1e-15)
# normalisation consistency: f_g = int dw/(2 pi xi P+) e^{-i xi P w} M_g(w)  <->  M_g = (P+)^2 int dxi e^{i xi P w} xi f_g
check('(c) (1/(2 pi P+)) * (2 pi/P+) * (P+)^2 = 1', abs(1 / (2 * mp.pi * Pp) * (2 * mp.pi / Pp) * Pp ** 2 - 1) < 1e-12)

# ---------------- (d) adjoint Wilson line on a lattice -----------------------------------------------------
def su2():
    s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
    t = [x / 2 for x in s]
    f = np.zeros((3, 3, 3))
    for a, b, c in itertools.permutations(range(3)):
        f[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])
    return t, f
def su3():
    l = np.zeros((8, 3, 3), complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    t = [x / 2 for x in l]
    f = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                f[a, b, c] = np.real(-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c]))
    return t, f
gc = 0.9
for name, (t, f) in (('SU(2)', su2()), ('SU(3)', su3())):
    na = len(t)
    coefs = np.random.default_rng(1).normal(size=(na, 3))
    Aplus = lambda s: sum((coefs[a, 0] + coefs[a, 1] * np.sin(1.3 * s) + coefs[a, 2] * s ** 2) * t[a] for a in range(na))
    Acomp = lambda s: np.array([coefs[a, 0] + coefs[a, 1] * np.sin(1.3 * s) + coefs[a, 2] * s ** 2 for a in range(na)])
    def W(w, N=4000):
        U = np.eye(t[0].shape[0], dtype=complex); ds = w / N
        for i in range(N):
            s = (i + 0.5) * ds
            U = expm(1j * gc * Aplus(s) * ds) @ U          # later points to the left
        return U
    def WA(w):
        U = W(w); Ud = U.conj().T
        return np.array([[2 * np.trace(t[a] @ U @ t[b] @ Ud) for b in range(na)] for a in range(na)]).real
    w0, h = 0.7, 1e-3
    dWA = (WA(w0 + h) - WA(w0 - h)) / (2 * h)
    pred = -gc * np.einsum('acd,c,db->ab', f, Acomp(w0), WA(w0))
    check('(d) %s: d/dw W^(A)_{ab}[w,0] = -g f^{acd} A^c(w) W^(A)_{db}[w,0] (max dev %.1e)' % (name, np.max(np.abs(dWA - pred))),
          np.max(np.abs(dWA - pred)) < 2e-5)
    # adjoint covariant derivative D X^a = dX^a + g f^{abc} A^b X^c ; Leibniz: d(X.Y) = (DX).Y + X.(DY)
    Xa = np.random.default_rng(2).normal(size=na); Ya = np.random.default_rng(3).normal(size=na)
    dX = np.random.default_rng(4).normal(size=na); dY = np.random.default_rng(6).normal(size=na)
    A0 = Acomp(w0)
    DX = dX + gc * np.einsum('abc,b,c->a', f, A0, Xa); DY = dY + gc * np.einsum('abc,b,c->a', f, A0, Ya)
    check('(d) %s: adjoint Leibniz rule  d(X.Y) = (DX).Y + X.(DY)' % name, abs((dX @ Ya + Xa @ dY) - (DX @ Ya + Xa @ DY)) < 1e-12)
    # left-acting derivative of G_a W_ab: d/dw[G_a W_ab] = (dG_a) W_ab + G_a dW_ab = [(D G)_d] W_db
    Gw = np.random.default_rng(7).normal(size=na); dG = np.random.default_rng(8).normal(size=na)
    lhs_ = dG @ WA(w0) + Gw @ pred
    DG = dG + gc * np.einsum('abc,b,c->a', f, A0, Gw)
    check('(d) %s: d/dw[G_a W^(A)_{ab}] = [(D^+ G)_a] W^(A)_{ab}' % name, np.max(np.abs(lhs_ - DG @ WA(w0))) < 1e-9)

# ---------------- (e) one-loop pole structure, all n ------------------------------------------------------
eps = sp.symbols('epsilon')
def S1(n): return sum(sp.Rational(1, j) for j in range(1, n + 1))
for n in range(1, 15):
    ladder = (1 - eps) ** 2 / ((n - eps) * (n + 1 - eps))
    wil = -2 * sum((1 / (i + 1 - eps) for i in range(1, n)), sp.Integer(0))
    se = -(1 - eps) / (2 - eps)
    tot = sp.together(ladder + wil + se)
    pole = sp.limit(tot, eps, 0)      # A_eps = (alpha_s/2pi) C_F [1/eps + ...]: the 1/eps coefficient is tot(0)
    gqq = sp.Rational(3, 2) + sp.Rational(1, n * (n + 1)) - 2 * S1(n)
    check('(e) n=%d: 1/eps coefficient of the bare n-th moment = %s = gamma_qq(n)/C_F' % (n, pole), sp.simplify(pole - gqq) == 0)

# ---------------- (f) entire Fourier-Laplace transform ---------------------------------------------------
# for T supported in [-1,1]: F(t) = <T, e^{-i t xi}> = sum_m (-i t)^m <T, xi^m>/m!  (entire); all moments 0 => F = 0 => T = 0
ftest = lambda xx: (1 - xx ** 2) ** 2 * (0.3 + xx)
Ft = lambda tt: mp.quad(lambda xx: ftest(xx) * mp.e ** (-1j * tt * xx), [-1, 1])
series = lambda tt, M: sum((-1j * tt) ** mm / mp.factorial(mm) * mp.quad(lambda xx: xx ** mm * ftest(xx), [-1, 1]) for mm in range(M))
check('(f) Fourier-Laplace transform = Taylor series built from the moments (t = 3.7, 40 terms)', abs(Ft(3.7) - series(3.7, 40)) < 1e-12)

print('\nSUMMARY v8: %d PASS, %d FAIL' % (npass, nfail))
