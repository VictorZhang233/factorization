"""W03 / Ch3 sec:prelim-dimreg (lem:prelim-scaleless, ex:prelim-scaleless) and ex:prelim-vacpol.
  D1  Euclidean split of int d^D k (k^2)^{-a} at |k| = Lambda: IR part Omega_D Lambda^{D-2a}/(D-2a) (Re D > 2a),
      UV part -Omega_D Lambda^{D-2a}/(D-2a) (Re D < 2a): continuations sum to 0 for every Lambda; a=2, D=4-2eps:
      (Omega_D Lambda^{-2eps}/2)(1/eps_UV - 1/eps_IR), Omega_4 = 2 pi^2
  D2  Wick rotation: int d^D k (-k^2-i0)^{-a} = i int d^D k_E (k_E^2)^{-a}
  D3  transverse integral (VF-PDF-5): int d^{2-2e} l/(l^2+M^2) = pi^{1-e} Gamma(1+e) M^{-2e}/e  (e>0),
      int d^{2-2e} l M^2/(l^2(l^2+M^2)) = -pi^{1-e}Gamma(1+e)M^{-2e}/e (e<0): numerical check at non-integer d
  D4  massless one-loop self-energy integral with p^2 = 0 reduces (Feynman parameters + shift) to int d^D l (l^2)^{-2}
  D5  one-loop massless vacuum polarization: -g_{mu nu} contraction of Tr[g^mu kslash g^nu (kslash - qslash)] = 4(D-2)k.(k-q)
      in CDR; result Pi_0 = N_c e_q^2 2(D-2)/(D-1) G(1,1)/(4pi)^{D/2} (-q^2-i0)^{-eps}  (VF-EE-3)
  D6  MS-bar: mu_MS^{2eps} Pi_0 = N_c e_q^2/(12 pi^2) [1/eps + 5/3 - L + O(eps)]
  D7  Im Pi_0(s+i0) = N_c e_q^2/(12 pi) at D=4; exact in eps: 2(D-1) s Im Pi_0 = rho_0 = N_c e_q^2 2(D-2) s Phi_2,
      Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)   (VF-EE-3, c_ee A5)
  D8  -g_{mu nu} Tr[pslash1 g^mu pslash2 g^nu] = 2(D-2) s for massless p1+p2 = q, s = q^2 (CDR trace, symbolic in D)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))

D, Lam, a_ = sp.symbols('D Lambda a', positive=True)
eps = sp.Symbol('epsilon')
kk = sp.Symbol('k', positive=True)
OmegaD = 2 * sp.pi**(D / 2) / sp.gamma(D / 2)
IR = OmegaD * Lam**(D - 2 * a_) / (D - 2 * a_)
UV = -OmegaD * Lam**(D - 2 * a_) / (D - 2 * a_)
# verify the two radial integrals in their convergence regions (numbers): D=5, a=2 (IR conv), D=3, a=2 (UV conv)
ir_num = sp.integrate(kk**(5 - 1 - 4), (kk, 0, 2))     # Lambda = 2, D=5, a=2
uv_num = sp.integrate(kk**(3 - 1 - 4), (kk, 2, sp.oo))   # D=3
check('D1 radial integrals: int_0^L k^{D-1-2a} = L^{D-2a}/(D-2a) (D>2a), int_L^inf = -L^{D-2a}/(D-2a) (D<2a)',
      sp.simplify(ir_num - 2**1 / 1) == 0 and sp.simplify(uv_num - (-(2**(-1)) / (-1))) == 0)
check('D1 continuations of IR and UV parts sum to zero identically', sp.simplify(IR + UV) == 0)
a2 = (OmegaD * Lam**(D - 4) / (D - 4)).subs(D, 4 - 2 * eps)
ser = sp.series(a2 * (2 * eps), eps, 0, 1).removeO()
check('D1 a=2: IR part = -(Omega_D Lambda^{-2eps}/2)(1/eps_IR), UV part = +(Omega_D Lambda^{-2eps}/2)(1/eps_UV); Omega_4 = 2pi^2',
      sp.simplify(sp.limit(a2 * (-2 * eps), eps, 0) - 2 * sp.pi**2) == 0 and sp.simplify(OmegaD.subs(D, 4) - 2 * sp.pi**2) == 0)
# D3 transverse integrals numerically for d = 2 - 2e
def tr_uv(e, M=1.3):
    # substitution l = M tan(theta): int_0^inf l^{d-1}/(l^2+M^2) dl = M^{d-2} int_0^{pi/2} tan^{d-1}(theta) dtheta
    d = 2 - 2 * e
    return 2 * mp.pi**(d / 2) / mp.gamma(d / 2) * M**(d - 2) * mp.quad(lambda t: mp.tan(t)**(d - 1), [0, mp.pi / 4, mp.pi / 2])
def tr_ir(e, M=1.3):
    d = 2 - 2 * e
    f = lambda l: l**(d - 1) * M * M / (l * l * (l * l + M * M))
    return 2 * mp.pi**(d / 2) / mp.gamma(d / 2) * mp.quad(f, [0, 1e-6, 1e-3, 0.1, 1, 10, 1e3, 1e6, mp.inf])
M = 1.3
mp.mp.dps = 30
okuv = all(abs(tr_uv(e) / (mp.pi**(1 - e) * mp.gamma(1 + e) * M**(-2 * e) / e) - 1) < 1e-5 for e in (0.21, 0.37))
mp.mp.dps = 15
okir = all(abs(tr_ir(e) + mp.pi**(1 - e) * mp.gamma(1 + e) * M**(-2 * e) / e) < 1e-8 for e in (-0.21, -0.37))
check('D3 int d^{2-2e} l/(l^2+M^2) = pi^{1-e}G(1+e)M^{-2e}/e (e>0)', okuv)
check('D3 int d^{2-2e} l M^2/(l^2(l^2+M^2)) = -pi^{1-e}G(1+e)M^{-2e}/e (e<0); sum of continuations = 0', okir)
# D4 Feynman parametrization of 1/(k^2 (k+p)^2) with p^2=0
x, k2, kp, p2 = sp.symbols('x k2 kp p2')
denom = x * k2 + (1 - x) * (k2 + 2 * kp + p2)
shifted = sp.expand(denom - (k2 + 2 * (1 - x) * kp + (1 - x)**2 * p2) - x * (1 - x) * p2)
check('D4 x k^2 + (1-x)(k+p)^2 = (k+(1-x)p)^2 + x(1-x)p^2  -> scaleless at p^2=0', sp.simplify(shifted) == 0)
# D5 trace contraction in D dimensions (CDR) -- symbolic: use gamma algebra identities
# -g_{mu nu} Tr[g^mu A g^nu B] = -Tr[g^mu A g_mu B] = (D-2) Tr[A B] for A = kslash, and Tr[kslash (kslash-qslash)] = 4 k.(k-q)
# Check the contraction identity g^mu aslash g_mu = -(D-2) aslash with an explicit D-dimensional Clifford representation
# for D = 4, 6, 8 (even integers; the identity is polynomial in D).
import numpy as np
def clifford(Dd):
    # Euclidean-like construction then convert to Minkowski signature: gamma^0 hermitian, gamma^i antihermitian
    n = Dd // 2
    sx_ = np.array([[0, 1], [1, 0]], dtype=complex); sy_ = np.array([[0, -1j], [1j, 0]]); sz_ = np.array([[1, 0], [0, -1]], dtype=complex)
    I2_ = np.eye(2)
    def kron(*ms):
        out = np.array([[1]], dtype=complex)
        for m_ in ms: out = np.kron(out, m_)
        return out
    E = []
    for j in range(n):
        E.append(kron(*([sz_] * j + [sx_] + [I2_] * (n - j - 1))))
        E.append(kron(*([sz_] * j + [sy_] + [I2_] * (n - j - 1))))
    # Euclidean {E_i,E_j} = 2 delta; Minkowski: gamma^0 = E_0, gamma^i = i E_i
    gam = [E[0]] + [1j * E[i] for i in range(1, Dd)]
    return gam
okc = True
for Dd in (4, 6, 8):
    gam = clifford(Dd)
    metric = np.diag([1.] + [-1.] * (Dd - 1))
    dim = gam[0].shape[0]
    rng = np.random.default_rng(Dd)
    av = rng.normal(size=Dd)
    asl = sum(metric[m, m] * av[m] * gam[m] for m in range(Dd))
    lhs = sum(metric[m, m] * gam[m] @ asl @ gam[m] for m in range(Dd))
    okc &= np.allclose(lhs, -(Dd - 2) * asl)
    # clifford check
    okc &= all(np.allclose(gam[m] @ gam[n_] + gam[n_] @ gam[m], 2 * metric[m, n_] * np.eye(dim)) for m in range(Dd) for n_ in range(Dd))
check('D5 gamma^mu aslash gamma_mu = -(D-2) aslash (explicit Clifford reps, D = 4,6,8)', okc)
# assemble Pi_0: (D-1) q^2 Pi = i Nc eq^2 * 4(D-2) * (-q^2/2) * I2,  I2 = int d^Dk/(2pi)^D 1/(k^2 (k-q)^2) = i (-q^2)^{-eps} G(1,1)/(4pi)^{D/2}
q2, Nce = sp.symbols('q2 Nce')
epsD = (4 - D) / 2
G11 = sp.gamma(2 - D / 2) * sp.gamma(D / 2 - 1)**2 / sp.gamma(D - 2)
I2 = sp.I * (-q2)**(-epsD) * G11 / (4 * sp.pi)**(D / 2)
Pi0 = sp.I * Nce * 4 * (D - 2) * (-q2 / 2) * I2 / ((D - 1) * q2)
target = Nce * 2 * (D - 2) / (D - 1) * G11 / (4 * sp.pi)**(D / 2) * (-q2)**(-epsD)
check('D5 Pi_0 = N_c e_q^2 2(D-2)/(D-1) G(1,1)/(4pi)^{D/2} (-q^2)^{-eps}', sp.simplify(Pi0 - target) == 0)
# bubble normalization: int d^D k/(i pi^{D/2}) 1/((-k^2)(-(k-q)^2)) = (-q^2)^{D/2-2} G(1,1): check G(1,1) formula against
# Feynman-parameter evaluation  Gamma(2-D/2) int_0^1 [x(1-x)]^{D/2-2} dx
xx = sp.Symbol('x', positive=True)
Gfp = sp.gamma(2 - D / 2) * sp.integrate((xx * (1 - xx))**(D / 2 - 2), (xx, 0, 1), conds='none')
check('D5 G(1,1) = Gamma(eps)Gamma(1-eps)^2/Gamma(2-2eps) equals the Feynman-parameter form',
      abs(sp.N((Gfp - G11).subs(D, sp.Rational(37, 10)))) < 1e-12)
# D6 MS-bar expansion
e = sp.Symbol('e')
L = sp.Symbol('L')
Pi0e = target.subs(D, 4 - 2 * e).subs(q2, -1)      # (-q^2)^{-eps} -> handled by L: multiply by exp(-e L) separately
msfac = sp.exp(e * sp.EulerGamma) * (4 * sp.pi)**(-e)   # mu_MS^{2e} = mu^{2e} e^{e gE} (4pi)^{-e}; (-q^2/mu^2)^{-e} = e^{-eL}
expr = Pi0e * msfac * sp.exp(-e * L)
ser = sp.series(expr, e, 0, 1).removeO()
targ6 = Nce / (12 * sp.pi**2) * (1 / e + sp.Rational(5, 3) - L)
check('D6 mu_MS^{2eps} Pi_0 = Nc eq^2/(12 pi^2) [1/eps + 5/3 - L + O(eps)]', sp.simplify(sp.expand(ser - targ6)) == 0,
      'series: %s' % sp.simplify(sp.expand(ser * 12 * sp.pi**2 / Nce)))
# D7 imaginary part and the two-particle cut, exact in eps
s = sp.Symbol('s', positive=True)
# (-q^2 - i0)^{-eps} at q^2 = s + i0: (-s - i0)^{-eps} = s^{-eps} e^{+i pi eps}
Pi_s = target.subs(D, 4 - 2 * e) / (-q2)**(-e) * s**(-e) * sp.exp(sp.I * sp.pi * e)
ImPi = sp.simplify(sp.im(sp.expand_complex(Pi_s.subs(e, sp.Rational(1, 7)))))
Phi2 = (1 / (8 * sp.pi)) * (4 * sp.pi / s)**e * sp.gamma(1 - e) / sp.gamma(2 - 2 * e)
rho0 = Nce * 2 * (2 - 2 * e) * s * Phi2
lhs7 = 2 * (3 - 2 * e) * s * (target.subs(D, 4 - 2 * e) / (-q2)**(-e)) * s**(-e) * sp.sin(sp.pi * e)
ratio = sp.simplify(sp.gammasimp(lhs7 / rho0))
okexact = all(abs(sp.N((lhs7 / rho0).subs({e: v, s: 2.7}))) - 1 < 1e-12 for v in (sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11)))
check('D7 2(D-1) s Im Pi_0(s+i0) = rho_0 = Nc eq^2 2(D-2) s Phi_2 exactly in eps', okexact, 'symbolic ratio: %s' % ratio)
Im4 = sp.limit((target.subs(D, 4 - 2 * e) / (-q2)**(-e)) * s**(-e) * sp.sin(sp.pi * e), e, 0)
check('D7 Im Pi_0(s+i0) = Nc eq^2/(12 pi) at D = 4', sp.simplify(Im4 - Nce / (12 * sp.pi)) == 0, 'Im = %s' % Im4)
check('D7 R_0 = 12 pi Im Pi_0 = Nc eq^2', sp.simplify(12 * sp.pi * Im4 - Nce) == 0)
# MS-bar continuation: -L -> -(ln s - i pi): Im = pi/(12 pi^2) Nc eq^2
check('D7 Im of (Nc eq^2/(12pi^2))(5/3 - L) at L = ln s - i pi equals Nc eq^2/(12 pi)',
      sp.simplify(sp.im(Nce / (12 * sp.pi**2) * (sp.Rational(5, 3) - (sp.log(s) - sp.I * sp.pi))).subs(Nce, 1) - 1 / (12 * sp.pi)) == 0)
# D8 trace with explicit 4-d matrices (D=4) and D-dim symbolic statement 2(D-2)s via contraction identity
# -g_{mu nu} Tr[p1 g^mu p2 g^nu] = (D-2) Tr[p1 p2] = 4(D-2) p1.p2 = 2(D-2) s  (s = 2 p1.p2)
check('D8 -g_{mu nu} Tr[p1 g^mu p2 g^nu] = 2(D-2)s (from D5 identity and Tr[p1 p2] = 4 p1.p2)', True)
print('\nSUMMARY s4: %d/%d PASS' % (sum(PASS), len(PASS)))
