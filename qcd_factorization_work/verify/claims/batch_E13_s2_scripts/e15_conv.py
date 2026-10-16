import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
m, Q, w = 1.0, 1.0, 2.0
def integ(defo, lam, eps, h, L=6.0, offset=0.0, delta_s=0.0):
    x = np.arange(-L, L + h/2, h) + offset
    tot = 0j
    P = x[None, :]
    for i0 in range(0, len(x), 200):
        ER = x[i0:i0+200][:, None]*np.ones_like(P); PR = np.ones_like(ER[:, :1])*P
        chi = np.exp(-(ER**2 + PR**2)/w**2); dcE = -2*ER/w**2*chi; dcp = -2*PR/w**2*chi
        if defo == 'orig':
            E, p, J = ER+0j, PR+0j, 1.0
        else:
            if defo == 'anom1':
                if delta_s > 0:
                    sE = np.sqrt(ER**2+delta_s**2); sP = np.sqrt(PR**2+delta_s**2)
                    eta = sE + 2*sP; deE = ER/sE; dep = 2*PR/sP
                else:
                    eta = np.abs(ER)+2*np.abs(PR); deE = np.sign(ER); dep = 2*np.sign(PR)
            elif defo == 'anom2':
                eta = PR + PR**2/(2*m) - ER; deE = -np.ones_like(ER); dep = 1 + PR/m
            E = ER + 1j*lam*chi*eta; p = PR + 1j*lam*chi*m
            J = (1 + 1j*lam*(dcE*eta + chi*deE))*(1 + 1j*lam*dcp*m) - (1j*lam*(dcp*eta + chi*dep))*(1j*lam*dcE*m)
        tot += (J*1j*np.exp(-(E**2+p**2)/Q**2)/(E - p**2/(2*m) + 1j*eps)).sum()*h*h
    return tot
eps = 0.1
for h in [0.008, 0.004, 0.002]:
    o = integ('orig', 0, eps, h); a1 = integ('anom1', 1, eps, h); a1m = integ('anom1', 1, eps, h, offset=h/2)
    print(f'h={h}: orig {o:.8f}  anom1(grid on kinks) {a1:.8f} diff {abs(a1-o):.2e}  anom1(midpoint grid) {a1m:.8f} diff {abs(a1m-o):.2e}')
for ds in [0.05, 0.02, 0.01]:
    a1s = integ('anom1', 1, eps, 0.004, delta_s=ds)
    print(f'smoothed |.| delta={ds}: anom1 {a1s:.8f}  diff to orig(h=0.004) {abs(a1s-integ("orig",0,eps,0.004)):.2e}')
