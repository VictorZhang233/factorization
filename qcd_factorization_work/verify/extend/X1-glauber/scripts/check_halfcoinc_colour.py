# Colour bookkeeping of the half-coincident pattern (one A spectator i; two B spectators j1, j2):
#   residual R = M2 + M2^dag + M1^dag M1 (O(c1 c2) part) = 2 i c1 c2 Im(W12) [X1, X2],
#   with X_e = T_i . T_{j_e}; [X1,X2] = i f^{abc} T_i^c T_{j1}^a T_{j2}^b (three-gluon-vertex colour).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
def su3():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1] = l[0][1,0] = 1; l[1][0,1] = -1j; l[1][1,0] = 1j; l[2][0,0] = 1; l[2][1,1] = -1
    l[3][0,2] = l[3][2,0] = 1; l[4][0,2] = -1j; l[4][2,0] = 1j; l[5][1,2] = l[5][2,1] = 1
    l[6][1,2] = -1j; l[6][2,1] = 1j; l[7][0,0] = l[7][1,1] = 1/np.sqrt(3); l[7][2,2] = -2/np.sqrt(3)
    return l/2
T = su3(); Tb = np.array([-t.T for t in T]); I3 = np.eye(3)
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = T[a] @ T[b] - T[b] @ T[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j*np.trace(comm @ T[c]))
def k3(a, b, c): return np.kron(np.kron(a, b), c)
allok = True
for name, TA, TB1, TB2 in (("3,3,3", T, T, T), ("3bar,3,3", Tb, T, T), ("3,3,3bar", T, T, Tb)):
    X1 = sum(k3(TA[a], TB1[a], I3) for a in range(8)); X2 = sum(k3(TA[a], I3, TB2[a]) for a in range(8))
    F = sum(f[a, b, c]*k3(TA[c], TB1[a], TB2[b]) for a in range(8) for b in range(8) for c in range(8))
    ok1 = np.allclose(X1 @ X2 - X2 @ X1, 1j*F)
    c1, c2 = 0.31, 0.53
    ok2 = True
    for W12 in (0.5 - 0.03j, 0.7 + 0.1j, 0.2, 0.5 + 0.2j):
        W21 = 1 - W12
        M2 = -c1*c2*(W12*(X2 @ X1) + W21*(X1 @ X2))
        M2d = M2.conj().T
        M1sq = c1*c2*(X1 @ X2 + X2 @ X1)
        R = M2 + M2d + M1sq
        ok2 = ok2 and np.allclose(R, 2j*c1*c2*np.imag(W12)*(X1 @ X2 - X2 @ X1))
    # singlet projection: does <[X1,X2]> vanish on the (i j1 j2) colour singlet(s)?
    w, V = np.linalg.eigh(sum(np.linalg.matrix_power(k3(TA[a], I3, I3) + k3(I3, TB1[a], I3) + k3(I3, I3, TB2[a]), 1) @
                              (k3(TA[a], I3, I3) + k3(I3, TB1[a], I3) + k3(I3, I3, TB2[a])) for a in range(8)))
    sing = V[:, np.abs(w) < 1e-9]
    ev = sing.conj().T @ (1j*F) @ sing if sing.shape[1] else np.zeros((0, 0))
    print(f"[{name}] [X1,X2] = i f T_i T_j1 T_j2: {ok1};  residual = 2i c1c2 Im(W12)[X1,X2]: {ok2};  "
          f"#singlets={sing.shape[1]}, singlet matrix of [X1,X2] = {np.round(ev, 6).tolist()}")
    allok = allok and ok1 and ok2
print("ALL PASS" if allok else "FAIL")
