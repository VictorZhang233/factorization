"""
s2_eikonal_identity.py -- item (2): eikonal identities.

 (1) abelian eikonal identity  sum_{pi in S_m} prod_{j=1}^m 1/(a_pi(1)+...+a_pi(j)) = prod_j 1/a_j ,  m = 2..6
 (2) with the adiabatic regulator (each gluon carries +i eps => j-th cumulative denominator carries + i j eps)
     the identity is EXACT at finite eps (past and future lines); with a uniform +i eps on every denominator it
     holds only for eps -> 0 (negative control);
 (3) the m = 2 case:  1/(n.k1 n.(k1+k2)) + 1/(n.k2 n.(k1+k2)) = 1/(n.k1 n.k2);
 (4) shuffle identity  sum_{sigma in Sh(p,q)} E(sigma) = E(k_1..k_p) E(l_1..l_q)  (p,q <= 3);
 (5) eikonal Ward identity  n.k/((n.l+i0)(n.(l+k)+i0)) = 1/(n.l+i0) - 1/(n.(l+k)+i0)
     <=> [i/(n.(l+k))] (i g n.k t^a) [i/(n.l)] = g t^a [ i/(n.(l+k)) - i/(n.l) ]  (same form as the quark line);
 (6) Wilson-line Ward identity: a scalar-polarized gluon (eps^mu = q^mu, colour T_q) inserted in all m+1
     positions of the m-gluon term of W[0,-inf] gives
        sum = -g T_q Y  +  g sum_{p=0}^{m-1} Z_p  T_m..T_{p+2} [T_q,T_{p+1}] T_p..T_1
     (Y = original term; Z_p = propagators of the line with gluon p+1 carrying k_{p+1}+q); abelian: sum = -g Y.
     Future-pointing analogue: sum = +g Y' T_q-structure (checked numerically);
 (7) non-abelian exponentiation at O(g^2): W^(2) - (W^(1))^2/2 contains only commutators (webs), and vanishes
     for commuting generators.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *
import sympy as sp

R = Report('s2_eikonal_identity')
eps = sp.symbols('epsilon', positive=True)
A = sp.symbols('a1:7', real=True)

# ------------------------------------------------------------------ (1),(2)
print('--- (1),(2) abelian eikonal identity ---')
from fractions import Fraction
import random
random.seed(5)


def eik_sum_exact(vals, eps_val=None, future=False):
    """exact (Fraction / Gaussian-rational via sympy Rational+I) sum over orderings"""
    m = len(vals); tot = 0
    for perm in itertools.permutations(range(m)):
        term = 1
        for j in range(1, m + 1):
            if future:
                Kc = sum(vals[perm[i]] for i in range(j - 1, m)); c = m - j + 1
                term *= (-sp.I) / (Kc - sp.I * c * eps_val) if eps_val is not None else 1 / Kc
            else:
                Kc = sum(vals[perm[i]] for i in range(j)); c = j
                term *= sp.I / (Kc + sp.I * c * eps_val) if eps_val is not None else 1 / Kc
        tot += term
    return tot


for m in range(2, 8):
    if m <= 4:
        a = A[:m]
        lhs = eik_sum_exact(list(a))
        rhs = sp.prod([1 / x for x in a])
        ok = sp.simplify(sp.together(lhs - rhs)) == 0
        R.flag(f'(1) m={m}: sum over m! orderings == product (symbolic)', ok)
    else:
        ok = True
        for trial in range(3):
            while True:   # reject points on the singular locus (a vanishing partial sum = a pole of the lhs)
                vals = [sp.Rational(random.randint(-97, 97) or 1, random.randint(1, 89)) for _ in range(m)]
                if all(sum(vals[i] for i in S) != 0 for r in range(1, m + 1) for S in itertools.combinations(range(m), r)):
                    break
            lhs = eik_sum_exact(vals)
            rhs = sp.prod([1 / x for x in vals])
            ok = ok and sp.nsimplify(lhs - rhs) == 0
        R.flag(f'(1) m={m}: sum over m! orderings == product (exact rationals, 3 random points)', ok)

for m in range(2, 5):
    a = A[:m]
    # past line: cumulative from -infinity, j-th denominator carries + i j eps
    lhs = 0; lhs_unif = 0
    for perm in itertools.permutations(range(m)):
        term = 1; term_u = 1
        for j in range(1, m + 1):
            term *= sp.I / (sum(a[perm[i]] for i in range(j)) + sp.I * j * eps)
            term_u *= sp.I / (sum(a[perm[i]] for i in range(j)) + sp.I * eps)
        lhs += term; lhs_unif += term_u
    rhs = sp.prod([sp.I / (x + sp.I * eps) for x in a])
    R.flag(f'(2) past   m={m}: exact at finite eps with additive regulator', sp.simplify(sp.together(lhs - rhs)) == 0)
    # future line: cumulative from +infinity, -i/(K - i c eps)
    lhs_f = 0
    for perm in itertools.permutations(range(m)):
        term = 1
        for j in range(1, m + 1):
            K = sum(a[perm[i]] for i in range(j - 1, m))
            term *= -sp.I / (K - sp.I * (m - j + 1) * eps)
        lhs_f += term
    rhs_f = sp.prod([-sp.I / (x - sp.I * eps) for x in a])
    R.flag(f'(2) future m={m}: exact at finite eps with additive regulator', sp.simplify(sp.together(lhs_f - rhs_f)) == 0)
    if m == 2:
        diff_u = sp.simplify(sp.together(lhs_unif - rhs))
        lim0 = sp.limit(diff_u.subs({a[0]: sp.Rational(3, 7), a[1]: -sp.Rational(5, 11)}), eps, 0)
        R.flag('(2) negative control: uniform +i eps on every denominator is NOT exact at finite eps, -> 0 as eps->0',
               diff_u != 0 and lim0 == 0, f'  [difference = {sp.factor(diff_u)}]')

for m in [5, 6]:
    ok = True
    for trial in range(2):
        vals = [sp.Rational(random.randint(-97, 97) or 1, random.randint(1, 89)) for _ in range(m)]
        ev = sp.Rational(random.randint(1, 50), random.randint(51, 400))
        lp = sp.expand(eik_sum_exact(vals, ev) - sp.prod([sp.I / (x + sp.I * ev) for x in vals]))
        lf = sp.expand(eik_sum_exact(vals, ev, future=True) - sp.prod([-sp.I / (x - sp.I * ev) for x in vals]))
        ok = ok and sp.simplify(lp) == 0 and sp.simplify(lf) == 0
    R.flag(f'(2) m={m}: exact at finite eps (past & future), exact Gaussian rationals, 2 random points', ok)

# ------------------------------------------------------------------ (3)
k1, k2 = sp.symbols('nk1 nk2', real=True)
expr = 1 / (k1 * (k1 + k2)) + 1 / (k2 * (k1 + k2)) - 1 / (k1 * k2)
R.flag('(3) 1/(n.k1 n.(k1+k2)) + (1<->2) = 1/(n.k1 n.k2)', sp.simplify(expr) == 0)

# ------------------------------------------------------------------ (4) shuffle identity
print('--- (4) shuffle identity ---')


def E(qs):
    out = 1
    for j in range(1, len(qs) + 1):
        out *= 1 / sum(qs[:j])
    return out


def shuffles(x, y):
    if not x:
        yield list(y); return
    if not y:
        yield list(x); return
    for rest in shuffles(x[1:], y):
        yield [x[0]] + rest
    for rest in shuffles(x, y[1:]):
        yield [y[0]] + rest


K = sp.symbols('k1:4', real=True); Lq = sp.symbols('l1:4', real=True)
for p in range(1, 4):
    for q in range(1, 4):
        lhs = sum(E(sh) for sh in shuffles(list(K[:p]), list(Lq[:q])))
        rhs = E(list(K[:p])) * E(list(Lq[:q]))
        R.flag(f'(4) shuffle (p,q)=({p},{q}): {sp.binomial(p+q,p)} shuffles', sp.simplify(sp.together(lhs - rhs)) == 0)

# ------------------------------------------------------------------ (5) eikonal Ward identity
l_, k_ = sp.symbols('nl nk', real=True)
w1 = sp.simplify(k_ / ((l_ + sp.I * eps) * (l_ + k_ + sp.I * eps)) - (1 / (l_ + sp.I * eps) - 1 / (l_ + k_ + sp.I * eps)))
g = sp.symbols('g', positive=True)
w2 = sp.simplify(sp.I / (l_ + k_ + sp.I * eps) * (sp.I * g * k_) * sp.I / (l_ + sp.I * eps)
                 - g * (sp.I / (l_ + k_ + sp.I * eps) - sp.I / (l_ + sp.I * eps)))
R.flag('(5) eikonal Ward identity (exact, same i0 on both propagators)', w1 == 0 and w2 == 0)

# ------------------------------------------------------------------ (6) Wilson-line Ward identity, numerically
print('--- (6) Wilson-line Ward identity (SU(3), random) ---')
rng = np.random.default_rng(11)
EPSN = 1e-3     # finite regulator; identities below are exact for the additive regulator


def herm():
    return np.einsum('a,aij->ij', rng.normal(size=8), TA)


def line_term_past(Ts, avals, epsn=EPSN):
    """m-gluon term of W[0,-inf], gluon 1 nearest -inf, unit polarization factors (n.eps_j = 1):
       prod (i g) * T_m...T_1 * prod_j i/(K_j + i j eps)  (g = 1)"""
    m = len(Ts)
    coef = (1j)**m
    for j in range(1, m + 1):
        coef *= 1j / (sum(avals[:j]) + 1j * j * epsn)
    M = I3.copy()
    for T in reversed(Ts):
        M = M @ T
    return coef * M


def line_term_future(Ts, avals, epsn=EPSN):
    """m-gluon term of W[inf,0], gluon 1 nearest 0: prod(i g) T_m..T_1 prod_j -i/(K'_j - i(m-j+1)eps)"""
    m = len(Ts)
    coef = (1j)**m
    for j in range(1, m + 1):
        coef *= -1j / (sum(avals[j - 1:]) - 1j * (m - j + 1) * epsn)
    M = I3.copy()
    for T in reversed(Ts):
        M = M @ T
    return coef * M


for m in range(1, 5):
    Ts = [herm() for _ in range(m)]
    av = list(rng.normal(size=m))
    Tq = herm(); b = rng.normal()
    # insertion of the K-gluon (polarization q^mu => n.eps = n.q = b) at position p (after p gluons from -inf)
    tot = np.zeros((3, 3), dtype=complex)
    for p in range(m + 1):
        Ts_p = Ts[:p] + [Tq] + Ts[p:]
        av_p = av[:p] + [b] + av[p:]
        # line_term_past uses unit polarizations; the K-gluon's polarization factor is n.q = b, taken with the
        # same adiabatic shift as its momentum (b -> b + i eps) so that the telescoping is exact at finite eps
        tot += (b + 1j * EPSN) * line_term_past(Ts_p, av_p)
    Y = line_term_past(Ts, av)
    # prediction (g=1): -T_q Y + sum_p Z_p T_m..T_{p+2}[T_q,T_{p+1}]T_p..T_1 ,
    # Z_p = line with gluon p+1 momentum a_{p+1}+b (regulators: the K-gluon adds one unit of eps to every
    # denominator to its right -- reproduced by giving the merged gluon the extra eps)
    pred = -Tq @ Y
    for p in range(m):
        Ts_c = Ts[:p] + [Tq @ Ts[p] - Ts[p] @ Tq] + Ts[p + 1:]
        av_c = av[:p] + [av[p] + b] + av[p + 1:]
        # regulator bookkeeping: denominators j >= p+1 carry (j+1) eps in the full sum
        m_ = len(Ts_c); coef = (1j)**m_
        for j in range(1, m_ + 1):
            shift = 1 if j >= p + 1 else 0
            coef *= 1j / (sum(av_c[:j]) + 1j * (j + shift) * EPSN)
        M = I3.copy()
        for T in reversed(Ts_c):
            M = M @ T
        pred += coef * M
    R.check(f'(6) past   m={m}: sum over K-gluon insertions == -T_q Y + commutator terms (exact, finite eps)',
            rel(tot, pred), 1e-11)
    # abelian case: all generators equal => commutators vanish => sum = -Y (times charge)
    Ts_ab = [I3 for _ in range(m)]
    tot_ab = sum((b + 1j * EPSN) * line_term_past(Ts_ab[:p] + [I3] + Ts_ab[p:], av[:p] + [b] + av[p:]) for p in range(m + 1))
    R.check(f'(6) past   m={m}: abelian sum == -Y', rel(tot_ab, -line_term_past(Ts_ab, av)), 1e-11)

# exact version (eps -> 0 limit taken analytically with sympy for m = 2, abelian and colour-ordered)
a1, a2, bq = sp.symbols('a1 a2 b', real=True)
# abelian m=2: insertions at p=0,1,2 of the K gluon (vertex i g b), unit vertices i g for the others (g=1)
def Epast(vals):
    out = 1
    for j in range(1, len(vals) + 1):
        out *= sp.I / sum(vals[:j])
    return out
ab_sum = sum(bq * sp.I**3 * Epast(v) for v in [[bq, a1, a2], [a1, bq, a2], [a1, a2, bq]])
R.flag('(6) exact (eps->0) abelian m=2: sum = -Y', sp.simplify(ab_sum - (-(sp.I**2) * Epast([a1, a2]))) == 0)

for m in range(1, 4):
    Ts = [herm() for _ in range(m)]
    av = list(rng.normal(size=m))
    Tq = herm(); b = rng.normal()
    tot = sum((b - 1j * EPSN) * line_term_future(Ts[:p] + [Tq] + Ts[p:], av[:p] + [b] + av[p:]) for p in range(m + 1))
    Y = line_term_future(Ts, av)
    # future line (gluon 1 nearest the finite end 0): the endpoint term is +T_q Y with T_q at the finite end
    # (rightmost), plus commutators
    pred = Y @ Tq
    for p in range(m):
        # K-gluon merged with gluon p+1 (numbering from the finite end); colour T..[T_q, T_{p+1}]..
        Ts_c = Ts[:p] + [Tq @ Ts[p] - Ts[p] @ Tq] + Ts[p + 1:]
        av_c = av[:p] + [av[p] + b] + av[p + 1:]
        m_ = len(Ts_c); coef = (1j)**m_
        for j in range(1, m_ + 1):
            shift = 1 if j <= p + 1 else 0
            coef *= -1j / (sum(av_c[j - 1:]) - 1j * (m_ - j + 1 + shift) * EPSN)
        M = I3.copy()
        for T in reversed(Ts_c):
            M = M @ T
        pred += coef * M
    R.check(f'(6) future m={m}: sum over K-gluon insertions == +Y T_q + commutator terms (exact, finite eps)', rel(tot, pred), 1e-11)
    Ts_ab = [I3 for _ in range(m)]
    tot_ab = sum((b - 1j * EPSN) * line_term_future(Ts_ab[:p] + [I3] + Ts_ab[p:], av[:p] + [b] + av[p:]) for p in range(m + 1))
    R.check(f'(6) future m={m}: abelian sum == +Y', rel(tot_ab, line_term_future(Ts_ab, av)), 1e-11)

# ------------------------------------------------------------------ (7) exponentiation at O(g^2)
print('--- (7) non-abelian exponentiation at O(g^2) ---')
Rm = 4
Tm = [herm() for _ in range(Rm)]
am = rng.normal(size=Rm)
cm = rng.normal(size=Rm) + 1j * rng.normal(size=Rm)
EP = 0.3
W1 = sum(1j * cm[r] * Tm[r] * 1j / (am[r] + 1j * EP) for r in range(Rm))
W2 = sum((1j * cm[r]) * (1j * cm[s]) * Tm[s] @ Tm[r] * 1j / (am[r] + 1j * EP) * 1j / (am[r] + am[s] + 2j * EP)
         for r in range(Rm) for s in range(Rm))
web = sum(0.25 * (1j * cm[r]) * (1j * cm[s]) * (Tm[s] @ Tm[r] - Tm[r] @ Tm[s])
          * (1j / (am[r] + 1j * EP) * 1j / (am[r] + am[s] + 2j * EP) - 1j / (am[s] + 1j * EP) * 1j / (am[r] + am[s] + 2j * EP))
          for r in range(Rm) for s in range(Rm))
R.check('(7) W^(2) - (W^(1))^2/2 == (1/4) sum [T_s,T_r](E(r,s)-E(s,r))  (pure commutator / web)', rel(W2 - W1 @ W1 / 2, web), 1e-12)
# abelian: commuting generators -> W^(2) = (W^(1))^2/2 exactly (exponentiation)
Tab = [rng.normal() * I3 for _ in range(Rm)]
W1a = sum(1j * cm[r] * Tab[r] * 1j / (am[r] + 1j * EP) for r in range(Rm))
W2a = sum((1j * cm[r]) * (1j * cm[s]) * Tab[s] @ Tab[r] * 1j / (am[r] + 1j * EP) * 1j / (am[r] + am[s] + 2j * EP)
          for r in range(Rm) for s in range(Rm))
R.check('(7) abelian: W^(2) == (W^(1))^2/2 exactly at finite eps', rel(W2a, W1a @ W1a / 2), 1e-12)
# commutator structure: [T_s,T_r] = i f^{src} T_c  -> the web is in the adjoint channel (single generator)
Wc = np.array([np.trace(web @ TA[c]) * 2 for c in range(8)])
recon = np.einsum('c,cij->ij', Wc, TA)
R.check('(7) web term is a pure generator (traceless, in span{t^c})', rel(web, recon), 1e-12)

R.summary()
