# -*- coding: utf-8 -*-
"""
common.py -- shared helpers for the c_scet verification scripts.

Conventions (CONTEXT.md, binding):
  metric (+,-,-,-);  D_mu = d_mu - i g A_mu^a t^a ;  quark-gluon vertex  i g gamma^mu t^a ;
  Tr(t^a t^b) = delta^{ab}/2 ;  D = 4 - 2 eps ;  MSbar: mu^2 -> mu^2 e^{gamma_E}/(4 pi).
  SCET: n = (1,0,0,1), nbar = (1,0,0,-1), n.nbar = 2,
        p^mu = nbar.p n^mu/2 + n.p nbar^mu/2 + p_perp^mu ;  nbar.p = sqrt2 p^+ , n.p = sqrt2 p^-.

Contents:
  * Check     : PASS/FAIL recorder (prints a summary; exit code 1 on failure)
  * Dirac     : explicit 4x4 Dirac-representation gamma matrices (numpy, complex)
  * spinors   : massive/massless Dirac spinors u, v (Dirac representation)
  * su3       : Gell-Mann generators t^a = lambda^a/2
  * DTrace    : symbolic D-dimensional trace engine (Tr 1 = 4), with index contraction
"""
import sys, os, itertools, functools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------------------------
class Check:
    def __init__(self, title):
        self.title = title
        self.n_pass = 0
        self.n_fail = 0
        self.items = []
        print('=' * 100)
        print(title)
        print('=' * 100)

    def __call__(self, name, ok, detail=''):
        ok = bool(ok)
        tag = 'PASS' if ok else 'FAIL'
        if ok:
            self.n_pass += 1
        else:
            self.n_fail += 1
        self.items.append((name, tag, detail))
        print(f'[{tag}] {name}' + (f'   :: {detail}' if detail else ''))
        sys.stdout.flush()
        return ok

    def summary(self):
        print('-' * 100)
        print(f'{self.title}: {self.n_pass} PASS, {self.n_fail} FAIL')
        print('-' * 100)
        return self.n_fail == 0


def close(a, b, tol=1e-9):
    a = np.asarray(a, dtype=complex)
    b = np.asarray(b, dtype=complex)
    scale = max(1.0, float(np.max(np.abs(b))) if b.size else 1.0)
    return float(np.max(np.abs(a - b))) <= tol * scale


# ----------------------------------------------------------------------------------------------
# Dirac matrices (Dirac representation)
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
sig = [np.array([[0, 1], [1, 0]], dtype=complex),
       np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]
G0 = np.block([[I2, Z2], [Z2, -I2]])
Gi = [np.block([[Z2, s], [-s, Z2]]) for s in sig]
GAM = [G0] + Gi                     # gamma^mu, upper index
G5 = 1j * GAM[0] @ GAM[1] @ GAM[2] @ GAM[3]
ID4 = np.eye(4, dtype=complex)
METRIC = np.diag([1.0, -1.0, -1.0, -1.0])


def lower(v):
    return METRIC @ np.asarray(v)


def mdot(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def slash(p):
    """p-slash = gamma^mu p_mu"""
    pl = lower(p)
    return sum(GAM[m] * pl[m] for m in range(4))


def bar(spinor):
    return spinor.conj().T @ G0


NVEC = np.array([1.0, 0.0, 0.0, 1.0])
NBVEC = np.array([1.0, 0.0, 0.0, -1.0])


def lc_components(p):
    """return (nbar.p, n.p, p_perp^mu) for the SCET decomposition"""
    p = np.asarray(p, dtype=float)
    nbp = mdot(NBVEC, p)
    np_ = mdot(NVEC, p)
    perp = p - nbp * NVEC / 2 - np_ * NBVEC / 2
    return nbp, np_, perp


def u_spinor(p, s, m=0.0):
    """Dirac spinor u(p,s), s = 0 (up), 1 (down) along z; normalization ubar u = 2m, u^dag u = 2E"""
    p = np.asarray(p, dtype=complex)
    E = p[0].real
    chi = np.array([1, 0], dtype=complex) if s == 0 else np.array([0, 1], dtype=complex)
    sp_ = sum(sig[i] * p[i + 1] for i in range(3))
    return np.concatenate([np.sqrt(E + m) * chi, (sp_ @ chi) / np.sqrt(E + m)])


def v_spinor(p, s, m=0.0):
    """Dirac spinor v(p,s) = C ubar^T convention: v = [ (sigma.p) eta/sqrt(E+m), sqrt(E+m) eta ],
       eta_s = -i sigma_2 chi_s^* (so that v describes the antiparticle with spin s)."""
    p = np.asarray(p, dtype=complex)
    E = p[0].real
    chi = np.array([1, 0], dtype=complex) if s == 0 else np.array([0, 1], dtype=complex)
    eta = -1j * sig[1] @ chi.conj()
    sp_ = sum(sig[i] * p[i + 1] for i in range(3))
    return np.concatenate([(sp_ @ eta) / np.sqrt(E + m), np.sqrt(E + m) * eta])


# ----------------------------------------------------------------------------------------------
# SU(3) generators
def su3_generators():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return l / 2.0


T_SU3 = su3_generators()


# ----------------------------------------------------------------------------------------------
# Symbolic D-dimensional trace engine.
# A gamma string is a tuple of "slots"; each slot is a string naming either a vector (slashed)
# or a Lorentz index.  The caller declares which names are indices (set `indices`).
# Tr[1] = 4.  Result: sympy expression in dot-product symbols dot(a,b), metric contractions
# done automatically; D symbolic.
D = sp.Symbol('D')

_dot_cache = {}


def dot(a, b):
    """symbol for the scalar product a.b of two vectors (symmetric)"""
    a, b = sorted([a, b])
    key = (a, b)
    if key not in _dot_cache:
        _dot_cache[key] = sp.Symbol(f'{a}.{b}' if a != b else f'{a}^2')
    return _dot_cache[key]


def _trace_pairs(slots):
    """return list of (sign, [pairs]) for Tr[gamma^{slots}] / 4 (complete pairing expansion)."""
    n = len(slots)
    if n == 0:
        return [(1, [])]
    if n % 2 == 1:
        return []
    out = []
    first = slots[0]
    for k in range(1, n):
        sign = 1 if (k % 2 == 1) else -1
        rest = slots[1:k] + slots[k + 1:]
        for s, pr in _trace_pairs(rest):
            out.append((sign * s, [(first, slots[k])] + pr))
    return out


def _contract(pairs, indices):
    """contract a list of pairs (x,y); returns (factor, remaining pairs) where remaining pairs
       contain no repeated index.  Pair of the same index -> D."""
    pairs = [tuple(p) for p in pairs]
    factor = sp.Integer(1)
    changed = True
    while changed:
        changed = False
        # self-contracted metric g^{i}_{i}
        for j, (x, y) in enumerate(pairs):
            if x == y and x in indices:
                factor *= D
                pairs.pop(j)
                changed = True
                break
        if changed:
            continue
        # find an index appearing in two different pairs
        seen = {}
        for j, (x, y) in enumerate(pairs):
            for z in (x, y):
                if z in indices:
                    if z in seen and seen[z] != j:
                        j1, j2 = seen[z], j
                        p1, p2 = pairs[j1], pairs[j2]
                        o1 = p1[1] if p1[0] == z else p1[0]
                        o2 = p2[1] if p2[0] == z else p2[0]
                        newp = (o1, o2)
                        for jj in sorted([j1, j2], reverse=True):
                            pairs.pop(jj)
                        pairs.append(newp)
                        changed = True
                        break
                    seen[z] = j
            if changed:
                break
    return factor, pairs


def dtrace(slots, indices=(), free_tensor=None):
    """D-dimensional trace of a product of gamma matrices.
       slots   : sequence of names (vectors or indices)
       indices : names that are Lorentz indices (repeated ones are contracted)
       Returns sympy expression; if free (uncontracted) indices remain, they appear as
       symbols g[i,j] or comp[v,i] (only used for checks)."""
    indices = set(indices)
    res = sp.Integer(0)
    for sign, pairs in _trace_pairs(tuple(slots)):
        fac, rem = _contract(pairs, indices)
        term = sp.Integer(4 * sign) * fac
        for (x, y) in rem:
            if x in indices or y in indices:
                term *= sp.Symbol(f'g[{x},{y}]' if (x in indices and y in indices) else
                                  f'c[{x if x not in indices else y},{y if y in indices else x}]')
            else:
                term *= dot(x, y)
        res += term
    return sp.expand(res)


def dtrace_sum(terms, indices=()):
    """terms: list of (coefficient, slots) ; returns sum coefficient*Tr[slots]"""
    return sp.expand(sum(c * dtrace(s, indices) for c, s in terms))


# ---------------------------------------------------------------------------------------------
def gamma_E():
    return sp.EulerGamma


def series_eps(expr, eps, n):
    """Laurent series of expr in eps up to and including eps^n"""
    return sp.series(expr, eps, 0, n + 1).removeO()


if __name__ == '__main__':
    # self-test of the trace engine against explicit 4x4 matrices at D = 4
    ck = Check('common.py self-test: D-dim trace engine vs explicit 4x4 traces (D=4)')
    rng = np.random.default_rng(1)
    vecs = {v: rng.normal(size=4) for v in 'abcdef'}
    def num_tr(slots):
        M = ID4.copy()
        for s in slots:
            M = M @ slash(vecs[s])
        return np.trace(M)
    def sym_val(expr):
        subs = {}
        for x in 'abcdef':
            for y in 'abcdef':
                subs[dot(x, y)] = mdot(vecs[x], vecs[y])
        return complex(expr.subs(subs).subs(D, 4))
    for slots in ['ab', 'abcd', 'abcdef', 'aabb', 'abab', 'abcabc']:
        ck(f'Tr[{slots}]', abs(sym_val(dtrace(tuple(slots))) - num_tr(slots)) < 1e-9)
    # contracted indices: Tr[g^m a g_m b] = (2-D) Tr[a b]
    e = dtrace(('m', 'a', 'm', 'b'), indices=('m',))
    ck('Tr[gamma^m a gamma_m b] = (2-D)*4 a.b', sp.simplify(e - (2 - D) * 4 * dot('a', 'b')) == 0, str(e))
    e = dtrace(('m', 'a', 'b', 'c', 'm', 'd'), indices=('m',))
    ref = -2 * dtrace(('c', 'b', 'a', 'd')) + (4 - D) * dtrace(('a', 'b', 'c', 'd'))
    ck('gamma^m a b c gamma_m = -2 c b a + (4-D) a b c  (inside trace)', sp.simplify(e - ref) == 0)
    e = dtrace(('m', 'a', 'b', 'm', 'c', 'd'), indices=('m',))
    ref = 4 * dot('a', 'b') * dtrace(('c', 'd')) - (4 - D) * dtrace(('a', 'b', 'c', 'd'))
    ck('gamma^m a b gamma_m = 4 a.b - (4-D) a b  (inside trace)', sp.simplify(e - ref) == 0)
    ck.summary()
