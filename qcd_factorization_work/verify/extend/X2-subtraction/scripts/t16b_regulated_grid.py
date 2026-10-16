"""X2/T16b: time-like rapidity-regulated massive-photon remainder on a log grid (vectorized LCPT engine).
int r^(Y) and int |rho_r^(Y)| (eps=0) vs Y, compared with the light-like values int r = -lam^2(L+1), norm ~ 3 lam^2 L."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, warnings
warnings.filterwarnings('ignore')
import t16_massive_regulated as T16
def grid_integrals(M2, Y, sgn=1, nx=1600, nk=900):
    lx = np.linspace(-40, 3*Y + 12, nx); lk = np.linspace(-40, 12, nk)
    LX, LK = np.meshgrid(lx, lk, indexing='ij')
    x = np.exp(LX).ravel(); k = np.exp(LK).ravel()
    r = T16.rho('r', x, k, M2, Y, sgn).reshape(LX.shape)
    r = np.nan_to_num(r)
    w = r*np.exp(LX)*np.exp(LK)
    I = np.trapz(np.trapz(w, lk, axis=1), lx); N = np.trapz(np.trapz(np.abs(w), lk, axis=1), lx)
    return I, N
for M2 in [1e-2, 1e-3, 1e-4]:
    L = np.log(1/M2)
    for Yf in [0.25, 0.5, 1.0, 2.0, 4.0]:
        Y = Yf*L
        I, N = grid_integrals(M2, Y)
        print(f"M2={M2:.0e} Y={Y:6.2f} (Y/L={Yf}): int r = {I:+.5e} ({I/M2:+.3f} lam^2; light-like -(L+1) = {-(L+1):.3f});"
              f"  norm = {N:.5e} ({N/(M2*L):.3f} lam^2 L)", flush=True)
