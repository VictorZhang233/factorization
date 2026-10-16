"""(1) Ordering weights for non-commuting equal-time insertions (p.195):
     w_{12} = z1/(z1+z2);  N insertions, order pi:  prod_j z_j / prod_m sum_{l>=m} z_{pi(l)}.
(2) Colour algebra behind Prop. E.31(iv): crossed - ladder = (C_A/2) T_A.T_B, and the O(chi^2) residue
     -(1/2) C_A chi^2 Re(p_opp) T_A.T_B of the side sum for two SS lines on the same pair of partons."""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
mp.mp.dps = 25

print("(1) ordering weights")
def tordered(zs, order):
    # int_{0<tau_{order[0]}<tau_{order[1]}<...} prod_j e^{-i z_j tau_j}, by iterated exact integration
    # = prod_i 1/(i * sum_{m>=i} z_{order[m]})
    val = mp.mpc(1)
    N = len(zs)
    for i in range(N):
        val *= 1 / (1j * sum(zs[order[m]] for m in range(i, N)))
    return val
def numeric2(z1, z2, order):
    # brute-force numeric 2D integral for N=2 as an independent check
    f = lambda t2: mp.exp(-1j * (z2 if order == (0, 1) else z1) * t2) * \
        (1 - mp.exp(-1j * (z1 if order == (0, 1) else z2) * t2)) / (1j * (z1 if order == (0, 1) else z2))
    return mp.quad(f, [0, mp.inf])
z1, z2 = mp.mpc(0.8, -0.3), mp.mpc(1.7, -0.2)
full = 1 / (1j * z1) / (1j * z2)
w12 = numeric2(z1, z2, (0, 1)) / full
print(f"  N=2: numeric w12={mp.nstr(w12,10)}   z1/(z1+z2)={mp.nstr(z1/(z1+z2),10)}")
zs = [mp.mpc(0.8, -0.1), mp.mpc(1.7, -0.2), mp.mpc(0.4, -0.05)]
fullN = 1
for z in zs: fullN *= 1 / (1j * z)
tot = 0
for order in itertools.permutations(range(3)):
    w = tordered(zs, order) / fullN
    form = zs[0] * zs[1] * zs[2]
    den = 1
    for m in range(3): den *= sum(zs[order[l]] for l in range(m, 3))
    tot += w
    print(f"  N=3 order {order}: w={mp.nstr(w,8)}  formula={mp.nstr(form/den,8)}")
print(f"  sum of weights = {mp.nstr(tot,12)} (should be 1)")

print("\n(2) colour algebra")
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = lam / 2
tbar = -np.transpose(t, (0, 2, 1))   # antitriplet generators
CA = 3.0
I3 = np.eye(3)
for name, TA, TB in [("3 x 3", t, t), ("3 x 3bar", t, tbar)]:
    A = [np.kron(TA[a], I3) for a in range(8)]
    B = [np.kron(I3, TB[a]) for a in range(8)]
    c = sum(A[a] @ B[a] for a in range(8))
    L = sum(A[a] @ A[b] @ B[a] @ B[b] for a in range(8) for b in range(8))
    X = sum(A[a] @ A[b] @ B[b] @ B[a] for a in range(8) for b in range(8))
    print(f"  {name}: ||X - L - (C_A/2) c|| = {np.linalg.norm(X - L - CA/2 * c):.2e};  ||L - c^2|| = {np.linalg.norm(L - c @ c):.2e}")
    chi = 0.37
    for p in [0.0, 0.5, 1.0, 0.3 + 0.2j]:
        amp2 = 0.5 * (-1j * chi)**2 * ((1 - p) * L + p * X)
        conj2 = amp2.conj().T            # conjugate-side double exchange = hermitian conjugate
        one_one = (1j * chi * c) @ (-1j * chi * c)
        total = amp2 + conj2 + one_one
        pred = -0.5 * CA * chi**2 * np.real(p) * c
        print(f"     p_opp={p}: ||side-sum - (-(1/2)C_A chi^2 Re p c)|| = {np.linalg.norm(total - pred):.2e};  ||side-sum|| = {np.linalg.norm(total):.3e}")
print("  => the O(chi^2) side sum vanishes iff Re p_opp = 0 (orderings perfectly correlated, e.g. RS regulator:")
print("     crossed Glauber boxes vanish), and equals -(1/4) C_A chi^2 T_A.T_B for p_opp = 1/2.")
