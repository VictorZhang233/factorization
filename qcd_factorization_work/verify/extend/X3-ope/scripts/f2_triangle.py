"""
f2_triangle.py -- Example F.3/F.4 of the report: one-loop forward triangle with one on-shell light-like leg.

Lines: k (power a3), k+q (power a2), k-p (power a1);  p^2 = 0, q^2 = -Q^2, (p+q)^2 = -Q^2 (1-omega).
Euclidean-type normalisation  I = int d^Dk / pi^{D/2}  prod 1/(-k_l^2)^{a_l}.

(A) exact parametric result
      I(omega) = Gamma(a-D/2)/prod Gamma(a_i) (Q^2)^{D/2-a} B(D/2-a2, D/2-a1-a3) B(a1,a3) 2F1(a-D/2, a1; a1+a3; omega)
    is compared with the naive Taylor expansion of the momentum-space integrand in p:
      1/((k-lam p)^2)^{a1} = sum_n (a1)_n/n! (2 lam k.p)^n / (k^2)^{a1+n}           (p^2 = 0)
    whose n-th term is a massless propagator-type integral (one-loop tensor formula, only the q..q tensor survives).
    Claim (Theorem F): coefficient of omega^n of I  ==  n-th naive term, identically in (a1,a2,a3,D).
(B) direct numerical check of (A) at three REAL parameter points in the convergent region (revision: the earlier
    wording "random complex parameters" was wrong; complex points are checked in review_r1_1_checks/r3), against
    (B1) the 2-dimensional Feynman-parameter integral by plain quadrature -- the endpoint singularity
         (1-y)^(a2-1+D/2-a) (= (1-y)^(-0.8) at the second point) limits its accuracy; tolerance 2e-5 (relative);
    (B2) the same integral with the y-integration done exactly (Beta function) and the remaining Euler-type
         t-integral by quadrature; tolerance 1e-12 (relative).
(C) a_i = 1, D = 4-2eps: Laurent structure of the exact result vs the naive terms (each naive term has an IR pole).
(D) Example F.4: off-shell leg p^2 = -P^2 (omega = 0): I = (1/Q^2)[ln(Q^2/P^2) + 2] + O(P^2/Q^4 log) in D = 4,
    i.e. the matrix element diverges logarithmically as P^2 -> 0 while the hard coefficient is unchanged.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

a1, a2, a3, D, n = sp.symbols('a1 a2 a3 D n')
a = a1 + a2 + a3

# ---------------- (A) symbolic identity of the omega^n coefficients
exact_coeff = (sp.gamma(a - D / 2) / (sp.gamma(a1) * sp.gamma(a2) * sp.gamma(a3))
               * sp.gamma(D / 2 - a2) * sp.gamma(D / 2 - a1 - a3) / sp.gamma(D - a)
               * sp.gamma(a1) * sp.gamma(a3) / sp.gamma(a1 + a3)
               * sp.rf(a - D / 2, n) * sp.rf(a1, n) / (sp.rf(a1 + a3, n) * sp.factorial(n)))


def A_tensor(m, alpha, beta, Dd):
    """t = 0 coefficient of the one-loop tensor formula (only q^{mu1..mu_m} survives since p^2 = 0)"""
    return (sp.gamma(alpha + beta - Dd / 2) * sp.gamma(Dd / 2 - alpha + m) * sp.gamma(Dd / 2 - beta)
            / (sp.gamma(alpha) * sp.gamma(beta) * sp.gamma(Dd - alpha - beta + m)))


# naive term n:  (a1)_n/n! * 2^n * <(k.p)^n> with (k.p)^n -> A(n,0) (q.p)^n (Q^2)^{...};  2^n (q.p)^n/Q^{2n} -> omega^n
naive_coeff = sp.rf(a1, n) / sp.factorial(n) * A_tensor(n, a1 + a3 + n, a2, D)
ratio = sp.gammasimp(sp.simplify(sp.combsimp(exact_coeff / naive_coeff)))
print("(A) symbolic ratio exact/naive coefficient of omega^n =", ratio)

# ---------------- (B) numerical check at random parameters against direct 2d Feynman-parameter integration
mp.mp.dps = 20


def I_param(a1v, a2v, a3v, Dv, om):
    """direct numerical evaluation of the Feynman-parameter integral (needs convergence)"""
    av = a1v + a2v + a3v
    pref = mp.gamma(av - Dv / 2) / (mp.gamma(a1v) * mp.gamma(a2v) * mp.gamma(a3v))
    # x2 = 1-y, x1 = y t, x3 = y (1-t)
    f = lambda y, t: (y * (y * t) ** (a1v - 1) * (1 - y) ** (a2v - 1) * (y * (1 - t)) ** (a3v - 1)
                      * ((1 - y) * y * ((1 - t) + (1 - om) * t)) ** (Dv / 2 - av))
    return pref * mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])


def I_exact(a1v, a2v, a3v, Dv, om):
    av = a1v + a2v + a3v
    return (mp.gamma(av - Dv / 2) / (mp.gamma(a1v) * mp.gamma(a2v) * mp.gamma(a3v))
            * mp.beta(Dv / 2 - a2v, Dv / 2 - a1v - a3v) * mp.beta(a1v, a3v)
            * mp.hyp2f1(av - Dv / 2, a1v, a1v + a3v, om))


def I_naive_sum(a1v, a2v, a3v, Dv, om, K=60):
    s = mp.mpf(0)
    for k in range(K):
        ck = (mp.rf(a1v, k) / mp.factorial(k) * mp.gamma(a1v + a3v + k + a2v - Dv / 2)
              * mp.gamma(Dv / 2 - a1v - a3v) * mp.gamma(Dv / 2 - a2v)
              / (mp.gamma(a1v + a3v + k) * mp.gamma(a2v) * mp.gamma(Dv - a1v - a2v - a3v)))
        s += ck * om ** k
    return s


def I_param_y_exact(a1v, a2v, a3v, Dv, om):
    """(B2): y-integral exactly (Beta function), t-integral numerically"""
    av = a1v + a2v + a3v
    pref = mp.gamma(av - Dv / 2) / (mp.gamma(a1v) * mp.gamma(a2v) * mp.gamma(a3v))
    ey = (a1v + a3v - 1) + (Dv / 2 - av)          # power of y (Jacobian included)
    e1y = (a2v - 1) + (Dv / 2 - av)               # power of (1-y)
    It = mp.quad(lambda t: t ** (a1v - 1) * (1 - t) ** (a3v - 1) * ((1 - t) + (1 - om) * t) ** (Dv / 2 - av),
                 [0, 0.5, 1])
    return pref * mp.beta(ey + 1, e1y + 1) * It


okB = True
for (a1v, a2v, a3v, Dv, om) in [(0.6, 0.7, 0.5, 3.3, 0.3), (0.8, 0.45, 0.55, 3.1, -0.5), (0.5, 0.6, 0.45, 3.0, 0.7)]:
    e = I_exact(a1v, a2v, a3v, Dv, om)
    q = I_param(a1v, a2v, a3v, Dv, om)
    s = I_naive_sum(a1v, a2v, a3v, Dv, om)
    with mp.workdps(30):
        q2 = I_param_y_exact(a1v, a2v, a3v, Dv, om)
        e2 = I_exact(a1v, a2v, a3v, Dv, om)
        d2 = abs(q2 / e2 - 1)
    d1 = abs(q / e - 1)
    okB &= (d1 < 2e-5) and (d2 < 1e-12)
    print("(B) a=(%.2f,%.2f,%.2f) D=%.2f omega=%+.2f : exact 2F1 = %s  param.quad = %s  naive Taylor sum = %s"
          % (a1v, a2v, a3v, Dv, om, mp.nstr(e, 12), mp.nstr(q, 12), mp.nstr(s, 12)))
    print("    rel. deviation (B1) 2d quadrature: %s [tol 2e-5] ; (B2) exact-y + 1d quadrature: %s [tol 1e-12]"
          % (mp.nstr(d1, 3), mp.nstr(d2, 3)))
print("(B) all points within tolerance:", okB)

# ---------------- (C) a_i = 1, D = 4 - 2 eps: Laurent structure
eps, om = sp.symbols('epsilon omega')
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
I_on = -cG / eps ** 2 * ((1 - om) ** (-eps) - 1) / om          # (Q^2 = 1)
ser = sp.series(I_on, om, 0, 4).removeO()
for k in range(4):
    ck = sp.simplify(ser.coeff(om, k))
    nk = sp.simplify(naive_coeff.subs({a1: 1, a2: 1, a3: 1, D: 4 - 2 * eps, n: k}))
    print("(C) omega^%d : exact = %s ; naive = %s ; equal: %s ; Laurent(naive) = %s"
          % (k, sp.simplify(ck / cG), sp.simplify(nk / cG), sp.simplify(sp.gammasimp(ck - nk)) == 0,
             sp.series(sp.gammasimp(nk / cG), eps, 0, 1)))

# ---------------- (D) off-shell leg (Example F.4), D = 4, omega = 0: I = int dt dy / [Q^2 (1-y) + P^2 y t (1-t)]
for P2 in [1e-2, 1e-4, 1e-6]:
    Qsq = 1.0
    val = mp.quad(lambda t, y: 1 / (Qsq * (1 - y) + P2 * y * t * (1 - t)), [0, 1], [0, 1])
    print("(D) P^2/Q^2 = %.0e : Q^2 I = %s ; ln(Q^2/P^2)+2 = %s ; difference = %s"
          % (P2, mp.nstr(val, 12), mp.nstr(mp.log(1 / P2) + 2, 12), mp.nstr(val - mp.log(1 / P2) - 2, 6)))
