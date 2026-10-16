r"""
w06_twoloop_diagrams.py -- writer W06: an independent, from-scratch computation of the O(g^2) (two-loop)
massless vector-current correlator, diagram by diagram (Feynman gauge), exactly in eps.

Nothing is taken from research/c_ee: the Dirac traces use W06's own engine (w06_dtrace.py), the two-loop
propagator integrals are evaluated by W06's own implementation of
  * the one-loop G-function  G(a,b)                                (lem:appC-bubble),
  * the one-loop tensor formula (itself checked below against scalar reductions for m <= 4),
  * the IBP triangle rule on the triangle (1,2,5)                  (lem:appC-ibp),
and every Gamma function Gamma(n + c eps) is reduced EXACTLY to  rational(eps) * Gamma(1 + c eps).

Checks:
 A1-A4  tensor formula vs scalar reductions (m = 1..4), exact
 I1     Ihat(1,1,1,1,1) = 6 zeta_3 + O(eps)
 L0     one-loop Pi_0 = N_c e_q^2 [2(D-2)/(D-1)] G(1,1) (Q^2)^-eps/(4pi)^{D/2} from the same code (normalisation)
 W1     q_mu q_nu Pi^{mu nu} = 0 at two loops (sum of diagrams), exactly
 F1     sum of diagrams = N_c e_q^2 C_F g0^2 (Q^2)^{-2eps}/(4pi)^D [r1 G(1,1)^2 + r2 G(1,1) G(1+eps,1)] with r1, r2 of VF-EE-7
 E1     only the two transcendental structures G(1,1)^2 and G(1,1)G(1+eps,1) occur
 S1     diagram-by-diagram Laurent expansions (MS-bar factor, units (a_s/pi) C_F N_c e_q^2/(12 pi^2)):
        V  = 1/(4e^2) + (17/12 - L/2)/e + L^2/2 - 17L/6 - 3 z3 - pi^2/24 + 259/36
        S1+S2 = -1/(4e^2) + (L/2 - 25/24)/e - L^2/2 + 25L/12 + pi^2/24 - 541/144
        sum = 3/(8e) + 55/16 - 3 z3 - 3L/4
Run: python3 -I w06_twoloop_diagrams.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from functools import lru_cache
from math import comb, factorial
import itertools
import sympy as sp
from w06_dtrace import trace, contract, dot, D as Dsym
from w06_series import laurent

e = sp.Symbol('eps')
Dv = 4 - 2 * e
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# ----------------------------------------------------------------------------- exact Gamma bookkeeping
# A "GT" (Gamma term) is a dict  key -> rational function of eps,  key = tuple(sorted((c, power)))  meaning
# prod Gamma(1 + c eps)^power.  Sums of GTs are dicts; products multiply keys and coefficients.
def _key(dct):
    return tuple(sorted((c, p) for c, p in dct.items() if p != 0))


def gamma_factor(n, c):
    """Gamma(n + c eps) = rat * Gamma(1 + c eps); returns (rat, c).  n integer, c rational."""
    x = c * e
    if n >= 1:
        rat = sp.Integer(1)
        for j in range(1, n):
            rat *= (j + x)
        return rat, c
    rat = sp.Integer(1)
    for j in range(n, 1):
        if c == 0 and j == 0:
            raise ZeroDivisionError('Gamma at a non-positive integer')
        rat /= (j + x)
    return rat, c


def split_arg(arg):
    """arg = n + c eps with n integer, c rational -> (n, c)"""
    arg = sp.expand(arg)
    c = sp.Rational(arg.coeff(e, 1))
    n = arg.coeff(e, 0)
    assert n.is_integer, arg
    return int(n), c


def gamma_ratio(num_args, den_args):
    """prod Gamma(num) / prod Gamma(den) as a GT; returns {} (zero) if a denominator Gamma has a pole."""
    rat = sp.Integer(1)
    pw = {}
    for a in num_args:
        n, c = split_arg(a)
        if c == 0 and n <= 0:
            raise ZeroDivisionError('divergent Gamma(%s) in a numerator' % a)
        r, cc = gamma_factor(n, c)
        rat *= r
        pw[cc] = pw.get(cc, 0) + 1
    for a in den_args:
        n, c = split_arg(a)
        if c == 0 and n <= 0:
            return {}                     # 1/Gamma(non-positive integer) = 0
        r, cc = gamma_factor(n, c)
        rat /= r
        pw[cc] = pw.get(cc, 0) - 1
    pw.pop(0, None)                       # Gamma(1) = 1
    return {_key(pw): sp.cancel(rat)}


def gt_add(A, B, scale=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = sp.cancel(out.get(k, 0) + scale * v)
        if out[k] == 0:
            del out[k]
    return out


def gt_mul(A, B):
    out = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            d = dict(ka)
            for c, p in kb:
                d[c] = d.get(c, 0) + p
            k = _key(d)
            out[k] = sp.cancel(out.get(k, 0) + va * vb)
            if out[k] == 0:
                del out[k]
    return out


def gt_scale(A, s):
    return {k: sp.cancel(v * s) for k, v in A.items() if sp.cancel(v * s) != 0}


def gt_to_expr(A):
    tot = sp.Integer(0)
    for k, v in A.items():
        m = 1
        for c, p in k:
            m *= sp.gamma(1 + c * e) ** p
        tot += v * m
    return tot


# ----------------------------------------------------------------------------- one-loop building blocks
def G(a, b):
    """int d^Dk/pi^{D/2} 1/[(k^2)^a ((k-p)^2)^b] = G(a,b) (p^2)^{D/2-a-b}  (Euclidean)"""
    return gamma_ratio([a + b - Dv / 2, Dv / 2 - a, Dv / 2 - b], [a, b, Dv - a - b])


def Atens(m, t, al, be):
    """int d^Dk/pi^{D/2} k^{mu1..mum}/[(k^2)^al ((p-k)^2)^be] = sum_t Atens(m,t) (p^2)^{D/2+t-al-be} {g^t p^{m-2t}}"""
    g = gamma_ratio([al + be - Dv / 2 - t, Dv / 2 - al + m - t, Dv / 2 - be + t], [al, be, Dv - al - be + m])
    return gt_scale(g, sp.Rational(1, 2 ** t))


def Ncount(m, t):
    """number of distinct terms in {g^t p^{m-2t}} = m!/(2^t t! (m-2t)!)"""
    return factorial(m) // (2 ** t * factorial(t) * factorial(m - 2 * t))


# ---- check the tensor formula against scalar reductions (Euclidean, p^2 = 1 units):
# contract with p^{mu1}..p^{mum}: LHS = int (k.p)^m /(...) with k.p = (k^2 + p^2 - (p-k)^2)/2  -> sum of G's
# RHS = sum_t A(m,t) Ncount(m,t) (p^2)^t (p^2)^{m-2t} ... all p^2 = 1.
okA = True
for m in range(1, 5):
    for (al, be) in ((1, 1), (2, 1), (1, 1 + e), (2, 3 + e)):
        lhs = {}
        # (k.p)^m = 2^-m sum multinomial (k^2)^i (p^2)^j (-(p-k)^2)^l
        for i in range(m + 1):
            for j in range(m + 1 - i):
                l = m - i - j
                coef = sp.Rational(factorial(m), factorial(i) * factorial(j) * factorial(l) * 2 ** m) * (-1) ** l
                lhs = gt_add(lhs, gt_scale(G(al - i, be - l), coef))
        rhs = {}
        for t in range(m // 2 + 1):
            rhs = gt_add(rhs, gt_scale(Atens(m, t, al, be), Ncount(m, t)))
        diff = gt_add(lhs, rhs, -1)
        if diff:
            # compare numerically (keys may differ by Gamma identities)
            val = sp.N(gt_to_expr(diff).subs(e, sp.Rational(3, 29)), 30)
            if abs(val) > 1e-25:
                okA = False
                print('   tensor check failed', m, al, be, val)
        # second contraction for m = 2, 4: with g_{mu1 mu2} (trace) -> int k^2 (k.p)^{m-2}
        if m in (2, 4):
            lhs2 = {}
            mm = m - 2
            for i in range(mm + 1):
                for j in range(mm + 1 - i):
                    l = mm - i - j
                    coef = sp.Rational(factorial(mm), factorial(i) * factorial(j) * factorial(l) * 2 ** mm) * (-1) ** l
                    lhs2 = gt_add(lhs2, gt_scale(G(al - 1 - i, be - l), coef))
            # g_{mu1mu2} {g^t p^{m-2t}} p^{mu3}..p^{mum}  (all p^2 = 1): count = D * (#terms with g_{12}) + (#others)
            # do it by brute force over pairings
            rhs2 = {}
            for t in range(m // 2 + 1):
                # explicit formula: terms where (0,1) is a g-pair: N(m-2,t-1) of them, each gives D;
                # terms where 0 and 1 are both p's: N(m-2,t), each gives p^2 = 1;
                # terms where 0 is paired with j>=2 and 1 is a p (or vice versa): 2 (m-2) N(m-3... ) handled below
                n12 = Ncount(m - 2, t - 1) if t >= 1 else 0
                npp = Ncount(m - 2, t) if (m - 2 - 2 * t) >= 0 else 0
                # 0 paired with some j>=2, 1 a p-slot (or 1 paired with j, 0 a p): each contracts to p^2 = 1
                nmix = 0
                if t >= 1 and m - 3 >= 0:
                    # choose partner j (m-2 ways) for slot 0, slot 1 is p; remaining m-3 slots carry t-1 pairs
                    nmix = 2 * (m - 2) * (Ncount(m - 3, t - 1) if (m - 3 - 2 * (t - 1)) >= 0 else 0)
                # pair (0,j) and (1,k) with j,k >= 2 distinct: contracts to g_{jk} -> after p-contraction gives 1
                ngg = 0
                if t >= 2 and m - 4 >= 0:
                    ngg = (m - 2) * (m - 3) * (Ncount(m - 4, t - 2) if (m - 4 - 2 * (t - 2)) >= 0 else 0)
                tot = n12 * Dv + npp + nmix + ngg
                rhs2 = gt_add(rhs2, gt_scale(Atens(m, t, al, be), tot))
            val = sp.N(gt_to_expr(gt_add(lhs2, rhs2, -1)).subs(e, sp.Rational(3, 29)), 30)
            if abs(val) > 1e-25:
                okA = False
                print('   trace-contraction check failed', m, al, be, val)
check('A1-A4 one-loop tensor formula (m=1..4) agrees with scalar reductions (p.p and g-contractions), exact', okA)


# ----------------------------------------------------------------------------- two-loop integrals
# Euclidean: D1=k^2, D2=(k-q)^2, D3=r^2, D4=(r-q)^2, D5=(k-r)^2, Q^2 = q^2 = 1 (units)
# Ihat(a) = int int d^Dk d^Dr / pi^D  prod D_i^{-a_i}  (times (Q^2)^{D - sum a})
def expand_dot_qr(power):
    """(q.r)^power with q.r = (D3 + 1 - D4)/2  ->  list of (coef, x3, x4) meaning coef * D3^x3 * D4^x4"""
    out = []
    for i in range(power + 1):
        for j in range(power + 1 - i):
            l = power - i - j
            coef = sp.Rational(factorial(power), factorial(i) * factorial(j) * factorial(l) * 2 ** power) * (-1) ** l
            out.append((coef, i, l))       # D3^i * 1^j * D4^l
    return out


def expand_dot_pq(power):
    """(p.q)^power with p = r - q, p.q = (D3 - D4 - 1)/2 -> list of (coef, x3, x4)"""
    out = []
    for i in range(power + 1):
        for j in range(power + 1 - i):
            l = power - i - j
            coef = sp.Rational(factorial(power), factorial(i) * factorial(j) * factorial(l) * 2 ** power) * (-1) ** (j + l)
            out.append((coef, i, j))       # D3^i (-D4)^j (-1)^l
    return out


@lru_cache(maxsize=None)
def Ihat(a1, a2, a3, a4, a5):
    a = (a1, a2, a3, a4, a5)
    # trivially scaleless
    if (a1 <= 0 and a2 <= 0) or (a3 <= 0 and a4 <= 0):
        return {}
    if a5 <= 0:
        return _factorized(*a)
    if a3 <= 0 or a4 <= 0:
        if a1 > 0 and a2 > 0:
            return Ihat(a3, a4, a1, a2, a5)       # symmetry k <-> r
    if a1 <= 0:
        return _nested_a1(*a)
    if a2 <= 0:
        return _nested_a2(*a)
    # all positive: IBP triangle rule on (1,2,5)
    pref = Dv - a1 - a2 - 2 * a5
    out = {}
    out = gt_add(out, Ihat(a1 + 1, a2, a3, a4, a5 - 1), a1)
    out = gt_add(out, Ihat(a1 + 1, a2, a3 - 1, a4, a5), -a1)
    out = gt_add(out, Ihat(a1, a2 + 1, a3, a4, a5 - 1), a2)
    out = gt_add(out, Ihat(a1, a2 + 1, a3, a4 - 1, a5), -a2)
    return gt_scale(out, 1 / pref)


def _factorized(a1, a2, a3, a4, a5):
    n5 = -a5
    out = {}
    # D5^{n5} = (D1 + D3 - 2 k.r)^{n5}
    for i in range(n5 + 1):
        for j in range(n5 + 1 - i):
            l = n5 - i - j
            coef = sp.Rational(factorial(n5), factorial(i) * factorial(j) * factorial(l)) * (-2) ** l
            for t in range(l // 2 + 1):
                Ak = Atens(l, t, a1 - i, a2)              # p = q, (q^2)^{...} = 1
                if not Ak:
                    continue
                # contract {g^t q^{l-2t}} with r^l: Ncount * (r^2)^t (q.r)^{l-2t}
                for (c2, x3, x4) in expand_dot_qr(l - 2 * t):
                    Gr = G(a3 - j - t - x3, a4 - x4)
                    if not Gr:
                        continue
                    out = gt_add(out, gt_mul(Ak, Gr), coef * Ncount(l, t) * c2)
    return out


def _nested_a2(a1, a2, a3, a4, a5):
    """a2 <= 0, a1, a5 > 0: k-loop with D1 = k^2, D5 = (r-k)^2, numerator D2^{n2} = (D1 - 2 k.q + 1)^{n2}"""
    n2 = -a2
    out = {}
    for i in range(n2 + 1):
        for j in range(n2 + 1 - i):
            l = n2 - i - j
            coef = sp.Rational(factorial(n2), factorial(i) * factorial(j) * factorial(l)) * (-2) ** l
            for t in range(l // 2 + 1):
                Ak = Atens(l, t, a1 - i, a5)              # (r^2)^{D/2+t-(a1-i)-a5} {g^t r^{l-2t}}
                if not Ak:
                    continue
                powD3 = Dv / 2 + t - (a1 - i) - a5          # extra power of D3 (non-integer)
                # contract with q^l: Ncount * (q^2)^t (q.r)^{l-2t}
                for (c2, x3, x4) in expand_dot_qr(l - 2 * t):
                    Gr = G(a3 - powD3 - x3, a4 - x4)
                    if not Gr:
                        continue
                    out = gt_add(out, gt_mul(Ak, Gr), coef * Ncount(l, t) * c2)
    return out


def _nested_a1(a1, a2, a3, a4, a5):
    """a1 <= 0, a2, a5 > 0: k' = k - q; D2 = k'^2, D5 = (p - k')^2 with p = r - q, D1 = D2 + 2 k'.q + 1"""
    n1 = -a1
    out = {}
    for i in range(n1 + 1):
        for j in range(n1 + 1 - i):
            l = n1 - i - j
            coef = sp.Rational(factorial(n1), factorial(i) * factorial(j) * factorial(l)) * 2 ** l
            for t in range(l // 2 + 1):
                Ak = Atens(l, t, a2 - i, a5)              # (p^2)^{D/2+t-(a2-i)-a5} = D4^{...}
                if not Ak:
                    continue
                powD4 = Dv / 2 + t - (a2 - i) - a5
                for (c2, x3, x4) in expand_dot_pq(l - 2 * t):
                    Gr = G(a3 - x3, a4 - powD4 - x4)
                    if not Gr:
                        continue
                    out = gt_add(out, gt_mul(Ak, Gr), coef * Ncount(l, t) * c2)
    return out


# ---- I1: Ihat(1,1,1,1,1) = 6 zeta3
I11111 = gt_to_expr(Ihat(1, 1, 1, 1, 1))
serI = laurent(I11111, e, 0)
check('I1  Ihat(1,1,1,1,1) = 6 zeta_3 + O(eps) (own IBP + tensor code)', sp.simplify(serI - 6 * sp.zeta(3)) == 0)

# ----------------------------------------------------------------------------- Dirac traces of the diagrams
# Minkowski momenta k, r, q.  Slots: ('i', name) = gamma^name ; ('p', name) = slashed momentum
def lin_trace(slots_lin):
    """slots_lin: list of slots; a momentum slot may be ('p', [(coef, name), ...]) (linear combination)."""
    choices = []
    for s_ in slots_lin:
        if s_[0] == 'p' and isinstance(s_[1], list):
            choices.append([(c, ('p', nm)) for c, nm in s_[1]])
        else:
            choices.append([(1, s_)])
    tot = 0
    for combo in itertools.product(*choices):
        coef = 1
        sl = []
        for c, s_ in combo:
            coef *= c
            sl.append(s_)
        tot += coef * trace(sl)
    return sp.expand(tot)


kq = [(1, 'k'), (-1, 'q')]
rq = [(1, 'r'), (-1, 'q')]
# fermion flow: mu -> S(k) -> ... ; trace written against the fermion flow (see the derivation in the chapter)
diagrams = {
    # V: mu -> k -> alpha -> r -> nu -> (r-q) -> alpha' -> (k-q) -> mu ; gluon alpha-alpha' carries k-r
    'V': ([('i', 'mu'), ('p', kq), ('i', 'al'), ('p', rq), ('i', 'nu'), ('p', 'r'), ('i', 'al'), ('p', 'k')], (1, 1, 1, 1, 1)),
    # S1: self-energy on the k line: mu -> k -> al -> r -> al -> k -> nu -> (k-q) -> mu
    'S1': ([('i', 'mu'), ('p', kq), ('i', 'nu'), ('p', 'k'), ('i', 'al'), ('p', 'r'), ('i', 'al'), ('p', 'k')], (2, 1, 1, 0, 1)),
    # S2: self-energy on the (k-q) line
    'S2': ([('i', 'mu'), ('p', kq), ('i', 'al'), ('p', rq), ('i', 'al'), ('p', kq), ('i', 'nu'), ('p', 'k')], (1, 2, 0, 1, 1)),
}
# conversion of Minkowski scalar products to Euclidean D's (Q^2 = 1 units; Minkowski a.b = -(a.b)_E):
d1, d2, d3, d4, d5, Q2 = sp.symbols('d1 d2 d3 d4 d5 Q2')
mink = {
    dot('k', 'k'): -d1, dot('r', 'r'): -d3, dot('q', 'q'): -Q2,
    dot('k', 'q'): -(d1 + Q2 - d2) / 2, dot('q', 'r'): -(d3 + Q2 - d4) / 2, dot('k', 'r'): -(d1 + d3 - d5) / 2,
}


def numerator(slots, proj):
    tr = lin_trace(slots)
    if proj == 'g':          # -g_{mu nu} contraction
        tr = contract(sp.expand(-tr * sp.Symbol('g_mu_nu')))
    elif proj == 'qq':       # q_mu q_nu contraction
        tr = contract(sp.expand(tr * sp.Symbol('V_q_mu') * sp.Symbol('V_q_nu')))
    tr = contract(tr)        # contract the gluon index al
    tr = sp.expand(tr.subs(Dsym, Dv))
    return sp.expand(tr.subs(mink))


def integrate(numer, a):
    """Minkowski int int d^Dk d^Dr/(2pi)^{2D} numer/prod (p_i^2)^{a_i}  ->  -(-1)^{sum a}/(4pi)^D sum c Ihat(a - n)
    returned as GT (coefficient of (Q^2)^{D - sum a + ...}/(4pi)^D); Q2 = 1 units."""
    poly = sp.Poly(numer, d1, d2, d3, d4, d5, Q2)
    out = {}
    sgn = -(-1) ** sum(a)
    for (n1, n2, n3, n4, n5, nq), c in poly.terms():
        Ival = Ihat(a[0] - n1, a[1] - n2, a[2] - n3, a[3] - n4, a[4] - n5)
        if Ival:
            out = gt_add(out, Ival, sgn * c)
    return out


# ---- L0: one-loop normalisation from the same machinery
# Pi0^{mu nu} = i (-1) N_c e_q^2 int d^Dp/(2pi)^D Tr[g^mu S(p) g^nu S(p-q)], S(p) = i pslash/p^2
#  => -g_{mu nu} Pi0^{mu nu} = i * N_c e_q^2 * int Tr[...]/(p^2 (p-q)^2) * (-g)  with i (-1) i^2 = i
tr0 = contract(sp.expand(-lin_trace([('i', 'mu'), ('p', 'k'), ('i', 'nu'), ('p', kq)]) * sp.Symbol('g_mu_nu')))
tr0 = sp.expand(tr0.subs(Dsym, Dv).subs(mink))
# one loop: int d^Dk/(2pi)^D (Minkowski) N/((k^2)^1((k-q)^2)^1) = i (-1)^{2}/(4pi)^{D/2} sum c G(1-n1, 1-n2)
poly0 = sp.Poly(tr0, d1, d2, Q2)
one = {}
for (n1, n2, nq), c in poly0.terms():
    one = gt_add(one, G(1 - n1, 1 - n2), c)
# -g Pi0 = i * [ i * one/(4pi)^{D/2} ]  = -one/(4pi)^{D/2};  Pi0 = -g Pi0 /((D-1) q^2), q^2 = -Q2 = -1
Pi0 = gt_scale(one, sp.Integer(-1) / ((Dv - 1) * (-1)))          # times N_c e_q^2 (Q^2)^{-eps}/(4pi)^{D/2}
ref0 = gt_scale(G(1, 1), 2 * (Dv - 2) / (Dv - 1))
check('L0  one loop from the same code: Pi_0 = N_c e_q^2 [2(D-2)/(D-1)] G(1,1) (Q^2)^-eps/(4pi)^{D/2}',
      sp.simplify(gt_to_expr(gt_add(Pi0, ref0, -1))) == 0)

# ---- two loops: Pi^{mu nu}_diag = g0^2 C_F N_c e_q^2 * int int Tr[...]/(...)   [constant i(-1)(ig)^2(-i) i^4 = g^2]
res_g = {}
res_qq = {}
per_diag = {}
for name, (slots, a) in diagrams.items():
    ng = numerator(slots, 'g')
    nq = numerator(slots, 'qq')
    Ig = integrate(ng, a)
    Iq = integrate(nq, a)
    per_diag[name] = Ig
    res_g = gt_add(res_g, Ig)
    res_qq = gt_add(res_qq, Iq)
# transversality: q_mu q_nu Pi^{mu nu} = 0 (sum)
check('W1  two loops: q_mu q_nu Pi^{mu nu} = 0 exactly (sum of V, S1, S2)', sp.simplify(gt_to_expr(res_qq)) == 0 or
      all(abs(sp.N(gt_to_expr(res_qq).subs(e, sp.Rational(kk, 31)), 40)) < 1e-30 for kk in (2, -3, 5)))
# Pi = -g Pi^{mu nu}/((D-1) q^2) with q^2 = -Q2 = -1 ;  result multiplies g0^2 C_F N_c e_q^2 (Q^2)^{-2eps}/(4pi)^D
Pi1 = gt_scale(res_g, sp.Integer(1) / ((Dv - 1) * (-1)))
r1 = -4 * (1 - e) * (2 - e + 2 * e ** 2) / (e * (3 - 2 * e))
r2 = 16 * (1 - e) * (1 - 2 * e) * (2 - 2 * e + e ** 2) / (e * (3 - 2 * e) * (2 - 3 * e))
ref1 = gt_add(gt_scale(gt_mul(G(1, 1), G(1, 1)), r1), gt_scale(gt_mul(G(1, 1), G(1 + e, 1)), r2))
diff1 = gt_add(Pi1, ref1, -1)
okF1 = (not diff1) or all(abs(sp.N(gt_to_expr(diff1).subs(e, sp.Rational(kk, 37)), 40)) < 1e-30 for kk in (1, -5, 7, 11))
check('F1  Pi^(1)_bare = N_c e_q^2 C_F g0^2 (Q^2)^{-2eps}/(4pi)^D [r1 G11^2 + r2 G11 G(1+eps,1)] (VF-EE-7), exact', okF1)
keys = set(Pi1.keys())
k_fac = set(gt_mul(G(1, 1), G(1, 1)).keys())
k_nes = set(gt_mul(G(1, 1), G(1 + e, 1)).keys())
check('E1  only the two transcendental structures G(1,1)^2 and G(1,1) G(1+eps,1) occur', keys <= (k_fac | k_nes))

# ---- S1: diagram-by-diagram expansion with the MS-bar factor
# Pihat = mu^{2eps} S_eps^{-1} Pi_bare, g0^2 = 4 pi a_s mu^{2eps} S^{-1}: Pihat^(1)/units = (3/16) e^{2 eps gE} e^{-2 eps L} [ ... ]
L = sp.Symbol('L')
EG = sp.EulerGamma


def msbar_series(gt):
    ex = sp.Rational(3, 16) * sp.exp(2 * e * EG) * sp.exp(-2 * e * L) * gt_to_expr(gt) / ((Dv - 1) * (-1))
    return sp.expand(laurent(ex, e, 0))


sV = msbar_series(per_diag['V'])
sS = msbar_series(gt_add(per_diag['S1'], per_diag['S2']))
z3 = sp.zeta(3)
refV = 1 / (4 * e ** 2) + (sp.Rational(17, 12) - L / 2) / e + L ** 2 / 2 - sp.Rational(17, 6) * L - 3 * z3 - sp.pi ** 2 / 24 + sp.Rational(259, 36)
refS = -1 / (4 * e ** 2) + (L / 2 - sp.Rational(25, 24)) / e - L ** 2 / 2 + sp.Rational(25, 12) * L + sp.pi ** 2 / 24 - sp.Rational(541, 144)
print('      V     :', sp.collect(sV, e))
print('      S1+S2 :', sp.collect(sS, e))
check('S1a diagram V (Feynman gauge) = 1/(4e^2) + (17/12 - L/2)/e + L^2/2 - 17L/6 - 3z3 - pi^2/24 + 259/36', sp.simplify(sV - refV) == 0)
check('S1b S1+S2 (Feynman gauge) = -1/(4e^2) + (L/2 - 25/24)/e - L^2/2 + 25L/12 + pi^2/24 - 541/144', sp.simplify(sS - refS) == 0)
check('S1c sum = 3/(8e) + 55/16 - 3 z3 - 3L/4 (local simple pole only)', sp.simplify(sV + sS - (sp.Rational(3, 8) / e + sp.Rational(55, 16) - 3 * z3 - sp.Rational(3, 4) * L)) == 0)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
