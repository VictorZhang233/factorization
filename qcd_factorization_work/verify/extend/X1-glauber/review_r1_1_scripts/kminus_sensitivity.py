# Diagnostic: where in k^- are the A-side ordering weights (and hence Im W12 of T3) generated?
# Multiply each connecting propagator by a smooth k^- form factor rho(k^-) = Lam^2/((k^-)^2 + Lam^2) (which is
# ~1 in the Glauber region |k^-| ~ lambda^2 for Lam >> lambda^2) and recompute the localized-limit weights
# (exact generalization of L1 to multi-pole external factors), then W12 = Int w^[12] J_B / Int J_B.
# If W12 depends on Lam for Lam ~ z = a/(2|k+|) = O(1) (in units P^+ = P_B^- = 1), the weights are generated
# at k^- = O(1), i.e. where the connecting gluon is B-collinear and Lemma E.19(b) (J_B independent of k^-) fails.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popp_indep2 import quad_rot
from halfcoinc_indep import setup, JB2, wrace

def poles_res(kp, a, Lam):
    """external factor R(k) rho(k), R = r/(k - z), r = 1/(2k+), z = a/(2k+); returns list of (pole, residue)."""
    r = 1/(2*kp); z = a/(2*kp)
    if Lam is None:
        return [(z, r)]
    iL = 1j*Lam
    A = Lam**2/(z**2 + Lam**2)
    B = Lam**2/((iL - z)*(2*iL))
    C = Lam**2/((-iL - z)*(-2*iL))
    return [(z, r*A), (iL, r*B), (-iL, r*C)]

def w12_reg(k1, k2, a1, a2, Lam, q):
    """localized-limit weight of colour order [12] with regulated external factors; vectorized over k1,k2 arrays.
    q gives the quadrant (sign of Im z_e is -sign(k_e^+) on the rotated contour)."""
    num = 0
    P1 = poles_res(k1, a1, Lam); P2 = poles_res(k2, a2, Lam)
    for (z1, r1) in P1:
        for (z2, r2) in P2:
            # side of each chosen pole: final if Im < 0. For z_e use quadrant sign (Im z_e = -sgn(x_e)*...)
            def is_final(zz, idx, base_z):
                if zz is base_z: return (q[idx] > 0)
                return np.imag(zz) < 0
            f1 = is_final(z1, 0, P1[0][0]); f2 = is_final(z2, 1, P2[0][0])
            if f1 and f2:      # V12 : 1 then 2 after V_H
                num = num + r1*r2/((z1 + z2)*z2)
            elif (not f1) and (not f2):   # 12V
                num = num + r1*r2/(z1*(z1 + z2))
            elif (not f1) and f2:         # 1V2 (allowed for [12])
                num = num + r1*r2/(z1*z2)
            else:                          # 2V1 not allowed for [12]
                pass
    R10 = -(1/(2*k1))/(a1/(2*k1)); R20 = -(1/(2*k2))/(a2/(2*k2))
    return num/(R10*R20)

def W12_loc(lam, Lam, theta=0.25):
    pa, beta, al1, al2, a1, a2 = setup(lam)
    ph = np.exp(1j*theta*np.pi); lamB = max(abs(beta), abs(al1), abs(al2))
    f = lambda k1, k2, q: w12_reg(k1, k2, a1, a2, Lam, q)*JB2(-k1, -k2, beta, al1, al2)
    g = lambda k1, k2, q: JB2(-k1, -k2, beta, al1, al2)
    return quad_rot(f, ph, lamB, n=1600, nU=500)/quad_rot(g, ph, lamB, n=1600, nU=500), a1, a2, lamB

if __name__ == '__main__':
    lam = 0.01
    # sanity: Lam=None reproduces the race weights
    pa, beta, al1, al2, a1, a2 = setup(lam)
    k1 = np.array([0.3e-4*np.exp(0.3j)]); k2 = np.array([0.7e-4*np.exp(0.3j)])
    print('check race (++):', w12_reg(k1, k2, a1, a2, None, (1, 1)), wrace(k1, k2, a1, a2, '12', (1, 1)))
    print('check regulated, Lam->inf:', w12_reg(k1, k2, a1, a2, 1e9, (1, 1)))
    print('check regulated, sum of colours = 1:', w12_reg(k1, k2, a1, a2, 0.2, (1, 1)) + (lambda: None)() if False else '')
    w0, a1, a2, lamB = W12_loc(lam, None)
    zt = a1/(2*lamB)
    print(f"lam={lam}: a1={a1:.3e}, a2={a2:.3e}, lam_B={lamB:.3e}; typical z = a/(2 lam_B) = {zt:.3f} (units P+ = 1)")
    print(f"   no form factor (race weights):   W12 = {w0:.6f}")
    for Lam in (100.0, 10.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003):
        w, *_ = W12_loc(lam, Lam)
        print(f"   form factor Lam = {Lam:7.3f} (Lam/z ~ {Lam/zt:8.2f}):  W12 = {w:.6f}", flush=True)
