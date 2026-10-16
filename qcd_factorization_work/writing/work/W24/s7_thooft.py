#!/usr/bin/env python3
"""W24 / Ch21 -- prop:power-thooft-model: checks of the 't Hooft-model derivation in the book's conventions.

2D QCD, light-cone coordinates x^pm = (x^0 pm x^1)/sqrt2, light-cone gauge A^+ = 0 (A_- = 0), D = d - i g A^a t^a,
Tr(t^a t^b) = delta^{ab}/2.  Gluon "propagator" <A_+^a A_+^b> = i delta^{ab}/(k^+)^2 (principal value / cutoff lambda),
vertex i g gamma^+ t^a, planar limit N_c -> oo with g^2 N_c fixed.  m_0^2 = g^2 N_c/(2 pi).
 (1) cutoff integral  int_{|k|>lambda} dk sgn(p-k)/k^2 = 2/lambda - 2/p  (p>0)
 (2) int dk^- 1/(A - B k^- + i0) = -i pi/|B|   (symmetric integration)
 (3) self-energy -> mass shift  m^2 -> m^2 - g^2 N_c/(2 pi) (+ IR-cutoff term that cancels in singlets)
 (4) finite parts: fp int_0^1 dy/(y-x)^2 = -1/x - 1/(1-x);  fp int_0^oo y^beta/(y-x)^2 dy = -pi beta cot(pi beta) x^{beta-1}
 (5) 't Hooft operator H phi = (m1^2-m0^2)/x phi + (m2^2-m0^2)/(1-x) phi - m0^2 fp int dy phi(y)/(y-x)^2
       = m1^2/x phi + m2^2/(1-x) phi - m0^2 PV int dy (phi(y)-phi(x))/(y-x)^2  (equivalent form; positive quadratic form)
 (6) Rayleigh-Ritz spectrum: massless pion for m=0; Regge behaviour mu_n^2 ~ pi^2 m0^2 n.
 (7) endpoint exponent: pi beta cot(pi beta) = 1 - m^2/m0^2.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

# (1)
k, lam, p = sp.symbols('k lambda p', positive=True)
I1 = sp.integrate(1/k**2, (k, lam, p)) - sp.integrate(1/k**2, (k, p, sp.oo)) + sp.integrate(1/k**2, (k, lam, sp.oo))  # k<0 part: sgn=+1, int_{-oo}^{-lam} dk/k^2 = 1/lam
check("(1) int_{|k|>lambda} dk sgn(p-k)/k^2 = 2/lambda - 2/p", sp.simplify(I1 - (2/lam - 2/p)) == 0)

# (2) exactly: int_{-C}^{C} dk/(A - B k + i eta) = -(1/B)[log(A - B k + i eta)]_{-C}^{C} (principal log, eta>0)
mp.mp.dps = 25
A, B, eta = mp.mpf('0.7'), mp.mpf('1.9'), mp.mpf('1e-12')
for C in [mp.mpf(10), mp.mpf(10)**6]:
    val = -(mp.log(A - B*C + 1j*eta) - mp.log(A + B*C + 1j*eta))/B
    print(f"   C={C}: int = {mp.nstr(val, 12)}   (-i pi/|B| = {mp.nstr(-1j*mp.pi/abs(B), 12)}; real part -> 0 as C->oo)")
check("(2) int dk^-/(A - B k^- + i0) -> -i pi/|B| with symmetric cutoff", abs(val + 1j*mp.pi/abs(B)) < 1e-5)

# (3) symbolic: self-energy diagram value  Sigma = -i (N g^2/(4 pi)) gamma^+ (1/lambda - 1/p^+)  ->  p^- shift
g, N, pp, pm, m = sp.symbols('g N p_plus p_minus m', positive=True)
shift = (N*g**2/(4*sp.pi))*(1/lam - 1/pp)
den = sp.expand(2*pp*(pm - shift) - m**2)
print("   dressed denominator:", den)
check("(3) mass shift m^2 -> m^2 - g^2 N/(2 pi) (plus IR term -g^2 N p^+/(2 pi lambda))",
      sp.simplify(den - (2*pp*pm - (m**2 - g**2*N/(2*sp.pi)) - g**2*N*pp/(2*sp.pi*lam))) == 0)
# colour factor: t^a t^a = C_F -> N/2 at large N ; Sigma prefactor: (N/2) * (i g)^2 * i * 2i * (-i pi)/(2|q^+|) * 1/(2pi)^2 ...
pref = sp.Rational(1, 2)*N*(sp.I*g)**2*sp.I*(2*sp.I)*(-sp.I*sp.pi)/2/(2*sp.pi)**2   # times gamma^+ * int dk^+ sgn/(k^+)^2
check("(3') prefactor of gamma^+ int dk^+ sgn(p^+-k^+)/(k^+)^2 equals -i N g^2/(8 pi)", sp.simplify(pref - (-sp.I*N*g**2/(8*sp.pi))) == 0)

# (4) finite parts (Hadamard): fp int_0^1 dy/(y-x)^2 = -1/x - 1/(1-x)
def fp_int(f, x, a, b, delta):
    # fp int_a^b f(y)/(y-x)^2 dy = lim [ int_{|y-x|>delta} f/(y-x)^2 - 2 f(x)/delta ]
    I = mp.quad(lambda y: f(y)/(y - x)**2, [a, x - delta]) + mp.quad(lambda y: f(y)/(y - x)**2, [x + delta, b])
    return I - 2*f(x)/delta
xv = mp.mpf('0.3')
v = fp_int(lambda y: 1, xv, 0, 1, mp.mpf('1e-6'))
check("(4a) fp int_0^1 dy/(y-x)^2 = -1/x - 1/(1-x)", abs(v - (-1/xv - 1/(1 - xv))) < 1e-4)
for beta in [mp.mpf('0.5'), mp.mpf('0.25'), mp.mpf('0.8')]:
    xx = mp.mpf(1)
    # integral over (0, oo): split, y^beta/(y-1)^2 ; tail int_2^oo converges for beta<1
    I = fp_int(lambda y: y**beta, xx, 0, 50, mp.mpf('1e-6')) + mp.quad(lambda y: y**beta/(y - 1)**2, [50, mp.inf])
    pred = -mp.pi*beta*mp.cot(mp.pi*beta)
    print(f"   beta={beta}: fp int_0^oo y^beta/(y-1)^2 = {mp.nstr(I, 10)}   -pi beta cot(pi beta) = {mp.nstr(pred, 10)}")
    check(f"(4b) fp int_0^oo y^beta/(y-x)^2 dy = -pi beta cot(pi beta) x^(beta-1) at beta={beta}", abs(I - pred) < 1e-4)

# (5) equivalence of the two forms of H on a test function phi(x) = x^0.6 (1-x)^0.6 (1 + x)
m0 = mp.mpf(1); m1 = mp.mpf('0.8')
phi = lambda y: y**mp.mpf('0.6')*(1 - y)**mp.mpf('0.6')*(1 + y)
x0 = mp.mpf('0.37')
form1 = ((m1**2 - m0**2)/x0 + (m1**2 - m0**2)/(1 - x0))*phi(x0) - m0**2*fp_int(phi, x0, 0, 1, mp.mpf('1e-6'))
d = mp.mpf('1e-6')
pv = mp.quad(lambda y: (phi(y) - phi(x0))/(y - x0)**2, [0, x0 - d]) + mp.quad(lambda y: (phi(y) - phi(x0))/(y - x0)**2, [x0 + d, 1])
form2 = (m1**2/x0 + m1**2/(1 - x0))*phi(x0) - m0**2*pv
print("   H phi(x0): form1 =", mp.nstr(form1, 10), " form2 =", mp.nstr(form2, 10))
check("(5) the two forms of the 't Hooft operator agree", abs(form1 - form2) < 1e-4)

# (6) Rayleigh-Ritz in the orthonormal basis sqrt2 sin(k pi x)
def spectrum(msq, K=40, Nq=240):
    xs, ws = np.polynomial.legendre.leggauss(Nq); xs = 0.5*(xs + 1); ws = 0.5*ws
    ks = np.arange(1, K + 1)
    Phi = np.sqrt(2)*np.sin(np.outer(ks, np.pi*xs))           # K x Nq
    dPhi = np.sqrt(2)*np.pi*ks[:, None]*np.cos(np.outer(ks, np.pi*xs))
    Hmass = msq*(Phi*(1/xs + 1/(1 - xs))*ws) @ Phi.T
    X, Y = np.meshgrid(xs, xs, indexing='ij'); W = np.outer(ws, ws)
    D = (X - Y); offd = ~np.eye(Nq, dtype=bool)
    Hkin = np.zeros((K, K))
    for a in range(K):
        Da = Phi[a][:, None] - Phi[a][None, :]
        for b in range(a, K):
            Db = Phi[b][:, None] - Phi[b][None, :]
            M = np.zeros((Nq, Nq)); M[offd] = (Da*Db)[offd]/D[offd]**2
            M[~offd] = dPhi[a]*dPhi[b]               # diagonal limit
            Hkin[a, b] = Hkin[b, a] = 0.5*np.sum(W*M)
    H = Hmass + Hkin          # m0^2 = 1
    ev = np.linalg.eigvalsh(H)
    return ev
for msq in [0.0, 1.0]:
    ev = spectrum(msq)
    print(f"   m^2/m0^2={msq}: lowest eigenvalues mu_n^2/m0^2 =", np.round(ev[:6], 4))
    print("      mu_n^2/(pi^2 n) for n=1..12 (n = index from 1 for the excited states):", np.round(ev[1:13]/(np.pi**2*np.arange(1, 13)), 3))
# chiral limit in an orthonormal Legendre basis sqrt(2l+1) P_l(2x-1) (contains the constant function)
def spectrum_legendre(K=30, Nq=240):
    xs, ws = np.polynomial.legendre.leggauss(Nq); xs = 0.5*(xs + 1); ws = 0.5*ws
    from numpy.polynomial import legendre as Lg
    Phi = np.array([np.sqrt(2*l + 1)*Lg.legval(2*xs - 1, [0]*l + [1]) for l in range(K)])
    dPhi = np.array([np.sqrt(2*l + 1)*2*Lg.legval(2*xs - 1, Lg.legder([0]*l + [1])) if l > 0 else np.zeros(Nq) for l in range(K)])
    X, Y = np.meshgrid(xs, xs, indexing='ij'); W = np.outer(ws, ws); D = X - Y; offd = ~np.eye(Nq, dtype=bool)
    H = np.zeros((K, K))
    for a in range(K):
        Da = Phi[a][:, None] - Phi[a][None, :]
        for b in range(a, K):
            Db = Phi[b][:, None] - Phi[b][None, :]
            M = np.zeros((Nq, Nq)); M[offd] = (Da*Db)[offd]/D[offd]**2; M[~offd] = dPhi[a]*dPhi[b]
            H[a, b] = H[b, a] = 0.5*np.sum(W*M)
    gram = (Phi*ws) @ Phi.T
    return np.linalg.eigvalsh(np.linalg.solve(gram, H)), gram
ev0, gram = spectrum_legendre()
print("   chiral limit (Legendre basis): lowest eigenvalues =", np.round(np.sort(ev0)[:6], 6), " (orthonormality error", f"{np.abs(gram-np.eye(len(gram))).max():.1e})")
check("(6a) chiral limit m=0: exact zero mode (massless pion, phi = 1) and positive excitations", abs(np.sort(ev0)[0]) < 1e-9 and np.sort(ev0)[1] > 1)
ev1 = spectrum(1.0, K=60, Nq=300)
ratio = ev1[20]/(np.pi**2*20)
check("(6b) Regge behaviour mu_n^2 ~ pi^2 m0^2 n at large n (ratio within 10% at n=20)", abs(ratio - 1) < 0.1)
check("(6c) positivity of the spectrum (quadratic form >= 0)", ev1.min() > 0 and np.sort(ev0)[0] > -1e-9)

# (7) endpoint exponent: pi beta cot(pi beta) = 1 - m^2/m0^2
for msq in [mp.mpf(1), mp.mpf('0.1'), mp.mpf('0.01')]:
    beta = mp.findroot(lambda b: mp.pi*b*mp.cot(mp.pi*b) - (1 - msq), mp.mpf('0.3') if msq > 0.5 else mp.mpf('0.1'))
    approx = mp.sqrt(3*msq)/mp.pi
    print(f"   m^2/m0^2={msq}: beta = {mp.nstr(beta, 8)}   small-m approx sqrt(3) m/(pi m0) = {mp.nstr(approx, 8)}")
check("(7) m^2 = m0^2 gives beta = 1/2", abs(mp.findroot(lambda b: mp.pi*b*mp.cot(mp.pi*b), mp.mpf('0.4')) - mp.mpf(1)/2) < 1e-15)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
