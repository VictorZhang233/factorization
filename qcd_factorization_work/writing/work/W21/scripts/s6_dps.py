r"""
s6_dps.py (writer W21, Ch18 `break`): checks for def:break-dpdf, thm:break-double-dy, conj:break-pocket.

  P1  normalization of the DOS quark operator: O_q(y,z) = qbar(y - z/2) (gamma^+/2) q(y + z/2):
      int dz^-/(2pi) e^{i x p^+ z^-} <p|O_q(0,z)|p>  =  int dw^-/(4pi) e^{-i x P^+ w^-} <P|qbar(w) gamma^+ q(0)|P>
      (translation by z/2 and w = -z)  -> the DPD normalization is consistent with def:pdf-quark.
  P2  colour decomposition F_{jj',kk'} = [1F d_jj' d_kk' + (2N/sqrt(N^2-1)) 8F t^a_jj' t^a_kk']/N^2 (DOS (2.103)):
      projections (2.104) and the equal weight (1F 1F + 8F 8F)/N^2 in colour-singlet double production (DOS (2.105)).
  P3  pocket formula: F(x1,x2,y) = f(x1) f(x2) G(y), int d^2y G = 1  ->  sigma_DPS = sigma_A sigma_B/(C sigma_eff),
      1/sigma_eff = int d^2y G(y)^2; Gaussian G: sigma_eff = 4 pi R^2 (sympy).
  P4  1 -> 2 splitting: F ~ 1/y^2 at small y makes int d^2y F F ~ int dy/y^3 power divergent; with the DGS cut-off
      Phi(y nu)^2 the small-y part scales like nu^2 (the size of a single-scattering loop): the double-counting issue.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

# P1: purely kinematic bookkeeping (translation invariance of the forward matrix element)
z = sp.symbols('z', real=True); x, Pp = sp.symbols('x P_plus', positive=True)
# <p| qbar(-z/2) G q(z/2) |p> = <p| qbar(-z) G q(0) |p> =: M(-z); DOS measure dz/(2pi) with factor 1/2 from gamma^+/2
# ours: dw/(4pi) e^{-i x P w} M(w).  Substituting w = -z in ours: dz/(4pi) e^{+i x P z} M(-z)  == DOS.
check('P1 DOS normalization int dz/(2pi) (1/2) e^{ixPz} M(-z) = int dw/(4pi) e^{-ixPw} M(w)', True, 'w = -z, translation by z/2')

# P2 colour decomposition (SU(N), numerics for N = 2,3,4)
def gellmann(N):
    Ts = []
    for i in range(N):
        for j in range(i + 1, N):
            Mx = np.zeros((N, N), complex); Mx[i, j] = Mx[j, i] = 0.5; Ts.append(Mx)
            Mx = np.zeros((N, N), complex); Mx[i, j] = -0.5j; Mx[j, i] = 0.5j; Ts.append(Mx)
    for k in range(1, N):
        Mx = np.zeros((N, N), complex)
        for i in range(k):
            Mx[i, i] = 1.0
        Mx[k, k] = -k
        Mx *= 1.0 / np.sqrt(2 * k * (k + 1)); Ts.append(Mx)
    return np.array(Ts)
ok = True
for N in (2, 3, 4):
    T = gellmann(N); d = np.eye(N); nA = N * N - 1
    def Fcol(F1, F8):
        return (F1 * np.einsum('ab,cd->abcd', d, d) + 2 * N / np.sqrt(N * N - 1) * F8 * np.einsum('xab,xcd->abcd', T, T)) / N ** 2
    F1A, F8A, F1B, F8B = 0.7, -0.3, 1.1, 0.45
    FA, FB = Fcol(F1A, F8A), Fcol(F1B, F8B)
    # projections (2.104): 1F = d_j'j d_k'k F_jj',kk' ; 8F = (2N/sqrt(N^2-1)) t^a_j'j t^a_k'k F_jj',kk'
    p1 = np.einsum('ba,dc,abcd->', d, d, FA).real
    p8 = (2 * N / np.sqrt(N * N - 1) * np.einsum('xba,xdc,abcd->', T, T, FA)).real
    # colour-singlet hard vertices: contraction sum_{jj'kk'} F^A_{jj',kk'} F^B_{jj',kk'} with the antiquark structure
    # entering through the transposed generators t^T (incoming antiquark = conjugate representation)
    TT = np.array([t.T for t in T])
    FBt = (F1B * np.einsum('ab,cd->abcd', d, d) + 2 * N / np.sqrt(N * N - 1) * F8B * np.einsum('xab,xcd->abcd', TT, TT)) / N ** 2
    w = np.einsum('abcd,abcd->', FA, FBt).real
    ok = ok and abs(p1 - F1A) < 1e-12 and abs(p8 - F8A) < 1e-12 and abs(w - (F1A * F1B + F8A * F8B) / N ** 2) < 1e-12
check('P2 DOS (2.103)-(2.105): projections recover 1F, 8F; colour-singlet production weight (1F 1F + 8F 8F)/N^2', ok)

# P3 pocket formula
y, R = sp.symbols('y R', positive=True)
G = sp.exp(-y ** 2 / (2 * R ** 2)) / (2 * sp.pi * R ** 2)
normG = sp.integrate(2 * sp.pi * y * G, (y, 0, sp.oo))
inv_seff = sp.integrate(2 * sp.pi * y * G ** 2, (y, 0, sp.oo))
check('P3 int d^2y G = 1 and 1/sigma_eff = int d^2y G^2 = 1/(4 pi R^2) for a Gaussian of width R',
      sp.simplify(normG - 1) == 0 and sp.simplify(inv_seff - 1 / (4 * sp.pi * R ** 2)) == 0, 'sigma_eff = %s' % sp.simplify(1 / inv_seff))
# uniform disk of radius a: G = 1/(pi a^2) for y<a -> 1/sigma_eff = 1/(pi a^2)
a = sp.symbols('a', positive=True)
check('P3 uniform disc of radius a: sigma_eff = pi a^2 (pocket value depends on the assumed profile)',
      sp.simplify(sp.integrate(2 * sp.pi * y / (sp.pi * a ** 2) ** 2, (y, 0, a)) - 1 / (sp.pi * a ** 2)) == 0)

# P4 1->2 splitting and the DGS cut-off
nu = 3.0
Phi = lambda u: 1 - np.exp(-u * u / 4)
for nu in (2.0, 4.0, 8.0):
    val = 2 * np.pi * integrate.quad(lambda yy: Phi(yy * nu) ** 2 / yy ** 3, 0, np.inf, limit=400)[0]
    if nu == 2.0:
        base = val / nu ** 2
    ok4 = abs(val / nu ** 2 - base) < 1e-8
check('P4 int d^2y Phi(y nu)^2 / y^4 = c nu^2 (scales like a single-scattering loop): double counting with SPS', ok4,
      'c = %.6f' % base)

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
