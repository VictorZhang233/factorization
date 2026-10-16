"""X2 final2 -- f2v_SR8.py: independent analysis of the collinear-type singles at delta = 0 and of Smirnov-Rakhmetov
(hep-ph/9812529) eqs. (8), (9), (10) [read from the full text; units Qt2 = 1; SR's -m^2 = our m2 > 0; SR omit
exp(-gamma_E eps) per loop in eps expansions].
  C1C1(eps,0) = Gamma(eps)Gamma(2eps)/Gamma(1+eps) * J2(eps) * m2^(-2eps),
      J2 = int_0^1 int_0^1 y^-e (1-y)^-e z^(-1-e) (1-z)^(-2e) / (z + y(1-z)) dy dz          (-1/2 < e < 0 in this code)
         = B(1-e,1-e) Gamma(-e) Gamma(1-2e)/Gamma(1-3e) 3F2(1,1-e,1-2e; 2-2e,1-3e; 1)        (geometric series)
         = Gamma(1-e)^2 Gamma(-e) Gamma(1-2e) Gamma(-2e)/(Gamma(1-3e) Gamma(1-4e)) * 3F2(1-2e,-3e,-2e;1-3e,1-4e;1) (Thomae)
  HC1(eps,0) = Gamma(eps)Gamma(1+eps)Gamma(1-eps)Gamma(-eps)/Gamma(1-2eps) [B(-2e,-e) - B(-e,-e)]/e * m2^(-eps).
Checks: (1) J2 by direct 2D quadrature vs both 3F2 forms; (2) HC1 vs SR (9) (straight contour e < c < 0);
(3) C1C1 vs the LITERAL SR (8) (contour 3e < c < e) at e = -0.42 ... -0.01, and the leading pole of eps^4 * SR(8);
(4) the Mellin-Barnes representation derived here (MB splitting of 1/(z + y(1-z)) in J2, then s -> eps - s):
      C1C1(eps,0) = Gamma(eps)Gamma(1-eps)Gamma(2eps)/(Gamma(1+eps)Gamma(-3eps)) m2^(-2eps)
                    x (1/2 pi i) int ds Gamma(s-3e)Gamma(s-2e)Gamma(s-e)Gamma(1+e-s)Gamma(-s)/Gamma(s+1-3e),  e < c < 0;
(5) e^(2 gamma e) 2[HC1 + C1C1] - SR(10) = O(eps) numerically (L = 0, 2, 5; eps = +-1e-3, +-1e-4; Thomae form for e > 0).
Run: python3 -I f2v_SR8.py  (log: ../final2_logs/f2v_SR8.log)"""
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
def J2_quad(e):
    # z = u^(1/(-e)) maps z^(-1-e) dz to (1/(-e)) du; the corner is handled by splitting at y = z
    f = lambda y, z: y**(-e)*(1 - y)**(-e)*(1 - z)**(-2*e)/(z + y*(1 - z))
    def inner(u):
        z = u**(1/(-e))
        return mp.quad(lambda y: f(y, z), [0, z, 1])/(-e)
    return mp.quad(inner, [0, mp.mpf('0.01'), mp.mpf('0.3'), 1])
def J2_series(e):
    return B(1 - e, 1 - e)*G(-e)*G(1 - 2*e)/G(1 - 3*e)*mp.hyp3f2(1, 1 - e, 1 - 2*e, 2 - 2*e, 1 - 3*e, 1)
def J2_thomae(e):
    return G(1 - e)**2*G(-e)*G(1 - 2*e)*G(-2*e)/(G(1 - 3*e)*G(1 - 4*e))*mp.hyp3f2(1 - 2*e, -3*e, -2*e, 1 - 3*e, 1 - 4*e, 1)
def C1C1(e, mm=1): return G(e)*G(2*e)/G(1 + e)*J2_thomae(e)*mp.mpf(mm)**(-2*e)
def HC1(e, mm=1): return G(e)*G(1 + e)*G(1 - e)*G(-e)/G(1 - 2*e)*(B(-2*e, -e) - B(-e, -e))/e*mp.mpf(mm)**(-e)
def MB(f, c):
    g = lambda t: f(c + 1j*t)
    return mp.quad(g, [-mp.inf, -40, -10, -2, 0, 2, 10, 40, mp.inf])/(2*mp.pi)
def SR8_literal(e):
    f = lambda s: G(s - 3*e)*G(s + 1 - 2*e)*G(s + 1 - e)*G(e - s)*G(-s)/G(s + 1 - 3*e)
    return G(e)*G(-e)*G(2*e)/G(1 + e)*MB(f, 2*e)             # 3e < 2e < e for e < 0
def SR9(e):
    f = lambda s: G(s + 1)*G(s - e)*G(s + 1 + e)*G(-e - s)*G(-s)/G(s + 1 - 2*e)
    return G(e)*G(-e)*G(1 - e)/G(1 - 2*e)*MB(f, e/2)          # e < e/2 < 0
def C1C1_MBours(e):
    f = lambda s: G(s - 3*e)*G(s - 2*e)*G(s - e)*G(1 + e - s)*G(-s)/G(s + 1 - 3*e)
    return G(e)*G(1 - e)*G(2*e)/(G(1 + e)*G(-3*e))*MB(f, e/2)  # e < e/2 < 0

mp.mp.dps = 30
print("(1) J2: 2D quadrature vs the two 3F2 forms")
for ev in ['-0.15', '-0.3', '-0.42']:
    e = mp.mpf(ev)
    q, s1, s2 = J2_quad(e), J2_series(e), J2_thomae(e)
    report(f"eps = {ev}: quad {mp.nstr(q, 18)}, series {mp.nstr(s1, 18)}, Thomae {mp.nstr(s2, 18)} "
           f"(rel {mp.nstr(abs(q/s2 - 1), 2)}, {mp.nstr(abs(s1/s2 - 1), 2)})", abs(q/s2 - 1) < 1e-10 and abs(s1/s2 - 1) < 1e-20)
print("\n(2) HC1(eps,0) vs SR (9)")
mp.mp.dps = 25
for ev in ['-0.15', '-0.3', '-0.42', '-0.05']:
    e = mp.mpf(ev); a_, b_ = HC1(e), SR9(e)
    report(f"eps = {ev}: HC1 {mp.nstr(a_, 18)}  SR(9) {mp.nstr(mp.re(b_), 18)}  rel {mp.nstr(abs(a_/b_ - 1), 2)}", abs(a_/b_ - 1) < 1e-15)
print("\n(3) C1C1(eps,0) vs the literal SR (8); (4) vs the MB representation derived here")
rows = []
for ev in ['-0.42', '-0.3', '-0.15', '-0.05', '-0.02', '-0.01']:
    e = mp.mpf(ev)
    c, s8, mbo = C1C1(e), SR8_literal(e), C1C1_MBours(e)
    rows.append((e, c, mp.re(s8)))
    print(f"   eps = {ev}: C1C1 {mp.nstr(c, 15)}   literal SR(8) {mp.nstr(mp.re(s8), 15)}   ratio {mp.nstr(mp.re(s8)/c, 8)}"
          f"   eps^4 (SR8 - C1C1) = {mp.nstr(e**4*(mp.re(s8) - c), 8)}")
    report(f"eps = {ev}: MB representation derived here = C1C1 (rel {mp.nstr(abs(mbo/c - 1), 2)})", abs(mbo/c - 1) < 1e-15)
print("   leading pole: eps^4 C1C1 -> 1/4;  eps^4 SR8_literal at eps = -0.01: "
      f"{mp.nstr(rows[-1][0]**4*rows[-1][2], 10)}, at -0.02: {mp.nstr(rows[-2][0]**4*rows[-2][2], 10)}")
report("the literal SR (8) differs from C1C1(eps,0) at O(eps^-4)-relevant size for eps -> 0- (eps^4 (SR8 - C1C1) does not tend to 0)",
       abs(rows[-1][0]**4*(rows[-1][2] - rows[-1][1])) > mp.mpf('1e-3'))
print("\n(5) exp(2 gamma e) * 2[HC1 + C1C1] (m2 = e^-L) minus SR (10), divided by eps: tends to a constant (O(eps) remainder)")
mp.mp.dps = 50
def SR10(e, L):
    z3 = mp.zeta(3)
    return (-mp.mpf(1)/(2*e**4) + (L**2 - mp.pi**2/2)/(2*e**2) + (L**3/2 - mp.pi**2*L/6 - 17*z3/3)/e
            + mp.mpf(7)/24*L**4 - 4*z3*L - mp.pi**4/144)
for L in [0, 2, 5]:
    L = mp.mpf(L); mm = mp.e**(-L); out = []
    for ev in ['1e-3', '-1e-3', '1e-4', '-1e-4']:
        e = mp.mpf(ev)
        val = mp.e**(2*mp.euler*e)*2*(HC1(e, mm) + C1C1(e, mm))
        out.append((ev, (val - SR10(e, L))/e))
    ok = all(abs(o[1] - out[2][1]) < mp.mpf('0.05')*(1 + abs(out[2][1])) for o in out)
    report(f"L = {L}: [value - SR(10)]/eps at eps = " + ", ".join(f"{o[0]}: {mp.nstr(o[1], 10)}" for o in out), ok)
print("\nALL CHECKS PASS (f2v_SR8)" if ALL_OK else "\nSOME CHECK FAILED (f2v_SR8)")
