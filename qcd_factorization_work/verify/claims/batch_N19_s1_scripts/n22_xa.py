"""
n22_xa.py -- independent check of claim N22 (X_A model of BBNS/BN annihilation; prescription dependence).
Integrands: BBNS 2001 (hep-ph/0104110) building blocks A_k^{i,f} (read from the arXiv source), asymptotic DAs
Phi(x) = 6 x xbar, twist-3 Phi_p = 1.  BN 2003 (hep-ph/0308039) eq. (XAdef): int_0^1 dy/y -> X_A, int_0^1 dy ln y/y -> -X_A^2/2,
'and similarly for M2 with y -> xbar'.  Cutoff realisation: y > delta (resp. xbar > delta), X_A = ln(1/delta).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 40
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''))
Phi = lambda t: 6*t*(1 - t)
# ---------------------------------------------------------------- BN-rule values (in units of pi alpha_s)
def A1i(delta, r1, r2):      # integrand: Phi2(x)Phi1(y)[1/(y(1-x ybar)) + 1/(xbar^2 y)] + r1 r2 2/(xbar y)
    d = mp.mpf(delta)
    fin = mp.quad(lambda x: mp.quad(lambda y: Phi(x)*Phi(y)/(y*(1 - x*(1 - y))), [0, 1]), [0, 1])    # convergent
    t2 = mp.quad(lambda x: Phi(x)/(1 - x)**2, [0, 1 - d])*mp.quad(lambda y: Phi(y)/y, [0, 1])          # xbar endpoint cut
    t3 = 2*r1*r2*mp.quad(lambda x: 1/(1 - x), [0, 1 - d])*mp.quad(lambda y: 1/y, [d, 1])
    return fin + t2 + t3
def A3f(delta, r1, r2):      # r1 Phi2(x) 2(1+xbar)/(xbar^2 y) + r2 Phi1(y) 2(1+y)/(xbar y^2)
    d = mp.mpf(delta)
    a = r1*mp.quad(lambda x: Phi(x)*2*(2 - x)/(1 - x)**2, [0, 1 - d])*mp.quad(lambda y: 1/y, [d, 1])
    b = r2*mp.quad(lambda x: 1/(1 - x), [0, 1 - d])*mp.quad(lambda y: Phi(y)*2*(1 + y)/y**2, [d, 1])
    return a + b
def A3i_r1_BN(delta):       # r1 term: 12 x ybar/(y(1-x ybar)), x integrated fully, y > delta (BN rule)
    d = mp.mpf(delta)
    inner = lambda y: -1/(1 - y) - mp.log(y)/(1 - y)**2          # int_0^1 x dx/(1 - x ybar)
    return 12*mp.quad(lambda y: (1 - y)/y*inner(y), [d, 10*d, 1e-3, 0.5, 1])
def A3i_r1_double(delta):   # same integrand, x < 1-delta AND y > delta
    d = mp.mpf(delta)
    f = lambda y: -(1 - d)/y - mp.log(y + d*(1 - y))/(y*(1 - y))
    return 12*mp.quad(f, [d, 10*d, 100*d, 1e-3, 0.5, 1])
def A3i_r2_double(delta):   # r2 term: 12 x ybar/(xbar (1 - x ybar)) with the same double cutoff (direct 2D)
    d = mp.mpf(delta)
    g = lambda x, y: 12*x*(1 - y)/((1 - x)*(1 - x*(1 - y)))
    return mp.quad(g, [0, 0.5, 1 - 100*d, 1 - 10*d, 1 - d], [d, 10*d, 100*d, 0.5, 1])
for delta in ['1e-6', '1e-9']:
    d = mp.mpf(delta); X = mp.log(1/d); r = mp.mpf('0.8'); r1, r2 = mp.mpf('0.9'), mp.mpf('0.6')
    v = A1i(d, r, r); bn = 18*(X - 4 + mp.pi**2/3) + 2*r**2*X**2
    check('A_1^i = pi a_s[18(X_A - 4 + pi^2/3) + 2 r_chi^2 X_A^2] (= 2 pi a_s[9(...) + r1 r2 X_A^2]), delta=%s' % delta, abs(v - bn) < 1e-4, 'diff %s' % mp.nstr(v - bn, 3))
    v = A3f(d, r1, r2); bn = 6*(r1 + r2)*(2*X**2 - X)
    check('A_3^f = 6 pi a_s (r1 + r2)(2 X_A^2 - X_A), delta=%s' % delta, abs(v - bn) < 1e-3, 'diff %s' % mp.nstr(v - bn, 3))
    v = A3i_r1_BN(d); bn = 6*(X**2 - 2*X + mp.pi**2/3)
    check('A_3^i r1-term (BN rule) = 6 pi a_s r1 (X_A^2 - 2 X_A + pi^2/3) up to O(delta ln^2 delta), delta=%s' % delta, abs(v - bn) < 10*d*X**2, 'diff %s' % mp.nstr(v - bn, 3))
# finite piece of A_1^i
fin = mp.quad(lambda x: mp.quad(lambda y: Phi(x)*Phi(y)/(y*(1 - x*(1 - y))), [0, 1]), [0, 1])
check('finite piece 36 int int x xbar ybar/(1 - x ybar) = 18(pi^2/3 - 3)', abs(fin - 18*(mp.pi**2/3 - 3)) < 1e-25)
# ---------------------------------------------------------------- prescription dependence
print('      prescription dependence of the A_3^i r1-term (units pi alpha_s r_chi^{M1}):')
for delta in ['1e-4', '1e-6', '1e-8', '1e-12']:
    d = mp.mpf(delta); X = mp.log(1/d)
    dbl = A3i_r1_double(d); bn = 6*(X**2 - 2*X + mp.pi**2/3)
    print('      delta=%-6s X_A=%8.4f  double cutoff %.10f   BN rule %.10f   shift %.10f' % (delta, float(X), float(dbl), float(bn), float(dbl - bn)))
d = mp.mpf('1e-6'); X = mp.log(1/d)
shift = A3i_r1_double(d) - 6*(X**2 - 2*X + mp.pi**2/3)
check('at X_A = 13.8 (delta = 1e-6) the shift is -pi^2 = -9.8696, NOT -21.6', abs(shift + mp.pi**2) < 1e-4, 'shift = %s' % mp.nstr(shift, 10))
d = mp.mpf('1e-12'); X = mp.log(1/d)
check('shift -> -pi^2 as delta -> 0 (X_A-independent): double cutoff = 6X_A^2 - 12X_A + pi^2 + O(delta ln^2 delta)',
      abs(A3i_r1_double(d) - (6*X**2 - 12*X + mp.pi**2)) < 1e-8)
# the removed corner region x in (1-delta,1), y in (delta,1) carries exactly pi^2 (12 int ln(1+delta/y)/y dy -> 12 pi^2/12)
d = mp.mpf('1e-8')
corner = 12*mp.quad(lambda y: mp.log((y + d*(1 - y))/y)/y, [d, 10*d, 1e-4, 1e-2, 1])   # = 12 int dy/y int_{1-d}^1 dx/(1-x ybar) (x ~ 1)
check('the excluded corner x > 1-delta contributes 12 int ln(1+delta ybar/y) dy/y -> 12 * pi^2/12 = pi^2 (up to O(delta ln delta))', abs(corner - mp.pi**2) < 20*d*mp.log(1/d), mp.nstr(corner, 12))
# symmetry: r2-term with the same double cutoff equals the r1-term  ->  A_3^i shifts by -pi^2 pi a_s (r1 - r2)
d = mp.mpf('1e-4')
v1 = A3i_r1_double(d); v2 = A3i_r2_double(d)
check('double cutoff is symmetric under (x,y) -> (ybar, xbar): r2-term = r1-term, so A_3^i -> pi a_s (r1-r2) I_dbl', abs(v1 - v2) < 1e-6*abs(v1), '%s vs %s' % (mp.nstr(v1, 14), mp.nstr(v2, 14)))
# the project's -21.6 is a non-converged scipy dblquad (reproduce the setting)
try:
    import numpy as np
    import scipy.integrate as si
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        delta = 1e-6
        dblq = 12*si.dblquad(lambda y, x: x*(1 - y)/(y*(1 - x*(1 - y))), 0, 1 - delta, lambda x: delta, lambda x: 1.0, epsabs=1e-10, epsrel=1e-10)[0]
    Xf = np.log(1/delta)
    print('      scipy dblquad (project setting) gives shift %.3f  (spurious; mpmath/analytic: %.4f)' % (dblq - 6*(Xf**2 - 2*Xf + np.pi**2/3), -np.pi**2))
except Exception as ex:
    print('scipy not available', ex)
print('\nSUMMARY n22: %d/%d PASS' % (sum(RES), len(RES)))
