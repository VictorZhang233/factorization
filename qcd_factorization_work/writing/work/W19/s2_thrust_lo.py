r"""
W19 / Ch16 -- s2_thrust_lo.py : leading-order thrust distribution (prop:jets-thrust-lo).

Conventions: x_i = 2E_i/Q, sum x_i = 2; (1/sigma0) dsigma/dx1dx2 = a (x1^2+x2^2)/((1-x1)(1-x2)), a = C_F as/(2 pi)
(VF-EE-5); sigma_tot = sigma0 (1 + (3/2) a) (VF-EE-6); tau = 1 - T, plus distributions in tau subtract at tau = 0.

Checks
 T1  dsigma/dT from the three regions T = x1, x2, x3 equals VF-SCET-13 (sympy, exact);
 T2  partial fractions: F(T) = [4/(1-T) + 4/T - 6] ln((2T-1)/(1-T)) - 3/(1-T) - 9T + 15;
 T3  F(1-tau) = -(4 ln tau + 3)/tau + r(tau), r integrable, r(0+) = -8 + ... ;
 T4  the elementary integrals (i)-(iv) of the remainder on (0,1/3) and the dilogarithm identities used;
 T5  C_r = int_0^{1/3} r = 5/2 - pi^2/3 + 2 ln^2 3 - 3 ln 3 (exact; 40-digit numerics);
 T6  cumulant R(tau) = 1 + a[-2 ln^2 tau - 3 ln tau + pi^2/3 - 1] + O(tau ln tau) (exact constant; numerics at
     tau = 1e-3..1e-7 against the full O(a) cumulant);
 T7  delta-coefficient from the sum rule: c_delta = 3/2 - int_0^1 rtilde = pi^2/3 - 1 (30 digits);
 T8  hemisphere identity (M_L^2+M_R^2)/Q^2 = tau - tau^2/2 + (M_R^2-M_L^2)^2/(2Q^4) (symbolic) and numerically on
     random massless 3,4,5,6-body events with the exact thrust (all partitions);
 T9  three partons: M_L^2 + M_R^2 = tau Q^2 exactly, T = max x_i.
Run:  python3 -I s2_thrust_lo.py
"""
import sys, os, itertools, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

T, x1, x2, tau, t = sp.symbols('T x1 x2 tau t', positive=True)
M = (x1 ** 2 + x2 ** 2) / ((1 - x1) * (1 - x2))

# --- T1: three regions ---
A = sp.integrate(M.subs(x1, T), (x2, 2 - 2 * T, T))                 # T = x1 (and T = x2 by symmetry)
B = sp.integrate(M.subs(x2, 2 - T - x1), (x1, 2 - 2 * T, T))         # T = x3
F_reg = sp.simplify(2 * A + B)
F_vf = 2 * (3 * T ** 2 - 3 * T + 2) / (T * (1 - T)) * sp.log((2 * T - 1) / (1 - T)) - 3 * (3 * T - 2) * (2 - T) / (1 - T)
ok = all(abs(sp.N((F_reg - F_vf).subs(T, val), 30)) < 1e-25 for val in [sp.Rational(7, 10), sp.Rational(3, 4),
                                                                         sp.Rational(9, 10), sp.Rational(99, 100),
                                                                         sp.Rational(9999, 10000)])
check('T1  2*int_{T=x1} + int_{T=x3} of the matrix element = VF-SCET-13 (5 points, 30 digits)', ok)

# --- T2: partial fractions ---
F_pf = (4 / (1 - T) + 4 / T - 6) * sp.log((2 * T - 1) / (1 - T)) - 3 / (1 - T) - 9 * T + 15
check('T2  partial-fraction form of F(T)', sp.simplify(F_vf - F_pf) == 0)

# --- T3: singular decomposition in tau ---
Ft = sp.simplify(F_pf.subs(T, 1 - tau))
S = -(4 * sp.log(tau) + 3) / tau
r = sp.simplify(Ft - S)
r_expl = 4 * sp.log(1 - 2 * tau) / tau + (4 / (1 - tau) - 6) * (sp.log(1 - 2 * tau) - sp.log(tau)) + 6 + 9 * tau
check('T3a F(1-tau) = -(4 ln tau + 3)/tau + r(tau) with r = 4ln(1-2tau)/tau + [4/(1-tau)-6](ln(1-2tau)-ln tau) + 6 + 9tau',
      sp.simplify(r - r_expl) == 0)
check('T3b tau*r(tau) -> 0 (r integrable at tau = 0: r ~ 2 ln tau)', sp.limit(tau * r_expl, tau, 0) == 0)

# --- T4: elementary integrals of r on (0, 1/3) ---
mp.mp.dps = 40
third = mp.mpf(1) / 3
def rnum(x):
    x = mp.mpf(x)
    return 4 * mp.log(1 - 2 * x) / x + (4 / (1 - x) - 6) * (mp.log(1 - 2 * x) - mp.log(x)) + 6 + 9 * x
i_num = mp.quad(lambda x: 4 * mp.log(1 - 2 * x) / x, [0, third])
ii_num = mp.quad(lambda x: (4 / (1 - x) - 6) * mp.log(1 - 2 * x), [0, third])
iii_num = mp.quad(lambda x: -(4 / (1 - x) - 6) * mp.log(x), [0, third])
iv_num = mp.quad(lambda x: 6 + 9 * x, [0, third])
L2, L3 = mp.log(2), mp.log(3)
i_an = -4 * mp.polylog(2, mp.mpf(2) / 3)
ii_an = 4 * (L2 * mp.log(mp.mpf(3) / 2) - mp.log(mp.mpf(2) / 3) ** 2 / 2 - mp.polylog(2, mp.mpf(3) / 4)
             + mp.polylog(2, mp.mpf(1) / 2)) + 2 - L3
iii_an = -4 * L3 * mp.log(mp.mpf(2) / 3) + 4 * mp.polylog(2, third) - 2 * L3 - 2
iv_an = mp.mpf(5) / 2
check('T4a (i)  int_0^{1/3} 4 ln(1-2t)/t = -4 Li2(2/3)', abs(i_num - i_an) < 1e-30)
check('T4b (ii) int_0^{1/3}[4/(1-t)-6] ln(1-2t) = 4[ln2 ln(3/2) - ln^2(2/3)/2 - Li2(3/4) + Li2(1/2)] + 2 - ln3',
      abs(ii_num - ii_an) < 1e-30)
check('T4c (iii) -int_0^{1/3}[4/(1-t)-6] ln t = -4 ln3 ln(2/3) + 4 Li2(1/3) - 2 ln3 - 2', abs(iii_num - iii_an) < 1e-30)
check('T4d (iv) int_0^{1/3}(6+9t) = 5/2', abs(iv_num - iv_an) < 1e-30)
# dilog identities
Li2 = lambda z: mp.polylog(2, z)
idA = abs(Li2(third) + Li2(2 * third) - (mp.pi ** 2 / 6 - mp.log(third) * mp.log(2 * third)))
idB = abs(Li2(third) + Li2(mp.mpf(-1) / 2) + mp.log(2 * third) ** 2 / 2)
idC = abs(Li2(mp.mpf(1) / 4) - 2 * (Li2(mp.mpf(1) / 2) + Li2(mp.mpf(-1) / 2)))
idD = abs(Li2(mp.mpf(1) / 2) - (mp.pi ** 2 / 12 - L2 ** 2 / 2))
idE = abs(Li2(mp.mpf(3) / 4) + Li2(mp.mpf(1) / 4) - (mp.pi ** 2 / 6 - mp.log(mp.mpf(3) / 4) * mp.log(mp.mpf(1) / 4)))
check('T4e Euler reflection, Landen, duplication and Li2(1/2) identities (40 digits)',
      max(idA, idB, idC, idD, idE) < 1e-35)
# symbolic: with a=ln2, b=ln3 the logarithmic bracket equals 2 b^2
a_, b_ = sp.symbols('a b')
br = (4 * b_ * (b_ - a_) + 4 * (b_ - 2 * a_) * (-2 * a_) - 4 * (a_ - b_) ** 2 - 6 * a_ ** 2 + 4 * a_ * (b_ - a_)
      - 2 * (a_ - b_) ** 2 - 4 * b_ * (a_ - b_))
check('T4f logarithmic bracket after cancelling Li2(1/3) equals 2 ln^2 3', sp.expand(br - 2 * b_ ** 2) == 0)

# --- T5 ---
Cr = mp.quad(rnum, [0, mp.mpf('1e-30'), mp.mpf('1e-10'), mp.mpf('1e-3'), third])
Cr_an = mp.mpf(5) / 2 - mp.pi ** 2 / 3 + 2 * L3 ** 2 - 3 * L3
check('T5  C_r = int_0^{1/3} r = 5/2 - pi^2/3 + 2 ln^2 3 - 3 ln 3', abs(Cr - Cr_an) < 1e-28, mp.nstr(Cr, 25))

# --- T6: cumulant ---
def Fn(T_):
    T_ = mp.mpf(T_)
    return 2 * (3 * T_ ** 2 - 3 * T_ + 2) / (T_ * (1 - T_)) * mp.log((2 * T_ - 1) / (1 - T_)) - 3 * (3 * T_ - 2) * (2 - T_) / (1 - T_)
def R1(tv):  # O(a) coefficient of the cumulant: 3/2 - int_tau^{1/3} F(1-tau') dtau'
    tv = mp.mpf(tv)
    return mp.mpf(3) / 2 - mp.quad(lambda s: Fn(1 - s), [tv, tv * 10, mp.mpf('1e-2') if tv < 1e-3 else (tv + third) / 2, third])
okc = True
for tv in ['1e-3', '1e-4', '1e-5', '1e-6', '1e-7']:
    lt = mp.log(mp.mpf(tv))
    pred = -2 * lt ** 2 - 3 * lt + mp.pi ** 2 / 3 - 1
    dif = R1(tv) - pred
    bound = 50 * mp.mpf(tv) * abs(lt) ** 2
    print('    tau=%s  R1=%s  singular=%s  diff=%s' % (tv, mp.nstr(R1(tv), 15), mp.nstr(pred, 15), mp.nstr(dif, 5)))
    okc &= abs(dif) < bound
check('T6  R(tau) = 1 + a[-2ln^2 tau - 3 ln tau + pi^2/3 - 1] + O(tau ln^2 tau)', okc)

# --- T7: delta coefficient from the sum rule ---
rt_int = Cr + mp.quad(lambda s: (3 + 4 * mp.log(s)) / s, [third, 1])     # rtilde on (1/3,1) = (3+4 ln tau)/tau
cdelta = mp.mpf(3) / 2 - rt_int
check('T7  c_delta = 3/2 - int_0^1 rtilde = pi^2/3 - 1', abs(cdelta - (mp.pi ** 2 / 3 - 1)) < 1e-28,
      mp.nstr(cdelta, 20) + ' vs ' + mp.nstr(mp.pi ** 2 / 3 - 1, 20))

# --- T8: hemisphere identity ---
ER, EL, P, Q = sp.symbols('E_R E_L P Q', positive=True)
MR2 = ER ** 2 - P ** 2; ML2 = EL ** 2 - P ** 2
expr = (ML2 + MR2) / Q ** 2 - (tau - tau ** 2 / 2 + (MR2 - ML2) ** 2 / (2 * Q ** 4))
expr = expr.subs({EL: Q - ER, P: (1 - tau) * Q / 2})
check('T8a symbolic: with E_L = Q - E_R, |P| = TQ/2 the identity holds', sp.simplify(expr) == 0)

rng = np.random.default_rng(16)
def random_event(n):
    # massless n-body event in the CM frame (RAMBO-like: isotropic + boost/rescale)
    q = []
    for _ in range(n):
        c = rng.uniform(-1, 1); ph = rng.uniform(0, 2 * math.pi); E = -math.log(rng.uniform() * rng.uniform())
        s = math.sqrt(1 - c * c)
        q.append(E * np.array([1.0, s * math.cos(ph), s * math.sin(ph), c]))
    q = np.array(q); Qv = q.sum(axis=0); Mq = math.sqrt(Qv[0] ** 2 - Qv[1:] @ Qv[1:])
    b = -Qv[1:] / Mq; gam = Qv[0] / Mq; aa = 1 / (1 + gam); x = 1.0 / Mq
    p = []
    for qi in q:
        bq = b @ qi[1:]
        p.append(x * np.concatenate([[gam * qi[0] + bq], qi[1:] + b * qi[0] + aa * bq * b]))
    return np.array(p)  # total energy 1
def thrust_exact(p):
    n = len(p); best = 0.0; bestS = None
    for mask in range(1, 2 ** (n - 1)):
        S = [i for i in range(n) if (mask >> i) & 1]
        PS = p[S, 1:].sum(axis=0); v = math.sqrt(PS @ PS)
        if v > best:
            best, bestS = v, S
    return 2 * best / p[:, 0].sum(), bestS
okh = True; ok3 = True
for n in [3, 4, 5, 6]:
    for _ in range(400):
        p = random_event(n)
        Th, S = thrust_exact(p)
        Sc = [i for i in range(n) if i not in S]
        def m2(idx):
            v = p[idx].sum(axis=0); return v[0] ** 2 - v[1:] @ v[1:]
        MR, ML = m2(S), m2(Sc)
        Qt = p[:, 0].sum(); ta = 1 - Th
        lhs = (ML + MR) / Qt ** 2; rhs = ta - ta ** 2 / 2 + (MR - ML) ** 2 / (2 * Qt ** 4)
        okh &= abs(lhs - rhs) < 1e-12
        if n == 3:
            ok3 &= abs((ML + MR) / Qt ** 2 - ta) < 1e-12 and abs(Th - 2 * p[:, 0].max() / Qt) < 1e-12
check('T8b numerical: identity on 1600 random massless 3-6 body events (exact thrust)', okh)
check('T9  three partons: M_L^2 + M_R^2 = tau Q^2 and T = max x_i', ok3)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
