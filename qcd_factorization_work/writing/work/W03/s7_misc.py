"""W03 misc checks for Ch3 text:
  H1  Hilbert matrix condition numbers cond_2(H_K), K = 5, 10, 20 (VF-MISC-2: 4.8e5 at K=5, 2.5e28 at K=20), slope ~ e^{3.5K}
  H2  sin(Q^2 x): |Q^2 int_0^1 x^n sin(Q^2 x) dx| bounded uniformly in Q for fixed n (VF-MISC-3)
  Q1  one-loop massless quark self-energy, Feynman gauge (ex:prelim-scaleless (i)):
        Sigma_V(p^2) = -(alpha_s C_F/4pi)(1-eps) e^{eps gE} Gamma(eps)Gamma(1-eps)^2/Gamma(2-2eps) (mu^2/(-p^2))^eps
                     = -(alpha_s C_F/4pi)[1/eps + 1 + ln(mu^2/(-p^2)) + O(eps)]
      derived independently with Feynman parameters (Sigma = p-slash * B-coefficient) and compared
  Q2  Mellin numbers: <D_0, z> = -1, <D_1, z> = 1 (N=2); large-N asymptotics numbers at N=100
  Q3  Phi_2 (two-body phase space in D dims) from the explicit angular integral
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))
mp.mp.dps = 80
conds = {}
for K in (5, 10, 20):
    H = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            H[i, j] = mp.mpf(1) / (i + j + 1)
    ev = mp.eigsy(H)[0]
    conds[K] = max(ev) / min(ev)
ok = abs(conds[5] / mp.mpf('4.766e5') - 1) < 0.01 and abs(conds[20] / mp.mpf('2.45e28') - 1) < 0.05
rate = (mp.log(conds[20]) - mp.log(conds[10])) / 10
check('H1 cond_2(H_K): K=5 %.3e, K=10 %.3e, K=20 %.3e; growth rate per unit K = %.3f' % (conds[5], conds[10], conds[20], rate), ok)
mp.mp.dps = 20
okh = True
for n in (0, 2, 5):
    vals = [abs(Q**2 * mp.quad(lambda x: x**n * mp.sin(Q**2 * x), mp.linspace(0, 1, 60))) for Q in (3, 6, 12, 24)]
    okh &= max(vals) < 2 + n
check('H2 sin(Q^2 x): Q^2 * moments bounded uniformly in Q (n = 0, 2, 5)', okh)
# Q1 self-energy via Feynman parameters
e = sp.Symbol('epsilon'); x = sp.Symbol('x', positive=True); D = 4 - 2 * e
# -i Sigma = (ig)^2 C_F int d^Dl/(2pi)^D gamma^mu i(pslash - lslash) gamma_mu (-i)/((p-l)^2 l^2)
#          = g^2 C_F (D-2) int (pslash - lslash)/((p-l)^2 l^2)
# Feynman: 1/(l^2 (p-l)^2) = int_0^1 dx 1/[(l - x p)^2 + x(1-x) p^2]^2 ; shift l = l' + x p: pslash - lslash -> (1-x) pslash
# int d^Dl'/(2pi)^D 1/(l'^2 - Delta)^2 = i/(4pi)^{D/2} Gamma(eps) Delta^{-eps}, Delta = -x(1-x)p^2
# => -i Sigma = g^2 C_F (D-2) pslash int dx (1-x) i/(4pi)^{D/2} Gamma(eps) (-x(1-x) p^2)^{-eps}
g2, CF, mp2 = sp.symbols('g2 C_F mp2', positive=True)     # mp2 = -p^2 > 0
# int_0^1 (1-x) (x(1-x))^{-eps} dx = int x^{-eps} (1-x)^{1-eps} dx = B(1-eps, 2-eps) (checked by quadrature below)
Ix = sp.gamma(1 - e) * sp.gamma(2 - e) / sp.gamma(3 - 2 * e)
for v in (0.13, -0.21):
    assert abs(mp.quad(lambda xx: xx**(-v) * (1 - xx)**(1 - v), [0, 1]) - float(Ix.subs(e, v))) < 1e-12
SigmaV = -(g2 * CF * (D - 2) * Ix / (4 * sp.pi)**(D / 2) * sp.gamma(e) * mp2**(-e))   # Sigma = pslash * SigmaV
# MS-bar: g2 = 4 pi alpha mu^{2e} e^{e gE} (4pi)^{-e}
al, mu2 = sp.symbols('alpha mu2', positive=True)
SigmaV_ms = SigmaV.subs(g2, 4 * sp.pi * al * mu2**e * sp.exp(e * sp.EulerGamma) * (4 * sp.pi)**(-e))
target = -(al * CF / (4 * sp.pi)) * (1 - e) * sp.exp(e * sp.EulerGamma) * sp.gamma(e) * sp.gamma(1 - e)**2 / sp.gamma(2 - 2 * e) * (mu2 / mp2)**e
okq = all(abs(sp.N((SigmaV_ms / target).subs({e: v, al: 0.3, CF: sp.Rational(4, 3), mu2: 2.0, mp2: 1.7})) - 1) < 1e-12
          for v in (sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11)))
ser = sp.series(target.subs({mu2: 1, mp2: 1}) * (4 * sp.pi) / (al * CF), e, 0, 1).removeO()
okser = sp.simplify(ser - (-(1 / e + 1))) == 0
check('Q1 Sigma_V = -(a C_F/4pi)(1-eps) e^{eps gE} G(1,1) (mu^2/(-p^2))^eps (independent Feynman-parameter derivation)', okq)
check('Q1 expansion: Sigma_V = -(a C_F/4pi)[1/eps + 1 + ln(mu^2/(-p^2)) + O(eps)]', okser, 'series (mu^2=-p^2): %s' % ser)
# Q2 Mellin numbers
z = sp.Symbol('z', positive=True)
u = sp.Symbol('u', positive=True)   # u = 1 - z (avoids a sympy branch bug for log(1-z) with positive z)
d0 = sp.integrate(sp.cancel((z - 1) / (1 - z)), (z, 0, 1)); d1 = sp.integrate(sp.cancel(sp.log(u) * (-u) / u), (u, 0, 1))
mp.mp.dps = 30
N = mp.mpf(100)
S1 = mp.digamma(N) + mp.euler; S2 = mp.zeta(2) - mp.psi(1, N)
check('Q2 N=2: <D_0,z> = -1, <D_1,z> = 1; N=100: -S_1(99) = %.6f vs -ln Nbar = %.6f; (S1^2+S2)/2 = %.5f vs (ln^2 Nbar + z2)/2 = %.5f'
      % (-S1, -(mp.log(N) + mp.euler), (S1**2 + S2) / 2, ((mp.log(N) + mp.euler)**2 + mp.zeta(2)) / 2),
      sp.simplify(d0 + 1) == 0 and sp.simplify(d1 - 1) == 0)
# Q3 Phi_2
s = sp.Symbol('s', positive=True)
# Phi_2 = int d^{D-1}p/((2pi)^{D-1} 4E^2) 2pi delta(sqrt s - 2E) = Omega_{D-1} E^{D-2}/(2pi)^{D-2} * 1/(4E^2) * (1/2), E = sqrt(s)/2
OmD1 = 2 * sp.pi**((D - 1) / 2) / sp.gamma((D - 1) / 2)
E = sp.sqrt(s) / 2
Phi2 = OmD1 * E**(D - 2) / (2 * sp.pi)**(D - 2) / (4 * E**2) / 2
target3 = (1 / (8 * sp.pi)) * (4 * sp.pi / s)**e * sp.gamma(1 - e) / sp.gamma(2 - 2 * e)
okp = all(abs(sp.N((Phi2 / target3).subs({e: v, s: 3.1})) - 1) < 1e-12 for v in (sp.Rational(1, 5), sp.Rational(-1, 3)))
check('Q3 Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps) from the angular integral', okp)
print('\nSUMMARY s7: %d/%d PASS' % (sum(PASS), len(PASS)))
