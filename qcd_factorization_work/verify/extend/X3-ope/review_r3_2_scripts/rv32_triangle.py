"""rv32_triangle.py -- reviewer r3-2: independent check of Example F.3 / Theorem F
on the one-loop forward triangle (lines k-p [a1], k+q [a2], k [a3]; p^2 = 0).

Independent route (not the one-loop tensor formula used by f2):
  naive term n = coefficient of lam^n of the momentum-space integrand with p -> lam p:
     1/(-(k-lam p)^2)^{a1} = sum_n (-1)^n (a1)_n/n! (2 lam k.p)^n / (-k^2)^{a1+n}     (p^2 = 0)
  then ONE Feynman parameter x for (-k^2)^{alpha} (-(k+q)^2)^{beta}, shift k = l - x q:
     (2k.p)^n -> (2 l.p - 2 x nu)^n ; every term with l.p averages to products of p^2 = 0,
     so only (-2 x nu)^n survives.  This gives (Q^2 = 1, omega = 2 nu)
     I_n = (a1)_n/n! * Gamma(a+n-D/2)/(Gamma(a1+a3+n) Gamma(a2)) * B(D/2-a1-a3, D/2-a2) * omega^n .
Checks:
 (A) symbolic: I_n equals the omega^n coefficient of the report's closed form
       Gamma(a-D/2)/prod Gamma(a_i) B(D/2-a2, D/2-a1-a3) B(a1,a3) 2F1(a-D/2, a1; a1+a3; omega)
 (B) closed form vs DIRECT 2-d simplex quadrature (parametrisation x1=u, x3=(1-u)w, x2=(1-u)(1-w),
     different from f2's), at complex omega inside AND outside the unit disk (cut plane holomorphy)
 (C) partial sums of the naive series vs closed form for |omega| < 1 (complex)
 (D) a_i = 1, D = 4 - 2 eps: leading pole of I_n is -1/((n+1) eps)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

a1, a2, a3, D, eps = sp.symbols('a1 a2 a3 D epsilon')
n = sp.symbols('n', integer=True, nonnegative=True)
a = a1 + a2 + a3

closed_coeff = (sp.gamma(a - D/2)/(sp.gamma(a1)*sp.gamma(a2)*sp.gamma(a3))
                * sp.gamma(D/2 - a2)*sp.gamma(D/2 - a1 - a3)/sp.gamma(D - a)
                * sp.gamma(a1)*sp.gamma(a3)/sp.gamma(a1 + a3)
                * sp.rf(a - D/2, n)*sp.rf(a1, n)/(sp.rf(a1 + a3, n)*sp.factorial(n)))
naive_mine = (sp.rf(a1, n)/sp.factorial(n) * sp.gamma(a + n - D/2)
              / (sp.gamma(a1 + a3 + n)*sp.gamma(a2))
              * sp.gamma(D/2 - a1 - a3)*sp.gamma(D/2 - a2)/sp.gamma(D - a))
print("(A) symbolic: closed-form omega^n coefficient / independent naive term =",
      sp.simplify(sp.gammasimp(closed_coeff/naive_mine)))
# also at explicit n to avoid relying on gammasimp with symbolic n
for nn in range(0, 6):
    r = sp.gammasimp(sp.simplify((closed_coeff/naive_mine).subs(n, nn)))
    print(f"    n={nn}: ratio = {r}")

# ---------------- (B) direct quadrature
mp.mp.dps = 20
def closed(a1v, a2v, a3v, Dv, om):
    av = a1v + a2v + a3v
    return (mp.gamma(av - Dv/2)/(mp.gamma(a1v)*mp.gamma(a2v)*mp.gamma(a3v))
            * mp.beta(Dv/2 - a2v, Dv/2 - a1v - a3v)*mp.beta(a1v, a3v)
            * mp.hyp2f1(av - Dv/2, a1v, a1v + a3v, om))

def direct(a1v, a2v, a3v, Dv, om):
    av = a1v + a2v + a3v
    pref = mp.gamma(av - Dv/2)/(mp.gamma(a1v)*mp.gamma(a2v)*mp.gamma(a3v))
    def f(u, w):
        x1 = u; x3 = (1 - u)*w; x2 = (1 - u)*(1 - w)
        F = x2*(x3 + (1 - om)*x1)          # U = 1 on the simplex, Q^2 = 1
        return (1 - u)*x1**(a1v - 1)*x2**(a2v - 1)*x3**(a3v - 1)*F**(Dv/2 - av)
    return pref*mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])

pars = (mp.mpf('0.7'), mp.mpf('0.55'), mp.mpf('0.65'), mp.mpf('3.5'))
maxrel = 0
for om in [mp.mpc(0.4, 0.3), mp.mpc(-0.9, -0.1), mp.mpc(1.5, 0.7), mp.mpc(-2.0, 0.5), mp.mpc(0, 3), mp.mpc(2.5, -0.2)]:
    c = closed(*pars, om); d = direct(*pars, om)
    rel = abs(c - d)/abs(c); maxrel = max(maxrel, rel)
    print(f"(B) omega={mp.nstr(om,4):>14}: closed={mp.nstr(c,12):>32}  direct={mp.nstr(d,12):>32}  rel.dev={mp.nstr(rel,3)}")
print("(B) max rel. deviation:", mp.nstr(maxrel, 3), " PASS" if maxrel < 1e-8 else " FAIL")

# ---------------- (C) naive series partial sums (|omega| < 1)
def naive_term(a1v, a2v, a3v, Dv, k):
    av = a1v + a2v + a3v
    return (mp.rf(a1v, k)/mp.factorial(k)*mp.gamma(av + k - Dv/2)/(mp.gamma(a1v + a3v + k)*mp.gamma(a2v))
            * mp.beta(Dv/2 - a1v - a3v, Dv/2 - a2v))
for om in [mp.mpc(0, 0.5), 0.6*mp.exp(1j*mp.pi/3), mp.mpc(-0.7, 0.2)]:
    s = mp.mpf(0)
    for k in range(0, 400):
        s += naive_term(*pars, k)*om**k
    c = closed(*pars, om)
    print(f"(C) omega={mp.nstr(om,4):>14}: sum_{{n<400}} naive = {mp.nstr(s,14)}  closed = {mp.nstr(c,14)}  rel={mp.nstr(abs(s-c)/abs(c),3)}")

# ---------------- (D) pole at a_i = 1, D = 4 - 2 eps
for nn in range(0, 5):
    In = naive_mine.subs({a1: 1, a2: 1, a3: 1, D: 4 - 2*eps, n: nn})
    lead = sp.limit(eps*In, eps, 0)
    print(f"(D) n={nn}: lim eps*I_n = {lead}   (expected -1/(n+1) = {sp.Rational(-1, nn+1)})")
