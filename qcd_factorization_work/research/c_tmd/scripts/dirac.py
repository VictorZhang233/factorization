# Minimal D-dimensional Dirac-trace utility (sympy).
# Vectors are named symbols; dot products are supplied by a user function.
# Tr(1) = 4 (standard convention, also in D dims).  Contracted Lorentz index pairs
# are represented by placeholder vectors ('e1','f1'), ('e2','f2'), ... and contracted
# after the trace:  e.f -> D,  (e.a)(f.b) -> a.b ,  (e.a)(e.b) never occurs.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from functools import lru_cache

D = sp.Symbol('D')

class Dots:
    """holds a dict of known dot products between named vectors"""
    def __init__(self, table):
        self.t = {}
        for (a, b), v in table.items():
            self.t[(a, b)] = v
            self.t[(b, a)] = v
    def __call__(self, a, b):
        if (a, b) in self.t:
            return self.t[(a, b)]
        # unknown (placeholder) -> symbol
        x, y = sorted([a, b])
        return sp.Symbol('dot_%s_%s' % (x, y))

def trace(vecs, dot):
    """Tr(a1-slash ... an-slash), recursive expansion"""
    vecs = tuple(vecs)
    @lru_cache(maxsize=None)
    def tr(vs):
        n = len(vs)
        if n == 0:
            return sp.Integer(4)
        if n % 2 == 1:
            return sp.Integer(0)
        a = vs[0]
        res = 0
        for k in range(1, n):
            sign = (-1) ** (k - 1)
            rest = vs[1:k] + vs[k + 1:]
            res += sign * dot(a, vs[k]) * tr(rest)
        return sp.expand(res)
    return tr(vecs)

def contract(expr, e, f, known_vectors):
    """contract the placeholder pair (e,f) = g_{mu nu} contraction.
    expr is a polynomial in symbols dot_x_y.  Terms: dot(e,f) -> D;
    dot(e,a)*dot(f,b) -> dot(a,b)."""
    expr = sp.expand(expr)
    def s(a, b):
        x, y = sorted([a, b])
        return sp.Symbol('dot_%s_%s' % (x, y))
    out = 0
    ef = s(e, f)
    eas = {a: s(e, a) for a in known_vectors}
    fbs = {b: s(f, b) for b in known_vectors}
    for term in sp.Add.make_args(expr):
        c = term
        if term.has(ef):
            out += term.subs(ef, D)
            continue
        ea = [a for a in known_vectors if term.has(eas[a])]
        fb = [b for b in known_vectors if term.has(fbs[b])]
        if not ea and not fb:
            out += term
            continue
        assert len(ea) == 1 and len(fb) == 1, term
        a, b = ea[0], fb[0]
        c = term.subs({eas[a]: 1, fbs[b]: 1})
        out += c * s(a, b)
    return sp.expand(out)
