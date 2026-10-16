# Check of refdoc p.67 (proof of Thm 10.6): under V = PT (antiunitary), with Peskin-Schroeder conventions
#   P psi(t,x) P^-1 = gamma^0 psi(t,-x),  T psi(t,x) T^-1 = (-gamma^1 gamma^3) psi(-t,x)  (T antiunitary)
# => V psi(x) V^-1 = M psi(-x), M = -gamma^1 gamma^3 gamma^0, and
#    V [psibar(w) Gamma psi(0)] V^-1 = psi^dag(-w) M^dag (gamma^0)^* Gamma^* M psi(0)
# Is this psibar(-w) Gamma' psi(0) with Gamma' = +Gamma for Gamma = gamma^mu (no hermitian conjugation needed)?
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
I2 = np.eye(2); Z2 = np.zeros((2,2))
s = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
g0 = np.block([[Z2,I2],[I2,Z2]]).astype(complex)
gi = [np.block([[Z2,si],[-si,Z2]]) for si in s]
g = [g0]+gi
g5 = 1j*g[0]@g[1]@g[2]@g[3]
M = -g[1]@g[3]@g[0]
names = ['0','1','2','3']
for mu in range(4):
    lhs = M.conj().T @ g0.conj() @ g[mu].conj() @ M
    print(f"vector  mu={names[mu]}: M^+ g0* (g^mu)* M == +g0 g^mu ? {np.allclose(lhs, g0@g[mu])}  == -g0 g^mu ? {np.allclose(lhs, -g0@g[mu])}")
for mu in range(4):
    G = g[mu]@g5
    lhs = M.conj().T @ g0.conj() @ G.conj() @ M
    print(f"axial   mu={names[mu]}: -> +g0 g^mu g5 ? {np.allclose(lhs, g0@G)}  -> -g0 g^mu g5 ? {np.allclose(lhs, -g0@G)}")
# gamma^+ = (g0+g3)/sqrt2 component and the sigma^{+j} (transversity) structure i sigma^{+j} g5
gp = (g0+g[3])/np.sqrt(2)
lhs = M.conj().T @ g0.conj() @ gp.conj() @ M
print("gamma^+ maps to +gamma^+ :", np.allclose(lhs, g0@gp))
for j in (1,2):
    sig = 0.5j*(gp@g[j]-g[j]@gp)
    G = 1j*sig@g5
    lhs = M.conj().T @ g0.conj() @ G.conj() @ M
    print(f"i sigma^(+{j}) g5 maps to: +? {np.allclose(lhs,g0@G)}  -? {np.allclose(lhs,-g0@G)}")
# M unitary? and antiunitary consistency M M* = ?
print("M unitary:", np.allclose(M@M.conj().T, np.eye(4)), "; M M^* =", np.round(M@M.conj(),3).diagonal())
