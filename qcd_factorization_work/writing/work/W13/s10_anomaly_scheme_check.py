"""W13 / s10: cross-checks of the one-loop photon-gluon box (prop:coll-anomaly-scheme) against the literature, and an
analytic proof that the first moment of the massive box vanishes for every quark mass.

Units: hat g1 for gamma* + g(helicity +) -> q qbar of one flavour, in units (alpha_s e_q^2/(2 pi)) T_F (as in s5, s5c).
Ours (s5, s5c):
  MSbar (HVBM):   DeltaC_g(x)/T_F = (2x-1)(ln((1-x)/x) - 1) + 2(1-x)
  off-shell:      hat g1 = (2x-1) ln(Q^2/P^2) + B_off(x),  B_off = (2x-1)(-2 ln x - 2)       (leading power)
  massive quarks: hat g1 = (2x-1) ln((1+b)/(1-b)) + b(3-4x),  b = sqrt(1 - 4 m^2 x/(Q^2 (1-x)))
Literature: Ball, Forte, Ridolfi, PLB 378 (1996) 255 [hep-ph/9510449], eqs. (16)-(18), Mellin moments
  C_g^MSbar(N) = -T_F (N-1)/(N(N+1)) [S1(N) + (N-1)/N]
  C_g^OS(N)    = -2 T_F (N^3 - N^2 + N + 1)/(N^2 (N+1)^2)           (incoming gluon off shell)
  C_g^AR(N)    = -T_F (N^2 + 1 + N(N-1) S1(N))/(N^2 (N+1))           (massive quarks, Altarelli-Ross scheme)
(normalization: first moments 0, -T_F, -T_F; their eq. (7) C_g(1) = -alpha_s/(4 pi) for T_F = 1/2.)
Checks:
 (a) Mellin moments of our MSbar DeltaC_g = BFR (16), N = 1..8 (exact rationals/zeta-free, sympy);
 (b) Mellin moments of B_off = BFR (17) (OS scheme coefficient = finite part of the off-shell box), N = 1..8;
 (c) massive box at leading power = MSbar coefficient + (2x-1) ln(Q^2/m^2): the implied AR-scheme quark-in-gluon
     density, B_m(N) - C_g^AR(N)/T_F, and its first moment;
 (d) analytic first moment of the exact massive box: int_0^{x_max} hat g1 dx = 0 for all m (change of variable x -> b).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

x = sp.Symbol('x', positive=True)
N = sp.Symbol('N', positive=True, integer=True)
S1 = lambda n: sum(sp.Rational(1, k) for k in range(1, n + 1))

DCg = (2*x - 1)*(sp.log(1 - x) - sp.log(x) - 1) + 2*(1 - x)
Boff = (2*x - 1)*(-2*sp.log(x) - 2)
Bm0 = (2*x - 1)*(sp.log(1 - x) - sp.log(x)) + 3 - 4*x          # massive box at m->0 minus (2x-1) ln(Q^2/m^2)

def mellin(f, n):
    return sp.nsimplify(sp.integrate(sp.expand(x**(n - 1)*f), (x, 0, 1)))

ok_a = True; ok_b = True
for n in range(1, 9):
    a = sp.simplify(mellin(DCg, n) - (-sp.Rational(n - 1, n*(n + 1))*(S1(n) + sp.Rational(n - 1, n))))
    b = sp.simplify(mellin(Boff, n) - (-2*sp.Rational(n**3 - n**2 + n + 1, n**2*(n + 1)**2)))
    ok_a &= (a == 0); ok_b &= (b == 0)
check('(a) Mellin moments N=1..8 of our MSbar DeltaC_g equal BFR (16): -(N-1)/(N(N+1)) [S1(N)+(N-1)/N]  (units T_F)', ok_a)
check('(b) Mellin moments N=1..8 of the off-shell finite part B_off equal BFR (17) (OS scheme)', ok_b)
print('   first moments: MSbar', mellin(DCg, 1), ' OS', mellin(Boff, 1), ' massive(m->0 finite part)', mellin(Bm0, 1))

# (c) implied AR-scheme quark-in-gluon density: d_AR(N) = B_m0(N) - C_AR(N)
dAR = []
for n in range(1, 9):
    cAR = -sp.Rational(n**2 + 1, n**2*(n + 1)) - sp.Rational(n*(n - 1), n**2*(n + 1))*S1(n)
    dAR.append(sp.simplify(mellin(Bm0, n) - cAR))
print('   implied AR quark-in-gluon density moments (units T_F alpha_s/2pi), N=1..8:', dAR)
# guess: 2(1-x) ?
ok_c = all(sp.simplify(dAR[n - 1] - mellin(2*(1 - x), n)) == 0 for n in range(1, 9))
check('(c) massive box = C_g^AR + [2(1-x) + (2x-1) ln(Q^2/m^2)]: the AR scheme moves the soft term 2(1-x) (first moment +1) '
      'from the coefficient into the quark density', ok_c)
check('(c) first moments: C_g^AR(1) = -1 (units T_F), soft density +1, full massive box 0',
      sp.simplify(dAR[0] - 1) == 0 and sp.simplify(mellin(Bm0, 1)) == 0)

# (d) exact first moment of the massive box, analytically, rho = 4 m^2/Q^2
rho, b = sp.symbols('rho b', positive=True)
# b^2 = 1 - rho x/(1-x)  <=>  x = (1-b^2)/(1-b^2+rho);  x: 0 -> 1/(1+rho)  <=>  b: 1 -> 0
xb = (1 - b**2)/(1 - b**2 + rho)
dxdb = sp.simplify(sp.diff(xb, b))
integrand_b = sp.simplify(((2*xb - 1)*sp.log((1 + b)/(1 - b)) + b*(3 - 4*xb))*dxdb)
# int_{x=0}^{xmax} = int_{b=1}^{0} (...) db = -int_0^1 (...) db
I1 = -sp.integrate(sp.expand(sp.simplify(integrand_b)), (b, 0, 1))
I1s = sp.simplify(I1)
print('   analytic first moment (sympy):', I1s)
okd = True
for rv in (sp.Rational(1, 10), sp.Rational(1, 3), sp.Rational(2, 1), sp.Rational(7, 100)):
    val = complex(sp.N(I1s.subs(rho, rv), 30)) if I1s != 0 else 0
    okd &= abs(val) < 1e-25
check('(d) int_0^{x_max} [(2x-1) ln((1+b)/(1-b)) + b(3-4x)] dx = 0 identically in m (analytic, x -> b substitution)', okd)

# numerical cross-check of (d) without the substitution
def fm(rv):
    rv = mp.mpf(rv); xmax = 1/(1 + rv)
    f = lambda xx: (2*xx - 1)*mp.log((1 + mp.sqrt(1 - rv*xx/(1 - xx)))/(1 - mp.sqrt(1 - rv*xx/(1 - xx)))) \
        + mp.sqrt(1 - rv*xx/(1 - xx))*(3 - 4*xx)
    return mp.quad(f, [0, xmax/2, xmax])
check('(d) numerical: first moment of the massive box ~ 0 for rho = 0.04, 1, 9',
      all(abs(fm(r)) < 1e-25 for r in ('0.04', '1', '9')))
print('\nSUMMARY s10: %d PASS, %d FAIL' % (npass, nfail))
