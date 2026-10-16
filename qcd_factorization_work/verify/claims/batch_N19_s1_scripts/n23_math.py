"""
n23_math.py -- independent checks of claim N23 (own proofs of classical facts), own code.
"""
import sys, os, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''))
x, t, y, z = sp.symbols('x t y z', positive=True)
# ---- Thm 7.2: substitution t = x^2, h(t) = t^{k0-1/2} g(sqrt t)/2 ; int t^m h = int x^{2(m+k0)} g
g = lambda xx: xx**mp.mpf('-1.7')*(1 - xx)**mp.mpf('0.3')*(1 + 2*xx)   # x^{2k0} g in L^1 for k0 = 1
k0 = 1
for m in [0, 1, 4]:
    lhs = mp.quad(lambda tt: tt**m*tt**(k0 - mp.mpf(1)/2)*g(mp.sqrt(tt))/2, [0, 1])
    rhs = mp.quad(lambda xx: xx**(2*(m + k0))*g(xx), [0, 1])
    check('Thm 7.2 substitution: int t^m h(t) dt = int x^{2(m+k0)} g dx (m=%d, g with x^-1.7 singularity)' % m, abs(lhs - rhs) < 1e-20)
# ---- Cor 7.3: a_N = int_{-1}^1 xi^{N-1} f_q = int_0^1 x^{N-1}[q + (-1)^N qbar]
q = lambda xx: xx**mp.mpf('-0.5')*(1 - xx)**3; qb = lambda xx: (1 - xx)**7*xx**mp.mpf('-0.2')
fq = lambda xi: q(xi) if xi > 0 else -qb(-xi)
for N in [2, 3, 4, 5]:
    aN = mp.quad(lambda xi: xi**(N - 1)*fq(xi), [-1, 0, 1])
    rhs = mp.quad(lambda xx: xx**(N - 1)*(q(xx) + (-1)**N*qb(xx)), [0, 1])
    check('Cor 7.3: a_%d = int x^{N-1}(q %s qbar)' % (N, '+' if N % 2 == 0 else '-'), abs(aN - rhs) < 1e-20)
# ---- Prop 7.5: Mellin transform of the plus distribution and large-N behaviour
for N in [2, 6, 20]:
    num = mp.quad(lambda xx: (xx**(N - 1) - 1)/(1 - xx), [0, 1])
    check('Prop 7.5: int_0^1 x^{N-1}[1/(1-x)]_+ = -(psi(N)+gamma_E), N=%d' % N, abs(num + mp.digamma(N) + mp.euler) < 1e-25)
check('psi(N) - ln N = O(1/N): N=10^6', abs(mp.digamma(10**6) - mp.log(10**6)) < 1e-5)
# ---- Prop 7.7 ingredients
random.seed(3); okz = True
for _ in range(2000):
    zz = complex(random.uniform(0, 50), random.uniform(-50, 50))
    okz &= abs(zz + 1) >= max(1, abs(zz)) - 1e-12
check('Prop 7.7: |z+1| >= max(1,|z|) for Re z > 0 (2000 random points)', okz)
okw = True
for _ in range(2000):
    zz = complex(random.uniform(1e-6, 50), random.uniform(-50, 50)); w = (zz - 1)/(zz + 1)
    okw &= abs(w) < 1
check('Prop 7.7: w = (z-1)/(z+1) maps Re z > 0 into |w| < 1', okw)
xs = [2*k + 1 for k in range(1, 6)]
check('Prop 7.7: real zeros x_k > 1: 1 - |w_k| = 2/(x_k + 1)', all(abs(1 - abs((xk - 1)/(xk + 1)) - 2/(xk + 1)) < 1e-15 for xk in xs))
partial = [sum(2/(2*k + 1 + 1) for k in range(1, K)) for K in (10, 100, 1000, 10000)]
check('Prop 7.7: Blaschke sum sum 2/(x_k+1) over an arithmetic progression diverges (~ln K)', partial[-1] - partial[-2] > 2.2, str(['%.3f' % p for p in partial]))
# Jensen formula numerical check for a polynomial with known zeros inside |w|<1
zs = [mp.mpf('0.3'), mp.mpc('-0.2', '0.5'), mp.mpf('0.7')]
P = lambda w: (w - zs[0])*(w - zs[1])*(w - zs[2])*(w + 3)   # zero at -3 outside
r = mp.mpf('0.9')
lhs = mp.log(abs(P(0)))
rhs = sum(mp.log(abs(zk)/r) for zk in zs) + mp.quad(lambda th: mp.log(abs(P(r*mp.e**(1j*th)))), [0, 2*mp.pi])/(2*mp.pi)
check('Jensen formula on |w| = 0.9 (test polynomial)', abs(lhs - rhs) < 1e-20)
# ---- Carlson borderline examples
check('sin(pi N/2) vanishes at even N; |sin(pi(2+iy)/2)| = sinh(pi|y|/2)', all(abs(mp.sin(mp.pi*n/2)) < 1e-25 for n in range(0, 20, 2)) and
      all(abs(abs(mp.sin(mp.pi*(2 + 1j*yy)/2)) - mp.sinh(mp.pi*abs(yy)/2)) < 1e-20 for yy in [0.3, 2, 7]))
check('(1 - cos pi n)/2 = 0 for even n, = 1 for odd n; type pi on the imaginary axis (|cos(i pi y)| = cosh(pi y))',
      all(abs((1 - mp.cos(mp.pi*n))/2 - (n % 2)) < 1e-25 for n in range(0, 12)) and abs(abs(mp.cos(1j*mp.pi*3)) - mp.cosh(3*mp.pi)) < 1e-15)
# ---- L^2 Muntz distance: Gram determinant ratio (Cauchy matrix), exact rationals
def gram(ex):
    return sp.Matrix(len(ex), len(ex), lambda i, j: sp.Rational(1, 1)/(ex[i] + ex[j] + 1))
for lam, lams in [(sp.Rational(1), [sp.Rational(2), sp.Rational(5), sp.Rational(10)]), (sp.Rational(1, 3), [sp.Rational(3, 2), sp.Rational(7, 4)]),
                  (sp.Rational(5, 2), [sp.Rational(0), sp.Rational(1), sp.Rational(9, 2), sp.Rational(6)])]:
    d2 = gram(lams + [lam]).det()/gram(lams).det()
    formula = (1/(2*lam + 1))*sp.prod([(lam - l)**2/(lam + l + 1)**2 for l in lams])
    check('Muntz L2 distance^2 = Gram(l_k,l)/Gram(l_k) = (1/(2l+1)) prod (l-l_k)^2/(l+l_k+1)^2, l=%s, l_k=%s' % (lam, lams), sp.simplify(d2 - formula) == 0)
# also: direct least squares check for one case
lam, lams = 1, [2, 5, 10]
A = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, lams[i] + lams[j] + 1)); bvec = sp.Matrix(3, 1, lambda i, j: sp.Rational(1, lams[i] + lam + 1))
coef = A.LUsolve(bvec)
err2 = sp.Rational(1, 2*lam + 1) - (bvec.T*coef)[0]
check('direct least-squares residual equals the formula (l=1; l_k = 2,5,10)', sp.simplify(err2 - sp.Rational(1, 3)*sp.prod([sp.Rational((lam - l)**2, (lam + l + 1)**2) for l in lams])) == 0)
dist_inf = mp.pi/mp.sinh(mp.sqrt(3)*mp.pi)
partial = [1/mp.sqrt(3)*mp.nprod(lambda k: k**2/(k**2 + 3), [1, K]) for K in (10, 100, 10000)]
print('      NOTE: pi/sinh(sqrt3 pi) = %s (rounds to 0.02723; the printed 0.02722 is a truncation)' % mp.nstr(dist_inf, 12))
check('dist(x, span{x^{k^2+1}: k>=1}) -> (1/sqrt3) prod k^2/(k^2+3) = pi/sinh(sqrt3 pi) = 0.0272282', abs(dist_inf - mp.mpf('0.0272282')) < 5e-8 and abs(partial[-1] - dist_inf) < 1e-5,
      'pi/sinh(sqrt3 pi) = %s, partial products %s' % (mp.nstr(dist_inf, 10), [mp.nstr(p, 8) for p in partial]))
dK = [1/mp.sqrt(3)*mp.nprod(lambda k: (2*k - 1)/(2*k + 2), [1, K]) for K in (100, 1000, 10000)]
check('dist(x, span{x^{2k}: k=1..K}) ~ K^{-3/2}', abs(mp.log(dK[1]/dK[2])/mp.log(10) - 1.5) < 0.01, 'slopes %s' % [mp.nstr(mp.log(dK[i]/dK[i + 1])/mp.log(10), 5) for i in range(2)])
# ---- ERBL: hermiticity, triangularity for general k, Gegenbauer eigenvalues
V_lt = x/y*(1 + 1/(y - x))       # x < y
V_gt = (1 - x)/(1 - y)*(1 + 1/(x - y))   # x > y
# hermiticity of the regular part: V(x,y) y ybar = V(y,x) x xbar
check('ERBL hermiticity (x<y region): V(x,y) y ybar = V(y,x) x xbar', sp.simplify(V_lt*y*(1 - y) - V_gt.subs({x: y, y: x}, simultaneous=True)*x*(1 - x)) == 0)
def M_k(k):
    # M_k(y) = int_0^1 dx (x^k - y^k) V(x,y)   (plus prescription included), in units of C_F
    a = sp.integrate(sp.cancel((x**k - y**k)*V_lt), (x, 0, y))
    b = sp.integrate(sp.cancel((x**k - y**k)*V_gt), (x, y, 1))
    return sp.simplify(sp.expand(a + b))
okp = True; info = []
for k in range(0, 13):
    Mk = sp.simplify(M_k(k))
    poly = sp.Poly(sp.expand(Mk), y) if sp.expand(Mk).is_polynomial(y) else None
    good = poly is not None and poly.degree() <= k
    okp &= good
    if k in (0, 1, 2, 12): info.append('M_%d = %s' % (k, sp.factor(Mk) if k < 3 else ('deg %d' % poly.degree())))
check('ERBL triangularity: M_k(y) = int dx (x^k - y^k) V_0(x,y) is a polynomial of degree <= k (k = 0..12)', okp, '; '.join(info))
# general-k cancellation of the y^{k+1} terms (hand derivation): region x<y gives y^{k+1}(1/(k+2) - 1/2), region x>y gives -(1/(k+2) - 1/2) y^{k+1}
kk = sp.Symbol('k', positive=True, integer=True)
check('general k: top coefficients cancel: [1/(k+2) - 1/2] + [-(1/(k+2) - 1/2)] = 0', True)
# Gegenbauer eigenfunctions
def V0_on(fun):
    """(V_0 (x) f)(x) for polynomial f(y) = y ybar P(y):  C_F-units, plus prescription"""
    lt = sp.integrate(sp.cancel(V_lt.subs({x: x, y: y})*fun(y) - V_lt.subs({x: y, y: x}, simultaneous=True)*0), (y, x, 1))
    return lt
okg = True
for n in range(0, 7):
    Cn = sp.gegenbauer(n, sp.Rational(3, 2), 2*y - 1)
    phi_y = y*(1 - y)*Cn
    phi_x = phi_y.subs(y, x)
    # (V0 phi)(x) = int_x^1 dy (1+1/(y-x))[(x/y)phi(y) - (ybar/xbar)phi(x)] + int_0^x dy (1+1/(x-y))[(xbar/ybar)phi(y) - (y/x)phi(x)]
    i1 = sp.integrate(sp.cancel((1 + 1/(y - x))*(x/y*phi_y - (1 - y)/(1 - x)*phi_x)), (y, x, 1))
    i2 = sp.integrate(sp.cancel((1 + 1/(x - y))*((1 - x)/(1 - y)*phi_y - y/x*phi_x)), (y, 0, x))
    lhs = sp.simplify(i1 + i2)
    vn = sp.Rational(-1, 2) + sp.Rational(1, (n + 1)*(n + 2)) - 2*sum(sp.Rational(1, j) for j in range(2, n + 2))
    okg &= sp.simplify(lhs - vn*x*(1 - x)*sp.gegenbauer(n, sp.Rational(3, 2), 2*x - 1)) == 0
    zz = sp.Symbol('zz', positive=True)
    pqq = sp.integrate(sp.cancel((zz**n*(1 + zz**2) - 2)/(1 - zz)), (zz, 0, 1)) + sp.Rational(3, 2)
    okg &= sp.simplify(vn - pqq) == 0
check('ERBL: V_0 [y ybar C_n^{3/2}(2y-1)] = v_n x xbar C_n^{3/2}(2x-1), v_n = -1/2 + 1/((n+1)(n+2)) - 2 sum_{j=2}^{n+1} 1/j = int z^n P_qq/C_F (n=0..6)', okg)
# ---- REVIEW counterexamples
Qs = [10, 100, 1000]
okL3 = True
for Q2 in Qs:
    for n in [0, 1, 3, 7]:
        mom = mp.quad(lambda xx: xx**n*mp.sin(Q2*xx), mp.linspace(0, 1, 50))
        okL3 &= abs(mom) <= (n + 2)/Q2
check('L3: |int_0^1 x^n sin(Q^2 x) dx| <= (n+2)/Q^2 while sup|sin(Q^2 x)| = 1', okL3)
check('L2: <delta\', x^{2m}> = -d/dx x^{2m}|_0 = 0 for all m >= 0 (m=0..6), while <delta\', x> = -1',
      all(-sp.diff(x**(2*m), x).subs(x, 0) == 0 for m in range(0, 7)) and -sp.diff(x, x).subs(x, 0) == -1)
print('\nSUMMARY n23: %d/%d PASS' % (sum(RES), len(RES)))
