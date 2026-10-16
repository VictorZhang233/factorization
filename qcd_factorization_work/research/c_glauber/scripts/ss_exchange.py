"""
ss_exchange.py  --  Part (1) of research/c_glauber: the spectator-spectator (S-S) Glauber exchange in
Drell-Yan at one-gluon level, derived by exact residues; exponentiation in impact-parameter space;
cancellation after the integral over the spectators' relative transverse momentum; what changes for a
non-abelian exchange (colour-matrix phase, non-commutation with other colour operators); and the
active-spectator (A-S) case where the contour is NOT trapped and can be deformed (DY: initial-state).

Conventions (CONTEXT.md): metric (+,-,-,-); v^pm=(v^0 pm v^3)/sqrt2; v.w=v^+w^- + v^-w^+ - vT.wT.
Scalar-QED-like couplings for the spectators: covariant derivative D=d - i e A  =>  vertex  +i e (p+p')^mu
(p, p' along the charge flow), scalar propagator i/(p^2-m^2+i0), gluon propagator -i g_{mu nu}/(k^2-mg^2+i0).
Hadron A moves along +z, hadron B along -z.

Routing (same as glauber_poles.py): the exchanged momentum k flows from the B-spectator into the A-spectator.
  A side: internal spectator  p_A' - k   (final spectator momentum p_A'),   active a:  l_a + k
  B side: internal spectator  p_B' + k   (final spectator momentum p_B'),   active b:  l_b - k
Glauber scaling: k^pm ~ lam^2 Q, kT ~ lam Q.

Checks
 SS1  exact residue derivation (sympy):  M1 = int d^2kT/(2pi)^2  V(kT) M0(p_A'-kT, p_B'+kT),
      V(kT) = -i e_A e_B /(kT^2+mg^2)   [purely imaginary, even in kT]
 SS2  numerical finite-eps check of the k^- and k^+ integrals.
 SS3  b-space: Vtilde(b) = i chi(b), chi(b) = -(e_A e_B/2pi) K0(mg b); abelian exponentiation exp(i chi);
      int d^2Delta |M|^2 = int d^2Delta |M0|^2 (cancellation) while |M(Delta)|^2 != |M0(Delta)|^2 pointwise;
      the cancellation holds at FIXED q_T = -(p_A'T+p_B'T) (TMD Drell-Yan), because the exchange only shifts
      the relative momentum Delta=(p_B'T-p_A'T)/2.
 SS4  non-abelian: e_A e_B -> g^2 T_A.T_B (Hermitian colour matrix c); U = exp(i chi c) is unitary =>
      colour-traced, Delta-integrated cancellation persists; [c, T_A.T_j] != 0 for a third coloured line j
      (the Glauber phase does not commute with other soft colour exchanges: origin of FSS / SLL effects).
 SS5  active (B) - spectator (A) exchange in DY: k^+ has only the initial-state pole of the active line b
      (UHP) near the Glauber region; deforming k^+ into the LHP reproduces the real-axis value and on the
      deformed contour the eikonal (past-pointing Wilson-line) approximation is accurate.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate, special
from scipy.linalg import expm

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

# ------------------------------------------------------------------------------------------------
print('=== SS1: exact residue derivation of the S-S Glauber kernel ===')
km, kp = sp.symbols('k_m k_p')                     # k^-, k^+ (integration variables)
pA, pB, LA, LB = sp.symbols('p_A p_B L_A L_B', positive=True)   # p_A'^+, p_B'^-, l_a^+, l_b^-
cA, cB, dA, dB = sp.symbols('c_A c_B d_A d_B', real=True)
eps = sp.symbols('epsilon', positive=True)
eA, eB, kT2, mg2 = sp.symbols('e_A e_B kT2 mg2', real=True)
# Glauber-region denominators (exact up to terms of relative order lam^2):
DsA = -2*pA*(km - cA) + sp.I*eps      # (p_A'-k)^2 - m_s^2 + i0 ; pole in UHP
Da = 2*LA*(km - dA) + sp.I*eps        # (l_a+k)^2 - m_a^2 + i0  ; pole in LHP
DsB = 2*pB*(kp - cB) + sp.I*eps       # (p_B'+k)^2 - m_s^2 + i0 ; pole in LHP
Db = -2*LB*(kp - dB) + sp.I*eps       # (l_b-k)^2 - m_b^2 + i0  ; pole in UHP
pole_sA = sp.solve(sp.Eq(DsA, 0), km)[0]
pole_a = sp.solve(sp.Eq(Da, 0), km)[0]
pole_sB = sp.solve(sp.Eq(DsB, 0), kp)[0]
pole_b = sp.solve(sp.Eq(Db, 0), kp)[0]
ok_half = (sp.im(pole_sA) > 0) == True and (sp.im(pole_a) < 0) == True and (sp.im(pole_sB) < 0) == True and (sp.im(pole_b) > 0) == True
check('SS1a pole half-planes: A-spectator UHP, a LHP (k^- trapped); B-spectator LHP, b UHP (k^+ trapped)', ok_half,
      'k^- poles %s | %s ; k^+ poles %s | %s' % (sp.simplify(pole_sA), sp.simplify(pole_a), sp.simplify(pole_sB), sp.simplify(pole_b)))
# A-side k^- integral with vertex (numerator 2p_A'^+ e_A, leading component) and the two propagators:
fA = (sp.I*eA*2*pA)*(sp.I/DsA)*(sp.I/Da)
# integrand ~ 1/km^2 : close in the UHP (counter-clockwise): picks the spectator pole only
Jm = sp.I*sp.residue(fA, km, pole_sA)            # = 2 pi i Res /(2 pi)
treeA = (sp.I/Da).subs(km, cA)                   # tree A-side factor with spectator momentum p_A'-k on shell
ratioA = sp.simplify(sp.limit(Jm/treeA, eps, 0))
fB = (sp.I*eB*2*pB)*(sp.I/DsB)*(sp.I/Db)
Jp = -sp.I*sp.residue(fB, kp, pole_sB)           # close in the LHP (clockwise): picks the B-spectator pole
treeB = (sp.I/Db).subs(kp, cB)
ratioB = sp.simplify(sp.limit(Jp/treeB, eps, 0))
# gluon propagator in the Glauber region: -i/(k^2-mg^2) with k^2 ~ -kT^2
gl = -sp.I/(-(kT2 + mg2))
V = sp.simplify(ratioA*ratioB*gl)
check('SS1b k^- residue: int dk^-/2pi [i e_A 2p^+][i/D_sA][i/D_a] = (i e_A) x [tree A-factor at on-shell spectator p_A\'-k]',
      sp.simplify(ratioA - sp.I*eA) == 0, 'ratio = %s' % ratioA)
check('SS1c k^+ residue: int dk^+/2pi [i e_B 2p^-][i/D_sB][i/D_b] = (i e_B) x [tree B-factor at on-shell spectator p_B\'+k]',
      sp.simplify(ratioB - sp.I*eB) == 0, 'ratio = %s' % ratioB)
check('SS1d S-S kernel V(kT) = -i e_A e_B/(kT^2+mg^2): M1 = int d^2kT/(2pi)^2 V(kT) M0(p_A\'-kT, p_B\'+kT)',
      sp.simplify(V - (-sp.I*eA*eB/(kT2 + mg2))) == 0, 'V = %s' % V)
# cross-check: closing the k^- contour in the LHP (active pole) gives the same value
Jm_alt = -sp.I*sp.residue(fA, km, pole_a)
check('SS1e closing k^- in the LHP (active-line pole) gives the same value (integrand ~ 1/k^2)',
      sp.simplify(sp.limit((Jm_alt - Jm), eps, 0)) == 0)

# ------------------------------------------------------------------------------------------------
print('\n=== SS2: numerical finite-eps check of the k^- integral ===')
vals = dict(pA=3.0, LA=1.7, cA=0.21, dA=-0.13, eA=0.8)
e_ = 1e-3
f_num = lambda t: (1j*vals['eA']*2*vals['pA'])*(1j/(-2*vals['pA']*(t - vals['cA']) + 1j*e_))*(1j/(2*vals['LA']*(t - vals['dA']) + 1j*e_))
pts = sorted([vals['cA'], vals['dA']])
edges = [-4e3] + [p + s*10.0**(-j) for p in pts for s in (-1, 1) for j in range(1, 6)] + pts + [4e3]
edges = sorted(set(edges))
num = 0j
for a_, b_ in zip(edges[:-1], edges[1:]):
    num += integrate.quad(lambda t: f_num(t).real, a_, b_, limit=500)[0] + 1j*integrate.quad(lambda t: f_num(t).imag, a_, b_, limit=500)[0]
num /= 2*np.pi
exact = 1j*vals['eA']*(1j/(2*vals['LA']*(vals['cA'] - vals['dA']) + 1j*e_*(1 + vals['LA']/vals['pA'])))
check('SS2 numerical k^- integral (eps=1e-3) = (i e_A) x i/D_a(on-shell spectator)', abs(num - exact) < 1e-3*abs(exact),
      'num=%.6f%+.6fi exact=%.6f%+.6fi' % (num.real, num.imag, exact.real, exact.imag))

# ------------------------------------------------------------------------------------------------
print('\n=== SS3: impact-parameter space, exponentiation, cancellation after the Delta integral ===')
import mpmath as mp
mp.mp.dps = 20
mgv, gAB = 0.6, 1.3          # gluon mass, e_A e_B
for bb in [0.3, 1.0, 2.5]:
    # Vtilde(b) = int d^2k/(2pi)^2 e^{-ik.b} V(k) = -i e_A e_B K0(mg b)/(2pi)
    val = mp.quadosc(lambda k: k*mp.besselj(0, k*bb)/(k**2 + mgv**2), [0, mp.inf], zeros=lambda n: mp.besseljzero(0, n)/bb)/(2*mp.pi)
    chi_num = -gAB*val
    chi_ex = -gAB*mp.besselk(0, mgv*bb)/(2*mp.pi)
    check('SS3a chi(b) = -(e_A e_B/2 pi) K0(mg b) at b=%.1f' % bb, abs(chi_num - chi_ex) < 1e-12, 'chi=%s' % mp.nstr(chi_ex, 10))
# small-mg behaviour: chi(b) -> (e_A e_B/2pi) [ln(mg b/2) + gamma_E] : IR-divergent constant + ln b
bb = 1.7
for m_ in [1e-3, 1e-5]:
    lhs = -gAB*special.k0(m_*bb)/(2*np.pi)
    rhs = gAB/(2*np.pi)*(np.log(m_*bb/2) + np.euler_gamma)
    check('SS3b mg->0: chi(b) = (e_A e_B/2pi)[ln(mg b/2)+gamma_E] + O(mg^2 b^2) (IR-divergent Coulomb phase), mg=%g' % m_,
          abs(lhs - rhs) < 1e-4*abs(rhs))
# exponentiation of n exchanges: (1/n!) n-fold convolution of V  <->  (i chi)^n / n!  in b space.
# Grid test in 2D: compare the n=2 convolution term computed in momentum space with FT of (i chi)^2/2 * M0tilde.
N = 128; L = 24.0
xs = (np.arange(N) - N//2)*(L/N)
X, Y = np.meshgrid(xs, xs, indexing='ij')
B = np.sqrt(X**2 + Y**2); B[B == 0] = 0.5*L/N
chi = -gAB*special.k0(mgv*B)/(2*np.pi)
M0t = np.exp(-0.5*((X - 0.4)**2 + 0.7*(Y + 0.2)**2))*(1 + 0.3j*X)       # M0tilde(b): smooth, complex, asymmetric
def to_mom(f):   # M(Delta) = int d^2b e^{-i Delta.b} f(b)  (discrete)
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(f)))*(L/N)**2
M0 = to_mom(M0t); Mfull = to_mom(np.exp(1j*chi)*M0t); M1 = to_mom(1j*chi*M0t)
dk = 2*np.pi/L
I0 = np.sum(np.abs(M0)**2)*dk**2; Ifull = np.sum(np.abs(Mfull)**2)*dk**2
check('SS3c all-orders abelian phase: int d^2Delta |M|^2 = int d^2Delta |M0|^2 (Parseval, |e^{i chi}|=1)',
      abs(Ifull - I0) < 1e-10*I0, 'rel diff %.1e' % (abs(Ifull - I0)/I0))
pw = np.max(np.abs(np.abs(Mfull)**2 - np.abs(M0)**2))/np.max(np.abs(M0)**2)
check('SS3d but |M(Delta)|^2 != |M0(Delta)|^2 point by point (redistribution in Delta)', pw > 1e-2, 'max rel change %.3f' % pw)
I1 = np.sum(2*np.real(M1*np.conj(M0)))*dk**2
check('SS3e one-exchange cut graphs: int d^2Delta 2Re[M1 M0^*] = 0 (the two cuts cancel only after the Delta integral)',
      abs(I1) < 1e-10*I0, '|int| = %.1e' % abs(I1))

# ------------------------------------------------------------------------------------------------
print('\n=== SS4: non-abelian S-S exchange: colour-matrix phase ===')
def gellmann(N):
    Ts = []
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), complex); M[i, j] = M[j, i] = 0.5; Ts.append(M)
            M = np.zeros((N, N), complex); M[i, j] = -0.5j; M[j, i] = 0.5j; Ts.append(M)
    for k in range(1, N):
        M = np.zeros((N, N), complex)
        for i in range(k):
            M[i, i] = 1.0
        M[k, k] = -k
        M *= 1.0/np.sqrt(2*k*(k + 1)); Ts.append(M)
    return Ts
T = gellmann(3); Tbar = [-t.T for t in T]; I3 = np.eye(3)
# three coloured objects: spectator A (3bar), spectator B (3bar), outgoing coloured parton j (3)
def op(a, b, c): return np.kron(np.kron(a, b), c)
cAB = sum(op(Tbar[a], Tbar[a], I3) for a in range(8))        # T_A.T_B
cAj = sum(op(Tbar[a], I3, T[a]) for a in range(8))           # T_A.T_j
check('SS4a T_A.T_B is Hermitian (so U = exp(i chi T_A.T_B) is unitary)', np.allclose(cAB, cAB.conj().T))
rng = np.random.default_rng(5)
psi = rng.normal(size=27) + 1j*rng.normal(size=27); psi /= np.linalg.norm(psi)
rho = np.outer(psi, psi.conj())
okU = True
for chv in [0.3, -1.1, 2.4]:
    U = expm(1j*chv*cAB)
    okU &= np.allclose(U.conj().T @ U, np.eye(27)) and abs(np.trace(U @ rho @ U.conj().T) - 1) < 1e-12
check('SS4b colour-traced probability Tr[U rho U^+] = Tr rho for every chi(b): the S-S cancellation survives (Delta-integrated, colour-summed)', okU)
comm = np.linalg.norm(cAB @ cAj - cAj @ cAB)
check('SS4c [T_A.T_B, T_A.T_j] != 0: the Glauber phase does not commute with soft exchanges involving a third coloured line',
      comm > 1e-6, '||[.,.]|| = %.3f' % comm)
# two-gluon order: U = 1 + i chi c - chi^2 c^2/2 + ... ; the cut sum at O(chi^2) cancels for any Hermitian c:
# (i c)(i c)^+ + [(-c^2/2) + h.c.] = 0
okcut = np.allclose((1j*cAB) @ (1j*cAB).conj().T + (-0.5*cAB @ cAB) + (-0.5*cAB @ cAB).conj().T, 0)
check('SS4d O(chi^2) cut identity for a Hermitian colour matrix: |i c|^2 + 2Re(-c^2/2) = 0', okcut)
# but a projector on a colour configuration that does not commute with c is not preserved (diffraction-like selection)
Pj = np.zeros((27, 27), complex)
s = np.zeros((3, 3, 3), complex)
for i in range(3):          # A-remnant (3bar) and parton j (3) in a colour singlet, B arbitrary
    for k in range(3):
        v = np.zeros((3, 3, 3), complex)
        v[i, k, i] = 1/np.sqrt(3)
        Pj += np.outer(v.reshape(-1), v.reshape(-1).conj())
U = expm(1j*0.9*cAB)
p0 = np.real(np.trace(Pj @ rho)); p1 = np.real(np.trace(Pj @ U @ rho @ U.conj().T))
check('SS4e a colour projection not commuting with T_A.T_B is changed by the Glauber phase (%.4f -> %.4f)' % (p0, p1),
      abs(p1 - p0) > 1e-3)

# ------------------------------------------------------------------------------------------------
print('\n=== SS5: active(B)-spectator(A) exchange in DY: k^+ not trapped, eikonal approximation on the deformed contour ===')
Q = 100.0; lam = 0.05; m = lam*Q
lbm = 0.45*Q                     # l_b^- of the incoming active parton b
cb = 0.7*m**2; epsb = 1e-3*m**2
K2 = (0.8*m)**2 + (0.5*m)**2; epsg = 1e-3*m**2
W = 3*lam*Q; Lmax = 2e4*Q
def seg_int(f, z0, z1):
    fr = lambda t: (f(z0 + (z1 - z0)*t)*(z1 - z0)).real
    fi = lambda t: (f(z0 + (z1 - z0)*t)*(z1 - z0)).imag
    return integrate.quad(fr, 0, 1, limit=2000)[0] + 1j*integrate.quad(fi, 0, 1, limit=2000)[0]
def real_line(f, a, b, centres, widths):
    pts = [a, b]
    for c_, w_ in zip(centres, widths):
        for kk in range(0, 16):
            for d_ in ([0.0] if kk == 0 else []) + [-w_*10.0**kk, w_*10.0**kk]:
                if a < c_ + d_ < b:
                    pts.append(c_ + d_)
    pts = sorted(set(pts)); tot = 0j
    for x0, x1 in zip(pts[:-1], pts[1:]):
        tot += integrate.quad(lambda t: f(t).real, x0, x1, limit=2000)[0] + 1j*integrate.quad(lambda t: f(t).imag, x0, x1, limit=2000)[0]
    return tot
for kmv in [+0.4*m**2/Q, -0.4*m**2/Q]:
    fb = lambda z, eik=False: 1.0/(-2*lbm*z + (0.0 if eik else cb) + 1j*epsb)      # (l_b-k)^2-m^2+i0 : pole UHP
    fg = lambda z: 1.0/(2*z*kmv - K2 + 1j*epsg)                                   # gluon: pole at |k^+| ~ Q
    f = lambda z: fb(z)*fg(z); feik = lambda z: fb(z, True)*fg(z)
    zb = (cb + 1j*epsb)/(2*lbm); zg = (K2 - 1j*epsg)/(2*kmv)
    I_real = real_line(f, -Lmax, Lmax, [zb.real, zg.real], [abs(zb.imag), abs(zg.imag)])
    depth = -lam*Q
    def deformed(fun, poles):
        tot = real_line(fun, -Lmax, -W, [p.real for p in poles], [abs(p.imag) for p in poles]) + \
              real_line(fun, W, Lmax, [p.real for p in poles], [abs(p.imag) for p in poles])
        tot += seg_int(fun, -W + 0j, -W + 1j*depth) + seg_int(fun, -W + 1j*depth, W + 1j*depth) + seg_int(fun, W + 1j*depth, W + 0j)
        return tot
    I_def = deformed(f, [zb, zg]); I_eik = deformed(feik, [1j*epsb/(2*lbm), zg])
    resb = (1.0/(-2*lbm))*fg(zb)
    check('SS5a k^-=%+.3g: deforming k^+ into the LHP (away from the initial-state pole of b) reproduces the real-axis value' % kmv,
          abs(I_def - I_real) < 1e-4*2*np.pi*abs(resb), '|diff|/|2pi Res| = %.1e' % (abs(I_def - I_real)/(2*np.pi*abs(resb))))
    check('SS5b k^-=%+.3g: on the deformed contour the eikonal line 1/(-2 l_b^- k^+ + i0) (past-pointing W in f_A) is accurate' % kmv,
          abs(I_eik - I_def) <= lam*abs(I_def), 'rel err %.1e' % (abs(I_eik - I_def)/abs(I_def)))

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
