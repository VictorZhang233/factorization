"""X2/T18: optimality of the hypothesis exponent within the 2x2 cover family U(theta), s = lambda^theta:
  A(theta) = int_{U_S} rho_C1   (rho_C1 >= 0 on 0<u<1)          ~ s            (expected)
  B(theta) = int_{U_C1} |rho_G - rho_S - rho_C1|                 ~ lambda^2/s * log (expected)
so max(A,B) >= c lambda^{min(theta,2-theta)}: exponent 1 (theta=1) is optimal within the family.

*** RETRACTED (X2 fix round 1, see REPORT X2-Err-own): the expectation B ~ lambda^2/s above is FALSE.  The output of this
script itself shows B(theta) = (theta/2) s L (1+o(1)) for theta < 2 (and ~1.44 s L at theta = 2, r1_theta2_lower.py), so
max(A,B) ~ s and the natural cover theta = 2 is optimal (sharp lambda^2 L^2).  Do not quote the sentence above. ***"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')
def dens(u, k, m2):
    v = 1 - u
    DG = (m2 + u)*(v*(1 + m2) + k) + k*v
    rG = v/((u*m2*v + k)*DG); rS = 1/((u*m2 + k)*(m2 + u)); rC1 = u*m2/((u*m2*v + k)*(u*m2 + k))
    return rG, rS, rC1
for theta in [0.5, 1.0, 1.5]:
    print(f"theta = {theta}")
    for kk in [4, 6, 8, 10]:
        m2 = 10.0**(-kk); lam = np.sqrt(m2); s = lam**theta; L = np.log(1/m2)
        # U_S: u in (0,s), y=kap/u <= s  -> kap in (0, s u)
        A = integrate.dblquad(lambda lk, lu: dens(np.exp(lu), np.exp(lk), m2)[2]*np.exp(lu)*np.exp(lk),
                              np.log(1e-30), np.log(s), lambda lu: np.log(1e-40), lambda lu: np.log(s) + lu, epsrel=1e-8)[0]
        # U_C1 (0<u<1/2 part is enough for a lower bound): u in (s, 1/2), kap in (0, s u)
        f = lambda lk, lu: abs(dens(np.exp(lu), np.exp(lk), m2)[0] - dens(np.exp(lu), np.exp(lk), m2)[1] - dens(np.exp(lu), np.exp(lk), m2)[2])*np.exp(lu)*np.exp(lk)
        B = integrate.dblquad(f, np.log(s), np.log(0.5), lambda lu: np.log(1e-40), lambda lu: np.log(s) + lu, epsrel=1e-8)[0]
        print(f"   lam2=1e-{kk}: A = {A:.4e} (A/s = {A/s:.4f});  B = {B:.4e} (B s/(lam^2 L) = {B*s/(m2*L):.4f}, B/s = {B/s:.3e})")
