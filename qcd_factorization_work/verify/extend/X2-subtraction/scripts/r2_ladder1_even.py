"""X2 fix round 2 / r2_ladder1_even.py -- one-rung DIS ladder (phi^3_6, Q = 1, x = 2): numerical check of the proof of
X2-Prop5.1'(d) written in this round (review r2_1):
    rho_r = odd + rest,   odd := -2 k.q (kappa_1 - kappa_0)/A^2,
    int |odd| = c1(x) lambda   EXACTLY (scale invariance in t/delta, delta = z m2),
    int |rest| <= C(x) lambda^2 L        (proved: E1 + E2 on |k| <= c_x/4, Prop 5.1'(a) bounds on |k| > c_x/4),
hence | int|rho_r| - c1 lambda | <= int|rest| = O(lambda^2 L).
rest is evaluated through the exact identity h - hhat = -s/A^2 + s^2/(A^2 (A+s)), s = v + 2 k.q, for |k| < 1, and as
rho_r - odd for |k| >= 1 (no large cancellations in either range).  Product Gauss-Legendre rules in (z = s^2, log|k|, theta);
d^4k = 4 pi |k|^3 d|k| sin^2(theta) d(theta)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
xB = 2.0
cx = 1 - 1/xB
c1 = None
def gl(a, b, n):
    t, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*t + 0.5*(b + a), 0.5*(b - a)*w
def composite(edges, n):
    xs, ws = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        x_, w_ = gl(a, b, n); xs.append(x_); ws.append(w_)
    return np.concatenate(xs), np.concatenate(ws)
def norms(m2, nz=48, nk=40, nth=96):
    m = np.sqrt(m2)
    # z = s^2 (z^{1/2} endpoint), s in (0,1)
    s_, ws_ = composite(np.linspace(0, 1, 9), nz // 8)
    z = s_**2; wz = 2*s_*ws_
    # log|k| grid with breaks around m and 1
    lm = np.log(m)
    edges = np.array([lm - 16, lm - 8, lm - 4, lm - 2, lm - 1, lm, lm + 1, lm + 2, lm + 4, -3, -2, -1, 0, 1, 2, 4, 7])
    edges = np.unique(np.sort(edges))
    lk, wlk = composite(edges, nk // 2)
    k = np.exp(lk); wk = wlk*k                      # d|k| = |k| dlog|k|
    th, wth = composite(np.linspace(0, np.pi, 17), nth // 16)
    Z, K, TH = np.meshgrid(z, k, th, indexing='ij')
    W = (wz[:, None, None]*wk[None, :, None]*wth[None, None, :])*4*np.pi*K**3*np.sin(TH)**2
    A = 1 - Z/xB
    v1 = Z*m2 + K**2/(1 - Z); v0 = K**2/(1 - Z)
    ka1 = 1/(np.pi**2*(1 - Z)*v1**2); ka0 = 1/(np.pi**2*(1 - Z)*v0**2)
    kq = K*np.cos(TH)
    s1 = v1 + 2*kq; s0 = v0 + 2*kq
    h1 = 1/(A + s1); h0 = 1/(A + s0); hh = 1/A
    rho = ka1*(h1 - hh) - ka0*(h0 - hh)
    odd = -2*kq*(ka1 - ka0)/A**2
    R2 = lambda s: s**2/(A**2*(A + s))
    rest_alg = -(ka1*v1 - ka0*v0)/A**2 + ka1*R2(s1) - ka0*R2(s0)
    rest = np.where(K < 1, rest_alg, rho - odd)
    return (W*np.abs(rho)).sum(), (W*np.abs(odd)).sum(), (W*np.abs(rest)).sum(), (W*rest).sum()
# c1(x) = 4 int_0^1 xi^{1/2}(1-xi)^{3/2}/(1-xi/x)^2
xi, wxi = composite(np.linspace(0, 1, 9), 40)
xi2 = xi**2
c1 = 4*np.sum(2*xi*wxi*np.sqrt(xi2)*(1 - xi2)**1.5/(1 - xi2/xB)**2)
print(f"x = {xB}: c1 = {c1:.9f}  (r1: 1.262983875)")
print(" m2        int|rho_r|/lam   int|odd|/lam   int|rest|/(lam^2 L)   (int|rho_r| - c1 lam)/(lam^2 L)   [t6b full norm/lam]")
t6b = {1e-2: 1.22808, 1e-3: 1.25256, 1e-4: 1.26000, 1e-5: 1.26232, 1e-6: 1.26306}
for m2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    lam = np.sqrt(m2); L = np.log(1/m2)
    nr, no, ne, se = norms(m2)
    print(f" {m2:7.0e}   {nr/lam:13.6f}   {no/lam:12.6f}   {ne/(m2*L):17.5f}     {(nr - c1*lam)/(m2*L):+22.5f}        [{t6b[m2]:.5f}]", flush=True)
# convergence check of the quadrature at one point
nr, no, ne, se = norms(1e-4, nz=96, nk=80, nth=192)
print(f" refined grid at m2=1e-4: int|rho_r|/lam = {nr/1e-2:.6f}, int|odd|/lam = {no/1e-2:.6f}, int|rest|/(lam^2 L) = {ne/(1e-4*np.log(1e4)):.5f}")
