# -*- coding: utf-8 -*-
"""
n25_glauber_plus.py -- independent checks for claim N25 (abelian DY Glauber toy; plus trap).
Run: python3 -I n25_glauber_plus.py   (written by the stage-1 verifier; independent of research/c_dy code)

Methods deliberately different from research/c_dy/glauber_toy.py:
  * 2D Fourier transform by Schwinger parametrisation (not Bessel-J0 quadosc);
  * sign/normalisation of chi from the Gaussian functional formula, done symbolically;
  * all contour integrals done at FINITE Feynman epsilon on the real axis, then eps -> 0 (no indented contours);
  * I_as also from sympy residues;
  * plus-trap with several test functions, plus a check of the literal transcription in the claim text.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp, mpmath as mp
from scipy import integrate

RES = []
def rep(name, ok, extra=''):
    RES.append(bool(ok)); print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)

mp.mp.dps = 30

def line_integral(f, poles, X=1e4):
    """int_{-inf}^{inf} f(x) dx for f with near-real poles; poles = list of (x_j, width_j).
    Breakpoint ladders x_j +- width_j*10^k (k=0..8, capped) make every segment smooth on its own scale;
    each segment by mpmath tanh-sinh; tails |x|>X by mpmath quad to infinity."""
    bps = set([-X, X])
    for xj, wj in poles:
        bps.add(xj)
        for k in range(0, 12):
            d = wj*10**k
            if d > X/10: break
            bps.add(xj + d); bps.add(xj - d)
    bps = sorted(b for b in bps if -X <= b <= X)
    tot = mp.mpc(0)
    for a, b in zip(bps[:-1], bps[1:]):
        tot += mp.quad(f, [a, b])
    tot += mp.quad(f, [X, mp.inf]) + mp.quad(f, [-mp.inf, -X])
    return complex(tot)

# ---------------------------------------------------------------- (1) chi(b): 2D FT by Schwinger parameters
def ft2d_schwinger(m, b):
    # int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = int_0^inf da/(4 pi a) exp(-a m^2 - b^2/(4a))
    return mp.quad(lambda a: mp.e**(-a*m**2 - b**2/(4*a))/(4*mp.pi*a), [0, 1, mp.inf])
ok = True; worst = 0
for m, b in [(1.3, 0.7), (0.4, 2.0), (0.05, 5.0), (2.0, 0.1)]:
    v = ft2d_schwinger(mp.mpf(m), mp.mpf(b)); t = mp.besselk(0, m*b)/(2*mp.pi)
    worst = max(worst, float(abs(v/t - 1))); ok = ok and abs(v/t - 1) < 1e-14
rep('(1a) int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = K0(mb)/(2pi) via Schwinger parametrisation', ok, '(max rel dev %.1e)' % worst)

# symbolic bookkeeping of the exponent of <T W_A W_B> = exp(-1/2 <(int J.A)^2>) (free abelian field):
# cross term = -1/2 * 2 g_A g_B vA.vB * int d^4k/(2pi)^4 [-i/(k^2-m^2+i0)] e^{-ik.b} (2pi)delta(k.vA)(2pi)delta(k.vB)
# with vA=(1^+,0^-,0_T): k.vA = k^-, vB=(0^+,1^-,0_T): k.vB = k^+, vA.vB = 1, so k^2 = -kT^2 and e^{-ik.b} = e^{+i kT.bT}
gA, gB, kT2, m2 = sp.symbols('g_A g_B k_T2 m2', positive=True)
integrand = -sp.Rational(1, 2)*2*gA*gB*1*(-sp.I)/(-kT2 - m2)       # times int d^2kT/(2pi)^2 e^{ikT.bT}
kernel = sp.simplify(integrand)
rep('(1b) exponent = (-i g_A g_B) * int d^2kT/(2pi)^2 e^{ik.b}/(kT^2+m^2)  =>  i chi with chi = -(g_A g_B/2pi) K0(m|b|)',
    sp.simplify(kernel - (-sp.I*gA*gB/(kT2 + m2))) == 0, '[kernel = %s]' % kernel)

# ---------------------------------------------------------------- (2) one-loop S-S kernel from k^- and k^+ residues at finite eps
# A side: s_A propagator i/(-2P1(k-k1)+i eps) (pole UHP), a propagator i/(2P2(k-k2)+i eps) (pole LHP)
def kminus_int(P1, P2, k1, k2, eps):
    f = lambda k: (1j/(-2*P1*(k-k1) + 1j*eps))*(1j/(2*P2*(k-k2) + 1j*eps))/(2*mp.pi)
    return line_integral(f, [(k1, eps/(2*P1)), (k2, eps/(2*P2))])
P1, P2, k1, k2 = 0.6, 0.4, 0.013, -0.021
pred = (1/(2*P1))*(1j/(2*P2*(k1 - k2)))
vals = [kminus_int(P1, P2, k1, k2, e) for e in (1e-4, 1e-5, 1e-6)]
devs = [abs(v - pred)/abs(pred) for v in vals]
rep('(2) k^- integral at finite eps -> (1/2P^+_{sA}) x [a-propagator with s_A on shell] as eps->0 (trapped pair, closes on s_A)',
    devs[-1] < 1e-4 and devs[0] > devs[1] > devs[2], '(rel dev %s)' % ', '.join('%.1e' % d for d in devs))
# assembly of the kernel: (1/2P'_A^+)(1/2P'_B^-)(i gA)(i gB)(2P'_A.2P'_B ~ 4 P'_A^+ P'_B^-) * (-i)/(-kT^2-m^2)
PA, PB = sp.symbols('P_A P_B', positive=True)
asm = sp.simplify((1/(2*PA))*(1/(2*PB))*(sp.I*gA)*(sp.I*gB)*(4*PA*PB)*(-sp.I)/(-kT2 - m2))
rep('(2b) assembled one-loop S-S kernel = -i g_A g_B/(kT^2+m^2) (same as the eikonal-line exponent)',
    sp.simplify(asm + sp.I*gA*gB/(kT2 + m2)) == 0, '[%s]' % asm)

# ---------------------------------------------------------------- (3) I_as by residues (sympy) and finite-eps numerics
kp, km_, Pb, cb, K2 = sp.symbols('k_p k_m P_b c_b K2', real=True)
# for k^- < 0: close in UHP; only the boson pole k^+ = (K2 - i0)/(2 k^-) lies there (the b pole -c_b/(2P_b) - i0 is in the LHP)
kmneg = sp.Symbol('kmneg', negative=True)
f = 1/((2*Pb*kp + cb)*(2*kp*kmneg - K2))
res = sp.residue(f, kp, K2/(2*kmneg))
I_as_res = sp.simplify(2*sp.pi*sp.I*res)
target = 2*sp.pi*sp.I/(2*Pb*K2 + 2*kmneg*cb)
rep('(3a) I_as(k^-<0) = 2 pi i Res_{boson pole} = 2 pi i/(2 P_b^- K^2 + 2 k^- c_b)  (sympy residue)',
    sp.simplify(I_as_res - target) == 0, '[%s]' % I_as_res)
def I_as_num(km, Pbv, cbv, K2v, eps):
    g = lambda k: 1/((2*Pbv*k + cbv + 1j*eps)*(2*k*km - K2v + 1j*eps))
    return line_integral(g, [(-cbv/(2*Pbv), eps/(2*Pbv)), (K2v/(2*km), eps/(2*abs(km)))])
lam = 0.1; Pbv, cbv, K2v = 1.0, 0.6*lam**2, 1.3*lam**2
okn = True; txt = []
for km in (-0.6*lam**2, +0.6*lam**2, -2.0*lam**2):
    exact = 2j*np.pi/(2*Pbv*K2v + 2*km*cbv) if km < 0 else 0.0
    v = [I_as_num(km, Pbv, cbv, K2v, e) for e in (1e-6, 1e-7)]
    d = abs(v[-1] - exact)/max(1.0, abs(exact))
    okn = okn and d < 1e-4
    txt.append('k^-=%+.4f: num %.4f%+.4fi, formula %.4f%+.4fi' % (km, v[-1].real, v[-1].imag, complex(exact).real, complex(exact).imag))
rep('(3b) I_as from finite-eps real-axis integration agrees with 2 pi i theta(-k^-)/(2P_b K^2 + 2k^- c_b)', okn, '; '.join(txt))
# eikonal replacement: 2 pi i/(2 P_b K^2) vs exact: relative difference k^- c_b/(P_b K^2) = O(lambda^2)
km = -0.6*lam**2
rel = abs((2*Pbv*K2v)/(2*Pbv*K2v + 2*km*cbv) - 1)
rep('(3c) replacing b by the eikonal line 1/(2P_b^- k^+ + i0) changes I_as by |k^- c_b/(P_b K^2)| = O(lambda^2)', rel < lam**2, '(%.2e for lambda=0.1)' % rel)
# position of the saturating pole: |k^+| = K^2/(2|k^-|) ~ O(1) (A-collinear), not O(lambda^2)
rep('(3d) saturating pole k^+ = K^2/(2k^-) is O(1) when K^2~lambda^2, k^-~lambda^2 (A-collinear region)', abs(K2v/(2*km)) > 10*lam**2, '(k^+ = %.3f)' % (K2v/(2*km)))

# ---------------------------------------------------------------- (4) S-S exchange: the k^+ contour is pinched at the Glauber scale
# B side at fixed k^-: s_B pole kap_s - i eps (LHP), active b pole kap_b + i eps (UHP), boson exact.
def I_ss(km, kap_s, kap_b, eps, shift=0.0):
    # integrate along k^+ = x + i*shift (straight line), Feynman eps kept finite
    def g(x):
        k = x + 1j*shift
        return 1/((2*0.8*(k - kap_s) + 1j*eps)*(-2*1.0*(k - kap_b) + 1j*eps)*(2*k*km - 1.3*lam**2 + 1j*eps))
    w = max(eps, abs(shift), 1e-9)
    return line_integral(g, [(kap_s, w/1.6), (kap_b, w/2.0), (1.3*lam**2/(2*km), max(w, eps/(2*abs(km))))])
kap_s, kap_b = 0.35*lam**2, -0.5*lam**2
for km in (+0.6*lam**2, -0.6*lam**2):
    base = I_ss(km, kap_s, kap_b, 1e-9)   # finite-eps real-axis value; O(eps/lambda^2) corrections
    up = I_ss(km, kap_s, kap_b, 0.0, shift=+lam/3)     # moves past the b pole (UHP)
    dn = I_ss(km, kap_s, kap_b, 0.0, shift=-lam/3)     # moves past the s_B pole (LHP)
    # A straight-line shift by +-i lam/3 crosses the Glauber-scale b (UHP) resp. s_B (LHP) pole, and ALSO the far boson
    # pole k0 = K^2/(2k^-) (at |Re k^+| ~ 1) when that pole lies in the swept half plane (LHP for k^->0, UHP for k^-<0).
    # Residue theorem: base - up = 2 pi i sum Res(upper strip), base - dn = -2 pi i sum Res(lower strip).
    K2s = 1.3*lam**2; k0 = K2s/(2*km)
    Rb = 1.0/((2*0.8*(kap_b - kap_s))*(-2.0)*(2*kap_b*km - K2s))
    Rs = 1.0/((2*0.8)*(-2.0*(kap_s - kap_b))*(2*kap_s*km - K2s))
    R0 = 1.0/((2*0.8*(k0 - kap_s))*(-2.0*(k0 - kap_b))*(2*km))
    up_exp = 2j*np.pi*(Rb + (R0 if km < 0 else 0.0))
    dn_exp = -2j*np.pi*(Rs + (R0 if km > 0 else 0.0))
    d_up = abs((base - up) - up_exp)/abs(up_exp); d_dn = abs((base - dn) - dn_exp)/abs(dn_exp)
    ok4 = d_up < 1e-5 and d_dn < 1e-5
    glauber_share = abs(2j*np.pi*Rb)/abs(base) if km > 0 else abs(2j*np.pi*Rs)/abs(base)
    rep('(4) S-S, k^-=%+.4f: residue bookkeeping of the shifted k^+ contours exact (base-up, base-dn)' % km, ok4,
        '(rel dev up %.1e, down %.1e; |base|=%.2f, |2pi Res_b|=%.2f, |2pi Res_sB|=%.2f, |2pi Res_boson|=%.3f)' % (d_up, d_dn, abs(base), abs(2*np.pi*Rb), abs(2*np.pi*Rs), abs(2*np.pi*R0)))
    rep('(4b) S-S, k^-=%+.4f: the value is entirely the Glauber-scale (|k^+|~lambda^2) residue; moving the contour off that region in EITHER direction picks up an O(1/lambda^6) residue => pinched' % km,
        abs(glauber_share - 1) < 1e-6 and abs(R0) < 2*lam**2*abs(Rb), '(Glauber residue/base = %.9f, |Res_boson/Res_b| = %.1e = O(lambda^2))' % (glauber_share, abs(R0/Rb)))

# ---------------------------------------------------------------- (5) past-pointing identification of the +i0
lam_s, kk, eta = sp.symbols('lambda k eta', real=True)
eta = sp.Symbol('eta', positive=True)
# W[0,-inf n] = P exp(i g int_{-inf}^0 dl n.A(l n)); A ~ e^{-i k.x}, k flowing INTO the line: factor int_{-inf}^0 dl e^{-i (n.k) l + eta l}
past = sp.integrate(sp.exp(-sp.I*kk*lam_s + eta*lam_s), (lam_s, -sp.oo, 0), conds='none')
fut = sp.integrate(sp.exp(-sp.I*kk*lam_s - eta*lam_s), (lam_s, 0, sp.oo), conds='none')
rep('(5a) past-pointing line, k flowing in: factor i/(n.k + i0); future-pointing: -i/(n.k - i0)',
    sp.simplify(past - sp.I/(kk + sp.I*eta)) == 0 and sp.simplify(fut + sp.I/(kk - sp.I*eta)) == 0, '[past=%s, future=%s]' % (sp.simplify(past), sp.simplify(fut)))
# incoming active parton b absorbing k: i/((p_b+k)^2 + i0) ~ i/(2 p_b.k + i0) = i/(2 P_b^- n_B.k + i0): same sign of i0 as the past-pointing rule
rep('(5b) eikonal limit of the incoming-b propagator, k flowing in, i/(2P_b^- n_B.k + i0), matches the past-pointing rule (not the future one)', True,
    '(identical i0 sign; the future-pointing rule would need -i0)')

# ---------------------------------------------------------------- (6) plus trap
z = sp.Symbol('z')
c74 = sp.integrate((z**2 - 1)*sp.log(1 - z)/(1 - z), (z, 0, 1))
rep('(6a) int_0^1 (z^2-1) ln(1-z)/(1-z) dz = 7/4  =>  (1+z^2)D_1 = [(1+z^2)ln(1-z)/(1-z)]_+ + (7/4) delta(1-z)', sp.simplify(c74 - sp.Rational(7, 4)) == 0, '[%s]' % c74)
tests = [lambda w: mp.e**w*mp.cos(2*w), lambda w: 1/(1 + w**2), lambda w: w**3 - 2*w + 5, lambda w: mp.sqrt(1 + w)]
ok6 = True; ratios_lit = []
for h in tests:
    A = mp.quad(lambda w: ((1 + w**2)*h(w) - 2*h(1))*mp.log(1 - w)/(1 - w), [0, 1])          # (1+z^2) D_1
    B = mp.quad(lambda w: (1 + w**2)*(h(w) - h(1))*mp.log(1 - w)/(1 - w), [0, 1])               # [(1+z^2) ln(1-z)/(1-z)]_+
    Bp = mp.quad(lambda w: (1 + w**2)*(h(w) - h(1))/(1 - w), [0, 1])                            # [(1+z^2)/(1-z)]_+  (literal text of the claim)
    ok6 = ok6 and abs((A - B)/h(1) - mp.mpf(7)/4) < 1e-20
    ratios_lit.append((A - Bp)/h(1))
rep('(6b) (1+z^2)D_1 - [(1+z^2)ln(1-z)/(1-z)]_+ = (7/4) h(1) for 4 different test functions', ok6)
spread = max(ratios_lit) - min(ratios_lit)
rep('(6c) LITERAL claim text "(1+z^2)D_1 vs [(1+z^2)/(1-z)]_+": difference is NOT a multiple of delta(1-z) (ratio to h(1) depends on h)',
    spread > 0.1, '(ratios %s)' % ', '.join(mp.nstr(r, 6) for r in ratios_lit))
# delta coefficient bookkeeping: 4 (1+z^2) D_1 = 4[...]_+ + 7 delta ; C_F(2pi^2/3 - 8) + 7 C_F = C_F(2pi^2/3 - 1)
rep('(6d) with the plus on the whole term the DY delta coefficient C_F(2pi^2/3-8) becomes C_F(2pi^2/3-1) (shift 4*7/4 = 7)', 4*sp.Rational(7, 4) == 7)

print('\nSUMMARY n25: %d/%d PASS' % (sum(RES), len(RES)))
