"""
dirac_d.py -- minimal D-dimensional Dirac algebra for one fermion line (one trace).

Conventions:  {gamma^mu, gamma^nu} = 2 g^{mu nu},  g^mu_mu = D,  Tr 1 = 4
(the standard choice of conventional dimensional regularisation, CDR).
No gamma_5 appears anywhere in this project.

A gamma string is a tuple of elements:
   ('v', name)  : slashed basis vector  name-slash
   ('i', name)  : gamma^{name};  an index name occurring TWICE in a string means
                  the contraction gamma^{a} ... gamma_{a}  (metric g_{ab}).
Contractions are removed with the exact D-dim recursion
   gamma^a X e gamma_a = 2 e X - (gamma^a X gamma_a) e      (e any single element)
   gamma^a gamma_a     = D
after which traces of slashed vectors are evaluated with the standard recursion
   Tr[a1 a2 ... an] = sum_{k>=2} (-1)^k (a1.ak) Tr[a2 .. (ak omitted) .. an].
Both identities only use the Clifford relation, hence hold for symbolic D.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from functools import lru_cache
from itertools import product

D = sp.Symbol('D')

# ---------------------------------------------------------------- dot products
_DOT = {}            # user-supplied table  frozenset({a,b}) or (a,a) -> sympy expr


def set_dots(table):
    """table: dict {(a,b): value}; symmetric completion is automatic."""
    _DOT.clear()
    for (a, b), v in table.items():
        _DOT[tuple(sorted((a, b)))] = sp.sympify(v)
    trace_v.cache_clear()


def dot(a, b):
    key = tuple(sorted((a, b)))
    if key in _DOT:
        return _DOT[key]
    return sp.Symbol(key[0] + '_' + key[1])          # generic symbol if not given


# ---------------------------------------------------------------- contractions
@lru_cache(maxsize=None)
def sandwich(X):
    """gamma^a X gamma_a as a tuple of (coeff, string); X is a tuple of elements."""
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
    """remove all contracted index pairs; returns tuple of (coeff, vector-only string)"""
    pr = _first_pair(s)
    if pr is None:
        return ((sp.Integer(1), s),)
    i, j = pr
    acc = {}
    for c, mid in sandwich(s[i + 1:j]):
        for c2, s2 in contract_all(s[:i] + mid + s[j + 1:]):
            acc[s2] = acc.get(s2, 0) + c * c2
    return tuple((sp.expand(c), k) for k, c in acc.items() if c != 0)


# ---------------------------------------------------------------- traces
@lru_cache(maxsize=None)
def trace_v(names):
    """Tr of slashed basis vectors (tuple of names), Tr 1 = 4."""
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
    """
    slots: list; each slot is either ('i', name)  (gamma^name) or a dict {basis_vector: coeff}
           (a slashed linear combination).  Returns the D-dim trace as a sympy expression.
    """
    terms = [(sp.Integer(1), ())]
    for s in slots:
        if isinstance(s, tuple) and s[0] == 'i':
            terms = [(c, t + (s,)) for c, t in terms]
        else:
            terms = [(c * sp.sympify(cv), t + (('v', v),)) for c, t in terms for v, cv in s.items()
                     if cv != 0]
    total = 0
    for c, t in terms:
        for c2, t2 in contract_all(t):
            total += c * c2 * trace_v(tuple(e[1] for e in t2))
    return sp.expand(total)


def I(name):
    return ('i', name)


def V(**kw):
    """slashed linear combination, e.g. V(p=1, q=1) = p-slash + q-slash"""
    return {k: v for k, v in kw.items()}
