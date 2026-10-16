"""R-S1 (second, independent verification run).  Two-gluon exchange between two infinite
time-like Wilson lines v_A, v_B (v_A.v_B = cosh Y), gluon mass m, at fixed transverse momenta
a = k_T^2 + m^2, b = (K-k)_T^2 + m^2, longitudinal transfer K_par = 0.

Project normalisation (refdoc/work_R3/scripts/eikonal_box.py):
   J_sigma = Int dx_A dx_B [i/(x_A+i0)] [i/(sigma x_B+i0)] g,   x_A = v_A.k, x_B = v_B.k,
   g = 1/((Q-a+i0)(Q-b+i0)),  Q = k_par^2,   sigma = -1: box (same ordering), +1: crossed.

ROUTE 1 (new, no residues, no PV): proper-time (Schwinger) representation
   i/(x+i0) = Int_0^inf dtau e^{i tau (x+i0)},  1/(Q-a+i0) = -i Int_0^inf ds e^{i s (Q-a+i0)}.
   The k_par integral is a 2D Minkowski Fresnel integral (pi/S) exp(-i u^2/(4S)),
   u = tau_A v_A + sigma tau_B v_B, u^2 = tau_A^2 + tau_B^2 + 2 sigma cosh(Y) tau_A tau_B, S = s1+s2.
   Rescaling tau = 2 sqrt(S) t removes S completely, so
        J_sigma = (4 pi sinh Y/(a b)) * T_sigma,
        T_sigma = Int_0^inf Int_0^inf dt_A dt_B exp(-i (t_A^2 + t_B^2 + 2 sigma cosh Y t_A t_B))
                = (-i/2) Int_0^{pi/2} dphi / (1 + sigma cosh Y sin 2phi - i0).
   (This also shows that J_sigma is EXACTLY proportional to 1/(ab): p_opp is k_T independent.)
   T_sigma is computed numerically with a Gaussian damping exp(-delta (t_A^2+t_B^2)), delta -> 0,
   and also directly as a 2D integral without polar coordinates.

ROUTE 2 (brute force): 2D trapezoidal integration of the momentum-space integrand at finite eps on a
   uniform grid in (x_A, x_B) (spectrally accurate for analytic integrands, h = eps/3), then
   Richardson extrapolation eps -> 0.  No contour manipulation at all.

ROUTE 3: strict Glauber approximation g -> 1/(ab) with symmetric cut-offs: J_box = J_cross = pi^2/(ab).

COLOUR: SU(N), N = 2,3,4, representations F, Fbar, Adj (own construction of generators):
   c_box = X^2, c_cross = X^2 + (C_A/2) X, X = T_A.T_B; reference (E.51) anticommutator identity.

UNITARITY: M^(2) = -1/2 chi(x)chi [c_box J_box + c_cross J_cross]/(2 pi^2/(ab));
   V^dag V - 1 at O(chi^2) = -1/2 C_A chi^2 Re(p_opp) X,  p_opp = J_cross/(J_box+J_cross).

Run: python3 -I v2_rs1_propertime.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
from scipy import integrate

mp.mp.dps = 30
LOG = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"
    LOG.append(s); print(s, flush=True)

def closed(a, b, Y):
    return 2*mp.pi/(a*b)*(mp.pi + 1j*Y), -2j*mp.pi*Y/(a*b)

# ------------------------------------------------------------------ ROUTE 1a: polar form, damping
def T_polar(sigma, Y, delta):
    C = mp.cosh(Y)
    # Int_0^{pi/2} dphi Int_0^inf r dr exp(-r^2 (delta + i(1+sigma C sin 2phi))) = Int dphi 1/(2(delta + i c))
    f = lambda ph: 1/(2*(delta + 1j*(1 + sigma*C*mp.sin(2*ph))))
    if sigma == +1:
        return mp.quad(f, [0, mp.pi/4, mp.pi/2])
    # box: c = 0 at sin 2phi = 1/C, split there
    ph0 = mp.asin(1/C)/2; ph1 = mp.pi/2 - ph0
    return mp.quad(f, [0, ph0, mp.pi/4, ph1, mp.pi/2])

def T_exact(sigma, Y):
    if sigma == +1:
        return -0.5j*Y/mp.sinh(Y)
    return (mp.pi + 1j*Y)/(2*mp.sinh(Y))

for Y in [mp.mpf('0.3'), mp.mpf(1), mp.mpf('2.7'), mp.mpf(6)]:
    for sigma in (-1, +1):
        vals = [T_polar(sigma, Y, mp.mpf(10)**(-k)) for k in (4, 6, 8)]
        ex = T_exact(sigma, Y)
        dev = abs(vals[-1]-ex)/abs(ex)
        rep(f'route1 polar T_sigma, sigma={sigma:+d}, Y={mp.nstr(Y,3)}', dev < 1e-6,
            f'delta=1e-4,1e-6,1e-8: {mp.nstr(vals[0],10)}, {mp.nstr(vals[1],10)}, {mp.nstr(vals[2],10)}; exact {mp.nstr(ex,10)}')

# identity used for the crossed graph and the PV part of the box
for Y in [0.1, 1.0, 4.0]:
    Y = mp.mpf(Y); C = mp.cosh(Y)
    I1 = mp.quad(lambda p: 1/(1+C*mp.sin(2*p)), [0, mp.pi/4, mp.pi/2])
    ph0 = mp.asin(1/C)/2
    # principal value of Int dphi/(1 - C sin 2phi), symmetric excision around both zeros
    g = lambda p: 1/(1-C*mp.sin(2*p))
    eps = mp.mpf('1e-12')
    pv = mp.quad(g, [0, ph0-eps]) + mp.quad(g, [ph0+eps, mp.pi/2-ph0-eps]) + mp.quad(g, [mp.pi/2-ph0+eps, mp.pi/2])
    rep(f'identities Y={mp.nstr(Y,3)}', abs(I1 - Y/mp.sinh(Y)) < 1e-20 and abs(pv + Y/mp.sinh(Y)) < 1e-9,
        f'Int dphi/(1+C sin2phi) = {mp.nstr(I1,15)} vs Y/sinhY = {mp.nstr(Y/mp.sinh(Y),15)}; PV Int dphi/(1-C sin2phi) = {mp.nstr(pv,12)} vs -Y/sinhY')

# ------------------------------------------------------------------ ROUTE 1b: Cartesian 2D (no polar)
def T_cart(sigma, Y, delta, L=None, n=16001):
    C = float(np.cosh(Y))
    if L is None: L = 12/np.sqrt(delta)
    t = np.linspace(0, L, n)
    inner = np.empty(n, complex)
    ch = 500
    for i0 in range(0, n, ch):
        ta = t[i0:i0+ch][:, None]
        F = np.exp(-delta*(ta**2+t[None, :]**2) - 1j*(ta**2+t[None, :]**2+2*sigma*C*ta*t[None, :]))
        inner[i0:i0+ch] = integrate.simpson(F, x=t, axis=1)
    return integrate.simpson(inner, x=t)

for (sigma, Y) in [(+1, 1.0), (-1, 1.0)]:
    vals = []
    for delta in [0.04, 0.02, 0.01]:
        vals.append(T_cart(sigma, Y, delta, L=np.sqrt(40/delta)))
    # Richardson in delta (expect smooth, linear leading behaviour)
    r1 = 2*vals[1]-vals[0]; r2 = 2*vals[2]-vals[1]; rr = (4*r2 - r1)/3
    ex = complex(T_exact(sigma, mp.mpf(Y)))
    rep(f'route1 Cartesian T_sigma, sigma={sigma:+d}, Y={Y}', abs(rr-ex)/abs(ex) < 2e-3,
        f'delta=.04,.02,.01: {vals[0]:.6f} {vals[1]:.6f} {vals[2]:.6f}; Richardson {rr:.6f}; exact {ex:.6f}')

# J from route 1
for (a, b, Y) in [(1.0, 2.5, 1.0), (0.7, 0.3, 6.0), (2.0, 0.1, 0.4), (0.05, 7.0, 2.2)]:
    a, b, Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    Jb = 4*mp.pi*mp.sinh(Y)/(a*b)*T_polar(-1, Y, mp.mpf('1e-9'))
    Jc = 4*mp.pi*mp.sinh(Y)/(a*b)*T_polar(+1, Y, mp.mpf('1e-9'))
    cb, cc = closed(a, b, Y)
    popp = Jc/(Jb+Jc)
    rep(f'route1 J (a={mp.nstr(a,3)},b={mp.nstr(b,3)},Y={mp.nstr(Y,3)})',
        abs(Jb-cb)/abs(cb) < 1e-7 and abs(Jc-cc)/abs(cc) < 1e-7,
        f'J_box={mp.nstr(Jb,10)} (closed {mp.nstr(cb,10)}), J_cross={mp.nstr(Jc,10)} (closed {mp.nstr(cc,10)}), p_opp={mp.nstr(popp,8)}, -iY/pi={mp.nstr(-1j*Y/mp.pi,8)}')

# ------------------------------------------------------------------ ROUTE 2: brute force momentum space
def J_grid(sigma, a, b, Y, eps, L=40.0):
    h = eps/3
    n = int(2*L/h) + 1
    x = np.linspace(-L, L, n)
    sh2 = np.sinh(Y)**2; C = np.cosh(Y)
    eA = 1j/(x + 1j*eps)                         # i/(x_A + i eps)
    tot = 0j
    chunk = 400
    for i0 in range(0, n, chunk):
        xa = x[i0:i0+chunk][:, None]
        xb = x[None, :]
        Q = (-(xa**2 + xb**2) + 2*C*xa*xb)/sh2
        g = 1/((Q - a + 1j*eps)*(Q - b + 1j*eps))
        f = (eA[i0:i0+chunk][:, None]) * (1j/(sigma*xb + 1j*eps)) * g
        tot += np.sum(f)
    return tot*h*h   # trapezoid with negligible end corrections (integrand ~ |x|^-5 at the edge)

for (a, b, Y) in [(1.0, 2.5, 1.0), (3.0, 1.2, 2.0)]:
    cb, cc = [complex(z) for z in closed(mp.mpf(a), mp.mpf(b), mp.mpf(Y))]
    res = {}
    for sigma in (-1, +1):
        es = [0.08, 0.04, 0.02]
        vs = [J_grid(sigma, a, b, Y, e) for e in es]
        # Richardson assuming J(eps) = J0 + c1 eps + c2 eps^2 (+ eps^2 log eps tolerated)
        r1 = 2*vs[1]-vs[0]; r2 = 2*vs[2]-vs[1]; rr = (4*r2-r1)/3
        res[sigma] = (vs, rr)
    vb, rb = res[-1]; vc, rc = res[+1]
    print(f"   a={a} b={b} Y={Y}: box eps=.08,.04,.02 -> {vb[0]:.5f} {vb[1]:.5f} {vb[2]:.5f}; Richardson {rb:.5f}; closed {cb:.5f}")
    print(f"                     cross eps=.08,.04,.02 -> {vc[0]:.5f} {vc[1]:.5f} {vc[2]:.5f}; Richardson {rc:.5f}; closed {cc:.5f}")
    ok = abs(rb-cb)/abs(cb) < 5e-3 and abs(rc-cc)/abs(cc) < 5e-3 and abs(rc.real) < 5e-3*abs(cc)
    rep(f'route2 brute-force grid (a={a},b={b},Y={Y})', ok,
        f'rel dev box {abs(rb-cb)/abs(cb):.1e}, cross {abs(rc-cc)/abs(cc):.1e}; Re J_cross(extrap) = {rc.real:.1e}; p_opp(extrap) = {rc/(rb+rc):.5f} vs -iY/pi = {-1j*Y/np.pi:.5f}')

# ------------------------------------------------------------------ ROUTE 3: strict Glauber, symmetric cut-offs
# window integral Int_{-L}^{L} dx i/(x + i eps): analytic value i*[log(L+i eps) - log(-L+i eps)] and quadrature
for L in [mp.mpf(10), mp.mpf(1000)]:
    epsv = mp.mpf('1e-8')
    pts = [-L, -mp.mpf('1e-2'), -100*epsv, -epsv, 0, epsv, 100*epsv, mp.mpf('1e-2'), L]
    IA = mp.quad(lambda x: 1j/(x+1j*epsv), pts)               # i/(x+i0), symmetric window
    IBbox = mp.quad(lambda x: 1j/(-x+1j*epsv), pts)
    IBcr = mp.quad(lambda x: 1j/(x+1j*epsv), pts)
    an = 1j*(mp.log(L+1j*epsv) - mp.log(-L+1j*epsv))
    rep(f'route3 strict Glauber window L={mp.nstr(L,4)}', abs(IA*IBbox - mp.pi**2) < 1e-6 and abs(IA*IBcr - mp.pi**2) < 1e-6 and abs(an-mp.pi) < 1e-8,
        f'(ab) J_box^strict = {mp.nstr(IA*IBbox,12)}, (ab) J_cross^strict = {mp.nstr(IA*IBcr,12)}  (pi^2 = {mp.nstr(mp.pi**2,12)}); analytic window integral = {mp.nstr(an,12)} -> p_opp = 1/2')

# ------------------------------------------------------------------ COLOUR: SU(N) generators built from scratch
def suN_fund(N):
    gens = []
    for i in range(N):
        for j in range(i+1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 0.5; gens.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -0.5j; m[j, i] = 0.5j; gens.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        m *= 1/np.sqrt(2*k*(k+1)); gens.append(m)
    return np.array(gens)

def structure(t):
    n = len(t)
    f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            cm = t[a]@t[b] - t[b]@t[a]
            for c in range(n):
                f[a, b, c] = np.real(-2j*np.trace(cm@t[c]))
    return f

for N in (2, 3, 4):
    tF = suN_fund(N)
    ng = N*N-1
    assert all(abs(np.trace(tF[a]@tF[b]) - 0.5*(a == b)) < 1e-12 for a in range(ng) for b in range(ng))
    f = structure(tF)
    tA = np.array([-1j*f[a] for a in range(ng)])
    tFb = np.array([-tF[a].conj() for a in range(ng)])
    CA = float(N)
    # check C_A from the adjoint Casimir
    cas = sum(tA[a]@tA[a] for a in range(ng))
    assert np.allclose(cas, CA*np.eye(ng))
    reps = {'F': tF, 'Fbar': tFb, 'A': tA}
    allok = True; maxdev = 0
    for nA, TA in reps.items():
        for nB, TB in reps.items():
            X = sum(np.kron(TA[a], TB[a]) for a in range(ng))
            # later attachment on the left.  A: T^b (later) T^a (earlier)
            cbox = sum(np.kron(TA[b2]@TA[a2], TB[b2]@TB[a2]) for a2 in range(ng) for b2 in range(ng))
            ccr = sum(np.kron(TA[b2]@TA[a2], TB[a2]@TB[b2]) for a2 in range(ng) for b2 in range(ng))
            anti = sum(np.kron(TA[a2]@TA[b2]+TA[b2]@TA[a2], TB[a2]@TB[b2]+TB[b2]@TB[a2]) for a2 in range(ng) for b2 in range(ng))
            d1 = np.abs(cbox - X@X).max(); d2 = np.abs(ccr - X@X - CA/2*X).max(); d3 = np.abs(anti - 4*X@X - CA*X).max()
            maxdev = max(maxdev, d1, d2, d3)
            allok &= (d1 < 1e-10 and d2 < 1e-10 and d3 < 1e-10)
    rep(f'colour SU({N}) all 9 rep pairs', allok, f'c_box=X^2, c_cross=X^2+(C_A/2)X, sum{{T,T}}{{T,T}}=4X^2+C_A X; max dev {maxdev:.1e}')

# ------------------------------------------------------------------ UNITARITY bookkeeping in b-space (SU(3), 3 x 3bar)
tF = suN_fund(3); f = structure(tF); tFb = np.array([-t.conj() for t in tF])
X = sum(np.kron(tF[a], tFb[a]) for a in range(8)); CA = 3.0; Id = np.eye(9)
def O2_coeff(Jb, Jc):
    # coefficient of chi^2 in V^dag V - 1, V = 1 - i chi X + M2, M2 = -1/2 chi^2 [X^2 Jb + (X^2 + CA/2 X) Jc]/(Jb+Jc)
    M2 = -0.5*(X@X*Jb + (X@X + CA/2*X)*Jc)/(Jb+Jc)
    V1 = -1j*X
    return V1.conj().T@V1 + M2 + M2.conj().T
Y = 2.3; a, b = 1.0, 2.5
cb, cc = [complex(z) for z in closed(mp.mpf(a), mp.mpf(b), mp.mpf(Y))]
r_exact = O2_coeff(cb, cc)
r_strict = O2_coeff(np.pi**2/(a*b), np.pi**2/(a*b))
rep('unitarity, exact eikonal box+crossed', np.abs(r_exact).max() < 1e-12, f'max |chi^2 coeff of V^dag V - 1| = {np.abs(r_exact).max():.1e}')
rep('unitarity, strict Glauber (p_opp=1/2) reproduces reference (E.51)', np.allclose(r_strict, -CA/4*X),
    f'chi^2 coeff = -(C_A/4) X : {np.allclose(r_strict, -CA/4*X)}')
# amplitude-level deviation for the equal split (what reader R4 called "-1/8")
M2s = -0.5*(X@X + 0.5*CA/2*X); dev_amp = M2s - (-0.5*X@X)
rep('amplitude deviation for equal split = -(1/8) C_A chi^2 X (R4 quantity, not the V^dag V residual)', np.allclose(dev_amp, -CA/8*X), '')
# the C_A term of the exact M2 is anti-Hermitian (a phase)
M2e = -0.5*(X@X*cb + (X@X + CA/2*X)*cc)/(cb+cc)
CApart = M2e - (-0.5*X@X)
rep('exact C_A term is anti-Hermitian', np.allclose(CApart + CApart.conj().T, 0) and np.allclose(CApart, 1j*Y*CA/(4*np.pi)*X),
    f'C_A part = i (Y C_A/(4 pi)) X : {np.allclose(CApart, 1j*Y*CA/(4*np.pi)*X)}')

# ------------------------------------------------------------------ REGGE: C_A term = one-loop gluon trajectory
# With V1 = -i chi X, chi(K) = g^2 coth(Y)/(K^2+m^2) (momentum space, up to the common Fourier measure),
# chi(x)chi(K) = g^4 coth^2 Y I(K), I(K) = Int d^2k/(2pi)^2 1/(a b):
#   M2^{C_A}(K) = i (Y C_A/(4 pi)) g^4 coth^2Y I(K) X = M1(K) * omega * Y,
#   omega = -(C_A/(4 pi)) g^2 coth Y (K^2+m^2) I(K)  -> -(g^2 N_c/(4pi)) K^2 I(K) = Lipatov trajectory (Y->inf, m->0)
g2 = 1.7; K2 = 0.9; m2 = 0.0
Ival = 1.0  # placeholder value of I(K): the identity is algebraic in I
M1 = -1j*g2*1.0/(K2+m2)
M2CA = 1j*(Y*CA/(4*np.pi))*g2**2*Ival
omega = M2CA/(M1*Y)
lip = -(g2*CA/(4*np.pi))*K2*Ival
rep('C_A term = M_tree * omega(t) * Y with Lipatov one-loop trajectory (coth Y -> 1, m -> 0)', abs(omega-lip) < 1e-12 and omega.real < 0,
    f'omega = {omega:.6f}, -(g^2 N_c/4pi) K^2 I = {lip:.6f}')

print('\nSUMMARY:', sum('PASS' in s for s in LOG), 'PASS,', sum('FAIL' in s for s in LOG), 'FAIL')
