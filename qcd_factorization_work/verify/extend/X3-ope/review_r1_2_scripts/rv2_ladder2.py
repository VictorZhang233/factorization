"""
rv2_ladder2.py -- reviewer #2 (X3 round 1): independent TWO-LOOP test of the forward on-shell expansion ("Theorem F")
on the planar ladder (quark target), identically in the seven line powers a1..a7 and D.

Graph (Euclidean, int d^Dk/pi^{D/2} per loop):  A1(p in) - A2 - J1(q in) - J2(q out) - B2 - B1(p out) on the quark line,
rungs A1-B1 (line 6) and A2-B2 (line 7).  Lines: 1=A1A2, 2=A2J1, 3=J1J2, 4=J2B2, 5=B2B1, 6=A1B1, 7=A2B2.
Routing: k on lines 2,4 ; k+q on 3 ; l on 1,5 ; l+p on 6 ; l-k on 7.   p^2 = 0, q^2 = Q^2 = 1, omega = -2 p.q (Euclid).

EXACT (p on shell): inner l-loop = one-loop triangle with a light-like leg => Euler integral turns it into
   int_0^1 dt w(t) [(k+tp)^2]^{-A}   (A = a1+a5+a6+a7-D/2)
and the outer k-loop is again a triangle with light-like leg t p, i.e. argument -t*omega.
The one-loop triangle formula used here is RE-DERIVED below by a 2d Feynman-parameter quadrature (not taken from f2).
NAIVE: expand only line 6 in p; inner and outer loops are one-loop tensor integrals with (p.k)^n, p^2 = 0.
Checks: (A) symbolic equality of omega^n coefficients (gammasimp), n = 0..5, identically in (a1..a7, D);
        (B) numeric equality exact(omega) vs naive sum at random real parameters, omega in (-1,1);
        (C) the one-loop triangle formula vs direct 2d Feynman-parameter quadrature.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

# ---------------- one-loop building blocks (Euclidean, int d^Dk/pi^{D/2})
def coef_tensor(n, al, be, D, G=sp.gamma):
    """int (p.k)^n / ((k^2)^al ((k+Q)^2)^be) = (-p.Q)^n (Q^2)^{D/2-al-be} * coef  (p^2 = 0)"""
    return G(al + be - D / 2) * G(D / 2 - al + n) * G(D / 2 - be) / (G(al) * G(be) * G(D - al - be + n))


def tri_coef_list(b1, b2, b3, D, nmax, G=sp.gamma, rf=sp.rf, fac=sp.factorial):
    """triangle: lines k (b3), k+Q (b2), k-P (b1), P^2=0, Q^2=1 ; returns Taylor coefficients in w = -2 P.Q
       from the closed form  Gamma(b-D/2)/prod Gamma B(D/2-b2, D/2-b1-b3) B(b1,b3) 2F1(b-D/2, b1; b1+b3; w)"""
    b = b1 + b2 + b3
    pref = (G(b - D / 2) / (G(b1) * G(b2) * G(b3)) * G(D / 2 - b2) * G(D / 2 - b1 - b3) / G(D - b)
            * G(b1) * G(b3) / G(b1 + b3))
    return [pref * rf(b - D / 2, n) * rf(b1, n) / (rf(b1 + b3, n) * fac(n)) for n in range(nmax + 1)]


# ---------------- (A) symbolic identity
a1, a2, a3, a4, a5, a6, a7, D = sp.symbols('a1:8 D')
nmax = 5
# exact: inner triangle (b1=a6, b2=a7, b3=a1+a5) -> prefactor C_in ; Euler weight for 2F1(A, a6; a6+a1+a5; .)
A = a1 + a5 + a6 + a7 - D / 2
C_in = tri_coef_list(a6, a7, a1 + a5, D, 0)[0]
euler = sp.gamma(a6 + a1 + a5) / (sp.gamma(a6) * sp.gamma(a1 + a5))
# outer triangle: b1 = A (line k+tp), b2 = a3 (k+q), b3 = a2+a4 (k); argument w_out = -2 (-t p).q?  -> see below
outer = tri_coef_list(A, a3, a2 + a4, D, nmax)
# Euclidean: outer line (k+tp)^2 = (k - P)^2 with P = -t p ; w = -2 P.q = 2 t p.q = -t*omega (omega = -2 p.q)
exact_c = []
for n in range(nmax + 1):
    # int_0^1 t^{a6-1}(1-t)^{a1+a5-1} (-t)^n dt = (-1)^n B(a6+n, a1+a5)
    tint = (-1) ** n * sp.gamma(a6 + n) * sp.gamma(a1 + a5) / sp.gamma(a6 + a1 + a5 + n)
    exact_c.append(C_in * euler * outer[n] * tint)
# naive: line 6: 1/((l+p)^2)^{a6} = sum (a6)_n/n! (-2 l.p)^n/(l^2)^{a6+n}
naive_c = []
for n in range(nmax + 1):
    al = a1 + a5 + a6 + n
    ci = coef_tensor(n, al, a7, D)            # int (p.l)^n/((l^2)^al ((l-k)^2)^a7) = (p.k)^n (k^2)^{D/2-al-a7} ci
    alo = a2 + a4 + al + a7 - D / 2
    co = coef_tensor(n, alo, a3, D)           # int (p.k)^n/((k^2)^alo ((k+q)^2)^a3) = (-p.q)^n co
    # (-2)^n (p.k)^n -> (-2)^n (-p.q)^n = (2 p.q)^n = (-omega)^n
    naive_c.append(sp.rf(a6, n) / sp.factorial(n) * ci * co * (-1) ** n)
for n in range(nmax + 1):
    r = sp.gammasimp(sp.combsimp(exact_c[n] / naive_c[n]))
    print("(A) n=%d : exact/naive coefficient ratio = %s" % (n, sp.simplify(r)))

# ---------------- (B) numeric: exact(omega) by t-quadrature of the outer 2F1 vs naive Taylor sum
mp.mp.dps = 30
def exact_num(p, om):
    a1v, a2v, a3v, a4v, a5v, a6v, a7v, Dv = p
    Av = a1v + a5v + a6v + a7v - Dv / 2
    Cin = tri_coef_list(a6v, a7v, a1v + a5v, Dv, 0, G=mp.gamma, rf=mp.rf, fac=mp.factorial)[0]
    eul = mp.gamma(a6v + a1v + a5v) / (mp.gamma(a6v) * mp.gamma(a1v + a5v))
    b1, b2, b3 = Av, a3v, a2v + a4v
    b = b1 + b2 + b3
    pref = (mp.gamma(b - Dv / 2) / (mp.gamma(b1) * mp.gamma(b2) * mp.gamma(b3)) * mp.beta(Dv / 2 - b2, Dv / 2 - b1 - b3)
            * mp.beta(b1, b3))
    f = lambda t: t ** (a6v - 1) * (1 - t) ** (a1v + a5v - 1) * mp.hyp2f1(b - Dv / 2, b1, b1 + b3, -t * om)
    return Cin * eul * pref * mp.quad(f, [0, 0.5, 1])

def naive_num(p, om, K=120):
    a1v, a2v, a3v, a4v, a5v, a6v, a7v, Dv = p
    s = mp.mpf(0)
    for n in range(K):
        al = a1v + a5v + a6v + n
        ci = coef_tensor(n, al, a7v, Dv, G=mp.gamma)
        alo = a2v + a4v + al + a7v - Dv / 2
        co = coef_tensor(n, alo, a3v, Dv, G=mp.gamma)
        s += mp.rf(a6v, n) / mp.factorial(n) * ci * co * (-om) ** n
    return s

import random
rng = random.Random(99)
for trial in range(4):
    while True:
        p = [mp.mpf(rng.uniform(0.3, 1.2)) for _ in range(7)] + [mp.mpf(rng.uniform(2.6, 3.8))]
        a1v, a2v, a3v, a4v, a5v, a6v, a7v, Dv = p
        # all Gamma arguments of both representations positive (convergent region of every building block)
        Av = a1v + a5v + a6v + a7v - Dv / 2
        args = [Av, Dv / 2 - a7v, Dv / 2 - a6v - a1v - a5v, Dv / 2 - a3v, Dv / 2 - Av - a2v - a4v,
                Av + a3v + a2v + a4v - Dv / 2]
        if min(args) > 0.05:
            break
    for om in [mp.mpf('0.6'), mp.mpf('-0.8'), mp.mpf('0.3')]:
        e = exact_num(p, om)
        nn = naive_num(p, om)
        print("(B) params=%s omega=%s : exact=%s naive=%s rel.diff=%s" % (
            [float(x) for x in p], float(om), mp.nstr(e, 15), mp.nstr(nn, 15), mp.nstr(abs(e / nn - 1), 3)))

# ---------------- (C) one-loop triangle closed form vs direct Feynman-parameter quadrature (Euclidean)
# I = Gamma(b-D/2)/prod Gamma(b_i) int dx (prod x^{b_i-1}) delta(1-sum x) U^{b-D} / F^{b-D/2}, U = sum x,
# F = x2 x3 Q^2 + x1 x2 (P+Q)^2 + x1 x3 P^2 ; lines: x3 <-> k, x2 <-> k+Q, x1 <-> k-P ; (P+Q)^2 = Q^2 (1 - w)
def tri_quad(b1, b2, b3, Dv, w):
    b = b1 + b2 + b3
    pref = mp.gamma(b - Dv / 2) / (mp.gamma(b1) * mp.gamma(b2) * mp.gamma(b3))
    def f(u, v):          # x1 = u v, x2 = 1-u, x3 = u (1-v) ; jacobian u
        x1, x2, x3 = u * v, 1 - u, u * (1 - v)
        F = x2 * x3 + x1 * x2 * (1 - w)
        return u * x1 ** (b1 - 1) * x2 ** (b2 - 1) * x3 ** (b3 - 1) * F ** (Dv / 2 - b)
    return pref * mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])
for (b1, b2, b3, Dv, w) in [(0.5, 0.6, 0.45, 3.0, 0.4), (0.45, 0.8, 0.35, 2.9, -0.6), (0.6, 0.5, 0.7, 3.5, 0.75)]:  # convergent region: b>D/2, D/2>b2, D/2>b1+b3
    cl = tri_coef_list(mp.mpf(b1), mp.mpf(b2), mp.mpf(b3), mp.mpf(Dv), 0, G=mp.gamma, rf=mp.rf, fac=mp.factorial)[0]
    b = b1 + b2 + b3
    closed = cl * mp.hyp2f1(b - Dv / 2, b1, b1 + b3, w)
    print("(C) triangle b=(%.1f,%.1f,%.1f) D=%.1f w=%+.1f : closed=%s quad=%s" % (b1, b2, b3, Dv, w, mp.nstr(closed, 12), mp.nstr(tri_quad(b1, b2, b3, Dv, w), 12)))
