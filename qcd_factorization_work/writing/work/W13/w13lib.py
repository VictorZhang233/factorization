"""w13lib.py -- small helpers for the W13 (Ch11) scripts.

(1) D-dimensional Dirac traces (CDR: {g^mu,g^nu}=2g^{mu nu}, g^mu_mu = D, Tr 1 = 4), adapted from
    research/c_dis/dirac_d.py (same algorithm: contracted index pairs removed by the exact D-dim recursion
    gamma^a X e gamma_a = 2 e X - (gamma^a X gamma_a) e,  gamma^a gamma_a = D; traces of slashed vectors by the
    standard recursion).  No gamma_5.
(2) Distributions on [0,1]: a distribution is a dict with keys 'delta', 'D0', 'D1', 'D2' (coefficients of
    delta(1-z) and of the plus distributions D_k = [ln^k(1-z)/(1-z)]_+) and 'reg' (a regular function of z).
    Pairing with a test function and Mellin moments are evaluated numerically (mpmath).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
from functools import lru_cache

D = sp.Symbol('D')
_DOT = {}


def set_dots(table):
    _DOT.clear()
    for (a, b), v in table.items():
        _DOT[tuple(sorted((a, b)))] = sp.sympify(v)
    trace_v.cache_clear()


def dot(a, b):
    key = tuple(sorted((a, b)))
    if key in _DOT:
        return _DOT[key]
    return sp.Symbol(key[0] + '_' + key[1])


@lru_cache(maxsize=None)
def sandwich(X):
    if len(X) == 0:
        return ((D, ()),)
    e, Xp = X[-1], X[:-1]
    out = [(sp.Integer(2), (e,) + Xp)]
    for c, s in sandwich(Xp):
        out.append((-c, s + (e,)))
    return tuple(out)


def _first_pair(s):
    seen = {}
    for pos, el in enumerate(s):
        if el[0] == 'i':
            if el[1] in seen:
                return seen[el[1]], pos
            seen[el[1]] = pos
    return None


@lru_cache(maxsize=None)
def contract_all(s):
    pr = _first_pair(s)
    if pr is None:
        return ((sp.Integer(1), s),)
    i, j = pr
    acc = {}
    for c, mid in sandwich(s[i + 1:j]):
        for c2, s2 in contract_all(s[:i] + mid + s[j + 1:]):
            acc[s2] = acc.get(s2, 0) + c * c2
    return tuple((sp.expand(c), k) for k, c in acc.items() if c != 0)


@lru_cache(maxsize=None)
def trace_v(names):
    n = len(names)
    if n == 0:
        return sp.Integer(4)
    if n % 2:
        return sp.Integer(0)
    a = names[0]
    res = 0
    for k in range(1, n):
        res += (-1) ** (k - 1) * dot(a, names[k]) * trace_v(names[1:k] + names[k + 1:])
    return sp.expand(res)


def tr(slots):
    """slots: list of ('i', name) [gamma^name; a name occurring twice is contracted with g (D-dim)]
    or dict {vector: coeff} [slashed linear combination]."""
    terms = [(sp.Integer(1), ())]
    for s in slots:
        if isinstance(s, tuple) and s[0] == 'i':
            terms = [(c, t + (s,)) for c, t in terms]
        else:
            terms = [(c * sp.sympify(cv), t + (('v', v),)) for c, t in terms for v, cv in s.items() if cv != 0]
    total = 0
    for c, t in terms:
        for c2, t2 in contract_all(t):
            total += c * c2 * trace_v(tuple(e[1] for e in t2))
    return sp.expand(total)


def I(name):
    return ('i', name)


def V(**kw):
    return dict(kw)


# ------------------------------------------------------------------ distributions
def pair(dist, h, eps_num=0):
    """<dist, h> for a test function h (python callable on mpf)."""
    tot = mp.mpf(0)
    h1 = h(mp.mpf(1))
    if dist.get('delta', 0):
        tot += mp.mpf(dist['delta']) * h1
    for k, key in enumerate(['D0', 'D1', 'D2']):
        cf = dist.get(key, 0)
        if cf:
            f = lambda zz, k=k: mp.log(1 - zz) ** k / (1 - zz) * (h(zz) - h1)
            tot += mp.mpf(cf) * mp.quad(f, [0, 0.5, 1])
    reg = dist.get('reg', None)
    if reg is not None:
        tot += mp.quad(lambda zz: reg(zz) * h(zz), [0, 0.5, 1])
    return tot


def moment(dist, N):
    return pair(dist, lambda zz: zz ** (N - 1))
