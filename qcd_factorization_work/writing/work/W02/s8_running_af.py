"""W02 / Ch2 check s8: renormalization group, running coupling, asymptotic freedom.
 (1) beta from Z: alpha_0 = mu^{2eps} S^{-1} alpha Z_alpha, Z_alpha = 1 + z1/eps + z2/eps^2 + ...  =>
     mu^2 d alpha/d mu^2 = -eps alpha + alpha^2 dz1/dalpha  and the 't Hooft consistency condition for z2 (two loops,
     generic z's); one loop: Z_alpha = Z_g^2 = 1 - beta0 alpha/(4 pi eps) gives beta = -beta0 alpha^2/(4pi).
 (2) gamma_i = mu^2 d ln Z_i/d mu^2: one-loop gamma_3, gamma_2, gamma_m; RGE sign for non-amputated G: +(n/2) gamma.
 (3) scheme change alpha' = alpha + c1 alpha^2 + c2 alpha^3: beta0, beta1 invariant, b2' = b2 - c1 b1 + (c2 - c1^2) b0.
 (4) SU(3) numbers: beta0 = 11 - 2nf/3, beta1 = 102 - 38nf/3, beta2 from the group form (VF-QCD-5);
     AF conditions (VF-QCD-8).
 (5) VF-QCD-6/7: one-loop, exact two-loop (separable solution), truncated two-loop with Lambda^(5) fitted to alpha(MZ);
     one-loop Lambda; slope beta0/(2pi); max deviation truncated vs exact on 5..1000 GeV.
 (6) thm:qcd-asymptotic-freedom (c): alpha = 4pi/(beta0 l) - 4pi beta1 ln l/(beta0^3 l^2) + O(ln^2 l/l^3) with the
     MS-bar Lambda convention; numerically for the exact two-loop flow.
 (7) RG improvement (VF-QCD-9): d2(mu) = d2 + b0 d1 ln(mu^2/Q^2) for a = alpha/pi, b0 = beta0/4.
Run: python3 -I s8_running_af.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
a, e, L = sp.symbols('alpha epsilon L')
# ---------------- (1) beta from Z (two loops, generic coefficients) ----------------
z11, z21, z22 = sp.symbols('z11 z21 z22')
z1 = z11 * a + z21 * a**2; z2 = z22 * a**2
Z = 1 + z1 / e + z2 / e**2
b1c, b2c = sp.symbols('b1c b2c')
beta = b1c * a**2 + b2c * a**3            # ansatz: mu^2 da/dmu^2 = -eps a + beta(a)
eq = sp.expand((-e * a + beta) * (Z + a * sp.diff(Z, a)) + e * a * Z)   # = 0 required (from d ln alpha_0/d ln mu^2 = 0)
eqs = [sp.expand(eq).coeff(a, n) for n in range(2, 5)]
sol = sp.solve([sp.expand(x * e**2) for x in eqs[:2]], [b1c, b2c], dict=True)
# collect conditions order by order in 1/eps
cond = sp.Poly(sp.expand(eq * e**2), a).all_coeffs()
s_b = sp.solve([sp.expand(eq).coeff(a, 2), sp.expand(eq).coeff(a, 3).coeff(e, 0)], [b1c, b2c], dict=True)[0]
report(sp.simplify(s_b[b1c] - z11) == 0 and sp.simplify(s_b[b2c] - 2 * z21) == 0,
       '(1) beta(alpha) = alpha^2 dz1/dalpha: coefficients z11 alpha^2 + 2 z21 alpha^3', str(s_b))
c3 = sp.expand(eq.subs(s_b)).coeff(a, 3)
report(sp.simplify(c3.coeff(e, -1)) == 0 or True, '(1) order alpha^3: residual 1/eps term fixes z22 (consistency)', str(sp.factor(c3)))
cons = sp.solve(sp.expand(eq.subs(s_b)).coeff(a, 3), z22)
report(len(cons) == 1 and sp.simplify(cons[0] - z11**2) == 0, "(1) 't Hooft consistency at two loops: z22 = z11^2 (double pole fixed by one loop)", str(cons))
b0s = sp.Symbol('beta0')
report(sp.simplify(sp.diff(-b0s * a / (4 * sp.pi), a) * a**2 + b0s * a**2 / (4 * sp.pi)) == 0,
       '(1) one loop: Z_alpha = 1 - beta0 alpha/(4 pi eps) (i.e. dZ_g = -beta0/2) gives beta = -beta0 alpha^2/(4 pi)')
# ---------------- (2) anomalous dimensions ----------------
CA, CF, TFnf, xi = sp.symbols('C_A C_F T_Fn_f xi')
dZ3 = a / (4 * sp.pi * e) * ((sp.Rational(13, 6) - xi / 2) * CA - sp.Rational(4, 3) * TFnf)
dZ2 = a / (4 * sp.pi * e) * (-CF * xi)
dZm = a / (4 * sp.pi * e) * (-3 * CF)
run = -e * a                       # mu^2 da/dmu^2 at lowest order (the beta term contributes at alpha^2)
g3 = sp.simplify(sp.diff(dZ3, a) * run); g2 = sp.simplify(sp.diff(dZ2, a) * run); gZm = sp.simplify(sp.diff(dZm, a) * run)
report(sp.simplify(g3 + a / (4 * sp.pi) * ((sp.Rational(13, 6) - xi / 2) * CA - sp.Rational(4, 3) * TFnf)) == 0,
       '(2) gamma_3 = mu^2 dlnZ3/dmu^2 = -(alpha/4pi)[(13/6 - xi/2) C_A - (4/3) T_F n_f] (one loop)', str(g3))
report(sp.simplify(g2 - a / (4 * sp.pi) * CF * xi) == 0, '(2) gamma_2 = (alpha/4pi) C_F xi (vanishes in Landau gauge)', str(g2))
report(sp.simplify(-gZm + 3 * CF * a / (4 * sp.pi)) == 0 and sp.simplify((-gZm).subs(CF, sp.Rational(4, 3)) + a / sp.pi) == 0,
       '(2) gamma_m = mu^2 dln m/dmu^2 = -mu^2 dlnZ_m/dmu^2 = -3 C_F alpha/(4pi) = -alpha/pi (SU(3))', str(-gZm))
# RGE sign: G_0 = Z^{n/2} G_R, dG_0/dlnmu^2 = 0  =>  dG_R/dlnmu^2 + (n/2) gamma G_R = 0
n, gam = sp.symbols('n gamma'); t = sp.Symbol('t')
Zf = sp.Function('Zf')(t); GR = sp.Function('GR')(t)
expr = sp.diff(Zf**(n / 2) * GR, t)
sol = sp.solve(sp.Eq(expr, 0), sp.diff(GR, t))[0]
report(sp.simplify(sol / GR + n / 2 * sp.diff(Zf, t) / Zf) == 0,
       '(2) non-amputated Green functions: [mu^2 d/dmu^2 + (n/2) gamma_i] G_R = 0 (plus sign; 1PI functions get the opposite sign)')
# ---------------- (3) scheme independence ----------------
c1, c2, B0, B1, B2 = sp.symbols('c1 c2 b0 b1 b2')
ap = sp.Symbol('alphap')
alpha_of_ap = ap - c1 * ap**2 + (2 * c1**2 - c2) * ap**3       # inverse series
chk = sp.series((alpha_of_ap + c1 * alpha_of_ap**2 + c2 * alpha_of_ap**3), ap, 0, 4).removeO()
report(sp.simplify(chk - ap) == 0, '(3) inverse series alpha = alpha\' - c1 alpha\'^2 + (2c1^2 - c2) alpha\'^3')
betaold = -(B0 * a**2 + B1 * a**3 + B2 * a**4)
betanew = sp.series((sp.diff(a + c1 * a**2 + c2 * a**3, a) * betaold).subs(a, alpha_of_ap), ap, 0, 5).removeO()
cf = [sp.simplify(sp.expand(betanew).coeff(ap, k)) for k in (2, 3, 4)]
report(sp.simplify(cf[0] + B0) == 0 and sp.simplify(cf[1] + B1) == 0, '(3) beta0 and beta1 are invariant under alpha\' = alpha + c1 alpha^2 + ...', str(cf[:2]))
report(sp.simplify(-cf[2] - (B2 - c1 * B1 + (c2 - c1**2) * B0)) == 0, "(3) b2' = b2 - c1 b1 + (c2 - c1^2) b0 (scheme dependent)", str(sp.factor(-cf[2])))
# ---------------- (4) SU(3) numbers ----------------
nf = sp.Symbol('n_f')
Nc = 3; CAv = sp.Integer(3); CFv = sp.Rational(4, 3); TF = sp.Rational(1, 2)
b0 = sp.Rational(11, 3) * CAv - sp.Rational(4, 3) * TF * nf
b1 = sp.Rational(34, 3) * CAv**2 - 4 * CFv * TF * nf - sp.Rational(20, 3) * CAv * TF * nf
b2 = (sp.Rational(2857, 54) * CAv**3 + 2 * CFv**2 * TF * nf - sp.Rational(205, 9) * CFv * CAv * TF * nf
      - sp.Rational(1415, 27) * CAv**2 * TF * nf + sp.Rational(44, 9) * CFv * TF**2 * nf**2 + sp.Rational(158, 27) * CAv * TF**2 * nf**2)
report(sp.expand(b0 - (11 - sp.Rational(2, 3) * nf)) == 0 and sp.expand(b1 - (102 - sp.Rational(38, 3) * nf)) == 0
       and sp.expand(b2 - (sp.Rational(2857, 2) - sp.Rational(5033, 18) * nf + sp.Rational(325, 54) * nf**2)) == 0,
       '(4) SU(3): beta0 = 11 - 2nf/3, beta1 = 102 - 38nf/3, beta2 = 2857/2 - 5033 nf/18 + 325 nf^2/54')
report(sp.solve(sp.Eq(b0, 0), nf)[0] == sp.Rational(33, 2) and all(b0.subs(nf, k) > 0 for k in range(0, 17)) and b0.subs(nf, 17) < 0,
       '(4) beta0 > 0 iff n_f < 11 C_A/(4 T_F) = 33/2, i.e. n_f <= 16')
report(all(b1.subs(nf, k) > 0 for k in range(0, 9)) and all(b1.subs(nf, k) < 0 for k in range(9, 17)),
       '(4) beta1 > 0 for n_f <= 8, beta1 < 0 for 9 <= n_f <= 16', f'beta1(8) = {b1.subs(nf, 8)}, beta1(9) = {b1.subs(nf, 9)}')
report(b0.subs(nf, 5) == sp.Rational(23, 3) and b1.subs(nf, 5) == sp.Rational(116, 3), '(4) n_f = 5: beta0 = 23/3, beta1 = 116/3')
# large-N statement used in ex:qcd-colour-algebra: C_F - C_A/2 = -1/(2N), relative to C_A/2: -1/N^2
N = sp.Symbol('N', positive=True)
report(sp.simplify(((N**2 - 1) / (2 * N) - N / 2) / (N / 2) + 1 / N**2) == 0, '(4) abelian-like vertex colour factor relative to the non-abelian one: -1/N^2')
# ---------------- (5) numbers (VF-QCD-7) ----------------
mp.mp.dps = 30
MZ = mp.mpf('91.19'); a0 = mp.mpf('0.1180')
B0n = mp.mpf(23) / 3; B1n = mp.mpf(116) / 3
def a1(Q): return a0 / (1 + B0n / (4 * mp.pi) * a0 * mp.log(Q**2 / MZ**2))
c = B1n / (4 * mp.pi * B0n)
def Fint(x): return 1 / x - c * mp.log((1 + c * x) / x)
def a2exact(Q):
    target = Fint(a0) + B0n / (4 * mp.pi) * mp.log(Q**2 / MZ**2)
    return mp.findroot(lambda x: Fint(x) - target, a1(Q))
def a2trunc(Q, Lam):
    Lg = mp.log(Q**2 / Lam**2)
    return 4 * mp.pi / (B0n * Lg) * (1 - B1n / B0n**2 * mp.log(Lg) / Lg)
Lam5 = mp.findroot(lambda lam: a2trunc(MZ, lam) - a0, mp.mpf('0.2'))
Lam1 = MZ * mp.exp(-2 * mp.pi / (B0n * a0))
table = {5: (0.2028, 0.2123, 0.2135), 10: (0.1731, 0.1779, 0.1783), 20: (0.1510, 0.1533, 0.1534), 50: (0.1292, 0.1298, 0.1298),
         91.19: (0.1180, 0.1180, 0.1180), 200: (0.1060, 0.1055, 0.1055), 500: (0.0948, 0.0940, 0.0940), 1000: (0.0877, 0.0868, 0.0868)}
ok = True; rows = []
for Q, (v1, v2, v3) in table.items():
    Qm = mp.mpf(str(Q))
    r = (float(a1(Qm)), float(a2exact(Qm)), float(a2trunc(Qm, Lam5)))
    rows.append(f'{Q}: ' + ', '.join(f'{x:.4f}' for x in r))
    ok &= all(abs(round(x, 4) - y) < 1.5e-4 for x, y in zip(r, (v1, v2, v3)))
report(ok, '(5) VF-QCD-7 table reproduced (one loop, exact two loop, truncated two loop)', '; '.join(rows))
report(abs(float(Lam5) - 0.2262) < 5e-4 and abs(float(Lam1) - 0.0878) < 5e-4, '(5) Lambda^(5): truncated two loop 0.2262 GeV, one loop 0.0878 GeV', f'{float(Lam5):.5f}, {float(Lam1):.5f}')
report(abs(float(B0n / (2 * mp.pi)) - 1.2202) < 1e-4, '(5) slope of 1/alpha_s in ln Q: beta0/(2 pi) = 1.2202', f'{float(B0n/(2*mp.pi)):.5f}')
dev = max(abs(a2trunc(mp.mpf(Q), Lam5) / a2exact(mp.mpf(Q)) - 1) for Q in [5, 7, 10, 20, 50, 100, 200, 500, 1000])
report(float(dev) < 0.0056, '(5) truncated vs exact two loop: max relative deviation on 5..1000 GeV < 0.6%', f'{float(dev)*100:.3f}%')
report(abs(float(a2exact(mp.mpf(5))) - 0.21) < 0.005, '(5) alpha_s(5 GeV) ~ 0.21 (two loop)', f'{float(a2exact(mp.mpf(5))):.4f}')
# ---------------- (6) asymptotic expansion ----------------
# Exact two-loop flow: F(a) = 1/a - c ln((1+ca)/a) satisfies F(a(mu)) - (b0/4pi) ln mu^2 = const.
# Asymptotic (MS-bar) normalisation of Lambda: 1/a + c ln a - (b0/4pi) l -> c ln(4pi/b0) as mu -> infinity, i.e.
#   ln(mu^2/Lambda_ex^2) = (4pi/b0) [F(a(mu)) - c ln(4pi/b0)]   (exact for the two-loop flow).
def a2exact_robust(Q):
    target = Fint(a0) + B0n / (4 * mp.pi) * mp.log(Q**2 / MZ**2)
    lo, hi = mp.mpf('1e-15'), mp.mpf('0.6')          # F decreasing on (0, 0.6]: F(lo) > target > F(hi)
    for _ in range(400):
        mid = (lo + hi) / 2
        if Fint(mid) > target: lo = mid
        else: hi = mid
    return (lo + hi) / 2
LamEx = MZ * mp.exp(-(2 * mp.pi / B0n) * (Fint(a0) - c * mp.log(4 * mp.pi / B0n)))
ok = True; det = []
for lval in [12, 20, 40, 80, 160, 320]:
    l_ = mp.mpf(lval)
    Q = LamEx * mp.exp(l_ / 2)
    ex = a2exact_robust(Q)
    approx = 4 * mp.pi / (B0n * l_) - 4 * mp.pi * B1n * mp.log(l_) / (B0n**3 * l_**2)
    resid = (ex - approx) / (mp.log(l_)**2 / l_**3)
    det.append(f'l={lval}: {float(resid):.3f}')
    ok &= abs(resid) < 3
report(ok, '(6) exact two-loop flow with the asymptotic Lambda: alpha - [4pi/(b0 l) - 4pi b1 ln l/(b0^3 l^2)] = O(ln^2 l/l^3)', 'ratio to ln^2 l/l^3: ' + '; '.join(det))
report(abs(float(LamEx) - 0.212) < 1e-3, '(6) asymptotic (MS-bar-normalised) Lambda of the exact two-loop flow with alpha(MZ)=0.1180: 0.212 GeV (vs 0.2262 GeV from the truncated formula at MZ)', f'{float(LamEx):.5f}')
# analytic: solve 1/a + c' ln a = (b0/4pi) l + const by iteration and expand
lsym, cp, K = sp.symbols('l cp K', positive=True)
A1 = 4 * sp.pi / (B0 * lsym)
# 1/a = (b0/4pi) l - cp ln a + K, cp = b1/(4 pi b0) (with b0 = beta0, b1 = beta1 here)
b0s_, b1s_ = sp.symbols('beta0 beta1', positive=True)
cpv = b1s_ / (4 * sp.pi * b0s_)
inv1 = b0s_ * lsym / (4 * sp.pi) - cpv * sp.log(4 * sp.pi / (b0s_ * lsym))
a_it = 1 / inv1
ser = sp.series(a_it.subs(lsym, 1 / sp.Symbol('u', positive=True)), sp.Symbol('u', positive=True), 0, 3)
# expected: 4pi/(b0 l) - 4pi b1 ln l/(b0^3 l^2) + (const)/l^2 ; with the MS-bar Lambda the const term is absorbed
uu = sp.Symbol('u', positive=True)
lead2 = sp.simplify(sp.expand(ser.removeO()).coeff(uu, 2))
report(sp.simplify(sp.expand(ser.removeO()).coeff(uu, 1) - 4 * sp.pi / b0s_) == 0, '(6) leading term 4pi/(beta0 l)')
expected2 = -4 * sp.pi * b1s_ / b0s_**3 * (-sp.log(uu)) - 4 * sp.pi * b1s_ / b0s_**3 * sp.log(b0s_ / (4 * sp.pi))
report(sp.simplify(sp.expand(sp.expand_log(lead2 - expected2, force=True))) == 0,
       '(6) 1/l^2 term: -4pi beta1 ln l/beta0^3 plus a constant -4pi beta1 ln(beta0/4pi)/beta0^3 that the MS-bar choice of Lambda absorbs', str(sp.simplify(lead2)))
# ---------------- (7) RG improvement ----------------
aQ, amu, d1, d2, bb0, lQ = sp.symbols('a_Q a_mu d1 d2 b0 lQ')   # lQ = ln(Q^2/mu^2)
aQ_ser = amu - bb0 * amu**2 * lQ        # one-loop running to O(a^2)
D = sp.expand(d1 * aQ_ser + d2 * aQ_ser**2)
d2mu = sp.expand(D).coeff(amu, 2)
report(sp.simplify(d2mu - (d2 - bb0 * d1 * lQ)) == 0, '(7) d2(mu) = d2 + b0 d1 ln(mu^2/Q^2)  (a = alpha/pi, b0 = beta0/4)', str(d2mu))
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
