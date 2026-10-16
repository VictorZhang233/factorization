# Fixed re-run of check_halfcoinc_singlets.py (fix round 1).
# The original crashed (LAPACK ZHEEVD 'illegal value' / LinAlgError) on the 4096x4096 Casimir of (8,8,8,8)
# before reaching (8,8,8,8) and (3b,8,8,3).  Here the singlet space is computed inside the zero-weight
# subspace (C_tot commutes with the Cartan generators), in a common REAL weight basis of 3, 3bar, 8, so the
# singlet basis is real.  Reported: number of singlets, the basis-INDEPENDENT operator norm of P[X1,X2]P on
# the full singlet space of (i, j1, j2[, passive]), and the value on a random real singlet state (always 0:
# [X1,X2] is real antisymmetric in this basis).  The original script reported the basis-dependent
# max|<S'|[X1,X2]|S>| in a complex eigh basis (e.g. 0.378 for (3b,3b,3b,8), whose operator norm is 0.433).
# Which of these configurations are Drell-Yan remnant configurations is analysed in
# ../fix_r1_scripts/colour_dy_check.py (a passive parton in the hadron of i gives zero; in the hadron of
# j1, j2 it can give a non-zero value for complex colour states).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fix_r1_scripts'))
import importlib.util
spec = importlib.util.spec_from_file_location('cdc', os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              '..', 'fix_r1_scripts', 'colour_dy_check_lib.py'))
cdc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cdc)

rng = np.random.default_rng(7)
allok = True
for labels in [('3b', '3b', '3b'), ('3', '3', '3'), ('3b', '8', '3'), ('8', '8', '8'), ('8', '3', '3b'),
               ('3b', '3b', '3b', '8'), ('3', '3b', '3b', '3'), ('3b', '3', '3b', '3'), ('8', '8', '8', '8'),
               ('3b', '8', '8', '3')]:
    S, Ts = cdc.singlets(labels)
    X1 = cdc.X(Ts[0], Ts[1]); X2 = cdc.X(Ts[0], Ts[2])
    K = X1 @ X2 - X2 @ X1
    M = S.T @ K @ S if S.shape[1] else np.zeros((0, 0))
    real_ok = np.allclose(M.imag, 0) and np.allclose(M, -M.T)
    norm = np.max(np.abs(np.linalg.eigvals(M))) if M.size else 0.0
    c = rng.normal(size=S.shape[1]); c /= max(np.linalg.norm(c), 1e-300)
    vr = abs((S @ c) @ K @ (S @ c)) if S.shape[1] else 0.0
    allok = allok and real_ok and vr < 1e-12 and (len(labels) > 3 or norm < 1e-12)
    print(f"spectators (i, j1, j2{', passive' if len(labels) > 3 else ''}) = {labels}: #singlets = {S.shape[1]}, "
          f"||P[X1,X2]P|| = {norm:.4f}, real antisymmetric: {real_ok}, random real singlet: {vr:.1e}", flush=True)
print("three-spectator singlets: [X1,X2] = 0 identically; four-spectator singlets: non-zero norm, zero on real states")
print("ALL PASS" if allok else "SOME CHECK FAILED")
