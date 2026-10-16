"""
diracD.py -- minimal D-dimensional Dirac algebra (anticommuting gammas, Tr 1 = 4, g^mu_mu = D).

A "string" is a tuple of slots; a slot is ('v', name) for a slashed vector, or ('i', name) for
a Lorentz-index gamma^name.  A linear combination (LC) is a dict {string: sympy coefficient}.
Index pairs that occur twice in one string are contracted with the D-dimensional identity
    gamma^mu S a gamma_mu = 2 a S - (gamma^mu S gamma_mu) a      (a = any slot),
    gamma^mu gamma_mu = D,
which only uses {gamma^mu, gamma^nu} = 2 g^{mu nu}; it therefore holds in CDR for any D.
Traces of vector-only strings use the standard recursion.  Scalar products are returned as
sympy symbols dot(a,b) = Symbol('a.b') with names sorted.
No gamma_5 anywhere (not needed for the vector current).

Run  python3 -I diracD.py  to execute the self-tests (including a numerical comparison with
explicit 4x4 Dirac matrices at D = 4).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
from functools import lru_cache
import sympy as sp

D = sp.Symbol('D')


def dot(a, b):
    a, b = sorted((a, b))
    return sp.Symbol(f'{a}.{b}')


def V(name):
    return ('v', name)


def I(name):
    return ('i', name)


def lc_add(x, y, c=1):
    out = dict(x)
    for k, v in y.items():
        out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v != 0}


def lc_mul(*lcs):
    """product (concatenation) of linear combinations of strings"""
    out = {(): sp.Integer(1)}
    for l in lcs:
        new = {}
        for s1, c1 in out.items():
            for s2, c2 in l.items():
                s = s1 + s2
                new[s] = new.get(s, 0) + c1 * c2
        out = new
    return out


def slash(**coeffs):
    """slash(p1=1, k=1) -> LC for (p1-slash + k-slash)"""
    return {(V(n),): sp.sympify(c) for n, c in coeffs.items()}


def gam(name):
    return {(I(name),): sp.Integer(1)}


def scal(c):
    return {(): sp.sympify(c)}


@lru_cache(maxsize=None)
def _contract_inner(S):
    """gamma^mu S gamma_mu as an LC (dict items tuple), S a tuple of slots"""
    if len(S) == 0:
        return ((tuple(), D),)
    Sp, a = S[:-1], S[-1]
    res = {}
    # 2 a S'
    key = (a,) + Sp
    res[key] = res.get(key, 0) + 2
    # - (gamma^mu S' gamma_mu) a
    for s, c in _contract_inner(Sp):
        key = s + (a,)
        res[key] = res.get(key, 0) - c
    return tuple((k, sp.expand(v)) for k, v in res.items() if v != 0)


def _find_pair(s):
    seen = {}
    for pos, slot in enumerate(s):
        if slot[0] == 'i':
            if slot[1] in seen:
                return seen[slot[1]], pos
            seen[slot[1]] = pos
    return None


def contract_all(lc):
    work = dict(lc)
    done = {}
    while work:
        s, c = work.popitem()
        pr = _find_pair(s)
        if pr is None:
            done[s] = done.get(s, 0) + c
            continue
        i, j = pr
        pre, inner, post = s[:i], s[i + 1:j], s[j + 1:]
        for t, ct in _contract_inner(inner):
            key = pre + t + post
            work[key] = work.get(key, 0) + c * ct
    return {k: v for k, v in done.items() if v != 0}


@lru_cache(maxsize=None)
def _trace_vec(names):
    n = len(names)
    if n == 0:
        return sp.Integer(4)
    if n % 2 == 1:
        return sp.Integer(0)
    a = names[0]
    res = 0
    for k in range(1, n):
        sign = 1 if k % 2 == 1 else -1
        rest = names[1:k] + names[k + 1:]
        res += sign * dot(a, names[k]) * _trace_vec(rest)
    return sp.expand(res)


def trace(lc):
    """trace of an LC; all Lorentz indices must be contracted inside each string"""
    lc = contract_all(lc)
    res = 0
    for s, c in lc.items():
        if any(sl[0] == 'i' for sl in s):
            raise ValueError('free index left in trace: %r' % (s,))
        res += c * _trace_vec(tuple(sl[1] for sl in s))
    return sp.expand(res)


# ----------------------------------------------------------------------------------------------
# self-tests
# ----------------------------------------------------------------------------------------------
def _selftest():
    import numpy as np
    a, b, c, d, e, f = 'a', 'b', 'c', 'd', 'e', 'f'
    # basic traces
    assert sp.simplify(trace(lc_mul(slash(a=1), slash(b=1))) - 4 * dot(a, b)) == 0
    t4 = trace(lc_mul(slash(a=1), slash(b=1), slash(c=1), slash(d=1)))
    assert sp.expand(t4 - 4 * (dot(a, b) * dot(c, d) - dot(a, c) * dot(b, d) + dot(a, d) * dot(b, c))) == 0
    # contraction identities (checked inside a trace with extra vectors)
    # gamma^mu gamma_mu = D
    assert sp.expand(trace(lc_mul(gam('m'), gam('m'))) - 4 * D) == 0
    # gamma^mu a gamma_mu = -(D-2) a
    lhs = trace(lc_mul(gam('m'), slash(a=1), gam('m'), slash(b=1)))
    assert sp.expand(lhs + (D - 2) * 4 * dot(a, b)) == 0
    # gamma^mu a b gamma_mu = 4 a.b - (4-D) a b
    lhs = trace(lc_mul(gam('m'), slash(a=1), slash(b=1), gam('m'), slash(c=1), slash(d=1)))
    rhs = 4 * dot(a, b) * 4 * dot(c, d) - (4 - D) * t4
    assert sp.expand(lhs - rhs) == 0
    # gamma^mu a b c gamma_mu = -2 c b a + (4-D) a b c
    lhs = trace(lc_mul(gam('m'), slash(a=1), slash(b=1), slash(c=1), gam('m'), slash(d=1)))
    rhs = -2 * trace(lc_mul(slash(c=1), slash(b=1), slash(a=1), slash(d=1))) + (4 - D) * t4
    assert sp.expand(lhs - rhs) == 0
    # numerical comparison at D=4 with explicit Dirac matrices (interleaved contractions)
    g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    Z = np.zeros((2, 2), dtype=complex)

    def gi(s):
        return np.block([[Z, s], [-s, Z]])
    G = [g0, gi(sx), gi(sy), gi(sz)]
    metric = np.diag([1., -1., -1., -1.])
    rng = np.random.default_rng(1)
    vecs = {n: rng.normal(size=4) for n in 'abcdef'}

    def sl(v):
        return sum(metric[m, m] * v[m] * G[m] for m in range(4))
    # Tr[ g^m a g^n b g_m c g_n d e f ]  (two interleaved contracted pairs, 10 slots)
    num = 0
    for m in range(4):
        for n in range(4):
            M = G[m] @ sl(vecs['a']) @ G[n] @ sl(vecs['b']) @ (metric[m, m] * G[m]) @ sl(vecs['c']) \
                @ (metric[n, n] * G[n]) @ sl(vecs['d']) @ sl(vecs['e']) @ sl(vecs['f'])
            num += np.trace(M)
    sym = trace(lc_mul(gam('m'), slash(a=1), gam('n'), slash(b=1), gam('m'), slash(c=1), gam('n'),
                       slash(d=1), slash(e=1), slash(f=1)))
    subs = {D: 4}
    for x, y in itertools.combinations_with_replacement('abcdef', 2):
        subs[dot(x, y)] = float(vecs[x] @ metric @ vecs[y])
    val = complex(sym.subs(subs))
    assert abs(val - num) < 1e-9 * max(1, abs(num)), (val, num)
    print('diracD self-tests passed (incl. numerical 4x4 check: %.6f vs %.6f)' % (val.real, num.real))


if __name__ == '__main__':
    _selftest()
