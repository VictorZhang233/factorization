"""
lorentz_engine.py -- minimal D-dimensional Lorentz / Dirac algebra engine (no gamma_5).

Representation
--------------
* Vec : linear combination of named basis vectors  {name: sympy coefficient}.
* slot: ('v', Vec)     -> a vector (v^mu, or vslash inside a Dirac string)
        ('i', label)   -> a Lorentz index (gamma^mu inside a Dirac string)
* A tensor monomial is a list of PAIRS (slot, slot):
        (v, w)   -> v.w          (v, mu) -> v^mu        (mu, nu) -> g^{mu nu}
  Every index label must occur exactly twice in a fully contracted product.
* Dirac trace (D dimensions, Tr 1 = 4):
        Tr[s_1 ... s_2n] = 4 * sum_{perfect matchings M} sign(M) prod_{(i,j) in M} <s_i, s_j>
  i.e. the matching produces pairs which are then contracted together with any
  extra pairs.  Index chains are followed; a closed chain of indices gives D.

Kinematics enter through a table  {(name1, name2): sympy expr}  of basis-vector dot products.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from functools import lru_cache

D = sp.Symbol('D')


class Vec:
    __slots__ = ('c',)

    def __init__(self, comps=None):
        self.c = {}
        if comps:
            for k, v in comps.items():
                v = sp.sympify(v)
                if v != 0:
                    self.c[k] = v

    @classmethod
    def b(cls, name):
        return cls({name: sp.Integer(1)})

    def __add__(self, o):
        c = dict(self.c)
        for k, v in o.c.items():
            c[k] = c.get(k, 0) + v
        return Vec(c)

    def __neg__(self):
        return Vec({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, s):
        return Vec({k: v * s for k, v in self.c.items()})

    __rmul__ = __mul__

    def __repr__(self):
        return 'Vec(%s)' % self.c


def V(name):
    return ('v', Vec.b(name)) if isinstance(name, str) else ('v', name)


def I(label):
    return ('i', label)


class Kin:
    """Dot-product table for basis vectors (symmetric)."""

    def __init__(self, table):
        self.t = {}
        for (a, b), val in table.items():
            self.t[(a, b)] = sp.sympify(val)
            self.t[(b, a)] = sp.sympify(val)

    def dot(self, x, y):
        s = 0
        for ka, va in x.c.items():
            for kb, vb in y.c.items():
                s += va * vb * self.t[(ka, kb)]
        return s


def contract(pairs, kin):
    """Contract a list of pairs. All index labels must appear exactly twice."""
    occ = {}
    for pi, pr in enumerate(pairs):
        for si, s in enumerate(pr):
            if s[0] == 'i':
                occ.setdefault(s[1], []).append((pi, si))
    for lab, lst in occ.items():
        if len(lst) != 2:
            raise ValueError('index %r occurs %d times' % (lab, len(lst)))
    visited = [False] * len(pairs)
    res = sp.Integer(1)

    def nxt(cur_p, cur_s):
        # we are at pair cur_p, leaving through slot (1-cur_s) which is an index
        lab = pairs[cur_p][1 - cur_s][1]
        o1, o2 = occ[lab]
        here = (cur_p, 1 - cur_s)
        return o2 if o1 == here else o1

    for pi in range(len(pairs)):
        if visited[pi]:
            continue
        for si in (0, 1):
            s = pairs[pi][si]
            if s[0] == 'v' and not visited[pi]:
                start = s[1]
                cp, cs = pi, si
                while True:
                    visited[cp] = True
                    other = pairs[cp][1 - cs]
                    if other[0] == 'v':
                        res *= kin.dot(start, other[1])
                        break
                    cp, cs = nxt(cp, cs)
                break
    for pi in range(len(pairs)):
        if not visited[pi]:
            cp, cs = pi, 0
            while not visited[cp]:
                visited[cp] = True
                cp, cs = nxt(cp, cs)
            res *= D
    return res


@lru_cache(None)
def matchings(n):
    """Perfect matchings of positions 0..n-1 with trace signs (recursive formula)."""
    if n == 0:
        return ((1, ()),)
    if n % 2:
        return ()
    out = []
    for k in range(1, n):
        sign = (-1) ** (k - 1)
        rest = [i for i in range(1, n) if i != k]
        for s2, m2 in matchings(n - 2):
            out.append((sign * s2, ((0, k),) + tuple((rest[a], rest[b]) for a, b in m2)))
    return tuple(out)


def trace(slots, extra, kin):
    """4 * sum over matchings; extra = list of pairs multiplying the trace."""
    n = len(slots)
    if n % 2:
        return sp.Integer(0)
    tot = 0
    for sign, M in matchings(n):
        prs = [(slots[i], slots[j]) for i, j in M] + list(extra)
        tot += sign * contract(prs, kin)
    return 4 * tot


class Term:
    """coef * [Dirac string slots] * prod(extra pairs)."""
    __slots__ = ('coef', 'g', 'e')

    def __init__(self, coef, g=(), e=()):
        self.coef = sp.sympify(coef)
        self.g = tuple(g)
        self.e = tuple(e)

    def __mul__(self, o):
        return Term(self.coef * o.coef, self.g + o.g, self.e + o.e)


def mul(*sums):
    """Product of sums of Terms (lists)."""
    out = [Term(1)]
    for s in sums:
        out = [a * b for a in out for b in s]
    return out


def tr_sum(terms, kin):
    return sp.Add(*[t.coef * trace(t.g, t.e, kin) for t in terms])


def contract_sum(terms, kin):
    out = 0
    for t in terms:
        assert len(t.g) == 0
        out += t.coef * contract(list(t.e), kin)
    return out


# ---------------------------------------------------------------- self tests
if __name__ == '__main__':
    a, b, c, d = sp.symbols('a b c d')
    kin = Kin({('a', 'a'): sp.Symbol('aa'), ('a', 'b'): sp.Symbol('ab'), ('a', 'c'): sp.Symbol('ac'),
               ('a', 'd'): sp.Symbol('ad'), ('b', 'b'): sp.Symbol('bb'), ('b', 'c'): sp.Symbol('bc'),
               ('b', 'd'): sp.Symbol('bd'), ('c', 'c'): sp.Symbol('cc'), ('c', 'd'): sp.Symbol('cd'),
               ('d', 'd'): sp.Symbol('dd')})
    ab, ac, ad, bc, bd, cd = sp.symbols('ab ac ad bc bd cd')
    checks = []
    checks.append(('Tr[g^m g_m] = 4D', trace([I('m'), I('m')], [], kin) - 4 * D))
    checks.append(('Tr[a b] = 4 a.b', trace([V('a'), V('b')], [], kin) - 4 * ab))
    checks.append(('Tr[abcd]', sp.expand(trace([V('a'), V('b'), V('c'), V('d')], [], kin)
                                          - 4 * (ab * cd - ac * bd + ad * bc))))
    checks.append(('Tr[g^m a g_m b] = 4(2-D)a.b',
                   sp.expand(trace([I('m'), V('a'), I('m'), V('b')], [], kin) - 4 * (2 - D) * ab)))
    # g^m a b g_m = 4 a.b - (4-D) a b  -> trace with c d: Tr[g^m a b g_m c d]
    lhs = trace([I('m'), V('a'), V('b'), I('m'), V('c'), V('d')], [], kin)
    rhs = 4 * ab * trace([V('c'), V('d')], [], kin) - (4 - D) * trace([V('a'), V('b'), V('c'), V('d')], [], kin)
    checks.append(('g^m a b g_m identity', sp.expand(lhs - rhs)))
    # g^m a b c g_m = -2 c b a + (4-D) a b c  -> times d
    lhs = trace([I('m'), V('a'), V('b'), V('c'), I('m'), V('d')], [], kin)
    rhs = -2 * trace([V('c'), V('b'), V('a'), V('d')], [], kin) + (4 - D) * trace([V('a'), V('b'), V('c'), V('d')], [], kin)
    checks.append(('g^m a b c g_m identity', sp.expand(lhs - rhs)))
    # external pairs: a^m b_m = a.b ; g^{mn} g_{nm} = D
    checks.append(('a^m b_m', contract([(V('a'), I('m')), (V('b'), I('m'))], kin) - ab))
    checks.append(('g^mn g_nm', contract([(I('m'), I('n')), (I('n'), I('m'))], kin) - D))
    checks.append(('g^mn a_n b_m', contract([(I('m'), I('n')), (V('a'), I('n')), (V('b'), I('m'))], kin) - ab))
    # linear combination vectors
    v = Vec.b('a') * 2 - Vec.b('b')
    checks.append(('(2a-b).c', contract([(('v', v), V('c'))], kin) - (2 * ac - bc)))
    ok = True
    for name, val in checks:
        st = 'PASS' if sp.simplify(val) == 0 else 'FAIL'
        ok &= (st == 'PASS')
        print('%-35s %s' % (name, st))
    print('ALL ENGINE TESTS PASS' if ok else 'ENGINE TEST FAILURE')
