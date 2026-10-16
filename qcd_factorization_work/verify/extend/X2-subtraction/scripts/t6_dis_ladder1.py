"""X2/T6: DIS forward amplitude in phi^3_6, one-rung ladder (one loop), unphysical region x>1, frame q^+=0.
  Gamma = H0(k) S(k)^2 R(p-k),  H0 = 1/(-(k+q)^2),  S = 1/(-k^2),  R = 1/(-r^2);  p^2=-m2, q=(0,q^-,q_T), Q^2=q_T^2.
Fibered ("rungs on shell") representation (REPORT Lemma C.1): after the k^- residue at the rung pole,
  L1 = (1/pi^2) int_0^1 dxi int d^4k_T  H0/((1-xi) v^2),  v = xi m2 + kT^2/(1-xi),
  H0 = 1/(Q^2(1-xi/x) + v + 2 kT.qT).
Checks: (1) covariant Feynman-parameter value; (2) remainder r = DeltaH0 S^2 DeltaR (signed integral, norm with and without
angular averaging); subtraction terms C_{R1} = H0hat S^2 R(p-k), C_{R0} = DeltaH0 S^2 R(phat-k)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')

def covariant_L1(m2, Q2=1.0, x=2.0):
    sbar = Q2*(1 - 1/x) + m2
    # int over simplex a1+a2+a3=1 of a2/(a1 a2 Q2 + a1 a3 sbar + a2 a3 m2)
    def inner(a2):
        f = lambda a1: a2/(a1*a2*Q2 + a1*(1 - a1 - a2)*sbar + a2*(1 - a1 - a2)*m2)
        return integrate.quad(f, 0, 1 - a2, limit=200, epsabs=0, epsrel=1e-11)[0]
    return integrate.quad(inner, 0, 1, limit=200, epsabs=0, epsrel=1e-10, points=[m2, 1e-3, 0.1])[0]

def fibered_L1(m2, Q2=1.0, x=2.0):
    Q = np.sqrt(Q2)
    # angular average over S^3 of 1/(a + b cos th): <.> = 2/(a + sqrt(a^2-b^2))
    def dens(kT, xi):
        v = xi*m2 + kT**2/(1 - xi)
        a = Q2*(1 - xi/x) + v; b = 2*kT*Q
        H = 2/(a + np.sqrt(a*a - b*b))
        return H/((1 - xi)*v**2) * 2*np.pi**2*kT**3 / np.pi**2   # d^4kT = 2 pi^2 kT^3 dkT (angle-averaged)
    f = lambda lk, xi: dens(np.exp(lk), xi)*np.exp(lk)
    return integrate.dblquad(f, 0, 1, lambda xi: -40, lambda xi: 15, epsrel=1e-10)[0]

for m2 in [1e-2, 1e-3, 1e-4]:
    c = covariant_L1(m2); fb = fibered_L1(m2)
    print(f"m2={m2:.0e}: covariant L1 = {c:.12f}   fibered = {fb:.12f}   rel diff {abs(c-fb)/c:.1e}")

# ---- remainder and norms ----
def H0(xi, v, kT, cth, Q2=1.0, x=2.0):
    return 1.0/(Q2*(1 - xi/x) + v + 2*kT*np.sqrt(Q2)*cth)
def H0hat(xi, Q2=1.0, x=2.0):
    return 1.0/(Q2*(1 - xi/x))
def rho_r(xi, kT, cth, m2):
    v = xi*m2 + kT**2/(1 - xi); vh = kT**2/(1 - xi)
    return ((H0(xi, v, kT, cth) - H0hat(xi))/v**2 - (H0(xi, vh, kT, cth) - H0hat(xi))/vh**2)/(1 - xi)
def avg_rho_r(xi, kT, m2, Q2=1.0, x=2.0):
    v = xi*m2 + kT**2/(1 - xi); vh = kT**2/(1 - xi); Q = np.sqrt(Q2); b = 2*kT*Q
    def Hav(vv):
        a = Q2*(1 - xi/x) + vv
        return 2/(a + np.sqrt(a*a - b*b))
    return ((Hav(v) - H0hat(xi))/v**2 - (Hav(vh) - H0hat(xi))/vh**2)/(1 - xi)

def norms(m2):
    # measure (1/pi^2) dxi d^4kT ; d^4kT = 4 pi kT^3 sin^2(th) dkT dth
    def full(th, lk, xi):
        kT = np.exp(lk)
        return abs(rho_r(xi, kT, np.cos(th), m2))*4*np.pi*np.sin(th)**2*kT**4/np.pi**2
    def signed(lk, xi):
        kT = np.exp(lk); return avg_rho_r(xi, kT, m2)*2*np.pi**2*kT**4/np.pi**2
    def avgabs(lk, xi):
        kT = np.exp(lk); return abs(avg_rho_r(xi, kT, m2))*2*np.pi**2*kT**4/np.pi**2
    S = integrate.dblquad(signed, 0, 1, lambda xi: -30, lambda xi: 12, epsrel=1e-9)[0]
    Na = integrate.dblquad(avgabs, 0, 1, lambda xi: -30, lambda xi: 12, epsrel=1e-9)[0]
    Nf = integrate.tplquad(full, 0, 1, lambda xi: -30, lambda xi: 12, lambda xi, lk: 0, lambda xi, lk: np.pi, epsrel=1e-6)[0]
    return S, Na, Nf

print("\nremainder of the one-rung ladder (Q=1, x=2):")
for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    S, Na, Nf = norms(m2)
    L = np.log(1/m2)
    print(f"  lam2=m2={m2:.0e}: int r = {S:+.6e} ({S/m2:+.4f} m2, {S/(m2*L):+.4f} m2 L); "
          f"norm(angle-averaged fiber) = {Na:.4e} ({Na/m2:.4f} m2 = {Na/(m2*L):.4f} m2 L); "
          f"full norm = {Nf:.4e} ({Nf/np.sqrt(m2):.4f} lam)")
