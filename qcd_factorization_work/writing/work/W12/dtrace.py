"""D-dimensional Dirac traces by the pairing (perfect-matching) expansion.

Independent re-implementation for writer W12 (Ch10).  Only the Clifford relation
{gamma^a, gamma^b} = 2 g^{ab}, Tr 1 = 4 and g^mu_mu = D are used (CDR).

A gamma string is a tuple of slots; a slot is ('v', name) for a slashed vector
or ('i', name) for a Lorentz index.  Every index name must occur exactly twice
in the string (contracted); vectors are contracted with each other through the
user-supplied dot-product function.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from functools import lru_cache

D = sp.Symbol('D')


def _matchings(n):
    """All perfect matchings of range(n) with their signs (as list of (sign, pairs))."""
    @lru_cache(maxsize=None)
    def rec(items):
        if not items:
            return [(1, ())]
        a = items[0]
        out = []
        rest = items[1:]
        for k, b in enumerate(rest):
            sign = -1 if (k % 2) else 1   # (-1)^k for partner at relative position k (0-based)
            remaining = rest[:k] + rest[k + 1:]
            for s, pr in rec(remaining):
                out.append((sign * s, ((a, b),) + pr))
        return out
    return rec(tuple(range(n)))


def trace(slots, dot):
    """Tr[ gamma^{s_1} ... gamma^{s_n} ] with D-dimensional contractions.

    slots: list of ('v', name) or ('i', name); dot(a, b) returns the scalar product of
    vectors a and b (sympy expression).
    """
    n = len(slots)
    if n == 0:
        return sp.Integer(4)
    if n % 2:
        return sp.Integer(0)
    # positions of each index
    idxpos = {}
    for pos, (kind, name) in enumerate(slots):
        if kind == 'i':
            idxpos.setdefault(name, []).append(pos)
    for name, ps in idxpos.items():
        if len(ps) != 2:
            raise ValueError('index %s must occur exactly twice' % name)
    partner_idx = {}
    for name, (p1, p2) in idxpos.items():
        partner_idx[p1] = p2
        partner_idx[p2] = p1
    total = sp.Integer(0)
    for sign, pairs in _matchings(n):
        match = {}
        for a, b in pairs:
            match[a] = b
            match[b] = a
        # evaluate product of pairings: follow alternating chains
        seen = set()
        val = sp.Integer(1)
        # chains starting at vector slots
        for start in range(n):
            if start in seen or slots[start][0] != 'v':
                continue
            cur = start
            seen.add(cur)
            while True:
                nxt = match[cur]          # pairing edge
                seen.add(nxt)
                if slots[nxt][0] == 'v':
                    val *= dot(slots[start][1], slots[nxt][1])
                    break
                # nxt is an index slot: go to the other occurrence of the index
                other = partner_idx[nxt]
                seen.add(other)
                cur = other
                # cur is an index slot; continue with its pairing edge
        # remaining: closed loops of index slots only
        for start in range(n):
            if start in seen:
                continue
            cur = start
            while True:
                seen.add(cur)
                nxt = match[cur]
                seen.add(nxt)
                other = partner_idx[nxt]
                if other == start:
                    break
                cur = other
            val *= D
        total += sign * val
    return sp.expand(4 * total)


def V(name):
    return ('v', name)


def I(name):
    return ('i', name)


if __name__ == '__main__':
    # self-tests
    a, b, c, d = sp.symbols('a b c d')
    dots = {}
    def dot(x, y):
        key = tuple(sorted((x, y)))
        return sp.Symbol('%s.%s' % key)
    # Tr[a b] = 4 a.b
    print('Tr[ab] =', trace([V('a'), V('b')], dot))
    # Tr[g^mu g_mu] = 4 D
    print('Tr[g^mu g_mu] =', trace([I('m'), I('m')], dot))
    # gamma^mu a gamma_mu = -(D-2) a  ->  Tr[gamma^mu a gamma_mu b] = -(D-2) 4 a.b
    t = trace([I('m'), V('a'), I('m'), V('b')], dot)
    print('Tr[g^m a g_m b] =', sp.factor(t))
    # gamma^mu a b gamma_mu = 4 a.b - (4-D) a b -> Tr[... c] ... check against explicit
    t = trace([I('m'), V('a'), V('b'), I('m'), V('c'), V('d')], dot)
    expect = 4*dot('a', 'b')*4*dot('c', 'd') - (4 - D)*trace([V('a'), V('b'), V('c'), V('d')], dot)
    print('check gamma^m a b gamma_m:', sp.simplify(t - expect))
    t = trace([I('m'), V('a'), V('b'), V('c'), I('m'), V('d')], dot)
    expect = -2*trace([V('c'), V('b'), V('a'), V('d')], dot) + (4 - D)*trace([V('a'), V('b'), V('c'), V('d')], dot)
    print('check gamma^m a b c gamma_m:', sp.simplify(t - expect))
