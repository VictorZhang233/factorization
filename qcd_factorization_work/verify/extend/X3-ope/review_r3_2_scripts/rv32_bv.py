"""rv32_bv.py -- reviewer r3-2: numerical sanity test of Lemma 5.5(c) (boundary values along
curved, x-dependent approaches) and of its use in Prop 5.6 step 6'(ii).

(1) 1-d: f(z) = z^{-2} on Im z > 0, boundary value (x+i0)^{-2}.  Curved approach
        Theta_eta(x) = x + eta^2 sin(3x) + i eta h(x),  h = (1+x^2)(1.2+cos x)/2 > 0,
    (x-dependent speed and a real distortion, Theta_eta -> id in C^infty).  Test function: compactly
    supported bump phi.  Limit predicted by the lemma:  <(x+i0)^{-2}, phi> = PV int phi'/x - i pi phi'(0).
(2) 2-d, the exact geometry of Prop 5.6 6'(ii): F(w,s) = (w - kappa s)^{-2}, holomorphic on the wedge
    with cone {eta_w - kappa eta_s > 0}; approach Theta_eta(x,s) = (x + i eta, s + eta^2 - 2 i x eta),
    i.e. Im Theta = eta (1, -2x): an x-dependent DIRECTION.  Prediction: the limit is the wedge boundary
    value  <(x - kappa s + i0)^{-2}, psi> = int ds [PV int d_x psi/(x - kappa s) dx - i pi d_x psi(kappa s, s)].
    The error should decrease like O(eta).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np

mp.mp.dps = 20

def bump(t):
    t = mp.mpf(t) if not isinstance(t, mp.mpc) else t
    return mp.exp(-1/(1 - t**2)) if abs(t) < 1 else mp.mpf(0)

def dbump(t):
    return bump(t)*(-2*t/(1 - t**2)**2) if abs(t) < 1 else mp.mpf(0)

# ---------------- (1) one dimension
R1 = mp.mpf(2)
phi = lambda x: (1 + x)*bump(x/R1)
dphi = lambda x: bump(x/R1) + (1 + x)*dbump(x/R1)/R1
h = lambda x: (1 + x**2)*(mp.mpf('1.2') + mp.cos(x))/2

L1 = mp.quad(lambda x: (dphi(x) - dphi(-x))/x, [0, 1, R1]) - 1j*mp.pi*dphi(0)
print("(1) predicted limit <(x+i0)^-2, phi> =", mp.nstr(L1, 14))
prev = None
for eta in [mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    Th = lambda x: x + eta**2*mp.sin(3*x) + 1j*eta*h(x)
    I = mp.quad(lambda x: phi(x)*Th(x)**-2, [-R1, -1, -10*eta, -eta, 0, eta, 10*eta, 1, R1])
    print(f"    eta={mp.nstr(eta,2):>6}: int phi(x) f(Theta_eta(x)) dx = {mp.nstr(I,14):>36}   |diff| = {mp.nstr(abs(I-L1),3)}")
    last1 = abs(I - L1)
ok1 = last1 < 1e-3

# ---------------- (2) two dimensions, Prop 5.6 geometry
kap = mp.mpf('0.3'); RX = mp.mpf('1.5'); RS = mp.mpf(2)
def psi(x, s):  return bump(x/RX)*bump(s/RS)*(1 + mp.mpf('0.4')*x - mp.mpf('0.3')*s + mp.mpf('0.2')*x*s)
def dxpsi(x, s):
    return (dbump(x/RX)/RX*bump(s/RS)*(1 + mp.mpf('0.4')*x - mp.mpf('0.3')*s + mp.mpf('0.2')*x*s)
            + bump(x/RX)*bump(s/RS)*(mp.mpf('0.4') + mp.mpf('0.2')*s))

# outer s-integral: Gauss-Legendre (integrand smooth in s)
ns = 40
xs, ws = np.polynomial.legendre.leggauss(ns)
snodes = [mp.mpf(float(t))*RS for t in xs]; sweights = [mp.mpf(float(w))*RS for w in ws]

def inner_limit(s):
    c = kap*s
    g = lambda x: dxpsi(x, s)
    reg = mp.quad(lambda x: (g(x) - g(c))/(x - c), [-RX, c, RX])
    return reg + g(c)*mp.log((RX - c)/(RX + c)) - 1j*mp.pi*g(c)

L2 = mp.fsum(w*inner_limit(s) for s, w in zip(snodes, sweights))
print("(2) predicted wedge boundary value <(x - kappa s + i0)^-2, psi> =", mp.nstr(L2, 14))

def inner_curved(s, eta):
    A = 1 + 2j*kap*eta; B = kap*s + kap*eta**2 - 1j*eta
    x0 = B/A                                   # pole of (A x - B)^-2, Im x0 < 0
    xr = mp.re(x0)
    # int psi (A x - B)^-2 dx = (1/A^2) int d_x psi /(x - x0) dx  (integration by parts, compact support)
    pts = [-RX, xr - 20*eta, xr - eta, xr, xr + eta, xr + 20*eta, RX]
    pts = sorted(set([p for p in pts if -RX <= p <= RX]))
    return mp.quad(lambda x: dxpsi(x, s)/(x - x0), pts)/A**2

for eta in [mp.mpf('0.05'), mp.mpf('0.01'), mp.mpf('0.002')]:
    I2 = mp.fsum(w*inner_curved(s, eta) for s, w in zip(snodes, sweights))
    # sanity: Im of (w - kappa s) along the approach is eta(1 + 2 kappa x) > 0 on supp psi
    print(f"    eta={mp.nstr(eta,2):>6}: int psi F(Theta_eta) = {mp.nstr(I2,14):>36}   |diff| = {mp.nstr(abs(I2-L2),3)}")
    last2 = abs(I2 - L2)
print("    min over supp of (1 + 2 kappa x) =", mp.nstr(1 - 2*kap*RX, 3), "(> 0: approach stays in the wedge)")
ok2 = last2 < 5e-3
print("RESULT:", "PASS" if (ok1 and ok2) else "FAIL", "(limits along curved / x-dependent approaches equal the boundary value)")
