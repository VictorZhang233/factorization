r"""W14 -- independent check of the O(alpha_s) Drell-Yan MS-bar coefficient functions (prop:dy-nlo, ex:dy-nlo,
prop:dy-scale, rem:dy-dis-scheme, ex:dy-threshold).  Our conventions: D=4-2eps, CDR, MS-bar with
S_eps=(4pi)^eps e^{-eps gamma_E}, a = alpha_s/(2pi), product convention g D_k = g(1) D_k + (g-g(1)) ln^k(1-z)/(1-z).

Method (independent of research/c_dy):
 A. real emission: start from the D-dim matrix elements (VF-DY-3) and phase space (VF-DY-4) with the normalization of
    VF-DY-2; do the v-integrals symbolically (Beta functions) and compare with the closed forms VF-DY-5.
 B. test-function method: for test functions h, compute <bare + counterterm, h> EXACTLY at finite eps<0 with mpmath
    (subtracting G(1) at z=1, an exact identity for eps<0), for a ladder of eps values; check that the eps-poles cancel
    and that the eps->0 limit equals <Delta^(1), h> of VF-DY-8 (with mu_R and mu_F logs).
 C. Laurent coefficients of the pieces (VF-DY-7) acting on test functions.
 D. Mellin moments N=1,2 (VF-DY-14), large N, DIS scheme (VF-DY-10), plus trap (VF-DY-12), mu_F independence (VF-DY-11).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); LOG.append(s)

# ------------------------------------------------------------------ A. real emission from matrix elements
eps, z, v = sp.symbols('epsilon z v')
CF, TF, als, mu2, Q2 = sp.symbols('C_F T_F alpha_s mu2 Q2', positive=True)
EG = sp.EulerGamma
g02 = 4*sp.pi*als*mu2**eps*sp.exp(eps*EG)*(4*sp.pi)**(-eps)
shat = Q2/z
# q qbar -> gamma* g : t = -shat(1-z)v, u = -shat(1-z)(1-v)
t = -shat*(1-z)*v; u = -shat*(1-z)*(1-v)
Tqq = 8*(1-eps)*((1-eps)*(u/t + t/u) + 2*shat*Q2/(t*u) - 2*eps)
# q g -> gamma* q : u = -shat(1-z)v, t = -shat(1-z)(1-v)
uq = -shat*(1-z)*v; tq = -shat*(1-z)*(1-v)
Tqg = -8*(1-eps)*((1-eps)*(shat/tq + tq/shat) + 2*uq*Q2/(shat*tq) - 2*eps)
dPhi_pref = sp.Rational(1, 8)/sp.pi*(4*sp.pi/shat)**eps*(1-z)**(1-2*eps)/sp.gamma(1-eps)   # times [v(1-v)]^{-eps} dv

# numerical v-integration (exact quadrature at finite eps; independent of the closed forms)
Kr = sp.exp(eps*EG)*sp.gamma(1-eps)/sp.gamma(1-2*eps)
a_ = als/(2*sp.pi)
DR_qq_vf = -a_*2*CF/eps*(mu2/Q2)**eps*Kr*z**eps*(1-z)**(-1-2*eps)*(1+z**2+2*eps**2*(1-z)**2/(1-2*eps))
DR_qg_vf = -a_*TF/(2*eps)*(mu2/Q2)**eps*Kr*z**eps*(1-z)**(-2*eps)*(2*(z**2+(1-z)**2)-eps*(5*z**2-6*z+7)+eps**2*(1+z)**2)/((1-eps)*(1-2*eps))
subsn = {als: 1, mu2: 3, Q2: 2, CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}
for name, T_, pref, vf in (('qqbar', Tqq, g02*CF/(8*sp.pi*(1-eps)), DR_qq_vf), ('qg', Tqg, g02*TF/(8*sp.pi*(1-eps)**2), DR_qg_vf)):
    ratios = []
    for (ev, zv) in ((sp.Rational(-1, 7), sp.Rational(1, 3)), (sp.Rational(-3, 10), sp.Rational(5, 7)), (sp.Rational(-1, 20), sp.Rational(2, 9))):
        Pv = sp.lambdify(v, sp.cancel(v*(1-v)*T_.subs({eps: ev, z: zv}).subs(subsn)), 'mpmath')   # polynomial in v
        ae = -mp.mpf(ev.p)/ev.q                                  # |eps|, eps<0
        # int_0^1 v^{-1-eps}(1-v)^{-1-eps} P(v) dv ; on each half substitute u = v^{|eps|} (resp. (1-v)^{|eps|})
        lo = mp.quad(lambda uu: (1-uu**(1/ae))**(-1+ae)*Pv(uu**(1/ae)), [0, mp.mpf(2)**(-ae)])/ae
        hi = mp.quad(lambda uu: (1-uu**(1/ae))**(-1+ae)*Pv(1-uu**(1/ae)), [0, mp.mpf(2)**(-ae)])/ae
        vint_num = lo + hi
        full = mp.mpf(sp.N((pref*dPhi_pref).subs({eps: ev, z: zv}).subs(subsn), 40))*vint_num
        ratios.append(full/mp.mpf(sp.N(vf.subs({eps: ev, z: zv}).subs(subsn), 40)))
    log('A. real emission %s: ratio (matrix element x phase space)/(VF-DY-5 closed form) at 3 points:' % name, [mp.nstr(r_, 20) for r_ in ratios])

# ------------------------------------------------------------------ B. test-function method
mp.mp.dps = 50
CFn, TFn = mp.mpf(4)/3, mp.mpf(1)/2
zeta2 = mp.pi**2/6
def Krn(e): return mp.exp(e*mp.euler)*mp.gamma(1-e)/mp.gamma(1-2*e)
def Kvn(e): return mp.exp(e*mp.euler)*mp.gamma(1+e)*mp.gamma(1-e)**2/mp.gamma(1-2*e)
def fV(e): return -Kvn(e)*(2-e+2*e**2)/(e**2*(1-2*e))

def int_sub(G, e):
    """exact <(1-z)^{-1-2e} G> for e<0: int (1-z)^{-1-2e}(G(z)-G(1)) dz - G(1)/(2e)."""
    G1 = G(mp.mpf(1))
    I = mp.quad(lambda zz: (1-zz)**(-1-2*e)*(G(zz)-G1), [0, mp.mpf(1)/2, 1])
    return I - G1/(2*e)

tests = {
    'h1=1': lambda zz: mp.mpf(1),
    'h2=z^3': lambda zz: zz**3,
    'h3=exp(-2z)': lambda zz: mp.exp(-2*zz),
    'h4=z^(1/2)(1+z)': lambda zz: mp.sqrt(zz)*(1+zz),
}
def Pqq_act(h):   # C_F [(1+z^2)/(1-z)]_+
    return CFn*mp.quad(lambda zz: (1+zz**2)*(h(zz)-h(mp.mpf(1)))/(1-zz), [0, 1])
def Pqg_act(h):
    return TFn*mp.quad(lambda zz: (zz**2+(1-zz)**2)*h(zz), [0, 1])
def D1prod_act(gfun, h):   # <g D_1, h> product convention
    return mp.quad(lambda zz: (gfun(zz)*h(zz)-gfun(mp.mpf(1))*h(mp.mpf(1)))*mp.log(1-zz)/(1-zz), [0, 1])
def D0_act(h):
    return mp.quad(lambda zz: (h(zz)-h(mp.mpf(1)))/(1-zz), [0, 1])

L = mp.mpf('0.37')     # ln(mu^2/Q^2)  (mu = mu_R = scale of alpha_s and of dim. reg.)
LF = mp.mpf('0.21')    # ln(Q^2/mu_F^2)
def bare_plus_ct_qq(h, e):
    pref = mp.exp(e*L)                                   # (mu^2/Q^2)^eps
    G = lambda zz: zz**e*(1+zz**2+2*e**2*(1-zz)**2/(1-2*e))*h(zz)
    real = -2*CFn/e*pref*Krn(e)*int_sub(G, e)
    virt = CFn*pref*mp.cos(mp.pi*e)*fV(e)*h(mp.mpf(1))
    ct = 2/e*mp.exp(e*(L+LF))*Pqq_act(h)                # (mu^2/mu_F^2)^eps = exp(eps(L+LF))
    return real + virt + ct
def bare_plus_ct_qg(h, e):
    pref = mp.exp(e*L)
    N_ = lambda zz: (2*(zz**2+(1-zz)**2)-e*(5*zz**2-6*zz+7)+e**2*(1+zz)**2)/((1-e)*(1-2*e))
    real = -TFn/(2*e)*pref*Krn(e)*mp.quad(lambda zz: zz**e*(1-zz)**(-2*e)*N_(zz)*h(zz), [0, 1])
    ct = 1/e*mp.exp(e*(L+LF))*Pqg_act(h)
    return real + ct
def target_qq(h):
    one = mp.mpf(1)
    res = CFn*(4*D1prod_act(lambda zz: 1+zz**2, h)
               - 2*mp.quad(lambda zz: (1+zz**2)*mp.log(zz)/(1-zz)*h(zz), [0, 1])
               + (2*mp.pi**2/3-8)*h(one))
    return res + 2*Pqq_act(h)*LF
def target_qg(h):
    return TFn*mp.quad(lambda zz: ((zz**2+(1-zz)**2)*mp.log((1-zz)**2/zz)+mp.mpf(1)/2+3*zz-mp.mpf(7)/2*zz**2)*h(zz), [0, 1]) + Pqg_act(h)*LF

def extrap(fun):
    # fit fun(eps) = c_{-2}/eps^2 + c_{-1}/eps + c0 + c1 eps + ... on a ladder of negative eps
    es = [-mp.mpf(k)/1000 for k in range(1, 9)]
    vals = [fun(e) for e in es]
    # solve linear system for c_{-2},c_{-1},c0..c5
    n = len(es)
    A = mp.matrix(n, n); bvec = mp.matrix(n, 1)
    for i, e in enumerate(es):
        for j in range(n):
            A[i, j] = e**(j-2)
        bvec[i] = vals[i]
    c = mp.lu_solve(A, bvec)
    return c[0], c[1], c[2]
log('B. test-function method (L=ln(mu^2/Q^2)=%s, ln(Q^2/mu_F^2)=%s): poles and finite part' % (mp.nstr(L,3), mp.nstr(LF,3)))
maxd = 0
for nm, h in tests.items():
    for ch, fun, tgt in (('qqbar', bare_plus_ct_qq, target_qq), ('qg', bare_plus_ct_qg, target_qg)):
        cm2, cm1, c0 = extrap(lambda e: fun(h, e))
        T = tgt(h)
        maxd = max(maxd, abs(c0-T))
        log('   %-18s %-5s: eps^-2 coeff %s, eps^-1 coeff %s, finite %s, VF-DY-8 %s, |d|=%s' % (nm, ch,
            mp.nstr(cm2, 3), mp.nstr(cm1, 3), mp.nstr(c0, 15), mp.nstr(T, 15), mp.nstr(abs(c0-T), 3)))
log('   max |finite - target| =', mp.nstr(maxd, 3))

# ------------------------------------------------------------------ C. Laurent coefficients of the pieces (VF-DY-7), mu=Q
def laurent_piece(fun):
    return extrap(fun)
Lsave = L; L = mp.mpf(0)
log('C. Laurent coefficients at L=0 acting on h=z^3 and h=exp(-2z) (real qqbar / virtual / real qg)')
for nm in ('h2=z^3', 'h3=exp(-2z)'):
    h = tests[nm]
    real_qq = lambda e: -2*CFn/e*Krn(e)*int_sub(lambda zz: zz**e*(1+zz**2+2*e**2*(1-zz)**2/(1-2*e))*h(zz), e)
    c = laurent_piece(real_qq)
    one = mp.mpf(1)
    pred_m2 = 2*CFn*h(one)
    pred_m1 = -4*CFn*D0_act(h) + 2*CFn*mp.quad(lambda zz: (1+zz)*h(zz), [0, 1])
    pred_0 = (CFn*(-mp.pi**2/2)*h(one) + 8*CFn*mp.quad(lambda zz: (h(zz)-h(one))*mp.log(1-zz)/(1-zz), [0, 1])
              - 4*CFn*mp.quad(lambda zz: (1+zz)*mp.log(1-zz)*h(zz), [0, 1])
              - 2*CFn*mp.quad(lambda zz: (1+zz**2)/(1-zz)*mp.log(zz)*h(zz), [0, 1]))
    log('   %s real qqbar: %s %s %s  vs VF-DY-7 %s %s %s' % (nm, mp.nstr(c[0],12), mp.nstr(c[1],12), mp.nstr(c[2],12),
        mp.nstr(pred_m2,12), mp.nstr(pred_m1,12), mp.nstr(pred_0,12)))
    virt = lambda e: CFn*mp.cos(mp.pi*e)*fV(e)*h(one)
    c = laurent_piece(virt)
    log('   %s virtual   : %s %s %s  vs VF-DY-7 %s %s %s' % (nm, mp.nstr(c[0],12), mp.nstr(c[1],12), mp.nstr(c[2],12),
        mp.nstr(-2*CFn*h(one),12), mp.nstr(-3*CFn*h(one),12), mp.nstr(CFn*(-8+7*mp.pi**2/6)*h(one),12)))
    real_qg = lambda e: -TFn/(2*e)*Krn(e)*mp.quad(lambda zz: zz**e*(1-zz)**(-2*e)*(2*(zz**2+(1-zz)**2)-e*(5*zz**2-6*zz+7)+e**2*(1+zz)**2)/((1-e)*(1-2*e))*h(zz), [0, 1])
    c = laurent_piece(real_qg)
    pred0 = TFn*mp.quad(lambda zz: ((zz**2+(1-zz)**2)*mp.log((1-zz)**2/zz)+(1+6*zz-7*zz**2)/2)*h(zz), [0, 1])
    log('   %s real qg   : %s %s %s  vs VF-DY-7 0 %s %s' % (nm, mp.nstr(c[0],3), mp.nstr(c[1],12), mp.nstr(c[2],12),
        mp.nstr(-Pqg_act(h),12), mp.nstr(pred0,12)))
L = Lsave

# pi^2 bookkeeping: delta coefficient 2pi^2/3 = -pi^2/2 (K_r) + pi^2/6 (K_v) + pi^2 (cos pi eps)
e_ = sp.symbols('e')
Krs = sp.exp(e_*EG)*sp.gamma(1-e_)/sp.gamma(1-2*e_); Kvs = sp.exp(e_*EG)*sp.gamma(1+e_)*sp.gamma(1-e_)**2/sp.gamma(1-2*e_)
log('C2. K_r = ', sp.series(Krs, e_, 0, 3).removeO(), ' ; K_v = ', sp.series(Kvs, e_, 0, 3).removeO(),
    ' ; cos(pi e) = ', sp.series(sp.cos(sp.pi*e_), e_, 0, 3).removeO())

# ------------------------------------------------------------------ D. moments, large N, DIS scheme, plus trap, mu_F
def Delta1_qq_act(h):   # at mu_F = Q
    one = mp.mpf(1)
    return CFn*(4*D1prod_act(lambda zz: 1+zz**2, h) - 2*mp.quad(lambda zz: (1+zz**2)*mp.log(zz)/(1-zz)*h(zz), [0, 1]) + (2*mp.pi**2/3-8)*h(one))
def Delta1_qg_act(h):
    return TFn*mp.quad(lambda zz: ((zz**2+(1-zz)**2)*mp.log((1-zz)**2/zz)+mp.mpf(1)/2+3*zz-mp.mpf(7)/2*zz**2)*h(zz), [0, 1])
mom = lambda N: (lambda zz: zz**(N-1))
for N, pq, pg in ((1, CFn*(8*zeta2-mp.mpf(7)/2), TFn/9), (2, CFn*(8*zeta2+mp.mpf(13)/18), -mp.mpf(11)/18*TFn)):
    dq, dg = Delta1_qq_act(mom(N)), Delta1_qg_act(mom(N))
    log('D1. N=%d: Delta_qq^(1)=%s (VF %s) ; Delta_qg^(1)=%s (VF %s)' % (N, mp.nstr(dq, 20), mp.nstr(pq, 20), mp.nstr(dg, 20), mp.nstr(pg, 20)))
# large N with exact harmonic sums for the D_k parts and numerics for the rest
def S1(n): return mp.harmonic(n)
def S2(n): return mp.zeta(2) - mp.zeta(2, n+1)
def largeN(N):
    # 4(1+z^2)D_1 = 8 D_1 - 4(1+z) ln(1-z)
    d1 = (S1(N-1)**2 + S2(N-1))/2
    reg = mp.quad(lambda zz: 0 if zz >= 1 else zz**(N-1)*(-4*(1+zz)*mp.log(1-zz) - 2*(1+zz**2)*mp.log(zz)/(1-zz)), [0, 1-mp.mpf(1)/N, 1])
    return CFn*(8*d1) + CFn*reg + CFn*(2*mp.pi**2/3-8)
for N in (10, 100, 1000, 10000):
    Nb = N*mp.exp(mp.euler)
    exact = largeN(N)
    asym = CFn*(4*mp.log(Nb)**2 + 8*zeta2 - 8)
    log('D2. N=%5d: Delta_qq,N^(1)=%s ; C_F(4 ln^2 Nbar + 8 zeta2 - 8)=%s ; diff=%s ; diff*N/lnN=%s' % (N, mp.nstr(exact, 12),
        mp.nstr(asym, 12), mp.nstr(exact-asym, 5), mp.nstr((exact-asym)*N/mp.log(N), 5)))
# DIS scheme
def C2q_act(h):
    one = mp.mpf(1)
    return CFn*(2*mp.quad(lambda zz: (h(zz)-h(one))*mp.log(1-zz)/(1-zz), [0, 1]) - mp.mpf(3)/2*D0_act(h)
                + mp.quad(lambda zz: (-(1+zz)*mp.log(1-zz) - (1+zz**2)*mp.log(zz)/(1-zz) + 3 + 2*zz)*h(zz), [0, 1])
                - (mp.mpf(9)/2 + mp.pi**2/3)*h(one))
def C2g_act(h):
    return TFn*mp.quad(lambda zz: ((zz**2+(1-zz)**2)*mp.log((1-zz)/zz) - 8*zz**2 + 8*zz - 1)*h(zz), [0, 1])
def DISqq_act(h):
    one = mp.mpf(1)
    return CFn*((1+4*mp.pi**2/3)*h(one) + 2*D1prod_act(lambda zz: 1+zz**2, h) + 3*D0_act(h) + mp.quad(lambda zz: (-6-4*zz)*h(zz), [0, 1]))
def DISqg_act(h):
    return TFn*mp.quad(lambda zz: ((zz**2+(1-zz)**2)*mp.log(1-zz) + mp.mpf(3)/2 - 5*zz + mp.mpf(9)/2*zz**2)*h(zz), [0, 1])
md = 0
for nm, h in tests.items():
    d1 = abs(Delta1_qq_act(h) - 2*C2q_act(h) - DISqq_act(h)); d2 = abs(Delta1_qg_act(h) - C2g_act(h) - DISqg_act(h))
    md = max(md, d1, d2)
log('D3. DIS scheme: max |Delta^MS - 2C2q - Delta^DIS|, |Delta_qg^MS - C2g - Delta_qg^DIS| over tests =', mp.nstr(md, 3))
# plus trap
pt = mp.quad(lambda zz: (1+zz)*mp.log(1-zz), [0, 1])
log('D4. int_0^1 (1+z) ln(1-z) dz =', mp.nstr(pt, 20), '(-7/4 =', -mp.mpf(7)/4, ') ; whole-term plus would shift delta coeff by 4C_F*7/4 = 7C_F')
# mu_F independence in Mellin space (symbolic)
aS, lF = sp.symbols('a ell_F')
gqq, gqg, d1q, d1g = sp.symbols('gamma_qq gamma_qg D1q D1g')
qA, qbA, gA, qB, qbB, gB = sp.symbols('qA qbA gA qB qbB gB')
Dqq = 1 + aS*(d1q - 2*gqq*lF); Dqg = aS*(d1g - gqg*lF)
dq = lambda q, g: aS*(gqq*q + gqg*g)
sig = (qA*qbB + qbA*qB)*Dqq + (gA*(qB+qbB) + (qA+qbA)*gB)*Dqg
dsig = sp.diff(sig, lF) + sum(sp.diff(sig, s_)*dq(s_, gl) for s_, gl in ((qA, gA), (qbA, gA), (qB, gB), (qbB, gB)))
dsig = sp.expand(dsig)
log('D5. d sigma_N / d ln mu_F^2 at O(a):', sp.simplify(dsig.coeff(aS, 1)), '; O(a^2) remainder present:', dsig.coeff(aS, 2) != 0)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'dy_nlo_check.log'), 'w').write('\n'.join(LOG) + '\n')
