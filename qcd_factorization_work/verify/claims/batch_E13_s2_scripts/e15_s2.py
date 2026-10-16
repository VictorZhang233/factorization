#!/usr/bin/env python3
"""E15 stage-2: test Collins App. B.1 anomalous deformations by Cauchy invariance.

I = int dE dp  i f(E,p) / (E - p^2/(2m) + i eps),   f = exp(-(E^2+p^2)/Q^2) (entire).
Deform (E,p) = (E_R,p_R) + i lam chi(E_R,p_R) (eta, xi), chi a Gaussian bump (so the
deformation decays at infinity and f stays bounded). If no singularity is crossed for
0 <= lam <= 1, the integral is unchanged (multidimensional Cauchy theorem).
  anom1: (eta,xi) = (|E_R| + 2|p_R|, m)        first-order shift zero at the origin
  anom2: (eta,xi) = (p_R + p_R^2/2m - E_R, m)   first-order shift zero on the whole surface
  bad  : (eta,xi) = (0, m)                      constant tangent direction (crosses the pole)
  nat  : (eta,xi) = (delta, 0) without bump     natural deformation, gives the eps -> 0+ limit
Also: sympy check that on anom2 the denominator vanishes only for lam = eps = 0.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

m, Q, w = 1.0, 1.0, 2.0
L, h = 6.0, 0.004
x = np.arange(-L, L + h/2, h) + h/2   # midpoint grid: kinks of anom1 at cell boundaries

def integrate(defo, lam, eps, delta=0.5):
    tot = 0.0 + 0.0j
    P = x[None, :]
    for i0 in range(0, len(x), 250):
        ER = x[i0:i0 + 250][:, None] * np.ones_like(P)
        PR = np.ones_like(ER[:, :1]) * P
        if defo == 'orig':
            E, p, J = ER + 0j, PR + 0j, 1.0
        elif defo == 'nat':
            E, p, J = ER + 1j*delta, PR + 0j, 1.0
        else:
            chi = np.exp(-(ER**2 + PR**2)/w**2)
            dchi_dE = -2*ER/w**2*chi; dchi_dp = -2*PR/w**2*chi
            if defo == 'anom1':
                eta = np.abs(ER) + 2*np.abs(PR); deta_dE = np.sign(ER); deta_dp = 2*np.sign(PR)
            elif defo == 'anom2':
                eta = PR + PR**2/(2*m) - ER; deta_dE = -1.0*np.ones_like(ER); deta_dp = 1 + PR/m
            elif defo == 'bad':
                eta = 0*ER; deta_dE = 0*ER; deta_dp = 0*ER
            xi = m
            E = ER + 1j*lam*chi*eta
            p = PR + 1j*lam*chi*xi
            dE_dE = 1 + 1j*lam*(dchi_dE*eta + chi*deta_dE)
            dE_dp = 1j*lam*(dchi_dp*eta + chi*deta_dp)
            dp_dE = 1j*lam*dchi_dE*xi
            dp_dp = 1 + 1j*lam*dchi_dp*xi
            J = dE_dE*dp_dp - dE_dp*dp_dE
        integrand = J * 1j*np.exp(-(E**2 + p**2)/Q**2)/(E - p**2/(2*m) + 1j*eps)
        tot += integrand.sum()*h*h
    return tot

# symbolic: anom2 denominator zero only at lam=eps=0 (bump chi>0 as a positive symbol c)
ER, PR, lam, c, eps = sp.symbols('E_R p_R lambda c epsilon', real=True)
mm = sp.symbols('m', positive=True)
eta2 = PR + PR**2/(2*mm) - ER
E_ = ER + sp.I*lam*c*eta2; p_ = PR + sp.I*lam*c*mm
den = sp.expand(E_ - p_**2/(2*mm) + sp.I*eps)
re, im = sp.re(den), sp.im(den)
ER0 = sp.solve(sp.Eq(re, 0), ER)[0]
im_on = sp.simplify(im.subs(ER, ER0))
print('anom2 with bump c: Re=0 at E_R =', ER0, ';  Im there =', sp.factor(im_on))
print('   (positive for lam>0, c>0 or eps>0; zero only at lam*c = 0 and eps = 0)')
eta1 = sp.Abs(ER) + 2*sp.Abs(PR)
im1 = sp.im(sp.expand(ER + sp.I*lam*c*eta1 - (PR + sp.I*lam*c*mm)**2/(2*mm) + sp.I*eps))
print('anom1 with bump c: Im =', sp.simplify(im1), ' >= lam c (|E_R| + |p_R|) + eps')

print('\nnumerics (m=1, Q=1, bump width 2, grid h=0.004 on [-6,6]^2):')
res = {}
for eps_v in [0.1]:
    for d in ['orig', 'anom1', 'anom2', 'bad']:
        lam_v = 0 if d == 'orig' else 1.0
        res[(d, eps_v)] = integrate(d, lam_v, eps_v)
        print(f'  eps={eps_v:5.3f}  {d:6s} lam={lam_v}:  I = {res[(d, eps_v)]:.8f}')
ref = integrate('nat', 1.0, 0.0)
print(f'  eps -> 0+ reference (natural deformation, eps=0):        I = {ref:.8f}')
for d in ['anom1', 'anom2', 'bad']:
    v = integrate(d, 1.0, 0.0)
    res[(d, 0.0)] = v
    print(f'  eps=0      {d:6s} lam=1:  I = {v:.8f}   |I - ref| = {abs(v - ref):.2e}')
for eps_v in [0.05, 0.02]:
    v = integrate('orig', 0, eps_v)
    print(f'  eps={eps_v:5.3f}  orig  lam=0:  I = {v:.8f}   |I - ref| = {abs(v - ref):.2e}')

ok = []
def check(n, c_):
    ok.append(bool(c_)); print(('PASS ' if c_ else 'FAIL ') + n)
check('anom1 (eps=0.1) reproduces the undeformed integral', abs(res[('anom1', 0.1)] - res[('orig', 0.1)]) < 1e-4)
check('anom2 (eps=0.1) reproduces the undeformed integral', abs(res[('anom2', 0.1)] - res[('orig', 0.1)]) < 1e-6)
check('bad tangent deformation (eps=0.1) changes the integral (crosses the pole)', abs(res[('bad', 0.1)] - res[('orig', 0.1)]) > 1e-2)
check('anom2 at eps=0 equals the eps->0+ limit', abs(res[('anom2', 0.0)] - ref) < 1e-4)
check('anom1 at eps=0 equals the eps->0+ limit', abs(res[('anom1', 0.0)] - ref) < 1e-4)
check('bad deformation at eps=0 does not', abs(res[('bad', 0.0)] - ref) > 1e-2)
print(f'\nSUMMARY: {sum(ok)}/{len(ok)} checks passed')
