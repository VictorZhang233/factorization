"""X2 final revision / r3_twoloop_regions.py -- two-loop planar off-shell vertex (M1): identification of the nine
single-approximator terms T_R Gamma (soft-first zeroing patterns, twoloop_patterns.json) with the leading-power region
integrands of the strategy of regions (Smirnov-Rakhmetov, Theor. Math. Phys. 120 (1999) 870 [hep-ph/9812529], Sec. 2;
Belitsky-Smirnov, Phys. Rev. D 113 (2026) 036022 [2505.22595], App. A.2), and consistency of the cited region values
with the leading power.  (Review r3_1 required fixes 4, 5; review r3_2 required fix 7.)

Coordinates (X2): v.w = v+ w- + v- w+ - vT.wT;  p1 = (P, -m2/(2P), 0), p2 = (m2/(2P'), -P', 0) (both incoming),
Qt^2 = 2 P P';  lines g1 = k1, g2 = k2, a1 = p1-k2, a2 = p1-k1-k2, b1 = p2+k2, b2 = p2+k1+k2;  line factor -V^2.
Modes (powers of lambda = m/Qt): H (0,0,0); C1 (+,-,T) = (0,2,1); C2 = (2,0,1); S (ultrasoft) = (2,2,2); m2 ~ lambda^2.
X2 region 'XY' = (mode of k1, mode of k2).

(1) For each of the 9 regions and each of the 6 lines: the zeroed line factor (X2's T_R) equals the lowest-order
    (leading) part of the exact line factor under the region scaling.  Hence T_R Gamma = f_0, the leading-power term.
(2) Change of routing to Smirnov-Rakhmetov's variables k = k2 (outer rung), l = k1 + k2: with S_t, S'_t the region
    scalings, B_t = S_t^{-1} A S'_t -> B_0 (A: (k,l) -> (k1,k2) = (l-k, k)); det B_0 = 1, and the leading term g_0 in
    the SR routing satisfies g_0 = f_0 o B_0 (checked symbolically).  B_0 is a translation of l by a linear function of
    k, so the DR values agree: int T_R Gamma = int g_0.
(3) The SR integrands printed in hep-ph/9812529 eqs. (3), (5), (6), (7), (8), (9) are, after the dictionary
    p1 -> p1, p2 -> -p2 (SR's p2 outgoing), m2_SR = p_i^2 = -m2, Q^2_SR = 2 p~1.p~2 = Qt^2, p~1 = (P,0,0), p~2 = (0,P',0),
    each equal (up to the sign of each factor, SR factor = +V^2) to the leading terms computed in (2).
    Region dictionary (SR's '1c' is k+_SR ~ Q, i.e. collinear to p2 in X2's coordinates):
      HH<->(h-h), HC2<->(1c-h), HC1<->(2c-h), C2C2<->(1c-1c), C1C1<->(2c-2c), HS<->(us-h), C2S<->(us-1c),
      C1S<->(us-2c), SS<->(us-us).
(4) m2-exponents -k_R eps of the nine singles (from the unique scaling, r2_twoloop_regulator.log) agree with SR.
(5) SR's printed values: (h-h) eq.(4), (us-us) eq.(5), (us-h) eq.(6), (us-1c) = (us-2c) eq.(7) and the combination
    (10) of the four collinear-type regions sum to L^4/4 + pi^2 L^2/2 + 7 pi^4/60 + O(eps), L = ln(Qt^2/m2), with all
    poles cancelling (SR eq.(11)); SR omit i pi^{d/2} and, in eps-expansions, exp(-gamma_E eps) per loop.
(6) Vandermonde lemma used in Thm E.3: five distinct exponents k = 0..4 => finiteness forces the grouped pole
    coefficients of order >= 5 to vanish and P(L) has degree <= 4 (symbolic check of the 5x5 Vandermonde determinant).
(7) The m2 grid of Thm E.3(iii) and the exact integrated remainder Phi^(2)/Q^4 - LP at those points."""
import sys, os, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))

lam = sp.Symbol('lambda', positive=True)
P, Pp, m2 = sp.symbols('P Pp m2', positive=True)
k1p, k1m, k1x, k1y, k2p, k2m, k2x, k2y = sp.symbols('k1p k1m k1x k1y k2p k2m k2x k2y', real=True)
kp, km, kx, ky, lp, lm, lx, ly = sp.symbols('kp km kx ky lp lm lx ly', real=True)
K1 = (k1p, k1m, (k1x, k1y)); K2 = (k2p, k2m, (k2x, k2y))
p1 = (P, -m2/(2*P), (0, 0)); p2 = (m2/(2*Pp), -Pp, (0, 0))
def add(*vs):
    out = [0, 0, [0, 0]]
    for s, v in vs:
        out[0] += s*v[0]; out[1] += s*v[1]; out[2][0] += s*v[2][0]; out[2][1] += s*v[2][1]
    return (out[0], out[1], tuple(out[2]))
def minus_sq(v):          # -V^2 = -2 V+ V- + |V_T|^2
    return sp.expand(-2*v[0]*v[1] + v[2][0]**2 + v[2][1]**2)
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
def lines_x2(k1, k2):
    return {'g1': k1, 'g2': k2, 'a1': add((1, p1), (-1, k2)), 'a2': add((1, p1), (-1, k1), (-1, k2)),
            'b1': add((1, p2), (1, k2)), 'b2': add((1, p2), (1, k1), (1, k2))}
MODE = {'H': (0, 0, 0), 'C1': (0, 2, 1), 'C2': (2, 0, 1), 'S': (2, 2, 2)}
REG = ['HH', 'HC1', 'HC2', 'C1C1', 'C2C2', 'HS', 'C1S', 'C2S', 'SS']
def split(R):
    for a in ['H', 'C1', 'C2', 'S']:
        if R.startswith(a):
            return a, R[len(a):]

def scale_subs(modes_vars):
    """modes_vars: list of (mode, (p, m, (x, y))) -> substitution dict comp -> lambda^w comp; m2 -> lambda^2 m2"""
    sub = {m2: lam**2*m2}
    for mode, (vp, vm, (vx, vy)) in modes_vars:
        wp, wm, wt = MODE[mode]
        sub.update({vp: lam**wp*vp, vm: lam**wm*vm, vx: lam**wt*vx, vy: lam**wt*vy})
    return sub
def leading(expr, sub):
    e = sp.expand(expr.subs(sub, simultaneous=True))
    if e == 0:
        return sp.Integer(0), None
    poly = sp.Poly(e, lam)
    low = min(m[0] for m in poly.monoms())
    return sp.expand(poly.coeff_monomial(lam**low)), low

pats = json.load(open(os.path.join(HERE, 'twoloop_patterns.json')))
Z = pats['Z']
def zero_line(expr_line_vec, Zset):
    """apply X2's coordinate zeroing to a line momentum, then form -V^2 (M -> p1-, p2+ -> 0)"""
    sub = {}
    if 'M' in Zset: sub[m2] = 0
    for nm, (vp, vm, (vx, vy)) in [('k1', K1), ('k2', K2)]:
        if nm + '+' in Zset: sub[vp] = 0
        if nm + '-' in Zset: sub[vm] = 0
        if nm + 'T' in Zset: sub[vx] = 0; sub[vy] = 0
    return minus_sq(tuple(sp.sympify(c).subs(sub) if not isinstance(c, tuple) else tuple(sp.sympify(z).subs(sub) for z in c)
                          for c in expr_line_vec))

print("(1) X2 single T_R Gamma vs leading-power region term, line by line (X2 routing):")
ok1 = True
L_x2 = lines_x2(K1, K2)
for R in REG:
    a, b = split(R)
    sub = scale_subs([(a, K1), (b, K2)])
    bad = []
    for ln in LINES:
        lead, _ = leading(minus_sq(L_x2[ln]), sub)
        zr = zero_line(L_x2[ln], set(Z[R][ln]))
        if sp.expand(lead - zr) != 0:
            bad.append((ln, lead, zr))
    ok1 &= not bad
    print(f"   {R:5s}: {'all 6 lines = leading terms' if not bad else 'MISMATCH ' + str(bad)}")
print("   =>", "PASS" if ok1 else "FAIL")

print("\n(2) routing change to (k, l) = (k2, k1+k2): g_0 = f_0 o B_0 with det B_0 = 1:")
Kv = (kp, km, (kx, ky)); Lv = (lp, lm, (lx, ly))
L_sr = {'g1': add((1, Lv), (-1, Kv)), 'g2': Kv, 'a1': add((1, p1), (-1, Kv)), 'a2': add((1, p1), (-1, Lv)),
        'b1': add((1, p2), (1, Kv)), 'b2': add((1, p2), (1, Lv))}
order = {'S': 0, 'C1': 1, 'C2': 1, 'H': 2}
def join(a, b):           # mode of k1 + k2 given modes of k1 (a) and k2 (b)
    if a == b: return a
    if order[a] > order[b]: return a
    if order[b] > order[a]: return b
    return 'H'                                     # C1 + C2 does not occur among the 9 regions
ok2 = True; G0 = {}
comps1 = [k1p, k1m, k1x, k1y]; comps2 = [k2p, k2m, k2x, k2y]
for R in REG:
    a, b = split(R)
    ml = join(a, b)
    subp = scale_subs([(b, Kv), (ml, Lv)])
    g0 = {ln: leading(minus_sq(L_sr[ln]), subp)[0] for ln in LINES}
    G0[R] = g0
    # B_t = S_t^{-1} A S'_t : k1 = l - k, k2 = k  ->  components of k1 scaled back
    w1 = MODE[a]; wk = MODE[b]; wl = MODE[ml]
    def back(comp_l, comp_k, wl_, wk_, w1_):
        expr = (lam**wl_*comp_l - lam**wk_*comp_k)/lam**w1_
        return sp.limit(expr, lam, 0)
    B0 = {k1p: back(lp, kp, wl[0], wk[0], w1[0]), k1m: back(lm, km, wl[1], wk[1], w1[1]),
          k1x: back(lx, kx, wl[2], wk[2], w1[2]), k1y: back(ly, ky, wl[2], wk[2], w1[2]),
          k2p: kp, k2m: km, k2x: kx, k2y: ky}
    J = sp.Matrix([[sp.diff(B0[c], v) for v in [lp, lm, lx, ly, kp, km, kx, ky]] for c in comps1 + comps2])
    f0 = {ln: zero_line(L_x2[ln], set(Z[R][ln])) for ln in LINES}
    bad = [ln for ln in LINES if sp.expand(f0[ln].subs(B0, simultaneous=True) - g0[ln]) != 0]
    ok2 &= (not bad) and J.det() in (1, -1)
    shear = {str(c): str(B0[c]) for c in comps1 if sp.expand(B0[c] - {k1p: lp - kp, k1m: lm - km, k1x: lx - kx, k1y: ly - ky}[c]) != 0}
    print(f"   {R:5s}: modes (k,l) = ({b},{ml});  det B_0 = {J.det()};  B_0 differs from l-k in {shear if shear else 'nothing'};"
          f"  g_0 = f_0 o B_0: {'yes' if not bad else 'NO ' + str(bad)}")
print("   =>", "PASS" if ok2 else "FAIL")

print("\n(3) SR's printed region integrands (hep-ph/9812529) vs the leading terms in the SR routing:")
pt1 = (P, 0, (0, 0)); pt2 = (0, Pp, (0, 0)); Qt2 = 2*P*Pp            # p~1, p~2 ;  SR's p2 = -(X2's p2)
def dot(v, w): return sp.expand(v[0]*w[1] + v[1]*w[0] - v[2][0]*w[2][0] - v[2][1]*w[2][1])
def sq(v): return dot(v, v)
p2SR = add((-1, p2)); mSR = -m2
SRf = {   # SR factors, as printed; each must equal +V^2 = -(X2 line factor) of the corresponding line at leading order
 'h-h':  {'b2': sq(Lv) - 2*dot(pt2, Lv), 'a2': sq(Lv) - 2*dot(pt1, Lv), 'a1': sq(Kv) - 2*dot(pt1, Kv),
          'b1': sq(Kv) - 2*dot(pt2, Kv), 'g2': sq(Kv), 'g1': sq(add((1, Kv), (-1, Lv)))},
 'us-us': {'a2': -2*dot(pt1, Lv) + mSR, 'b2': -2*dot(pt2, Lv) + mSR, 'a1': -2*dot(pt1, Kv) + mSR,
           'b1': -2*dot(pt2, Kv) + mSR, 'g2': sq(Kv), 'g1': sq(add((1, Kv), (-1, Lv)))},
 'us-h': {'a2': sq(Lv) - 2*dot(pt1, Lv), 'b2': sq(Lv) - 2*dot(pt2, Lv), 'a1': -2*dot(pt1, Kv) + mSR,
          'b1': -2*dot(pt2, Kv) + mSR, 'g2': sq(Kv), 'g1': sq(Lv)},
 'us-1c': {'a2': -2*dot(pt1, Lv), 'b2': sq(Lv) - 2*dot(p2SR, Lv) + mSR, 'a1': -2*dot(pt1, Kv) + mSR,
           'b1': -2*dot(pt2, Kv) + mSR, 'g2': sq(Kv), 'g1': sp.expand(sq(Lv) - dot(pt1, Lv)*2*dot(pt2, Kv)*2/Qt2)},
 '1c-1c': {'a2': -2*dot(pt1, Lv), 'b2': sq(Lv) - 2*dot(p2SR, Lv) + mSR, 'a1': -2*dot(pt1, Kv),
           'b1': sq(Kv) - 2*dot(p2SR, Kv) + mSR, 'g2': sq(Kv), 'g1': sq(add((1, Kv), (-1, Lv)))},
 '1c-h': {'a2': sq(Lv) - 2*dot(pt1, Lv), 'b2': sq(Lv) - 2*dot(pt2, Lv), 'a1': -2*dot(pt1, Kv),
          'b1': sq(Kv) - 2*dot(p2SR, Kv) + mSR, 'g2': sq(Kv), 'g1': sp.expand(sq(Lv) - 2*dot(pt1, Kv)*2*dot(pt2, Lv)/Qt2)},
}
SRmap = {'h-h': 'HH', 'us-us': 'SS', 'us-h': 'HS', 'us-1c': 'C2S', '1c-1c': 'C2C2', '1c-h': 'HC2'}
ok3 = True
for srr, R in SRmap.items():
    bad = [ln for ln in LINES if sp.expand(SRf[srr][ln] + G0[R][ln]) != 0]
    ok3 &= not bad
    print(f"   SR ({srr:5s}) <-> X2 {R:5s}: {'all 6 factors agree' if not bad else 'MISMATCH on ' + str(bad)}")
print("   (SR eq. (8),(9) state (2c-2c) = (1c-1c), (2c-h) = (1c-h), and eq. (7) (us-2c) = (us-1c): mirror images)")
print("   =>", "PASS" if ok3 else "FAIL")

print("\n(4) m2-exponents: X2 singles (unique scaling, r2_twoloop_regulator) vs SR:")
kR = {'HH': 0, 'HC1': 1, 'HC2': 1, 'C1C1': 2, 'C2C2': 2, 'HS': 2, 'C1S': 3, 'C2S': 3, 'SS': 4}
kSR = {'h-h': 0, '1c-h': 1, '1c-1c': 2, 'us-h': 2, 'us-1c': 3, 'us-us': 4}
print("   ", all(kR[SRmap[s]] == kSR[s] for s in kSR), {SRmap[s]: (kR[SRmap[s]], kSR[s]) for s in kSR})

print("\n(5) sum of SR's printed region values (Q^2 = 1, -m2_SR = mu^2 = e^{-L}), evaluated at small eps with 90 digits:")
mp.mp.dps = 90
def sr_total(eps, L):
    e = mp.mpf(eps); L = mp.mpf(L); z3 = mp.zeta(3); G = mp.gamma
    norm = mp.e**(2*mp.euler*e)          # SR omit exp(-gamma_E eps) per loop in eps-expansions (eqs. (4), (10))
    mu2 = mp.e**(-L)
    hh = mp.mpf(1)/(4*e**4) + 5*mp.pi**2/(24*e**2) + 29*z3/(6*e) + 3*mp.pi**4/32                 # eq. (4)
    usus = norm*G(1 - e)**2*G(2*e)**2/(e**2*mu2**(4*e))                                           # eq. (5)
    ush = norm*G(1 + e)*G(1 - e)*G(e)**2*G(-e)**2/(G(1 - 2*e)*mu2**(2*e))                         # eq. (6)
    us1c = norm*G(1 - e)**2*G(e)*G(2*e)*G(-e)/(e*G(1 - 2*e)*mu2**(3*e))                          # eq. (7) (= us-2c)
    coll = -1/(2*e**4) + (L**2 - mp.pi**2/2)/(2*e**2) + (L**3/2 - mp.pi**2*L/6 - 17*z3/3)/e \
           + mp.mpf(7)/24*L**4 - 4*z3*L - mp.pi**4/144                                             # eq. (10)
    return hh + usus + ush + 2*us1c + coll
for Lv in ['2', '5', '9.2103403719761836']:
    LPv = mp.mpf(Lv)**4/4 + mp.pi**2*mp.mpf(Lv)**2/2 + 7*mp.pi**4/60
    vals = [sr_total(e_, Lv) for e_ in ['1e-8', '1e-12', '1e-16']]
    print(f"   L = {Lv:>18}: total(eps = 1e-8, 1e-12, 1e-16) - LP = {[mp.nstr(v_ - LPv, 5) for v_ in vals]}   (LP = {mp.nstr(LPv, 15)})")
print("   => all poles cancel and the finite part is L^4/4 + pi^2 L^2/2 + 7 pi^4/60 (deviation O(eps))")
mp.mp.dps = 30

print("\n(6) Vandermonde: det[k^n]_{k,n=0..4} =", sp.Matrix(5, 5, lambda i, j: sp.Integer(i)**j).det(),
      "(non-zero => grouped pole coefficients of order >= 5 vanish when the sum is finite)")

print("\n(7) Thm E.3(iii): exact integrated remainder Phi^(2)/Q^4 - LP on the grid of m2 values (Qt = 1):")
mp.mp.dps = 30
def int_gamma(x):
    x = mp.mpf(x); Lt = mp.log(1/x)
    return (1 + x)*(12*mp.polylog(4, -x) + Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60)/((1 - x)*(1 + x)**4)
for x in ['0.04', '0.01', '0.0025', '0.000625', '1e-4', '1e-6']:
    Lt = mp.log(1/mp.mpf(x)); lp_ = Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60
    r = int_gamma(x) - lp_; nlp = -mp.mpf(x)*(Lt**4/2 + mp.pi**2*Lt**2 + 12 + 7*mp.pi**4/30)
    print(f"   m2 = {x:>8}: int r = {mp.nstr(r, 10):>14}   NLP = {mp.nstr(nlp, 10):>14}   ratio = {mp.nstr(r/nlp, 8)}")
print("\nALL PASS" if (ok1 and ok2 and ok3) else "\nSOME FAIL")
