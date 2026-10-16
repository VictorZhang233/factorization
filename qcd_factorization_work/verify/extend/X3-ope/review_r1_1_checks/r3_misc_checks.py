"""
Reviewer check R3 (independent code):
 (1) one-loop forward triangle (f2): Taylor coefficients of the exact 2F1 result vs the naive tensor-integral terms at
     COMPLEX (a1,a2,a3,D,omega) -- f2's docstring claims complex parameters but uses real ones.
     Exact:  I = G(a-D/2)/(G(a1)G(a2)G(a3)) B(D/2-a2, D/2-a1-a3) B(a1,a3) 2F1(a-D/2, a1; a1+a3; w)   (Q^2 = 1)
     Naive:  c_n = (a1)_n/n! * G(a+n-D/2) G(D/2-a1-a3) G(D/2-a2) / (G(a1+a3+n) G(a2) G(D-a))
     Also an independent check of the exact formula by direct 2D quadrature of the Feynman-parameter integral at a
     complex point inside the convergence domain.
 (2) Markov/Chebyshev constants used in h1 (h): sum of |coefficients| of T_n equals |T_n(i)| <= (1+sqrt2)^n.
 (3) slice-geometry inequality of h1 (e): closed form of v^2 - (Im s)^2 = 2 v^2 Q^2/(A + sqrt(A^2 - 4 v^2 Q^2)).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
from numpy.polynomial import chebyshev as C

mp.mp.dps = 30
G = mp.gamma


def exact(a1, a2, a3, D, w):
    a = a1 + a2 + a3
    return G(a - D / 2) / (G(a1) * G(a2) * G(a3)) * mp.beta(D / 2 - a2, D / 2 - a1 - a3) * mp.beta(a1, a3) \
        * mp.hyp2f1(a - D / 2, a1, a1 + a3, w)


def naive(a1, a2, a3, D, n):
    a = a1 + a2 + a3
    return mp.rf(a1, n) / mp.factorial(n) * G(a + n - D / 2) * G(D / 2 - a1 - a3) * G(D / 2 - a2) \
        / (G(a1 + a3 + n) * G(a2) * G(D - a))


pts = [(mp.mpc('0.7', '0.3'), mp.mpc('1.1', '-0.4'), mp.mpc('0.9', '0.2'), mp.mpc('3.6', '0.5')),
       (mp.mpc('1.3', '-0.7'), mp.mpc('0.6', '0.9'), mp.mpc('1.2', '0.1'), mp.mpc('4.4', '-1.2'))]
for (a1, a2, a3, D) in pts:
    # Taylor coefficients of the exact function by Cauchy integral on |w| = 0.5
    for n in [0, 1, 3, 7]:
        cn = mp.quad(lambda t: exact(a1, a2, a3, D, 0.5 * mp.e ** (1j * t)) * (0.5 * mp.e ** (1j * t)) ** (-n),
                     [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi)
        print('(1) a=(%s,%s,%s) D=%s n=%d : Cauchy coeff / naive = %s'
              % (mp.nstr(a1, 3), mp.nstr(a2, 3), mp.nstr(a3, 3), mp.nstr(D, 3), n, mp.nstr(cn / naive(a1, a2, a3, D, n), 15)))

# direct Feynman-parameter quadrature at a complex point in the convergence domain:
# Re(a-D/2) > 0, Re(D/2-a2) > 0, Re(D/2-a1-a3) > 0, Re a_i > 0
a1, a2, a3, D, w = mp.mpc('0.6', '0.2'), mp.mpc('0.7', '-0.1'), mp.mpc('0.5', '0.15'), mp.mpc('3.3', '0.3'), mp.mpc('0.2', '0.5')
a = a1 + a2 + a3
pref = G(a - D / 2) / (G(a1) * G(a2) * G(a3))
# x2 = 1-y, x1 = y t, x3 = y(1-t), Jacobian y ; U = 1 ; F/Q^2 = x2 (x3 + (1-w) x1)
f = lambda y, t: y * (y * t) ** (a1 - 1) * (1 - y) ** (a2 - 1) * (y * (1 - t)) ** (a3 - 1) \
    * ((1 - y) * (y * (1 - t) + (1 - w) * y * t)) ** (D / 2 - a)
mp.mp.dps = 20
val = pref * mp.quad(f, [0, 1], [0, 1], maxdegree=10)
mp.mp.dps = 30
print('(1b) complex point: direct quadrature =', mp.nstr(val, 10), '; exact 2F1 formula =', mp.nstr(exact(a1, a2, a3, D, w), 10))

# (2) Chebyshev
for n in [1, 3, 5, 7, 9, 11, 15, 21]:
    c = C.cheb2poly([0] * n + [1])
    s = np.sum(np.abs(c))
    Ti = abs(np.polynomial.polynomial.polyval(1j, c))
    print('(2) n=%2d : max|coef T_n| = %8.0f ; sum|coef| = %10.0f ; |T_n(i)| = %10.0f ; (1+sqrt2)^n = %12.1f'
          % (n, np.max(np.abs(c)), s, Ti, (1 + np.sqrt(2)) ** n))

# (3) slice geometry closed form
rng = np.random.default_rng(1)
worst = 0
for _ in range(20000):
    Q = rng.uniform(0.1, 10)
    w = complex(rng.normal() * 10, abs(rng.normal()) * 10 + 1e-6)
    s = np.sqrt(w * w + Q * Q)
    if s.real < 0:
        s = -s
    v = w.imag
    A = abs(w) ** 2 + Q * Q
    lhs = v * v - s.imag ** 2
    rhs = 2 * v * v * Q * Q / (A + np.sqrt(max(A * A - 4 * v * v * Q * Q, 0)))
    worst = max(worst, abs(lhs - rhs) / max(abs(rhs), 1e-300))
print('(3) max relative deviation of v^2-(Im s)^2 from closed form:', worst)
