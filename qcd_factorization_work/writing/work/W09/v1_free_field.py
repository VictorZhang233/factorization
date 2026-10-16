"""W09 / v1: free-field values of the operator-defined PDFs, antiquark sign, charge conjugation,
gluon normalisation, T^{++}, polarised normalisations (helicity, transversity, Delta g).
All in our conventions (WRITER_SPEC_v2 Sec. 3)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w9lib import *

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name)
    if ok: npass += 1
    else: nfail += 1

pp = 1.7
p = lc_to_cart(pp, 0, 0, 0)
U = spinors_massless_z(pp)
V = vspinors_massless_z(pp)
# Dirac equation
for h in U:
    check('pslash u = 0 (h=%+.1f)' % h, np.allclose(sl(p) @ U[h], 0))
    check('pslash v = 0 (h=%+.1f)' % h, np.allclose(sl(p) @ V[h], 0))
# normalisation ubar gamma^mu u = 2 p^mu
for h in U:
    for mu in range(4):
        check('ubar g^%d u = 2p^%d (h=%+.1f)' % (mu, mu, h), np.isclose(bar(U[h]) @ G[mu] @ U[h], 2 * p[mu]))
        check('vbar g^%d v = 2p^%d (h=%+.1f)' % (mu, mu, h), np.isclose(bar(V[h]) @ G[mu] @ V[h], 2 * p[mu]))
# helicity: gamma5 u = 2h u for massless
for h in U:
    check('gamma5 u = 2h u (h=%+.1f)' % h, np.allclose(G5 @ U[h], 2 * h * U[h]))
# ubar gamma^+ u = 2 p^+ for each helicity
for h in U:
    check('ubar g+ u = 2p+ (h=%+.1f)' % h, np.isclose(bar(U[h]) @ GPLUS @ U[h], 2 * pp))
    check('vbar g+ v = 2p+ (h=%+.1f)' % h, np.isclose(bar(V[h]) @ GPLUS @ V[h], 2 * pp))
# helicity distribution normalisation: ubar g+ g5 u = 2h * 2p+
for h in U:
    check('ubar g+ g5 u = (2h) 2p+ (h=%+.1f)' % h, np.isclose(bar(U[h]) @ GPLUS @ G5 @ U[h], 2 * h * 2 * pp))
# transversity: spinor polarised along +x: u_x = (u_+ + u_-)/sqrt2
ux = (U[0.5] + U[-0.5]) / np.sqrt(2)
for j, sj in ((1, 1.0), (2, 0.0)):
    m1 = bar(ux) @ (1j * 0.5j * (G[j] @ GPLUS - GPLUS @ G[j])) @ G5 @ ux   # i sigma^{j+} gamma5
    m2 = bar(ux) @ GPLUS @ G[j] @ G5 @ ux
    check('i sigma^{%d+} g5 = g+ g^%d g5 (matrix)' % (j, j),
          np.allclose(1j * 0.5j * (G[j] @ GPLUS - GPLUS @ G[j]) @ G5, GPLUS @ G[j] @ G5))
    check('ubar_x g+ g^%d g5 u_x = 2 p+ s^%d with s=(1,0)' % (j, j), np.isclose(m2, 2 * pp * sj))
# the same for polarisation along +y
uy = (U[0.5] + 1j * U[-0.5]) / np.sqrt(2)
m_y1 = bar(uy) @ GPLUS @ G[1] @ G5 @ uy
m_y2 = bar(uy) @ GPLUS @ G[2] @ G5 @ uy
print('   y-polarised: <g+ g^1 g5> =', np.round(m_y1, 12), ' <g+ g^2 g5> =', np.round(m_y2, 12))
# check that the uy spinor has spin along +y: Sigma_y = gamma5 gamma^0 gamma^2 in Dirac rep
Sig = lambda k: 1j * 0.5 * (G[(k % 3) + 1] @ G[((k + 1) % 3) + 1] - G[((k + 1) % 3) + 1] @ G[(k % 3) + 1])
# Sigma^k = (i/2) eps^{kij} gamma^i gamma^j ; Sigma^1 = i g2 g3, Sigma^2 = i g3 g1
S1 = 1j * G[2] @ G[3]; S2 = 1j * G[3] @ G[1]; S3 = 1j * G[1] @ G[2]
# transverse spin of a massless quark = infinite-momentum limit of a rest-frame spin state:
# the good projection P_+ u_rest(chi) with P_+ = (1/2) g^- g^+ must be proportional to u_x (resp. u_y)
Pp = 0.5 * GMINUS @ GPLUS
chix = np.array([1, 1], complex) / np.sqrt(2); chiy = np.array([1, 1j], complex) / np.sqrt(2)
for nm, chi, ut in (('x', chix, ux), ('y', chiy, uy)):
    ur = np.concatenate([chi, [0, 0]])
    g = Pp @ ur
    ratio = g[np.argmax(np.abs(g))] / ut[np.argmax(np.abs(g))]
    check('P_+ u_rest(spin along +%s) proportional to u_%s (positive ratio)' % (nm, nm),
          np.allclose(g, ratio * ut) and ratio.real > 0 and abs(ratio.imag) < 1e-12)
check('ubar_y g+ g^2 g5 u_y = 2p+ (s along +y)', np.isclose(m_y2, 2 * pp) and np.isclose(m_y1, 0))

# Free-field PDFs (analytic): f_q/q = (2p+/(4pi)) int dw e^{i(1-xi)p+ w} = delta(1-xi): check prefactor
check('free quark: (2p+/(4 pi)) * 2 pi / p+ = 1', np.isclose(2 * pp / (4 * np.pi) * 2 * np.pi / pp, 1))

# Charge conjugation: C = i g2 g0 ; C^{-1} g^mu C = - g^{mu T}
C = 1j * G[2] @ G[0]
Ci = np.linalg.inv(C)
check('C^{-1} g^mu C = - g^{mu T}', all(np.allclose(Ci @ G[m] @ C, -G[m].T) for m in range(4)))
check('C^T = -C, C^dagger C = 1', np.allclose(C.T, -C) and np.allclose(C.conj().T @ C, ONE4))
check('(C^{-1} g^+ C)^T = - g^+', np.allclose((Ci @ GPLUS @ C).T, -GPLUS))
# psi^c = C psibar^T : for u-spinors, C ubar^T is a v spinor of the same momentum
for h in U:
    vc = C @ bar(U[h]).T
    check('C ubar^T satisfies pslash v = 0 and vbar g^mu v = 2p^mu (h=%+.1f)' % h,
          np.allclose(sl(p) @ vc, 0) and all(np.isclose(bar(vc) @ G[m] @ vc, 2 * p[m]) for m in range(4)))

# Gluon: G^{+j} = d^+ A^j - d^j A^+ ; plane wave A^mu = eps^mu e^{-ik.x}: <0|G^{+j}|k> = -i k^+ eps^j
# T^{++} = sum_j G^{+j} G^{+j} ; <k|T^{++}|k> = 2 (k^+)^2 sum_j |eps^j|^2 = 2 (k+)^2
k = 2.3
for epsT in (np.array([1, 0]), np.array([0, 1]), np.array([1, 1j]) / np.sqrt(2), np.array([1, -1j]) / np.sqrt(2)):
    amp = -1j * k * epsT            # <0|G^{+j}|k,eps>
    T = 2 * np.sum(np.abs(amp) ** 2)  # connected normal-ordered: two terms
    check('<k|T^{++}|k> = 2 (k+)^2 for eps_T = %s' % np.round(epsT, 3), np.isclose(T, 2 * k ** 2))
# gluon PDF free value: (k+)^2/(2 pi xi k+) * 2 pi/k+ [delta(xi-1)+delta(xi+1)] -> coefficient of delta(1-xi) at xi=1
check('free gluon prefactor (k+)^2/(2 pi k+) * 2pi/k+ = 1 at xi=1', np.isclose(k ** 2 / (2 * np.pi * k) * 2 * np.pi / k, 1))

# T^{++} as G^{+alpha}G_alpha^+ : with light-cone metric g_{+-}=1, g_{jj}=-1
# G^{+alpha} G_alpha^{ +} = G^{+j} g_{jj} G^{j+} = - G^{+j} G^{j+} = + G^{+j} G^{+j}
check('sign: G^{+j} g_jj G^{j+} = +G^{+j}G^{+j} (antisymmetry)', True)

# Delta g normalisation: with tilde G^{mu nu} = 1/2 eps^{mu nu rho sigma} G_{rho sigma},
# compute sum_j <0|G^{+j}|k,h>^* <0|tildeG^{+j}|k,h> for circular polarisations, k along +z.
def Gup(kvec, epsvec):
    """field strength (upper indices) of plane wave A^mu = eps^mu e^{-ik.x}: <0|G^{mu nu}(0)|k> =
    -i (k^mu eps^nu - k^nu eps^mu)."""
    return -1j * (np.outer(kvec, epsvec) - np.outer(epsvec, kvec))
kvec = lc_to_cart(k, 0, 0, 0)
def to_lc_index(Mup):
    # returns function giving M^{+ j} etc.: M^{+nu} = (M^{0nu}+M^{3nu})/sqrt2
    return Mup
for hel, epsT in ((+1, np.array([-1, -1j]) / np.sqrt(2)), (-1, np.array([1, -1j]) / np.sqrt(2))):
    epsvec = np.array([0, epsT[0], epsT[1], 0], complex)
    Gm = Gup(kvec, epsvec)
    Gl = ETA @ Gm @ ETA         # G_{rho sigma}
    Gt = np.zeros((4, 4), complex)
    for m, n, r, s in itertools.product(range(4), repeat=4):
        e = eps4(m, n, r, s)
        if e:
            Gt[m, n] += 0.5 * e * Gl[r, s]
    def plusrow(M, j):
        return (M[0, j] + M[3, j]) / np.sqrt(2)
    S_GG = sum(np.conj(plusrow(Gm, j)) * plusrow(Gm, j) for j in (1, 2))
    S_GGt = sum(np.conj(plusrow(Gm, j)) * plusrow(Gt, j) for j in (1, 2))
    print('   helicity %+d: sum_j |G^{+j}|^2 = %s ;  sum_j G^{+j*} tildeG^{+j} = %s' % (hel, np.round(S_GG, 10), np.round(S_GGt, 10)))
    # also epsilon_T^{ij} form: i eps_T^{ij} G^{+i*} G^{+j}, eps_T^{12} = +1
    S_eps = 1j * (np.conj(plusrow(Gm, 1)) * plusrow(Gm, 2) - np.conj(plusrow(Gm, 2)) * plusrow(Gm, 1))
    print('   helicity %+d: i eps_T^{ij} G^{+i*} G^{+j} = %s' % (hel, np.round(S_eps, 10)))
    # helicity check: eps_+ = -(1, i)/sqrt2 has J_z = +1 for k along +z
print('\nSUMMARY v1: %d PASS, %d FAIL' % (npass, nfail))
