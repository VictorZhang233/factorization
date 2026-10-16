# X1 fix round 2 -- P2 (strict window) with general independent regulators: regulator-shape dependence.
# Strict-Glauber limit (connecting propagators k^- independent, |z_e| -> infinity), jet A localized:
# J_A^[12]_eik(k1,k2) = Jcal 2 pi delta(k1+k2) i/(k1+i0),  J_A^[21]_eik = Jcal 2 pi delta(k1+k2) i/(-k1+i0)
# (sum over the three sectors of each colour order = time-ordered product with no restriction relative to V_H).
# With regulators chi_1(k1^-) chi_2(k2^-):
#     w^A_12 = 1/2 + i delta_A,  delta_A = (1/2pi) PV int chi_1(k) chi_2(-k) dk/k / (chi_1(0) chi_2(0)),
#     w^A_21 = 1 - w^A_12 = 1/2 - i delta_A;   same on the B side;  p_opp = 1/2 + 2 delta_A delta_B (identity).
# Tests: (a) sharp independent windows; (b) even (Lorentzian) regulators, line-dependent scales;
#        (c) rational non-even line-dependent regulators vs the regulator-pole race of L1' (reviewer 2 chkB);
#        (d) the algebraic identity p_opp = 1/2 + 2 delta_A delta_B and its range.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30

def delta_from_regs(chi1, chi2, pts):
    f = lambda k: (chi1(k)*chi2(-k) - chi1(-k)*chi2(k))/(2*k)     # odd part / k  (PV integral of g(k)/k = int of odd part/k)
    val = mp.quad(f, pts)
    return val/(2*mp.pi*chi1(0)*chi2(0))

# (a) sharp windows: line 1 window [-K1, K2], line 2 window [-K1p, K2p]
def sharp(Ka, Kb):
    return lambda k: mp.mpf(1) if (-Ka <= k <= Kb) else mp.mpf(0)
allok = True
for (K1, K2, K1p, K2p) in [(1, 1, 1, 1), (1, 3, 1, 3), (1, 3, 3, 1), (1, mp.e**mp.pi, mp.e**mp.pi, 1), (2, 5, 1, 7)]:
    c1 = sharp(K1, K2); c2 = sharp(K1p, K2p)
    pts = sorted(set([-50, -K1, -K2p, -K1p, -K2, 0, K2, K1p, K2p, K1, 50]))
    pts = [mp.mpf(p) for p in pts]
    d = delta_from_regs(c1, c2, pts)
    pred = mp.log(min(K2, K1p)/min(K1, K2p))/(2*mp.pi)
    ok = abs(d - pred) < 1e-8; allok &= ok
    print(f"(a) windows line1 [-{mp.nstr(K1,4)},{mp.nstr(K2,4)}], line2 [-{mp.nstr(K1p,4)},{mp.nstr(K2p,4)}]: delta = {mp.nstr(d,10)}; "
          f"predicted ln(min(K2,K1')/min(K1,K2'))/(2pi) = {mp.nstr(pred,10)};  w12 = 1/2 + i delta;  ok={ok}")

# (b) even Lorentzian regulators with line-dependent scales -> delta = 0
for (Ka, Kb) in [(1, 1), (1, 5), (0.3, 7)]:
    c1 = lambda k, K=Ka: K**2/(k**2 + K**2); c2 = lambda k, K=Kb: K**2/(k**2 + K**2)
    d = delta_from_regs(c1, c2, [-mp.inf, -10, -1, 0, 1, 10, mp.inf])
    ok = abs(d) < 1e-20; allok &= ok
    print(f"(b) Lorentzian scales ({Ka},{Kb}): delta = {mp.nstr(d,5)}  -> w12 = 1/2;  ok={ok}")

# (c) rational non-even regulators chi_e(k) = K1e K2e/((K1e + i k)(K2e - i k)); compare with L1' regulator-pole race
def rat(K1, K2):
    return lambda k: K1*K2/((K1 + 1j*k)*(K2 - 1j*k))
def race_w12(K1a, K2a, K1b, K2b):
    up1 = mp.mpf(K2a)/(K1a + K2a); um1 = 1 - up1; up2 = mp.mpf(K2b)/(K1b + K2b); um2 = 1 - up2
    init = mp.mpf(K1b)/(K1a + K1b); fin = mp.mpf(K2a)/(K2a + K2b)
    return up1*up2*init + um1*um2*fin + up1*um2
for (K1a, K2a, K1b, K2b) in [(1, 3, 1, 3), (1, 3, 4, 0.5), (2, 1, 0.5, 6)]:
    c1 = rat(K1a, K2a); c2 = rat(K1b, K2b)
    d = delta_from_regs(c1, c2, [-mp.inf, -100, -10, -1, 0, 1, 10, 100, mp.inf])
    w_pv = 0.5 + 1j*d; w_race = race_w12(K1a, K2a, K1b, K2b)
    ok = abs(w_pv - w_race) < 1e-15; allok &= ok
    print(f"(c) rational regs ({K1a},{K2a};{K1b},{K2b}): PV formula w12 = {mp.nstr(w_pv,12)};  L1' regulator-pole race w12 = {mp.nstr(w_race,12)};  ok={ok}")
print(f"    (97/105 = {mp.nstr(mp.mpf(97)/105,12)})")

# (d) identity and range
for (dA, dB) in [(0, 0.3), (0.5, 0.5), (0.5, -0.5), (1, 1), (0.2+0.1j, -0.4j)]:
    wA = 0.5 + 1j*dA; wB = 0.5 + 1j*dB
    p = wA*(1 - wB) + (1 - wA)*wB
    ok = abs(p - (0.5 + 2*dA*dB)) < 1e-15; allok &= ok
    print(f"(d) delta_A={dA}, delta_B={dB}: p_opp = {p}  (1/2 + 2 dA dB = {0.5 + 2*dA*dB});  ok={ok}")
print("ALL PASS" if allok else "SOME CHECK FAILED")
