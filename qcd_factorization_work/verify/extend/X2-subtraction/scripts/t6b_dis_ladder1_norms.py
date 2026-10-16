import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')
x = 2.0; Q2 = 1.0
th_n, th_w = np.polynomial.legendre.leggauss(96)
th = 0.5*np.pi*(th_n + 1); thw = 0.5*np.pi*th_w
def rho_r_vec(xi, kT, m2):
    c = np.cos(th)
    v = xi*m2 + kT**2/(1 - xi); vh = kT**2/(1 - xi)
    Hh = 1.0/(Q2*(1 - xi/x))
    H = lambda vv: 1.0/(Q2*(1 - xi/x) + vv + 2*kT*c)
    return ((H(v) - Hh)/v**2 - (H(vh) - Hh)/vh**2)/(1 - xi)
def full(lk, xi, m2):
    kT = np.exp(lk)
    vals = np.abs(rho_r_vec(xi, kT, m2))
    return np.sum(vals*np.sin(th)**2*thw)*4*np.pi*kT**4/np.pi**2
def avg(lk, xi, m2, absval):
    kT = np.exp(lk)
    vals = rho_r_vec(xi, kT, m2)
    s = np.sum(vals*np.sin(th)**2*thw)*4*np.pi*kT**4/np.pi**2
    return abs(s) if absval else s
print("one-rung DIS ladder remainder (phi^3_6, Q=1, x=2):")
for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:
    L = np.log(1/m2)
    S = integrate.dblquad(lambda lk, xi: avg(lk, xi, m2, False), 0, 1, lambda xi: -30, lambda xi: 12, epsrel=1e-9)[0]
    Na = integrate.dblquad(lambda lk, xi: avg(lk, xi, m2, True), 0, 1, lambda xi: -30, lambda xi: 12, epsrel=1e-9)[0]
    Nf = integrate.dblquad(lambda lk, xi: full(lk, xi, m2), 0, 1, lambda xi: -30, lambda xi: 12, epsrel=1e-7)[0]
    print(f"  m2={m2:.0e}: int r = {S:+.6e} = {S/m2:+.5f} m2 ; |avg-fiber| norm = {Na/m2:.5f} m2 = {Na/(m2*L):.5f} m2 L ;"
          f" full norm = {Nf/np.sqrt(m2):.5f} lam = {Nf/(np.sqrt(m2)):.5f}")
