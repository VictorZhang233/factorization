# -*- coding: utf-8 -*-
"""
glauber_toy.py -- abelian toy model for Glauber exchanges in Drell-Yan (see DERIVATION.md section 3).

Model: U(1) vector boson of mass m (Feynman gauge, propagator -i g_{mu nu}/(k^2-m^2+i0)), charged scalars with
D_mu = d_mu - i g_j A_mu (vertex +i g_j (p+p')^mu).  Hadron A (+z) -> active a + spectator s_A,
hadron B (-z) -> active b + spectator s_B; a + b annihilate at a hard vertex.  Light-front: as in CONTEXT.

G1  eikonal phase of two infinite light-like lines (position space, exact in the free abelian theory)
G2  one-boson spectator-spectator graph in momentum space: residues -> spectators on shell, kernel -i g_A g_B/(k_T^2+m^2)
G3  unitarity: the phase cancels in cross sections inclusive in the spectators' relative transverse momentum
    (numerical demonstration with a complex amplitude; O(g^2), O(g^4), all orders)
G4  trapped (spectator-spectator) versus deformable (active-spectator) k^+ contours, exact boson propagator
G5  sum over cuts / eikonal identities (symbolic)

Numerical contour integrals: the real-axis integral with Feynman i0's is evaluated EXACTLY (no small-delta
regulators) on an indented contour that passes above every pole lying (infinitesimally) in the lower half plane
and below every pole in the upper half plane; tails |x| > X are added analytically.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import integrate, special
from itertools import permutations
from fractions import Fraction

RES = []
def report(name, ok, extra=''):
    RES.append((name, bool(ok)))
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)


def contour_int(f, bumps, X, tail=0.0):
    """int_{-X}^{X} dx f(k(x)) k'(x) + tail,  k(x) = x + i sum_j s_j h_j phi((x-x_j)/w_j),  phi(u) = (1-u^2)^2 (|u|<1).
    bumps: list of (x_j, s_j*h_j, w_j)."""
    def kk(x):
        val = x + 0j; der = 1 + 0j
        for xj, hj, wj in bumps:
            uu = (x - xj) / wj
            if abs(uu) < 1:
                val += 1j * hj * (1 - uu**2)**2
                der += 1j * hj * (-4 * uu * (1 - uu**2)) / wj
        return val, der
    def g(x, part):
        k_, d_ = kk(x)
        v_ = f(k_) * d_
        return v_.real if part == 0 else v_.imag
    pts = sorted(set([p for xj, hj, wj in bumps for p in (xj - wj, xj, xj + wj) if -X < p < X]))
    re = integrate.quad(g, -X, X, args=(0,), points=pts, limit=10000, epsabs=1e-13, epsrel=1e-12)[0]
    im = integrate.quad(g, -X, X, args=(1,), points=pts, limit=10000, epsabs=1e-13, epsrel=1e-12)[0]
    return re + 1j * im + tail

# ============================================================== G1: position-space eikonal phase
def lfdot(a, b):   # light-front components (v^+, v^-, v_T1, v_T2)
    return a[0] * b[1] + a[1] * b[0] - (a[2] * b[2] + a[3] * b[3])
vA = (1, 0, 0, 0); vB = (0, 1, 0, 0)
report('G1 light-like eikonal lines: v_A^2 = v_B^2 = 0 (self-energies vanish in Feynman gauge), v_A.v_B = 1',
       lfdot(vA, vA) == 0 and lfdot(vB, vB) == 0 and lfdot(vA, vB) == 1)
mp.mp.dps = 20
def ft2d(b, m):
    f = lambda k: k * mp.besselj(0, k * b) / (k**2 + m**2)
    return mp.quadosc(f, [0, mp.inf], omega=b) / (2 * mp.pi)
okft = all(abs(ft2d(b, m) - mp.besselk(0, m * b) / (2 * mp.pi)) < 1e-12 for b, m in [(0.7, 1.3), (2.0, 0.4), (5.0, 0.05)])
report('G1 2D Fourier transform: int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = K_0(mb)/(2pi)  (3 points, quadosc)', okft)
bb, mm = 1.0, 1e-4
chi_exact = -float(special.k0(mm * bb)) / (2 * np.pi)
chi_coul = (np.log(mm * bb / 2) + np.euler_gamma) / (2 * np.pi)
report('G1 Coulomb limit: chi(b) -> (g_A g_B/2pi)[ln(mb/2)+gamma_E]: IR-divergent but real (a pure phase)', abs(chi_exact - chi_coul) < 1e-6,
       '(g_A g_B = 1, m b = 1e-4: %.10f vs %.10f)' % (chi_exact, chi_coul))

# ============================================================== G2: momentum-space spectator-spectator graph
# k^- integral of the A-side propagators (Glauber region, leading power):
#   s_A (momentum p'_A - k, p'_A on shell):  i/(-2P1 (k^- - k1) + i0)   -> pole in UHP  (pass below)
#   a   (momentum P_A - p'_A + k):           i/( 2P2 (k^- - k2) + i0)   -> pole in LHP  (pass above)
P1, P2, k1, k2 = 0.6, 0.4, 0.013, -0.021
fA = lambda k: (1j / (-2 * P1 * (k - k1))) * (1j / (2 * P2 * (k - k2))) / (2 * np.pi)
Xc = 4000.0
JA = contour_int(fA, [(k1, -0.004, 0.01), (k2, +0.004, 0.01)], Xc, tail=2 * (1 / (4 * P1 * P2 * Xc)) / (2 * np.pi))
pred = (1 / (2 * P1)) * (1j / (2 * P2 * (k1 - k2)))
report('G2 k^- integral = (1/2P^+_{s_A}) x [a propagator at s_A on shell]  (exact contour; s_A pole UHP, a pole LHP)',
       abs(JA - pred) / abs(pred) < 1e-8, '(%.8f%+.8fi vs %.8f%+.8fi)' % (JA.real, JA.imag, pred.real, pred.imag))
# the opposite assignment (a pole also in the UHP) would give zero -- i.e. the result really comes from the trapped pair
JA_wrong = contour_int(lambda k: (1j / (-2 * P1 * (k - k1))) * (1j / (-2 * P2 * (k - k2))) / (2 * np.pi), [(k1, -0.004, 0.01), (k2, -0.004, 0.01)], Xc,
                       tail=2 * (-1 / (4 * P1 * P2 * Xc)) / (2 * np.pi))
report('G2 control: if both A-side poles were in the UHP the k^- integral would vanish (close below)', abs(JA_wrong) < 1e-8 * abs(pred), '(|J| = %.1e)' % abs(JA_wrong))
gA_, gB_, PA_, PB_, kT2, m2 = sp.symbols('g_A g_B P_A P_B k_T2 m2', positive=True)
kernel = sp.simplify((1 / (2 * PA_)) * (1 / (2 * PB_)) * (sp.I * gA_) * (sp.I * gB_) * (4 * PA_ * PB_) * (-sp.I) / (-kT2 - m2))
report('G2 one-loop spectator-spectator graph = int d^2k_T/(2pi)^2 [-i g_A g_B/(k_T^2+m^2)] M0(p_A-k, p_B+k)  (= G1 phase at O(g^2))',
       sp.simplify(kernel - (-sp.I * gA_ * gB_ / (kT2 + m2))) == 0, '  [kernel = %s]' % kernel)

# ============================================================== G3: unitarity -- numerical demonstration
N = 512; Lbox = 48.0; dp = Lbox / N
p = (np.arange(N) - N // 2) * dp
PX, PY = np.meshgrid(p, p, indexing='ij')
M0 = np.exp(-((PX - 0.8)**2 + (PY + 0.3)**2) / 2.0) * np.exp(1j * (1.3 * PX * PY + 0.7 * PX))   # complex toy amplitude
g2 = 1.7; mB = 0.5
Kt = -1j * g2 / (PX**2 + PY**2 + mB**2)                  # i chi~(k): purely imaginary and even
Kt[0, :] = 0.0; Kt[:, 0] = 0.0                            # drop the unpaired edge momentum so the grid kernel is exactly even
def conv(A, B):
    FA = np.fft.fft2(np.pad(A, ((0, N), (0, N)))); FB = np.fft.fft2(np.pad(B, ((0, N), (0, N))))
    C = np.fft.ifft2(FA * FB); s0 = N // 2
    return C[s0:s0 + N, s0:s0 + N] * dp**2 / (2 * np.pi)**2
M1 = conv(Kt, M0)
M2 = 0.5 * conv(Kt, conv(Kt, M0))
I0 = np.sum(np.abs(M0)**2) * dp**2
I1_point = 2 * np.real(np.conj(M0) * M1)
I1 = np.sum(I1_point) * dp**2
I2 = np.sum(np.abs(M1)**2 + 2 * np.real(np.conj(M0) * M2)) * dp**2
scale1 = np.sum(np.abs(I1_point)) * dp**2; scale2 = np.sum(np.abs(M1)**2) * dp**2
report('G3 O(g^2): pointwise 2Re(M0* M1) != 0 but its integral over the spectator relative k_T vanishes',
       scale1 > 1e-2 * I0 and abs(I1) < 1e-12 * scale1, '(int|.| = %.3e, int = %.1e)' % (scale1, I1))
report('G3 O(g^4): int [|M1|^2 + 2Re(M0* M2)] = 0  (cuts through the exchanges summed)', abs(I2) < 1e-12 * scale2,
       '(int|M1|^2 = %.3e, sum = %.1e)' % (scale2, I2))
F0 = np.fft.fft2(np.pad(M0, ((0, N), (0, N))))
FK = np.fft.fft2(np.pad(Kt, ((0, N), (0, N)))) * dp**2 / (2 * np.pi)**2
kx = np.fft.fftfreq(2 * N) * 2 * N
shift = np.exp(-2j * np.pi * (N // 2) * (kx[:, None] + kx[None, :]) / (2 * N))
ichi = FK / shift
report('G3 discretised i*chi(b) is purely imaginary (chi real): the exchange is a pure phase in b-space',
       np.max(np.abs(ichi.real)) < 1e-10 * np.max(np.abs(ichi.imag)), '(max|Re|/max|Im| = %.1e)' % (np.max(np.abs(ichi.real)) / np.max(np.abs(ichi.imag))))
Mall = np.fft.ifft2(F0 * np.exp(ichi))
Iall = np.sum(np.abs(Mall)**2) * dp**2
report('G3 all orders: int |e^{i chi} (x) M0|^2 = int |M0|^2 (|e^{i chi}| = 1)', abs(Iall / I0 - 1) < 1e-12, '(ratio %.15f)' % (Iall / I0))
P2_0 = np.sum((PX**2 + PY**2) * np.abs(M0)**2) * dp**2 / I0
dP2 = np.sum((PX**2 + PY**2) * (2 * np.real(np.conj(M0) * M1) + np.abs(M1)**2 + 2 * np.real(np.conj(M0) * M2))) * dp**2 / I0
report('G3 ... while the spectator relative-k_T distribution IS changed (exchange is not trivial)', abs(dP2) > 1e-3,
       '(<p^2> = %.4f, shift through O(g^4) = %.4f)' % (P2_0, dP2))

# ============================================================== G4: trapped versus deformable k^+ contours
lam = 0.1                         # power counting: A-collinear (1, lam^2, lam), B-collinear (lam^2, 1, lam), Glauber (lam^2, lam^2, lam)
Pb, Ps = 1.0, 0.8                 # minus momenta of b and s_B (~Q = 1)
cb = 0.6 * lam**2                 # active b after absorbing k:  (p_b + k)^2 - m^2 ~ 2 Pb k^+ + cb,  pole at -cb/(2Pb) - i0 (LHP)
kap_s, kap_b = 0.35 * lam**2, -0.5 * lam**2    # spectator-spectator: s_B pole kap_s - i0 (LHP), b pole kap_b + i0 (UHP)
K2 = 1.3 * lam**2                 # k_T^2 + m^2
XG = 3000.0
def f_as(kp, km):  return 1.0 / ((2 * Pb * kp + cb) * (2 * kp * km - K2))
def f_eik(kp, km): return 1.0 / ((2 * Pb * kp) * (2 * kp * km - K2))
def f_ss(kp, km):  return 1.0 / ((2 * Ps * (kp - kap_s)) * (-2 * Pb * (kp - kap_b)) * (2 * kp * km - K2))
def boson_bump(km):
    # boson pole k^+ = (K2 - i0)/(2k^-): LHP for k^- > 0 (pass above), UHP for k^- < 0 (pass below)
    xb = K2 / (2 * km)
    return (xb, (+1 if km > 0 else -1) * 0.02, 0.1)
def tail_as(km):   # f ~ 1/(4 Pb k^- x^2)
    return 2.0 / (4 * Pb * km * XG)
def res_as(km):    # exact real-axis value: 2 pi i theta(-k^-)/(2 Pb K2 + 2 k^- cb)
    return 2j * np.pi / (2 * Pb * K2 + 2 * km * cb) if km < 0 else 0.0
for km in (-0.6 * lam**2, +0.6 * lam**2):
    exact = res_as(km)
    # (i) real axis with i0's (tiny indentation: above the b pole, boson pole per its i0)
    real_axis = contour_int(lambda k: f_as(k, km), [(-cb / (2 * Pb), +0.001, 0.003), boson_bump(km)], XG, tail_as(km))
    # (ii) deformed into the UHP by ~lam over |x| < 3 lam (>> Glauber scale lam^2, << boson-pole distance ~ 1)
    deformed = contour_int(lambda k: f_as(k, km), [(0.0, +lam, 3 * lam), boson_bump(km)], XG, tail_as(km))
    ok = (abs(real_axis - exact) < 1e-7 * max(1, abs(exact))) and (abs(deformed - exact) < 1e-7 * max(1, abs(exact)))
    report('G4 active(b)-spectator(s_A), k^- = %+.4f: real-axis value = residue formula, and = value on contour lifted by ~i lam' % km, ok,
           '(real %.6f%+.6fi, lifted %.6f%+.6fi, formula %.6f%+.6fi)' % (real_axis.real, real_axis.imag, deformed.real, deformed.imag, complex(exact).real, complex(exact).imag))
    if km < 0:
        eik = contour_int(lambda k: f_eik(k, km), [(0.0, +lam, 3 * lam), boson_bump(km)], XG, tail_as(km))
        rel = abs(eik - exact) / abs(exact)
        report('G4   ... on the lifted contour b may be replaced by the eikonal line 1/(2P_b^- k^+ + i0): rel. error O(c_b |k^-|/(P_b K^2)) ~ lam^2',
               rel < lam**2, '(rel. error %.2e; the result comes from the boson pole k^+ = -K^2/(2|k^-|) = %.2f, |k^+| ~ Q: A-collinear)' % (rel, -K2 / (2 * abs(km))))
def ss_exact(km):
    if km > 0:   # close in UHP: only the b pole (kap_b + i0)
        return 2j * np.pi * (1.0 / (2 * Ps * (kap_b - kap_s))) * (1.0 / (-2 * Pb)) * (1.0 / (2 * kap_b * km - K2))
    # close in LHP: only the s_B pole (kap_s - i0)
    return -2j * np.pi * (1.0 / (2 * Ps)) * (1.0 / (-2 * Pb * (kap_s - kap_b))) * (1.0 / (2 * kap_s * km - K2))
for km in (+0.6 * lam**2, -0.6 * lam**2):
    exact = ss_exact(km)
    ind = [(kap_s, +0.0008, 0.002), (kap_b, -0.0008, 0.002), boson_bump(km)]
    real_axis = contour_int(lambda k: f_ss(k, km), ind, XG)
    up = contour_int(lambda k: f_ss(k, km), [(0.0, +lam, 3 * lam), boson_bump(km)], XG)
    down = contour_int(lambda k: f_ss(k, km), [(0.0, -lam, 3 * lam), boson_bump(km)], XG)
    glauber = exact * (2 * (kap_b if km > 0 else kap_s) * km - K2) / (-K2)
    ok_real = abs(real_axis - exact) < 1e-7 * abs(exact)
    report('G4 spectator-spectator, k^- = %+.4f: real-axis value = Glauber-scale residue formula' % km, ok_real,
           '(real %.4f%+.4fi, formula %.4f%+.4fi)' % (real_axis.real, real_axis.imag, exact.real, exact.imag))
    crossed = abs(up - exact) > 0.5 * abs(exact) and abs(down - exact) > 0.5 * abs(exact)
    report('G4   ... lifting OR lowering the k^+ contour by i lam changes the value (crosses the b or s_B pole): contour trapped', crossed,
           '(lifted %.2f%+.2fi, lowered %.2f%+.2fi)' % (up.real, up.imag, down.real, down.imag))
    report('G4   ... and at the residue point boson -> -1/(k_T^2+m^2) (Glauber approximation) is accurate', abs(glauber / exact - 1) < lam**2,
           '(|Glauber/exact - 1| = %.1e)' % abs(glauber / exact - 1))

# ============================================================== G5: sum over cuts and eikonal identities
X = sp.Symbol('chi', real=True)
okcuts = all(sp.simplify(sum((sp.I * X)**j / sp.factorial(j) * (-sp.I * X)**(n - j) / sp.factorial(n - j) for j in range(n + 1))) == 0 for n in range(1, 9))
report('G5 sum over cut positions at order g^{2n}: sum_j (i chi)^j/j! (-i chi)^{n-j}/(n-j)! = 0, n=1..8', okcuts)
ws = sp.symbols('w1:5')
oke = True
for n in range(2, 5):
    lhs = sum(sp.prod([1 / sum(ws[s_] for s_ in perm[:j + 1]) for j in range(n)]) for perm in permutations(range(n)))
    oke = oke and sp.simplify(sp.together(lhs) - sp.prod([1 / ws[i] for i in range(n)])) == 0
rng = np.random.default_rng(5)
for trial in range(3):   # n = 5, 6 with exact rational arithmetic at random points
    for n in (5, 6):
        w = [Fraction(int(rng.integers(1, 97)), int(rng.integers(1, 89))) for _ in range(n)]
        lhs = sum(np.prod([1 / sum(w[s_] for s_ in perm[:j + 1]) for j in range(n)]) for perm in permutations(range(n)))
        rhs = np.prod([1 / wi for wi in w])
        oke = oke and (lhs == rhs)
report('G5 eikonal identity: sum_{perms} prod_j 1/(w_s1+...+w_sj) = prod_j 1/w_j  (symbolic n=2..4; exact rationals n=5,6)', oke)
def lhs_n2(delta):
    phi = lambda w1, w2: np.exp(-(w1 - 0.3)**2 - 2 * (w2 + 0.1)**2 - 0.5 * w1 * w2)
    f = lambda w1: (1j / (w1 + 1j * delta) + 1j / (-w1 + 1j * delta)) * phi(w1, -w1)
    re = integrate.quad(lambda w: f(w).real, -30, 30, points=[0.0], limit=2000)[0]
    im = integrate.quad(lambda w: f(w).imag, -30, 30, points=[0.0], limit=2000)[0]
    return 2 * np.pi * (re + 1j * im)
target = (2 * np.pi)**2 * np.exp(-0.09 - 0.02)
vals = [lhs_n2(d) for d in (1e-2, 1e-3)]
report('G5 on-shell eikonal identity n=2: 2pi delta(w1+w2)[i/(w1+i0)+i/(w2+i0)] = (2pi)^2 delta(w1)delta(w2)  (test function)',
       abs(vals[-1] - target) / abs(target) < 5e-3, '(delta=1e-2: %.5f, 1e-3: %.5f, target %.5f)' % (vals[0].real, vals[1].real, target))
kk = sp.Symbol('k', real=True); eta = sp.Symbol('eta', positive=True); lmb = sp.Symbol('lambda', real=True)
past = sp.simplify(sp.integrate(sp.exp(sp.I * lmb * (kk - sp.I * eta)), (lmb, -sp.oo, 0), conds='none'))
fut = sp.simplify(sp.integrate(sp.exp(sp.I * lmb * (kk + sp.I * eta)), (lmb, 0, sp.oo), conds='none'))
report('G5 semi-infinite lines: past-pointing factor -i/(k - i0), future-pointing i/(k + i0)',
       sp.simplify(past + sp.I / (kk - sp.I * eta)) == 0 and sp.simplify(fut - sp.I / (kk + sp.I * eta)) == 0)
report('G5 past + future = 2 eta/(k^2+eta^2) -> 2 pi delta(k) (infinite line): each carries pi delta(k), principal parts opposite',
       sp.simplify(past + fut - 2 * eta / (kk**2 + eta**2)) == 0)

print()
print('SUMMARY glauber_toy: %d/%d PASS' % (sum(ok for _, ok in RES), len(RES)))
