"""X2 fix round 1 / r1_theta2_lower.py -- the cover-family numbers at theta = 2 (complement of t18, whose docstring claim
'exponent 1 (theta=1) is optimal' is RETRACTED, see X2-Err-own):  A = int_{U_S} rho_C1 (>= s/4 analytically) and
B = int_{U_C1 cap {u<1/2}} |rho_G - rho_S - rho_C1| at s = lambda^theta, theta in {1, 1.5, 2}; t18 conventions."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')
def dens(u, k, m2):
    v = 1 - u
    DG = (m2 + u)*(v*(1 + m2) + k) + k*v
    return v/((u*m2*v + k)*DG), 1/((u*m2 + k)*(m2 + u)), u*m2/((u*m2*v + k)*(u*m2 + k))
for theta in [1.0, 1.5, 2.0]:
    print(f"theta = {theta}")
    for kk in [4, 6, 8, 10]:
        m2 = 10.0**(-kk); lam = np.sqrt(m2); s = lam**theta; L = np.log(1/m2)
        A = integrate.dblquad(lambda lk, lu: dens(np.exp(lu), np.exp(lk), m2)[2]*np.exp(lu + lk),
                              np.log(1e-30), np.log(s), lambda lu: np.log(1e-40), lambda lu: np.log(s) + lu, epsrel=1e-9)[0]
        f = lambda lk, lu: abs(dens(np.exp(lu), np.exp(lk), m2)[0] - dens(np.exp(lu), np.exp(lk), m2)[1] - dens(np.exp(lu), np.exp(lk), m2)[2])*np.exp(lu + lk)
        B = integrate.dblquad(f, np.log(s), np.log(0.5), lambda lu: np.log(1e-40), lambda lu: np.log(s) + lu, epsrel=1e-9)[0]
        print(f"   lam2=1e-{kk}: A/s = {A/s:.4f}   B/(s L) = {B/(s*L):.4f}")
