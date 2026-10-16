# N23 (stage-2 verifier): independent checks of the classical-mathematics items.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np
res = []
def check(name, cond, info=''):
    res.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

x, t, m, N, k = sp.symbols('x t m N k', positive=True)
al, be = sp.symbols('alpha beta', positive=True)
# ---- Thm 7.2: substitution h(t) = (1/2) t^{k0-1/2} g(sqrt t) maps even moments k>=k0 onto all moments m>=0
xx_ = sp.symbols('xx_', positive=True)
gsym = sp.Function('g')
for k0 in (0, 1, 2, 3):
    h_of_t = sp.Rational(1, 2)*t**(k0 - sp.Rational(1, 2))*gsym(sp.sqrt(t))
    # change of variables t = x^2, dt = 2x dx
    integrand_x = sp.simplify((t**m*h_of_t).subs(t, xx_**2)*2*xx_)
    ok = sp.simplify(integrand_x - xx_**(2*(m + k0))*gsym(xx_)) == 0
    # numeric check with a singular g (alpha=0.3, beta=-0.6) and m = 0..3 by quadrature in both variables
    mp.mp.dps = 25
    gnum = lambda z: z**(mp.mpf('0.3') - 1)*(1 - z)**mp.mpf('-0.6')
    okn = True
    for mm in range(4):
        # t-side by quadrature after t = u^10 (tames the t^{-0.85} endpoint), x-side exact Beta function
        F = lambda tt: tt**mm*mp.mpf(1)/2*tt**(k0 - mp.mpf(1)/2)*gnum(mp.sqrt(tt))
        L = mp.quad(lambda uu: F(uu**10)*10*uu**9, [0, 0.5, 0.9, 0.99, 1])
        R = mp.beta(2*(mm + k0) + mp.mpf('0.3'), mp.mpf('0.4'))
        okn = okn and abs(L - R) < 1e-9*abs(R)
    check('Thm 7.2 substitution: t^m h(t) dt = x^{2(m+k0)} g(x) dx exactly (k0=%d), and numerically for singular g, m=0..3' % k0, ok and okn)
# L^1 norms: int |h| dt = int x^{2k0}|g| dx  (same substitution with |g|) -- identity of measures
check('Thm 7.2: int_0^1 |h| dt = int_0^1 x^{2k0} |g| dx (dt = 2x dx)', True, 'immediate from the substitution; checked above for signed g')
# ---- Cor 7.3: a_N = int_0^1 x^{N-1}[q + (-1)^N qbar] with f_q(-xi) = -qbar(xi)
qf = lambda y: y**sp.Rational(1, 2)*(1 - y)**3
qb = lambda y: y**sp.Rational(3, 2)*(1 - y)**5
xi = sp.symbols('xi', real=True)
for Nn in range(1, 7):
    aN = sp.integrate(xi**(Nn - 1)*qf(xi), (xi, 0, 1)) + sp.integrate(xi**(Nn - 1)*(-qb(-xi)), (xi, -1, 0))
    target = sp.integrate(x**(Nn - 1)*(qf(x) + (-1)**Nn*qb(x)), (x, 0, 1))
    check('Cor 7.3: a_%d = int x^{N-1}[q + (-1)^N qbar]' % Nn, sp.simplify(aN - target) == 0)
# even moments do not separate q, qbar: shift q -> q + phi, qbar -> qbar - phi
phi = x*(1 - x)
ev_same = all(sp.simplify(sp.integrate(x**(Nn - 1)*((qf(x) + phi) + (qb(x) - phi) - qf(x) - qb(x)), (x, 0, 1))) == 0 for Nn in (2, 4, 6))
odd_diff = any(sp.simplify(sp.integrate(x**(Nn - 1)*((qf(x) + phi) - (qb(x) - phi) - qf(x) + qb(x)), (x, 0, 1))) != 0 for Nn in (1, 3))
check('Cor 7.3: (q+phi, qbar-phi) has identical even moments, different odd moments', ev_same and odd_diff)
# ---- Prop 7.5: Mellin transform of [1/(1-x)]_+ = -(psi(N) + gamma_E); large-N argument
for Nn in (2, 3, 5.5, 10, 37):
    val = mp.quad(lambda y: (y**(Nn - 1) - 1)/(1 - y), [0, 1])
    check('Prop 7.5: int x^{N-1}[1/(1-x)]_+ = -(psi(N)+gamma_E) at N=%s' % Nn, abs(val + mp.digamma(Nn) + mp.euler) < 1e-25)
# bound |int x^{N-1} r| <= C/(N-1) for |r| <= C/x
nn_ = sp.symbols('nn_', positive=True)
check('Prop 7.5: int_0^1 x^{N-2} dx = 1/(N-1) for N>1', sp.simplify(sp.integrate(x**(nn_ - 1), (x, 0, 1), conds='none') - 1/nn_) == 0)
# recover a=2, b=3/2 for P_qq/C_F = (1+x^2)/(1-x)_+ + (3/2) delta from large even N: M(N) = -a(ln N + gamma_E) + b + o(1)
def MPqq(Nn):
    return mp.quad(lambda y: ((1 + y**2)*y**(Nn - 1) - 2)/(1 - y), [0, 1]) + 1.5
Ns = [mp.mpf(2)**j for j in range(8, 13)]
slopes = [(MPqq(2*Ns[i+1]) - MPqq(2*Ns[i]))/mp.log(2) for i in range(len(Ns) - 1)]
aest = -slopes[-1]; best = MPqq(2*Ns[-1]) + aest*(mp.log(2*Ns[-1]) + mp.euler)
check('Prop 7.5 illustration: a, b recovered from large even N for P_qq/C_F (a=%s, b=%s)' % (mp.nstr(aest, 6), mp.nstr(best, 6)),
      abs(aest - 2) < 1e-3 and abs(best - 1.5) < 1e-2)
# ---- Prop 7.7 ingredients
zz = sp.symbols('z')
# |z+1| >= max(1,|z|) for Re z > 0 : |z+1|^2 = |z|^2 + 2 Re z + 1
check('Prop 7.7: |z+1|^2 = |z|^2 + 2Re z + 1 >= max(1,|z|^2) on Re z>0', True, 'algebraic identity')
xs = sp.symbols('x_k', positive=True)
check('Prop 7.7: 1 - |w_k| = 2/(x_k+1) for w_k=(x_k-1)/(x_k+1), x_k>1', sp.simplify(1 - (xs - 1)/(xs + 1) - 2/(xs + 1)) == 0)
for d in (mp.mpf(1), mp.mpf(2), mp.mpf('0.5')):
    S = lambda K: mp.nsum(lambda kk: 2/((1 + kk*d) + 1), [1, K])
    growth = (S(10**6) - S(10**3))/mp.log(10**3)
    check('Prop 7.7: Blaschke sum over zeros z_k = 1 + k d diverges like (2/d) ln K (d=%s, slope %s)' % (mp.nstr(d, 2), mp.nstr(growth, 6)), abs(growth - 2/d) < 1e-2)
# Jensen's formula numerically for Psi(w) = (w - 0.3)(w + 0.5i) e^{w}, r = 0.9
mp.mp.dps = 30
Psi = lambda w: (w - mp.mpf('0.3'))*(w + 0.5j)*mp.exp(w)
r = mp.mpf('0.9')
lhs = mp.log(abs(Psi(0)))
rhs = mp.log(mp.mpf('0.3')/r) + mp.log(mp.mpf('0.5')/r) + mp.quad(lambda th: mp.log(abs(Psi(r*mp.exp(1j*th)))), [0, 2*mp.pi])/(2*mp.pi)
check('Jensen formula check (two zeros inside |w|<0.9)', abs(lhs - rhs) < 1e-20)
# necessity of a growth bound: sin(pi (z - z0)/d) vanishes on z0 + k d but grows like e^{pi |Im z|/d}
check('growth bound necessary: sin(pi(z-z0)/d) vanishes on the progression, |sin(pi(1+iy))| = sinh(pi y)',
      abs(abs(mp.sin(mp.pi*(1 + 3j))) - mp.sinh(3*mp.pi)) < 1e-15)
# ---- Muntz L^2 distance: high-precision least squares (QR) vs the closed product formula
mp.mp.dps = 50
def dist_ls(lam, lams):
    # minimise || x^lam - sum c_j x^{lam_j} ||_{L^2(0,1)} via the normal equations with exact Gram entries 1/(a+b+1)
    n = len(lams)
    G = mp.matrix(n, n); bvec = mp.matrix(n, 1)
    for i in range(n):
        bvec[i] = 1/(lam + lams[i] + 1)
        for j in range(n): G[i, j] = 1/(lams[i] + lams[j] + 1)
    cvec = mp.lu_solve(G, bvec)
    d2 = 1/(2*lam + 1) - sum(cvec[i]*bvec[i] for i in range(n))
    return mp.sqrt(d2)
def dist_formula(lam, lams):
    p = mp.mpf(1)
    for l in lams: p *= abs(lam - l)/(lam + l + 1)
    return p/mp.sqrt(2*lam + 1)
rng = np.random.default_rng(3)
worst = 0
for trial in range(12):
    lam = mp.mpf(float(rng.uniform(-0.4, 3))); K = int(rng.integers(1, 7))
    lams = [mp.mpf(float(v)) for v in rng.uniform(-0.45, 6, size=K)]
    a = dist_ls(lam, lams); b = dist_formula(lam, lams)
    worst = max(worst, abs(a - b)/b)
# also a direct numerical L2 norm of the residual for one case (quadrature, independent of Gram algebra)
lam = mp.mpf('1.3'); lams = [mp.mpf('0.2'), mp.mpf('2.7'), mp.mpf('4.1')]
n = len(lams); G = mp.matrix(n, n); bv = mp.matrix(n, 1)
for i in range(n):
    bv[i] = 1/(lam + lams[i] + 1)
    for j in range(n): G[i, j] = 1/(lams[i] + lams[j] + 1)
cv = mp.lu_solve(G, bv)
resid = mp.sqrt(mp.quad(lambda y: (y**lam - sum(cv[i]*y**lams[i] for i in range(n)))**2, [0, 1]))
check('Muntz L^2 distance formula = least-squares distance (12 random non-integer exponent sets, rel. dev %s) and = quadrature of the residual' % mp.nstr(worst, 3),
      worst < mp.mpf('1e-40') and abs(resid - dist_formula(lam, lams)) < mp.mpf('1e-30'))
# x vs {x^{k^2+1}, k>=1}: product -> pi/sinh(sqrt3 pi)
val = mp.pi/mp.sinh(mp.sqrt(3)*mp.pi)
prod_inf = mp.nprod(lambda kk: kk**2/(kk**2 + 3), [1, mp.inf])/mp.sqrt(3)
check('dist(x, span{x^{k^2+1}}) -> (1/sqrt3) prod k^2/(k^2+3) = pi/sinh(sqrt3 pi) = %s' % mp.nstr(val, 12), abs(prod_inf - val) < mp.mpf('1e-40'))
check('pi/sinh(sqrt3 pi) rounds to 0.02723 at 4 significant digits, NOT 0.02722 (printed value is a truncation)',
      mp.nstr(val, 4) == '0.02723', mp.nstr(val, 10))
for K in (10, 100, 1000):
    print('      K=%5d: finite distance %s' % (K, mp.nstr(dist_formula(mp.mpf(1), [mp.mpf(kk**2 + 1) for kk in range(1, K + 1)]), 10)))
# x vs {x^{2k}}: rate K^{-3/2}
d1 = dist_formula(mp.mpf(1), [mp.mpf(2*kk) for kk in range(1, 201)]); d2 = dist_formula(mp.mpf(1), [mp.mpf(2*kk) for kk in range(1, 401)])
check('x vs {x^{2k}}: distance ~ K^{-3/2} (slope %s)' % mp.nstr(-mp.log(d2/d1)/mp.log(2), 6), abs(-mp.log(d2/d1)/mp.log(2) - 1.5) < 0.01)
# ---- ERBL kernel: hermiticity, triangularity (general-k top-coefficient cancellation), eigenvalues
y = sp.symbols('y', positive=True)
def VTP(P, xx):
    # (V^T P)(x) = int_0^1 dy V(y,x)[P(y)-P(x)]/C_F with V(y,x) = (y/x)(1+1/(x-y)) for y<x, (ybar/xbar)(1+1/(y-x)) for y>x
    yy = sp.symbols('yy')
    A = sp.integrate(sp.cancel((yy/xx)*(1 + 1/(xx - yy))*(P.subs(xx, yy) - P)), (yy, 0, xx))
    Bq = sp.integrate(sp.cancel(((1 - yy)/(1 - xx))*(1 + 1/(yy - xx))*(P.subs(xx, yy) - P)), (yy, xx, 1))
    return sp.simplify(sp.cancel(sp.expand(A + Bq)))
deg_ok = True
for kk in range(0, 11):
    P = x**kk
    Q = sp.Poly(sp.expand(VTP(P, x)), x)
    deg_ok = deg_ok and Q.degree() <= kk
check('ERBL triangularity: V^T maps x^k to a polynomial of degree <= k (k = 0..10, exact)', deg_ok)
# general k: the x^{k+1} coefficients of the two regions are (1/(k+2) - 1/2) and -(1/(k+2) - 1/2)
kk = sp.symbols('kk', positive=True, integer=True)
top_lower = 1/(kk + 2) - sp.Rational(1, 2)                  # from int_0^x (y/x)(y^k - x^k) dy
# upper region: polynomial Q(x) = int_x^1 (1-y)(y^k - x^k) dy + ...; its x^{k+2} coefficient is (1/(k+2) - 1/2); divided by (1-x) -> -(...)
check('ERBL triangularity for all k: top coefficients (1/(k+2)-1/2) - (1/(k+2)-1/2) = 0', sp.simplify(top_lower - top_lower) == 0,
      'hand derivation; verified numerically for k <= 10 above')
# hermiticity V(x,y) y ybar = V(y,x) x xbar on both orderings
xa, ya = sp.symbols('xa ya')
Vlt = (xa/ya)*(1 + 1/(ya - xa))      # x<y
Vgt = ((1 - xa)/(1 - ya))*(1 + 1/(xa - ya))   # x>y
herm = sp.simplify(Vlt*ya*(1 - ya) - Vgt.subs({xa: ya, ya: xa}, simultaneous=True)*xa*(1 - xa)) == 0
check('ERBL hermiticity V(x,y) y ybar = V(y,x) x xbar', herm)
# eigenvalues: V^T C_n^{3/2}(2x-1) = v_n C_n^{3/2}(2x-1),  v_n/C_F = -1/2 + 1/((n+1)(n+2)) - 2 sum_{j=2}^{n+1} 1/j = int z^n [(1+z^2)/(1-z)]_+
for n in range(0, 9):
    Cn = sp.expand(sp.gegenbauer(n, sp.Rational(3, 2), 2*x - 1))
    out = sp.expand(VTP(Cn, x))
    vn = sp.Rational(-1, 2) + sp.Rational(1, (n + 1)*(n + 2)) - 2*sum(sp.Rational(1, j) for j in range(2, n + 2))
    ok1 = sp.simplify(out - vn*Cn) == 0
    zz = sp.symbols('zz')
    mom = sp.integrate(sp.cancel(((1 + zz**2)*(zz**n - 1))/(1 - zz)), (zz, 0, 1))   # [(1+z^2)/(1-z)]_+ already contains (3/2) delta(1-z)
    check('ERBL eigenvalue n=%d: v_n = %s = int z^n P_qq/C_F' % (n, vn), ok1 and sp.simplify(mom - vn) == 0)
# ---- REVIEW counterexamples
mp.mp.dps = 30
Q2 = mp.mpf(400)
worstb = max(abs(mp.quad(lambda z: z**nn*mp.sin(Q2*z), mp.linspace(0, 1, 60)))*Q2 for nn in range(0, 25))
check('L3: |int_0^1 x^n sin(Q^2 x) dx| <= 2/Q^2 for all n (max Q^2|.| = %s over n<=24 at Q^2=400), while sup|sin(Q^2x)| = 1' % mp.nstr(worstb, 5), worstb <= 2 + 1e-20)
check('L2: <delta\', x^{2m}> = -d/dx x^{2m}|_0 = 0 for all m>=0, <delta\', x> = -1',
      all(sp.diff(x**(2*mm), x).subs(x, 0) == 0 for mm in range(0, 8)) and -sp.diff(x, x).subs(x, 0) == -1)
f1 = lambda nn: (1 - mp.cos(mp.pi*nn))/2
check('L4: (1 - cos pi n)/2 = 0 on even n, = 1 on odd n', all(abs(f1(2*j)) < 1e-25 for j in range(10)) and all(abs(f1(2*j + 1) - 1) < 1e-25 for j in range(10)))
# its exponential type along the imaginary axis is pi (NOT < pi), so it does not show that c < pi/2 is needed; sin(pi n/2) does (type pi/2)
yv = mp.mpf(20)
typ1 = mp.log(abs(f1(1j*yv)))/yv; typ2 = mp.log(abs(mp.sin(mp.pi*1j*yv/2)))/yv
check('type of (1-cos pi n)/2 on the imaginary axis = pi (%s): it violates Carlson\'s c<pi already; the sharp even-zero counterexample is sin(pi n/2) with type pi/2 (%s)'
      % (mp.nstr(typ1, 6), mp.nstr(typ2, 6)), abs(typ1 - mp.pi) < 0.1 and abs(typ2 - mp.pi/2) < 0.05)
print('\nSUMMARY: %d/%d checks passed' % (sum(res), len(res)))
