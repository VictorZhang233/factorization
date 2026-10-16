"""X2 fix round 1 / r1_dis_Honly.py -- one-loop DIS forward-amplitude graphs of (M2) with only the hard region:
UV divergences, integrand-level renormalization, commutation with T_H, and the (H1)_H norm.

Model (M2): complex psi (target, 'quark'), real phi ('gluon'), vertex g psi* psi phi, current J = psi* psi, d = 6 - 2 eps,
target p = (p+, -m2/2p+, 0), p^2 = -m2; q = (0, q-, q_T), Q^2 = q_T^2 = 1, x = Q^2/2p.q > 1; P = p + q, s = -P^2 = m2 + (1-1/x),
T_H: p -> phat = (p+, 0, 0), so P -> Phat with shat = s - m2 = 1 - 1/x (P^+ and P_T unchanged).

Vertex correction at J_in (s channel), loop psi(l), psi(l+q), phi(p-l); the k^- residue at the phi pole gives
   rho_V = S(P) f(m2),  f(m2) = 1/(pi^2 (1-z) v H),  v = z m2 + |l|^2/(1-z),  H = A + v + 2 l.q,  A = 1 - z/x,
on the base (z = l+/p+ in (0,1), l in R^4).  UV: f ~ (1-z)/|l|^4, log divergent; the unrenormalized
(1-T_H)Gamma = S(P)[f(m2) - f(0)] + [S(P) - S(Phat)] f(0) is log divergent at O(m2).
BPHZ at a fixed space-like point with matched plus components (p0+ = p+, q0+ = 0):  p0^2 = -mu^2, q0^2 = -1,
(p0+q0)^2 = -mu^2 + 1/x0 - 1 (fixed invariants, so the integrated counterterm is a constant times the tree vertex):
   f0 = 1/(pi^2 (1-z) v_mu H_mu),  v_mu = z mu^2 + |l|^2/(1-z),  H_mu = (1 - z/x0) + v_mu + 2 l.q0.
T_H acts on p only, the subtraction point is p-independent  =>  T_H R = R T_H, and
   (1-T_H) R Gamma = S(P)[f(m2) - f(0)] + [S(P) - S(Phat)] [f(0) - f0]   (both terms UV finite pointwise in z).
Hard-line self-energy (s channel): after the shift l -> l - z P_T the density is (1/pi^2)/(a + z(1-z)s), a = |l|^2
(quadratically divergent); subtraction of the first-order Taylor polynomial in s at s0 (= Taylor in P^- at fixed P^+, P_T)
gives g(s) = (c-c0)^2/(pi^2 (a+c)(a+c0)^2), c = z(1-z)s; graph S(P)^2 Sigma_R:  rho = g(s)/s^2,  T_H: g(shat)/shat^2."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

x, x0, mu2 = 2.0, 2.0, 1.0
zn, zw = np.polynomial.legendre.leggauss(64)
thn, thw = np.polynomial.legendre.leggauss(48)
TH = 0.5*np.pi*(thn + 1); THW = 0.5*np.pi*thw*4*np.pi*np.sin(0.5*np.pi*(thn + 1))**2     # d Omega_3 = 4 pi sin^2 dth
def zgrid():
    # z in (0,1) with endpoint clustering: z = (1 - cos(pi t))/2
    t = 0.5*(zn + 1); z = 0.5*(1 - np.cos(np.pi*t)); jz = 0.5*np.pi*np.sin(np.pi*t)*0.5*zw
    return z, jz
def lgrid(lo, hi, n=400):
    s = np.linspace(np.log(lo), np.log(hi), n); w = np.gradient(s)
    return np.exp(s), w

def f(m2, z, l, c, qq=1.0, xx=x, muv=None):
    v = z*(m2 if muv is None else muv) + l**2/(1 - z)
    H = (1 - z/xx) + v + 2*l*c*qq
    return 1.0/(np.pi**2*(1 - z)*v*H)

def vertex_norms(m2, Lam=1e6, renorm=True):
    s = m2 + (1 - 1/x); sh = 1 - 1/x
    SP, SPh = 1/s, 1/sh
    z, jz = zgrid(); l, wl = lgrid(1e-9, Lam)
    Z = z[:, None, None]; Lr = l[None, :, None]; C = np.cos(TH)[None, None, :]
    fm = f(m2, Z, Lr, C); f0m = f(0.0, Z, Lr, C)
    if renorm:
        fct = f(None, Z, Lr, C, qq=1.0, xx=x0, muv=mu2)
        rho = SP*(fm - fct) - SPh*(f0m - fct)
    else:
        rho = SP*fm - SPh*f0m
    meas = (Lr**4)*wl[None, :, None]*THW[None, None, :]*jz[:, None, None]     # d^4 l = |l|^3 d|l| dOmega = |l|^4 dln|l| dOmega
    return np.sum(np.abs(rho)*meas), np.sum(rho*meas)

def sigma_norms(m2, s0=1.0):
    s = m2 + (1 - 1/x); sh = 1 - 1/x
    z, jz = zgrid(); l, wl = lgrid(1e-9, 1e7, 600)
    Z = z[:, None]; A = (l**2)[None, :]
    def g(ss):
        c = Z*(1 - Z)*ss; c0 = Z*(1 - Z)*s0
        return (c - c0)**2/(np.pi**2*(A + c)*(A + c0)**2)
    rho = g(s)/s**2 - g(sh)/sh**2
    meas = 2*np.pi**2*(l**4)[None, :]*wl[None, :]*jz[:, None]
    return np.sum(np.abs(rho)*meas), np.sum(rho*meas)

if __name__ == "__main__":
    print("vertex correction (M2, s channel, J_in), x = 2:")
    print("  unrenormalized (1-T_H)Gamma, UV cutoff |l| < Lambda:  int |rho| / m2")
    for m2 in [1e-3, 1e-5]:
        row = []
        for Lam in [1e2, 1e4, 1e6]:
            N, _ = vertex_norms(m2, Lam, renorm=False); row.append(N/m2)
        print(f"     m2={m2:.0e}: Lambda=1e2,1e4,1e6 -> {['%.4f' % r for r in row]}   (grows like ln Lambda: UV divergent at O(m2))")
    print("  BPHZ-renormalized (plus-matched subtraction point, mu^2 = 1, x0 = 2):  int |rho_r|,  int rho_r")
    for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:
        L = np.log(1/m2)
        N, S = vertex_norms(m2, 1e6, renorm=True)
        N2, _ = vertex_norms(m2, 1e8, renorm=True)
        print(f"     m2={m2:.0e}: norm = {N:.5e} = {N/m2:.4f} m2 = {N/(m2*L):.4f} m2 L   (cutoff 1e8: {N2/m2:.4f} m2)   signed = {S/m2:+.4f} m2")
    print("hard-line self-energy (M2, s channel), Taylor subtraction in s at s0 = 1:")
    for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        N, S = sigma_norms(m2)
        print(f"     m2={m2:.0e}: norm = {N/m2:.5f} m2   signed = {S/m2:+.5f} m2")
