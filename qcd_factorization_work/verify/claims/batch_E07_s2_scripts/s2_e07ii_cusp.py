# E07(ii) stage-2 check: two-loop cusp anomalous dimension at Euclidean angle pi/2 vs the
# constant term gamma_HH of the large-hyperbolic-angle limit.
# Normalization: Gamma(alpha_s, angle) = (as/pi) Gamma1 + (as/pi)^2 Gamma2 + ..., d/dln(mu) of one cusp,
# Gamma1 = C_F (theta coth theta - 1) (Minkowski), = C_F (phi cot phi - 1) for theta = i phi (Euclidean).
# Source A: Kidonakis PRL 102 (2009) 232003 (arXiv:0903.2561) eq. (9) (Minkowski cusp angle gamma),
#           continued analytically to gamma = i phi  [exact evaluation: coth(i pi/2) = 0].
# Source B: Grozin-Henn-Korchemsky-Marquard JHEP 01 (2016) 140 (arXiv:1510.07803) eqs. (2.14), (5.2)-(5.5),
#           natively Euclidean, x = e^{i phi}; HPLs evaluated numerically along the path y = 1 - x^2.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
mp.mp.dps = 30
z2, z3 = mp.zeta(2), mp.zeta(3)

# ---------- Source A: Kidonakis eq. (9), C_F C_A and C_F n_f parts separately (coefficients of (as/pi)^2)
def kid(g, part):
    g = mp.mpc(g)
    cth = mp.cosh(g)/mp.sinh(g)
    G1 = g*cth - 1                 # Gamma_S^(1)/C_F
    E = mp.exp(-2*g)
    if part == 'CA':               # coefficient of C_F C_A
        K2 = (mp.mpf(67)/18 - z2)/2
        rest = (mp.mpf(1)/2 + z2/2 + g**2/2
                - cth**2/2*(z3 - z2*g - g**3/3 - g*mp.polylog(2, E) - mp.polylog(3, E))
                - cth/2*(z2 + z2*g + g**2 + g**3/3 + 2*g*mp.log(1 - E) - mp.polylog(2, E)))
        return K2*G1 + rest
    else:                          # coefficient of C_F n_f  (K = ... - 5 n_f/9)
        return -mp.mpf(5)/18*G1

# exact Euclidean pi/2 by hand: coth(i pi/2)=0, (i pi/2)^2/2 = -pi^2/8, G1 = -1
exactA_CA = -(mp.mpf(67)/18 - z2)/2 + mp.mpf(1)/2 + z2/2 - mp.pi**2/8
print('A: Kidonakis at gamma = i pi/2 (exact by hand), C_F C_A coeff =', exactA_CA,
      ' vs pi^2/24 - 49/36 =', mp.pi**2/24 - mp.mpf(49)/36)
for phi in [mp.pi/2 - mp.mpf('1e-8'), mp.pi/2 - mp.mpf('1e-3'), mp.mpf('1.2')]:
    print('   numeric gamma = i*phi, phi =', mp.nstr(phi, 12), ': CA part', mp.nstr(kid(1j*phi, 'CA'), 15),
          ' nf part', mp.nstr(kid(1j*phi, 'nf'), 15))
for th in [10, 20, 40]:
    th = mp.mpf(th)
    cusp2 = (mp.mpf(67)/18 - z2)/2
    print('   large Minkowski angle theta =', th, ': CA part - theta*Gamma_cusp^(2)_CA =',
          mp.nstr(kid(th, 'CA').real - th*cusp2, 15), ' ; nf part - theta*(-5/18) =',
          mp.nstr(kid(th, 'nf').real + th*mp.mpf(5)/18, 15))
print('   expected gamma_HH^(2): CA', -mp.mpf(49)/36 + mp.pi**2/12 - z3/2, ' nf(=5/9 T_F n_f, T_F=1/2) +5/18')

# ---------- Source B: GHKM HPL representation (Euclidean, x = e^{i phi}, y = 1 - x^2)
def hpls(phi):
    # continuation along y(p) = 1 - e^{2 i p}, p in [0, phi]  (Im y < 0 for 0 < p < pi/2)
    x = mp.exp(1j*phi)
    y = 1 - x**2
    L = 2j*phi                       # ln(1-y) = ln(x^2) continued from 0
    H1 = -L
    H11 = L**2/2
    H111 = -L**3/6
    H01 = mp.polylog(2, y) if abs(phi - mp.pi/2) > mp.mpf('1e-25') else mp.polylog(2, mp.mpc(2, -1e-40))
    H101 = -2j*mp.quad(lambda p: mp.polylog(2, 1 - mp.exp(2j*p)), [0, phi])
    xi = (1 + x**2)/(1 - x**2)
    return xi, H1, H01, H11, H111, H101

def A123(phi):
    xi, H1, H01, H11, H111, H101 = hpls(phi)
    A1 = xi*H1/2
    A2 = (mp.pi**2/3 + H11/2) + xi*(-H01 - H11/2)
    A3 = xi*(-mp.pi**2/6*H1 - H111/4) + xi**2*(H101/2 + H111/4)
    return A1, A2, A3

# values at x = 1 (zero cusp angle) as limits
for eps in ['1e-4', '1e-6']:
    A1, A2, A3 = A123(mp.mpf(eps))
    print('B: small-angle limits phi =', eps, ': A1 =', mp.nstr(A1, 12), ' A2 =', mp.nstr(A2, 12),
          '(pi^2/3-2 =', mp.nstr(mp.pi**2/3 - 2, 12), ')  A3 =', mp.nstr(A3, 12), '(1-pi^2/3 =', mp.nstr(1 - mp.pi**2/3, 12), ')')
A1_1, A2_1, A3_1 = mp.mpf(1), mp.pi**2/3 - 2, 1 - mp.pi**2/3

def gamma2_GHKM(phi):
    A1, A2, A3 = A123(phi)
    t1, t2, t3 = A1 - A1_1, A2 - A2_1, A3 - A3_1
    CA = (t2 + t3)/2 + mp.mpf(67)/36*t1     # coefficient of C_R C_A
    TFnf = -mp.mpf(5)/9*t1                    # coefficient of C_R T_F n_f
    return CA, TFnf, t1

for phi in [mp.mpf('0.7'), mp.mpf('1.2'), mp.pi/2 - mp.mpf('1e-6')]:
    CA, TFnf, t1 = gamma2_GHKM(phi)
    print('B vs A at phi =', mp.nstr(phi, 10), ': GHKM CA =', mp.nstr(CA, 14), ' Kidonakis CA =', mp.nstr(kid(1j*phi, 'CA'), 14),
          ' | GHKM T_F n_f =', mp.nstr(TFnf, 12), ' Kid. n_f part*2 =', mp.nstr(2*kid(1j*phi, 'nf'), 12))
# exact at pi/2 using xi = 0
Ad2 = mp.pi**2/3 + (2j*mp.pi/2)**2/4      # pi^2/3 + (1/2)H11, H11 = L^2/2, L = i pi
t2 = Ad2 - A2_1; t3 = 0 - A3_1; t1 = -1
print('B exact at phi = pi/2 (xi=0): A~2 =', mp.nstr(t2, 15), '(2 - pi^2/4 =', mp.nstr(2 - mp.pi**2/4, 15), '), A~3 =', mp.nstr(t3, 15),
      ' => CA coeff', mp.nstr((t2 + t3)/2 + mp.mpf(67)/36*t1, 15))

# large Minkowski angle from GHKM: phi = -i theta  (x = e^{theta}?)  use x = e^{-theta} real in (0,1)
def gamma2_GHKM_mink(theta):
    x = mp.exp(-mp.mpf(theta)); y = 1 - x**2; L = mp.log(x**2)
    H1 = -L; H11 = L**2/2; H111 = -L**3/6; H01 = mp.polylog(2, y)
    H101 = mp.quad(lambda tt: mp.polylog(2, tt)/(1 - tt), [0, y])
    xi = (1 + x**2)/(1 - x**2)
    A1 = xi*H1/2
    A2 = (mp.pi**2/3 + H11/2) + xi*(-H01 - H11/2)
    A3 = xi*(-mp.pi**2/6*H1 - H111/4) + xi**2*(H101/2 + H111/4)
    t1, t2, t3 = A1 - A1_1, A2 - A2_1, A3 - A3_1
    return (t2 + t3)/2 + mp.mpf(67)/36*t1, t1
for th in [8, 16, 30]:
    CA, t1 = gamma2_GHKM_mink(th)
    print('B: large Minkowski angle theta =', th, ': Gamma1/C_F =', mp.nstr(t1, 10), ' CA coeff - theta*(67/36 - pi^2/12) =',
          mp.nstr(CA - th*(mp.mpf(67)/36 - mp.pi**2/12), 14))

# ---------- symbolic summary
pi, zeta3 = sp.pi, sp.zeta(3)
G_pi2 = sp.Rational(-49, 36) + pi**2/24
G_HH = sp.Rational(-49, 36) + pi**2/12 - zeta3/2
d = sp.simplify(G_pi2 - G_HH)
print('Gamma^(2)(pi/2) - gamma_HH^(2) (C_F C_A coefficient, units (as/pi)^2) =', d, '=', sp.N(d, 12))
print('n_f parts: both (5/9) C_F T_F n_f -> difference 0;  one loop: both = -C_F')
