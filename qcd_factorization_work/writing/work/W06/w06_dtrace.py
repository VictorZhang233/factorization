r"""
w06_dtrace.py -- writer W06's own D-dimensional Dirac-trace engine (written from scratch for Ch6/App C;
independent of research/c_ee/diracD.py).

Conventions: CDR, {gamma^mu, gamma^nu} = 2 g^{mu nu}, g^mu_mu = D, Tr 1 = 4 (no gamma_5 anywhere).
A gamma string is a list of slots; a slot is ('p', 'k1') (slashed momentum) or ('i', 'mu') (gamma^mu).
trace(slots) returns a sympy expression in the symbols  dot_a_b (= a.b, a<=b alphabetically),
D, and open-index objects; contract() removes repeated (contracted) Lorentz indices.

Recursion: Tr(a1 a2 ... an) = sum_{k=2}^n (-1)^k <a1 ak> Tr(a2 .. ^ak .. an),  <p q> = p.q, <p mu> = p^mu,
<mu nu> = g^{mu nu}.  Run this file to execute the self-tests (4D numerical comparison with explicit
Dirac matrices, and D-dimensional contraction identities).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools, random
from functools import lru_cache
import sympy as sp

D = sp.Symbol('D')


def dot(a, b):
    a, b = sorted([a, b])
    return sp.Symbol('dot_%s_%s' % (a, b))


class Idx:
    """bookkeeping of open-index objects: we encode p^mu as Symbol('V_p_mu'), g^{mu nu} as Symbol('g_mu_nu')"""
    pass


def V(p, mu):
    return sp.Symbol('V_%s_%s' % (p, mu))


def g(mu, nu):
    mu, nu = sorted([mu, nu])
    return sp.Symbol('g_%s_%s' % (mu, nu))


def pair(a, b):
    ta, na = a
    tb, nb = b
    if ta == 'p' and tb == 'p':
        return dot(na, nb)
    if ta == 'p' and tb == 'i':
        return V(na, nb)
    if ta == 'i' and tb == 'p':
        return V(nb, na)
    return g(na, nb)


@lru_cache(maxsize=None)
def _trace(slots):
    n = len(slots)
    if n == 0:
        return sp.Integer(4)
    if n % 2 == 1:
        return sp.Integer(0)
    a1 = slots[0]
    res = 0
    for k in range(1, n):
        rest = slots[1:k] + slots[k + 1:]
        sign = 1 if (k % 2 == 1) else -1        # k is 0-based position; (-1)^{(k+1)} with 1-based index k+1
        res += sign * pair(a1, slots[k]) * _trace(rest)
    return sp.expand(res)


def trace(slots):
    return _trace(tuple(tuple(s) for s in slots))


# ------------------------------------------------------------------ contraction of repeated indices
def _parse(sym):
    s = sym.name
    if s.startswith('V_'):
        _, p, mu = s.split('_', 2)
        return ('V', p, mu)
    if s.startswith('g_'):
        _, mu, nu = s.split('_', 2)
        return ('g', mu, nu)
    return None


def _contract_monomial(coeff, factors):
    """factors: list of (kind, a, b) with repetitions allowed (powers expanded). Returns sympy expr."""
    changed = True
    factors = list(factors)
    while changed:
        changed = False
        # count index occurrences
        occ = {}
        for i, f in enumerate(factors):
            kind, a, b = f
            idxs = [b] if kind == 'V' else [a, b]
            for ix in idxs:
                occ.setdefault(ix, []).append(i)
        for ix, where in occ.items():
            if len(where) == 1:
                continue
            if len(where) > 2:
                raise ValueError('index %s appears more than twice' % ix)
            i, j = where
            if i == j:      # g_mu_mu
                kind, a, b = factors[i]
                assert kind == 'g' and a == b == ix
                factors.pop(i)
                coeff = coeff * D
                changed = True
                break
            fi, fj = factors[i], factors[j]
            for _ in range(2):
                if fi[0] == 'V' and fj[0] == 'V':
                    new = ('dot', fi[1], fj[1])
                elif fi[0] == 'g' and fj[0] == 'V':
                    other = fi[1] if fi[2] == ix else fi[2]
                    new = ('V', fj[1], other)
                elif fi[0] == 'g' and fj[0] == 'g':
                    o1 = fi[1] if fi[2] == ix else fi[2]
                    o2 = fj[1] if fj[2] == ix else fj[2]
                    a, b = sorted([o1, o2])
                    new = ('g', a, b)
                else:
                    fi, fj = fj, fi
                    continue
                break
            for k in sorted([i, j], reverse=True):
                factors.pop(k)
            if new[0] == 'dot':
                coeff = coeff * dot(new[1], new[2])
            else:
                factors.append(new)
            changed = True
            break
    expr = coeff
    for f in factors:
        kind, a, b = f
        expr = expr * (V(a, b) if kind == 'V' else g(a, b))
    return expr


def contract(expr):
    expr = sp.expand(expr)
    terms = expr.args if isinstance(expr, sp.Add) else [expr]
    out = 0
    for t in terms:
        coeff = 1
        factors = []
        for f in (t.args if isinstance(t, sp.Mul) else [t]):
            base, ex = f.as_base_exp()
            if isinstance(base, sp.Symbol) and _parse(base) is not None and ex.is_Integer and ex > 0:
                factors += [_parse(base)] * int(ex)
            else:
                coeff = coeff * f
        out += _contract_monomial(coeff, factors)
    return sp.expand(out)


# ------------------------------------------------------------------ self tests
def _self_test():
    import numpy as np
    ok = True
    # explicit 4D Dirac matrices (Dirac representation), metric (+,-,-,-)
    I2 = np.eye(2); Z2 = np.zeros((2, 2))
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
    G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
    metric = np.diag([1, -1, -1, -1]).astype(float)
    rnd = np.random.default_rng(7)
    vecs = {n: rnd.normal(size=4) for n in ('a', 'b', 'c', 'e', 'f', 'h')}

    def slash(v):
        vl = metric @ v
        return sum(G[m] * vl[m] for m in range(4))
    # (1) traces of 4 and 6 slashed vectors
    for names in (('a', 'b', 'c', 'e'), ('a', 'b', 'c', 'e', 'f', 'h'), ('a', 'a', 'b', 'c')):
        num = np.trace(np.linalg.multi_dot([slash(vecs[n]) for n in names]))
        sym = trace([('p', n) for n in names])
        subs = {dot(x, y): float(vecs[x] @ metric @ vecs[y]) for x in vecs for y in vecs}
        val = complex(sym.subs(subs).subs(D, 4))
        good = abs(num - val) < 1e-9
        ok &= good
        print(('PASS ' if good else 'FAIL ') + 'trace of %s (4D numeric vs engine)' % ''.join(names))
    # (2) D-dim contraction identities
    t = contract(trace([('i', 'm'), ('p', 'a'), ('i', 'm'), ('p', 'b')]))     # Tr[g^m a g_m b] = -(D-2) 4 a.b
    good = sp.simplify(t - (-(D - 2) * 4 * dot('a', 'b'))) == 0
    ok &= good; print(('PASS ' if good else 'FAIL ') + 'Tr[gamma^m a gamma_m b] = -4(D-2) a.b')
    t = contract(trace([('i', 'm'), ('p', 'a'), ('p', 'b'), ('i', 'm'), ('p', 'c'), ('p', 'e')]))
    # gamma^m a b gamma_m = 4 a.b - (4-D) a b
    ref = 4 * dot('a', 'b') * 4 * dot('c', 'e') - (4 - D) * trace([('p', 'a'), ('p', 'b'), ('p', 'c'), ('p', 'e')])
    good = sp.simplify(t - sp.expand(ref)) == 0
    ok &= good; print(('PASS ' if good else 'FAIL ') + 'gamma^m a b gamma_m = 4 a.b - (4-D) a b (inside a trace)')
    t = contract(trace([('i', 'm'), ('p', 'a'), ('p', 'b'), ('p', 'c'), ('i', 'm'), ('p', 'e')]))
    # gamma^m a b c gamma_m = -2 c b a + (4-D) a b c
    ref = -2 * trace([('p', 'c'), ('p', 'b'), ('p', 'a'), ('p', 'e')]) + (4 - D) * trace([('p', 'a'), ('p', 'b'), ('p', 'c'), ('p', 'e')])
    good = sp.simplify(t - sp.expand(ref)) == 0
    ok &= good; print(('PASS ' if good else 'FAIL ') + 'gamma^m a b c gamma_m = -2 c b a + (4-D) a b c (inside a trace)')
    t = contract(trace([('i', 'm'), ('i', 'n'), ('i', 'm'), ('i', 'n')]))
    good = sp.simplify(t - 4 * D * (2 - D)) == 0      # gamma^m gamma^n gamma_m gamma_n = -(D-2) D
    ok &= good; print(('PASS ' if good else 'FAIL ') + 'Tr[g^m g^n g_m g_n] = 4 D (2-D)')
    print('SELFTEST', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    _self_test()
