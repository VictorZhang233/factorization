# -*- coding: utf-8 -*-
"""
dtrace.py -- minimal D-dimensional Dirac-trace engine (written for the Drell-Yan study, c_dy).

Conventions (CDR): {gamma^mu, gamma^nu} = 2 g^{mu nu}, g^mu_mu = D, Tr 1 = 4, no gamma_5.

A gamma string is a tuple of atoms:
    ('v', name)  : slashed vector  (name refers to a momentum; dot products supplied by the user)
    ('i', name)  : gamma^mu with Lorentz index 'name'; an index appearing twice in a string is contracted.
A "sum of strings" is a dict {tuple_of_atoms: sympy coefficient}.

Algorithm:
  1. every contracted index pair is removed with the exact D-dim recursion
        gamma^mu S a gamma_mu = 2 a S - (gamma^mu S gamma_mu) a ,   gamma^mu gamma_mu = D,
     valid for any string S and any atom a (vector or index);
  2. the trace of a string of slashed vectors is computed with
        Tr(a1 a2 ... an) = sum_{k=2}^n (-1)^k (a1.ak) Tr(a2 ... ^ak ... an),  Tr(1)=4.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from functools import lru_cache

D = sp.Symbol('D')


def V(name):
    return ('v', name)


def I(name):
    return ('i', name)


def _add(d, key, c):
    if c == 0:
        return
    d[key] = d.get(key, 0) + c


def string_product(items):
    """items: list whose elements are atoms or dicts {vector_name: coeff} (linear combination of
    slashed vectors).  Returns the expanded sum of strings."""
    res = {(): sp.Integer(1)}
    for it in items:
        new = {}
        if isinstance(it, tuple):
            for k, c in res.items():
                _add(new, k + (it,), c)
        else:  # linear combination of vectors
            for k, c in res.items():
                for vn, cv in it.items():
                    _add(new, k + (('v', vn),), c * cv)
        res = new
    return res


@lru_cache(maxsize=None)
def _sandwich(S):
    """gamma^mu S gamma_mu for a tuple S of atoms (no free index named like the contracted one).
    Returns tuple of (string, coeff) pairs (hashable for caching)."""
    if len(S) == 0:
        return (((), D),)
    a = S[-1]
    Sp = S[:-1]
    out = {}
    # 2 a S'
    _add(out, (a,) + Sp, sp.Integer(2))
    # - (gamma^mu S' gamma_mu) a
    for st, c in _sandwich(Sp):
        _add(out, st + (a,), -c)
    return tuple(out.items())


def contract_all(strings):
    """Remove all repeated index pairs (cyclic trace context)."""
    work = dict(strings)
    done = {}
    while work:
        st, c = work.popitem()
        # find a repeated index
        pos = {}
        pair = None
        for j, at in enumerate(st):
            if at[0] == 'i':
                if at[1] in pos:
                    pair = (pos[at[1]], j)
                    break
                pos[at[1]] = j
        if pair is None:
            _add(done, st, c)
            continue
        i0, j0 = pair
        # cyclically rotate so that the first gamma of the pair is at position 0
        rot = st[i0:] + st[:i0]
        j1 = j0 - i0
        S = rot[1:j1]
        R = rot[j1 + 1:]
        for s2, c2 in _sandwich(S):
            _add(work, s2 + R, c * c2)
    return done


def make_trace(dot):
    """dot(a, b) -> sympy expression for the scalar product of vectors named a and b."""
    @lru_cache(maxsize=None)
    def trv(st):
        n = len(st)
        if n == 0:
            return sp.Integer(4)
        if n % 2 == 1:
            return sp.Integer(0)
        a1 = st[0]
        tot = sp.Integer(0)
        for k in range(1, n):
            sign = 1 if (k % 2 == 1) else -1   # (-1)^(k+1) with k counted from 0 -> (-1)^k for 1-based
            rest = st[1:k] + st[k + 1:]
            tot += sign * dot(a1[1], st[k][1]) * trv(rest)
        return tot

    def trace(strings):
        cs = contract_all(strings)
        tot = sp.Integer(0)
        for st, c in cs.items():
            if any(at[0] == 'i' for at in st):
                raise ValueError('free index left in trace: %s' % (st,))
            tot += c * trv(st)
        return sp.expand(tot)
    return trace


# ------------------------------------------------------------------ self tests
if __name__ == '__main__':
    a, b, c, d = sp.symbols('ab ac ad bc', real=True)
    sym = {}
    names = ['a', 'b', 'c', 'd', 'e', 'f']
    for i, x in enumerate(names):
        for y in names[i:]:
            sym[(x, y)] = sym[(y, x)] = sp.Symbol('%s%s' % (x, y))

    def dot(x, y):
        return sym[(x, y)]
    tr = make_trace(dot)
    # 1) Tr(a b c d) = 4[(ab)(cd) - (ac)(bd) + (ad)(bc)]
    t = tr(string_product([V('a'), V('b'), V('c'), V('d')]))
    ok1 = sp.simplify(t - 4 * (sym['a', 'b'] * sym['c', 'd'] - sym['a', 'c'] * sym['b', 'd'] + sym['a', 'd'] * sym['b', 'c'])) == 0
    # 2) gamma^mu gamma_mu = D -> Tr = 4D
    ok2 = sp.simplify(tr(string_product([I('m'), I('m')])) - 4 * D) == 0
    # 3) Tr(g^mu a g_mu b) = -(D-2) 4 (ab)
    ok3 = sp.simplify(tr(string_product([I('m'), V('a'), I('m'), V('b')])) + (D - 2) * 4 * sym['a', 'b']) == 0
    # 4) gamma^mu a b gamma_mu = 4 ab - (4-D) a b  -> Tr(... c d)
    lhs = tr(string_product([I('m'), V('a'), V('b'), I('m'), V('c'), V('d')]))
    rhs = 4 * sym['a', 'b'] * tr(string_product([V('c'), V('d')])) - (4 - D) * tr(string_product([V('a'), V('b'), V('c'), V('d')]))
    ok4 = sp.simplify(lhs - rhs) == 0
    # 5) gamma^mu a b c gamma_mu = -2 c b a + (4-D) a b c   (times d, traced)
    lhs = tr(string_product([I('m'), V('a'), V('b'), V('c'), I('m'), V('d')]))
    rhs = -2 * tr(string_product([V('c'), V('b'), V('a'), V('d')])) + (4 - D) * tr(string_product([V('a'), V('b'), V('c'), V('d')]))
    ok5 = sp.simplify(lhs - rhs) == 0
    # 6) Tr(g^m g^n g_m g_n) = -(D-2) 4 D
    ok6 = sp.simplify(tr(string_product([I('m'), I('n'), I('m'), I('n')])) + (D - 2) * 4 * D) == 0
    # 7) interleaved pairs, 6 gammas: compare with brute-force numerical 4D matrices at D=4
    import numpy as np
    g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
    def gk(s):
        m = np.zeros((4, 4), dtype=complex); m[:2, 2:] = s; m[2:, :2] = -s; return m
    G = [g0, gk(sx), gk(sy), gk(sz)]
    metric = np.diag([1., -1., -1., -1.])
    rng = np.random.default_rng(1)
    vecs = {n: rng.normal(size=4) for n in names}
    def sl(v):
        return sum(metric[m, m] * v[m] * G[m] for m in range(4))
    def mdot(x, y):
        return float(vecs[x] @ metric @ vecs[y])
    # string: g^m a g^n b g_m c g_n d
    num = 0
    for m in range(4):
        for n in range(4):
            num += metric[m, m] * metric[n, n] * np.trace(G[m] @ sl(vecs['a']) @ G[n] @ sl(vecs['b']) @ G[m] @ sl(vecs['c']) @ G[n] @ sl(vecs['d']))
    t7 = tr(string_product([I('m'), V('a'), I('n'), V('b'), I('m'), V('c'), I('n'), V('d')]))
    t7n = complex(t7.subs(D, 4).subs({sym[k]: mdot(*k) for k in sym}))
    ok7 = abs(t7n - num) < 1e-9 * max(1, abs(num))
    print('dtrace self-tests:', ok1, ok2, ok3, ok4, ok5, ok6, ok7, ' (numeric 4D check: %.6f vs %.6f)' % (t7n.real, num.real))
    assert all([ok1, ok2, ok3, ok4, ok5, ok6, ok7])
    print('ALL dtrace SELF-TESTS PASS')
