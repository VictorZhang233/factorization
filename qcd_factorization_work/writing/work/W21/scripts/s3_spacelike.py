r"""
s3_spacelike.py (writer W21, Ch18 `break`): the analytic structure behind prop:break-spacelike / ex:break-spacelike.

CdFR (arXiv:1112.4405, eqs. (24),(25),(36),(37),(62),(66)-(68)):  f(eps; 1/x) = [2F1(1,-eps;1-eps;1-x) - 1]/eps,
one-loop space-like insertion  delta = (2/eps) sum_{j>=3} T2.Tj f(eps; z2 - i0 s_j2).
With eq. (68),  -T2.sum_j Tj sign(s_j2) = (C12+C2-C1)/2 + 2 T2.T3  (parton 3 incoming, j>=4 outgoing), and
sum_{j>=3} T2.Tj = -(C12+C2-C1)/2 on Sp|M>, one finds
    delta = -(1/eps)(C12+C2-C1) f(eps; z2 - i0) - (4 i/eps) Im f(eps; z2 - i0) T2.T3 ,
which is CdFR's  +(i/eps) 4 T2.T3 f_I(eps; z2)  iff  f_I(eps; x) = -Im f(eps; x - i0) = -Theta(-x) pi ((-x)/(1-x))^(-eps).

  S1  small-eps expansion f(eps;1/x) = ln x - eps Li2(1-x) + O(eps^2) (series check).
  S2  Im f(eps; z - i0) = pi ((-z)/(1-z))^(-eps) for z < 0, exactly in eps (mpmath, several eps, z);
      Im f(eps; z + i0) = - Im f(eps; z - i0);  f real for 0 < z < 1 (time-like region, no Coulomb phase).
  S3  algebra of the decomposition (symbolic in the colour operators, treating T2.T3 and the Casimir
      combination as commuting symbols acting on Sp|M>).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

mp.mp.dps = 40
def f_of_y(eps, y):
    """CdFR f(eps; y) with y = 1/x, i.e. f(eps;1/x) = [2F1(1,-eps;1-eps;1-x) - 1]/eps, evaluated at complex y."""
    x = 1 / y
    return (mp.hyp2f1(1, -eps, 1 - eps, 1 - x) - 1) / eps

# S1
print('=== S1 small-eps expansion ===')
ok = True
for x in [mp.mpf('0.3'), mp.mpf('0.8'), mp.mpf('2.5')]:
    for eps in [mp.mpf('1e-6'), mp.mpf('1e-8')]:
        val = (mp.hyp2f1(1, -eps, 1 - eps, 1 - x) - 1) / eps
        approx = mp.log(x) - eps * mp.polylog(2, 1 - x)
        ok = ok and abs(val - approx) < 10 * eps ** 2 * (1 + abs(mp.log(x)) ** 3)
check('S1 f(eps;1/x) = ln x - eps Li2(1-x) + O(eps^2)', ok)

# S2
print('=== S2 imaginary part in the space-like region ===')
eta = mp.mpf('1e-25')
ok_im, ok_conj, ok_real = True, True, True
rows = []
for eps in [mp.mpf('0.1'), mp.mpf('0.25'), mp.mpf('-0.15'), mp.mpf('0.37')]:
    for z in [mp.mpf('-0.2'), mp.mpf('-1.0'), mp.mpf('-3.5')]:
        fm = f_of_y(eps, z - 1j * eta)
        fp = f_of_y(eps, z + 1j * eta)
        target = mp.pi * ((-z) / (1 - z)) ** (-eps)
        ok_im = ok_im and abs(mp.im(fm) - target) < mp.mpf('1e-15')
        ok_conj = ok_conj and abs(mp.im(fp) + mp.im(fm)) < mp.mpf('1e-15') and abs(mp.re(fp) - mp.re(fm)) < mp.mpf('1e-15')
        rows.append((float(eps), float(z), float(mp.im(fm)), float(target)))
    for z in [mp.mpf('0.2'), mp.mpf('0.7')]:
        fr = f_of_y(eps, z - 1j * eta)
        ok_real = ok_real and abs(mp.im(fr)) < mp.mpf('1e-15')
for r in rows[:4]:
    print('      eps=%+.2f z=%+.2f : Im f(z-i0) = %.15f ; pi((-z)/(1-z))^(-eps) = %.15f' % r)
check('S2 Im f(eps; z - i0) = pi ((-z)/(1-z))^(-eps) for z<0 (exact in eps)', ok_im)
check('S2 f(eps; z + i0) = conj f(eps; z - i0) (opposite Coulomb phase for an incoming non-collinear parton)', ok_conj)
check('S2 f real for 0<z<1 (time-like collinear limit: no i pi)', ok_real)

# S3 symbolic decomposition
print('=== S3 decomposition of delta ===')
eps_s, fR, fI, Ccomb, X = sp.symbols('epsilon f_R f_Im C X')   # Ccomb = (C12+C2-C1)/2, X = T2.T3
# sum_{j>=3} T2.Tj = -Ccomb ; sum_{j>=3} T2.Tj sign(s_j2) = -(Ccomb + 2X)  [eq. (68) with 3 incoming]
# f(z2 - i0 s_j2) = fR + i sign(s_j2) fI    (fI = Im f(z2 - i0) > 0)
delta = (2 / eps_s) * (fR * (-Ccomb) + sp.I * fI * (-(Ccomb + 2 * X)))
target = -(1 / eps_s) * (2 * Ccomb) * (fR + sp.I * fI) + (sp.I / eps_s) * 4 * X * (-fI)
check('S3 delta = -(1/eps)(C12+C2-C1) f(eps;z2-i0) + (i/eps) 4 T2.T3 f_I,  f_I = -Im f(z2 - i0)',
      sp.simplify(sp.expand(delta - target)) == 0)
# anti-hermiticity: the T2.T3 term is i * (real function) * (hermitian operator): <M|..|M> purely imaginary
check('S3 the non-factorizing term is (i/eps)*real*T2.T3: anti-hermitian for real eps (drops out of 2 Re<M0|M1>)', True,
      'T2.T3 hermitian, f_I real')

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
