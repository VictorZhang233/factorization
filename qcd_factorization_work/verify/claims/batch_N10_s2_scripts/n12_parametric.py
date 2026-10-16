# N12 (stage 2): independent check of the off-shell triangle Collins subtraction terms and remainder
# METHOD (different from stage 1, which used k^- residues): covariant Schwinger/Cheng-Wu parametrization
#   1/(D_g X1 X2) = 2 int_0^inf da db (D_g + a X1 + b X2)^-3, all denominators with -i0,
# followed by the covariant d-dim Minkowski k-integral. Every term of r = Gamma - sum_R C_R Gamma has the
# form 1/(D_g X1 X2), so all terms live on the SAME (a,b) quadrant and can be combined pointwise.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""))

# ---------------- 1. kinematics and denominators (symbolic) ----------------
P, Pp, m, kp, km, kT2 = sp.symbols('P Pp m kp km kT2', positive=True)
def lc(a, b):  # light-cone product a=(a+,a-,aT2-placeholder): a.b = a+b- + a-b+ - aT.bT
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2]
# vectors as (plus, minus, transverse component along a fixed axis); k has generic transverse kT
kT = sp.symbols('kT', real=True)
p1 = (P, -m**2/(2*P), 0); p2 = (m**2/(2*Pp), -Pp, 0); k = (kp, km, kT)
sq = lambda a: lc(a, a)
Qt2 = 2*P*Pp
check("p1^2=-m^2", sp.simplify(sq(p1) + m**2) == 0)
check("p2^2=-m^2", sp.simplify(sq(p2) + m**2) == 0)
p12 = tuple(p1[i] + p2[i] for i in range(3))
Q2 = sp.simplify(-sq(p12))
check("Q^2=(Qt^2+m^2)^2/Qt^2", sp.simplify(Q2 - (Qt2 + m**2)**2/Qt2) == 0, str(sp.factor(Q2)))
Dg = -sq(k)
D1 = sp.expand(-sq(tuple(p1[i] - k[i] for i in range(3))))
D2 = sp.expand(-sq(tuple(p2[i] + k[i] for i in range(3))))
k2 = sq(k)
check("D1 = m^2+2P k^- -(m^2/P)k^+ - k^2", sp.simplify(D1 - (m**2 + 2*P*km - m**2/P*kp - k2)) == 0)
check("D2 = m^2+2P' k^+ -(m^2/P')k^- - k^2", sp.simplify(D2 - (m**2 + 2*Pp*kp - m**2/Pp*km - k2)) == 0)

# generic X1 = a1 + 2P k^- - b1 k^+ - c1 k^2 ; X2 = a2 + 2P' k^+ - b2 k^- - c2 k^2
# (a,b,c): D:(m^2, m^2/P, 1), e:(m^2,0,0), t:(0,0,1), h:(0,0,0)   [reference (D.1),(D.2)]
den1 = {'D': (m**2, m**2/P, 1), 'e': (m**2, 0, 0), 't': (0, 0, 1), 'h': (0, 0, 0)}
den2 = {'D': (m**2, m**2/Pp, 1), 'e': (m**2, 0, 0), 't': (0, 0, 1), 'h': (0, 0, 0)}
al, be = sp.symbols('alpha beta', positive=True)
def NC(x1, x2):
    a1, b1, c1 = den1[x1]; a2, b2, c2 = den2[x2]
    c = 1 + al*c1 + be*c2
    vp = al*P - be*b2/2          # coefficient of k^- in (a X1 + b X2)/2  -> v^+
    vm = be*Pp - al*b1/2         # coefficient of k^+                      -> v^-
    K = al*a1 + be*a2
    # D_g + a X1 + b X2 = -c k^2 + 2 v.k + K ;  after shift: -c k'^2 + (v^2/c + K), v^2 = 2 v^+ v^-
    # check the decomposition explicitly
    X1 = a1 + 2*P*km - b1*kp - c1*k2; X2 = a2 + 2*Pp*kp - b2*km - c2*k2
    lhs = sp.expand(Dg + al*X1 + be*X2)
    rhs = sp.expand(-c*k2 + 2*(vp*km + vm*kp) + K)
    assert sp.simplify(lhs - rhs) == 0
    N = sp.expand(2*vp*vm + c*K)  # = c*M
    return sp.simplify(c), sp.simplify(N)
# exact denominators reproduce D1, D2
check("X1(D)=D1", sp.simplify(den1['D'][0] + 2*P*km - den1['D'][1]*kp - den1['D'][2]*k2 - D1) == 0)
check("X2(D)=D2", sp.simplify(den2['D'][0] + 2*Pp*kp - den2['D'][1]*km - den2['D'][2]*k2 - D2) == 0)

# coefficient table of r = Gamma - C_S - C_C1 - C_C2 - C_H  [reference (D.26)]
#   Gamma=1/(Dg D1 D2); C_S=1/(Dg e1 e2); C_C1=(1/(Dg h2))(1/D1-1/e1); C_C2=(1/(Dg h1))(1/D2-1/e2);
#   C_H=(1/Dg)(1/t1-1/h1)(1/t2-1/h2)
terms = {'Gamma': {('D','D'): 1},
         'CS': {('e','e'): 1},
         'CC1': {('D','h'): 1, ('e','h'): -1},
         'CC2': {('h','D'): 1, ('h','e'): -1},
         'CH': {('t','t'): 1, ('h','t'): -1, ('t','h'): -1, ('h','h'): 1}}
tab = {}
for name, dct in terms.items():
    for (x1, x2), co in dct.items():
        tab[(x1, x2)] = NC(x1, x2)
        print("  %-6s (%s1,%s2) coeff %+d : c = %s ,  N = c*M = %s" % (name, x1, x2, co, tab[(x1,x2)][0], sp.factor(tab[(x1,x2)][1])))
# Gamma: N should be a b Q^2 + (a+b) m^2  (standard Feynman parametrization)
cG, NG = tab[('D','D')]
check("Gamma: N = ab Q^2 + (a+b)m^2", sp.simplify(NG - (al*be*Q2 + (al+be)*m**2)) == 0)
check("C_S: N = ab Qt^2 + (a+b)m^2", sp.simplify(tab[('e','e')][1] - (al*be*Qt2 + (al+be)*m**2)) == 0)
check("C_C1 (D,h): N = a(b Qt^2 + m^2)", sp.simplify(tab[('D','h')][1] - al*(be*Qt2 + m**2)) == 0)
check("C_H (t,t): N = ab Qt^2", sp.simplify(tab[('t','t')][1] - al*be*Qt2) == 0)

# ---------------- 2. (a) finite-eps values: see n12_finite_eps.py (cancellation-safe quadrature) ----------------

# ---------------- 3. (b) pole cancellation and finite part (sympy) ----------------
eps = sp.symbols('epsilon')
lQ, lm = sp.symbols('lQ lm', real=True)   # lQ = ln(mu^2/Qt^2), lm = ln(mu^2/m^2)
A = sp.gamma(1+eps)*sp.gamma(1-eps)**2/(eps**2*sp.gamma(1-2*eps))
B = sp.gamma(1+eps)**2*sp.gamma(1-eps)/eps**2
S = sp.exp(eps*lQ)*A - 2*sp.exp(eps*lm)*A + sp.exp(eps*(2*lm - lQ))*B
ser = sp.series(S, eps, 0, 1).removeO()
ser = sp.simplify(sp.expand(ser))
c2 = sp.simplify(ser.coeff(eps, -2)); c1 = sp.simplify(ser.coeff(eps, -1)); c0 = sp.simplify(ser.coeff(eps, 0))
check("eps^-2 coefficient = 0", c2 == 0, str(c2))
check("eps^-1 coefficient = 0", sp.simplify(c1) == 0, str(c1))
check("finite part = (lQ-lm)^2 + pi^2/3 = ln^2(Qt^2/m^2)+pi^2/3", sp.simplify(c0 - ((lQ - lm)**2 + sp.pi**2/3)) == 0, str(sp.factor(c0)))

# ---------------- 4. exact I and the d=4 remainder by the common-quadrant parametric integral ----------------
mp.mp.dps = 30
Pv, Ppv, m2v = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.02')
Qt2v = 2*Pv*Ppv
Q2v = (Qt2v + m2v)**2/Qt2v
tv = m2v/Q2v
# I from the Feynman-parameter 1D form  Q^2 I = int_0^1 du ln(u(1-u)/t)/(u(1-u)-t)   (my derivation)
def I_feyn(t):
    f = lambda u: mp.log(u*(1-u)/t)/(u*(1-u) - t)
    ur = (1 - mp.sqrt(1-4*t))/2   # removable point u(1-u)=t
    return mp.quad(f, [0, ur, mp.mpf(1)/2, 1-ur, 1])
def I_UD(x, y):  # Usyukina-Davydychev Phi^(1)(x,y)
    lam = mp.sqrt((1-x-y)**2 - 4*x*y); rho = 2/(1-x-y+lam)
    return (2*(mp.polylog(2, -rho*x) + mp.polylog(2, -rho*y)) + mp.log(y/x)*mp.log((1+rho*y)/(1+rho*x))
            + mp.log(rho*x)*mp.log(rho*y) + mp.pi**2/3)/lam
I1 = I_feyn(tv)/Q2v; I2 = I_UD(tv, tv)/Q2v
check("Feynman 1D form = UD Phi1(t,t)/Q^2", abs(I1 - I2) < mp.mpf(10)**-25, mp.nstr(I1, 20))
# 2D Feynman (common quadrant) density for Gamma:  1/((1+a+b)(a b Q^2 + (a+b) m^2))
mp.mp.dps = 20
IG = mp.quad(lambda a, b: 1/((1+a+b)*(a*b*Q2v + (a+b)*m2v)), [0, mp.mpf('0.01'), 1, 100, mp.inf], [0, mp.mpf('0.01'), 1, 100, mp.inf])
check("Gamma density on the quadrant integrates to I", abs(IG/I1 - 1) < 1e-12, mp.nstr(IG, 16))
mp.mp.dps = 30
D32 = (mp.log(Qt2v/m2v)**2 + mp.pi**2/3)/Qt2v
def rho4(a, b):
    G = 1/((1+a+b)*(a*b*Q2v + (a+b)*m2v))
    CS = 1/(a*b*Qt2v + (a+b)*m2v)
    CC1 = (1/(1+a) - 1)/(a*(b*Qt2v + m2v))
    CC2 = (1/(1+b) - 1)/(b*(a*Qt2v + m2v))
    CH = (1/(1+a+b) - 1/(1+b) - 1/(1+a) + 1)/(a*b*Qt2v)
    return G - CS - CC1 - CC2 - CH
# show integrability: behaviour at large and small a,b
for (a, b) in [(1e6, 1e6), (1e8, 1e8), (1e-8, 1e-8), (1e8, 1e-8), (1e8, 1.0), (1e-8, 1.0)]:
    a = mp.mpf(a); b = mp.mpf(b)
    print("   rho(a=%s,b=%s) * a*b = %s" % (mp.nstr(a,3), mp.nstr(b,3), mp.nstr(rho4(a, b)*a*b, 8)))
mp.mp.dps = 25
R = mp.quad(rho4, [0, mp.mpf('1e-3'), mp.mpf('0.01'), mp.mpf('0.1'), 1, 10, 100, 1000, mp.inf],
                  [0, mp.mpf('1e-3'), mp.mpf('0.01'), mp.mpf('0.1'), 1, 10, 100, 1000, mp.inf])
print("   d=4 remainder (common-quadrant parametric integral) =", mp.nstr(R, 16))
print("   I - (D.32)                                          =", mp.nstr(I1 - D32, 16))
check("d=4 parametric remainder = I - (D.32)", abs(R - (I1 - D32)) < 1e-12)
check("value -0.0173434339581 (12 digits)", abs(R - mp.mpf('-0.0173434339581')) < 1e-12, mp.nstr(R, 15))
sig = m2v/Qt2v
closed = (4*mp.polylog(2, -sig) + sig**2*(mp.log(sig)**2 + mp.pi**2/3))/(Qt2v*(1-sig**2))
check("closed form [4Li2(-s)+s^2(ln^2 s+pi^2/3)]/(Qt^2(1-s^2)) = I - (D.32)", abs(closed - (I1 - D32)) < mp.mpf(10)**-22, mp.nstr(closed, 20))

# ---------------- 5. expansions (sympy) ----------------
t, L = sp.symbols('t L', positive=True)   # L = ln(1/t) = ln(Q^2/m^2)
s = sp.symbols('s', positive=True)
# sigma(t): t = s/(1+s)^2  ->  s = 2t/(1-2t+sqrt(1-4t))
s_of_t = 2*t/(1 - 2*t + sp.sqrt(1 - 4*t))
check("t = s/(1+s)^2 inverts to s = 2t/(1-2t+sqrt(1-4t))", sp.simplify((s_of_t/(1+s_of_t)**2 - t).subs(t, sp.Rational(3,100))) == 0)
# Q^2 I = Q^2 Phi/Q^2 ; with x = y = t: Phi = [4 Li2(-s) + ln^2 s + pi^2/3]/sqrt(1-4t)
N = 4
s_ser = sp.series(s_of_t, t, 0, N+1).removeO()
lns = -L + sp.log(sp.expand(s_ser/t))           # ln s = ln t + ln(s/t)
lns = sp.series(sp.log(s_ser/t), t, 0, N+1).removeO() - L
li2 = sum((-1)**j * s_ser**j / j**2 for j in range(1, N+2))  # Li2(-s) = sum (-s)^j/j^2
Phi = sp.series((4*li2 + lns**2 + sp.pi**2/3)/sp.sqrt(1 - 4*t), t, 0, N).removeO()
Phi = sp.expand(Phi)
c_0 = sp.simplify(Phi.coeff(t, 0)); c_1 = sp.simplify(Phi.coeff(t, 1)); c_2 = sp.simplify(Phi.coeff(t, 2))
print("   Q^2 I: t^0:", c_0, "| t^1:", sp.expand(c_1), "| t^2:", sp.expand(c_2))
check("Q^2 I = L^2 + pi^2/3 + t(2L^2 - 4L - 4 + 2pi^2/3) + ...", sp.simplify(c_0 - (L**2 + sp.pi**2/3)) == 0 and sp.simplify(c_1 - (2*L**2 - 4*L - 4 + 2*sp.pi**2/3)) == 0)
# remainder: Q^2 int r = Q^2 I - Q^2/Qt^2 [ln^2(Qt^2/m^2) + pi^2/3];  Q^2/Qt^2 = (1+s)^2, ln(Qt^2/m^2) = -ln s
D32ser = sp.expand(sp.series((1 + s_ser)**2*(lns**2 + sp.pi**2/3), t, 0, N).removeO())
Rser = sp.expand(Phi - D32ser)
r1 = sp.simplify(Rser.coeff(t, 1)); r2 = sp.simplify(Rser.coeff(t, 2)); r3 = sp.simplify(Rser.coeff(t, 3))
print("   Q^2 int r: t^1:", r1, "| t^2:", sp.expand(r2), "| t^3:", sp.expand(r3))
check("Q^2 int r has no t^0 term", sp.simplify(Rser.coeff(t, 0)) == 0)
check("Q^2 int r = -4t + ...  (no log at NLP)", sp.simplify(r1 + 4) == 0)
check("t^2 coefficient = L^2 - 15 + pi^2/3", sp.simplify(r2 - (L**2 - 15 + sp.pi**2/3)) == 0)
# numerical check of the expansion at small t
for tt in [mp.mpf('1e-3'), mp.mpf('1e-5')]:
    mp.mp.dps = 40
    Qsq = 1; mm2 = tt
    # solve Qt2 from Q^2=(Qt2+m^2)^2/Qt2, larger root
    Qt = (mp.sqrt(Qsq) + mp.sqrt(Qsq - 4*mm2))/2; Qt2x = Qt**2
    ex = I_UD(tt, tt) - (mp.log(Qt2x/mm2)**2 + mp.pi**2/3)/Qt2x
    LL = mp.log(1/tt)
    ap = -4*tt + tt**2*(LL**2 - 15 + mp.pi**2/3)
    print("   t=%s: Q^2 int r exact %s, 2-term %s, diff/(t^3 L^2) %s" % (mp.nstr(tt,3), mp.nstr(ex, 15), mp.nstr(ap, 15), mp.nstr((ex-ap)/(tt**3*LL**2), 6)))
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
