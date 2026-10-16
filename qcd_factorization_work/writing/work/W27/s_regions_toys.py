#!/usr/bin/env python3
"""
W27 / Ch24 sec:front-regions -- two pedagogical toy examples (writer-derived, additional examples):
 (T1) ex:front-jantzen-toy: I(t) = Int_0^oo dx x^(-eps)/((x+t)(x+1)), 0<eps<1, t -> 0.
      exact: I = (pi/sin(pi eps)) (t^(-eps) - 1)/(1 - t);
      soft region (x ~ t): F^(s) = (pi/sin pi eps) t^(-eps)/(1-t);  hard region (x ~ 1): F^(h) = -(pi/sin pi eps)/(1-t);
      overlap F^(s,h) = 0 (scaleless);  master identity I = F^(s) + F^(h) - F^(s,h) exactly (all orders, |t|<1).
 (T2) ex:front-hidden-toy: G(t) = Int_0^oo dx x^(-eps)/((x-1)^2 + t): P = x^2 - 2x + 1 + t has a negative
      coefficient; the only essential facet of conv{(2,0),(1,0),(0,0),(0,1)} is the bottom edge (r = (0,1),
      naive Taylor expansion in t, non-integrable at x = 1); after splitting at x = 1, y = |x - 1|, P = y^2 + t
      and the new region y ~ t^(1/2) gives G(t) = pi t^(-1/2) + O(t^0).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + info) if info else ""))

mp.mp.dps = 30
# ---- (T1)
for eps in [mp.mpf('0.3'), mp.mpf('0.55')]:
    for t in [mp.mpf('0.01'), mp.mpf('0.3')]:
        num = mp.quad(lambda x: x**(-eps) / ((x + t) * (x + 1)), [0, t, 1, 10, mp.inf])
        exact = mp.pi / mp.sin(mp.pi * eps) * (t**(-eps) - 1) / (1 - t)
        Fs = mp.pi / mp.sin(mp.pi * eps) * t**(-eps) / (1 - t)
        Fh = -mp.pi / mp.sin(mp.pi * eps) / (1 - t)
        check(f"(T1) eps={mp.nstr(eps,3)}, t={mp.nstr(t,3)}: numeric = exact = F(s) + F(h)",
              abs(num - exact) < 1e-15 * abs(exact) * 1e3 and abs(Fs + Fh - exact) < 1e-25, f"I = {mp.nstr(num, 12)}")
# term-by-term: soft terms Int x^(k-eps)/(x+t) = t^(k-eps) (-1)^k pi/sin(pi eps) (analytic continuation),
# hard terms Int x^(-eps-k-1)/(x+1) = -(-1)^k pi/sin(pi eps)
s_ = sp.symbols('s')
k = sp.symbols('k', integer=True, nonnegative=True)
e = sp.symbols('epsilon', positive=True)
check("(T1') sin(pi(k+1-eps)) = (-1)^k sin(pi eps) and sin(pi(-eps-k)) = -(-1)^k sin(pi eps)  (k=0..6)",
      all(sp.simplify(sp.sin(sp.pi * (j + 1 - e)) - (-1)**j * sp.sin(sp.pi * e)) == 0 and
          sp.simplify(sp.sin(sp.pi * (-e - j)) + (-1)**j * sp.sin(sp.pi * e)) == 0 for j in range(7)))
# Mellin formula Int_0^oo x^(s-1)/(x+a) dx = a^(s-1) pi/sin(pi s), 0<Re s<1
for sv in [mp.mpf('0.2'), mp.mpf('0.7')]:
    num = mp.quad(lambda u: mp.e**(u * sv) / (mp.e**u + 2), [-mp.inf, -20, 0, 20, mp.inf])   # x = e^u
    check(f"(T1'') Mellin formula at s={mp.nstr(sv,2)}, a=2", abs(num - 2**(sv - 1) * mp.pi / mp.sin(mp.pi * sv)) < 1e-12)
# ---- (T2)
for eps in [mp.mpf('0.1'), mp.mpf('0.4')]:
    vals = []
    for t in [mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]:
        G = mp.quad(lambda x: x**(-eps) / ((x - 1)**2 + t), [0, 1 - mp.sqrt(t) * 50, 1, 1 + mp.sqrt(t) * 50, 10, mp.inf])
        vals.append((t, G, (G - mp.pi / mp.sqrt(t))))
    ok = abs(vals[-1][1] * mp.sqrt(vals[-1][0]) - mp.pi) < 1e-3
    check(f"(T2) eps={mp.nstr(eps,2)}: sqrt(t) G(t) -> pi; G - pi/sqrt(t) stays O(1)", ok,
          "; ".join(f"t={mp.nstr(a,1)}: sqrt(t)G={mp.nstr(b*mp.sqrt(a),8)}, G-pi/sqrt t={mp.nstr(c,6)}" for a, b, c in vals))
# Newton polytope of x^2 - 2x + 1 + t in (x-exponent, t-exponent): hull of (2,0),(1,0),(0,0),(0,1)
# inward normals: bottom (0,1) [essential], left (1,0) [r_t = 0], hypotenuse -(1,2) [r_t < 0]
pts = [(2, 0), (1, 0), (0, 0), (0, 1)]
def is_facet(r):
    vals = [r[0] * a + r[1] * b for a, b in pts]
    mn = min(vals)
    on = [p for p, v in zip(pts, vals) if v == mn]
    return len(on) >= 2
check("(T2') the only essential facet (inward normal with r_t > 0) is the bottom edge r = (0,1)",
      is_facet((0, 1)) and not is_facet((1, 2)) and is_facet((-1, -2)) and is_facet((1, 0)))
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
