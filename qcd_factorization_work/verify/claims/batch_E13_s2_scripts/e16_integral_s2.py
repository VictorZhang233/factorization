#!/usr/bin/env python3
"""E16 stage-2: (i) the 1/480 coefficient from the *exact* BFH boundaries
(u(k)=Theta(tau - (kT/Q) tan(theta/2)), theta in [kT/Q, 1], mu_F = tau Q), numerically for
several tau and a polynomial fit in L = ln(1/tau); (ii) BCH: the O(a b^2) term of
V^dag V with V = exp(a S_ad + i b S_s) equals -(1/3) a b^2 [S_s,[S_s,S_ad]] (random matrices).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
from numpy.polynomial import polynomial as P
import mpmath as mp

def I_exact(L):
    # variables: l = ln(kT/(tau Q)) in [0, L]; theta in [kT/Q, 1]  -> t = ln(1/theta) in [0, L - l]
    # u: tan(theta/2) < exp(-l)  <=> theta < 2 atan(exp(-l))  <=> t > -ln(2 atan(exp(-l)))
    def inner(l):
        tlow = max(0.0, -mp.log(2*mp.atan(mp.e**(-l))))
        thigh = L - l
        return mp.mpf(0) if thigh <= tlow else (thigh - tlow)
    f = lambda l: 2*l**4*inner(l)       # 2 u(k) * L2 * ln^2 = 2 l^2 * l^2
    # integrate piecewise (kink where thigh = tlow ~ l = (L+ln2)/2)
    lk = mp.findroot(lambda l: (L - l) + mp.log(2*mp.atan(mp.e**(-l))), (L + mp.log(2))/2)
    return mp.quad(f, [0, 1, lk, L])

mp.mp.dps = 30
Ls = [20, 30, 40, 60, 80, 100, 140, 200]
vals = [I_exact(mp.mpf(L)) for L in Ls]
# fit polynomial of degree 6 in L
A = np.array([[float(L)**k for k in range(7)] for L in Ls])
c, *_ = np.linalg.lstsq(A, np.array([float(v) for v in vals]), rcond=None)
print('fit coefficients c_k of L^k:', ['%.6g' % x for x in c])
print('L^6 coefficient = %.10f ; 1/480 = %.10f' % (c[6], 1/480))
print('L^5 coefficient = %.8f ; expected 6 ln2/480 = %.8f (from tan(theta/2) ~ theta/2)' % (c[5], 6*np.log(2)/480))
ok = abs(c[6] - 1/480) < 1e-8
print(('PASS' if ok else 'FAIL'), 'exact-boundary integral = L^6/480 + O(L^5)')
# simplified LL integral, exact: 2 int_0^{L/2} l^4 (L-2l) dl
import sympy as sp
l, Ls_ = sp.symbols('l L', positive=True)
simp = sp.integrate(2*l**4*(Ls_ - 2*l), (l, 0, Ls_/2))
print('LL integral =', sp.simplify(simp), '->', ('PASS' if sp.simplify(simp - Ls_**6/480) == 0 else 'FAIL'))

# (ii) BCH check
rng = np.random.default_rng(7)
def herm(n):
    X = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); return (X + X.conj().T)/2
from scipy.linalg import expm
n = 5; Sad, Ss = herm(n), herm(n)
def VdV(a, b):
    V = expm(a*Sad + 1j*b*Ss); return V.conj().T @ V
# extract coefficient of a^1 b^2 by finite differences: d/da d^2/db^2 /2 at 0
h = 1e-3
def f(a, b): return VdV(a, b)
d = (f(h, h) - 2*f(h, 0) + f(h, -h) - f(-h, h) + 2*f(-h, 0) - f(-h, -h))/(2*h)/(h*h)/2
comm = lambda X, Y: X @ Y - Y @ X
pred = -(1/3)*comm(Ss, comm(Ss, Sad))
print('BCH a b^2 coefficient vs -(1/3)[S_s,[S_s,S_ad]]: max dev = %.2e' % np.max(np.abs(d - pred)))
print(('PASS' if np.max(np.abs(d - pred)) < 1e-4 else 'FAIL'), 'V^dag V|_{a b^2} = -(1/3) a b^2 [Ss,[Ss,Sad]] = (1/3) a (i b)^2 [Ss,[Ss,Sad]]')
# with i b = -i pi (as/pi) ln : (ib)^2 = (-i pi ln)^2 (as/pi)^2 -> BFH's third term (1/3) L2 ((-i pi) ln)^2 [Ts^2,[Ts^2,Tad^2]]
# single commutator: O(a b) term
d1 = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h))/(4*h*h)
print('O(a b) term: max|d1 - i[Sad,Ss]| = %.2e ; max|d1 + i[Sad,Ss]| = %.2e' % (np.max(np.abs(d1 - 1j*comm(Sad, Ss))), np.max(np.abs(d1 + 1j*comm(Sad, Ss)))))
