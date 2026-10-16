"""R-m26 checks (minor corrections m26, m27 of reference App. E; independent code).

(a) Lemma E.28(iii): with E(k) = J^fi(k) + i J_+/(k - i lamJ) (analytic in the closed LHP, O(k^-2)) and
    R_down(k) = sum_i r_i/(k - z_i), Im z_i < 0:  int dk/2pi E R_down = -i sum_i r_i E(z_i)  (close in the LHP),
    and |E(z)| <= 2 M lamJ/|z|^2 for Im z <= 0, |z| >= 2 lamJ (M the constant of (J2)).
(c) (E.30): Lemma E.28(iii) gives an ABSOLUTE error O(M lamJ ||R||/Lambda); relative to R(0)J(0) it is
    (M/|J(0)|) lamJ/Lambda, unbounded when J(0) << M.  Numerical counterexample to the relative form.
(d) (E.51): A1 = -i chi X, A2 = (1/2)(-i chi)^2 (X^2 + C_A X/4)  with  sum_ab {T^a,T^b}{T'^a,T'^b} = 4X^2 + C_A X;
    (1+A1+A2)^dag (1+A1+A2) = 1 - (1/4) C_A chi^2 X + O(chi^3): the compensating term needed is +(1/4) C_A chi^2 X.
(f) ordering weights: two insertions with single poles z_j = kTj^2/(2 kj^+) in the LHP: weight of
    'insertion 1 first' = z1/(z1+z2); N-insertion formula prod z_j / prod_m sum_{l>=m} z_pi(l); sum = 1.
    The weights depend on kTj^2 as well as kj^+.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp

# ---------------- (a) ----------------
lamJ = 0.05
a1, a2, a3 = 0.03, -0.04, 0.02          # final-state energies A'_D, |A'_D| <= lamJ
c1, c2 = 0.7+0.2j, -1.3+0.5j
eta0 = 0.01            # finite i0: poles at A'_D + i eta0 in the UHP, |pole| <= lamJ
def Jfi(k):   # LCOPT-type final-state factor: poles at k = A'_D + i eta0 (UHP) -> analytic in the closed LHP
    return c1/(a1 + 1j*eta0 - k) + c2/((a2 + 1j*eta0 - k)*(a3 + 1j*eta0 - k))
Jplus = -1j*c1          # J^fi ~ -c1/k ; J^fi + i J_+/k = O(k^-2)  =>  J_+ = -i c1
def E(k): return Jfi(k) + 1j*Jplus/(k - 1j*lamJ)
# constant M of (J2) for |k| >= 2 lamJ, Im k <= 0 : estimate sup |k|^2 |Jfi + i J+/k| / lamJ on a grid (and |J+|)
grid = [r*np.exp(1j*th) for r in np.geomspace(2*lamJ, 1e4, 400) for th in np.linspace(-np.pi, 0, 200)]
M = max(max(abs(k)**2*abs(Jfi(k) + 1j*Jplus/k)/lamJ for k in grid), abs(Jplus))
ratio = max(abs(E(k))*abs(k)**2/(lamJ*M) for k in grid)
print(f"(a) M = {M:.4f};  max |E(z)| |z|^2/(M lamJ) over Im z<=0, |z|>=2 lamJ : {ratio:.4f}  (claim <= 2; reference used 3)")
# R_down with poles in the LHP at |z_i| >= 2 Lambda, Lambda >= 8 lamJ
Lam = 8*lamJ
zs = [2.5*Lam - 0.3j*Lam, -3.0*Lam - 1e-3j, 5*Lam - 2j*Lam]
rs = [0.4-0.1j, -0.8+0.3j, 0.25+0.0j]
def Rdown(k): return sum(r/(k - z) for r, z in zip(rs, zs))
mp.mp.dps = 25
f = lambda x: complex(E(complex(x))*Rdown(complex(x)))
val = mp.quad(lambda x: mp.mpc(f(float(x))), [-mp.inf, -10, -3*Lam-0.1, -3*Lam, -3*Lam+0.1, -1, 0, 1, 10, mp.inf])/(2*mp.pi)
pred = -1j*sum(r*E(z) for r, z in zip(rs, zs))
print(f"    int dk/2pi E R_down = {complex(val):.10f};  -i sum r_i E(z_i) = {pred:.10f}")
normR = sum(abs(r/z) for r, z in zip(rs, zs))
print(f"    |result| = {abs(pred):.3e}  <=  2 M lamJ ||R|| / (2 Lambda) = {2*M*lamJ*normR/(2*Lam):.3e}")

# ---------------- (c) ----------------
print()
# J^in: poles at k = A_D - i0 (LHP) -> analytic in UHP; spectator insertion: J(0) = J_- = J_+ = J0
J0 = 1e-3; C = 50.0
b1, b2, b3 = 0.01, -0.02, 0.015
et = 0.005
def Jin(k):  return 1j*C*(1/(k - b1 + 1j*et) - 1/(k - b2 + 1j*et)) + 1j*J0/(k - b3 + 1j*et)   # poles in LHP; J_- = J0
def Jfi2(k): return -1j*C*(1/(k - b2 - 1j*et) - 1/(k - b1 - 1j*et)) - 1j*J0/(k - b3 - 1j*et)  # poles in UHP; J_+ = J0
# check asymptotics
kbig = 1e6
print(f"(c) J_- = lim(-i k)J^in = {(-1j*kbig*Jin(kbig)):.6f};  J_+ = lim(i k)J^fi = {(1j*kbig*Jfi2(kbig)):.6f}; J0 = {J0}")
lamJ2 = 0.02
Lam2 = 1.0
kp, kT2 = 0.1, 2*Lam2*4*0.1   # R(k) = 1/(2 k^+ k - kT^2 + i0): pole at kT^2/(2k^+) = 4 Lambda
zR = kT2/(2*kp) - 0.02j                       # pole of R in the LHP (k^+ > 0), finite width
R = lambda k: 1/(2*kp*(k - zR))
num = mp.quad(lambda x: mp.mpc((Jin(float(x)) + Jfi2(float(x)))*R(float(x))),
              [-mp.inf, -100, -1, -0.1, b2, b3, b1, 0.1, 1, 4*Lam2-0.5, 4*Lam2, 4*Lam2+0.5, 100, mp.inf])/(2*mp.pi)
# exact by contour closure: J^in R closes in the UHP (0); J^fi R closes in the LHP: -i Res_{zR}
exact = -1j*Jfi2(zR)/(2*kp)
print(f"    contour closure: int dk/2pi J R = -i J^fi(zR)/(2k^+) = {exact:.6e}  (numeric {complex(num):.6e})")
lead = R(0)*J0
print(f"    int dk/2pi J R = {complex(num):.6e};  R(0) J(0) = {lead:.6e};  relative error = {abs(complex(num)/lead - 1):.3f}")
print(f"    lamJ/Lambda = {lamJ2/Lam2:.3f}: a relative bound C' lamJ/Lambda would need C' >= {abs(complex(num)/lead-1)/(lamJ2/Lam2):.1f};"
      f" the absolute bound M lamJ |R(0)|/Lambda with M ~ C = {C} is respected: |diff| = {abs(complex(num)-lead):.3e} vs {C*lamJ2*abs(R(0))/Lam2:.3e}")

# ---------------- (d) ----------------
print()
def su3_fund():
    l = np.zeros((8, 3, 3), complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7] = np.diag([1, 1, -2])/np.sqrt(3)
    return l/2
T = su3_fund()
Tbar = np.array([-t.conj() for t in T])          # antifundamental
fabc = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    fabc[a, b, c] = np.real(-2j*np.trace((T[a]@T[b] - T[b]@T[a])@T[c]))
Tadj = np.array([-1j*fabc[a] for a in range(8)])  # (T^a)_{bc} = -i f^{abc}
CA = 3.0
for name, (TA, TB) in {'F x F': (T, T), 'F x Fbar': (T, Tbar), 'F x A': (T, Tadj)}.items():
    dA, dB = TA.shape[1], TB.shape[1]
    X = sum(np.kron(TA[a], TB[a]) for a in range(8))
    lhs = sum(np.kron(TA[a]@TA[b] + TA[b]@TA[a], TB[a]@TB[b] + TB[b]@TB[a]) for a in range(8) for b in range(8))
    rhs = 4*X@X + CA*X
    chi = 1e-3
    A1 = -1j*chi*X
    A2 = 0.5*(-1j*chi)**2*(X@X + CA*X/4)
    Id = np.eye(dA*dB)
    U = Id + A1 + A2
    dev = U.conj().T@U - Id
    print(f"(d) {name}: sum {{T^a,T^b}}{{T'^a,T'^b}} = 4X^2 + C_A X : {np.allclose(lhs, rhs)};  "
          f"(U^dag U - 1)/chi^2 = -C_A X/4 + O(chi): {np.allclose(dev/chi**2, -CA*X/4, atol=5e-3)}")
print("    => residual -(1/4) C_A chi^2 X; the contributions outside the window must supply +(1/4) C_A chi^2 X.")

# ---------------- (f) ----------------
print()
def weight_formula(zs, perm):
    num = np.prod(zs)
    den = 1.0
    for m in range(len(perm)):
        den *= sum(zs[perm[l]] for l in range(m, len(perm)))
    return num/den
def weight_numeric(zs, perm, n=200000, rng=np.random.default_rng(5)):
    # z real positive (pole just below the real axis): densities z_j exp(-z_j tau) after tau -> -i tau rotation
    taus = np.array([rng.exponential(1/z, n) for z in zs])
    order = np.argsort(-taus, axis=0)    # pi(1) = latest ... compare with formula convention below
    # formula: insertion pi(1) is the EARLIEST? test both conventions
    return order
zs = [0.7, 1.9, 0.4]
tot = sum(weight_formula(zs, p) for p in itertools.permutations(range(3)))
print(f"(f) N=3: sum over orderings of prod z_j / prod_m sum_(l>=m) z_pi(l) = {tot:.12f}")
# two insertions: P(tau1 < tau2) with densities z_j e^{-z_j tau}
rng = np.random.default_rng(1)
z1, z2 = 0.7, 1.9
t1 = rng.exponential(1/z1, 2_000_000); t2 = rng.exponential(1/z2, 2_000_000)
print(f"    N=2: MC P(insertion 1 earlier) = {np.mean(t1 < t2):.4f};  z1/(z1+z2) = {z1/(z1+z2):.4f}")
# exact complex-pole version: rho_j(tau) = i z_j e^{-i z_j tau}, Im z_j < 0
z1c, z2c = 0.7-0.05j, 1.9-0.3j
P12 = mp.quad(lambda t: 1j*z1c*mp.e**(-1j*z1c*t)*mp.e**(-1j*z2c*t), [0, mp.inf])
print(f"    complex poles: int_0^inf rho_1(t) P(tau2>t) dt = {complex(P12):.10f};  z1/(z1+z2) = {z1c/(z1c+z2c):.10f}")
for kT1sq, kT2sq, k1p, k2p in [(1.0, 1.0, 0.3, 0.6), (4.0, 1.0, 0.3, 0.6)]:
    za, zb = kT1sq/(2*k1p), kT2sq/(2*k2p)
    print(f"    kT1^2={kT1sq}, kT2^2={kT2sq}, k1+={k1p}, k2+={k2p}:  w12 = {za/(za+zb):.4f}  (same k^+, different kT^2 -> different weight)")
