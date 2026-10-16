r"""W14 -- symbolic checks of the intermediate formulas printed in sec:dy-nlo (prop:dy-nlo proof, ex:dy-nlo,
prop:dy-scale, rem:dy-dis-scheme, ex:dy-threshold) that are not themselves VERIFIED_FORMULAS entries.
Conventions: D = 4-2eps, CDR, MS-bar (S_eps = (4pi)^eps e^{-eps gamma_E}), a = alpha_s/(2pi), L = ln(mu^2/Q^2),
product convention g D_k = g(1) D_k + (g-g(1)) ln^k(1-z)/(1-z)  (WRITER_SPEC_v2 row 21).

 1. Beta-function v-integrals:  int_0^1 dv [v(1-v)]^{-eps} T_{qqbar}, T_{qg}  and the closed forms VF-DY-5.
 2. eps-expansions of K_r, K_v, cos(pi eps), f(eps); real/imaginary part of the timelike F^(1).
 3. Laurent rows (VF-DY-7) re-derived from the closed forms, the pole sum = -(2/eps) P_qq, finite parts = VF-DY-8.
 4. N=1, N=2 moments term by term; large-N limit and the Moch-Vogt constant; DIS-scheme identity; mu_F derivative.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import functools
print = functools.partial(print, flush=True)

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); LOG.append(s)

eps, z, v, L, LF = sp.symbols('epsilon z v L L_F')
CF, TF = sp.symbols('C_F T_F', positive=True)
EG = sp.EulerGamma
z2 = sp.zeta(2)


def numratio(expr, syms, pts):
    """evaluate expr (expected == 1) at the given points with 40 digits; return max |expr-1|"""
    mx = 0
    for p in pts:
        val = sp.N(expr.subs(dict(zip(syms, p))), 40)
        mx = max(mx, abs(complex(val) - 1))
    return mx
PTS = [(sp.Rational(-1, 7), sp.Rational(1, 3)), (sp.Rational(-3, 10), sp.Rational(5, 7)), (sp.Rational(-1, 20), sp.Rational(2, 9)),
       (sp.Rational(1, 9), sp.Rational(3, 5))]

# ------------------------------------------------------------------------------------------- 1. v-integrals
def vint(expr):
    """int_0^1 dv v^{-eps}(1-v)^{-eps} expr, expr a Laurent polynomial in v and (1-v): expand in monomials v^m (1-v)^n."""
    w = sp.Symbol('w')   # w = 1-v
    e = sp.expand(sp.together(expr).subs(v, 1 - w))   # not used directly; do term-wise on v and 1-v
    return None

def beta(a, b):
    return sp.gamma(a)*sp.gamma(b)/sp.gamma(a + b)

# q qbar: T = 8(1-eps)[(1-eps)((1-v)/v + v/(1-v)) + 2z/((1-z)^2 v(1-v)) - 2eps]
I_qq = 8*(1 - eps)*((1 - eps)*(beta(-eps, 2 - eps) + beta(2 - eps, -eps))
                    + 2*z/(1 - z)**2*beta(-eps, -eps) - 2*eps*beta(1 - eps, 1 - eps))
G = sp.gamma(1 - eps)**2/sp.gamma(1 - 2*eps)
I_qq_printed = -16*(1 - eps)/eps*G*(1 + z**2 + 2*eps**2*(1 - z)**2/(1 - 2*eps))/(1 - z)**2
log('1a. int dv [v(1-v)]^-eps T_qqbar  / printed closed form: max|ratio-1| =', numratio(I_qq/I_qq_printed, (eps, z), PTS))
# the three Beta functions as printed
log('    B(-eps,2-eps) * eps(1-2eps)/(-(1-eps) G): max|r-1| =', numratio(beta(-eps, 2 - eps)*eps*(1 - 2*eps)/(-(1 - eps)*G), (eps, z), PTS))
log('    B(-eps,-eps) * eps/(-2 G): max|r-1| =', numratio(beta(-eps, -eps)*eps/(-2*G), (eps, z), PTS))
log('    B(1-eps,1-eps) * (1-2eps)/G: max|r-1| =', numratio(beta(1 - eps, 1 - eps)*(1 - 2*eps)/G, (eps, z), PTS))
# q g: T = 8(1-eps)[(1-eps)(1/((1-z)(1-v)) + (1-z)(1-v)) - 2 z v/(1-v) + 2 eps]
I_qg = 8*(1 - eps)*((1 - eps)*(beta(1 - eps, -eps)/(1 - z) + (1 - z)*beta(1 - eps, 2 - eps))
                    - 2*z*beta(2 - eps, -eps) + 2*eps*beta(1 - eps, 1 - eps))
# full prefactor chain: Delta^R = g0^2 C/(8 pi (1-eps)^k) * (1/8pi)(4pi/shat)^eps (1-z)^{1-2eps}/Gamma(1-eps) * I
als, mu2, Q2 = sp.symbols('alpha_s mu2 Q2', positive=True)
g02_4pi_over_shat = 4*sp.pi*als*(mu2/Q2)**eps*z**eps*sp.exp(eps*EG)     # g0^2 (4pi/shat)^eps, shat = Q2/z
Kr = sp.exp(eps*EG)*sp.gamma(1 - eps)/sp.gamma(1 - 2*eps)
a_ = als/(2*sp.pi)
DRqq = g02_4pi_over_shat*CF/(8*sp.pi*(1 - eps))/(8*sp.pi)*(1 - z)**(1 - 2*eps)/sp.gamma(1 - eps)*I_qq
DRqq_vf = -a_*2*CF/eps*(mu2/Q2)**eps*Kr*z**eps*(1 - z)**(-1 - 2*eps)*(1 + z**2 + 2*eps**2*(1 - z)**2/(1 - 2*eps))
DRqg = g02_4pi_over_shat*TF/(8*sp.pi*(1 - eps)**2)/(8*sp.pi)*(1 - z)**(1 - 2*eps)/sp.gamma(1 - eps)*I_qg
DRqg_vf = -a_*TF/(2*eps)*(mu2/Q2)**eps*Kr*z**eps*(1 - z)**(-2*eps)*(2*(z**2 + (1 - z)**2) - eps*(5*z**2 - 6*z + 7)
                                                                    + eps**2*(1 + z)**2)/((1 - eps)*(1 - 2*eps))
log('1b. Delta^R_qqbar (matrix element x phase space) / VF-DY-5: max|r-1| =', numratio((DRqq/DRqq_vf).subs({als: 1, mu2: 3, Q2: 2, CF: sp.Rational(4,3)}), (eps, z), PTS))
log('1c. Delta^R_qg    (matrix element x phase space) / VF-DY-5: max|r-1| =', numratio((DRqg/DRqg_vf).subs({als: 1, mu2: 3, Q2: 2, TF: sp.Rational(1,2)}), (eps, z), PTS))
# averaging factors -> prefactors g0^2 C_F/(8 pi (1-eps)) and g0^2 T_F/(8 pi (1-eps)^2)
Nc, eq2, g02 = sp.symbols('N_c e_q2 g0sq', positive=True)
avg_qq = sp.Rational(1, 4)/Nc**2*eq2*g02*CF*Nc               # <-gHH*> / T_qqbar
avg_qg = sp.Rational(1, 2)/(2*(1 - eps))/(Nc*(Nc**2 - 1))*eq2*g02*TF*(Nc**2 - 1)
norm = Nc/(2*sp.pi*eq2*(1 - eps))
log('1d. prefactors: qqbar', sp.simplify(norm*avg_qq), ' ; qg', sp.simplify(norm*avg_qg))

# ------------------------------------------------------------------------------------------- 2. expansions
Kv = sp.exp(eps*EG)*sp.gamma(1 + eps)*sp.gamma(1 - eps)**2/sp.gamma(1 - 2*eps)
f = -Kv*(2 - eps + 2*eps**2)/(eps**2*(1 - 2*eps))
log('2a. K_r =', sp.series(Kr, eps, 0, 3).removeO().subs(sp.zeta(2), z2), ' ; K_v =', sp.series(Kv, eps, 0, 3).removeO())
log('    cos(pi eps) =', sp.series(sp.cos(sp.pi*eps), eps, 0, 3).removeO(), ' ; f(eps) =', sp.series(f, eps, 0, 1).removeO())
ImF = sp.series(sp.exp(eps*L)*sp.sin(sp.pi*eps)*f, eps, 0, 1).removeO()      # times alpha_s C_F/(4 pi)
log('2b. (4pi/(alpha_s C_F)) Im F^(1) =', sp.expand(ImF), '  => Im F^(1) = -(alpha_s C_F/2)(1/eps + L + 3/2) + O(eps):',
    sp.simplify(sp.expand(ImF) - (-2*sp.pi/eps - 2*sp.pi*L - 3*sp.pi)) == 0)
ReF = sp.series(sp.exp(eps*L)*sp.cos(sp.pi*eps)*f, eps, 0, 1).removeO()
log('2c. virtual row (units a C_F): eps^-2, eps^-1, eps^0 =', [sp.simplify(ReF.coeff(eps, k)) for k in (-2, -1, 0)])

# ------------------------------------------------------------------------------------------- 3. Laurent rows
# represent distributions symbolically: delta, D0, D1, plus regular functions; real qqbar row:
# (-2 C_F/eps) e^{eps L} K_r z^eps (1-z)^{-1-2eps} [1+z^2+O(eps^2)],  (1-z)^{-1-2eps} = -delta/(2eps) + D0 - 2eps D1 + ...
delta, D0, D1 = sp.symbols('delta D0 D1')
pre = sp.series(sp.exp(eps*L)*Kr, eps, 0, 3).removeO()
# delta part: z^eps(1+z^2+2eps^2(1-z)^2/(1-2eps)) at z=1 -> 2
row_delta = sp.expand(sp.series((-2*CF/eps)*pre*(-1/(2*eps))*2, eps, 0, 1).removeO())
# D0 and D1 parts with the product convention; g(z) = z^eps (1+z^2) (the eps^2 term is O(eps^2) x (1-z)^2: regular, no pole)
g0 = 1 + z**2
gz = (1 + eps*sp.log(z))*g0                       # z^eps(1+z^2) to O(eps)
# g D0 = g(1) D0 + (g - g(1))/(1-z);  g D1 similar
def times_D(gfun, k):
    g1 = gfun.subs(z, 1)
    return g1*(D0 if k == 0 else D1) + sp.simplify((gfun - g1)/(1 - z))*sp.log(1 - z)**k
row_D = sp.expand((-2*CF/eps)*(1 + eps*L)*(times_D(gz, 0) - 2*eps*times_D(g0, 1)))
row_D = sp.expand(sp.series(row_D, eps, 0, 1).removeO())
real_row = sp.expand(row_delta*delta + row_D)
log('3a. real qqbar row: eps^-2:', sp.simplify(real_row.coeff(eps, -2)), '; eps^-1:', sp.simplify(real_row.coeff(eps, -1)))
log('    eps^0:', sp.simplify(real_row.coeff(eps, 0)))
vf_real0 = CF*(L**2 - sp.pi**2/2)*delta - 4*CF*L*D0 + 8*CF*D1 + 2*CF*(1 + z)*L - 4*CF*(1 + z)*sp.log(1 - z) \
    - 2*CF*(1 + z**2)/(1 - z)*sp.log(z)
log('    eps^0 - VF-DY-7 =', sp.simplify(real_row.coeff(eps, 0) - vf_real0))
virt_row = sp.expand(CF*ReF*delta)
Pqq = CF*(2*D0 - (1 + z) + sp.Rational(3, 2)*delta)
def lcoef(expr, k, zv):
    e = sp.expand(sp.series(sp.expand(expr).subs(z, zv), eps, 0, 1).removeO())
    return sp.simplify(e.coeff(eps, k))
for zv in (sp.Rational(3, 7), sp.Rational(2, 9)):
    m2 = lcoef(real_row + virt_row, -2, zv); m1 = lcoef(real_row + virt_row, -1, zv)
    log('3b. z=%s: real+virtual eps^-2 =' % zv, m2, '; eps^-1 + 2 P_qq =', sp.simplify(m1 + 2*Pqq.subs(z, zv)),
        '; real eps^-1 =', lcoef(real_row, -1, zv), ' expected 2C_F L delta - 4C_F D0 + 2C_F(1+z) =', sp.simplify((2*CF*L*delta - 4*CF*D0 + 2*CF*(1 + z)).subs(z, zv)))
ct = sp.expand(2*(1/eps + (L + LF))*Pqq)        # (2/eps)(mu^2/mu_F^2)^eps P_qq,  ln(mu^2/mu_F^2) = L + L_F
fin = sp.expand(real_row.coeff(eps, 0) + virt_row.coeff(eps, 0) + ct.coeff(eps, 0))
target = CF*(8*D1 - 4*(1 + z)*sp.log(1 - z) - 2*(1 + z**2)/(1 - z)*sp.log(z) + (2*sp.pi**2/3 - 8)*delta) + 2*Pqq*LF
log('3c. finite qqbar - VF-DY-8 (8 D1 - 4(1+z)ln(1-z) = 4(1+z^2)D1) =', sp.simplify(fin - target))
log('    delta coefficient pieces: real', sp.simplify(real_row.coeff(eps, 0).coeff(delta)), ' virtual', sp.simplify(virt_row.coeff(eps, 0).coeff(delta)),
    ' counterterm', sp.simplify(ct.coeff(eps, 0).coeff(delta)))
# qg row
Nqg = 2*(z**2 + (1 - z)**2) - eps*(5*z**2 - 6*z + 7) + eps**2*(1 + z)**2
qg = (-TF/(2*eps))*(1 + eps*L)*(1 + eps*sp.log(z))*(1 - 2*eps*sp.log(1 - z))*Nqg*(1 + 3*eps)
qg = sp.expand(sp.series(sp.expand(qg), eps, 0, 1).removeO())
Pqg = TF*(z**2 + (1 - z)**2)
log('3d. real qg: eps^-1 + P_qg =', sp.simplify(qg.coeff(eps, -1) + Pqg))
qg_fin = sp.expand(qg.coeff(eps, 0) + Pqg*(L + LF))
qg_target = TF*((z**2 + (1 - z)**2)*sp.log((1 - z)**2/z) + sp.Rational(1, 2) + 3*z - sp.Rational(7, 2)*z**2) + Pqg*LF
log('    finite qg - VF-DY-8 =', sp.simplify(sp.expand_log(qg_fin - qg_target, force=True)))
log('    1/((1-eps)(1-2eps)) =', sp.series(1/((1 - eps)*(1 - 2*eps)), eps, 0, 2).removeO())

# ------------------------------------------------------------------------------------------- 4. moments etc.
x = sp.symbols('x')
mp.mp.dps = 30
def mom_terms_qq(N):
    h = lambda s: s**(N - 1)
    t1 = 4*mp.quad(lambda s: ((1 + s**2)*h(s) - 2)*mp.log(1 - s)/(1 - s), [0, 1])
    t2 = -2*mp.quad(lambda s: (1 + s**2)*mp.log(s)/(1 - s)*h(s), [0, 1])
    t3 = 2*mp.pi**2/3 - 8
    return t1, t2, t3
for N, exact in ((1, 8*mp.zeta(2) - mp.mpf(7)/2), (2, 8*mp.zeta(2) + mp.mpf(13)/18)):
    t1, t2, t3 = mom_terms_qq(N)
    log('4a. N=%d qqbar terms: %s %s %s ; sum - VF-DY-14 = %s ; x C_F = %s' % (N, mp.nstr(t1, 15), mp.nstr(t2, 15), mp.nstr(t3, 15),
        mp.nstr(t1 + t2 + t3 - exact, 3), mp.nstr(mp.mpf(4)/3*(t1 + t2 + t3), 12)))
    if N == 1:
        log('    N=1 term checks: t1-7 =', mp.nstr(t1 - 7, 3), ' t2-(4 zeta2-5/2) =', mp.nstr(t2 - (4*mp.zeta(2) - mp.mpf(5)/2), 3))
    hq = lambda s: s**(N - 1)
    q1 = mp.quad(lambda s: (s**2 + (1 - s)**2)*2*mp.log(1 - s)*hq(s), [0, 1])
    q2 = mp.quad(lambda s: -(s**2 + (1 - s)**2)*mp.log(s)*hq(s), [0, 1])
    q3 = mp.quad(lambda s: (mp.mpf(1)/2 + 3*s - mp.mpf(7)/2*s**2)*hq(s), [0, 1])
    log('    N=%d qg terms (units T_F): %s %s %s ; sum = %s' % (N, mp.nstr(q1, 12), mp.nstr(q2, 12), mp.nstr(q3, 12), mp.nstr(q1 + q2 + q3, 15)))
log('    N=1 qg exact terms: -13/9, 13/18, 5/6 ->', mp.nstr(-mp.mpf(13)/9, 12), mp.nstr(mp.mpf(13)/18, 12), mp.nstr(mp.mpf(5)/6, 12), ' sum 1/9 =', mp.nstr(mp.mpf(1)/9, 12))
# large N: <D0, z^{N-1}> = -S1(N-1), <D1, z^{N-1}> = (S1(N-1)^2 + S2(N-1))/2, int z^{N-1} ln z/(1-z) = -psi'(N)
mp.mp.dps = 30
def S1(n): return mp.harmonic(n)
def S2(n): return mp.zeta(2) - mp.zeta(2, n + 1)
for N in (3, 7):
    hz = lambda t: t**(N - 1)
    d0 = mp.quad(lambda t: (hz(t) - 1)/(1 - t), [0, 1]); d1 = mp.quad(lambda t: (hz(t) - 1)*mp.log(1 - t)/(1 - t), [0, 1])
    lz = mp.quad(lambda t: hz(t)*mp.log(t)/(1 - t), [0, 1])
    log('4b. N=%d: <D0>+S1 = %s ; <D1>-(S1^2+S2)/2 = %s ; int z^(N-1) ln z/(1-z) + psi1(N) = %s' % (N, mp.nstr(d0 + S1(N - 1), 3),
        mp.nstr(d1 - (S1(N - 1)**2 + S2(N - 1))/2, 3), mp.nstr(lz + mp.psi(1, N), 3)))
CFn = mp.mpf(4)/3
for N in (10, 100, 1000, 10000):
    exact = CFn*(2*(S1(N - 1)**2 + S2(N - 1) + S1(N + 1)**2 + S2(N + 1)) + 2*(mp.psi(1, N) + mp.psi(1, N + 2)) + 4*mp.zeta(2) - 8)
    lnNb = mp.log(N) + mp.euler
    asym = CFn*(4*lnNb**2 + 8*mp.zeta(2) - 8)
    lead = 4*CFn*lnNb/N
    log('4g. N=%5d: Delta^(1)_N = %s ; asymptotic = %s ; diff/(4 C_F ln Nbar/N) = %s' % (N, mp.nstr(exact, 12), mp.nstr(asym, 12), mp.nstr((exact - asym)/lead, 6)))
# Moch-Vogt: 2*C_F[4 ln^2 Nbar + 8 zeta2 - 8] = C_F[8 ln^2 N + 16 gamma_E ln N + (-16 + 16 zeta2 + 8 gamma_E^2)]
lnN = sp.symbols('lnN')
mv = sp.expand(2*(4*(lnN + EG)**2 + 8*z2 - 8) - (8*lnN**2 + 16*EG*lnN + (-16 + 16*z2 + 8*EG**2)))
log('4c. Moch-Vogt constant g01 = C_F(-16+16 zeta2+8 gamma_E^2) reproduced (a_s = alpha_s/4pi):', sp.simplify(mv) == 0)
# DIS scheme identity on the distribution basis
C2q = CF*(2*D1 - sp.Rational(3, 2)*D0 - (1 + z)*sp.log(1 - z) - (1 + z**2)/(1 - z)*sp.log(z) + 3 + 2*z
          - (sp.Rational(9, 2) + sp.pi**2/3)*delta)
C2g = TF*((z**2 + (1 - z)**2)*sp.log((1 - z)/z) - 8*z**2 + 8*z - 1)
DMSqq = CF*(8*D1 - 4*(1 + z)*sp.log(1 - z) - 2*(1 + z**2)/(1 - z)*sp.log(z) + (2*sp.pi**2/3 - 8)*delta)
DMSqg = TF*((z**2 + (1 - z)**2)*sp.log((1 - z)**2/z) + sp.Rational(1, 2) + 3*z - sp.Rational(7, 2)*z**2)
DDISqq = CF*((1 + 4*sp.pi**2/3)*delta + (4*D1 - 2*(1 + z)*sp.log(1 - z)) + 3*D0 - 6 - 4*z)   # 2(1+z^2)D1 = 4D1 - 2(1+z)ln(1-z)
DDISqg = TF*((z**2 + (1 - z)**2)*sp.log(1 - z) + sp.Rational(3, 2) - 5*z + sp.Rational(9, 2)*z**2)
log('4d. Delta^MS_qq - 2C_2^q - Delta^DIS_qq =', sp.simplify(sp.expand(DMSqq - 2*C2q - DDISqq)),
    ' ; Delta^MS_qg - C_2^g - Delta^DIS_qg =', sp.simplify(sp.expand_log(DMSqg - C2g - DDISqg, force=True)))
# whole-term plus: 4 C_F (1+z^2) D1 = 4 C_F [(1+z^2)ln(1-z)/(1-z)]_+ + 7 C_F delta
log('4e. -int_0^1 (1+z) ln(1-z) dz =', sp.integrate(-(1 + z)*sp.log(1 - z), (z, 0, 1)))
# 4-dim Born normalization: (1-eps) * (-(2/eps) P_qq) = -(2/eps)P_qq + 2 P_qq
log('4f. (1-eps)(-2/eps) expansion:', sp.expand((1 - eps)*(-2/eps)))

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'p7_checks.log'), 'w').write('\n'.join(LOG) + '\n')
