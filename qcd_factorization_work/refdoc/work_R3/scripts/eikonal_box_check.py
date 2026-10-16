# Brute-force check of the inner x_B integrals in eikonal_box.py with finite i*eps
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'eikonal_box.py')).read().split("for (a,b,Y)")[0])
def brute(xA, a, b, Y, eps, sgn):
    # sgn=+1: Int g/(xB + i eps) ; sgn=-1: Int g/(-xB + i eps)
    xB = np.concatenate([np.linspace(-400,-20,40001), np.linspace(-20,20,2000001), np.linspace(20,400,40001)])
    Q = (-(xA**2+xB**2) + 2*np.cosh(Y)*xA*xB)/np.sinh(Y)**2
    g = 1/((Q-a+1j*eps)*(Q-b+1j*eps))
    f = g/(sgn*xB + 1j*eps)
    return np.trapz(f, xB)
for xA in [0.37, -1.6, 2.2]:
    a,b,Y = 1.0, 2.5, 1.0
    for eps in [1e-2, 3e-3, 1e-3]:
        print(f"xA={xA} eps={eps}: brute cross={brute(xA,a,b,Y,eps,+1):.6f}  residue={complex(inner_cross(mp.mpf(xA),mp.mpf(a),mp.mpf(b),mp.mpf(Y))):.6f} | "
              f"brute box={brute(xA,a,b,Y,eps,-1):.6f} residue={complex(inner_box(mp.mpf(xA),mp.mpf(a),mp.mpf(b),mp.mpf(Y))):.6f}")
