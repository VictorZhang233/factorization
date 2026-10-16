# -*- coding: utf-8 -*-
"""
E22 (independent check of the technical core of Collins-Diehl, hep-ph/9907498, Sec. II).
(1) CD eq. (1): gamma^lambda gamma^+ gamma^i gamma_lambda = -eps gamma^+ gamma^i in D = 4 - eps (CD's convention).
    Checked with explicit Clifford algebras in D = 4, 6, 8, 10 (dimension 2^{D/2}); the result is linear in D,
    gamma^l a b gamma_l = 4 a.b - (4 - D) a b, so it holds for all D.
(2) Toy version of CD eqs. (I)-(I.bar): Born ~ eps, collinear pole ~ 1/eps.  The unsubtracted one-loop term has a finite,
    chirality-violating remainder; the subtraction H0 * f1 (Born ~ eps times the MS-bar pole of the parton density) removes it.
Run: python3 -I e22_dirac.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = nfail = 0
def check(label, ok, extra=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + label + (('   [' + str(extra) + ']') if extra else ''))

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
e2 = np.eye(2, dtype=complex)

def euclid_gammas(n):
    """2n Hermitian matrices of size 2^n with {G_a, G_b} = 2 delta_ab (Jordan-Wigner)."""
    mats = []
    for k in range(n):
        for s in (s1, s2):
            ops = [s3] * k + [s] + [e2] * (n - k - 1)
            m = ops[0]
            for o in ops[1:]:
                m = np.kron(m, o)
            mats.append(m)
    return mats

def minkowski_gammas(D):
    E = euclid_gammas(D // 2)
    g = [E[0]] + [1j * E[a] for a in range(1, D)]    # gamma^0 hermitian, gamma^k antihermitian
    metric = np.diag([1.0] + [-1.0] * (D - 1))
    return g, metric

for D in (4, 6, 8, 10):
    g, met = minkowski_gammas(D)
    ok = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * met[a, b] * np.eye(len(g[0]))) for a in range(D) for b in range(D))
    gplus = (g[0] + g[3]) / np.sqrt(2)
    lhs = sum(met[l, l] * g[l] @ gplus @ g[1] @ g[l] for l in range(D))   # gamma^l ... gamma_l
    rhs = -(4 - D) * gplus @ g[1]
    check('D = %2d: Clifford algebra; gamma^l gamma^+ gamma^1 gamma_l = -(4-D) gamma^+ gamma^1' % D, ok and np.allclose(lhs, rhs))
print('   => with D = 4 - eps (CD notation): gamma^l gamma^+ gamma^i gamma_l = -eps gamma^+ gamma^i  (CD eq. (1)); zero in D = 4.')

# (2) toy subtraction: A1 = Born(eps) * [pole(eps) + finite], Born = eps * b, pole = 2/eps (MS-bar normalised)
eps, b, c = sp.symbols('epsilon b c')
Born = eps * b
loop = 2 / eps + c                     # unsubtracted collinear-divergent loop factor (k_T integral in 4-eps dims)
A1 = sp.expand(Born * loop)
f1 = 2 / eps                           # one-loop parton density (MS-bar: pure pole) on a quark target
H1 = sp.expand(A1 - Born * f1)
check('unsubtracted A1 -> 2 b at eps = 0 (finite, chirality-violating: what Hoodbhoy-Lu kept)', sp.limit(A1, eps, 0) == 2 * b)
check('subtracted H1 = A1 - H0 * f1 -> 0 at eps = 0 (CD: the subtraction cancels the eps/eps term)', sp.limit(H1, eps, 0) == 0)
print('-' * 70)
print('e22_dirac: %d PASS, %d FAIL' % (npass, nfail))
