"""X2 final2 / f2_E4_singles.py -- Prop E.4 (discharge of (RA1), (RA2) for the nine single-approximator terms of the
two-loop planar off-shell vertex), part (d): closed forms with independent analytic powers, obtained by direct
integration of the Schwinger representation built from the EXACT polynomials U, F of f2_twoloop_polytopes.py, their
convergence/overlap domains, and their delta -> 0 limits compared with Smirnov-Rakhmetov hep-ph/9812529 eqs. (5)-(9).

Conventions.  Lines g1=k1, g2=k2, a1=p1-k2, a2=p1-k1-k2, b1=p2+k2, b2=p2+k1+k2; line factor -V^2 with X2's coordinate
zeroing; powers a_l = 1 + delta_l; d/2 = 2 - eps; Qt2 = 2 P P'.  Schwinger representation (definition of the value,
X2 §1.4 items 2 and 4):  I_R = (1/prod Gamma(a_l)) int_{R_+^6} x^{a-1} U^{-d/2} exp(-F/U) dx, with U = det M / 4,
F = U * (stationary value of sum_l x_l D_l) [M as in f2_twoloop_polytopes.py].  It equals the Lee-Pomeransky form
Gamma(d/2)/(Gamma(3d/2-|a|) prod Gamma(a_l)) int x^{a-1} (U+F)^{-d/2} dx wherever both converge (0 < w < d/2,
w = |a| - d).  Every step below is a Tonelli exchange of a NON-NEGATIVE integrand plus an elementary Gamma/Beta integral.

Checks printed: (0) U, F of each single = polynomials of f2_twoloop_polytopes.py divided by 4, with det M = 4 det A_T
(the light-cone and transverse Gaussians combine into U^{-d/2}); mirror symmetry HC2<->HC1, C2C2<->C1C1, C2S<->C1S;
(1) the algebraic decompositions used for SS, HS, C1S, HC1, C1C1 (exact sympy identities); (2) the closed forms and
their delta = 0 limits vs SR eqs. (5), (6), (7) (exact), HC1 at delta = 0 in closed Gamma form; (3) a rational point
of the derivation domain intersected with the Lee-Pomeransky convergence domain (exact; also checked against the facet
inequalities of f2_twoloop_polytopes.json); (4) numerical cross-checks of the two-dimensional representations of HC1
and C1C1 against reduced three-dimensional integrals at a point with delta != 0."""
import sys, os, json, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import functools
print = functools.partial(print, flush=True)
import f2_twoloop_polytopes as TP

LINES = TP.LINES
xg1, xg2, xa1, xa2, xb1, xb2 = TP.X
XV = dict(zip(LINES, TP.X))
P, Pp, m2 = TP.P, TP.Pp, TP.m2
Qt2 = sp.Symbol('Qt2', positive=True)
eps = sp.Symbol('epsilon')
dl = {ln: sp.Symbol('d_' + ln) for ln in LINES}
a = {ln: 1 + dl[ln] for ln in LINES}
h = 2 - eps                                                  # d/2
G = sp.gamma
def B(x, y): return G(x)*G(y)/G(x + y)
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

# ---------------------------------------------------------------- (0) U, F and the transverse check
def transverse_matrix(factors):
    S = sp.expand(sum(x*f for x, f in zip(TP.X, factors)))
    k1x, k2x = TP.COMP[2], TP.COMP[6]
    A11 = sp.diff(S, k1x, 2)/2; A22 = sp.diff(S, k2x, 2)/2; A12 = sp.diff(S, k1x, k2x)/2
    return sp.Matrix([[A11, A12], [A12, A22]])

Z = TP.PAT['Z']
SINGLES = ['HH', 'HC1', 'HC2', 'C1C1', 'C2C2', 'HS', 'C1S', 'C2S', 'SS']
UF = {}
print("(0) parametric polynomials of the nine singles")
for R in SINGLES:
    fac = [TP.line_factor(ln, Z[R][ln]) for ln in LINES]
    U4, F4, M = TP.UF(fac)
    AT = transverse_matrix(fac)
    ok_t = sp.expand(M.det() - 4*AT.det()) == 0
    Up = sp.expand(U4/4); Fp = sp.expand(sp.factor(F4)/4)
    UF[R] = (Up, sp.expand(Fp.subs(Pp, Qt2/(2*P))))
    report(f"{R}: det M = 4 det A_T (single power U^(-d/2)); U = {sp.factor(Up)}", ok_t)
mir = {xa1: xb1, xb1: xa1, xa2: xb2, xb2: xa2}
for R1, R2 in [('HC1', 'HC2'), ('C1C1', 'C2C2'), ('C1S', 'C2S')]:
    okU = sp.expand(UF[R1][0].xreplace(mir) - UF[R2][0]) == 0
    okF = sp.expand(UF[R1][1].xreplace(mir) - UF[R2][1]) == 0
    report(f"mirror: U_{R2}, F_{R2} = U_{R1}, F_{R1} with x_a <-> x_b", okU and okF)
for R in SINGLES:
    print(f"   {R}: F = {sp.factor(UF[R][1])}")

# ---------------------------------------------------------------- (1)+(2) decompositions and closed forms
print("\n(1)-(2) decompositions (exact) and closed forms")
CF = {}       # closed forms R(eps, delta) (Gamma products) -- or (prefactor, 2D-integrand, variables)
COND = {}     # derivation-domain conditions (strict positivity of these real parts)
SR = {}       # SR's printed values (exact Gamma forms), our normalization Qt2, m2 > 0 (SR: -m2_SR = m2, Q2_SR = Qt2)
SR['SS'] = G(1 - eps)**2*G(2*eps)**2/(eps**2*m2**(4*eps)*Qt2**(2 - 2*eps))                       # SR (5)
SR['HS'] = G(1 + eps)*G(1 - eps)*G(eps)**2*G(-eps)**2/(G(1 - 2*eps)*m2**(2*eps)*Qt2**2)          # SR (6)
SR['C1S'] = G(1 - eps)**2*G(eps)*G(2*eps)*G(-eps)/(eps*G(1 - 2*eps)*m2**(3*eps)*Qt2**(2 - eps))  # SR (7)

# --- SS: U = xg1 xg2 (monomial)
U, F = UF['SS']
ok = sp.expand(U - xg1*xg2) == 0 and sp.simplify(F/U - (Qt2*((xa1 + xa2)*(xb1 + xb2)/xg2 + xa2*xb2/xg1)
                                                      + m2*(xa1 + xa2 + xb1 + xb2))) == 0
report("SS: U = x_g1 x_g2,  F/U = Qt2[(x_a1+x_a2)(x_b1+x_b2)/x_g2 + x_a2 x_b2/x_g1] + m2(x_a1+x_a2+x_b1+x_b2)", ok)
Aa = a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*h; Bb = a['b1'] + a['b2'] + a['g1'] + a['g2'] - 2*h
CF['SS'] = (G(h - a['g1'])*G(h - a['g2'])*Qt2**(a['g1'] + a['g2'] - 2*h)*G(Aa)*G(Bb)*m2**(-Aa - Bb)
            *B(a['a1'], a['a2'] + a['g1'] - h)*B(a['b1'], a['b2'] + a['g1'] - h)/sp.Mul(*[G(a[l]) for l in LINES]))
COND['SS'] = [h - a['g1'], h - a['g2'], Aa, Bb, a['a1'], a['a2'] + a['g1'] - h, a['b1'], a['b2'] + a['g1'] - h]

# --- HS: product of the massless on-shell triangle (g1, a2, b2) and the soft integral (g2, a1, b1)
U, F = UF['HS']
U1 = xg1 + xa2 + xb2
ok = sp.expand(U - xg2*U1) == 0 and sp.simplify(F/U - (Qt2*xa2*xb2/U1 + Qt2*xa1*xb1/xg2 + m2*(xa1 + xb1))) == 0
report("HS: U = x_g2 (x_g1+x_a2+x_b2),  F/U = Qt2 x_a2 x_b2/U_1 + Qt2 x_a1 x_b1/x_g2 + m2(x_a1+x_b1)  (factorizes)", ok)
N1 = a['g1'] + a['a2'] + a['b2']
T0 = G(N1 - h)*G(h - a['g1'] - a['b2'])*G(h - a['g1'] - a['a2'])/(G(a['a2'])*G(a['b2'])*G(2*h - N1))*Qt2**(h - N1)
S2 = (G(h - a['g2'])*G(a['a1'] + a['g2'] - h)*G(a['b1'] + a['g2'] - h)/(G(a['g2'])*G(a['a1'])*G(a['b1']))
      *Qt2**(a['g2'] - h)*m2**(2*h - 2*a['g2'] - a['a1'] - a['b1']))
CF['HS'] = T0*S2
COND['HS'] = [N1 - h, h - a['g1'] - a['b2'], h - a['g1'] - a['a2'], a['g1'], a['a2'], a['b2'],
              h - a['g2'], a['a1'] + a['g2'] - h, a['b1'] + a['g2'] - h]

# --- C1S
U, F = UF['C1S']
sig = xa2 + xg1; Xeff = xa1 + xa2*xg1/sig
ok = (sp.expand(U - xg2*sig) == 0 and
      sp.simplify(F/U - (Qt2*xb1*Xeff/xg2 + Qt2*xa2*xb2/sig + m2*(Xeff + xb1))) == 0)
report("C1S: U = x_g2 sigma (sigma = x_a2+x_g1),  F/U = Qt2 x_b1 X/x_g2 + Qt2 x_a2 x_b2/sigma + m2 (X + x_b1),"
       "  X = x_a1 + x_a2 x_g1/sigma", ok)
CF['C1S'] = (G(a['b2'])*G(h - a['g2'])*G(a['b1'] + a['g2'] - h)*B(a['a2'] + a['g1'] - h, a['a1'])
             *G(a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*h)*B(h - a['g1'] - a['b2'], h - a['a2'])
             *Qt2**(a['g2'] - h - a['b2'])*m2**(-(a['b1'] + a['g2'] - h) - (a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*h))
             /sp.Mul(*[G(a[l]) for l in LINES]))
COND['C1S'] = [a['b2'], h - a['g2'], a['b1'] + a['g2'] - h, a['a2'] + a['g1'] - h, a['a1'],
               a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*h, h - a['g1'] - a['b2'], h - a['a2'], a['a2'], a['g1']]

for R in ['SS', 'HS', 'C1S']:
    lim = sp.gammasimp(CF[R].subs({dl[l]: 0 for l in LINES}))
    report(f"{R}: delta = 0 limit of the closed form = SR's printed value (eq. {dict(SS=5, HS=6, C1S=7)[R]})",
           sp.simplify(sp.gammasimp(lim/SR[R]) - 1) == 0)
    print(f"      {R}(eps, delta) = {CF[R]}")

# --- HC1: U = (x_a1 + x_g2)(x_g1 + x_a2 + x_b2)
U, F = UF['HC1']
U2 = xa1 + xg2; U1 = xg1 + xa2 + xb2
ok = (sp.expand(U - U2*U1) == 0 and
      sp.expand(F - (Qt2*(xa1*xb1*U1 + xb2*(xa1*xa2 + xa1*xg1 + xa2*xg2)) + m2*xa1*xg2*U1)) == 0)
z_, w_ = sp.symbols('z w', positive=True)
Lam = sp.Symbol('Lam', positive=True)
ok2 = sp.expand((xa1*xa2 + xa1*xg1 + xa2*xg2).xreplace({xa1: Lam*z_, xg2: Lam*(1 - z_)}) - Lam*(xa2 + z_*xg1)) == 0
report("HC1: U = (x_a1+x_g2)(x_g1+x_a2+x_b2),  F = Qt2[x_a1 x_b1 U_1 + x_b2(x_a1 x_a2 + x_a1 x_g1 + x_a2 x_g2)] + m2 x_a1 x_g2 U_1;"
       "  with x_a1 = U_2 z, x_g2 = U_2(1-z): x_a1 x_a2 + x_a1 x_g1 + x_a2 x_g2 = U_2 (x_a2 + z x_g1)", ok and ok2)
N1 = a['g1'] + a['a2'] + a['b2']
pref_HC1 = (G(a['a1'] + a['g2'] - h)*G(N1 - h)*B(h - a['b2'], h - a['g1'] - a['a2'])
            /(G(a['g2'])*G(a['a1'])*G(a['g1'])*G(a['a2'])*G(a['b2']))*Qt2**(-a['b1'] + h - N1)*m2**(h - a['a1'] - a['g2']))
dens_HC1 = (z_**(h - a['b1'] - a['g2'] - 1)*(1 - z_)**(h - a['a1'] - 1)*w_**(a['a2'] - 1)*(1 - w_)**(a['g1'] - 1)
            *(w_ + z_ - z_*w_)**(h - N1))
CF['HC1'] = (pref_HC1, dens_HC1, (z_, w_))
# derivation domain: b1 integral, U_2-scale integral, triangle Feynman steps, and absolute convergence of the 2D integral
COND['HC1'] = [a['b1'], a['a1'] + a['g2'] - h, N1 - h, h - a['b2'], h - a['g1'] - a['a2'], a['a1'], a['g2'],
               # 2D integral: w^(a_a2-1), (1-w)^(a_g1-1), z^(h-a_b1-a_g2-1), (1-z)^(h-a_a1-1), corner
               a['a2'], a['g1'], h - a['b1'] - a['g2'], h - a['a1'], a['a2'] + (h - a['b1'] - a['g2']) - (N1 - h)]
COND2D_HC1 = [a['a2'], a['g1'], h - a['b1'] - a['g2'], h - a['a1'], a['a2'] + (h - a['b1'] - a['g2']) - (N1 - h)]

# --- C1C1: U = A_1 + x_g2 (x_a2 + x_g1)
U, F = UF['C1C1']
A1 = xa1*xa2 + xa1*xg1 + xa2*xg1; A2 = A1 + xa2*xg2
ok = (sp.expand(U - (A1 + xg2*(xa2 + xg1))) == 0 and
      sp.expand(F - (Qt2*(xb1*A1 + xb2*A2) + m2*xg2*A1)) == 0)
sg, y_, Xs = sp.symbols('sigma y X', positive=True)
subs_in = {xa2: sg*y_, xg1: sg*(1 - y_), xa1: Xs - sg*y_*(1 - y_)}
ok2 = (sp.expand(A1.subs(subs_in) - sg*Xs) == 0 and sp.expand(U.subs(subs_in) - sg*(Xs + xg2)) == 0
       and sp.expand(A2.subs(subs_in) - sg*(Xs + y_*xg2)) == 0)
report("C1C1: U = A_1 + x_g2 sigma, F = Qt2 (x_b1 A_1 + x_b2 A_2) + m2 x_g2 A_1 (A_1 = x_a1 x_a2 + x_a1 x_g1 + x_a2 x_g1,"
       " A_2 = A_1 + x_a2 x_g2);  with x_a2 = sigma y, x_g1 = sigma(1-y), X = x_a1 + sigma y(1-y): A_1 = sigma X,"
       " U = sigma (X + x_g2), A_2 = sigma (X + y x_g2)", ok and ok2)
bpp = a['a1'] + a['g1'] + a['a2'] - h
pref_C1C1 = (G(a['g1'] + a['a2'] - h)*G(a['g2'] + bpp - h)/(G(a['g1'])*G(a['a2'])*G(a['g2'])*G(bpp))
             *Qt2**(-a['b1'] - a['b2'])*m2**(h - a['g2'] - bpp))
dens_C1C1 = (y_**(h - a['g1'] - 1)*(1 - y_)**(h - a['a2'] - 1)*z_**(h - a['g2'] - a['b1'] - 1)*(1 - z_)**(h - bpp - 1)
             *(z_ + y_ - y_*z_)**(-a['b2']))
CF['C1C1'] = (pref_C1C1, dens_C1C1, (y_, z_))
COND['C1C1'] = [a['b1'], a['b2'], a['g1'] + a['a2'] - h, a['a1'], a['g2'] + bpp - h, a['g1'], a['a2'], a['g2'],
                h - a['g1'], h - a['a2'], h - a['g2'] - a['b1'], h - bpp,
                (h - a['g1']) + (h - a['g2'] - a['b1']) - a['b2']]
COND2D_C1C1 = [h - a['g1'], h - a['a2'], h - a['g2'] - a['b1'], h - bpp, (h - a['g1']) + (h - a['g2'] - a['b1']) - a['b2']]

d0 = {dl[l]: 0 for l in LINES}
print("\n   HC1 and C1C1 at delta = 0:")
print("      HC1  = ", sp.simplify(pref_HC1.subs(d0)), " x int int ", sp.simplify(dens_HC1.subs(d0)), " dz dw")
print("      C1C1 = ", sp.simplify(pref_C1C1.subs(d0)), " x int int ", sp.simplify(dens_C1C1.subs(d0)), " dy dz")
for nm, cl in [('HC1', COND2D_HC1), ('C1C1', COND2D_C1C1)]:
    print(f"      2D-integral convergence conditions at delta = 0 (all > 0): {[sp.simplify(c.subs(d0)) for c in cl]}")
# HC1 at delta = 0 in closed form: the w-integral is elementary, then two Beta functions
Jw = sp.integrate((w_ + z_ - z_*w_)**(-1 - sp.Symbol('e', negative=True)), (w_, 0, 1))
HC1_0 = (G(eps)*G(1 + eps)*G(1 - eps)*G(-eps)/G(1 - 2*eps)*Qt2**(-2 - eps)*m2**(-eps)
         *(B(-2*eps, -eps) - B(-eps, -eps))/eps)
print("      HC1(eps, 0) = Gamma(eps)Gamma(1+eps)Gamma(1-eps)Gamma(-eps)/Gamma(1-2eps) Qt2^(-2-eps) m2^(-eps)"
      " [B(-2eps,-eps) - B(-eps,-eps)]/eps   (valid as written for -1/2 < eps < 0)")
mp.mp.dps = 30
for ev in ['-0.15', '-0.3', '-0.42']:
    e_ = mp.mpf(ev)
    f2d = lambda z, w: z**(-1 - e_)*(1 - z)**(-e_)*(w + z - z*w)**(-1 - e_)
    pz = 2/(-e_)                                    # z = t^pz removes the z^(-1-eps) endpoint singularity
    g2d = lambda t: (lambda z: pz*t**(pz - 1)*mp.quad(lambda w: f2d(z, w), [0, z, 1]))(t**pz)
    v2d = mp.quad(g2d, [0, mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), 1])
    vcf = (mp.beta(-2*e_, -e_) - mp.beta(-e_, -e_))/e_
    report(f"HC1 2D integral at delta = 0 equals [B(-2e,-e) - B(-e,-e)]/e at eps = {ev}: {mp.nstr(v2d, 18)} vs "
           f"{mp.nstr(vcf, 18)}", abs(v2d/vcf - 1) < mp.mpf('1e-10'))

# ---------------------------------------------------------------- (3) overlap points (exact rationals)
print("\n(3) a rational point in (derivation domain) x (Lee-Pomeransky convergence domain), checked exactly")
POLY = json.load(open(os.path.join(os.path.dirname(HERE), 'final2_logs', 'f2_twoloop_polytopes.json')))
def facet_ok(R, pt):
    """BFP Thm 2.2 criterion <mu, a> > nu (d/2) for every facet of Newt(U+F), at the rational point"""
    ev = Fr(pt['eps']); hv = 2 - ev
    av = [1 + Fr(pt[l]) for l in LINES]
    for mu_s, nu in POLY[R]['facets'].items():
        mu = [int(t) for t in mu_s.strip('()').split(',')]
        if not sum(m_*a_ for m_, a_ in zip(mu, av)) > nu*hv: return False
    return True
grid_e = [Fr(k, 20) for k in range(-9, 10) if k != 0]
grid_d = [Fr(k, 10) for k in range(-6, 7)]
def margin_point(R, conds, need=0.2):
    """grid point maximizing the minimal margin of (derivation conditions, w, d/2 - w); exact re-check"""
    syms = [eps] + [dl[l] for l in LINES]
    w_expr = sum(a[l] for l in LINES) - 2*h
    allc = list(conds) + [w_expr, h - w_expr]
    fns = [sp.lambdify(syms, c, 'math') for c in allc]
    best = None
    ge = [Fr(k, 20) for k in range(-9, 10) if k != 0]; gd = [Fr(k, 10) for k in range(-8, 9)]
    for ev in ge:
        for nz in range(0, 4):
            for idx in itertools.combinations(range(6), nz):
                for vals in itertools.product(gd, repeat=nz):
                    if any(v == 0 for v in vals): continue
                    dv = [Fr(0)]*6
                    for i, v in zip(idx, vals): dv[i] = v
                    num = [float(ev)] + [float(x) for x in dv]
                    mn = min(f(*num) for f in fns)
                    if best is None or mn > best[0] + 1e-12:
                        best = (mn, ev, dv)
    mn, ev, dv = best
    pt = {'eps': ev, **{l: x for l, x in zip(LINES, dv)}}
    sub = {eps: sp.Rational(ev.numerator, ev.denominator)}
    sub.update({dl[l]: sp.Rational(x.numerator, x.denominator) for l, x in zip(LINES, dv)})
    exact_ok = all(sp.nsimplify(c.subs(sub)) > 0 for c in allc) and facet_ok(R, pt)
    return pt, mn, exact_ok
def find_point(R, conds, extra_lp=True):
    syms = [eps] + [dl[l] for l in LINES]
    fns = [sp.lambdify(syms, c, 'math') for c in conds]
    w_expr = sum(a[l] for l in LINES) - 2*h
    best = None
    # structured search: eps on a grid, deltas on a coarse grid with few non-zero entries
    for ev in grid_e:
        for nz in range(0, 4):
            for idx in itertools.combinations(range(6), nz):
                for vals in itertools.product(grid_d, repeat=nz):
                    if any(v == 0 for v in vals): continue
                    dv = [Fr(0)]*6
                    for i, v in zip(idx, vals): dv[i] = v
                    num = [float(ev)] + [float(x) for x in dv]
                    if not all(f(*num) > 1e-12 for f in fns): continue
                    sub = {eps: sp.Rational(ev.numerator, ev.denominator)}
                    sub.update({dl[l]: sp.Rational(x.numerator, x.denominator) for l, x in zip(LINES, dv)})
                    if not all(sp.nsimplify(c.subs(sub)) > 0 for c in conds): continue
                    wv = w_expr.subs(sub); hv = h.subs(sub)
                    if extra_lp and not (0 < wv < hv): continue
                    pt = {'eps': ev, **{l: x for l, x in zip(LINES, dv)}}
                    if extra_lp and not facet_ok(R, pt): continue
                    return pt
    return None
POINTS = {}; MPOINTS = {}
for R in ['SS', 'HS', 'C1S', 'HC1', 'C1C1']:
    pt = find_point(R, COND[R])
    POINTS[R] = pt
    mpt, mn, ok_m = margin_point(R, COND[R])
    MPOINTS[R] = mpt
    report(f"{R}: max-margin grid point {({k: str(v) for k, v in mpt.items()})}: minimal margin {mn:.3f} "
           f"(derivation conditions, w, d/2 - w), exact re-check incl. facet inequalities", ok_m and mn > 0)
    report(f"{R}: point (eps, delta) = {({k: str(v) for k, v in pt.items()} if pt else None)} satisfies every derivation"
           f" condition, 0 < w < d/2, and all facet inequalities of Newt(U+F) (BFP Thm 2.2)", pt is not None)

# ---------------------------------------------------------------- (4) numerical cross-checks with delta != 0
print("\n(4) HC1, C1C1: two-dimensional representation vs a reduced three-dimensional integral (delta != 0)")
import numpy as np
def de_rule(hstep, tmax=3.3):
    """tanh-sinh nodes/weights on (0,1); returns x, 1-x (computed without cancellation), w"""
    t = np.arange(-tmax, tmax + 1e-12, hstep)
    s = np.pi*np.sinh(t)
    x = 1.0/(1.0 + np.exp(-s)); xm = 1.0/(1.0 + np.exp(s))
    w = hstep*(np.pi/2)*np.cosh(t)/(2*np.cosh(np.pi/2*np.sinh(t))**2)
    keep = (x > 1e-200) & (xm > 1e-200)
    return x[keep], xm[keep], w[keep]
def fl(pt, k): return float(Fr(pt[k]))
def eval_2d_np(R, pt, hstep):
    ev = fl(pt, 'eps'); hv = 2 - ev; av = {l: 1 + fl(pt, l) for l in LINES}; mm = 1/3.
    x, xm, w = de_rule(hstep)
    U1, U2 = np.meshgrid(x, x, indexing='ij'); M1, M2 = np.meshgrid(xm, xm, indexing='ij'); W = np.outer(w, w)
    if R == 'HC1':
        z, ww, zm, wm = U1, U2, M1, M2
        N1_ = av['g1'] + av['a2'] + av['b2']
        f = (z**(hv - av['b1'] - av['g2'] - 1)*zm**(hv - av['a1'] - 1)*ww**(av['a2'] - 1)*wm**(av['g1'] - 1)
             *(ww + z*wm)**(hv - N1_))
        from math import gamma as g
        pre = (g(av['a1'] + av['g2'] - hv)*g(N1_ - hv)*g(hv - av['b2'])*g(hv - av['g1'] - av['a2'])/g(2*hv - N1_)
               /(g(av['g2'])*g(av['a1'])*g(av['g1'])*g(av['a2'])*g(av['b2']))*mm**(hv - av['a1'] - av['g2']))
    else:
        y, z, ym, zm = U1, U2, M1, M2
        bpp_ = av['a1'] + av['g1'] + av['a2'] - hv
        f = (y**(hv - av['g1'] - 1)*ym**(hv - av['a2'] - 1)*z**(hv - av['g2'] - av['b1'] - 1)*zm**(hv - bpp_ - 1)
             *(z + y*zm)**(-av['b2']))
        from math import gamma as g
        pre = (g(av['g1'] + av['a2'] - hv)*g(av['g2'] + bpp_ - hv)/(g(av['g1'])*g(av['a2'])*g(av['g2'])*g(bpp_))
               *mm**(hv - av['g2'] - bpp_))
    return pre*np.sum(W*f)
def eval_3d_np(R, pt, hstep):
    ev = fl(pt, 'eps'); hv = 2 - ev; av = {l: 1 + fl(pt, l) for l in LINES}; mm = 1/3.
    x, xm, w = de_rule(hstep)
    T1, T2, T3 = np.meshgrid(x, x, x, indexing='ij'); S1, S2, S3 = np.meshgrid(xm, xm, xm, indexing='ij')
    W = w[:, None, None]*w[None, :, None]*w[None, None, :]
    from math import gamma as g
    if R == 'C1C1':
        e, ep = av['b2'], av['b1']; Nq = av['g1'] + av['g2'] + av['a1'] + av['a2']
        pre = g(e)*g(ep)*g(Nq - 2*hv)/np.prod([g(av[l]) for l in LINES])
        X2 = T1; A_ = S1*T2; Y2 = S1*S2*T3; X1 = S1*S2*S3; jac = S1**2*S2
        Uu = A_*Y2 + A_*X1 + Y2*X1 + X2*(Y2 + X1); a1_ = A_*Y2 + A_*X1 + Y2*X1; a2_ = a1_ + Y2*X2
        f = (jac*X1**(av['g1'] - 1)*X2**(av['g2'] - 1)*A_**(av['a1'] - 1)*Y2**(av['a2'] - 1)
             *Uu**(-hv + e + ep)*a1_**(-ep)*a2_**(-e)*(mm*X2*a1_/Uu)**(2*hv - Nq))
    else:
        N1_ = av['g1'] + av['a2'] + av['b2']
        pre = (g(av['a1'] + av['g2'] - hv)*g(N1_ - hv)/np.prod([g(av[l]) for l in ['g2', 'a1', 'g1', 'a2', 'b2']])
               *mm**(hv - av['a1'] - av['g2']))
        z, zm, t, tm, s, sm = T1, S1, T2, S2, T3, S3
        g1 = t*s; a2 = t*sm; b2 = tm
        F1 = b2*(a2 + z*g1)
        f = (z**(av['a1'] - 1 - av['b1'])*zm**(av['g2'] - 1)*(z*zm)**(hv - av['a1'] - av['g2'])
             *t*g1**(av['g1'] - 1)*a2**(av['a2'] - 1)*b2**(av['b2'] - 1)*F1**(hv - N1_))
    return pre*np.sum(W*f)
for R in ['HC1', 'C1C1']:
    pt = MPOINTS[R]
    v2 = [eval_2d_np(R, pt, hs) for hs in (0.05, 0.035)]
    v3 = [eval_3d_np(R, pt, hs) for hs in (0.07, 0.05)]
    rel = abs(v2[-1]/v3[-1] - 1)
    report(f"{R} at {({k: str(v) for k, v in pt.items()})}, Qt2 = 1, m2 = 1/3: 2D {v2[-1]:.10g} (step change "
           f"{abs(v2[-1]/v2[0]-1):.1e}) vs reduced 3D {v3[-1]:.10g} (step change {abs(v3[-1]/v3[0]-1):.1e}); rel {rel:.1e}",
           rel < 1e-4)

json.dump({'first': {R: {k: str(v) for k, v in pt.items()} for R, pt in POINTS.items()},
           'max_margin': {R: {k: str(v) for k, v in pt.items()} for R, pt in MPOINTS.items()}},
          open(os.path.join(os.path.dirname(HERE), 'final2_logs', 'f2_E4_points.json'), 'w'), indent=1)
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
