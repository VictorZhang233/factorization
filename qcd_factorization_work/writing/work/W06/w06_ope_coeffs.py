r"""
w06_ope_coeffs.py -- writer W06: leading-order Wilson coefficients of the vector-current correlator OPE
(thm:ee-ope), derived from scratch in the normalisation of VF-CONV-12:
    Pi^{mu nu}(q) = i int d^4x e^{iqx} <T j^mu(x) j^nu(0)> = (q^mu q^nu - q^2 g^{mu nu}) Pi(q^2),  j = e_q qbar gamma q.

 G   gluon condensate:  Pi  ->  e_q^2 (1/12) <(a_s/pi) G^a_{mn} G^{a mn}> / Q^4      (Q^2 = -q^2)
     method: hard-region (Taylor) expansion to O(k^2) of the forward one-loop amplitude with two soft background
     gluons (momenta k, -k), sum of the 6 orderings, DR, Minkowski Feynman rules as in Ch2;
     vacuum average of the constant field strength  <g^2 G^a_{ra} G^b_{sb}> = d^{ab}/(N^2-1) (g_rs g_ab - g_rb g_as) <g^2 G^2>/12
     implemented by a linear functional  <k_a k_b A_c A'_d> = y1 g_ab g_cd + y2 (g_ac g_bd + g_bc g_ad),  2(y1-y2) = X;
     checks: (i) zero-momentum term vanishes, (ii) Ward identity at O(k^3), (iii) independence of y2, (iv) finite.
 Q   quark condensate:   Pi  ->  e_q^2 2 m_q <qbar q> / Q^4  (with <qbar(0) q(x)> = <qbar q>/(4N_c) [1 - (i m/4) xslash])
 M   mass term of the unit operator:  Pi -> -(N_c e_q^2/(2 pi^2)) m^2/Q^2 = (N_c e_q^2/(12 pi^2)) (-6 m^2/Q^2)
Run: python3 -I w06_ope_coeffs.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itertools
from math import factorial
import sympy as sp
from w06_dtrace import trace, contract, dot, D as Dsym

e = sp.Symbol('eps')
Dv = 4 - 2 * e
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


t = sp.Symbol('t')            # bookkeeping parameter for the soft gluon momentum k -> t k


def lin_trace(slots_lin):
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


# ------------------------------------------------------------------------------------------- G
# loop momentum p; line momenta along the fermion flow mu -> v1 -> v2 -> v3 -> mu
kick = {'nu': [(-1, 'q')], 'al': [(t, 'k')], 'be': [(-t, 'k')]}
vertex_slot = {'nu': ('i', 'nu'), 'al': ('p', 'u'), 'be': ('p', 'w')}   # u = A (polarisation), w = A'


def add(m1, m2):
    d = {}
    for c, n in m1 + m2:
        d[n] = d.get(n, 0) + c
    return [(c, n) for n, c in d.items() if c != 0]


# Euclidean symbols after Wick rotation: P1 = p_E^2, P2 = (p+q)_E^2, Q2 = q_E^2
P1, P2, Q2 = sp.symbols('P1 P2 Q2', positive=True)
names = ['p', 'q', 'k', 'u', 'w']
dE = {}
for a_ in names:
    for b_ in names:
        aa, bb = sorted([a_, b_])
        dE[(aa, bb)] = sp.Symbol('E_%s_%s' % (aa, bb))


def E(a_, b_):
    aa, bb = sorted([a_, b_])
    return dE[(aa, bb)]


def denom_series(mom, order=2):
    """1/(Minkowski mom^2) for mom = P + c t k (P in {p, p+q}) as a series in t up to t^order, in Euclidean form:
    Minkowski X.Y = -(X.Y)_E.  Returns (series_in_t, P_label) with P^2_E -> symbol."""
    coefs = dict((n, c) for c, n in mom)
    ck = coefs.get('k', 0)
    base = {n: c for n, c in coefs.items() if n != 'k'}
    if base == {'p': 1}:
        PE2 = P1
        PdotK = E('p', 'k')
    elif base == {'p': 1, 'q': 1}:
        PE2 = P2
        PdotK = E('p', 'k') + E('k', 'q')
    else:
        raise ValueError(mom)
    # Minkowski (P + ck k)^2 = -(PE2 + 2 ck PdotK + ck^2 kk_E)
    x = 2 * ck * PdotK + ck ** 2 * E('k', 'k')
    ser = sum((-x) ** n / PE2 ** (n + 1) for n in range(order + 1))
    return -sp.expand(ser)                       # 1/(-(PE2 + x)) = -1/(PE2 + x)


def mink_to_E(expr):
    """replace Minkowski dot symbols dot_a_b by -(a.b)_E"""
    rep = {}
    for a_ in names:
        for b_ in names:
            if a_ <= b_:
                rep[dot(a_, b_)] = -E(a_, b_)
    return expr.xreplace(rep)


def truncate_t(expr, order):
    expr = sp.expand(expr)
    return sum(expr.coeff(t, n) * t ** n for n in range(order + 1))


total = {0: 0, 1: 0, 2: 0}
for perm in itertools.permutations(['nu', 'al', 'be']):
    line1 = [(1, 'p'), (1, 'q')]
    line2 = add(line1, kick[perm[0]])
    line3 = add(line2, kick[perm[1]])
    line4 = add(line3, kick[perm[2]])
    assert sorted(line4, key=lambda z: z[1]) == [(1, 'p')], line4
    slots = [('i', 'mu'), ('p', line4), vertex_slot[perm[2]], ('p', line3), vertex_slot[perm[1]], ('p', line2), vertex_slot[perm[0]], ('p', line1)]
    tr = lin_trace(slots)
    tr = contract(sp.expand(-tr * sp.Symbol('g_mu_nu')))          # -g_{mu nu} projection
    tr = sp.expand(tr.subs(Dsym, Dv))
    num = truncate_t(mink_to_E(tr), 2)
    den = 1
    for L_ in (line1, line2, line3, line4):
        den = sp.expand(truncate_t(den * denom_series(L_), 2))
    integrand = truncate_t(sp.expand(num * den), 2)
    for n in range(3):
        total[n] += sp.expand(integrand.coeff(t, n))

# integrand in Euclidean variables; replace (p.q)_E = (P2 - P1 - Q2)/2 and p.p = P1
def reduce_pp(expr):
    return sp.expand(expr.xreplace({E('p', 'p'): P1, E('p', 'q'): (P2 - P1 - Q2) / 2, E('q', 'q'): Q2}))


def Gfun(a, b):
    return sp.gamma(a + b - Dv / 2) * sp.gamma(Dv / 2 - a) * sp.gamma(Dv / 2 - b) / (sp.gamma(a) * sp.gamma(b) * sp.gamma(Dv - a - b))


def Acoef(m, tt, al, be):
    return sp.gamma(al + be - Dv / 2 - tt) * sp.gamma(Dv / 2 - al + m - tt) * sp.gamma(Dv / 2 - be + tt) / (
        2 ** tt * sp.gamma(al) * sp.gamma(be) * sp.gamma(Dv - al - be + m))


def pairings(items, npairs):
    """all ways to choose npairs disjoint unordered pairs from the list of slot indices"""
    items = list(items)
    if npairs == 0:
        yield [], items
        return
    if len(items) < 2 * npairs:
        return
    first = items[0]
    rest = items[1:]
    # first is paired
    for i, other in enumerate(rest):
        remaining = rest[:i] + rest[i + 1:]
        for prs, singles in pairings(remaining, npairs - 1):
            yield [(first, other)] + prs, singles
    # first is single
    for prs, singles in pairings(rest, npairs):
        yield prs, [first] + singles


def tensor_integrate(expr):
    """Euclidean int d^Dp/pi^{D/2} of (polynomial in (p.X)_E, X in {k,u,w}) / (P1^a P2^b):
    = sum_t A(m,t; a,b) Q2^{D/2+t-a-b} {delta^t (-q)^{m-2t}} contracted with the X's."""
    expr = sp.expand(expr)
    gens = [P1, P2, E('k', 'p'), E('p', 'u'), E('p', 'w')]
    out = 0
    for term in sp.Add.make_args(expr):
        c, rest = term.as_independent(*gens)
        pw = {g_: 0 for g_ in gens}
        for f in sp.Mul.make_args(rest):
            b_, ex_ = f.as_base_exp()
            pw[b_] += ex_
        a = -pw[P1]
        b = -pw[P2]
        vecs = ['k'] * pw[E('k', 'p')] + ['u'] * pw[E('p', 'u')] + ['w'] * pw[E('p', 'w')]
        m = len(vecs)
        if a <= 0 or b <= 0:
            continue                                 # scaleless
        res = 0
        for tt in range(m // 2 + 1):
            A_ = Acoef(m, tt, a, b)
            if A_ == 0:
                continue
            cont = 0
            for prs, singles in pairings(range(m), tt):
                val = 1
                for (i, j) in prs:
                    val *= E(vecs[i], vecs[j])
                for i in singles:
                    val *= -E('q', vecs[i])          # P = -q
                cont += val
            res += A_ * Q2 ** (Dv / 2 + tt - a - b) * cont
        out += c * res
    return sp.expand(out)


# Minkowski integral: int d^Dp/(2pi)^D (...) with denominators written as -1/(P_E^2...): the series above already
# contains the Euclidean denominators with their signs; Wick rotation d^Dp = i d^Dp_E, and
# int d^Dp_E/(2pi)^D = (1/(4pi)^{D/2}) int d^Dp_E/pi^{D/2}.
def minkowski_integral(integrand):
    red = reduce_pp(integrand)
    return sp.I * tensor_integrate(red) / (4 * sp.pi) ** (Dv / 2)


# overall factor of the colour-stripped amplitude: i (def. of Pi) * (-1) (loop) * i^2 (gluon vertices i gamma)
#   * i^4 (propagators i pslash/p^2; the 1/p^2 are in den) = i
overall = sp.I
G0 = sp.simplify(overall * minkowski_integral(total[0]))
check('G0  zero-momentum two-gluon term vanishes (gauge invariance)', sp.simplify(G0) == 0)

amp2 = sp.expand(overall * minkowski_integral(total[2]))       # -g_{mu nu} Gamma_6^{mu nu}, O(k^2), Euclidean dots


def E_to_mink(expr):
    rep = {}
    for a_ in names:
        for b_ in names:
            if a_ <= b_ and (a_, b_) != ('p', 'p'):
                rep[E(a_, b_)] = -dot(a_, b_)
    rep[Q2] = -dot('q', 'q')
    return sp.expand(expr.xreplace(rep))


amp2M = E_to_mink(amp2)
# Ward identity: replace u -> k: must vanish (O(k^3))
ward = sp.simplify(amp2M.xreplace({dot('k', 'u'): dot('k', 'k'), dot('q', 'u'): dot('k', 'q'), dot('u', 'w'): dot('k', 'w')}))
check('G1  Ward identity: the O(k^2) amplitude vanishes for A -> k (transverse)', sp.simplify(ward) == 0)

y1, y2, Xc = sp.symbols('y1 y2 X')


def apply_functional(expr, y1v, y2v):
    expr = sp.expand(expr)
    gens = [dot(a_, b_) for a_ in ['k', 'q', 'u', 'w'] for b_ in ['k', 'q', 'u', 'w'] if a_ <= b_ and (a_, b_) != ('q', 'q')]
    P = sp.Poly(expr, *gens)
    out = 0
    for monom, coef in P.terms():
        kidx = ['ka', 'kb']
        used = 0
        fac = sp.Integer(1)
        for g_, n_ in zip(gens, monom):
            if n_ == 0:
                continue
            a_, b_ = g_.name.split('_')[1:]
            for _ in range(n_):
                idx = []
                for v in (a_, b_):
                    if v == 'k':
                        idx.append(kidx[used]); used += 1
                    elif v == 'u':
                        idx.append('c')
                    elif v == 'w':
                        idx.append('d')
                    else:
                        idx.append(None)
                if idx[0] is None and idx[1] is None:
                    fac *= g_
                elif idx[0] is None:
                    fac *= sp.Symbol('V_q_%s' % idx[1])
                elif idx[1] is None:
                    fac *= sp.Symbol('V_q_%s' % idx[0])
                else:
                    i1, i2 = sorted(idx)
                    fac *= sp.Symbol('g_%s_%s' % (i1, i2))
        assert used == 2, (monom, used)
        functional = y1v * sp.Symbol('g_ka_kb') * sp.Symbol('g_c_d') + y2v * (sp.Symbol('g_c_ka') * sp.Symbol('g_d_kb') + sp.Symbol('g_c_kb') * sp.Symbol('g_d_ka'))
        val = contract(sp.expand(fac * functional))
        out += coef * val
    return sp.expand(out.subs(Dsym, Dv))


# Pi_(2)^{mu nu} = (1/2)[identical background field] (1/2)[Tr t^a t^b = delta^ab/2] <Gamma_6>  with 2(y1-y2) = <g^2 G^2>/12
# (sum over colour a of delta^{aa}/(N^2-1) = 1);  Pi_(2) = -g Pi^{mu nu}/((D-1) q^2)
Gsq = sp.Symbol('GG')          # <g^2 G^a_{mn} G^{a mn}>
res_by_y2 = []
for y2v in (sp.Integer(0), sp.Integer(1), sp.Rational(-3, 7)):
    y1v = y2v + Gsq / 24
    val = apply_functional(amp2M, y1v, y2v) / 4
    Pi2 = sp.simplify(val / ((Dv - 1) * dot('q', 'q')))
    res_by_y2.append(Pi2)
check('G2  result independent of the gauge-variant part y2 of the averaging functional',
      sp.simplify(res_by_y2[0] - res_by_y2[1]) == 0 and sp.simplify(res_by_y2[0] - res_by_y2[2]) == 0)
Pi2 = res_by_y2[0]
Qs = sp.Symbol('Qs', positive=True)
Pi2Q = sp.simplify(Pi2.subs(dot('q', 'q'), -Qs))
lim = sp.limit(sp.simplify(Pi2Q * Qs ** 2), e, 0)
print('      Pi_(2) * Q^4 at eps -> 0 :', sp.simplify(lim), '   (expected <g^2 G^2>/(48 pi^2) = <(a_s/pi) G^2>/12)')
check('G3  gluon-condensate coefficient: Pi -> (1/12) <(a_s/pi) G^2>/Q^4 per unit charge^2 (finite, Q^{-4})',
      sp.simplify(lim - Gsq / (48 * sp.pi ** 2)) == 0)
# finiteness: no pole in eps
ser = sp.series(sp.simplify(Pi2Q * Qs ** 2 * Qs ** e), e, 0, 1).removeO()
check('G4  no 1/eps pole in the gluon-condensate coefficient at this order', not ser.has(1 / e) and sp.simplify(ser - Gsq / (48 * sp.pi ** 2)) == 0)

# ------------------------------------------------------------------------------------------- Q
# Pi^{mu nu} > e_q^2 (<qbar q>/4) { Tr[g^mu S(q) g^nu] + Tr[g^mu g^nu S(-q)]  (mass parts, S = i(pslash+m)/p^2)
#                    + (i m/4) Tr[g^mu dS(q)_l g^nu g^l] - (i m/4) Tr[g^mu g_l g^nu d_l(S(-p))|_{p=q}] }
# with i int e^{iqx} x^l S_F(x) = d^l S(q), i int e^{iqx} x^l S_F(-x) = d^l_p S(-p)|_{p=q}; 4D Dirac algebra.
import numpy as np
g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
def gk(s_):
    return np.block([[np.zeros((2, 2)), s_], [-s_, np.zeros((2, 2))]])
gam = [g0, gk(sx), gk(sy), gk(sz)]
eta = np.diag([1.0, -1, -1, -1])
rng = np.random.default_rng(7)
qv = rng.normal(size=4)
m_ = 0.37
def sl(v):
    return sum(eta[i, i] * v[i] * gam[i] for i in range(4))
def mdot(a_, b_):
    return a_[0] * b_[0] - a_[1:] @ b_[1:]
q2 = mdot(qv, qv)
S_mass = 1j * m_ / q2 * np.eye(4)                     # O(m) part of S(q) and S(-q)
def dS_massless(pv, sign):
    """d/dp_l [ i (sign pslash)/(p^2) ] at p (lower index l): returns list over l of matrices (O(m^0))"""
    p2 = mdot(pv, pv)
    out = []
    for l in range(4):
        # d/dp^l (p_s gamma^s) = gamma_l (lower) ; d/dp^l p^2 = 2 p_l
        gl = eta[l, l] * gam[l]
        pl = eta[l, l] * pv[l]
        out.append(sign * 1j * (gl / p2 - 2 * pl * sl(pv) / p2 ** 2))
    return out
dSq = dS_massless(qv, +1)        # d/dp_l of S(p) at p=q
dSmq = dS_massless(qv, -1)       # d/dp_l of S(-p) = -i pslash/p^2 at p=q
qq = 1.0                          # <qbar q> set to 1
okQ = True
for mu in range(4):
    for nu in range(4):
        t1 = 1j * np.trace(gam[mu] @ S_mass @ gam[nu])        # i int e^{iqx} S_F(x) = i S(q)
        t3 = 1j * np.trace(gam[mu] @ gam[nu] @ S_mass)        # i int e^{iqx} S_F(-x) = i S(-q)
        # index l of x^l contracted with gamma_l -> sum_l gamma^l (upper) * dS_l (lower derivative index)
        t2 = (1j * m_ / 4) * sum(np.trace(gam[mu] @ dSq[l] @ gam[nu] @ gam[l]) for l in range(4))
        t4 = -(1j * m_ / 4) * sum(np.trace(gam[mu] @ gam[l] @ gam[nu] @ dSmq[l]) for l in range(4))
        lhs = (qq / 4) * (t1 + t3 + t2 + t4)
        qmu = qv[mu]; qnu = qv[nu]
        # upper indices: q^mu q^nu - q^2 g^{mu nu}
        rhs = 2 * m_ * qq * (qmu * qnu - q2 * eta[mu, nu]) / q2 ** 2
        okQ &= abs(lhs - rhs) < 1e-12
check('Q1  quark condensate: Pi^{mu nu} -> e_q^2 2 m <qbar q> (q^mu q^nu - q^2 g^{mu nu})/q^4  (transverse; 4D Dirac matrices)', okQ)
# check of the condensate expansion: <qbar^b q^a(x)> = <qbar q>/(4N)[delta - (i m/4) xslash]: trace with gamma_l gives
# <qbar gamma^l d_l q> = -i m <qbar q> (free EOM i dslash q = m q): sum_l Tr[ (-(i m/4) gamma^l) gamma_l ] /4 /N per colour ...
Nc = 3
lhsEOM = sum(np.trace((-1j * m_ / 4) * gam[l] @ (eta[l, l] * gam[l])) for l in range(4)) * qq / (4 * Nc) * Nc
check('Q2  condensate expansion consistent with the EOM: <qbar dslash q> = -i m <qbar q>', abs(lhsEOM - (-1j * m_ * qq)) < 1e-12)

# ------------------------------------------------------------------------------------------- M
# massive one-loop: Pi(q^2) = -(N_c e_q^2/(2 pi^2)) int_0^1 dx x(1-x) ln[(m^2 - x(1-x) q^2)/mu^2] + const ; large Q^2 = -q^2
x, Qq, mm, mu_ = sp.symbols('x Q m mu', positive=True)
integrand = x * (1 - x) * sp.log((mm ** 2 + x * (1 - x) * Qq ** 2) / mu_ ** 2)
ser_m = sp.series(integrand, mm, 0, 3).removeO()
m2coef = sp.simplify(sp.integrate(sp.expand(ser_m).coeff(mm, 2), (x, 0, 1)))
check('M1  m^2 term: Pi -> -(N_c e_q^2/(2 pi^2)) m^2/Q^2 = (N_c e_q^2/(12 pi^2)) (-6 m^2/Q^2)', sp.simplify(m2coef - 1 / Qq ** 2) == 0)
# the massless limit of the same representation reproduces -(N_c e_q^2/(12 pi^2)) ln(Q^2) (normalisation)
lncoef = sp.simplify(sp.integrate(x * (1 - x), (x, 0, 1)) * 6)
check('M2  normalisation: -(1/(2pi^2)) int x(1-x) ln Q^2 = -(1/(12 pi^2)) ln Q^2', lncoef == 1)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
