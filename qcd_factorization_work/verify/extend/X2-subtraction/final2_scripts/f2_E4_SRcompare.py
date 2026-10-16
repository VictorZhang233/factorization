"""X2 final2 / f2_E4_SRcompare.py -- Prop E.4(d): the delta = 0 values of the collinear-type singles HC1 (= HC2 by
mirror symmetry) and C1C1 (= C2C2), obtained from the Schwinger representation in f2_E4_singles.py, compared with
Smirnov-Rakhmetov hep-ph/9812529:
  (1) the C1C1 double integral J2(eps) = int int y^-e (1-y)^-e z^(-1-e) (1-z)^(-2e) (y+z-yz)^(-1) dy dz (-1/2 < e < 0)
      vs its hypergeometric forms: B(1-e,1-e) Gamma(-e) Gamma(1-2e)/Gamma(1-3e) 3F2(1,1-e,1-2e;2-2e,1-3e;1) and, after
      Thomae's relation (DLMF 16.4.11), Gamma(1-e)^2 Gamma(-e) Gamma(1-2e) Gamma(-2e)/(Gamma(1-3e) Gamma(1-4e))
      * 3F2(1-2e,-3e,-2e;1-3e,1-4e;1), whose series converges for |e| < 1/4 (parameter excess 1);
  (2) HC1(e,0) and C1C1(e,0) vs SR's Mellin-Barnes representations eq. (9) and eq. (8), evaluated with straight
      contours (possible for -1/2 < e < 0), at e = -0.15, -0.3, -0.42;
  (3) the Laurent expansion of 2 [HC1 + C1C1] at delta = 0 (Qt2 = 1, m2 = e^-L), computed here independently (exact
      Gamma functions times the Taylor coefficients of the Thomae-transformed 3F2, obtained by Cauchy integrals on
      |e| = 0.1), vs SR's printed eq. (10) (SR omit exp(-gamma_E eps) per loop in eps-expansions);
  (4) the sum of all nine singles (HH from SR eq. (4), SS/HS/C1S/C2S exact Gamma products = SR (5)-(7), the four
      collinear-type ones from (3)) -> LP = L^4/4 + pi^2 L^2/2 + 7 pi^4/60 + O(eps)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import functools
print = functools.partial(print, flush=True)
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

G = mp.gamma
def B(x, y): return G(x)*G(y)/G(x + y)
def F3_thomae(e):
    return mp.hyp3f2(1 - 2*e, -3*e, -2*e, 1 - 3*e, 1 - 4*e, 1)
def J2_thomae(e):
    return G(1 - e)**2*G(-e)*G(1 - 2*e)*G(-2*e)/(G(1 - 3*e)*G(1 - 4*e))*F3_thomae(e)
def J2_orig(e):
    return B(1 - e, 1 - e)*G(-e)*G(1 - 2*e)/G(1 - 3*e)*mp.hyp3f2(1, 1 - e, 1 - 2*e, 2 - 2*e, 1 - 3*e, 1)
def J2_quad(e):
    f = lambda y, z: y**(-e)*(1 - y)**(-e)*z**(-1 - e)*(1 - z)**(-2*e)/(y + z - y*z)
    pz = 2/(-e)                                     # z = t^pz removes the z^(-1-eps) endpoint singularity
    g = lambda t: (lambda z: pz*t**(pz - 1)*mp.quad(lambda y: f(y, z), [0, z, 1]))(t**pz)
    return mp.quad(g, [0, mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), 1])
def HC1_0(e, Q2=1, mm=1):
    return (G(e)*G(1 + e)*G(1 - e)*G(-e)/G(1 - 2*e)*mp.mpf(Q2)**(-2 - e)*mp.mpf(mm)**(-e)
            *(B(-2*e, -e) - B(-e, -e))/e)
def C1C1_0(e, Q2=1, mm=1):
    return G(e)*G(2*e)/G(1 + e)*mp.mpf(Q2)**(-2)*mp.mpf(mm)**(-2*e)*J2_thomae(e)
def SR8(e, c):
    """SR (8): (1c-1c) = (2c-2c), our normalization Qt2 = 1, m2 = 1 (SR's -m2 = 1, Q2 = 1); straight contour Re s = c"""
    f = lambda t: (lambda s: G(s - 3*e)*G(s + 1 - 2*e)*G(s + 1 - e)*G(e - s)*G(-s)/G(s + 1 - 3*e))(c + 1j*t)
    mb = mp.quad(f, [-mp.inf, -20, -5, 0, 5, 20, mp.inf])/(2*mp.pi)
    return G(e)*G(-e)*G(2*e)/G(1 + e)*mb
def SR9(e, c):
    f = lambda t: (lambda s: G(s + 1)*G(s - e)*G(s + 1 + e)*G(-e - s)*G(-s)/G(s + 1 - 2*e))(c + 1j*t)
    mb = mp.quad(f, [-mp.inf, -20, -5, 0, 5, 20, mp.inf])/(2*mp.pi)
    return G(e)*G(-e)*G(1 - e)/G(1 - 2*e)*mb

print("(1) C1C1 double integral vs the hypergeometric forms")
mp.mp.dps = 30
for ev in ['-0.15', '-0.3', '-0.42']:
    e = mp.mpf(ev)
    jq, jo, jt = J2_quad(e), J2_orig(e), J2_thomae(e)
    report(f"eps = {ev}: quadrature {mp.nstr(jq, 20)}  3F2 {mp.nstr(jo, 20)}  Thomae {mp.nstr(jt, 20)}  "
           f"(rel {mp.nstr(abs(jq/jt - 1), 2)}, {mp.nstr(abs(jo/jt - 1), 2)})",
           abs(jq/jt - 1) < mp.mpf('1e-12') and abs(jo/jt - 1) < mp.mpf('1e-15'))

print("\n(2) delta = 0 values vs SR's Mellin-Barnes representations (straight contours)")
mp.mp.dps = 25
for ev in ['-0.15', '-0.3', '-0.42']:
    e = mp.mpf(ev)
    c8 = 2*e; c9 = e/2                      # 3e < c8 < e;  e < c9 < 0 (and > -1 - e)
    v8, v9 = SR8(e, c8), SR9(e, c9)
    h, cc = HC1_0(e), C1C1_0(e)
    report(f"eps = {ev}: HC1 {mp.nstr(h, 18)} vs SR (9) {mp.nstr(mp.re(v9), 18)} (rel {mp.nstr(abs(h/v9 - 1), 2)})",
           abs(h/v9 - 1) < mp.mpf('1e-15'))
    print(f"      OBSERVATION eps = {ev}: C1C1 {mp.nstr(cc, 18)} vs the literal value of SR's printed (8) {mp.nstr(mp.re(v8), 18)}"
          f" (rel {mp.nstr(abs(cc/v8 - 1), 2)}): the printed (8) is NOT reproduced; SR's (10) is (part (3)), so (8) as printed"
          f" is inconsistent with SR's own (9)+(10); (8) is not used")

print("\n(3) Laurent expansion of 2(HC1 + C1C1) at delta = 0 vs SR eq. (10)")
mp.mp.dps = 35
N = 48; r = mp.mpf('0.06')
def taylor(fun, kmax):
    pts = [r*mp.expj(2*mp.pi*j/N) for j in range(N)]
    vals = [fun(p) for p in pts]
    return [sum(v*p**(-k) for v, p in zip(vals, pts))/N for k in range(kmax + 1)]
eg = mp.euler
# g_C(e) = e^4 * exp(2 gamma e) * C1C1(e, 0)|_{m2 = 1};  g_H(e) = e^4 * exp(2 gamma e) * HC1(e, 0)|_{m2 = 1}
gC = taylor(lambda e: e**4*mp.exp(2*eg*e)*C1C1_0(e), 6)
gH = taylor(lambda e: e**4*mp.exp(2*eg*e)*HC1_0(e), 6)
print("   Taylor coefficients of e^4 e^(2 gamma e) C1C1|_(m2=1):", [mp.nstr(mp.re(x), 15) for x in gC[:5]],
      " (imaginary parts <", mp.nstr(max(abs(mp.im(x)) for x in gC[:5]), 2), ")")
print("   Taylor coefficients of e^4 e^(2 gamma e) HC1|_(m2=1) :", [mp.nstr(mp.re(x), 15) for x in gH[:5]])
z3 = mp.zeta(3)
def laurent_mine(L):
    # 2 C1C1 m2^(-2e) + 2 HC1 m2^(-e) with m2 = e^-L:  m2^(-k e) = exp(k e L) -> convolution of Taylor series
    L = mp.mpf(L)
    cC = [sum(gC[k - j]*(2*L)**j/mp.factorial(j) for j in range(k + 1)) for k in range(5)]
    cH = [sum(gH[k - j]*L**j/mp.factorial(j) for j in range(k + 1)) for k in range(5)]
    return [2*mp.re(x + y) for x, y in zip(cC, cH)]          # coefficients of e^-4 ... e^0
def laurent_SR(L):
    L = mp.mpf(L)
    return [mp.mpf(-1)/2, mp.mpf(0), (L**2 - mp.pi**2/2)/2, L**3/2 - mp.pi**2*L/6 - 17*z3/3,
            mp.mpf(7)/24*L**4 - 4*z3*L - mp.pi**4/144]
for L in [0, 1, 2, 5]:
    mine = laurent_mine(L); sr = laurent_SR(L)
    dev = max(abs(a_ - b_) for a_, b_ in zip(mine, sr))
    report(f"L = {L}: coefficients of eps^-4..eps^0  mine {[mp.nstr(x, 12) for x in mine]}  SR {[mp.nstr(x, 12) for x in sr]}"
           f"  max dev {mp.nstr(dev, 2)}", dev < mp.mpf('1e-20'))

print("\n(4) sum of the nine singles at small eps -> LP (HH from SR (4); the others computed here)")
mp.mp.dps = 70
def total(e, L):
    e = mp.mpf(e); L = mp.mpf(L); mm = mp.e**(-L); norm = mp.e**(2*eg*e)
    hh = mp.mpf(1)/(4*e**4) + 5*mp.pi**2/(24*e**2) + 29*z3/(6*e) + 3*mp.pi**4/32         # SR (4), printed norm.
    ss = norm*G(1 - e)**2*G(2*e)**2/(e**2*mm**(4*e))
    hs = norm*G(1 + e)*G(1 - e)*G(e)**2*G(-e)**2/(G(1 - 2*e)*mm**(2*e))
    c1s = norm*G(1 - e)**2*G(e)*G(2*e)*G(-e)/(e*G(1 - 2*e)*mm**(3*e))
    coll = norm*2*(HC1_0(e, 1, mm) + C1C1_0(e, 1, mm))
    return hh + ss + hs + 2*c1s + coll
for L in ['2', '5', '9.21034037197618']:
    lp = mp.mpf(L)**4/4 + mp.pi**2*mp.mpf(L)**2/2 + 7*mp.pi**4/60
    vals = [total(ev, L) - lp for ev in ['1e-8', '1e-11']]
    report(f"L = {L}: total - LP at eps = 1e-8, 1e-11: {[mp.nstr(v, 5) for v in vals]} (O(eps))",
           abs(vals[1]) < mp.mpf('1e-6')*(1 + lp) and abs(vals[1]/vals[0]) < mp.mpf('2e-3'))
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
