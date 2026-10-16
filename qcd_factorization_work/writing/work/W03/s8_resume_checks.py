"""
W03 s8 -- checks added in the resume session (2026-10-14) for statements (re)written then.
  R1  reversed path ordering: V = Pbar exp(ig int_a^b dz.A) transforms as U(a) V U^dag(b) under the Collins-convention
      gauge transformation A' = U A U^-1 + (i/g)(dU)U^-1 (i.e. V is Collins' Wilson line P exp(-ig int) from b to a);
      under OUR transformation A' = U A U^-1 - (i/g)(dU)U^-1 it is covariant in neither way (cf. s2 C1).
  R2  eps^{mu nu rho sigma} F_{mu nu} F_{rho sigma} = -8 E.B for eps^{0123} = +1 (used in the E||B sign check of the ABJ
      anomaly: d.j5 = +(e^2/2pi^2) E.B  <=>  d.j5 = -(e^2/16pi^2) eps F F, i.e. c = -1 of s6 G8 in our convention).
  R3  gluon polarization average: averaging over 2 instead of D-2 polarizations multiplies the partonic gluon structure
      function (c_dis R_2^g, normalized as F^g/(z e_q^2) = (as/2pi)[-(2/eps) P_qg + 2 C_2^g]) by (1-eps):
      shift 2 P_qg in R_2^g, i.e. C_2^g -> C_2^g + P_qg (VF-CONV-6).
  R4  DGLAP consistency of the pure-DR partonic PDF f = delta - (as/2pi)(1/eps) P (VF-PDF-5) with
      mu^2 d as/d mu^2 = -eps as + O(as^2) in D = 4 - 2 eps.
  R5  first moment of the Mertig-van Neerven finite renormalization z_qq(x) = -8 C_F (1-x) (units g^2/16pi^2):
      -4 C_F, i.e. Z_5^ns = 1 - 4 C_F as/(4 pi) (VF-POL-1, T-status coefficient).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy.linalg import expm

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

# ---------------- R1 ----------------
rng = np.random.default_rng(7)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
t = [s / 2 for s in sig]
g = 0.9
N = 4000
s_grid = (np.arange(N) + 0.5) / N; ds = 1.0 / N
c1, c2 = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
def a_of(s):    # zdot.A(z(s)) along the path, smooth hermitian traceless
    return sum((c1[k, 0] + c1[k, 1] * np.sin(2 * s + c1[k, 2]) + c2[k, 0] * s**2) * t[k] for k in range(3))
d1 = rng.normal(size=(3, 2))
def theta(s): return sum((d1[k, 0] * np.cos(1.3 * s + d1[k, 1])) * t[k] for k in range(3))
def U(s): return expm(1j * theta(s))
def dU(s, h=1e-6): return (U(s + h) - U(s - h)) / (2 * h)
def Pexp(afun, reverse):
    M = np.eye(2, dtype=complex)
    for s in s_grid:
        step = expm(1j * g * afun(s) * ds)
        M = (M @ step) if reverse else (step @ M)     # reverse: earlier points left; else later points left
    return M
V = Pexp(a_of, True)
a_collins = lambda s: U(s) @ a_of(s) @ np.linalg.inv(U(s)) + (1j / g) * dU(s) @ np.linalg.inv(U(s))
a_ours = lambda s: U(s) @ a_of(s) @ np.linalg.inv(U(s)) - (1j / g) * dU(s) @ np.linalg.inv(U(s))
Vc = Pexp(a_collins, True)
err_c = np.abs(Vc - U(0) @ V @ U(1).conj().T).max()
Vo = Pexp(a_ours, True)
err_o1 = np.abs(Vo - U(0) @ V @ U(1).conj().T).max(); err_o2 = np.abs(Vo - U(1) @ V @ U(0).conj().T).max()
check('R1 Pbar exp(ig int A) -> U(a) V U^dag(b) under the Collins-convention transformation (g -> -g)', err_c < 1e-5,
      'err = %.1e' % err_c)
check('R1 ... and is covariant in neither way under our transformation', min(err_o1, err_o2) > 1e-2,
      'errs = %.2e, %.2e' % (err_o1, err_o2))

# ---------------- R2 ----------------
import itertools
def levi(*i): return float(sp.LeviCivita(*i))
eta = np.diag([1., -1, -1, -1])
E = rng.normal(size=3); B = rng.normal(size=3)
F_up = np.zeros((4, 4))           # F^{mu nu}: F^{i0} = E^i, F^{ij} = -eps_{ijk} B^k
for i in range(3):
    F_up[i + 1, 0] = E[i]; F_up[0, i + 1] = -E[i]
    for j in range(3):
        F_up[i + 1, j + 1] = -sum(levi(i, j, k) * B[k] for k in range(3))
F_dn = eta @ F_up @ eta
epsFF = sum(levi(m, n, r, s_) * F_dn[m, n] * F_dn[r, s_] for m, n, r, s_ in itertools.permutations(range(4)))
check('R2 eps^{mnrs} F_mn F_rs = -8 E.B (eps^{0123} = +1)', abs(epsFF + 8 * E @ B) < 1e-12,
      'epsFF = %.6f, -8E.B = %.6f' % (epsFF, -8 * E @ B))
# consistency of the field-strength convention: F_{0i} = E^i for A^mu = (phi, A), E = -grad phi - dA/dt
check('R2 F_{0i} = E^i with this convention', np.allclose([F_dn[0, i + 1] for i in range(3)], E))

# ---------------- R3 ----------------
e, z = sp.symbols('epsilon z', positive=True)
P = z**2 + (1 - z)**2
R2g = 2 * sp.exp(e * sp.EulerGamma) * sp.gamma(-e) / sp.gamma(2 - 2 * e) * (z / (1 - z))**e * (P - 3 * e + 4 * e**2 - 2 * e**3) / (1 - e)**2
ser = sp.series(R2g, e, 0, 1).removeO()
C2g = sp.simplify((ser.coeff(e, 0)) / 2)     # R_2^g = -(2/eps) P + 2 C_2^g/T_F + O(eps)
okpole = sp.simplify(ser.coeff(e, -1) + 2 * P) == 0
# (sympy does not simplify the log forms to zero; compare at several points to 25 digits)
okC = all(abs(sp.N((C2g - (P * sp.log((1 - z) / z) - 8 * z**2 + 8 * z - 1)).subs(z, zv), 25)) < 1e-20
          for zv in (sp.Rational(1, 10), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(7, 10), sp.Rational(9, 10)))
ser2 = sp.series((1 - e) * R2g, e, 0, 1).removeO()
shift = sp.simplify((ser2.coeff(e, 0) - ser.coeff(e, 0)) / 2)
check('R3 c_dis R_2^g = -(2/eps)P + 2[P ln((1-z)/z) - 8z^2 + 8z - 1] + O(eps)', okpole and okC)
check('R3 averaging over 2 polarizations: C_2^g -> C_2^g + P_qg (VF-CONV-6)', sp.simplify(shift - P) == 0, 'shift/T_F = %s' % sp.factor(shift))

# ---------------- R4 ----------------
a_s, mu, Pq = sp.symbols('alpha_s mu P_qq')
f = 1 - a_s / (2 * sp.pi) / e * Pq                  # coefficient structure (delta -> 1)
dadlnmu2 = -e * a_s                                  # mu^2 d a_s/d mu^2 at lowest order in D dims
dfdlnmu2 = sp.diff(f, a_s) * dadlnmu2
check('R4 pure-DR f = delta - (as/2pi)(1/eps)P obeys df/dln mu^2 = (as/2pi) P at O(as)', sp.simplify(dfdlnmu2 - a_s / (2 * sp.pi) * Pq) == 0)

# ---------------- R5 ----------------
x, CF = sp.symbols('x C_F')
m1 = sp.integrate(-8 * CF * (1 - x), (x, 0, 1))
check('R5 first moment of z_qq = -8 C_F (1-x) is -4 C_F (Z_5^ns = 1 - 4 C_F as/4pi)', sp.simplify(m1 + 4 * CF) == 0, 'moment = %s' % m1)

print('\nSUMMARY s8: %d/%d PASS' % (sum(PASS), len(PASS)))
