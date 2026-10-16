r"""W14 -- checks for prop:dy-glauber-pinch, prop:dy-abelian-model (G-i)-(G-iv), ex:dy-future-vs-past,
ex:dy-spectator-lcopt, ex:dy-glauber-model, rem:dy-dft-premises (VF-REF-8), lem:dy-poles-orientation (signs).
Conventions: metric (+,-,-,-), v^pm=(v^0 pm v^3)/sqrt2, v.w = v+w- + v-w+ - vT.wT, Feynman propagators +i0,
D_mu = d_mu - i g A_mu (vertex +i g), eikonal rules VF-WL-1 (k flows into the line).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); LOG.append(s)

mp.mp.dps = 30
# ---------------------------------------------------------------- 1. Glauber pinch (prop:dy-glauber-pinch)
# spectator s_A: final momentum p' (on shell), carries p'-k before the attachment; active a: l + k
kp, km, kT2 = sp.symbols('k_p k_m k_T2', real=True)
pp, pm_, pT_k, lp, lm, lT_k, lT2, ms2, ma2 = sp.symbols('pp pm pTk lp lm lTk lT2 ms2 ma2', real=True)
# exact denominators (without i0), written with light-cone components; pT.kT = pT_k etc.
Ds_exact = -2*(pp*km + pm_*kp - pT_k) + 2*kp*km - kT2        # (p'-k)^2 - ms^2 with p'^2 = ms^2
Da_exact = (2*lp*lm - lT2 - ma2) + 2*(lp*km + lm*kp - lT_k) + 2*kp*km - kT2   # (l+k)^2 - ma^2
c_ = (2*pT_k - kT2)/(2*pp)
d_ = (lT2 + 2*lT_k + kT2 + ma2 - 2*lp*lm)/(2*lp)
lam = sp.symbols('lambda', positive=True)
scal = {kp: lam**2*kp, km: lam**2*km, kT2: lam**2*kT2, pT_k: lam**2*pT_k, lT_k: lam**2*lT_k,
        pm_: lam**2*pm_, lm: lam**2*lm, lT2: lam**2*lT2, ms2: lam**2*ms2, ma2: lam**2*ma2}
rs = sp.expand(Ds_exact.subs(scal, simultaneous=True) - (-2*pp*(km - c_)).subs(scal, simultaneous=True))
ra = sp.expand(Da_exact.subs(scal, simultaneous=True) - (2*lp*(km - d_)).subs(scal, simultaneous=True))
log('1a. D_s - [-2p+(k- - c)] =', sp.factor(rs), ' ; D_a - [2l+(k- - d)] =', sp.factor(ra), ' (both O(lambda^4))')
# residue: int dk-/(2pi) [i/(-2p(k-c)+i0)] [i/(2l(k-d)+i0)] = i/(4 p l (c-d) + i0)
p_, l_, c0, d0 = mp.mpf('0.6'), mp.mpf('0.4'), mp.mpf('0.013'), mp.mpf('-0.021')
def integrand(x, e):
    return (1j/(-2*p_*(x-c0)+1j*e))*(1j/(2*l_*(x-d0)+1j*e))/(2*mp.pi)
for e in (mp.mpf('1e-4'), mp.mpf('1e-6')):
    val = mp.quad(lambda x: integrand(x, e), [-mp.inf, d0, c0, mp.inf])
    log('1b. real axis, i0->i%s: %s ; residue formula i/(4pl(c-d)) = %s' % (mp.nstr(e,1), mp.nstr(val, 12), mp.nstr(1j/(4*p_*l_*(c0-d0)), 12)))
for kap in (mp.mpf('0.05'), mp.mpf('0.2'), mp.mpf('-0.05'), mp.mpf('-0.2')):
    val = mp.quad(lambda x: integrand(x + 1j*kap, mp.mpf('1e-9')), [-mp.inf, -1, 0, 1, mp.inf])
    log('1c. contour shifted to Im k- = %s (|c-d| = %s): %s' % (mp.nstr(kap,2), mp.nstr(abs(c0-d0),2), mp.nstr(val, 6)))

# ---------------------------------------------------------------- 2. (G-i) Fourier transform and exponent
m_, bb = mp.mpf('0.7'), mp.mpf('1.9')
ft = mp.quadosc(lambda k: k*mp.besselj(0, k*bb)/(k**2+m_**2), [0, mp.inf], omega=bb)/(2*mp.pi)
log('2a. int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = %s ; K0(mb)/2pi = %s' % (mp.nstr(ft, 15), mp.nstr(mp.besselk(0, m_*bb)/(2*mp.pi), 15)))
log('2b. small-m limit: chi -> (gAgB/2pi)[ln(m b/2) + gamma_E]: K0(x)+ln(x/2)+gamma_E at x=1e-4:', mp.nstr(mp.besselk(0, mp.mpf('1e-4')) + mp.log(mp.mpf('0.5e-4')) + mp.euler, 5))
# (G-ii) combinatorial identity
chi = sp.symbols('chi', real=True)
for n in range(1, 9):
    sm = sum((sp.I*chi)**j/sp.factorial(j)*(-sp.I*chi)**(n-j)/sp.factorial(n-j) for j in range(n+1))
    assert sp.expand(sm) == 0
log('2c. sum_j (i chi)^j/j! (-i chi)^(n-j)/(n-j)! = 0 for n=1..8: OK')

# ---------------------------------------------------------------- 3. (G-iv) active-spectator exchange: I_as
k, kmn = sp.symbols('k k_m', real=True)
pb, cb, K2 = sp.symbols('p_b c_b K2', positive=True)
# I_as(k-) = int dk+ 1/((2 pb k+ + cb + i0)(2 k+ k- - K2 + i0))
def Ias_num(kmv, e=mp.mpf('1e-8')):
    pbv, cbv, K2v = mp.mpf('1.1'), mp.mpf('0.003'), mp.mpf('0.012')
    f = lambda x: 1/((2*pbv*x + cbv + 1j*e)*(2*x*kmv - K2v + 1j*e))
    poles = sorted([-cbv/(2*pbv), K2v/(2*kmv)])
    return mp.quad(f, [-mp.inf] + poles + [mp.inf]), 2j*mp.pi*(1 if kmv < 0 else 0)/(2*pbv*K2v + 2*kmv*cbv)
for kmv in (mp.mpf('0.006'), mp.mpf('-0.006'), mp.mpf('-0.02')):
    num, form = Ias_num(kmv)
    log('3a. k-=%s: I_as numeric %s ; formula 2 pi i theta(-k-)/(2 pb K^2 + 2 k- cb) %s' % (mp.nstr(kmv,2), mp.nstr(num,10), mp.nstr(form,10)))
pbv, cbv, K2v, kmv = mp.mpf('1.1'), mp.mpf('0.003'), mp.mpf('0.012'), mp.mpf('-0.006')
log('3b. pole location k+ = K^2/(2k-) = %s (O(1): A-collinear), eikonal replacement rel. change k- c_b/(p_b K^2) = %s'
    % (mp.nstr(K2v/(2*kmv), 4), mp.nstr(abs(kmv*cbv/(pbv*K2v)), 3)))

# ---------------------------------------------------------------- 4. ex:dy-future-vs-past (VF-REF-11)
x = sp.symbols('x', real=True)
Qa = sp.symbols('Q_a', real=True)
e_ = sp.symbols('e', positive=True)
lhs = sp.I*Qa/(x + sp.I*e_) + sp.I*(-Qa)*(1/(x + sp.I*e_) - 1/(x - sp.I*e_))
log('4a. iQa/(x+ie) + iQs[1/(x+ie) - 1/(x-ie)] with Qs=-Qa, minus iQa/(x-ie):', sp.simplify(lhs - sp.I*Qa/(x - sp.I*e_)))
# Sokhotski: i[1/(x+i0) - 1/(x-i0)] = 2 pi delta(x)
hfun = lambda t: mp.exp(-t**2)*(1+t)
val = mp.quad(lambda t: 1j*(1/(t+1j*mp.mpf('1e-6')) - 1/(t-1j*mp.mpf('1e-6')))*hfun(t), [-mp.inf, 0, mp.inf])
log('4b. <i[1/(x+i0)-1/(x-i0)], h> = %s ; 2 pi h(0) = %s' % (mp.nstr(val, 10), mp.nstr(2*mp.pi*hfun(0), 10)))

# ---------------------------------------------------------------- 5. ex:dy-spectator-lcopt
al, be, D1 = sp.symbols('alpha beta D_1', real=True)
Jin = (sp.I/D1)*sp.I/(x - al); Jfi = (sp.I/D1)*sp.I/(be - x)
prod = (sp.I/(x - al))*(sp.I/(be - x))
log('5a. J_in + J_fi - [i/(x-alpha)][i/(beta-x)] with D1 = beta - alpha:', sp.simplify((Jin + Jfi - prod).subs(D1, be - al)))
# equal-time transfer: int dk/(2pi) J R with R = r/(k - z), Im z<0, |z| >> |alpha|,|beta|
alv, bev = mp.mpf('-0.011'), mp.mpf('0.017'); D1v = bev - alv
for zv in (mp.mpf('0.9') - 0.05j, mp.mpf('-2.5') - 0.4j, mp.mpf('0.6') + 0.03j):
    r = mp.mpf(1)
    J = lambda t: (1j/D1v)*(1j/(t - alv + 1j*mp.mpf('1e-12')) + 1j/(bev - t + 1j*mp.mpf('1e-12')))
    R = lambda t: r/(t - zv)
    val = mp.quad(lambda t: J(t)*R(t)/(2*mp.pi), [-mp.inf] + sorted([alv, bev, mp.re(zv)]) + [mp.inf])
    log('5b. z=%s: int dk/(2pi) J R = %s ; R(0) i/D1 = %s ; rel.dev = %s' % (mp.nstr(zv,3), mp.nstr(val,10), mp.nstr(R(0)*1j/D1v,10), mp.nstr(abs(val/(R(0)*1j/D1v)-1),3)))
# single orderings: symmetric truncation |k|<K with strict R = const -> 1/2 each; full propagator -> theta(k+)
K = mp.mpf(50)
fin = mp.quad(lambda t: (1j/(bev - t + 1j*mp.mpf('1e-14')))/(2*mp.pi), [-K, alv, bev, K])
ini = mp.quad(lambda t: (1j/(t - alv + 1j*mp.mpf('1e-14')))/(2*mp.pi), [-K, alv, bev, K])
log('5c. symmetric truncation K=%s: final ordering weight %s, initial ordering weight %s (each -> 1/2)' % (mp.nstr(K,2), mp.nstr(fin, 6), mp.nstr(ini, 6)))
kplus, kT2v = mp.mpf('0.01'), mp.mpf('0.04')
zpole = (kT2v - 1j*mp.mpf('1e-14'))/(2*kplus)
Rf = lambda t: 1/(2*kplus*t - kT2v + 1j*mp.mpf('1e-14'))
finw = mp.quad(lambda t: (1j/(bev - t + 1j*mp.mpf('1e-14')))*Rf(t)/(2*mp.pi), [-mp.inf, alv, bev, mp.re(zpole), mp.inf])
iniw = mp.quad(lambda t: (1j/(t - alv + 1j*mp.mpf('1e-14')))*Rf(t)/(2*mp.pi), [-mp.inf, alv, bev, mp.re(zpole), mp.inf])
R0 = Rf(0)
log('5d. full propagator, k+ = %s > 0: final/R(0) = %s, initial/R(0) = %s (theta(k+) and 0 up to O(beta/z))' % (mp.nstr(kplus,2), mp.nstr(finw/R0, 6), mp.nstr(iniw/R0, 6)))

# ---------------------------------------------------------------- 6. ex:dy-glauber-model: FFT demonstration
Ng = 512; Lbox = 40.0
dx = Lbox/Ng
grid = (np.arange(Ng) - Ng//2)*dx
DX, DY = np.meshgrid(grid, grid, indexing='ij')
# complex toy amplitude in the relative transverse momentum Delta (units: width 1)
M0 = np.exp(-((DX-0.4)**2 + DY**2)/2.0)*(1.0 + 0.9j*DX + 0.3*DY**2)*np.exp(0.7j*DY)
# b-space via FFT with the convention M(Delta) = int d^2b e^{-i Delta.b} Mt(b)
kgrid = 2*np.pi*np.fft.fftfreq(Ng, d=dx)
BX, BY = np.meshgrid(kgrid, kgrid, indexing='ij')
Mt0 = np.fft.ifft2(np.fft.ifftshift(M0))
bmod = np.sqrt(BX**2 + BY**2)
mg = 0.3; c_gg = 2.0    # boson mass and g_A g_B (dimensionless toy values)
bsafe = np.where(bmod > 0, bmod, 0.5*(kgrid[1]-kgrid[0]))
from scipy.special import k0
chi_b = -c_gg/(2*np.pi)*k0(mg*bsafe)
Mt1 = 1j*chi_b*Mt0
M1 = np.fft.fftshift(np.fft.fft2(Mt1))
inter = 2*np.real(M1*np.conj(M0))
single = np.abs(M1*np.conj(M0))
r_point = np.sum(np.abs(inter))/np.sum(2*single)
r_int = np.sum(inter)/np.sum(2*single)
log('6a. O(g^2): int|2Re M1 M0*| / int|2 M1 M0*| = %.3f (pointwise non-cancellation); int 2Re M1 M0* / int|2M1M0*| = %.1e' % (r_point, r_int))
Mt2 = 0.5*(1j*chi_b)**2*Mt0
M2 = np.fft.fftshift(np.fft.fft2(Mt2))
g4 = np.abs(M1)**2 + 2*np.real(np.conj(M0)*M2)
log('6b. O(g^4): int[|M1|^2 + 2Re M0* M2] / int|M1|^2 = %.1e ; pointwise int|...|/int|M1|^2 = %.3f' % (np.sum(g4)/np.sum(np.abs(M1)**2), np.sum(np.abs(g4))/np.sum(np.abs(M1)**2)))
Mall = np.fft.fftshift(np.fft.fft2(np.exp(1j*chi_b)*Mt0))
log('6c. all orders: int|M|^2 / int|M0|^2 = %.15f' % (np.sum(np.abs(Mall)**2)/np.sum(np.abs(M0)**2)))
w0 = np.abs(M0)**2; w1 = np.abs(Mall)**2
d2_0 = np.sum((DX**2+DY**2)*w0)/np.sum(w0); d2_1 = np.sum((DX**2+DY**2)*w1)/np.sum(w1)
log('6d. <Delta^2>: without exchange %.4f, with exchange %.4f (the relative-momentum distribution changes)' % (d2_0, d2_1))
log('6e. chi(b) real: max|Im chi| = %.1e ; parameters: grid %d^2, box %.0f, m=%.1f, g_A g_B=%.1f' % (np.max(np.abs(np.imag(chi_b))), Ng, Lbox, mg, c_gg))

# ---------------------------------------------------------------- 7. rem:dy-dft-premises (VF-REF-8)
pAp, m2, kpl, kmi, kT2s = sp.symbols('p_Ap m2 k_p k_m k_T2', real=True)
pA_minus = m2/(2*pAp)
lhs = (2*pAp*pA_minus - 0) - 2*(pAp*kmi + pA_minus*kpl) + (2*kpl*kmi - kT2s) - m2   # (pA-k)^2 - m^2, pA_T = 0
rhs = -2*pAp*(kmi + m2/(2*pAp**2)*kpl) + (2*kpl*kmi - kT2s)
log('7. (pA-k)^2 - m^2 - [-2pA+(k- + m^2 k+/(2 pA+^2)) + k^2] =', sp.simplify(lhs - rhs))

# ---------------------------------------------------------------- 8. lem:dy-poles-orientation: sign of Im of LCOPT denominators
# initial: D = P^- + K_injected - sum E(l) with E(l) = (lT^2 + m^2 - i0)/(2 l+): Im(-E) = +i0/(2l+) > 0 for l+>0
lplus = sp.symbols('l_plus', positive=True); eta = sp.symbols('eta', positive=True)
E = (sp.Symbol('A2', positive=True) - sp.I*eta)/(2*lplus)
log('8. Im(-E(l)) for l+>0:', sp.simplify(sp.im(-E)), '> 0 ; initial zero k- = -A_D - i0 (LHP), final zero k- = A_D\' + i0 (UHP)')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'glauber_model_check.log'), 'w').write('\n'.join(LOG) + '\n')
