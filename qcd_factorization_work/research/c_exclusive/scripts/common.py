# -*- coding: utf-8 -*-
"""
common.py -- shared helpers for research/c_exclusive.

Conventions (match CONTEXT.md, plus the gamma_5 / epsilon conventions fixed here):
  metric (+,-,-,-); light-front v^pm = (v^0 pm v^3)/sqrt2; v.w = v^+ w^- + v^- w^+ - v_T.w_T
  Dirac representation; gamma_5 = i g^0 g^1 g^2 g^3; epsilon^{0123} = +1  (so epsilon_{0123} = -1)
  => Tr(g^mu g^nu g^rho g^sigma g5) = -4 i epsilon^{mu nu rho sigma}   (checked in s1)
  QCD vertex  +i g gamma^mu t^a ; quark propagator i(kslash)/(k^2+i0); gluon -i g_{mu nu}/(k^2+i0)

Four-vectors are stored as python lists of CONTRAVARIANT Cartesian components [v0,v1,v2,v3].
lc(vp, vm, v1, v2) builds such a list from light-front components.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
import sympy as sp

I = sp.I
sqrt2 = sp.sqrt(2)

# ---------------------------------------------------------------- Dirac matrices
_s1 = sp.Matrix([[0, 1], [1, 0]])
_s2 = sp.Matrix([[0, -I], [I, 0]])
_s3 = sp.Matrix([[1, 0], [0, -1]])
_Z = sp.zeros(2)
_E = sp.eye(2)
SIG1, SIG2, SIG3 = _s1, _s2, _s3          # Pauli matrices (public names)


def _blk(a, b, c, d):
    M = sp.zeros(4)
    M[0:2, 0:2] = a
    M[0:2, 2:4] = b
    M[2:4, 0:2] = c
    M[2:4, 2:4] = d
    return M


g0 = _blk(_E, _Z, _Z, -_E)
g1 = _blk(_Z, _s1, -_s1, _Z)
g2 = _blk(_Z, _s2, -_s2, _Z)
g3 = _blk(_Z, _s3, -_s3, _Z)
G = [g0, g1, g2, g3]                      # gamma^mu (upper index)
g5 = sp.simplify(I * g0 * g1 * g2 * g3)
E4 = sp.eye(4)
METRIC = [1, -1, -1, -1]
gp = (g0 + g3) / sqrt2                     # gamma^+
gm = (g0 - g3) / sqrt2                     # gamma^-
GL = [METRIC[m] * G[m] for m in range(4)]  # gamma_mu (lower index)


def lc(vp, vm, v1=0, v2=0):
    """contravariant Cartesian components from light-front components (v^+, v^-, v^1, v^2)"""
    return [sp.sympify(c_) for c_ in ((vp + vm) / sqrt2, v1, v2, (vp - vm) / sqrt2)]


def plus(v):
    return (v[0] + v[3]) / sqrt2


def minus(v):
    return (v[0] - v[3]) / sqrt2


def dot(a, b):
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def add(*vs):
    return [sum(v[i] for v in vs) for i in range(4)]


def scal(c, v):
    return [c * vi for vi in v]


def sub(a, b):
    return [a[i] - b[i] for i in range(4)]


def slash(v):
    return g0 * v[0] - g1 * v[1] - g2 * v[2] - g3 * v[3]


def tr(M):
    return sp.expand(M.trace())


def levi(mu, nu, rho, sig):
    """epsilon^{mu nu rho sigma} with epsilon^{0123}=+1 (upper indices)"""
    idx = [mu, nu, rho, sig]
    if len(set(idx)) < 4:
        return 0
    # parity of permutation
    perm = list(idx)
    sgn = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if perm[i] > perm[j]:
                sgn = -sgn
    return sgn


def eps_contract(a, b, c, d):
    """epsilon^{mu nu rho sigma} a_mu b_nu c_rho d_sigma with vectors given contravariantly"""
    low = lambda v: [METRIC[i] * v[i] for i in range(4)]
    A, B, C, D = low(a), low(b), low(c), low(d)
    s = 0
    for mu, nu, rho, sig in itertools.permutations(range(4)):
        s += levi(mu, nu, rho, sig) * A[mu] * B[nu] * C[rho] * D[sig]
    return sp.expand(s)


# ---------------------------------------------------------------- PASS/FAIL bookkeeping
class Checker:
    def __init__(self, name):
        self.name = name
        self.results = []

    def check(self, label, ok, detail=''):
        ok = bool(ok)
        self.results.append((label, ok))
        print(('PASS' if ok else 'FAIL') + '  ' + label + (('   [' + str(detail) + ']') if detail != '' else ''))
        return ok

    def zero(self, label, expr, detail=''):
        e = sp.simplify(sp.expand(expr))
        return self.check(label, e == 0, detail if detail != '' else ('residual=' + str(e) if e != 0 else ''))

    def close(self, label, a, b, tol=1e-8, detail=''):
        a = complex(a)
        b = complex(b)
        ok = abs(a - b) <= tol * max(1.0, abs(b))
        return self.check(label, ok, detail if detail != '' else 'got %.12g%+.3gi, expected %.12g%+.3gi' % (a.real, a.imag, b.real, b.imag))

    def summary(self):
        n = len(self.results)
        npass = sum(1 for _, ok in self.results if ok)
        print('-' * 70)
        print('%s: %d/%d PASS' % (self.name, npass, n))
        if npass != n:
            for lab, ok in self.results:
                if not ok:
                    print('   FAILED: ' + lab)
        return npass == n
