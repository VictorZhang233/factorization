# X1 final2 (Fix 5) -- verification of the HAND proof printed in the report (Lemma V, proof of T3(e) step (3)):
#   |v_K| < 1/2  and  |v_K| <= s/4,  s := |x_1| + |x_2|,   v_K := w_K^[12] - 1/2 on the theta = pi/4 contour,
# and of the cubic remainder bound |v_K - (x_1 - x_2)/4| <= s^3 (1+s/4)(3/2+s/4) / (4(1+sqrt2 s)).
# The printed proof works in the variables s = t1 + t2, p = t1 t2 (0 <= p <= s^2/4) and groups A^2 - |N|^2 into five
# terms that are each >= 0 for p <= s^2/4.  This script checks every algebraic step symbolically:
#   (1) the nine pole pairs of L1' (gluon pole z_e, regulator poles +iK [initial], -iK [final]) give the closed forms;
#   (2) on the rays: D (pattern I,F) and S (pattern I,I) both equal s w - i p, and v_II = ((t1-t2)/s) v_IF;
#   (3) |P|^2 = A(s,p) := 1 + sqrt2 s + s^2 + sqrt2 s p + p^2 and |N|^2 = 1 + 2sqrt2(s-q) + 4s^2 + 4q^2 + 8sqrt2 p(s+q) + 16p^2,
#       q := p^2/s, where v_IF = (s w/4) N/P^2, P = 1 + D;
#   (4) A^2 - |N|^2 = G1 + G2 + G3 + G4 + G5 with
#       G1 = s^4 - 14 p^2, G2 = 2sqrt2 (s^3 - 3 s p), G3 = 4 p^2 (s^2 - p^2/s^2), G4 = 2sqrt2 p^2 (s - 4p/s),
#       G5 = 2sqrt2 s^3 p + 4 s^2 p + 2sqrt2 s p^3 + p^4 + 2sqrt2 p^2/s   (each >= 0 for 0 <= p <= s^2/4);
#   (5) 2|1+D|^2 - (2|D|^2 + s) = 2 + (2sqrt2 - 1) s  (=> |v_IF| < 1/2);
#   (6) v_K - (x1-x2)/4 = O(s^3) in every pattern (no quadratic term), and the remainder identity of the report;
#   (7) random-point confirmation of the two bounds and of the remainder bound in all four patterns.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

out = []
def log(s=''):
    print(s, flush=True); out.append(s)
ok = True
x1, x2 = sp.symbols('x1 x2')
t1, t2 = sp.symbols('t1 t2', positive=True)
s, p = sp.symbols('s p', positive=True)
r2 = sp.sqrt(2)
one = sp.Integer(1)
uz = lambda x: x**2/(x**2 - 1); up = lambda x: one/(2*(1 - x)); um = lambda x: one/(2*(1 + x))
# race weight of colour order [12] for a pole pair, with poles iK/y (y = x for the gluon pole, 1 for +iK, -1 for -iK)
def W12(y1, f1, y2, f2):
    if f1 and f2: return y2/(y1 + y2)
    if (not f1) and (not f2): return y1/(y1 + y2)
    return one if ((not f1) and f2) else sp.Integer(0)
def vpattern(c1, c2):
    tot = 0
    for (y1, u1, f1) in ((x1, uz(x1), c1 == 'F'), (one, up(x1), False), (-one, um(x1), True)):
        for (y2, u2, f2) in ((x2, uz(x2), c2 == 'F'), (one, up(x2), False), (-one, um(x2), True)):
            tot += u1*u2*W12(y1, f1, y2, f2)
    return sp.simplify(tot - sp.Rational(1, 2))
v = {(a, b): vpattern(a, b) for a in 'IF' for b in 'IF'}
D = x1 - x2 - x1*x2; S = x1 + x2 + x1*x2
cIF = (2*D**2 + (x1 - x2))/(4*(1 + D)**2)
cII = (x1 - x2)*(2*S**2 + (x1 + x2))/(4*(1 + S)**2*(x1 + x2))
c1 = sp.simplify(v[('I', 'F')] - cIF) == 0
c2 = sp.simplify(v[('I', 'I')] - cII) == 0
c3 = sp.simplify(v[('F', 'I')] + v[('I', 'F')].subs({x1: -x1, x2: -x2}, simultaneous=True)) == 0
c4 = sp.simplify(v[('F', 'F')] + v[('I', 'I')].subs({x1: -x1, x2: -x2}, simultaneous=True)) == 0
ok &= c1 and c2 and c3 and c4
log(f"(1) nine-pole-pair sums: v_IF closed form {c1}; v_II closed form {c2}; v_FI = -v_IF(-x) {c3}; v_FF = -v_II(-x) {c4}")
w = sp.exp(-sp.I*sp.pi/4)
sub_IF = {x1: t1*w, x2: -t2*w}; sub_II = {x1: t1*w, x2: t2*w}
target = (t1 + t2)*w - sp.I*t1*t2
d1 = sp.simplify(sp.expand_complex(D.subs(sub_IF, simultaneous=True) - target)) == 0
d2 = sp.simplify(sp.expand_complex(S.subs(sub_II, simultaneous=True) - target)) == 0
vIF = cIF.subs(sub_IF, simultaneous=True); vII = cII.subs(sub_II, simultaneous=True)
d3 = sp.simplify(vII - (t1 - t2)/(t1 + t2)*vIF) == 0
ok &= d1 and d2 and d3
log(f"(2) on the rays: D_IF = s w - i p: {d1};  S_II = s w - i p: {d2};  v_II = ((t1-t2)/s) v_IF: {d3}")
# (3) |P|^2 and |N|^2 in terms of s, p
Pt = 1 + target
P2 = sp.expand(sp.expand_complex(Pt*sp.conjugate(Pt)))
A = 1 + r2*s + s**2 + r2*s*p + p**2
sp_sub = {s: t1 + t2, p: t1*t2}
e1 = sp.simplify(P2 - sp.expand(A.subs(sp_sub, simultaneous=True))) == 0
Nt = sp.simplify(vIF*4*Pt**2/((t1 + t2)*w))
N2 = sp.simplify(sp.expand_complex(sp.expand(Nt*sp.conjugate(Nt))))
q = p**2/s
N2sp = 1 + 2*r2*(s - q) + 4*s**2 + 4*q**2 + 8*r2*p*(s + q) + 16*p**2
e2 = sp.simplify(N2 - N2sp.subs(sp_sub, simultaneous=True)) == 0
# the explicit form of N as printed: N = 1 + 2 s w - 4 i p - 2 q conj(w)
Nform = 1 + 2*(t1 + t2)*w - 4*sp.I*t1*t2 - 2*(t1*t2)**2/(t1 + t2)*sp.conjugate(w)
e3 = sp.simplify(sp.expand_complex(Nt - Nform)) == 0
ok &= e1 and e2 and e3
log(f"(3) |P|^2 = 1 + sqrt2 s + s^2 + sqrt2 s p + p^2: {e1};  |N|^2 = 1 + 2sqrt2(s-q) + 4s^2 + 4q^2 + 8sqrt2 p(s+q) + 16p^2: {e2};"
    f"  N = 1 + 2 s w - 4 i p - 2 q w*: {e3}")
# (4) grouping
G1 = s**4 - 14*p**2; G2 = 2*r2*(s**3 - 3*s*p); G3 = 4*p**2*(s**2 - p**2/s**2); G4 = 2*r2*p**2*(s - 4*p/s)
G5 = 2*r2*s**3*p + 4*s**2*p + 2*r2*s*p**3 + p**4 + 2*r2*p**2/s
e4 = sp.simplify(sp.expand(A**2 - N2sp - (G1 + G2 + G3 + G4 + G5))) == 0
ok &= e4
log(f"(4) A^2 - |N|^2 = G1+G2+G3+G4+G5 identically: {e4}")
# each group >= 0 on 0 <= p <= s^2/4 : substitute p = s^2 r/4, r in [0,1]
rr = sp.symbols('r', nonnegative=True)
ps = s**2*rr/4
g1 = sp.factor(sp.simplify(G1.subs(p, ps))); g2 = sp.factor(sp.simplify(G2.subs(p, ps)))
g3 = sp.factor(sp.simplify(G3.subs(p, ps))); g4 = sp.factor(sp.simplify(G4.subs(p, ps)))
log(f"    with p = r s^2/4 (0 <= r <= 1):  G1 = {g1},  G2 = {g2},  G3 = {g3},  G4 = {g4}  (G5 has only positive terms)")
grid = np.linspace(0, 1, 2001)
pos = True
for gexpr in (g1, g2, g3, g4):
    f = sp.lambdify((s, rr), gexpr, 'numpy')
    for sv in (1e-3, 0.1, 1.0, 10.0, 1e3):
        pos &= np.all(f(sv, grid) >= -1e-12*max(1, sv**4))
ok &= pos
log(f"    G1..G4 >= 0 on the sampled (s, r) grid: {pos}  [analytically, for 0 <= r <= 1: G1 = s^4(8-7r^2)/8 >= s^4/8, "
    f"G2 = (sqrt2/2) s^3 (4-3r) >= (sqrt2/2) s^3, G3 = r^2 s^6 (16-r^2)/64 >= 0, G4 = (sqrt2/8) r^2 s^5 (1-r) >= 0]")
# (5) |v_IF| < 1/2
lhs = sp.expand(sp.expand_complex(2*(1 + target)*sp.conjugate(1 + target) - 2*target*sp.conjugate(target)))
e5 = sp.simplify(lhs - (2 + 2*r2*(t1 + t2))) == 0
ok &= e5
log(f"(5) 2|1+D|^2 - 2|D|^2 = 2 + 2sqrt2 s on the rays: {e5}  =>  2|1+D|^2 - (2|D|^2 + s) = 2 + (2sqrt2-1) s > 0, |v_IF| < 1/2")
# (6) cubic remainder: series in a scale parameter h (x_e -> h x_e)
h = sp.symbols('h')
cub = True
for key, expr in v.items():
    ser = sp.series(expr.subs({x1: h*x1, x2: h*x2}, simultaneous=True), h, 0, 3).removeO()
    lin = sp.simplify(ser - h*(x1 - x2)/4)
    cub &= (lin == 0)
ok &= cub
rid = sp.simplify(cIF - (x1 - x2)/4 + D*(2*x1*x2 + (x1 - x2)*D)/(4*(1 + D)**2)) == 0
ok &= rid
log(f"(6) v_K = (x1-x2)/4 + O(|x|^3) in all four patterns (no quadratic term): {cub};  remainder identity "
    f"v_IF - (x1-x2)/4 = -D(2x1x2 + (x1-x2)D)/(4(1+D)^2): {rid}")
# (7) random points, all four patterns, independent numerical pole sum
rng = np.random.default_rng(7)
def wnum(xa, xb, fa, fb):
    poles = lambda x, f: [(x, x**2/(x**2 - 1), f), (1.0, 1/(2*(1 - x)), False), (-1.0, 1/(2*(1 + x)), True)]
    tot = 0
    for (ya, ua, Fa) in poles(xa, fa):
        for (yb, ub, Fb) in poles(xb, fb):
            Wt = yb/(ya + yb) if (Fa and Fb) else (ya/(ya + yb) if (not Fa and not Fb) else (1.0 if (not Fa and Fb) else 0.0))
            tot += ua*ub*Wt
    return tot - 0.5
wn = np.exp(-1j*np.pi/4)
m_half = m_lin = m_rem = 0
for _ in range(200000):
    tt = 10**rng.uniform(-4, 4, size=2); sg = rng.choice([1, -1], size=2)   # sg = +1: initial (x = t w), -1: final (x = -t w)
    xa, xb = sg[0]*tt[0]*wn, sg[1]*tt[1]*wn
    vv = wnum(xa, xb, sg[0] < 0, sg[1] < 0)
    sv = tt.sum()
    m_half = max(m_half, abs(vv)); m_lin = max(m_lin, abs(vv)/(sv/4))
    m_rem = max(m_rem, abs(vv - (xa - xb)/4)/(sv**3*(1 + sv/4)*(1.5 + sv/4)/(4*(1 + np.sqrt(2)*sv))))
ok &= m_half < 0.5 and m_lin <= 1 + 1e-9 and m_rem <= 1 + 1e-9
log(f"(7) 2e5 random points, |x_e| in [1e-4, 1e4], four patterns: sup|v_K| = {m_half:.6f} (< 1/2); "
    f"sup |v_K|/(s/4) = {m_lin:.6f} (<= 1); sup |v_K - (x1-x2)/4| / cubic bound = {m_rem:.4f} (<= 1)")
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'vK_hand_proof.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
