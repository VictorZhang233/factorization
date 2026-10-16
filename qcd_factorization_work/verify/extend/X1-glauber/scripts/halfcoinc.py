# [Fix round 1 label note] 'Thm T5' below is the author's ORIGINAL prediction, which was WRONG: the
# residual is 2 i c1 c2 Im(W12) [X1,X2] (REPORT L4(b)/T3), and Im W12 = O(1) in this unregulated model.
# Current labels: T3 (half-coincident model result, [V] withdrawn), L4 (colour).
# Half-coincident pattern: two SS lines on the SAME spectator of jet A but on DIFFERENT spectators of
# jet B (B -> b + s1 + s2).  Prediction (REPORT Thm T5): Re W_12 -> 1/2 (no log), hence the side-sum
# residual proportional to [T_i^a, T_i^b] (x) T_j1^a T_j2^b * Re(W_12 - W_21) vanishes at leading power.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoexch_rotated_fast import jet_params, FA, E
import twoexch_rotated_fast2 as R2

def JB2(p1, p2, pb2):
    beta, al1, al2 = pb2
    return (1j)**3/((p1 + p2 - beta)*(al1 - p1)*(al2 - p2))

def Irot(pa, pb2, a1, a2, cA, nt=3000, nphi=2000):
    ph = 1j; tot = 0
    t, wt = R2.gl(nt, -45, 25); phi, wp = R2.gl(nphi, 0, np.pi/2)
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp); r = np.exp(T)
    for q in itertools.product((1, -1), repeat=2):
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI)
        k1, k2 = ph*x1, ph*x2
        tot += np.sum(W*FA(k1, k2, pa, a1, a2, cA, q)*JB2(-k1, -k2, pb2)*r*r)
    return tot*ph**2/(2*np.pi)**2

if __name__ == '__main__':
    for lam in (0.03, 0.01, 0.003):
        sc = lambda v: (lam*v[0], lam*v[1])
        k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
        pa = jet_params(0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
        # jet B: B -> b + s1 + s2 (plus fractions xb, x1, x2), spectator j_e absorbs -k_e
        MB, mb, m1, m2 = 1.1*lam, 0.5*lam, 0.4*lam, 0.6*lam
        x1, x2 = 0.3, 0.35; xb = 1 - x1 - x2
        s1T, s2T = sc((-0.2, 0.3)), sc((0.25, -0.15))
        Es1 = E(s1T, m1, x1); Es2 = E(s2T, m2, x2)
        s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
        bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
        Eb = E(bT, mb, xb)
        al1 = Es1 - E(s1b, m1, x1); al2 = Es2 - E(s2b, m2, x2); beta = Eb + Es1 + Es2 - MB**2/2
        d0B = al1 + al2 - beta
        a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
        I12 = Irot(pa, (beta, al1, al2), a1, a2, '12'); I21 = Irot(pa, (beta, al1, al2), a1, a2, '21')
        N = I12 + I21; N0 = (1j/pa['d0'])*(1j/d0B)/(a1*a2)
        print(f"lam={lam}: B finals al1,al2={al1/lam**2:.3f},{al2/lam**2:.3f}  N/N0={N/N0:.8f}  W12={I12/N:.8f}  W21={I21/N:.8f}", flush=True)
