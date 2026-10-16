# E07(i) stage-2 check: target-mass correction (TMC) of quasi-PDFs.
# Independent of stage 1: exact symbolic moments (sympy) + quadrature with a different test PDF.
# Alexandrou et al. PRD 92 014502 (arXiv:1504.07455v3) eq. (4): a~_n = K_n a~_n^(0), K_n = sum_j C(n-j,j) mu^j,
#   eq. (11): q~(x) = q~0(xi)/(1+mu xi^2), xi = 2x/(1+sqrt(1+4 mu x^2)).
# Chen et al. NPB 911 (2016) 246 (arXiv:1603.06664) App. B eq. (61):
#   q~(x) = [ (f+/2) q(2x/f+) - (f-/2) q(-2x/f-) ] / sqrt(1+4c), f+- = sqrt(1+4c) +- 1.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

mu, x, xi, c, t = sp.symbols('mu x xi c t', positive=True)

def K(n, cc):
    return sum(sp.binomial(n - j, j) * cc**j for j in range(0, n // 2 + 1))

# --- 1. Alexandrou eq. (11): change of variables x -> xi
xi_of_x = 2*x/(1 + sp.sqrt(1 + 4*mu*x**2))
x_of_xi = xi/(1 - mu*xi**2)
# check the inverse map
chk = sp.simplify(xi_of_x.subs(x, x_of_xi) - xi)
print('inverse map check (should be 0):', sp.simplify(chk.subs(mu, sp.Rational(1, 7)).subs(xi, sp.Rational(1, 3))))
jac = sp.simplify(sp.diff(x_of_xi, xi))
print('dx/dxi =', sp.factor(jac))
# n-th moment of Alexandrou's q~ in terms of q~0: int dx x^(n-1) q~0(xi)/(1+mu xi^2) = int dxi W_n(xi) q~0(xi)
for n in range(1, 5):
    W = sp.simplify(x_of_xi**(n - 1) * jac/(1 + mu*xi**2))
    print(f'n={n}: weight W_n(xi) = {sp.factor(W)} ;  exact TMC requires W_n = K_n xi^(n-1) with K_n = {sp.expand(K(n-1+0, mu)) if False else sp.expand(K(n, mu))}')
# series of W_1 in mu: shows the n=1 (particle number) moment is NOT conserved
W1 = sp.simplify(jac/(1 + mu*xi**2))
print('W_1 series:', sp.series(W1, mu, 0, 3))

# --- 2. Chen eq. (61): exact moments (Lucas-sequence identity)
fp = sp.sqrt(1 + 4*c) + 1
fm = sp.sqrt(1 + 4*c) - 1
for n in range(1, 9):
    mom_factor = ((fp/2)**(n + 1) - (-fm/2)**(n + 1))/sp.sqrt(1 + 4*c)
    diff = sp.simplify(sp.expand(mom_factor) - K(n, c))
    print(f'Chen eq.(61) n={n}: moment factor - K_n = {diff}')

# --- 3. Numerical illustration with a test valence-like PDF q(x) = N x^(-0.3) (1-x)^3.5 on [0,1]
mp.mp.dps = 30
a_, b_ = mp.mpf('-0.3'), mp.mpf('3.5')
qn = lambda y: (y**a_ * (1 - y)**b_) if 0 < y < 1 else mp.mpf(0)
norm = mp.quad(qn, [0, 1])
q = lambda y: qn(y)/norm
def mom(f, n, lo, hi, pts=None):
    return mp.quad(lambda y: y**(n - 1) * f(y), [lo] + (pts or []) + [hi])
for cval in [mp.mpf('0.05'), mp.mpf('0.25')]:
    # Alexandrou: q~(x) = q0(xi(x))/(1+mu xi^2); support x in [0, 1/(1-mu)]
    def qA(xx, cval=cval):
        xx = mp.mpf(xx)
        xiv = 2*xx/(1 + mp.sqrt(1 + 4*cval*xx**2))
        return q(xiv)/(1 + cval*xiv**2)
    xmax = 1/(1 - cval)
    sp_ = mp.sqrt(1 + 4*cval); fpv = sp_ + 1; fmv = sp_ - 1
    def qC(xx, fpv=fpv, fmv=fmv, sp_=sp_):
        return ((fpv/2)*q(2*xx/fpv) - (fmv/2)*q(-2*xx/fmv))/sp_
    print(f'--- c = mu = {cval}')
    for n in range(1, 5):
        exact = K(n, sp.Rational(str(cval))) * mom(q, n, 0, 1)
        mA = mom(qA, n, 0, xmax)
        mC = mom(qC, n, -fmv/2, fpv/2, [0])
        print(f'  n={n}: K_n<x^(n-1)>_q = {mp.nstr(mp.mpf(sp.N(exact, 30)), 12)}, Alexandrou(11) = {mp.nstr(mA, 12)} (rel. dev {mp.nstr(mA/mp.mpf(sp.N(exact,30)) - 1, 4)}), Chen(61) = {mp.nstr(mC, 12)}')
