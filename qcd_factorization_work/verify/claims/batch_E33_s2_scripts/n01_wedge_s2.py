# N01 stage-2: two-gluon exchange between infinite time-like Wilson lines, by a COORDINATE-SPACE
# (proper-time) route, independent of the k^+/k^- residue method used in the project and by stage 1.
#
# Definition (same normalisation as refdoc/work_R3/scripts/eikonal_box.py):
#   J_sigma = Int dxA dxB [i/(xA+i0)] [i/(sigma xB+i0)] g(k),  xA = vA.k, xB = vB.k (2D longitudinal k),
#   g = 1/((k^2-a+i0)(k^2-b+i0)),  dxA dxB = sinhY d^2k.   sigma=-1: box (ladder), sigma=+1: crossed.
# With i/(y+i0) = Int_0^inf dl e^{i l y - eps l}:
#   J_sigma = sinhY Int_0^inf dlA dlB e^{-eps(lA+lB)} G(lA vA + sigma lB vB),
#   G(x) = Int d^2k e^{i k.x} g(k) = (-2 pi i/(a-b)) [K0(sqrt(a) s) - K0(sqrt(b) s)],  s = sqrt(-x^2 + i0).
# Polar coordinates lA = r cos(th), lB = r sin(th): x^2 = r^2 (1 + sigma sin(2th) coshY).
#   r-integral: Int_0^inf r e^{-p r} K0(kappa r) dr = 1/(kappa^2-p^2) + p ln((p+w)/kappa)/w^3, w = sqrt(p^2-kappa^2)
#   (-> 1/kappa^2 as p->0), giving the closed forms
#   J_sigma(eps->0) = -(2 pi i sinhY/(ab)) Int_0^{pi/2} dth / (1 + sigma coshY sin(2th) - i0)
#   => J_cross = -2 pi i Y/(ab),  J_box = (2 pi/(ab)) (pi + i Y).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
mp.mp.dps = 25

def Ir(p, kap):
    """Int_0^inf r e^{-p r} K0(kap r) dr, kap in the closed right half plane (kap = i beta + 0 allowed)."""
    w = mp.sqrt(p**2 - kap**2)
    return 1/(kap**2 - p**2) + p*mp.log((p + w)/kap)/w**3

# --- (0) check the r-integral formula against direct quadrature (real, complex and imaginary kappa)
print("(0) r-integral closed form vs direct quadrature:")
for p, kap in [(mp.mpf('0.7'), mp.mpf('1.3')), (mp.mpf('0.3'), mp.mpc('0.8', '0.6')), (mp.mpf('0.4'), mp.mpc('0', '1.1'))]:
    direct = mp.quad(lambda r: r*mp.exp(-p*r)*mp.besselk(0, kap*r), [0, 1, 5, 20, 60, mp.inf])
    print(f"    p={mp.nstr(p,3)}, kappa={mp.nstr(kap,3)}: closed={mp.nstr(Ir(p,kap),12)}  direct={mp.nstr(direct,12)}")

def q_of(th, sigma, Y):
    X = 1 + sigma*mp.sin(2*th)*mp.cosh(Y)        # x^2 = r^2 X ; s = r sqrt(-X + i0)
    return mp.sqrt(-X) if X < 0 else 1j*mp.sqrt(X)  # timelike (X>0): +i sqrt(X) (Feynman i0)

def J_eps(sigma, a, b, Y, eps):
    """finite-eps value, theta integral done numerically (split at the light-cone angles)."""
    def f(th):
        q = q_of(th, sigma, Y); p = eps*(mp.cos(th) + mp.sin(th))
        return mp.sinh(Y)*(-2j*mp.pi/(a - b))*(Ir(p, mp.sqrt(a)*q) - Ir(p, mp.sqrt(b)*q))
    pts = [mp.mpf(0), mp.pi/2]
    if sigma < 0:
        th1 = mp.asin(1/mp.cosh(Y))/2               # light cone: sin(2th) coshY = 1
        pts = [mp.mpf(0), th1, mp.pi/2 - th1, mp.pi/2]
    return mp.quad(f, pts)

def J_closed(sigma, a, b, Y):
    return (2*mp.pi/(a*b))*(mp.pi + 1j*Y) if sigma < 0 else -2j*mp.pi*Y/(a*b)

print("\n(1) theta-integral identity  Int_0^{pi/2} dth/(1 + s coshY sin2th - i delta):")
for Y in [mp.mpf('0.4'), mp.mpf('1'), mp.mpf('3')]:
    for s in (+1, -1):
        dl = mp.mpf('1e-7')
        th1 = mp.asin(1/mp.cosh(Y))/2
        pts = [0, mp.pi/2] if s > 0 else [0, th1, mp.pi/2 - th1, mp.pi/2]
        val = mp.quad(lambda t: 1/(1 + s*mp.cosh(Y)*mp.sin(2*t) - 1j*dl), pts)
        expect = Y/mp.sinh(Y) if s > 0 else (-Y + 1j*mp.pi)/mp.sinh(Y)
        print(f"    Y={mp.nstr(Y,3)}, sigma={s:+d}: numeric={mp.nstr(val,10)}  closed={mp.nstr(expect,10)}")

print("\n(2) finite-eps coordinate-space evaluation -> closed forms as eps -> 0:")
for (a, b, Y) in [(1.0, 2.5, 1.0), (0.7, 0.3, 3.0), (2.0, 0.1, 0.4)]:
    a, b, Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    for sigma, name in ((-1, 'box  '), (+1, 'cross')):
        Jc = J_closed(sigma, a, b, Y)
        row = []
        for eps in ['1e-2', '1e-3', '1e-4']:
            Je = J_eps(sigma, a, b, Y, mp.mpf(eps))
            row.append(mp.nstr(abs(Je - Jc)/abs(Jc), 3))
        print(f"    a={mp.nstr(a,2)}, b={mp.nstr(b,2)}, Y={mp.nstr(Y,2)} {name}: closed = {mp.nstr(Jc,10)};"
              f"  rel. dev. at eps=1e-2,1e-3,1e-4: {row}")
    print(f"        Re J_cross(eps=1e-4) = {mp.nstr(mp.re(J_eps(+1, a, b, Y, mp.mpf('1e-4'))), 3)}  (closed form: 0)")

# (3) colour factors for SU(N), N=2,3,4: fundamental, antifundamental, adjoint
def gellmann(N):
    T = []
    for i in range(N):
        for j in range(i+1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 0.5; T.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -0.5j; m[j, i] = 0.5j; T.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        T.append(m/np.sqrt(2*k*(k+1)))
    return T
def adjoint(T):
    n = len(T); f = np.zeros((n, n, n))
    for a_ in range(n):
        for b_ in range(n):
            comm = T[a_] @ T[b_] - T[b_] @ T[a_]
            for c_ in range(n):
                f[a_, b_, c_] = np.real(-2j*np.trace(comm @ T[c_]))   # [Ta,Tb] = i f^{abc} Tc, Tr TaTb = 1/2
    return [-1j*f[a_] for a_ in range(n)], f                         # (T^a_adj)_{bc} = -i f^{abc}
print("\n(3) colour algebra: c_box = X^2, c_cross = X^2 + (C_A/2) X  (max abs deviation)")
for N in (2, 3, 4):
    TF = gellmann(N); TA, f = adjoint(TF); TFbar = [-t.conj() for t in TF]
    CA = np.einsum('abc,abd->cd', f, f)[0, 0]
    reps = {'F': TF, 'Fbar': TFbar, 'A': TA}
    out = []
    for ra, rb in [('F', 'F'), ('F', 'Fbar'), ('A', 'F'), ('A', 'A')]:
        A_, B_ = reps[ra], reps[rb]
        X = sum(np.kron(A_[i], B_[i]) for i in range(len(TF)))
        cbox = sum(np.kron(A_[j] @ A_[i], B_[j] @ B_[i]) for i in range(len(TF)) for j in range(len(TF)))
        ccr = sum(np.kron(A_[j] @ A_[i], B_[i] @ B_[j]) for i in range(len(TF)) for j in range(len(TF)))
        out.append(f"{ra}x{rb}: {max(np.abs(cbox - X@X).max(), np.abs(ccr - X@X - CA/2*X).max()):.1e}")
    print(f"    SU({N}) (C_A = {CA:.6f}): " + ", ".join(out))

# (4) unitarity at O(chi^2): V = 1 + i chi X + (1/2)(i chi)^2 [X^2 + p (C_A/2) X], p = -iY/pi
print("\n(4) V^dag V - 1 at O(chi^2) for random Hermitian X, p_opp = -iY/pi vs strict-window p = 1/2:")
rng = np.random.default_rng(1); H = rng.normal(size=(5, 5)) + 1j*rng.normal(size=(5, 5)); X = (H + H.conj().T)/2
for p_opp, lab in [(-1j*1.7/np.pi, 'p=-iY/pi (Y=1.7)'), (0.5, 'p=1/2 (strict window)')]:
    CA = 3.0
    V1 = 1j*X; V2 = 0.5*(1j)**2*(X@X + p_opp*CA/2*X)
    O2 = V2 + V2.conj().T + V1.conj().T@V1                 # coefficient of chi^2 in V^dag V
    print(f"    {lab}: max |O(chi^2) coefficient| = {np.abs(O2).max():.2e}")
