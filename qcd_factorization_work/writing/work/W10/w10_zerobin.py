"""
W10 / Ch9 ex:method-sudakov-subtraction, step (6): the zero-bin term of the off-shell triangle in the light-cone
(k^- residue) representation.

    T_{C1} T_S Gamma = 1/(D_g e_1 h_2),  D_g = -(2k^+k^- - kT^2) - i0,  e_1 = m^2 + 2P k^- - i0,  h_2 = 2P' k^+ - i0,
    measure mu^{2 eps} int d^D k /(i pi^{D/2}),  d^D k = dk^+ dk^- d^{2-2eps} kT,  D = 4 - 2 eps.

Claim printed in the text:
    int T_{C1}T_S Gamma = Gamma(1+eps)/(eps Qt^2) (mu^2/m^2)^eps int_0^infty dsigma sigma^{-1-eps},  sigma = k^+/P,
    Qt^2 = 2PP',  i.e. a scaleless sigma integral = (1/eps_UV - 1/eps_IR) times the prefactor.

Checks:
 (1) k^- residue: for k^+>0 only the D_g pole is in the lower half plane; int dk^- 1/(D_g e_1) = pi i/(k^+ e_1(k0)),
     k0 = kT^2/(2k^+), e_1(k0) = m^2 + P kT^2/k^+;  for k^+<0 all poles are in the upper half plane -> 0.
 (2) transverse integral in 2-2eps dimensions: int d^{2-2eps}kT 1/(a + P kT^2) = pi^{1-eps} Gamma(eps) (a/P)^{-eps}/P.
 (3) assembling: the integrand in sigma is (1/Qt^2) Gamma(eps) (mu^2/m^2)^eps sigma^{-1-eps}; numerical check on a
     finite window [s1,s2] at eps = 0.3 (UV side convergent) and eps = -0.3 (IR side convergent), against the
     direct numerical integration of the residue form over k^+ and |kT|.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

npass = nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# (1) k^- integral at finite i0 (eta), numerically, for both signs of k^+, against the residue formula
mp.mp.dps = 30
def kminus_integral(kpv, kT2v, m2v, Pv, etav):
    Dg = lambda x: -(2*kpv*x - kT2v) - 1j*etav
    e1 = lambda x: m2v + 2*Pv*x - 1j*etav
    f = lambda x: 1/(Dg(x)*e1(x))
    pts = sorted([kT2v/(2*kpv), -m2v/(2*Pv)])
    return mp.quad(f, [-mp.inf, pts[0]-1, pts[0], (pts[0]+pts[1])/2, pts[1], pts[1]+1, mp.inf])
for kpv in [mp.mpf('0.4'), mp.mpf('1.7')]:
    kT2v, m2v, Pv, etav = mp.mpf('0.3'), mp.mpf('0.05'), mp.mpf('0.8'), mp.mpf('1e-9')
    num = kminus_integral(kpv, kT2v, m2v, Pv, etav)
    target = mp.pi*1j/(kpv*(m2v + Pv*kT2v/kpv))
    check('(1) k^+=%s>0: int dk^- 1/(D_g e_1) = pi i/(k^+ e_1(k0)), k0=kT^2/(2k^+)' % mp.nstr(kpv, 3),
          abs(num/target - 1) < 1e-6, mp.nstr(num, 12) + ' vs ' + mp.nstr(target, 12))
num = kminus_integral(mp.mpf('-0.6'), mp.mpf('0.3'), mp.mpf('0.05'), mp.mpf('0.8'), mp.mpf('1e-9'))
check('(1) k^+<0: both poles in the upper half plane -> integral vanishes', abs(num) < 1e-6, mp.nstr(num, 6))
# symbolic residue at the D_g pole (closing below, clockwise)
kp, kT2, m2, P, eta, x = sp.symbols('kp kT2 m2 P eta x', positive=True)
k0 = (kT2 - sp.I*eta)/(2*kp)
res = sp.limit(1/(-2*kp*(m2 + 2*P*x - sp.I*eta)), x, k0)
I_sym = sp.simplify(sp.limit(-2*sp.pi*sp.I*res, eta, 0))
check('(1) symbolic residue: -2 pi i Res = pi i/(k^+ (m^2 + P kT^2/k^+))',
      sp.simplify(I_sym - sp.pi*sp.I/(kp*(m2 + P*kT2/kp))) == 0, I_sym)

# (2) transverse integral in 2-2eps dimensions (radial form) vs closed form, numerically
mp.mp.dps = 30
for epsv in [mp.mpf('0.3'), mp.mpf('0.17')]:
    a, Pv = mp.mpf('0.7'), mp.mpf('1.3')
    d = 2 - 2*epsv
    Omega = 2*mp.pi**(d/2)/mp.gamma(d/2)
    radial = Omega*mp.quad(lambda r: r**(d-1)/(a + Pv*r**2), [0, 1, mp.inf])
    closed = mp.pi**(1-epsv)*mp.gamma(epsv)*(a/Pv)**(-epsv)/Pv
    check('(2) int d^{2-2eps}kT/(a+P kT^2) = pi^{1-eps} Gamma(eps) (a/P)^{-eps}/P at eps=%s' % mp.nstr(epsv, 3),
          abs(radial/closed - 1) < 1e-9, mp.nstr(radial/closed - 1, 3))

# (3) assembling on a window [s1, s2] in sigma = k^+/P: direct (residue form) vs printed formula
def direct(epsv, s1, s2, m2v, Pv, Ppv, mu2):
    # mu^{2eps}/(i pi^{D/2}) * int dk^+ (pi i/(k^+ e1(k0))) /(2P'k^+) * int d^{2-2eps}kT
    d = 2 - 2*epsv
    Omega = 2*mp.pi**(d/2)/mp.gamma(d/2)
    def inner(kpv):
        g = lambda r: r**(d-1)*(mp.pi/(kpv*(m2v + Pv*r**2/kpv)))/(2*Ppv*kpv)
        return Omega*mp.quad(g, [0, mp.sqrt(m2v*kpv/Pv), 1, mp.inf])
    val = mp.quad(inner, [s1*Pv, s2*Pv])
    return mu2**epsv*val/mp.pi**(2-epsv)
def printed(epsv, s1, s2, m2v, Pv, Ppv, mu2):
    Qt2 = 2*Pv*Ppv
    sig = (s1**(-epsv) - s2**(-epsv))/epsv          # int_{s1}^{s2} dsigma sigma^{-1-eps}
    return mp.gamma(1+epsv)/(epsv*Qt2)*(mu2/m2v)**epsv*sig
# for eps <= 0 the kT integral is UV divergent (int kT^{-1-2eps} dkT): the printed Gamma(eps)(a/P)^{-eps} is then its
# analytic continuation; the direct check is therefore made at eps > 0 only (two values).
for epsv in [mp.mpf('0.3'), mp.mpf('0.45')]:
    args = (epsv, mp.mpf('0.05'), mp.mpf('3.0'), mp.mpf('0.02'), mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('1.7'))
    dv, pv = direct(*args), printed(*args)
    check('(3) window [0.05,3] in sigma, eps=%s: direct residue form = printed formula' % mp.nstr(epsv, 2),
          abs(dv/pv - 1) < 1e-12, '%s vs %s' % (mp.nstr(dv, 14), mp.nstr(pv, 14)))
# divergence at both ends: int_0^1 sigma^{-1-eps} needs eps<0, int_1^inf needs eps>0
s = sp.symbols('s', positive=True); ep = sp.symbols('ep')
lo = sp.integrate(s**(-1-sp.Rational(-3, 10)), (s, 0, 1))
hi = sp.integrate(s**(-1-sp.Rational(3, 10)), (s, 1, sp.oo))
check('(3) [kT integral needs eps>0; sigma->0 end needs eps<0] int_0^1 = -1/eps (eps=-3/10 -> 10/3), int_1^oo = 1/eps (eps=3/10 -> 10/3): sum 1/eps_UV - 1/eps_IR',
      lo == sp.Rational(10, 3) and hi == sp.Rational(10, 3), (lo, hi))

print('\n=== w10_zerobin: %d PASS, %d FAIL ===' % (npass, nfail))
