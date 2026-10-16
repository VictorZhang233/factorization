"""W09 / v10: sign conventions of def:pdf-polarized.
 (a) helicity: ubar_h g+ g5 u_h = (2h) 2p+;  for v = C ubar^T (antiparticle of the same helicity) gamma5 v = -2h v and
     vbar_h g+ g5 v_h = -(2h) 2p+  =>  Delta f_{q/qbar,h}(xi) = +2h delta(1+xi), so Delta qbar(x) = + Delta f_q(-x);
 (b) transversity: i sigma^{j+} g5 = g+ g^j g5; transversely polarised free quark (spin along +x): ubar g+ g^1 g5 u = 2 p+;
 (c) gluon helicity: for eps_+ ~ (1, i)/sqrt2 (J_z = +1 for k along +z) i eps_T^{ij} eps^{i*} eps^j = -1, and
     Delta f_g := - sum_ij int dw/(2 pi xi P+) e^{-i xi P+ w} i eps_T^{ij} <G^{+i}(w) G^{+j}(0)>  gives  delta(1-xi) + delta(1+xi).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w9lib import *

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name)
    if ok: npass += 1
    else: nfail += 1

pp = 1.3
U = spinors_massless_z(pp)
C = 1j * G[2] @ G[0]
for h in U:
    u = U[h]
    check('(a) gamma5 u_h = 2h u_h (h=%+.1f)' % h, np.allclose(G5 @ u, 2 * h * u))
    check('(a) ubar g+ g5 u = (2h)(2p+) (h=%+.1f)' % h, np.isclose(bar(u) @ GPLUS @ G5 @ u, 2 * h * 2 * pp))
    v = C @ bar(u).T          # antiparticle with the same helicity label
    check('(a) v = C ubar^T: gamma5 v = -2h v (h=%+.1f)' % h, np.allclose(G5 @ v, -2 * h * v))
    vv = bar(v) @ GPLUS @ G5 @ v
    check('(a) vbar g+ g5 v = -(2h)(2p+) (h=%+.1f): %s' % (h, np.round(vv, 10)), np.isclose(vv, -2 * h * 2 * pp))
    # Delta f_{q/qbar}(xi) = -(vbar g+ g5 v)/(2p+) delta(1+xi) = (2h) delta(1+xi)
    check('(a) Delta f_{q/qbar,h} coefficient of delta(1+xi) = 2h (h=%+.1f)' % h, np.isclose(-vv / (2 * pp), 2 * h))
# (b) transversity
ux = (U[0.5] + U[-0.5]) / np.sqrt(2)
for j in (1, 2):
    sig = 0.5j * (G[j] @ GPLUS - GPLUS @ G[j])
    check('(b) i sigma^{%d+} g5 = g+ g^%d g5' % (j, j), np.allclose(1j * sig @ G5, GPLUS @ G[j] @ G5))
check('(b) spin along +x: ubar g+ g^1 g5 u = 2p+, ubar g+ g^2 g5 u = 0',
      np.isclose(bar(ux) @ GPLUS @ G[1] @ G5 @ ux, 2 * pp) and np.isclose(bar(ux) @ GPLUS @ G[2] @ G5 @ ux, 0))
# (c) gluon helicity
eps_plus = np.array([1, 1j]) / np.sqrt(2)
Jz = np.array([[0, -1j], [1j, 0]])            # (J_z)_{jk} = -i eps_{3jk} on (x, y)
check('(c) eps_+ = (1, i)/sqrt2 is the J_z = +1 eigenvector', np.allclose(Jz @ eps_plus, eps_plus))
epsT = np.array([[0, 1], [-1, 0]])            # eps_T^{12} = +1
first = 1j * sum(epsT[i, j] * np.conj(eps_plus[i]) * eps_plus[j] for i in range(2) for j in range(2))
second = 1j * sum(epsT[i, j] * np.conj(eps_plus[j]) * eps_plus[i] for i in range(2) for j in range(2))
check('(c) i eps^{ij} eps^{i*} eps^j = -1 (term e^{+ik+w}), i eps^{ij} eps^{j*} eps^i = +1 (term e^{-ik+w})',
      np.isclose(first, -1) and np.isclose(second, 1))
# Fourier transform with 1/(2 pi xi k+): (k+)^2 [first e^{ikw} + second e^{-ikw}] -> (1/xi)[first delta(xi-1) + second delta(xi+1)]
coef_at_plus1 = first / 1.0      # 1/xi at xi = +1
coef_at_minus1 = second / (-1.0)  # 1/xi at xi = -1
check('(c) with the overall minus sign: Delta f_{g/g,+} = delta(1-xi) + delta(1+xi)', np.isclose(-coef_at_plus1, 1) and np.isclose(-coef_at_minus1, 1))
print('\nSUMMARY v10: %d PASS, %d FAIL' % (npass, nfail))
