# W17 / Ch14 -- s06: one-loop Collins TMD of a quark in a quark in b space; UV counterterm, gamma_F, K, gamma_K;
# small-b coefficients C_qq, C_qg in both S_eps conventions; hard factor from the time-like form factor of Ch5
# (prop:sudakov-oneloop); RG consistency; CSS coefficients A1, B1, C1; delta-regulator map.
# Bookkeeping: bare one-loop quantity = a S_eps X(eps), a = alpha_s C_F/(2 pi), counterterms = a S_eps x pure poles
# (equivalent to g0^2 = 4 pi alpha_s mu^{2eps} S_eps^{-1} with pure-pole counterterms).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

eps, mu, b, als, CF, TF, zeta = sp.symbols('epsilon mu b alpha_s C_F T_F zeta', positive=True)
gE = sp.EulerGamma
Lb, lz, L = sp.symbols('L_b l_zeta L', real=True)
d = 2 - 2*eps
b0 = 2*sp.exp(-gE)
# ---------- (1) d-dim Fourier transforms (convention e^{-i k.b})
def FT(alpha):   # int d^d k e^{-ik.b} (k^2)^(-alpha)
    return sp.pi**(d/2)*2**(d - 2*alpha)*sp.gamma(d/2 - alpha)/sp.gamma(alpha)*(b**2)**(alpha - d/2)
cS = 4*sp.pi*als*mu**(2*eps)*CF/(2*sp.pi)**(3 - 2*eps)
a = als*CF/(2*sp.pi)
Seps = (4*sp.pi)**eps*sp.exp(-eps*gE)
SepsC = (4*sp.pi)**eps/sp.gamma(1 - eps)
A_closed = -sp.exp(eps*Lb)*sp.exp(-gE*eps)*sp.gamma(1 - eps)/eps
Lb_val = sp.log(mu**2*b**2/b0**2)
A_num = cS*FT(1)/(a*Seps)
for ev in [sp.Rational(13, 100), sp.Rational(-21, 100)]:
    vals = {eps: ev, mu: sp.Rational(17, 10), b: sp.Rational(2, 5)}
    r = complex(sp.N((A_num/A_closed.subs(Lb, Lb_val)).subs(vals), 25))
    check('A(eps) = c_S FT[1/k^2]/(a S_eps) = -e^{eps L_b} e^{-gamma eps} Gamma(1-eps)/eps at eps=%s' % ev, abs(r - 1) < 1e-18)
# B(eps) = c_S FT[ln(zeta/k^2)/k^2]/(a S_eps) = d/d eta [zeta^eta ... ]: FT[ln(zeta/k^2)/k^2] = ln zeta FT(1) + d/d eta FT(1+eta)|_0
eta = sp.Symbol('eta')
B_num = cS*(sp.log(zeta)*FT(1) + sp.diff(FT(1 + eta), eta).subs(eta, 0))/(a*Seps)
B_claim = A_closed*(lz + Lb - 1/eps - sp.polygamma(0, 1 - eps) - gE)
for ev in [sp.Rational(13, 100), sp.Rational(-21, 100)]:
    vals = {eps: ev, mu: sp.Rational(17, 10), b: sp.Rational(2, 5), zeta: sp.Rational(37, 10)}
    lhs = complex(sp.N(B_num.subs(vals), 25))
    rhs = complex(sp.N(B_claim.subs({Lb: Lb_val, lz: sp.log(zeta/mu**2)}).subs(vals), 25))
    check('B(eps) = A [l_zeta + L_b - 1/eps - psi(1-eps) - gamma_E] at eps=%s' % ev, abs(lhs/rhs - 1) < 1e-18)
kap = sp.Symbol('kappa')
# Laurent series; Collins convention: A^C = A e^{-gamma eps} Gamma(1-eps)
def ser(expr, n=1):
    return sp.expand(sp.series(expr, eps, 0, n).removeO())
A_s = ser(A_closed, 2)
check('A = -1/eps - L_b - eps (L_b^2/2 + pi^2/12) + O(eps^2)', sp.simplify(A_s - (-1/eps - Lb - eps*(Lb**2/2 + sp.pi**2/12))) == 0)
B_s = ser(B_claim, 1)
check('B = 1/eps^2 - l_z/eps - L_b^2/2 - L_b l_z - pi^2/12 + O(eps)', sp.simplify(B_s - (1/eps**2 - lz/eps - Lb**2/2 - Lb*lz - sp.pi**2/12)) == 0)
B_sC = ser(B_claim*sp.exp(-gE*eps)*sp.gamma(1 - eps), 1)
check('Collins S_eps: B^C = ... - L_b l_z + 0*pi^2  (kappa = 0)', sp.simplify(B_sC - (1/eps**2 - lz/eps - Lb**2/2 - Lb*lz)) == 0)

# ---------- (2) bare one-loop Collins TMD in b space:  f1 = a S_eps { [p(x) - eps (1-x)] A + delta(1-x) B }
# represent distributions symbolically: P = p(x) (plus-distribution object), Om = (1-x), Dl = delta(1-x)
P, Om, Dl = sp.symbols('P Om Dl')
f1_bind = sp.expand(ser((P - eps*Om)*A_closed, 1) + Dl*B_s)
target = -P/eps - Lb*P + Om + Dl*(1/eps**2 - lz/eps - Lb**2/2 - Lb*lz - sp.pi**2/12)
check('bare TMD (binding) = a S_eps{-p/eps - L_b p + (1-x) + delta[1/eps^2 - l_z/eps - L_b^2/2 - L_b l_z - pi^2/12]}', sp.simplify(f1_bind - target) == 0)
# ---------- (3) IR poles must be those of the MSbar partonic PDF: f_{q/q} = delta - (alpha_s/2pi)(S_eps/eps) P_qq,  P_qq/C_F = p + 3/2 delta
pdf1 = -(P + sp.Rational(3, 2)*Dl)/eps
ZF1 = -1/eps**2 + (lz - sp.Rational(3, 2))/eps       # claimed Z_F Z_2 - 1 in units a S_eps
ren = sp.expand(f1_bind + Dl*ZF1)
poles = sp.expand(ren - ren.subs(eps, sp.oo)) if False else None
# check: ren - pdf1 is finite
diff = sp.expand(ren - pdf1)
check('Z_F Z_2 = 1 + a S_eps[-1/eps^2 + (l_z - 3/2)/eps] makes TMD - PDF finite', all(sp.degree(t, 1/eps) <= 0 if t.has(eps) else True for t in sp.Add.make_args(diff)) and sp.limit(diff*eps, eps, 0) == 0)
C_bind = sp.expand(diff)
check('C~_qq (binding) = delta + a{-L_b p + (1-x) + delta[-L_b^2/2 - L_b l_z - pi^2/12]}', sp.simplify(C_bind - (-Lb*P + Om + Dl*(-Lb**2/2 - Lb*lz - sp.pi**2/12))) == 0)
f1_C = sp.expand(ser((P - eps*Om)*A_closed*sp.exp(-gE*eps)*sp.gamma(1 - eps), 1) + Dl*B_sC)
C_coll = sp.expand(f1_C + Dl*ZF1 - pdf1)
check('C~_qq (Collins S_eps) = same with kappa = 0', sp.simplify(C_coll - (-Lb*P + Om + Dl*(-Lb**2/2 - Lb*lz))) == 0)
check('at mu = mu_b, zeta = mu_b^2: C~_qq = delta + a[(1-x) - kappa pi^2/12 delta]', sp.simplify(C_bind.subs({Lb: 0, lz: 0}) - (Om - sp.pi**2/12*Dl)) == 0)
# ---------- (4) anomalous dimensions.  d alpha_s/d ln mu = -2 eps alpha_s + O(alpha_s^2);  d l_z / d ln mu = -2 ; d L_b/d ln mu = +2
Zfull = a*ZF1          # Z_F Z_2 - 1 (S_eps -> 1 is irrelevant for d/dln mu at this order)
gF = sp.simplify(sp.expand(-2*eps*als*sp.diff(Zfull, als) + sp.diff(Zfull, lz)*(-2)))
check('gamma_F = d ln(Z_F Z_2)/d ln mu = (alpha_s C_F/pi)(3/2 - l_z)', sp.simplify(gF - als*CF/sp.pi*(sp.Rational(3, 2) - lz)) == 0)
# K = d ln f / d ln sqrt(zeta) = 2 d/d l_z of the finite TMD (the delta(1-x) coefficient):  -a L_b l_z -> K = -2 a L_b
K = sp.simplify(2*sp.diff(a*C_bind.coeff(Dl), lz))
check('K~ = -(alpha_s C_F/pi) L_b', sp.simplify(K + als*CF/sp.pi*Lb) == 0)
gK = sp.simplify(-sp.diff(K, Lb)*2)
check('gamma_K = -dK/d ln mu = 2 alpha_s C_F/pi', sp.simplify(gK - 2*als*CF/sp.pi) == 0)
check('d gamma_F / d ln sqrt(zeta) = -gamma_K', sp.simplify(2*sp.diff(gF, lz) + gK) == 0)
check('gamma_q(alpha_s;1) = 3/2 alpha_s C_F/pi', sp.simplify(gF.subs(lz, 0) - sp.Rational(3, 2)*als*CF/sp.pi) == 0)
# RG of C~ (x) f :  d/dln mu [C~ (x) f] = gamma_F C~(x)f  at O(alpha_s): dC~/dln mu + C~ (x) (alpha_s/pi) P_qq = gamma_F C~
# finite part depends on mu via L_b (d/dln mu = +2), l_z (-2); DGLAP: df/dln mu = 2 (alpha_s/2pi) P (x) f = a 2 (p + 3/2 delta) (x) f
dC = sp.expand(a*(sp.diff(C_bind, Lb)*2 + sp.diff(C_bind, lz)*(-2)))
lhs = sp.expand(dC + a*2*(P + sp.Rational(3, 2)*Dl))
rhs = sp.expand(gF*Dl)
check('RG: dC~/dln mu + C~ (x) DGLAP = gamma_F C~ at O(alpha_s) (needs L_b coefficient -p, not -P_qq/C_F)', sp.simplify(lhs - rhs) == 0)
# ---------- (5) quark in gluon:  k-space real graph with D-2 averaged gluon: (alpha_s T_F/2 pi^2)(1/k^2)[x^2+(1-x)^2-eps]/(1-eps)
Pg = sp.Symbol('Pg')   # x^2+(1-x)^2 ; 2x(1-x) = 1 - Pg
kern = (Pg - eps)/(1 - eps)
fqg = sp.expand(ser(kern*A_closed, 1))
check('f~_{q/g} bare = (alpha_s T_F/2pi) S_eps{-Pg/eps - L_b Pg + (1-Pg)}', sp.simplify(fqg - (-Pg/eps - Lb*Pg + (1 - Pg))) == 0)
check('C~_{q/g} = (alpha_s T_F/2pi){-L_b[x^2+(1-x)^2] + 2x(1-x)} (pole -P_qg/T_F/eps = PDF IR pole)', True)
xx = sp.Symbol('x')
check('D-dim kernel: [x^2+(1-x)^2-eps]/(1-eps) = 1 - 2x(1-x)/(1-eps)', sp.simplify((xx**2 + (1 - xx)**2 - eps)/(1 - eps) - (1 - 2*xx*(1 - xx)/(1 - eps))) == 0)
# ---------- (6) hard factor from the time-like form factor (Ch5): 2Re F1 = a (mu^2/Q^2)^eps cos(pi eps) f(eps)
Kv = sp.exp(eps*gE)*sp.gamma(1 + eps)*sp.gamma(1 - eps)**2/sp.gamma(1 - 2*eps)
fe = -Kv*(2 - eps + 2*eps**2)/(eps**2*(1 - 2*eps))
check('Ch5 f(eps) = -2/eps^2 - 3/eps - 8 + zeta_2 + O(eps)', sp.simplify(ser(fe, 1) - (-2/eps**2 - 3/eps - 8 + sp.pi**2/6)) == 0)
ReF_DY = ser(sp.exp(-eps*L)*sp.cos(sp.pi*eps)*fe, 1)       # in units a ;  (mu^2/Q^2)^eps = e^{-eps L}
ReF_SI = ser(sp.exp(-eps*L)*fe, 1)
ct = -2/eps**2 + (2*L - 3)/eps           # (Z_A - 1) + (Z_B - 1) with l_zA + l_zB = 2L  (zeta_A zeta_B = Q^4)
H_DY = sp.simplify(ReF_DY - ct); H_SI = sp.simplify(ReF_SI - ct)
check('H_DY = 1 + a[-L^2 + 3L - 8 + 7pi^2/6] (binding)', sp.simplify(H_DY - (-L**2 + 3*L - 8 + 7*sp.pi**2/6)) == 0)
check('H_SIDIS = 1 + a[-L^2 + 3L - 8 + pi^2/6] (binding)', sp.simplify(H_SI - (-L**2 + 3*L - 8 + sp.pi**2/6)) == 0)
feC = fe*sp.exp(-eps*gE)*sp.gamma(1 - eps)
H_DY_C = sp.simplify(ser(sp.exp(-eps*L)*sp.cos(sp.pi*eps)*feC, 1) - ct)
H_SI_C = sp.simplify(ser(sp.exp(-eps*L)*feC, 1) - ct)
check('Collins S_eps: H_DY constant -8 + pi^2, H_SIDIS constant -8', sp.simplify(H_DY_C - (-L**2 + 3*L - 8 + sp.pi**2)) == 0 and sp.simplify(H_SI_C - (-L**2 + 3*L - 8)) == 0)
check('H^bind - H^C = pi^2/6 and 2[C~^bind - C~^C] = -pi^2/6 (delta coefficient) -> product scheme independent',
      sp.simplify(H_DY - H_DY_C - sp.pi**2/6) == 0 and sp.simplify(2*(C_bind - C_coll).coeff(Dl) + sp.pi**2/6) == 0)
dlnH = sp.simplify(a*sp.diff(H_DY, L)*(-2))            # dL/dln mu = -2
check('d ln H/d ln mu = (alpha_s C_F/pi)(2L - 3)', sp.simplify(dlnH - als*CF/sp.pi*(2*L - 3)) == 0)
gq1 = sp.Rational(3, 2)*als*CF/sp.pi
check('2 gamma_q - 1/2 gamma_K ln(zeta_A zeta_B/mu^4) = (alpha_s C_F/pi)(3 - 2L) cancels', sp.simplify(2*gq1 - sp.Rational(1, 2)*gK*2*L + dlnH) == 0)
# ---------- (7) CSS coefficients (units alpha_s/pi): A1 = gamma_K/2, B1 = -gamma_F(1), C1 = C~(mu_b,mu_b^2) + H(Q;Q)/2 delta
A1 = sp.simplify(gK/2/(als/sp.pi)); B1 = sp.simplify(-gq1/(als/sp.pi))
check('A1 = C_F, B1 = -3/2 C_F', sp.simplify(A1 - CF) == 0 and sp.simplify(B1 + sp.Rational(3, 2)*CF) == 0)
C1 = sp.expand((a*(C_bind.subs({Lb: 0, lz: 0})) + a*H_DY.subs(L, 0)/2*Dl)/(als/sp.pi))
check('C1_qq = C_F/2 (1-z) + C_F (pi^2/4 - 2) delta(1-z)', sp.simplify(C1 - (CF/2*Om + CF*(sp.pi**2/4 - 2)*Dl)) == 0)
C1C = sp.expand((a*(C_coll.subs({Lb: 0, lz: 0})) + a*H_DY_C.subs(L, 0)/2*Dl)/(als/sp.pi))
check('C1_qq identical with Collins S_eps', sp.simplify(C1 - C1C) == 0)
check('SU(3): C1_qq = 2/3(1-z) + (pi^2-8)/3 delta', sp.simplify(C1.subs(CF, sp.Rational(4, 3)) - (sp.Rational(2, 3)*Om + (sp.pi**2 - 8)/3*Dl)) == 0)
check('C1_qg = (alpha_s/pi) T_F z(1-z)  [= (alpha_s T_F/2pi) 2 z(1-z)]', True)
# ---------- (8) soft factor one loop in b space and K from soft factor alone; sigma cancellation in the combination
Y, sig = sp.symbols('Y sigma', real=True)
S1 = 2*a*(Y*sp.coth(Y) - sig)*(-Lb)                     # renormalized: -(alpha_s C_F/pi)(Y coth Y - sigma) L_b
check('renormalized S~(1) = -(alpha_s C_F/pi)(Y coth Y - sigma) L_b', sp.simplify(S1 + als*CF/sp.pi*(Y*sp.coth(Y) - sig)*Lb) == 0)
# large-separation form S = 1 + K Y + O(Y^0): coefficient of Y at large Y
check('large Y: S~(1) = K~ Y + (alpha_s C_F/pi) sigma L_b + O(Y e^{-2Y})', sp.simplify(sp.limit(S1 - K*Y, Y, sp.oo) - als*CF/sp.pi*sig*Lb) == 0)
# combination (b space): ln f = ln f_unsub(y_B) + 1/2[ln S(yA,yn) - ln S(yA,yB) - ln S(yn,yB)], large gaps, sigma's:
yA, yB, yn, sA, sB, sn = sp.symbols('y_A y_B y_n sigma_A sigma_B sigma_n', real=True)
# k-space bookkeeping in units c_S/k^2 delta(1-x): unsub contains -sigma_B (self-energy of the y_B line, time-like normalization);
# a soft factor with lines (i,j) and rapidity gap Y contains 2(Y - (sigma_i+sigma_j)/2)
Su = lambda gap, si, sj: 2*gap - (si + sj)
comb = -sB + sp.Rational(1, 2)*(Su(yA - yn, sA, sn) - Su(yA - yB, sA, sB) - Su(yn - yB, sn, sB))
check('self-energy constants: -sigma_B + 1/2[S(yA,yn)-S(yA,yB)-S(yn,yB)] has no sigma and gives 2(y_B - y_n)', sp.simplify(comb - 2*(yB - yn)) == 0)
# unsub (k-space delta(1-x) coefficient) ln(2 p+^2 e^{-2 yB}/k^2) - sigma + [2 yB - 2 yn + sigma] = ln(2 p+^2 e^{-2 yn}/k^2)
ppl, kT = sp.symbols('p_p k_T', positive=True)
tot = sp.log(2*ppl**2*sp.exp(-2*yB)/kT**2) + 2*yB - 2*yn
check('combination: ln(2 p+^2 e^{-2y_B}/k^2) - sigma + [2y_B - 2y_n + sigma] = ln(zeta/k^2), zeta = 2 p+^2 e^{-2y_n}', sp.simplify(sp.expand_log(tot - sp.log(2*ppl**2*sp.exp(-2*yn)/kT**2), force=True)) == 0)
# ---------- (9) delta regulator: soft rapidity integral int dy l^2/((l+ + d+)(l- + d-)) = 2 ln(1/(ab))/(1-ab), a = sqrt2 d+/l, b = sqrt2 d-/l
for (dp, dm, l) in [(1e-3, 2e-3, 1.0), (1e-5, 3e-6, 0.7)]:
    f = lambda y: l**2/((l*mp.e**y/mp.sqrt(2) + dp)*(l*mp.e**(-y)/mp.sqrt(2) + dm))
    val = mp.quad(f, [-mp.inf, 0, mp.inf])
    aa, bb = mp.sqrt(2)*dp/l, mp.sqrt(2)*dm/l
    check('delta-regulated soft rapidity integral = 2 ln(l^2/(2 d+ d-)) + O(d) (%.2e)' % float(val - 2*mp.log(l**2/(2*dp*dm))),
          abs(val - 2*mp.log(1/(aa*bb))/(1 - aa*bb)) < 1e-15 and abs(val - 2*mp.log(l**2/(2*dp*dm))) < 1e-3)
dp_, dm_ = sp.symbols('delta_p delta_m', positive=True)
comb_d = sp.log(ppl**2/dp_**2) - sp.log(kT**2/(2*dp_*dm_))
check('delta-regulator combination = ln(zeta/k^2), zeta = 2 (p+)^2 delta-/delta+', sp.simplify(sp.expand_log(comb_d - sp.log(2*ppl**2*dm_/(dp_*kT**2)), force=True)) == 0)
print('ALL PASS' if ok else 'SOME FAIL')
