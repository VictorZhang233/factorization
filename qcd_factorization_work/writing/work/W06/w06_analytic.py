r"""
w06_analytic.py -- writer W06: numerical checks of the conventions and identities of sec:ee-analytic,
sec:ee-higher, sec:ee-duality on model spectral functions (no QCD input needed: these are R_def statements).

Model: R(s) = 12 pi Im Pi(s+i0) >= 0 supported on [s0, inf); Pi from the once-subtracted dispersion relation
   Pi(q2) - Pi(-mu2) = (q2 + mu2)/pi * int_{s0}^inf ds Im Pi(s) / ((s - q2)(s + mu2)).
 K1  Im Pi(s + i eta) -> R(s)/(12 pi) as eta -> 0 (Sokhotski-Plemelj; sign of the i0)
 K2  Adler: D(Q2) := -12 pi^2 Q2 dPi(-Q2)/dQ2 equals Q2 int ds R(s)/(s + Q2)^2   (prop:ee-adler-dispersion)
 K3  constant R -> D = R
 K4  smearing: (Delta/pi) int ds' R(s')/((s'-s)^2+Delta^2) = (12 pi/2i)[Pi(s+i Delta) - Pi(s-i Delta)]   (prop:ee-smearing)
 K5  contour formula: R(s) = (1/2pi) int_{-pi}^{pi} dtheta D(s e^{i theta}) for a model with resonances
 K6  subtraction condition: (s+Q2)^{-2} >= (2s)^{-2} for s >= Q2, and the comparison bounds
 K7  PT check of K4 at O(a^0): Rbar = R0 (1 - arctan(Delta/s)/pi)
Run: python3 -I w06_analytic.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

mp.mp.dps = 30
RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


s0 = mp.mpf(1)
mu2 = mp.mpf(2)
# model: continuum with log running + a narrow Breit-Wigner resonance
M2, G = mp.mpf(3), mp.mpf('0.3')


def Rmod(s):
    if s <= s0:
        return mp.mpf(0)
    cont = 2 * (1 + 1 / mp.log(s / mp.mpf('0.3') + 2)) * (1 - s0 / s) ** 2
    res = 5 * M2 * G ** 2 / ((s - M2) ** 2 + M2 * G ** 2)
    return cont + res


def ImPi(s):
    return Rmod(s) / (12 * mp.pi)


def Pi(q2):
    """once-subtracted dispersion relation, Pi(-mu2) := 0"""
    f = lambda s: ImPi(s) * (q2 + mu2) / ((s - q2) * (s + mu2))
    return mp.quad(f, [s0, M2 - 3 * G, M2, M2 + 3 * G, 10, 100, mp.inf]) / mp.pi


# K1: Im Pi(s+i eta) = (1/pi) int ImPi(s') eta/((s'-s)^2+eta^2) ds' -> ImPi(s) as eta -> 0 (sign of the i0)
sx = mp.mpf('2.2')
errs = []
for eta in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
    pts = [s0, sx - 50 * eta, sx - eta, sx, sx + eta, sx + 50 * eta, M2 - 3 * G, M2, M2 + 3 * G, 10, 100, mp.inf]
    pts = sorted(set(pts))
    q2 = sx + 1j * eta
    f = lambda t: ImPi(t) * (q2 + mu2) / ((t - q2) * (t + mu2))
    val = mp.im(mp.quad(f, pts)) / mp.pi
    errs.append(abs(val - ImPi(sx)))
print('      K1 |Im Pi(s+i eta) - R/(12pi)| for eta = 1e-2,1e-3,1e-4:', ['%.2e' % float(x) for x in errs])
check('K1  Im Pi(s + i eta) -> R(s)/(12 pi) linearly in eta (s=2.2; +i0 gives Im Pi >= 0)',
      errs[2] < errs[1] < errs[0] and errs[2] < 2e-3 * abs(ImPi(sx)) and all(x >= 0 for x in errs))
# K2
Q2 = mp.mpf('1.7')
dPi = mp.diff(lambda x: Pi(-x), Q2)
Dnum = -12 * mp.pi ** 2 * Q2 * dPi
Ddisp = Q2 * mp.quad(lambda s: Rmod(s) / (s + Q2) ** 2, [s0, M2 - 3 * G, M2, M2 + 3 * G, 10, 100, mp.inf])
check('K2  D(Q2) = -12 pi^2 Q2 dPi(-Q2)/dQ2 = Q2 int R/(s+Q2)^2   (rel. diff %.1e)' % float(abs(Dnum / Ddisp - 1)), abs(Dnum / Ddisp - 1) < 1e-12)
# K3
check('K3  constant R: Q2 int_0^inf ds/(s+Q2)^2 = 1', abs(Q2 * mp.quad(lambda s: 1 / (s + Q2) ** 2, [0, mp.inf]) - 1) < 1e-20)
# K4
ss, Dl = mp.mpf('2.6'), mp.mpf('0.8')
lhs = Dl / mp.pi * mp.quad(lambda t: Rmod(t) / ((t - ss) ** 2 + Dl ** 2), [s0, M2 - 3 * G, M2, M2 + 3 * G, 10, 100, mp.inf])
rhs = 12 * mp.pi / (2j) * (Pi(ss + 1j * Dl) - Pi(ss - 1j * Dl))
check('K4  smearing identity (rel. diff %.1e; imaginary part of rhs %.1e)' % (float(abs(rhs / lhs - 1)), float(abs(mp.im(rhs)))), abs(rhs / lhs - 1) < 1e-15 and abs(mp.im(rhs)) < 1e-15)
# K5 contour formula, closed-form models with a genuine cut (no quadrature across the cut):
#  (i)  R(s') = theta(s'-s0)          ->  D(Q2) = Q2/(s0+Q2)
#  (ii) R(s') = theta(s'-s0) s0/s'    ->  D(Q2) = (s0/Q2)[ln((s0+Q2)/s0) - Q2/(s0+Q2)]   (principal log: cut Q2 < -s0)
D_i = lambda Q2c: Q2c / (s0 + Q2c)
D_ii = lambda Q2c: (s0 / Q2c) * (mp.log((s0 + Q2c) / s0) - Q2c / (s0 + Q2c))
# cross-check the closed forms against the dispersion integral at a complex point
zt = mp.mpf('1.3') * mp.expj(mp.mpf('2.1'))
num_ii = zt * mp.quad(lambda t: (s0 / t) / (t + zt) ** 2, [s0, 10, mp.inf])
num_i = zt * mp.quad(lambda t: 1 / (t + zt) ** 2, [s0, 10, mp.inf])
check('K5a closed forms of D for models (i),(ii) equal Q2 int R/(s+Q2)^2 at a complex Q2', abs(num_i - D_i(zt)) < 1e-20 and abs(num_ii - D_ii(zt)) < 1e-20)
for sv in (mp.mpf('2.6'), mp.mpf('5.0')):
    ci = mp.quad(lambda th: D_i(sv * mp.expj(th)), [-mp.pi, 0, mp.pi]) / (2 * mp.pi)
    cii = mp.quad(lambda th: D_ii(sv * mp.expj(th)), [-mp.pi, 0, mp.pi]) / (2 * mp.pi)
    check('K5  contour formula at s=%s: model (i) %.12f (R=1), model (ii) %.12f (R=s0/s=%.12f)' % (sv, float(mp.re(ci)), float(mp.re(cii)), float(s0 / sv)),
          abs(ci - 1) < 1e-15 and abs(cii - s0 / sv) < 1e-15)
svb = mp.mpf('0.6')
contb = mp.quad(lambda th: D_ii(svb * mp.expj(th)), [-mp.pi, 0, mp.pi]) / (2 * mp.pi)
check('K5b below threshold (s=0.6 < s0): contour integral of model (ii) = 0 = R(s)', abs(contb) < 1e-15)
# K6
okK6 = all((sv_ + q_) ** -2 >= (2 * sv_) ** -2 for sv_ in (1.0, 2.5, 10.0, 1e6) for q_ in (0.1, 1.0) if sv_ >= q_)
check('K6  (s+Q2)^{-2} >= (2s)^{-2} for s >= Q2', okK6)
# K7: PT LO smearing: R0 = 1, Pi0 = (1/12pi^2)(5/3 - ln(-q2/mu^2)) ; principal log
R0 = 1
Pi0 = lambda z: (mp.mpf(5) / 3 - mp.log(-z)) / (12 * mp.pi ** 2)
for sv, dv in ((mp.mpf(1), mp.mpf('0.5')), (mp.mpf(3), mp.mpf(2))):
    r_ = 12 * mp.pi / (2j) * (Pi0(sv + 1j * dv) - Pi0(sv - 1j * dv))
    check('K7  PT LO: (12pi/2i)[Pi0(s+iD) - Pi0(s-iD)] = 1 - arctan(D/s)/pi  (s=%s, D=%s)' % (sv, dv), abs(r_ - (1 - mp.atan(dv / sv) / mp.pi)) < 1e-25)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
