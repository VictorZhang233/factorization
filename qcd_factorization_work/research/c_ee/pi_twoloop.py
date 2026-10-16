"""
pi_twoloop.py -- the vector-current correlator Pi(q^2) of massless QCD through two loops (O(alpha_s)),
computed in the Euclidean region from Feynman diagrams, exactly in D = 4 - 2 eps.

  Pi^{mu nu}(q) = i Int d^Dx e^{iqx} <0|T j^mu(x) j^nu(0)|0> = (q^mu q^nu - q^2 g^{mu nu}) Pi(q^2),
  j^mu = sum_q e_q qbar gamma^mu q ;  R(s) = 12 pi Im Pi(s + i0).

Method
  * Dirac traces with diracD.py (D-dim, Tr 1 = 4); Feynman gauge; the three O(g^2) diagrams
    (gluon exchange "V" and the two quark self-energy insertions "S1","S2").
  * scalar products -> inverse propagators of the two-loop propagator topology
        D1 = k^2, D2 = (k-q)^2, D3 = r^2, D4 = (r-q)^2, D5 = (k-r)^2 ,
  * Wick rotation; Euclidean integrals  Int d^Dk d^Dr/pi^D  prod D_i^-a_i = Ihat(a) (Q^2)^{D - sum a},
    evaluated exactly:  IBP triangle rule (Chetyrkin-Tkachov) for all a_i >= 1; one-loop tensor
    formula (Feynman parameters, derived in DERIVATION.md) for the nested / factorised cases.
    Every integral becomes  rational(eps) x {G(1,1)^2  or  G(1,1) G(1+eps,1)} .
Checks
  T1  I(1,1,1,1,0) = G(1,1)^2 ;  T2  I(1,1,1,1,1) = 6 zeta_3/Q^2 + O(eps) ;  T3 the second IBP triangle
  (lines 3,4,5) gives the same I(1,1,1,1,1) ;  T4 a nested integral with a numerator vs a hand result ;
  W1  transversality  q_mu q_nu Pi^{mu nu} = 0  at one and two loops (exact in eps) ;
  P1  one-loop Pi ;  P2 two-loop pole structure (no 1/eps^2: Ward identity Z1 = Z2) ;
  P3  MS-bar result  Pi = (N_c e_q^2/12 pi^2)[ 5/3 - L + (alpha_s/pi)(55/12 - 4 zeta_3 - L) ] , L = ln(-q^2/mu^2) ;
  P4  RG:  mu^2 dPi/dmu^2 = (N_c e_q^2/12 pi^2)(1 + alpha_s/pi) ; Adler function D = N_c e_q^2 (1 + alpha_s/pi) ;
  C1  exact-in-eps cutting identity  2 (D-1) s Im Pi_2(s+i0) = rho_V + rho_R  (from ee_nlo.py results) ;
  C2  R = 12 pi Im Pi = N_c e_q^2 (1 + alpha_s/pi).
Run:  python3 -I pi_twoloop.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from functools import lru_cache
import sympy as sp
import mpmath as mp
from diracD import D as Dsym, dot, slash, gam, lc_mul, trace

eps = sp.Symbol('eps')
Dd = 4 - 2 * eps
PASS = []


def check(name, cond):
    PASS.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# ---------------------------------------------------------------------------------------------
# Gamma-function bookkeeping: Gamma(n + c eps) -> Gm[c] * rational,  Gm[c] := Gamma(1 + c eps)
# ---------------------------------------------------------------------------------------------
Gm = {c: sp.Symbol('Gm%+d' % c) for c in range(-6, 7)}


def gam_red(arg):
    """Gamma(arg) with arg = n + c*eps (n, c integers) -> Gm[c] * rational(eps)"""
    arg = sp.expand(arg)
    c = arg.coeff(eps)
    n = sp.expand(arg - c * eps)
    assert n.is_Integer and c.is_Integer, arg
    n, c = int(n), int(c)
    if c == 0:
        if n <= 0:
            return sp.zoo  # pole: caller must avoid
        return sp.factorial(n - 1)
    x = c * eps
    res = Gm[c]
    if n >= 1:
        for j in range(1, n):
            res *= (j + x)
    else:
        for j in range(n, 1):
            res /= (j + x)
    return res


def inv_gamma(arg):
    """1/Gamma(arg); zero for non-positive integer arg"""
    arg = sp.expand(arg)
    if arg.is_Integer and arg <= 0:
        return sp.Integer(0)
    return 1 / gam_red(arg)


def Gfun(a, b):
    """Euclidean one-loop G(a,b): Int d^Dk/pi^{D/2} 1/[(k^2)^a ((k-q)^2)^b] = G(a,b) (Q^2)^{D/2-a-b}"""
    ia, ib = inv_gamma(a), inv_gamma(b)
    if ia == 0 or ib == 0:
        return sp.Integer(0)
    return gam_red(a + b - Dd / 2) * gam_red(Dd / 2 - a) * gam_red(Dd / 2 - b) * ia * ib * inv_gamma(Dd - a - b)


def Acoef(m, t, al, be):
    """one-loop tensor coefficient: Int d^Dk/pi^{D/2} k^{mu1..mum}/[(k^2)^al ((p-k)^2)^be]
       = sum_t A(m,t) (p^2)^{D/2+t-al-be} {g^t p^{m-2t}}"""
    ia, ib = inv_gamma(al), inv_gamma(be)
    if ia == 0 or ib == 0:
        return sp.Integer(0)
    return gam_red(al + be - Dd / 2 - t) * gam_red(Dd / 2 - al + m - t) * gam_red(Dd / 2 - be + t) * ia * ib \
        * inv_gamma(Dd - al - be + m) / 2 ** t


def Ncount(m, t):
    return sp.factorial(m) / (2 ** t * sp.factorial(t) * sp.factorial(m - 2 * t))


def tensor_contract(m, al, be):
    """Int d^Dk/pi^{D/2} (k.v)^m/[(k^2)^al((p-k)^2)^be] = sum_t C_t (p^2)^{D/2+t-al-be} (v^2)^t (p.v)^{m-2t};
       returns list of (C_t, t)"""
    return [(Ncount(m, t) * Acoef(m, t, al, be), t) for t in range(m // 2 + 1)]


# ---------------------------------------------------------------------------------------------
# two-loop Euclidean integrals  Ihat(a1..a5)  (coefficient of (Q^2)^{D - sum a})
# ---------------------------------------------------------------------------------------------
@lru_cache(maxsize=None)
def Ihat(a1, a2, a3, a4, a5):
    a = (a1, a2, a3, a4, a5)
    if a5 <= 0:
        return _factorised(a)
    if min(a1, a2, a3, a4) >= 1:
        # IBP triangle rule on lines (1,2,5):
        # (D - a1 - a2 - 2 a5) I = a1[I(1+,5-) - I(1+,3-)] + a2[I(2+,5-) - I(2+,4-)]
        rhs = a1 * (Ihat(a1 + 1, a2, a3, a4, a5 - 1) - Ihat(a1 + 1, a2, a3 - 1, a4, a5)) \
            + a2 * (Ihat(a1, a2 + 1, a3, a4, a5 - 1) - Ihat(a1, a2 + 1, a3, a4 - 1, a5))
        return sp.expand(rhs / (Dd - a1 - a2 - 2 * a5))
    if (a1 <= 0 and a2 <= 0) or (a3 <= 0 and a4 <= 0):
        return sp.Integer(0)
    if a4 <= 0:
        return _nested(a)
    if a3 <= 0:
        return Ihat(a2, a1, a4, a3, a5)      # (k,r) -> (q-k, q-r)
    if a2 <= 0:
        return Ihat(a3, a4, a1, a2, a5)      # k <-> r
    if a1 <= 0:
        return Ihat(a4, a3, a2, a1, a5)
    raise RuntimeError(a)


def _factorised(a):
    """a5 <= 0: numerator D5^n = (k^2 + r^2 - 2 k.r)^n, k- and r-loops factorise"""
    a1, a2, a3, a4, a5 = a
    n = -a5
    tot = sp.Integer(0)
    for i in range(n + 1):
        for j in range(n + 1 - i):
            m = n - i - j
            mult = sp.factorial(n) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(m)) * (-2) ** m
            # k-loop: Int (k.r)^m (k^2)^i /[(k^2)^a1 ((k-q)^2)^a2] -> sum_t C (Q^2)^.. (r^2)^t (q.r)^{m-2t}
            for Ck, t in tensor_contract(m, a1 - i, a2):
                if Ck == 0:
                    continue
                mm = m - 2 * t
                # r-loop: Int (r^2)^{j+t} (q.r)^{mm} / [(r^2)^a3 ((r-q)^2)^a4]  (v = p = q)
                for Cr, t2 in tensor_contract(mm, a3 - j - t, a4):
                    if Cr == 0:
                        continue
                    tot += mult * Ck * Cr
    return sp.expand(tot)


def _nested(a):
    """a4 <= 0 < a3, a5 >= 1: inner r-loop {r^2, (k-r)^2} with numerator D4^n=(r^2 - 2 r.q + Q^2)^n,
       then outer k-loop {k^2 (non-integer power), (k-q)^2}"""
    a1, a2, a3, a4, a5 = a
    n = -a4
    tot = sp.Integer(0)
    for i in range(n + 1):
        for m in range(n + 1 - i):
            l = n - i - m
            mult = sp.factorial(n) / (sp.factorial(i) * sp.factorial(m) * sp.factorial(l)) * (-2) ** m
            # inner: Int (r.q)^m/[(r^2)^{a3-i} ((k-r)^2)^{a5}] = sum_t C (k^2)^{D/2+t-(a3-i)-a5} (Q^2)^t (k.q)^{m-2t}
            for Ci, t in tensor_contract(m, a3 - i, a5):
                if Ci == 0:
                    continue
                pw = Dd / 2 + t - (a3 - i) - a5          # power of k^2 produced
                # outer: Int (k.q)^{m-2t} (k^2)^pw / [(k^2)^a1 ((k-q)^2)^a2]
                for Co, t2 in tensor_contract(m - 2 * t, a1 - pw, a2):
                    if Co == 0:
                        continue
                    tot += mult * Ci * Co
    return sp.expand(tot)


def to_gamma(expr):
    return expr.subs({Gm[c]: sp.gamma(1 + c * eps) for c in Gm})


def num_eval(expr, ev, dps=40):
    mp.mp.dps = dps
    f = sp.lambdify(eps, to_gamma(expr), 'mpmath')
    return f(mp.mpf(ev))


# ---------------------------------------------------------------------------------------------
# basic integral tests
# ---------------------------------------------------------------------------------------------
print('=== integral tests ===')
G11 = Gfun(1, 1)
check('T1  I(1,1,1,1,0) = G(1,1)^2', sp.simplify(Ihat(1, 1, 1, 1, 0) - G11 ** 2) == 0)
I11111 = Ihat(1, 1, 1, 1, 1)
mp.mp.dps = 50
vals = [num_eval(I11111, e, 50) for e in ['1e-8', '-1e-8']]
check('T2  I(1,1,1,1,1) -> 6 zeta(3) as eps->0  (got %s)' % mp.nstr(vals[0], 15),
      all(abs(v - 6 * mp.zeta(3)) < 1e-6 for v in vals))
# T3: second triangle rule on lines (3,4,5) (differentiate w.r.t. r):
# (D - a3 - a4 - 2a5) I = a3[I(3+,5-) - I(3+,1-)] + a4[I(4+,5-) - I(4+,2-)]
alt = (1 * (Ihat(1, 1, 2, 1, 0) - Ihat(0, 1, 2, 1, 1)) + 1 * (Ihat(1, 1, 1, 2, 0) - Ihat(1, 0, 1, 2, 1))) / (Dd - 4)
check('T3  I(1,1,1,1,1) from the (3,4,5) triangle == from (1,2,5) (exact, 3 values of eps)',
      all(abs(num_eval(I11111 - sp.expand(alt), e)) < 1e-30 for e in ['0.1', '-0.23', '0.37']))
# T4: I(1,1,1,-1,1) by hand: -(G11/2)[G(eps,1) + G(1+eps,1)] + G11 G(1+eps,1)  (Q^2)^{D-3}
hand = -(G11 / 2) * (Gfun(eps, 1) + Gfun(1 + eps, 1)) + G11 * Gfun(1 + eps, 1)
check('T4  nested integral with numerator, I(1,1,1,-1,1), vs hand reduction',
      all(abs(num_eval(Ihat(1, 1, 1, -1, 1) - hand, e)) < 1e-30 for e in ['0.1', '-0.23']))
# T5: symmetric relation I(2,1,0,1,1) = G(1,1) G(2,1+eps)
check('T5  I(2,1,0,1,1) = G(1,1) G(2,1+eps)', abs(num_eval(Ihat(2, 1, 0, 1, 1) - G11 * Gfun(2, 1 + eps), '0.17')) < 1e-30)

# ---------------------------------------------------------------------------------------------
# Feynman diagrams
# ---------------------------------------------------------------------------------------------
Dv = sp.symbols('D1:6')
q2 = sp.Symbol('q2')     # Minkowski q^2
SUB = {dot('k', 'k'): Dv[0], dot('q', 'q'): q2, dot('k', 'q'): (Dv[0] + q2 - Dv[1]) / 2,
       dot('r', 'r'): Dv[2], dot('q', 'r'): (Dv[2] + q2 - Dv[3]) / 2, dot('k', 'r'): (Dv[0] + Dv[2] - Dv[4]) / 2}


def mink_to_eucl(expr_num, den):
    """Minkowski  Int d^Dk d^Dr/(2pi)^{2D}  expr_num(D_i, q2)/prod D_i^den_i
       = -(1/(4pi)^D) sum (-1)^{sum n} Ihat(n) (Q^2)^{D - sum n} * (q2)^c ;  returns coefficient X of
       (Q^2)^{power}/(4pi)^D as a dict {power_shift: value} with q2 = -Q^2 substituted."""
    poly = sp.Poly(sp.expand(expr_num), *Dv, q2)
    out = 0
    for mon, cf in poly.terms():
        n = [den[i] - mon[i] for i in range(5)]
        cpow = mon[5]
        val = Ihat(*n)
        if val == 0:
            continue
        # (q2)^c = (-1)^c (Q^2)^c ; (Q^2)^{D - sum n + c} must be the same for all terms
        out += -(-1) ** sum(n) * (-1) ** cpow * cf * val
        shift = (4 - sum(n) + cpow)
        if not hasattr(mink_to_eucl, 'shift'):
            mink_to_eucl.shift = shift
        assert shift == mink_to_eucl.shift, (shift, mink_to_eucl.shift)
    return sp.expand(out)


def S(**kw):
    return slash(**kw)


def diagram_traces(left, right):
    """left/right: LC for the current insertions (gamma^m pair or q-slash)."""
    TV = trace(lc_mul(left, S(k=1), gam('a'), S(r=1), right, S(r=1, q=-1), gam('a'), S(k=1, q=-1)))
    TS1 = trace(lc_mul(left, S(k=1), gam('a'), S(r=1), gam('a'), S(k=1), right, S(k=1, q=-1)))
    TS2 = trace(lc_mul(left, S(k=1), right, S(k=1, q=-1), gam('a'), S(r=1, q=-1), gam('a'), S(k=1, q=-1)))
    return [(TV, (1, 1, 1, 1, 1)), (TS1, (2, 1, 1, 0, 1)), (TS2, (1, 2, 0, 1, 1))]


def twoloop_contract(left, right, sign):
    """sign * sum over diagrams of Minkowski integrals, prefactor g^2 C_F N_c e_q^2 /(4pi)^D implied"""
    tot = 0
    for T, den in diagram_traces(left, right):
        Tn = sp.expand(T.subs(SUB).subs(Dsym, Dd))
        mink_to_eucl.__dict__.pop('shift', None)
        tot += mink_to_eucl(Tn, den)
    return sp.expand(sign * tot)


print('=== one loop (calibration) ===')
# Pi^{mu nu}_1 = i N_c e_q^2 Int d^Dk/(2pi)^D Tr[g^mu k g^nu (k-q)]/(k^2 (k-q)^2);
# one-loop Wick rotation: Int d^Dk/(2pi)^D prod D_i^-a_i = (i/(4pi)^{D/2}) (-1)^{sum a} Ghat(a) (Q^2)^{D/2-sum a}
T1 = trace(lc_mul(gam('m'), S(k=1), gam('m'), S(k=1, q=-1)))
T1 = sp.expand(T1.subs(SUB).subs(Dsym, Dd))
p1 = sp.Poly(T1, Dv[0], Dv[1], q2)
gmunu_Pi1 = 0     # coefficient of (Q^2)^{1-eps} N_c e_q^2/(4pi)^{D/2}
for (i1, i2, c), cf in p1.terms():
    n1, n2 = 1 - i1, 1 - i2
    gmunu_Pi1 += cf * sp.I * sp.I * (-1) ** (n1 + n2) * Gfun(n1, n2) * (-1) ** c
gmunu_Pi1 = -gmunu_Pi1        # -g_{mu nu} contraction sign
# Pi_1 = -g Pi /((D-1) q^2) = .../((D-1)(-Q^2))
Pi1 = sp.expand(gmunu_Pi1 / ((Dd - 1) * (-1)))   # coefficient of N_c e_q^2 (Q^2)^-eps/(4pi)^{D/2}
Pi1_expected = 2 * (Dd - 2) / (Dd - 1) * G11
check('P1  one-loop Pi = N_c e_q^2 [2(D-2)/(D-1)] G(1,1) (Q^2)^-eps/(4pi)^{D/2}',
      abs(num_eval(Pi1 - Pi1_expected, '0.123')) < 1e-30)
# transversality at one loop
Tq = trace(lc_mul(S(q=1), S(k=1), S(q=1), S(k=1, q=-1)))
Tq = sp.expand(Tq.subs(SUB).subs(Dsym, Dd))
pq = sp.Poly(Tq, Dv[0], Dv[1], q2)
qq1 = sum(cf * (-1) ** (1 - i1 + 1 - i2) * Gfun(1 - i1, 1 - i2) * (-1) ** c for (i1, i2, c), cf in pq.terms())
check('W1a one loop: q_mu q_nu Pi^{mu nu} = 0', sp.simplify(to_gamma(qq1)) == 0 or abs(num_eval(qq1, '0.2')) < 1e-30)

print('=== two loops ===')
gPi2 = twoloop_contract(gam('m'), gam('m'), -1)       # -g_{mu nu} Pi^{mu nu}: coefficient of g^2 CF Nc eq^2 (Q^2)^{1-2eps}/(4pi)^D
qqPi2 = twoloop_contract(S(q=1), S(q=1), +1)         # q_mu q_nu Pi^{mu nu}: coefficient of ... (Q^2)^{2-2eps}
check('W1b two loops: q_mu q_nu Pi^{mu nu} = 0 exactly (3 values of eps)',
      all(abs(num_eval(qqPi2, e)) < 1e-28 for e in ['0.1', '-0.21', '0.33']))
Pi2 = sp.expand(gPi2 / ((Dd - 1) * (-1)))       # Pi_2 coefficient of g^2 C_F N_c e_q^2 (Q^2)^{-2eps}/(4pi)^D
# decompose on the two transcendental structures:  Pi2/G11^2 = r1 + r2 * [G(1+eps,1)/G(1,1)]
B1 = sp.expand(G11 ** 2)
B2 = sp.expand(G11 * Gfun(1 + eps, 1))
GmSyms = list(Gm.values())
X = Pi2 / B1
rho = B2 / B1
all1 = {Gm[c]: 1 for c in Gm}


def ratfun(expr):
    n, d = sp.fraction(sp.together(expr))
    n, d = sp.Poly(sp.expand(n), eps), sp.Poly(sp.expand(d), eps)
    gc = sp.gcd(n, d)
    return sp.factor(n.quo(gc).as_expr() / d.quo(gc).as_expr())


rho_rat = ratfun(rho.subs(all1))
# X depends on the Gamma symbols only through rho, which is linear in Gm[+2]:
r1 = ratfun(X.subs({**all1, Gm[2]: 0}))
r2 = ratfun(sp.diff(X, Gm[2]).subs(all1) / rho_rat)
print('      r1 =', r1)
print('      r2 =', r2)
Pi2_closed = r1 * B1 + r2 * B2
check('P0  closed form  Pi_2 = r1 G(1,1)^2 + r2 G(1,1) G(1+eps,1)  equals the diagram sum (4 values of eps)',
      all(abs(num_eval(Pi2_closed - Pi2, e)) < 1e-30 for e in ['0.137', '-0.29', '0.41', '0.0071']))
r1_claim = -4 * (1 - eps) * (2 - eps + 2 * eps ** 2) / (eps * (3 - 2 * eps))
r2_claim = 16 * (1 - eps) * (1 - 2 * eps) * (2 - 2 * eps + eps ** 2) / (eps * (3 - 2 * eps) * (2 - 3 * eps))
check('P0c r1 = -4(1-e)(2-e+2e^2)/(e(3-2e)),  r2 = 16(1-e)(1-2e)(2-2e+e^2)/(e(3-2e)(2-3e))',
      sp.simplify(r1 - r1_claim) == 0 and sp.simplify(r2 - r2_claim) == 0)

# ---------------------------------------------------------------------------------------------
# expansions, MS-bar renormalisation
# ---------------------------------------------------------------------------------------------
# Pi = Nc eq^2 { Pi1hat (Q^2)^-eps /(4pi)^{D/2}  +  g^2 CF Pi2hat (Q^2)^-2eps/(4pi)^D }
# MS-bar: g^2 = 4 pi as mu^{2eps} e^{eps gE} (4pi)^-eps ; multiply Pi by mu_MS^{2eps} = mu^{2eps}(e^gE/4pi)^eps
# and subtract pure poles.  In units of Nc eq^2/(12 pi^2) and as/pi, with L = ln(Q^2/mu^2):
Lsym = sp.Symbol('L')
a_s = sp.Symbol('a_s', positive=True)
def _trunc(ex, N):
    ex = sp.expand(ex)
    return sum(ex.coeff(eps, j) * eps ** j for j in range(-6, N + 1))


def _exp_trunc(P, N):
    """exp(P) through eps^N for a polynomial P(eps) without constant term"""
    res, term = sp.Integer(1), sp.Integer(1)
    for j in range(1, N + 1):
        term = _trunc(term * P / j, N)
        res += term
    return sp.expand(res)


def _lg(c, N):
    x = c * eps
    return -sp.EulerGamma * x + sum((-1) ** k * sp.zeta(k) * x ** k / k for k in range(2, N + 1))


def _split_monomial(B):
    """B = rational(eps) * prod Gm[c]^k_c  ->  (rational, {c: k_c})"""
    ks = {}
    for c in Gm:
        if B.has(Gm[c]):
            k = sp.simplify(sp.diff(B, Gm[c]) * Gm[c] / B)
            assert k.is_Integer, (c, k)
            ks[c] = int(k)
    rat = sp.factor(sp.cancel(B.subs({Gm[c]: 1 for c in Gm})))
    return rat, ks


def series_terms(terms, extra_log, order):
    """sum over terms [(rational, {c:k})] of rational * prod Gamma(1+c eps)^k * exp(extra_log), Laurent through eps^order"""
    tot = 0
    for rat, ks in terms:
        p = 0
        while sp.limit(rat * eps ** p, eps, 0) in (sp.oo, -sp.oo, sp.zoo):
            p += 1
        N = order + p
        Srat = sp.expand(sp.series(rat, eps, 0, order + 1).removeO())
        P = sp.expand(sum(k * _lg(c, N) for c, k in ks.items()) + extra_log)
        Sexp = _exp_trunc(P, N)
        tot += _trunc(Srat * Sexp, order)
    tot = sp.expand(tot)
    out = sum(sp.simplify(tot.coeff(eps, j)) * eps ** j for j in range(-6, order + 1))
    out = out.replace(lambda e: isinstance(e, sp.zeta) and e.args[0] in (2, 4, 6), lambda e: sp.expand_func(e))
    return sp.expand(out)


# one loop: (4pi)^{-D/2} mu_MS^{2eps} (Q^2)^-eps = e^{eps gE} e^{-eps L}/(16 pi^2) ; units Nc eq^2/(12 pi^2)
one_terms = [(sp.Rational(12, 16) * _split_monomial(Pi1_expected)[0], _split_monomial(Pi1_expected)[1])]
one_ser = series_terms(one_terms, eps * sp.EulerGamma - eps * Lsym, 1)
# two loops: g^2 CF/(4pi)^D mu_MS^{2eps} (Q^2)^{-2eps} = as CF e^{2 eps gE} e^{-2 eps L}/(64 pi^3);
# in units (as/pi) C_F Nc eq^2/(12 pi^2):  factor 12 pi^2 * pi/(64 pi^3) = 3/16
rB1, kB1 = _split_monomial(B1)
rB2, kB2 = _split_monomial(B2)
two_terms = [(sp.Rational(3, 16) * r1 * rB1, kB1), (sp.Rational(3, 16) * r2 * rB2, kB2)]
two_ser = series_terms(two_terms, 2 * eps * sp.EulerGamma - 2 * eps * Lsym, 1)
print('      one-loop  [units Nc eq^2/(12 pi^2)]       :', sp.collect(sp.expand(one_ser.subs(eps, eps)), eps))
print('      two-loop  [units (as/pi) C_F Nc eq^2/(12 pi^2)]:', sp.collect(two_ser, eps))
check('P2  two-loop bare Pi: no 1/eps^2 (subdivergences cancel, Z1=Z2); simple pole L-independent',
      sp.simplify(two_ser.coeff(eps, -2)) == 0 and sp.simplify(sp.diff(two_ser.coeff(eps, -1), Lsym)) == 0)
fin1 = sp.simplify(one_ser.coeff(eps, 0))
fin2 = sp.simplify(two_ser.coeff(eps, 0))
pole1 = sp.simplify(one_ser.coeff(eps, -1))
pole2 = sp.simplify(two_ser.coeff(eps, -1))
print('      MS-bar finite parts:  one loop:', fin1, ' ;  two loop (per C_F):', sp.nsimplify(fin2, [sp.zeta(3)]))
CFv = sp.Rational(4, 3)
check('P3a one loop MS-bar:  Pi^(0) = (Nc eq^2/12pi^2)(5/3 - L)', sp.simplify(fin1 - (sp.Rational(5, 3) - Lsym)) == 0)
check('P3b two loop MS-bar:  Pi^(1) = (Nc eq^2/12pi^2)(as/pi)(3 C_F/4)(55/12 - 4 zeta3 - L)  [= (55/12-4z3-L) for C_F=4/3]',
      sp.simplify(sp.expand(fin2 * CFv) - (sp.Rational(55, 12) - 4 * sp.zeta(3) - Lsym)) == 0)
# RG: Pi_R = Pihat - Z, Z = z0/eps + (as) z1/eps  =>  mu^2 dPi_R/dmu^2 = z0 + 2 z1 as
gamma_Pi = pole1 + 2 * pole2 * CFv            # units Nc eq^2/(12 pi^2), as/pi -> 1 placeholder
check('P4  mu^2 dPi/dmu^2 = (Nc eq^2/12pi^2)[1 + (3C_F/4)(as/pi)] from the poles, = -dPi/dL',
      sp.simplify(pole1 - 1) == 0 and sp.simplify(2 * pole2 - sp.Rational(3, 4)) == 0
      and sp.simplify(-sp.diff(fin1, Lsym) - 1) == 0 and sp.simplify(-sp.diff(fin2, Lsym) - sp.Rational(3, 4)) == 0)
# Adler function  D(Q^2) = -12 pi^2 Q^2 dPi/dQ^2 = 12 pi^2 * (-dPi/dL)
Adler = sp.expand(-sp.diff(fin1 + a_s * fin2 * CFv, Lsym))   # D/(Nc eq^2) = 12 pi^2 (-dPi/dL)/(12 pi^2)
check('P5  Adler function D(Q^2) = -12pi^2 Q^2 dPi/dQ^2 = Nc eq^2 (1 + as/pi): L-independent (RG invariant), finite',
      sp.simplify(Adler - (1 + a_s)) == 0)

# ---------------------------------------------------------------------------------------------
# diagram by diagram (Feynman gauge): the vertex-type graph V and the self-energy graphs S1+S2
# separately contain 1/eps^2 (UV subdivergence x overall divergence); they cancel in the sum (Z1 = Z2)
# ---------------------------------------------------------------------------------------------
diag_ser = {}
for name, idx in (('V', [0]), ('S1+S2', [1, 2])):
    tot = 0
    for i in idx:
        T, den = diagram_traces(gam('m'), gam('m'))[i]
        Tn = sp.expand(T.subs(SUB).subs(Dsym, Dd))
        mink_to_eucl.__dict__.pop('shift', None)
        tot += mink_to_eucl(Tn, den)
    Pd = sp.expand(-tot / ((Dd - 1) * (-1)))
    Xd = Pd / B1
    r1d = ratfun(Xd.subs({**all1, Gm[2]: 0}))
    r2d = ratfun(sp.diff(Xd, Gm[2]).subs(all1) / rho_rat)
    ok = abs(num_eval(r1d * B1 + r2d * B2 - Pd, '0.173')) < 1e-30
    ser = series_terms([(sp.Rational(3, 16) * r1d * rB1, kB1), (sp.Rational(3, 16) * r2d * rB2, kB2)],
                       2 * eps * sp.EulerGamma - 2 * eps * Lsym, 0)
    diag_ser[name] = ser
    print('      %-6s [units (as/pi) C_F Nc eq^2/12pi^2, MS-bar factor]: %s   (basis ok: %s)' % (name, sp.collect(ser, eps), ok))
check('P2b individual graphs have 1/eps^2 poles that cancel in the sum (V vs S1+S2)',
      sp.simplify(diag_ser['V'].coeff(eps, -2)) != 0
      and sp.simplify(diag_ser['V'].coeff(eps, -2) + diag_ser['S1+S2'].coeff(eps, -2)) == 0)

# ---------------------------------------------------------------------------------------------
# exact cutting identity in D dims:  2(D-1) s Im Pi_2(s+i0) = rho_V + rho_R
# ---------------------------------------------------------------------------------------------
# Im (Q^2)^{-2eps} at Q^2 = -s - i0:  (-s-i0)^{-2eps} = s^{-2eps} e^{2 i pi eps}  => Im = s^{-2eps} sin(2 pi eps)
# LHS (per Nc eq^2, g^2 CF): 2(D-1) s * s^{-2eps} sin(2 pi eps) Pi2_closed/(4pi)^D
# RHS: rho_LO * (as CF/2pi)(4pi/s)^eps * total(eps),  rho_LO = 2(D-2) s Phi2
s_ = sp.Symbol('s', positive=True)
Phi2 = (1 / (8 * sp.pi)) * (4 * sp.pi / s_) ** eps * sp.gamma(1 - eps) / sp.gamma(2 - 2 * eps)
cG = sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
f_ff = -(2 - eps + 2 * eps ** 2) / (eps ** 2 * (1 - 2 * eps))
real = 2 * (1 - 2 * eps) * (2 - 2 * eps + eps ** 2) * sp.gamma(1 - eps) ** 2 / (
    eps ** 2 * (1 - 3 * eps) * (2 - 3 * eps) * sp.gamma(1 - 3 * eps))
total = real + f_ff * cG * sp.cos(sp.pi * eps)
g2 = sp.Symbol('g2')
rhs = 2 * (Dd - 2) * s_ * Phi2 * (g2 / (4 * sp.pi)) / (2 * sp.pi) * (4 * sp.pi / s_) ** eps * total
lhs = 2 * (Dd - 1) * s_ * s_ ** (-2 * eps) * sp.sin(2 * sp.pi * eps) * to_gamma(Pi2_closed) * g2 / (4 * sp.pi) ** Dd
fl = sp.lambdify(eps, (lhs / rhs).subs({s_: sp.Rational(29, 10), g2: 1}), 'mpmath')
mp.mp.dps = 40
ratios = [fl(mp.mpf(e)) for e in ['0.1', '-0.2', '0.31', '-0.43', '0.0123']]
print('      LHS/RHS at eps = 0.1,-0.2,0.31,-0.43,0.0123:', [mp.nstr(x, 20) for x in ratios])
check('C1  exact D-dim cutting identity: 2(D-1) s Im Pi_2(s+i0) = rho_virtual + rho_real for all eps',
      all(abs(x - 1) < 1e-30 for x in ratios))
# R: Im of the renormalised Pi at s+i0 (L -> ln(s/mu^2) - i pi)
ls = sp.Symbol('ls', real=True)
PiR = (fin1 + a_s * CFv * fin2)                   # units Nc eq^2/(12 pi^2), a_s = as/pi
ImPiR = sp.im(sp.expand(PiR.subs(Lsym, ls - sp.I * sp.pi)))
Rval = sp.simplify(12 * sp.pi * ImPiR / (12 * sp.pi ** 2))
check('C2  R = 12 pi Im Pi(s+i0) = Nc eq^2 (1 + as/pi)   [got Nc eq^2 x (%s)]' % Rval,
      sp.simplify(Rval - (1 + a_s)) == 0)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
