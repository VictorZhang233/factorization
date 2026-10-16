"""W12 (Ch10) -- ex:disall-heavy-lo: LO gamma* g -> Q Qbar with full mass dependence (writer-derived).

 1. Traces with masses (own D-dim trace engine, here D = 4), -g vs light-cone polarization sums.
 2. Projections (F_2, F_L) and the massive two-body phase space -> closed forms in beta = sqrt(1 - 4m^2/s).
 3. Comparison with the standard closed form (structure of Witten / Glueck-Reya type formulas), threshold.
 4. m -> 0 limit: Fhat_2^g/(z e_Q^2) -> (as/2pi) 2 [C_2^g + P_qg ln(Q^2/m^2)] + O(m^2/Q^2), F_L -> (as/2pi) 2 C_L^g.
 5. One-loop MSbar heavy-quark density of a gluon with mass m: f_{Q/g}(z,mu) = (as/2pi) P_qg(z) ln(mu^2/m^2)
    (computed from the operator definition in light-cone gauge, D dims).  ACOT/CWZ subtraction -> MSbar C_2^g.
 6. Numbers for the text.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dtrace import trace, V, I, D

m, Q2, z, c = sp.symbols('m Q2 z c', positive=True)   # c = cos(theta)
s, t1, u1 = sp.symbols('s t1 u1')
m2 = m ** 2

# ---------------- 1. traces ----------------
# gamma*(q) + g(p) -> Q(p1) + Qbar(p2);  t1 = (p-p1)^2 - m^2 = -2 p.p1, u1 = (p-p2)^2 - m^2 = -2 p.p2
# s = (p+q)^2;  s + t1 + u1 = -Q2  (since p^2=0, q^2=-Q2, p1^2=p2^2=m^2: s+t+u = 2m^2 - Q2)
def dot(a, b):
    a, b = sorted((a, b))
    tab = {('p', 'p'): 0, ('p1', 'p1'): m2, ('p2', 'p2'): m2, ('q', 'q'): -Q2,
           ('p', 'q'): (s + Q2) / 2, ('p', 'p1'): -t1 / 2, ('p', 'p2'): -u1 / 2,
           ('p1', 'p2'): (s - 2 * m2) / 2, ('p1', 'q'): -(u1 + Q2) / 2, ('p2', 'q'): -(t1 + Q2) / 2,
           ('n', 'n'): 0, ('n', 'p'): sp.Symbol('np'), ('n', 'p1'): sp.Symbol('np1'),
           ('n', 'p2'): sp.Symbol('np2'), ('n', 'q'): sp.Symbol('nq')}
    return tab[(a, b)]

def expand_factors(factors):
    """factors: list of lists of (slot or None, coeff); returns list of (slots, coeff)."""
    out = [([], sp.Integer(1))]
    for f in factors:
        new = []
        for sl, cf in out:
            for slot, w in f:
                new.append((sl + ([slot] if slot is not None else []), cf * w))
        out = new
    return out

def mat_el(proj, polsum='g'):
    mu = I('mu') if proj == 'g' else V('p')
    # amplitude: g^mu (p1 - q + m) g^rho / u1 + g^rho (p1 - p + m) g^mu / t1
    A = [(V('p1'), 1), (V('q'), -1), (None, m)]
    B = [(V('p1'), 1), (V('p'), -1), (None, m)]
    amp = [([[(mu, 1)], A, [(I('rho'), 1)]], 1 / u1), ([[(I('rho'), 1)], B, [(mu, 1)]], 1 / t1)]
    cnj = [([[(I('sig'), 1)], A, [(mu, 1)]], 1 / u1), ([[(mu, 1)], B, [(I('sig'), 1)]], 1 / t1)]
    res = sp.Integer(0)
    for fa, ca in amp:
        for fc, cc in cnj:
            facs = [[(V('p1'), 1), (None, m)]] + fa + [[(V('p2'), 1), (None, -m)]] + fc
            for slots, w in expand_factors(facs):
                sgn = -1 if proj == 'g' else 1
                sl_g = [(I('rho') if x == I('sig') else x) for x in slots]
                res += sgn * (-1) * ca * cc * w * trace(sl_g, dot)
                if polsum == 'lc':
                    for (r1, r2) in (('p', 'n'), ('n', 'p')):
                        sl2 = [(V(r1) if x == I('rho') else (V(r2) if x == I('sig') else x)) for x in slots]
                        res += sgn * ca * cc * w * trace(sl2, dot) / sp.Symbol('np')
    return sp.simplify(sp.expand(res.subs(D, 4)))

Mg = mat_el('g')
Mp = mat_el('pp')
Mg_lc = mat_el('g', 'lc')
chk = sp.simplify((Mg_lc - Mg).subs({sp.Symbol('np2'): sp.Symbol('np') + sp.Symbol('nq') - sp.Symbol('np1')}).subs(s, -Q2 - t1 - u1))
print('1. light-cone polarization sum = -g sum (massive):', 'PASS' if chk == 0 else chk)
print('   (-g) projection:', sp.factor(Mg.subs(s, -Q2 - t1 - u1)))
print('   (p p) projection:', sp.factor(Mp.subs(s, -Q2 - t1 - u1)))

# ---------------- 2. phase space and projections ----------------
# CM frame: t1 = -(s+Q2)(1 - beta c)/2, u1 = -(s+Q2)(1 + beta c)/2, s = Q2 (1-z)/z
beta = sp.sqrt(1 - 4 * m2 / s)
kin = {t1: -(s + Q2) * (1 - beta * c) / 2, u1: -(s + Q2) * (1 + beta * c) / 2}
# Fhat/(z e^2) = (as/2pi) T_F (beta/16) int_{-1}^{1} dc  Proj   [4D: (1/4pi) g^2 T_F (1/2) (beta/(16 pi)) int dc]
P2 = Mg + 3 * 4 * z ** 2 / Q2 * Mp
PL = 8 * z ** 2 / Q2 * Mp
def cint(expr):
    e = sp.simplify(expr.subs(kin))
    return sp.simplify(sp.integrate(e, (c, -1, 1)))
b = sp.Symbol('b', positive=True)   # beta
sval = 4 * m2 / (1 - b ** 2)        # s in terms of beta
H2 = sp.Rational(1, 16) * beta * cint(P2)
HL = sp.Rational(1, 16) * beta * cint(PL)
# express in z and eps_m = m^2/Q2 :  s = Q2 (1-z)/z
em = sp.Symbol('epsilon_m', positive=True)
H2z = H2.subs(s, Q2 * (1 - z) / z).subs(m, sp.sqrt(em * Q2))
HLz = HL.subs(s, Q2 * (1 - z) / z).subs(m, sp.sqrt(em * Q2))
print('2. Fhat_2^g/(z e^2) and Fhat_L^g/(z e^2) obtained (phase-space integral done analytically in cos theta)')

# ---------------- 3. comparison with the standard closed form ----------------
bz = sp.sqrt(1 - 4 * em * z / (1 - z))
Lb = sp.log((1 + bz) / (1 - bz))
H2_std = 2 * ((z ** 2 + (1 - z) ** 2 + 4 * em * z * (1 - 3 * z) - 8 * em ** 2 * z ** 2) * Lb
              + bz * (8 * z * (1 - z) - 1 - 4 * em * z * (1 - z)))
HL_std = 2 * (-8 * em * z ** 2 * Lb + 4 * bz * z * (1 - z))
def num_close(e1, e2):
    worst = 0
    for zz in (sp.Rational(1, 10), sp.Rational(1, 3), sp.Rational(1, 2)):
        for ee in (sp.Rational(1, 100), sp.Rational(1, 20), sp.Rational(1, 9)):
            if 4 * ee * zz / (1 - zz) < 1:
                v1 = sp.N(e1.subs({z: zz, em: ee}), 30); v2 = sp.N(e2.subs({z: zz, em: ee}), 30)
                worst = max(worst, abs(v1 - v2))
    return worst
print('3. |H2 - standard form| =', num_close(H2z, H2_std), ';  |HL - standard form| =', num_close(HLz, HL_std))
print('   H2 = 2{[z^2+(1-z)^2+4e z(1-3z)-8e^2z^2] ln((1+b)/(1-b)) + b[8z(1-z)-1-4e z(1-z)]},  e = m^2/Q^2')
print('   HL = 2{-8 e z^2 ln((1+b)/(1-b)) + 4 b z(1-z)},  b = sqrt(1 - 4 e z/(1-z)), threshold z < 1/(1+4e)')

# ---------------- 4. m -> 0 ----------------
lead2 = sp.simplify(sp.limit(H2_std - 2 * (z ** 2 + (1 - z) ** 2) * sp.log(1 / em), em, 0))
print('4. lim_{m->0} [H2 - 2 P_qg/T_F ln(Q^2/m^2)] =', sp.simplify(lead2))
C2g_over_TF = (z ** 2 + (1 - z) ** 2) * sp.log((1 - z) / z) - 8 * z ** 2 + 8 * z - 1
print('   equals 2 C_2^g/T_F (MSbar, massless):', sp.simplify(sp.expand_log(lead2 - 2 * C2g_over_TF, force=True)) == 0)
print('   lim_{m->0} HL =', sp.factor(sp.limit(HL_std, em, 0)), ' (= 2 C_L^g/T_F = 8 z(1-z))')

# ---------------- 5. heavy-quark density of a gluon at one loop ----------------
eps = sp.Symbol('epsilon')
xi, kT2, pplus = sp.symbols('xi kT2 p_plus', positive=True)
n = 2 - 2 * eps     # transverse dimension D-2
# light-front vectors in (+,-,T): p = (p+,0,0), k = (xi p+, k-, kT), p2 = p - k on shell
# trace: Tr[(p2 - m) eps* (k + m) gamma^+ (k + m) eps] summed over physical pols (-g + (p n + n p)/n.p)
# gamma^+ = n_B-slash (n_B.v = v^+): use vector 'nB'
kminus = -(kT2 + m2) / (2 * (1 - xi) * pplus)
def dotf(a_, b_):
    a_, b_ = sorted((a_, b_))
    # components: p=(P,0,0), k=(xi P, km, kT), p2=((1-xi)P, -km, -kT), nB: nB.v = v^+  -> nB=(0,1,0) in (+,-) ; nB.nB=0
    P = pplus; km = kminus
    vec = {'p': (P, 0, 0), 'k': (xi * P, km, 1), 'p2': ((1 - xi) * P, -km, -1), 'nB': (0, 1, 0)}
    A, B = vec[a_], vec[b_]
    T = A[2] * B[2] * kT2     # transverse parts are +/- kT
    return A[0] * B[1] + A[1] * B[0] - T
def tr_heavy():
    res = sp.Integer(0)
    facs_base = [[(V('p2'), 1), (None, -m)], 'eps*', [(V('k'), 1), (None, m)], [(V('nB'), 1)], [(V('k'), 1), (None, m)], 'eps']
    for polterm in ('g', 'pn', 'np'):
        facs = []
        for f in facs_base:
            if f == 'eps*':
                facs.append([(I('a') if polterm == 'g' else V('p' if polterm == 'pn' else 'nB'), 1)])
            elif f == 'eps':
                facs.append([(I('a') if polterm == 'g' else V('nB' if polterm == 'pn' else 'p'), 1)])
            else:
                facs.append(f)
        w0 = -1 if polterm == 'g' else 1 / pplus
        for slots, w in expand_factors(facs):
            res += w0 * w * trace(slots, dotf)
    return sp.simplify(res.subs(D, 4 - 2 * eps))
TR = tr_heavy()
print('5. Tr[...] (D dims, physical pol sum) =', sp.factor(TR))
# f = g^2 T_F/(D-2) (1-xi)/(4 p+) int d^n kT/(2pi)^{D-1} TR (1-xi)^2/(kT2+m^2)^2 ... see derivation in text:
# f = g^2 T_F/(D-2) * (1/2) * 1/(2(1-xi)p+) * int d^n kT/(2pi)^(D-1) * TR / ((kT2+m2)/(1-xi))^2
def kTint(expr):
    """int d^n kT expr, expr = polynomial in kT2 / (kT2+m2)^2 ; formula int d^n k (k^2)^a/(k^2+m^2)^b."""
    expr = sp.expand(sp.simplify(expr * (kT2 + m2) ** 2))
    Pp = sp.Poly(expr, kT2)
    tot = 0
    for (aa,), cf in Pp.terms():
        bb = 2
        tot += cf * sp.pi ** (n / 2) * sp.gamma(aa + n / 2) * sp.gamma(bb - aa - n / 2) / (sp.gamma(n / 2) * sp.gamma(bb)) * (m2) ** (aa - bb + n / 2)
    return tot
fbare = (sp.Symbol('g0sq') * sp.Rational(1, 2) / ((4 - 2 * eps) - 2) / (2 * (1 - xi) * pplus)
         * kTint(TR * (1 - xi) ** 2 / (kT2 + m2) ** 2) / (2 * sp.pi) ** (3 - 2 * eps))
alphas, mu = sp.symbols('alpha_s mu', positive=True)
g0sq = 4 * sp.pi * alphas * mu ** (2 * eps) * sp.exp(eps * sp.EulerGamma) * (4 * sp.pi) ** (-eps)
fb = sp.simplify(fbare.subs(sp.Symbol('g0sq'), g0sq) / (alphas / (2 * sp.pi)))   # units of as/2pi, T_F=1 here (T_F set to 1)
ser = sp.series(fb, eps, 0, 1).removeO()
pole = sp.simplify(sp.expand(ser).coeff(eps, -1))
fin = sp.simplify(sp.expand(ser).coeff(eps, 0))
print('   f_{Q/g}^bare/(as/2pi T_F): pole =', sp.factor(pole), ';  finite =', sp.simplify(fin))
print('   pole = P_qg/T_F :', sp.simplify(pole - (xi ** 2 + (1 - xi) ** 2)) == 0)
print('   MSbar finite part = P_qg/T_F ln(mu^2/m^2) :', sp.simplify(sp.expand_log(fin - (xi ** 2 + (1 - xi) ** 2) * sp.log(mu ** 2 / m2), force=True)) == 0)
# massless check of the D-dim kernel: coefficient of the scaleless integral: TR at m=0
TR0 = sp.factor(sp.simplify(TR.subs(m, 0)))
print('   m=0 kernel check: TR(m=0)*(1-xi)/(...) ->', TR0)

# ---------------- 6. numbers ----------------
print('6. numbers (z, eps_m): exact H2/2 vs massless asymptote C_2^g/T_F + P_qg/T_F ln(1/eps_m), and HL/2')
for zz in (0.1, 0.3):
    for ee in (0.1, 0.01, 0.001):
        if 4 * ee * zz / (1 - zz) < 1:
            ex = float(sp.N((H2_std / 2).subs({z: zz, em: ee})))
            asym = float(sp.N((C2g_over_TF + (z ** 2 + (1 - z) ** 2) * sp.log(1 / em)).subs({z: zz, em: ee})))
            exL = float(sp.N((HL_std / 2).subs({z: zz, em: ee})))
            print('   z=%.2f m^2/Q^2=%.3g : H2/2=%.5f  asymptote=%.5f  diff=%.5f   HL/2=%.5f (massless %.5f)' %
                  (zz, ee, ex, asym, ex - asym, exL, 4 * zz * (1 - zz)))
