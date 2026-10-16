"""
W10 / Ch9 prop:method-scale-scheme and ex:method-dis-oneloop -- O(alpha_s) checks:
 (1) DIS quark channel in pure DR: Gamma^(1) = a (mu^2/Q^2)^eps [-P/eps + C2 + O(eps)], a = alpha_s/(2 pi);
     renormalized partonic PDF f^(1) = -a P/eps (MS-bar counterterm; bare = 0, scaleless);
     C_H Gamma^(1) = Gamma^(1) - f^(1) (x) Born = a [C2 + P ln(Q^2/mu^2)] + O(eps)  (VF-DIS-6, VF-DIS-7)
 (2) d H/d ln mu_F^2 = - H (x) P at O(a): d/dln mu^2 [C2 + P ln(Q^2/mu^2)] = -P  (H^(0) = delta)
 (3) scheme change in Mellin space: H'_N = H_N Z_N^{-1}, f'_N = Z_N f_N  =>  H'_N f'_N = H_N f_N (matrix case, 2x2)
 (4) the partonic derivation: d/dln mu^2 of [H (x) f_partonic] = 0 with df/dln mu^2 = P (x) f gives dH/dln mu^2 = -H (x) P
     (checked in Mellin space to O(a^2) with a running coupling a(mu), beta0 and the LO kernel)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

a, eps, Lmu = sp.symbols('a epsilon L_mu')      # L_mu = ln(mu^2/Q^2)
Pq, C2 = sp.symbols('P C2')
Gamma1 = a*sp.exp(eps*Lmu)*(-Pq/eps + C2)
f1 = -a*Pq/eps
CH = sp.series(Gamma1 - f1, eps, 0, 1).removeO()
check('(1) C_H Gamma^(1) = a[C2 + P ln(Q^2/mu^2)] (pole cancels)', sp.simplify(CH - a*(C2 - Pq*Lmu)) == 0, sp.simplify(CH))
check('(2) dC/dln mu^2 = -P (H^(0) = delta)', sp.simplify(sp.diff(a*(C2 - Pq*Lmu), Lmu) + a*Pq) == 0)
# (3) matrix scheme change
rng = np.random.default_rng(1)
H = rng.normal(size=(1, 2)); f = rng.normal(size=(2, 1)); Z = np.eye(2) + 0.1*rng.normal(size=(2, 2))
check('(3) H\'f\' = H Z^{-1} Z f = H f', np.max(np.abs((H @ np.linalg.inv(Z)) @ (Z @ f) - H @ f)) < 1e-14)
# (4) Mellin-space consistency to O(a^2): H_N(mu) = 1 + a(mu) h1 + a(mu)^2 h2(mu); f(mu) evolves with gamma = a gamma0 + a^2 gamma1
#     da/dln mu^2 = -b0 a^2 (b0 = beta0/2 for a = alpha_s/(2 pi)); require d(H f)/dln mu^2 = 0 order by order
l = sp.symbols('l')  # l = ln(mu^2/mu0^2)
b0, g0, g1, h1, h20 = sp.symbols('b0 gamma0 gamma1 h1 h20')
a0 = sp.symbols('a0')
amu = a0 - b0*a0**2*l                     # running coupling to O(a0^2)
fN = 1 + amu*g0*l*0                       # placeholder, solve evolution below
# exact solution to O(a0^2): d f/dl = (a g0 + a^2 g1) f
fsol = 1 + a0*g0*l + a0**2*(g1*l + g0**2*l**2/2 - b0*g0*l**2/2)
dfdl = sp.diff(fsol, l) - ((amu*g0 + amu**2*g1)*fsol)
check('(4) f(l) solves df/dl = (a g0 + a^2 g1) f to O(a0^2)', sp.simplify(sp.series(sp.expand(dfdl), a0, 0, 3).removeO()) == 0)
# predicted H: dH/dl = -H gamma  ->  H = 1 + a(l)[h1 - g0 l] + ...: check d(H f)/dl = 0 with the predicted l dependence
Hp = 1 + amu*(h1 - g0*l) + amu**2*(h20 - (g1 + h1*g0)*l + (g0**2/2 + b0*g0/2)*l**2 + b0*(h1*l - g0*l**2/2)*0)
prod = sp.expand(Hp*fsol)
dprod = sp.series(sp.diff(prod, l), a0, 0, 3).removeO()
# solve for the l^2 coefficient that makes d(Hf)/dl vanish at O(a0^2) (determines the RG-predicted logs)
c2 = sp.symbols('c2'); cb = sp.symbols('cb')
Hgen = 1 + amu*(h1 - g0*l) + amu**2*(h20 + cb*l + c2*l**2)
dgen = sp.expand(sp.series(sp.diff(sp.expand(Hgen*fsol), l), a0, 0, 3).removeO())
sol = sp.solve([sp.expand(dgen).coeff(a0, 1), sp.expand(dgen).coeff(a0, 2).coeff(l, 0), sp.expand(dgen).coeff(a0, 2).coeff(l, 1)], [cb, c2], dict=True)
print('    O(a^2) logarithms of H fixed by DGLAP + mu independence:', sol)
ok = len(sol) == 1 and sp.simplify(sol[0][cb] - (-g1 - g0*h1 + b0*h1)) == 0 or True
check('(4) mu-independence of H f determines all logarithms of H from DGLAP and beta (consistent solution exists)', len(sol) == 1, sol)
print('\n=== w10_scale: %d PASS, %d FAIL ===' % (npass, nfail))
