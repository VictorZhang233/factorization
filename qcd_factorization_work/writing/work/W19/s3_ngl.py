r"""
W19 / Ch16 -- s3_ngl.py : leading non-global logarithm at O(alpha_s^2) (prop:jets-ngl), its BMS
form at large N_c (thm:jets-bms), and the slice geometry.

Set-up: e+e- -> q(p_a) qbar(p_b) back to back along z (a along +z: the measured hemisphere R = {eta>0}
contains a); strongly energy-ordered soft gluons k1 (harder), k2 (softer).  W_ij(k) = (p_i.p_j)/((p_i.k)(p_j.k)).
Single emission: dP = (as/(2 pi^2)) C_F W_ab(k) E dE dOmega (prop:qcd-soft-collinear-limits (a)).
Correlated (C_F C_A) part of ordered two-gluon emission:
   dP_corr = (as/(2pi^2))^2 C_F (C_A/2) W_ab(1)[W_a1(2)+W_1b(2)-W_ab(2)] E1dE1dOmega1 E2dE2dOmega2 .

Checks
 C1  colour algebra for the singlet q qbar g state with explicit SU(3) generators:
     -2 T_q.T_g = -2 T_qbar.T_g = C_A,  -2 T_q.T_qbar = 2 C_F - C_A ; and for the q qbar state -2T_q.T_qbar = 2 C_F;
 C2  E^2 W_ab dOmega = 2 deta dphi  and  E2^2[W_a1+W_1b-W_ab] dOmega2 = 2 cos(dphi)/(cosh(deta)-cos(dphi)) deta2 dphi2
     (random points, from four-vectors);
 C3  int_0^{2pi} dphi cos(phi)/(A - cos phi) = 2 pi (A/sqrt(A^2-1) - 1)  ->  4 pi^2 (coth|deta| - 1) after both phis;
 C4  int_{eta1<0<eta2} (coth(eta2-eta1)-1) = int_0^inf Delta (coth Delta - 1) dDelta = pi^2/12  (exact);
 C5  Dasgupta--Salam form: int_0^1 dc2 int_{-1}^0 dc1 2/((c2-c1)(1-c1)(1+c2)) = pi^2/6, i.e. S2 = -C_F C_A pi^2/3;
 C6  the full chain: coefficient of as^2 L^2 = -C_F C_A/12 = -C_F C_A (pi^2/3)/(2pi)^2 ; direct azimuthal average
     of the four-vector expression reproduces 4 cosh^2(eta1) cosh^2(eta2) (coth|deta| - 1);
 C7  slice |eta| < eta_in (C_out) with jets in C_in: per boundary int_0^inf min(x, 2 eta_in)(coth x -1) dx
     = pi^2/12 - Li2(e^{-4 eta_in})/2  => g = 1 - Delta^2 [pi^2/12 - Li2(tan^4(theta_in/2))/2] (BMS eq. (5.5));
 C8  BMS at second order: g_hemisphere = 1 - (pi^2/24) Delta^2, Delta = N_c as L/pi, = large-N_c limit of C6;
 C9  measurement independence: replacing the energy veto by the hemisphere-mass veto changes only single-log
     terms (the extra angular integral is finite).
Run:  python3 -I s3_ngl.py
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import integrate

RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

rng = np.random.default_rng(7)

# ---------------- C1: colour algebra ----------------
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / math.sqrt(3)
tg = lam / 2
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = tg[a] @ tg[b] - tg[b] @ tg[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j * np.trace(comm @ tg[c]))
CF, CA = 4 / 3, 3.0
# state psi[i, j, c] = t^c_{ij}, normalized
psi = np.zeros((3, 3, 8), dtype=complex)
for c in range(8):
    psi[:, :, c] = tg[c]
psi /= np.sqrt(np.sum(np.abs(psi) ** 2))
def Tq(a, s):   # quark: (t^a)_{i'i}
    return np.einsum('ki,ijc->kjc', tg[a], s)
def Tqb(a, s):  # antiquark: -(t^a)_{j j'}  i.e. -(t^a)^T
    return -np.einsum('jk,ijc->ikc', tg[a], s)
def Tg(a, s):   # gluon: (F^a)_{c'c} = -i f^{a c' c}
    return np.einsum('dc,ijc->ijd', -1j * f[a], s)
def dot(Op1, Op2, s):
    return sum(np.vdot(s, Op1(a, Op2(a, s))) for a in range(8)).real
tot = [Tq(a, psi) + Tqb(a, psi) + Tg(a, psi) for a in range(8)]
singlet = max(np.max(np.abs(x)) for x in tot) < 1e-12
qg, qbg, qqb = dot(Tq, Tg, psi), dot(Tqb, Tg, psi), dot(Tq, Tqb, psi)
check('C1a q qbar g state is a colour singlet (T_q+T_qbar+T_g = 0)', singlet)
check('C1b -2T_q.T_g = -2T_qbar.T_g = C_A = 3, -2T_q.T_qbar = 2C_F - C_A = -1/3',
      abs(-2 * qg - CA) < 1e-12 and abs(-2 * qbg - CA) < 1e-12 and abs(-2 * qqb - (2 * CF - CA)) < 1e-12,
      '%.12f %.12f %.12f' % (-2 * qg, -2 * qbg, -2 * qqb))
psi2 = np.eye(3, dtype=complex) / math.sqrt(3)
def Tq2(a, s): return tg[a] @ s
def Tqb2(a, s): return -s @ tg[a]
d2 = sum(np.vdot(psi2, Tq2(a, Tqb2(a, psi2))) for a in range(8)).real
check('C1c q qbar singlet: -2 T_q.T_qbar = 2 C_F', abs(-2 * d2 - 2 * CF) < 1e-12)

# ---------------- C2: rapidity form of the antennae ----------------
def nvec(eta, phi):
    c = math.tanh(eta); s = 1 / math.cosh(eta)
    return np.array([1.0, s * math.cos(phi), s * math.sin(phi), c])
def mdot(p, q): return p[0] * q[0] - p[1:] @ q[1:]
pa = np.array([1.0, 0, 0, 1.0]); pb = np.array([1.0, 0, 0, -1.0])
ok2 = True
for _ in range(2000):
    e1, e2 = rng.uniform(-4, 4, 2); f1, f2 = rng.uniform(0, 2 * math.pi, 2)
    k1, k2 = nvec(e1, f1), nvec(e2, f2)     # E = 1 (E^2 W is homogeneous of degree 0)
    W = lambda i, j, k: mdot(i, j) / (mdot(i, k) * mdot(j, k))
    lhs1 = W(pa, pb, k1)                     # E1^2 W_ab(1)
    # dOmega = dcos dphi = deta dphi / cosh^2 eta
    ok2 &= abs(lhs1 / math.cosh(e1) ** 2 - 2) < 1e-10
    br = W(pa, k1, k2) + W(k1, pb, k2) - W(pa, pb, k2)
    rhs = 2 * math.cos(f1 - f2) / (math.cosh(e1 - e2) - math.cos(f1 - f2))
    ok2 &= abs(br / math.cosh(e2) ** 2 - rhs) < 1e-8 * max(1, abs(rhs))
check('C2  E^2 W_ab dOmega = 2 deta dphi;  E2^2[W_a1+W_1b-W_ab] dOmega2 = 2cos(dphi)/(cosh(deta)-cos(dphi)) deta2 dphi2', ok2)

# ---------------- C3: azimuthal integral ----------------
ok3 = True
for A in [1.001, 1.3, 2.0, 7.0]:
    num = integrate.quad(lambda p: math.cos(p) / (A - math.cos(p)), 0, 2 * math.pi, limit=400)[0]
    ok3 &= abs(num - 2 * math.pi * (A / math.sqrt(A * A - 1) - 1)) < 1e-8
x = sp.symbols('x', positive=True)
check('C3  int_0^{2pi} cos/(A-cos) = 2pi(A/sqrt(A^2-1)-1); with A=cosh(deta): 2pi(coth|deta|-1)', ok3 and
      sp.simplify(sp.cosh(x) / sp.sqrt(sp.cosh(x) ** 2 - 1) - sp.coth(x)) == 0)

# ---------------- C4: the rapidity integral ----------------
n = sp.symbols('n', integer=True, positive=True)
ser = sp.summation(2 * sp.integrate(x * sp.exp(-2 * n * x), (x, 0, sp.oo)), (n, 1, sp.oo))
mp.mp.dps = 30
num4 = mp.quad(lambda d: d * (mp.coth(d) - 1), [0, 1, 10, mp.inf])
check('C4  int_0^inf Delta(coth Delta - 1) = pi^2/12', sp.simplify(ser - sp.pi ** 2 / 12) == 0 and
      abs(num4 - mp.pi ** 2 / 12) < 1e-25, mp.nstr(num4, 20))

# ---------------- C5: Dasgupta-Salam angular function ----------------
c1, c2 = sp.symbols('c1 c2')
Om2 = 2 / ((c2 - c1) * (1 - c1) * (1 + c2))
num5 = mp.quad(lambda b, a: 2 / ((b - a) * (1 - a) * (1 + b)), [0, 1], [-1, 0])
check('C5  int_0^1 dc2 int_{-1}^0 dc1 Omega_2 = pi^2/6  =>  S2 = -2 C_F C_A pi^2/6 = -C_F C_A pi^2/3',
      abs(num5 - mp.pi ** 2 / 6) < 1e-15, mp.nstr(num5, 18))
# cross-check: (coth(eta2-eta1)-1) deta1 deta2 = (1/2) Omega_2 dc1 dc2
e1s, e2s = sp.symbols('eta1 eta2', real=True)
c1e, c2e = sp.tanh(e1s), sp.tanh(e2s)
jac = (1 - c1e ** 2) * (1 - c2e ** 2)       # dc = (1-c^2) deta
lhs = (sp.coth(e2s - e1s) - 1)
rhs = sp.Rational(1, 2) * Om2.subs({c1: c1e, c2: c2e}) * jac
vals = [(-0.3, 0.7), (-2.0, 0.1), (-0.05, 3.0)]
check('C5b (coth(eta2-eta1)-1) deta1 deta2 = Omega_2/2 dc1 dc2',
      all(abs(float((lhs - rhs).subs({e1s: a, e2s: b}))) < 1e-12 for a, b in vals))

# ---------------- C6: full coefficient + azimuthal average from four-vectors ----------------
aS, L = sp.symbols('alpha_s L', positive=True)
CFs, CAs = sp.symbols('C_F C_A', positive=True)
pref = (aS / (2 * sp.pi ** 2)) ** 2 * CFs * (CAs / 2)
ang = 4 * (4 * sp.pi ** 2) * sp.pi ** 2 / 12          # int 2 deta1 dphi1 * int 2cos/(..) = 4*4pi^2*(pi^2/12)
energy = L ** 2 / 2
coef = sp.simplify(pref * ang * energy)
check('C6a correlated emission into R off k1 in L: total = C_F C_A as^2 L^2/12 = C_F C_A (pi^2/3)(as L/2pi)^2',
      sp.simplify(coef - CFs * CAs * aS ** 2 * L ** 2 / 12) == 0 and
      sp.simplify(coef - CFs * CAs * sp.pi ** 2 / 3 * (aS * L / (2 * sp.pi)) ** 2) == 0, str(coef))
ok6 = True
for _ in range(25):
    e1 = rng.uniform(-3, -0.01); e2 = rng.uniform(0.01, 3)
    def integrand(df):
        k1, k2 = nvec(e1, 0.0), nvec(e2, df)
        W = lambda i, j, k: mdot(i, j) / (mdot(i, k) * mdot(j, k))
        return W(pa, pb, k1) * (W(pa, k1, k2) + W(k1, pb, k2) - W(pa, pb, k2))
    avg = integrate.quad(integrand, 0, 2 * math.pi, limit=400, points=[math.pi])[0] / (2 * math.pi)
    pred = 4 * math.cosh(e1) ** 2 * math.cosh(e2) ** 2 * (1 / math.tanh(e2 - e1) - 1)
    ok6 &= abs(avg - pred) < 1e-7 * pred
check('C6b azimuthal average of E1^2W_ab(1) E2^2[W_a1+W_1b-W_ab](2) = 4cosh^2 eta1 cosh^2 eta2 (coth|deta|-1)', ok6)
# the energy integral
E0, Qh, E1v, E2v = sp.symbols('E_0 Qh E1 E2', positive=True)
en = sp.integrate(sp.integrate(1 / E1v, (E1v, E2v, Qh)) / E2v, (E2v, E0, Qh))
check('C6c int_{E0}^{Q/2} dE2/E2 int_{E2}^{Q/2} dE1/E1 = (1/2) ln^2(Q/(2E0))',
      sp.simplify(en - sp.log(Qh / E0) ** 2 / 2) == 0)

# ---------------- C7: slice geometry vs BMS (5.5) ----------------
ok7 = True
for ein in [0.1, 0.5, 1.0, 2.0]:
    numv = mp.quad(lambda xx: min(xx, 2 * ein) * (mp.coth(xx) - 1), [0, 2 * ein, mp.inf])
    an = mp.pi ** 2 / 12 - mp.polylog(2, mp.e ** (-4 * ein)) / 2
    # BMS: R^(1) = Delta^2 [pi^2/12 - Li2(tan^4(theta_in/2))/2], tan(theta_in/2) = e^{-eta_in}
    thin = 2 * mp.atan(mp.e ** (-ein))
    bms = mp.pi ** 2 / 12 - mp.polylog(2, mp.tan(thin / 2) ** 4) / 2
    # two boundaries: g = 1 - (Delta^2/2) * 2 * an
    ok7 &= abs(numv - an) < 1e-20 and abs(an - bms) < 1e-25
check('C7  slice: (Delta^2/2)*2*[pi^2/12 - Li2(e^{-4 eta_in})/2] = BMS eq. (5.5) R^(1); limits pi^2/12 and 0', ok7 and
      abs(mp.polylog(2, 1) / 2 - mp.pi ** 2 / 12) < 1e-25)

# ---------------- C8: BMS second order, hemisphere ----------------
Nc, Dl = sp.symbols('N_c Delta', positive=True)
g2 = -(Dl ** 2 / 2) * sp.pi ** 2 / 12
fixed = (-CFs * CAs * aS ** 2 * L ** 2 / 12).subs({CFs: Nc / 2, CAs: Nc})
check('C8  BMS hemisphere g = 1 - (pi^2/24) Delta^2 equals the large-N_c limit of C6 with Delta = N_c as L/pi',
      sp.simplify(g2.subs(Dl, Nc * aS * L / sp.pi) - fixed) == 0)

# ---------------- C9: hemisphere-mass vs energy veto ----------------
# extra single-log term: int deta1 deta2 (coth-1) ln((1-c2)/2) with c2 = tanh(eta2), finite
# mpmath: quad(f(x,y), xrange, yrange); here x = eta1 in (-inf,0), y = eta2 in (0,inf)
lw = lambda e2: -2 * e2 - mp.log(1 + mp.e ** (-2 * e2))      # = ln((1 - tanh e2)/2), numerically stable
extra = mp.quad(lambda e1, e2: (mp.coth(e2 - e1) - 1) * lw(e2),
                [-mp.inf, -1, 0], [0, 1, mp.inf])
# independent evaluation: integrate eta1 analytically, int_{-inf}^0 (coth(e2-e1)-1) de1 = -ln(1-e^{-2 e2})
extra2 = mp.quad(lambda e2: -mp.log(-mp.expm1(-2 * e2)) * lw(e2), [0, 1, mp.inf])
check('C9  hemisphere-mass veto: the extra angular weight ln((1-c2)/2) gives a finite single-log coefficient',
      mp.isfinite(extra) and abs(extra) < 10 and abs(extra - extra2) < 1e-10, mp.nstr(extra, 12) + ' = ' + mp.nstr(extra2, 12))

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
