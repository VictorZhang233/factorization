"""E30 -- independent check (Weyl representation, P_T solved for numerically) of the Dirac-structure
signs used in the PT argument of Collins 2002 / Collins 2011 Sec. 13.17:
  (PT)^dag psibar(y) Gamma psi(z) PT = psibar(-y) P_T^dag Gamma^* P_T psi(-z)       (Collins (13.120))
with P_T unitary, P_T^{-1} (gamma^mu)^* P_T = gamma^mu (Collins (13.118)).
Expected: Gamma = gamma^+ -> +gamma^+ (number density: Sivers term flips only through S -> -S),
          Gamma = gamma^+ gamma_5 -> -,  Gamma = gamma^+ gamma^j gamma_5 (transversity) -> -
          (=> Boer-Mulders h_1^perp, a quark-spin density in an unpolarized hadron, is PT-odd).
Plus the one-gluon eikonal phase: Im 1/(l^+ - i0) = +pi delta(l^+) (future-pointing, SIDIS)
versus Im 1/(l^+ + i0) = -pi delta(l^+) (past-pointing, DY): the T-odd (imaginary-part) piece flips.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2), complex)
# Weyl (chiral) representation
gam = [np.block([[Z, s0], [s0, Z]])] + [np.block([[Z, s], [-s, Z]]) for s in (sx, sy, sz)]
g5 = 1j * gam[0] @ gam[1] @ gam[2] @ gam[3]
eta = np.diag([1, -1, -1, -1])
ok = all(np.allclose(gam[m] @ gam[n] + gam[n] @ gam[m], 2 * eta[m, n] * np.eye(4)) for m in range(4) for n in range(4))
print('Clifford algebra (Weyl rep):', ok)
# solve P^{-1} gamma^mu* P = gamma^mu  <=>  gamma^mu* P - P gamma^mu = 0  (linear in P)
rows = []
for m in range(4):
    Gs = gam[m].conj()
    # vec(Gs P - P G) = (I kron Gs - G^T kron I) vec(P)  (column-major vec)
    rows.append(np.kron(np.eye(4), Gs) - np.kron(gam[m].T, np.eye(4)))
Mlin = np.vstack(rows)
u, s, vh = np.linalg.svd(Mlin)
null = vh[np.abs(s) < 1e-10] if np.sum(np.abs(s) < 1e-10) else vh[-1:]
P = vh[-1].conj().reshape(4, 4, order='F')
P = P / np.sqrt(abs(np.linalg.det(P))) ** 0.5
P = P / np.sqrt((P @ P.conj().T)[0, 0])
print('null space dim:', int(np.sum(s < 1e-10)), ' P_T unitary:', np.allclose(P @ P.conj().T, np.eye(4)),
      ' P^-1 g^mu* P = g^mu:', all(np.allclose(np.linalg.inv(P) @ gam[m].conj() @ P, gam[m]) for m in range(4)),
      ' commutes with gamma^0:', np.allclose(P @ gam[0], gam[0] @ P))
gp = (gam[0] + gam[3]) / np.sqrt(2)


def pt_sign(G):
    Gt = P.conj().T @ G.conj() @ P
    for sgn in (+1, -1):
        if np.allclose(Gt, sgn * G):
            return sgn
    return None


res = {'gamma^+': pt_sign(gp), 'gamma^+ gamma_5': pt_sign(gp @ g5),
       'gamma^+ gamma^1 gamma_5': pt_sign(gp @ gam[1] @ g5), 'gamma^+ gamma^2 gamma_5': pt_sign(gp @ gam[2] @ g5)}
for k, v in res.items():
    print('  PT sign of Gamma = %-26s : %+d' % (k, v))
expected = {'gamma^+': 1, 'gamma^+ gamma_5': -1, 'gamma^+ gamma^1 gamma_5': -1, 'gamma^+ gamma^2 gamma_5': -1}
ok &= res == expected
# eikonal imaginary parts (Sokhotski-Plemelj, numerically with a finite width)
e = 1e-4
l = np.linspace(-1, 1, 2000001)
f = np.exp(-l ** 2) * (1 + 0.3 * l)       # test function, f(0) = 1
im_future = np.trapezoid(np.imag(1 / (l - 1j * e)) * f, l)
im_past = np.trapezoid(np.imag(1 / (l + 1j * e)) * f, l)
print('  int Im 1/(l - i0) f = %.5f (pi f(0) = %.5f);  int Im 1/(l + i0) f = %.5f' % (im_future, np.pi, im_past))
ok &= abs(im_future - np.pi) < 2e-3 and abs(im_past + np.pi) < 2e-3
print('E30 PT/eikonal sign checks:', 'PASS' if ok else 'FAIL')
