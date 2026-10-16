# X1 final revision -- P5 (round-3 fix F3): structure of the three-particle cuts of the direct-line ladder class C.
#
# A three-particle cut of a class-C graph at O(g^6) cuts one rung whose two ends lie on OPPOSITE sides of the cut
# (line A on one side, line B on the other).  With eikonal (straight-line) emission currents sharing the colour
# operator C = f^{a1 a2 b} T_A^{a1} T_B^{a2} of the line part of the Lipatov vertex,
#     A_A^mu = C v_A^mu/(v_A.k),   A_B^mu = -C v_B^mu/(v_B.k),
# the class yields only the interference D_C ~ C^dag C * [A_A^dag A_B + h.c.] contracted with a polarization sum.
# Checks: (i) Feynman gauge (-g): interference = 2 v_A.v_B/((v_A.k)(v_B.k)) > 0; self terms -v^2/(v.k)^2 <= 0 (outside C);
#         (ii) the full |A_A + A_B|^2 is the same in Feynman and light-cone gauge (conserved total current), while the
#              interference alone is NOT (D_C is gauge dependent);  (iii) light-like lines: self terms vanish.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(20261011)
g = np.diag([1.0, -1.0, -1.0, -1.0])
dot = lambda a, b: a @ g @ b

def timelike(y, phi):
    # unit time-like velocity with rapidity y along z and a small transverse tilt phi
    return np.array([np.cosh(y), np.sinh(phi)*0.0, 0.0, np.sinh(y)])

def onshell(kt, y, az):
    return np.array([kt*np.cosh(y), kt*np.cos(az), kt*np.sin(az), kt*np.sinh(y)])

def polsum(kind, k, n=None):
    if kind == 'F':
        return -g
    # light-cone gauge: -g_{mu nu} + (k_mu n_nu + n_mu k_nu)/(n.k), indices lowered with g
    kl = g @ k; nl = g @ n
    return -g + (np.outer(kl, nl) + np.outer(nl, kl))/dot(n, k)

ok_all = True
nA = np.array([1.0, 0, 0, 1.0]); nB = np.array([1.0, 0, 0, -1.0])
for case, (yA, yB) in [('timelike Y=0.5', (0.25, -0.25)), ('timelike Y=3', (1.5, -1.5)), ('lightlike', (None, None))]:
    worst_pos = np.inf; worst_id = 0.0; gauge_diff = 0.0; full_diff = 0.0; self_max = -np.inf
    for _ in range(2000):
        if yA is None:
            vA, vB = nA.copy(), nB.copy()
        else:
            vA, vB = timelike(yA, 0), timelike(yB, 0)
        k = onshell(rng.uniform(0.1, 3.0), rng.uniform(-4, 4), rng.uniform(0, 2*np.pi))
        JA = vA/dot(vA, k); JB = -vB/dot(vB, k)
        n_ref = np.array([1.0, *(rng.normal(size=3))]); n_ref[1:] *= 1/np.linalg.norm(n_ref[1:])   # light-like reference
        for kind in ('F', 'LC'):
            P = polsum(kind, k, n_ref)
            cross = 2*(JA @ P @ JB)
            selfs = JA @ P @ JA + JB @ P @ JB
            full = (JA + JB) @ P @ (JA + JB)
            if kind == 'F':
                crossF, fullF, selfF = cross, full, selfs
                pred = 2*dot(vA, vB)/(dot(vA, k)*dot(vB, k))
                worst_id = max(worst_id, abs(cross - pred)/abs(pred))
                worst_pos = min(worst_pos, cross)
                self_max = max(self_max, selfs)
            else:
                gauge_diff = max(gauge_diff, abs(cross - crossF)/abs(crossF))
                full_diff = max(full_diff, abs(full - fullF)/max(abs(fullF), 1e-300))
    ok = worst_id < 1e-12 and worst_pos > 0 and full_diff < 1e-9 and gauge_diff > 1e-3 and \
        (self_max <= 1e-12 if yA is not None else abs(self_max) < 1e-12)
    ok_all &= ok
    print(f"{case:15s}: Feynman interference = 2vA.vB/((vA.k)(vB.k)) to {worst_id:.1e} (min value {worst_pos:.3e} > 0);"
          f" max Feynman self term {self_max:.3e} (<= 0);  |full_F - full_LC|/full = {full_diff:.1e} (gauge invariant);"
          f"  max |cross_LC - cross_F|/cross_F = {gauge_diff:.2f} (gauge dependent);  ok={ok}")
print("ALL PASS" if ok_all else "SOME CHECK FAILED")
