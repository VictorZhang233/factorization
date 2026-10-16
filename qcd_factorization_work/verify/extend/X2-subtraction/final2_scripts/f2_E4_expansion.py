"""X2 final2 / f2_E4_expansion.py -- Prop E.4(d), Thm E.3(iv): EXACT (symbolic) Laurent expansion of the four
collinear-type singles at delta = 0 and comparison with Smirnov-Rakhmetov eq. (10), and of all nine singles -> LP.

Inputs (derived in f2_E4_singles.py / f2_E4_SRcompare.py; units Qt2 = 1, m2 = e^-L, so m2^(-k eps) = exp(k eps L)):
  HC1(e,0)  = G(e)G(1+e)G(1-e)G(-e)/G(1-2e) * [B(-2e,-e) - B(-e,-e)]/e * exp(e L)
  C1C1(e,0) = G(e)G(2e)/G(1+e) * G(1-e)^2 G(-e) G(1-2e) G(-2e)/(G(1-3e) G(1-4e)) * Ft(e) * exp(2 e L)
  Ft(e) = 3F2(1-2e,-3e,-2e; 1-3e,1-4e; 1) = 1 + 6 e^2 sum_{n>=1} t_n,
  t_n = n^-2 (1-2e/n)/(1-3e/n) prod_{k<n}(1-2e/k)^2 / prod_{k<=n}(1-4e/k) = n^-2 [1 + 5e/n + e^2 (23/n^2 + 4 H2_{n-1})] + O(e^3)
  => Ft = 1 + pi^2 e^2 + 30 zeta3 e^3 + (26/15) pi^4 e^4 + O(e^5)   (zeta(2,2) = (zeta2^2 - zeta4)/2 = pi^4/120).
Checks: (1) the expansion of t_n (sympy, exact in n); (2) the Taylor coefficients of Ft against a high-precision Cauchy
integral (numerical); (3) 2(HC1 + C1C1) e^(2 gamma e) expanded symbolically = SR eq. (10) (printed normalization:
SR omit exp(-gamma_E eps) per loop) EXACTLY, as polynomials in L; (4) the nine singles: SR (4) for HH (cited) + the exact
Gamma products SS, HS, 2 C1S (= SR (5)-(7)) + the four collinear-type ones from (3) -> LP + O(eps) exactly."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import functools
print = functools.partial(print, flush=True)
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

e, n, L, k = sp.symbols('epsilon n L k', positive=True)
G = sp.gamma
def B(a, b): return G(a)*G(b)/G(a + b)

print("(1) expansion of t_n (exact in n, through O(e^2))")
# log of the product part: 2 sum_{k<n} log(1-2e/k) - sum_{k<=n} log(1-4e/k) = 4e/n + e^2 (4 H2_{n-1} + 8/n^2) + O(e^3)
H2m = sp.Symbol('H2m')                        # H^{(2)}_{n-1}
logprod = 4*e/n + e**2*(4*H2m + 8/n**2)
tn = sp.series((1 - 2*e/n)/(1 - 3*e/n)*sp.exp(logprod), e, 0, 3).removeO()
target = 1 + 5*e/n + e**2*(sp.Rational(23)/n**2 + 4*H2m)
report(f"n^2 t_n = {sp.expand(tn)} = 1 + 5e/n + e^2(23/n^2 + 4 H2_(n-1)) + O(e^3)", sp.simplify(sp.expand(tn - target)) == 0)
# the log-sum identity: 2 sum_{k<n} log(1-2e/k) = -4e H_{n-1} - 4e^2 H2_{n-1} + ...,  -sum_{k<=n} log(1-4e/k) = 4e H_n + 8e^2 H2_n + ...
ok_h = True
for nv in range(1, 12):
    H = lambda m, p=1: sum(sp.Rational(1, kk**p) for kk in range(1, m + 1))
    ok_h &= (-4*H(nv - 1) + 4*H(nv) == sp.Rational(4, nv)) and (-4*H(nv - 1, 2) + 8*H(nv, 2) == 4*H(nv - 1, 2) + sp.Rational(8, nv**2))
report("e-coefficient of the log-product: -4 H_(n-1) + 4 H_n = 4/n;  e^2: -4 H2_(n-1) + 8 H2_n = 4 H2_(n-1) + 8/n^2"
       " (exact rationals, n = 1..11)", ok_h)
# t_n from the Pochhammer definition vs the product formula (exact rationals, several n and e)
ok_t = True
for nv in (1, 2, 5, 9):
    for ev in (sp.Rational(1, 7), sp.Rational(-2, 9)):
        poch = (sp.rf(1 - 2*ev, nv)*sp.rf(-3*ev, nv)*sp.rf(-2*ev, nv)/(sp.rf(1 - 3*ev, nv)*sp.rf(1 - 4*ev, nv)*sp.factorial(nv)))
        prodf = 6*ev**2*sp.Rational(1, nv**2)*(1 - 2*ev/nv)/(1 - 3*ev/nv)*sp.Mul(*[(1 - 2*ev/kk)**2 for kk in range(1, nv)])/sp.Mul(*[(1 - 4*ev/kk) for kk in range(1, nv + 1)])
        ok_t &= sp.simplify(poch - prodf) == 0
report("n-th term of Ft = 6 e^2 t_n with t_n = n^-2 (1-2e/n)/(1-3e/n) prod_{k<n}(1-2e/k)^2/prod_{k<=n}(1-4e/k) (exact, n = 1,2,5,9)", ok_t)
z2, z3, z4 = sp.zeta(2), sp.zeta(3), sp.zeta(4)
z22 = (z2**2 - z4)/2
S = z2 + 5*z3*e + e**2*(23*z4 + 4*z22)
Ft = sp.expand(1 + 6*e**2*S)
report(f"Ft = {sp.nsimplify(Ft)}  (zeta(2,2) = {sp.nsimplify(z22)})",
       sp.simplify(Ft - (1 + sp.pi**2*e**2 + 30*z3*e**3 + sp.Rational(26, 15)*sp.pi**4*e**4)) == 0)

print("\n(2) Taylor coefficients of Ft vs a Cauchy integral (|e| = 0.06, 48 points, 30 digits)")
mp.mp.dps = 30
N = 48; r = mp.mpf('0.06')
pts = [r*mp.expj(2*mp.pi*j/N) for j in range(N)]
vals = [mp.hyp3f2(1 - 2*p, -3*p, -2*p, 1 - 3*p, 1 - 4*p, 1) for p in pts]
coef = [sum(v*p**(-kk) for v, p in zip(vals, pts))/N for kk in range(5)]
exact = [1, 0, mp.pi**2, 30*mp.zeta(3), mp.mpf(26)/15*mp.pi**4]
dev = max(abs(c_ - x_) for c_, x_ in zip(coef, exact))
report(f"coefficients {[mp.nstr(mp.re(c_), 15) for c_ in coef]} vs exact {[mp.nstr(x_, 15) for x_ in exact]}; max dev {mp.nstr(dev, 2)}",
       dev < mp.mpf('1e-18'))

print("\n(3) 2(HC1 + C1C1) at delta = 0, exp(2 gamma e) x, expanded exactly, vs SR eq. (10)")
# Gamma(x) = g(x)/x with g(x) = Gamma(1+x);  ln g(x) = -gamma x + sum_{k>=2} (-1)^k zeta(k) x^k / k
ORD = 6
def lng(x): return -sp.EulerGamma*x + sum((-1)**kk*sp.zeta(kk)*x**kk/kk for kk in range(2, ORD + 1))
def ser(expr_exp, pref_rat, order=0):
    """pref_rat * exp(expr_exp) expanded in e through e^order (pref_rat = c e^-4 exactly)"""
    s = sp.series(sp.exp(sp.expand(expr_exp)), e, 0, order + 5).removeO()
    return sp.expand(pref_rat*s)
def trunc(expr, lo=-4, hi=0):
    expr = sp.expand(expr)
    return sum(expr.coeff(e, kk)*e**kk for kk in range(lo, hi + 1))
g2 = 2*sp.EulerGamma*e                    # exp(2 gamma e): SR's printed normalization
# HC1 = g(e)^2 g(-e)^2 / e^4 [ (3/2) g(-e)/g(-3e) - 2 g(-e)^2/g(-2e)^2 ] e^{eL}
HC1a = ser(2*lng(e) + 2*lng(-e) + lng(-e) - lng(-3*e) + e*L + g2, sp.Rational(3, 2)/e**4)
HC1b = ser(2*lng(e) + 2*lng(-e) + 2*lng(-e) - 2*lng(-2*e) + e*L + g2, -2/e**4)
# C1C1 = g(2e) g(-e)^3 g(-2e)^2 / (4 e^4 g(-3e) g(-4e)) * Ft * e^{2eL}
Ftp = 1 + sp.pi**2*e**2 + 30*z3*e**3 + sp.Rational(26, 15)*sp.pi**4*e**4
C1C1s = sp.expand(ser(lng(2*e) + 3*lng(-e) + 2*lng(-2*e) - lng(-3*e) - lng(-4*e) + 2*e*L + g2, sp.Rational(1, 4)/e**4)*Ftp)
coll = trunc(2*(HC1a + HC1b + C1C1s))
SR10 = (-sp.Rational(1, 2)/e**4 + (L**2 - sp.pi**2/2)/(2*e**2) + (L**3/2 - sp.pi**2*L/6 - 17*z3/3)/e
        + sp.Rational(7, 24)*L**4 - 4*z3*L - sp.pi**4/144)
diff = sp.simplify(sp.expand(coll - SR10).subs(sp.zeta(4), sp.pi**4/90).subs(sp.zeta(2), sp.pi**2/6))
report(f"Laurent coefficients e^-4..e^0 of e^(2 gamma e) 2(HC1+C1C1) minus SR (10): {diff}", diff == 0)
collz = sp.expand(coll.subs(sp.zeta(4), sp.pi**4/90).subs(sp.zeta(2), sp.pi**2/6))
for kk in range(-4, 1):
    print(f"      e^{kk}: {sp.simplify(collz.coeff(e, kk))}")
# individual pieces (for the report)
for nm, ex in [('2 HC1', trunc(2*(HC1a + HC1b))), ('2 C1C1', trunc(2*C1C1s))]:
    exz = sp.expand(ex.subs(sp.zeta(4), sp.pi**4/90).subs(sp.zeta(2), sp.pi**2/6))
    print(f"      {nm}: " + ' + '.join(f"({sp.simplify(exz.coeff(e, kk))}) e^{kk}" for kk in range(-4, 1)))

print("\n(4) the nine singles (HH from SR (4)) -> LP exactly")
HH_SR4 = sp.Rational(1, 4)/e**4 + 5*sp.pi**2/(24*e**2) + 29*z3/(6*e) + 3*sp.pi**4/32           # printed normalization
SSs = ser(2*lng(-e) + 2*lng(2*e) + 4*e*L + g2, sp.Rational(1, 4)/e**4)
HSs = ser(3*lng(e) + 3*lng(-e) - lng(-2*e) + 2*e*L + g2, 1/e**4)
C1Ss = ser(3*lng(-e) + lng(e) + lng(2*e) - lng(-2*e) + 3*e*L + g2, -sp.Rational(1, 2)/e**4)
tot = trunc(HH_SR4 + SSs + HSs + 2*C1Ss) + coll
LP = L**4/4 + sp.pi**2*L**2/2 + 7*sp.pi**4/60
d4 = sp.simplify(sp.expand(tot - LP).subs(sp.zeta(4), sp.pi**4/90).subs(sp.zeta(2), sp.pi**2/6))
report(f"sum of the nine singles (printed normalization) - LP through O(e^0): {d4}", d4 == 0)
# cross-check of the Gamma rewriting of SS, HS, C1S against the closed forms (numerical, eps = -0.123, L = 0.7)
mp.mp.dps = 30
ev, Lv = mp.mpf('-0.123'), mp.mpf('0.7'); Gm = mp.gamma
chk = {'SS': (Gm(1 - ev)**2*Gm(2*ev)**2/ev**2*mp.exp(4*ev*Lv), Gm(1 - ev)**2*Gm(1 + 2*ev)**2/(4*ev**4)*mp.exp(4*ev*Lv)),
       'HS': (Gm(1 + ev)*Gm(1 - ev)*Gm(ev)**2*Gm(-ev)**2/Gm(1 - 2*ev)*mp.exp(2*ev*Lv),
              Gm(1 + ev)**3*Gm(1 - ev)**3/(ev**4*Gm(1 - 2*ev))*mp.exp(2*ev*Lv)),
       'C1S': (Gm(1 - ev)**2*Gm(ev)*Gm(2*ev)*Gm(-ev)/(ev*Gm(1 - 2*ev))*mp.exp(3*ev*Lv),
               -Gm(1 - ev)**3*Gm(1 + ev)*Gm(1 + 2*ev)/(2*ev**4*Gm(1 - 2*ev))*mp.exp(3*ev*Lv)),
       'HC1': (Gm(ev)*Gm(1 + ev)*Gm(1 - ev)*Gm(-ev)/Gm(1 - 2*ev)*(mp.beta(-2*ev, -ev) - mp.beta(-ev, -ev))/ev,
               Gm(1 + ev)**2*Gm(1 - ev)**2/ev**4*(mp.mpf(3)/2*Gm(1 - ev)/Gm(1 - 3*ev) - 2*Gm(1 - ev)**2/Gm(1 - 2*ev)**2)),
       'C1C1/Ft': (Gm(ev)*Gm(2*ev)/Gm(1 + ev)*Gm(1 - ev)**2*Gm(-ev)*Gm(1 - 2*ev)*Gm(-2*ev)/(Gm(1 - 3*ev)*Gm(1 - 4*ev)),
                   Gm(1 + 2*ev)*Gm(1 - ev)**3*Gm(1 - 2*ev)**2/(4*ev**4*Gm(1 - 3*ev)*Gm(1 - 4*ev)))}
report("Gamma rewritings used above equal the closed forms (eps = -0.123): " +
       ', '.join(f"{k} rel {mp.nstr(abs(a_/b_ - 1), 2)}" for k, (a_, b_) in chk.items()),
       all(abs(a_/b_ - 1) < mp.mpf('1e-25') for a_, b_ in chk.values()))
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
