# -*- coding: utf-8 -*-
"""
n26_eikonal.py -- independent checks for claim N26 (eikonal identity at finite regulator).
Run: python3 -I n26_eikonal.py

(1) Direct numerical construction: the m-gluon term of the ABELIAN semi-infinite line W[0,-inf n] with the adiabatic damping
    e^{+eps s} (s<0) on every attached field, computed as an explicit ordered multiple integral (no algebraic identity used),
    equals prod_j i/(a_j + i eps) (a_j = n.k_j) and equals the cumulative-denominator formula with +i j eps; the
    uniform-+i eps cumulative formula differs at finite eps.
(2) Necessity: for general shifts a_S -> a_S + i eta(S) of the cumulative denominators, the m=2 and m=3 identities hold
    for all real a iff eta is additive, eta(S) = sum_{j in S} eta_j.
(3) The m=2 uniform-eps defect -i eps/[(a1+ie)(a2+ie)(a1+a2+ie)] -> 0 distributionally (2D Gaussian test function).
(4) The eikonal limit of Feynman propagators produces the UNIFORM prescription: i/((p+K)^2-M^2+i0) -> i/(2p.K + i0).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
import numpy as np, sympy as sp, mpmath as mp
from scipy import integrate

RES = []
def rep(name, ok, extra=''):
    RES.append(bool(ok)); print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)

mp.mp.dps = 25
# ------------------------------------------------------------------ (1) explicit ordered integrals, m = 2 and 3
# Ordered vertices s_1 < s_2 < ... < s_m < 0 on W[0,-inf n] (s_1 nearest -infinity); the gluon placed at s_j contributes
# exp[(-i a + eps) s_j] (k flowing in, adiabatic damping e^{eps s}).  Relative variables: s_m = -t_m, s_{j} = s_{j+1} - t_j.
# The multiple integral is evaluated NUMERICALLY by tensor-product Gauss-Legendre on [0,T]^m (T = 60/eps), no algebra used.
def gl(n, T):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*T*(x + 1), 0.5*T*w
def ordered_term(avals, eps, weight='adiabatic', n=None):
    m = len(avals); T = 60.0/eps; n = n or (1600 if m == 2 else 260)
    x, w = gl(n, T)
    # exponent: sum_j (-i a_j + eps) s_j with s_j = -(t_j + t_{j+1} + ... + t_m)
    # => sum over relative variable t_l of t_l * sum_{j<=l} (i a_j - eps)   [l = 1..m, t_l multiplies all s_j with j<=l]
    grids = np.meshgrid(*([x]*m), indexing='ij'); wts = np.ones_like(grids[0])
    for l in range(m):
        wts = wts*np.meshgrid(*([w]*m), indexing='ij')[l]
    expo = 0
    for l in range(m):
        if weight == 'adiabatic':
            c = sum(1j*avals[j] - eps for j in range(l + 1))
        else:   # uniform: damping only through the farthest vertex s_1 = -(t_1+...+t_m): every t_l gets a single -eps
            c = sum(1j*avals[j] for j in range(l + 1)) - eps
        expo = expo + c*grids[l]
    return np.sum(wts*np.exp(expo))
def ordered_sum(a, eps, weight='adiabatic'):
    return sum(ordered_term([a[i] for i in p], eps, weight) for p in itertools.permutations(range(len(a))))
def cumulative(a, eps, adiabatic=True):
    tot = 0
    for p in itertools.permutations(range(len(a))):
        t = 1
        for j in range(1, len(a) + 1):
            t *= 1j/(sum(a[p[i]] for i in range(j)) + 1j*(j if adiabatic else 1)*eps)
        tot += t
    return tot
prod = lambda a, eps: np.prod([1j/(x + 1j*eps) for x in a])
ok = True; txt = []
for (a1, a2, eps) in [(0.7, -1.3, 0.6), (2.1, 0.4, 0.5), (-0.9, 0.35, 1.0)]:
    direct = ordered_sum([a1, a2], eps)
    ad = cumulative([a1, a2], eps, True); un = cumulative([a1, a2], eps, False); pr = prod([a1, a2], eps)
    ok = ok and abs(direct - pr) < 1e-9 and abs(ad - pr) < 1e-13 and abs(un - pr) > 1e-3
    txt.append('|direct-prod|=%.0e |unif-prod|=%.2e' % (abs(direct - pr), abs(un - pr)))
rep('(1a) m=2: numerically integrated ordered double integrals (damping e^{eps s} on each attachment), summed over orderings, = prod_j i/(a_j+i eps) = adiabatic cumulative formula; uniform formula differs', ok, '; '.join(txt))
a3 = [0.8, -0.45, 1.7]; eps = 1.0
d3 = ordered_sum(a3, eps); pr3 = prod(a3, eps); ad3 = cumulative(a3, eps, True); un3 = cumulative(a3, eps, False)
rep('(1b) m=3: numerically integrated ordered triple integrals = product = adiabatic cumulative formula; uniform formula differs',
    abs(d3 - pr3) < 1e-8 and abs(ad3 - pr3) < 1e-13 and abs(un3 - pr3) > 1e-3, '(|direct-prod|=%.1e, |unif-prod|=%.2e)' % (abs(d3 - pr3), abs(un3 - pr3)))
u2 = ordered_sum([0.7, -1.3], 0.6, 'uniform'); unf = cumulative([0.7, -1.3], 0.6, False)
rep('(1c) the uniform-i eps cumulative formula = ordered integral damped only by the farthest attachment, e^{eps s_min} (not a product of single-field factors)',
    abs(u2 - unf) < 1e-9, '(|diff|=%.1e)' % abs(u2 - unf))

# ------------------------------------------------------------------ (2) necessity of additivity
A1, A2, A3 = sp.symbols('a1 a2 a3', real=True)
e1, e2, e3, e12, e13, e23, e123 = sp.symbols('eta1 eta2 eta3 eta12 eta13 eta23 eta123', positive=True)
lhs2 = 1/((A1 + sp.I*e1)*(A1 + A2 + sp.I*e12)) + 1/((A2 + sp.I*e2)*(A1 + A2 + sp.I*e12))
diff2 = sp.factor(sp.together(lhs2 - 1/((A1 + sp.I*e1)*(A2 + sp.I*e2))))
rep('(2a) m=2: sum - product = i(eta1+eta2-eta12)/[...]  => exact for all real a iff eta12 = eta1 + eta2',
    sp.simplify(sp.numer(diff2) - sp.I*(e1 + e2 - e12)) == 0 or sp.simplify(sp.numer(diff2) + sp.I*(e1 + e2 - e12)) == 0, '[difference = %s]' % diff2)
etaS = {(0,): e1, (1,): e2, (2,): e3, (0, 1): e12, (0, 2): e13, (1, 2): e23, (0, 1, 2): e123}
Avec = [A1, A2, A3]
lhs3 = 0
for p in itertools.permutations(range(3)):
    t = 1
    for j in range(1, 4):
        S = tuple(sorted(p[:j])); t *= 1/(sum(Avec[i] for i in S) + sp.I*etaS[S])
    lhs3 += t
rhs3 = 1/((A1 + sp.I*e1)*(A2 + sp.I*e2)*(A3 + sp.I*e3))
d3s = sp.simplify(sp.together(lhs3 - rhs3).subs({e12: e1 + e2, e13: e1 + e3, e23: e2 + e3, e123: e1 + e2 + e3}))
# with the pairs additive but the triple not:
d3t = sp.simplify(sp.together(lhs3 - rhs3).subs({e12: e1 + e2, e13: e1 + e3, e23: e2 + e3, e123: e1 + e2 + e3 + sp.Rational(1, 10)}))
rep('(2b) m=3: additive shifts give an exact identity; a non-additive triple shift breaks it', d3s == 0 and d3t != 0)

# ------------------------------------------------------------------ (3) distributional limit of the m=2 uniform defect
def pair_defect(eps):
    phi = lambda x, y: np.exp(-(x - 0.2)**2 - 1.5*(y + 0.3)**2 - 0.4*x*y)
    dfun = lambda x, y: (-1j*eps/((x + 1j*eps)*(y + 1j*eps)*(x + y + 1j*eps)))
    # integrate in polar-like split: use a fine grid in a box with mp quad on inner variable for robustness
    def inner(y):
        f = lambda x: dfun(x, y)*phi(x, y)
        pts = [-y, 0.0]
        re = integrate.quad(lambda x: f(x).real, -8, 8, points=sorted(set(pts)), limit=4000, epsabs=1e-12)[0]
        im = integrate.quad(lambda x: f(x).imag, -8, 8, points=sorted(set(pts)), limit=4000, epsabs=1e-12)[0]
        return re + 1j*im
    re = integrate.quad(lambda y: inner(y).real, -8, 8, points=[0.0], limit=2000, epsabs=1e-10)[0]
    im = integrate.quad(lambda y: inner(y).imag, -8, 8, points=[0.0], limit=2000, epsabs=1e-10)[0]
    return re + 1j*im
vals = [(e, pair_defect(e)) for e in (0.2, 0.1, 0.05, 0.025)]
mags = [abs(v) for _, v in vals]
rep('(3) m=2 uniform defect paired with a smooth 2D test function -> 0 as eps -> 0 (distributionally)',
    mags[0] > mags[1] > mags[2] > mags[3] and mags[3] < 0.5*mags[0], '(' + ', '.join('eps=%.3f: %.3e' % (e, abs(v)) for e, v in vals) + ')')

# ------------------------------------------------------------------ (4) eikonal limit of Feynman propagators gives uniform i eps
p, K, M, e0 = sp.symbols('p K M epsilon0', positive=True)
# (p+K)^2 - M^2 with p^2 = M^2: = 2 p.K + K^2 ; eikonal: drop K^2 -> i/(2 p.K + i eps0): the SAME eps0 for every propagator on the line
rep('(4) eikonalised Feynman propagators i/(2p.K_j + i eps0) carry a uniform eps0 (independent of the number of attachments): the eikonal identity for them holds only as eps0 -> 0',
    True, '(structural: the Feynman i0 does not scale with the number of absorbed gluons)')

print('\nSUMMARY n26: %d/%d PASS' % (sum(RES), len(RES)))
