# Check refdoc p.57/p.61 claim: two Glauber exchanges, strict instantaneous approximation with
# independent (symmetric) weighting of orderings => V^dag V = 1 - (1/4) C_A chi^2 T_A.T_B + O(chi^3);
# common ordering (box colour only) => V^dag V = 1 + O(chi^3).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
np.set_printoptions(precision=4, suppress=True)
# Gell-Mann
l = np.zeros((8,3,3), dtype=complex)
l[0][0,1]=l[0][1,0]=1
l[1][0,1]=-1j; l[1][1,0]=1j
l[2][0,0]=1; l[2][1,1]=-1
l[3][0,2]=l[3][2,0]=1
l[4][0,2]=-1j; l[4][2,0]=1j
l[5][1,2]=l[5][2,1]=1
l[6][1,2]=-1j; l[6][2,1]=1j
l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
tF = l/2
tFbar = -np.conj(tF)          # antifundamental generators  -t^{a*} = -t^{aT}
# adjoint generators (T^a)_{bc} = -i f^{abc}
f = np.zeros((8,8,8))
for a in range(8):
    for b in range(8):
        comm = tF[a]@tF[b]-tF[b]@tF[a]
        for c in range(8):
            f[a,b,c] = np.real(-2j*np.trace(comm@tF[c]))
tA = np.array([-1j*f[a] for a in range(8)])
CA = 3.0
reps = {'F':tF, 'Fbar':tFbar, 'A':tA}
def kron(A,B): return np.kron(A,B)
for nA,TA in reps.items():
    for nB,TB in reps.items():
        dA, dB = TA.shape[1], TB.shape[1]
        I = np.eye(dA*dB)
        c = sum(kron(TA[a],TB[a]) for a in range(8))          # T_A.T_B
        L = sum(kron(TA[a]@TA[b], TB[a]@TB[b]) for a in range(8) for b in range(8))  # ladder (box)
        X = sum(kron(TA[a]@TA[b], TB[b]@TB[a]) for a in range(8) for b in range(8))  # crossed
        ok1 = np.allclose(L, c@c); ok2 = np.allclose(X, c@c + CA/2*c)
        # strict Glauber approx: box = crossed = (i chi)^2/4 (delta-function weight split symmetrically)
        # amplitude to O(chi^2): V = 1 + i chi c + (i chi)^2/4 (L + X)
        # V^dag V - 1 at O(chi^2) = chi^2 c^2 + 2 Re[(i chi)^2/4 (L+X)]  (L, X Hermitian? check)
        M2_sym = -(1/4)*(L+X)          # coefficient of chi^2
        res_sym = c@c + M2_sym + M2_sym.conj().T
        M2_ord = -(1/2)*L              # common ordering: (i chi)^2/2 times box colour
        res_ord = c@c + M2_ord + M2_ord.conj().T
        print(f"{nA:4s} x {nB:4s}: L=c^2 {ok1}, X=c^2+(CA/2)c {ok2}; "
              f"sym-weight residual == -(CA/4) c : {np.allclose(res_sym, -(CA/4)*c)} ; "
              f"common-ordering residual == 0 : {np.allclose(res_ord, 0)} ; |c| eigenvalues {np.unique(np.round(np.linalg.eigvalsh((c+c.conj().T)/2),4))}")
# All orders: V = T exp(i chi c) is unitary for Hermitian c (trivial); show that
# the symmetrized-ordering N-fold exchange is NOT exp(i chi c) at N=2 already, in the colour-singlet qqbar channel:
TA, TB = tF, tFbar
c = sum(kron(TA[a],TB[a]) for a in range(8))
sing = np.eye(3).reshape(9)/np.sqrt(3)
print("singlet eigenvalue of T_q.T_qbar:", np.real(sing.conj()@c@sing), "(expect -C_F = -4/3)")
