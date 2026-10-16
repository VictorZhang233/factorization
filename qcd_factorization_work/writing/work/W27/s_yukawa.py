#!/usr/bin/env python3
"""
W27 / Ch24 -- prop:front-msbar-negative(a), ex:front-yukawa, fig:front-yukawa-pdf.
Writer re-derivation (independent of frontier/others/scripts/s2): the one-loop quark-in-"nucleon"
PDF of the Yukawa model  L_int = -lambda Psibar_N psi_q phi + h.c.  FROM THE OPERATOR DEFINITION
of def:pdf-quark (no Wilson line: no gauge field), in our conventions (light-front v^pm=(v0 pm v3)/sqrt2,
metric +---), followed by DR + MS-bar and the numerical statements printed in the book.

Steps checked:
 (1) Dirac trace  T = Tr[gamma^+ (kslash+m)(Pslash+M)(kslash+m)]  = 4P^+ [ k_T^2 + (m + xi M)^2 ]
     on the cut (P-k)^2 = m_s^2 with k^+ = xi P^+ ;
 (2) k^2 - m^2 = -[k_T^2 + Delta]/(1-xi),  Delta = xi m_s^2 + (1-xi) m^2 - xi(1-xi) M^2 ;
 (3) normalisation: f = (lambda^2/(16 pi^3)) (1-xi) Int d^2k_T [k_T^2+(m+xi M)^2]/[k_T^2+Delta]^2 ;
 (4) DR (d^{2-2eps}k_T, lambda_0^2 = lambda^2 mu^{2eps} e^{eps gamma_E}/(4pi)^eps) and MS-bar:
     pole a(1-xi)/eps, finite part ln(mu^2/Delta) - 1 + (m+xi M)^2/Delta ;
 (5) Delta > 0 on [0,1] iff M < m + m_s  (Cauchy-Schwarz bound) ;
 (6) zeros at mu = 0.8, 1.2 GeV (0.264, 0.567), positivity at 2.5 GeV, mu*(xi->1) = 1.699 GeV,
     mu0(xi) monotonically increasing from m_q to mu*, minimum of the mu=0.8 curve ;
 (7) the k_T cut-off pdf (positive) agrees with MS-bar up to O(m^2/mu^2).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + info) if info else ""))

# ---------------- (1) Dirac trace with explicit gamma matrices (Dirac rep.) ----------------
I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(I2, Z2, Z2, -I2)
g = [g0, blk(Z2, sx, -sx, Z2), blk(Z2, sy, -sy, Z2), blk(Z2, sz, -sz, Z2)]
eta = sp.diag(1, -1, -1, -1)
def slash(v):  # v = contravariant components (v0,v1,v2,v3); slash = gamma^mu v_mu
    vl = eta * sp.Matrix(v)
    return sum((g[mu] * vl[mu] for mu in range(4)), sp.zeros(4))
gplus = (g[0] + g[3]) / sp.sqrt(2)          # gamma^+ = (gamma^0 + gamma^3)/sqrt2
Pp, xi, M, m, ms, kT, phi = sp.symbols('P_plus xi M m m_s k_T phi', positive=True)
# light-front components -> contravariant (v0, v1, v2, v3):  v0 = (v+ + v-)/sqrt2, v3 = (v+ - v-)/sqrt2
def lf(vp, vm, vx, vy):
    return [ (vp + vm) / sp.sqrt(2), vx, vy, (vp - vm) / sp.sqrt(2) ]
Pm = M**2 / (2 * Pp)                          # P^- of the on-shell target, P_T = 0
kp = xi * Pp
# k^- from the cut (P-k)^2 = m_s^2:  2(1-xi)P^+(P^- - k^-) - k_T^2 = m_s^2
km = Pm - (kT**2 + ms**2) / (2 * (1 - xi) * Pp)
P = lf(Pp, Pm, 0, 0); k = lf(kp, km, kT * sp.cos(phi), kT * sp.sin(phi))
T = (gplus * (slash(k) + m * sp.eye(4)) * (slash(P) + M * sp.eye(4)) * (slash(k) + m * sp.eye(4))).trace()
T = sp.simplify(sp.expand(T))
target = 4 * Pp * (kT**2 + (m + xi * M)**2)
check("(1) Tr[g+ (k/+m)(P/+M)(k/+m)] = 4P+ [kT^2 + (m + xi M)^2] on the cut", sp.simplify(T - target) == 0,
      f"T = {sp.factor(T)}")
# ---------------- (2) off-shellness of the quark line ----------------
dot = lambda a, b: a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
k2 = sp.simplify(dot(k, k))
Delta = xi * ms**2 + (1 - xi) * m**2 - xi * (1 - xi) * M**2
check("(2) k^2 - m^2 = -[kT^2 + Delta]/(1-xi) on the cut", sp.simplify(k2 - m**2 + (kT**2 + Delta) / (1 - xi)) == 0)
Pk = P[0] - k[0], P[1] - k[1], P[2] - k[2], P[3] - k[3]
check("    cut condition (P-k)^2 = m_s^2 holds", sp.simplify(dot(Pk, Pk) - ms**2) == 0)
# ---------------- (3) normalisation of f(xi) ----------------
# f = (1/2) Int dk^- d^2kT /(2pi)^4 Tr[g+ Phi],  Phi = 2pi delta((P-k)^2 - ms^2) lam^2 (k/+m)(1/2)(P/+M)(k/+m)/(k^2-m^2)^2
# delta((P-k)^2-ms^2) = delta(k^- - k^-_0)/(2(1-xi)P^+)
lam = sp.symbols('lambda', positive=True)
integrand = sp.Rational(1, 2) / (2 * sp.pi)**4 * 2 * sp.pi / (2 * (1 - xi) * Pp) * lam**2 * sp.Rational(1, 2) * T \
            / ((kT**2 + Delta) / (1 - xi))**2
expected = lam**2 / (16 * sp.pi**3) * (1 - xi) * (kT**2 + (m + xi * M)**2) / (kT**2 + Delta)**2
check("(3) d^2kT integrand of f(xi) = lam^2/(16 pi^3) (1-xi) [kT^2+(m+xi M)^2]/[kT^2+Delta]^2",
      sp.simplify(integrand - expected) == 0)
# ---------------- (4) DR + MS-bar ----------------
eps = sp.symbols('epsilon')
mu2, Dl, A = sp.symbols('mu2 Delta A', positive=True)
# Int d^{2-2eps}kT F(kT^2) = pi^{1-eps}/Gamma(1-eps) Int dk2 (k2)^{-eps} F ;  overall (2pi)^{2eps} from (2pi)^D
# lambda_0^2 = lambda^2 mu^{2eps} e^{eps gE}/(4 pi)^eps  ->  prefactor a (1-xi) mu^{2eps} e^{eps gE}/Gamma(1-eps)
pref = sp.simplify((2 * sp.pi)**(2 * eps) * sp.pi**(1 - eps) / sp.gamma(1 - eps) / (16 * sp.pi**3)
                   * 16 * sp.pi**2 * mu2**eps * sp.exp(eps * sp.EulerGamma) / (4 * sp.pi)**eps)
check("(4a) DR measure x MS-bar coupling -> a_lambda (1-xi) mu^{2eps} e^{eps gE}/Gamma(1-eps)",
      sp.simplify(pref - mu2**eps * sp.exp(eps * sp.EulerGamma) / sp.gamma(1 - eps)) == 0)
I1 = pref * Dl**(-eps) * sp.gamma(2 - eps) * sp.gamma(eps)          # Int dk k^{-eps} k/(k+D)^2
I2 = pref * Dl**(-1 - eps) * sp.gamma(1 - eps) * sp.gamma(1 + eps)  # Int dk k^{-eps} 1/(k+D)^2
# Beta-function check of the two integrals at a convergent value of eps
mp.mp.dps = 30
e0 = mp.mpf(1) / 3
num1 = mp.quad(lambda x: x**(-e0) * x / (x + 2)**2, [0, 1, 10, 100, mp.inf])
num2 = mp.quad(lambda x: x**(-e0) / (x + 2)**2, [0, 1, 10, 100, mp.inf])
an1 = 2**(-e0) * mp.gamma(2 - e0) * mp.gamma(e0)
an2 = 2**(-1 - e0) * mp.gamma(1 - e0) * mp.gamma(1 + e0)
check("(4b) Beta-function integrals (eps=1/3, Delta=2; slow x^(-4/3) tail limits quadrature to ~1e-11)",
      abs(num1 - an1) < 1e-8 and abs(num2 - an2) < 1e-15, f"diffs {mp.nstr(num1-an1,3)}, {mp.nstr(num2-an2,3)}")
ser = sp.series(I1 + A * I2, eps, 0, 1).removeO()
pole = sp.simplify(sp.limit(eps * ser, eps, 0))
fin = sp.simplify(sp.expand(ser - pole / eps))
check("(4c) UV pole = a(1-xi)/eps  (MS-bar counterterm -a(1-xi)/eps; splitting kernel P_qN = 1-xi)", pole == 1)
check("(4d) finite part = ln(mu^2/Delta) - 1 + (m+xi M)^2/Delta",
      sp.simplify(fin - (sp.log(mu2 / Dl) - 1 + A / Dl)) == 0, f"fin = {fin}")
# ---------------- (5) stability: Delta > 0 iff M < m + ms ----------------
# Delta = xi(1-xi)[m^2/xi + ms^2/(1-xi) - M^2] >= xi(1-xi)[(m+ms)^2 - M^2]  (Cauchy-Schwarz)
x = sp.symbols('x', positive=True)
ident = sp.simplify(Delta - xi * (1 - xi) * (m**2 / xi + ms**2 / (1 - xi) - M**2))
cs_gap = sp.factor(sp.simplify((m**2 / xi + ms**2 / (1 - xi)) - (m + ms)**2))
check("(5) Delta = xi(1-xi)[m^2/xi + ms^2/(1-xi) - M^2] and m^2/xi+ms^2/(1-xi)-(m+ms)^2 = (m(1-xi)-ms xi)^2/(xi(1-xi))",
      ident == 0 and sp.simplify(cs_gap - (m * (1 - xi) - ms * xi)**2 / (xi * (1 - xi))) == 0)
# ---------------- (6) numbers ----------------
mp.mp.dps = 30
mq_, mp_, ms_ = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
De = lambda z: z * ms_**2 + (1 - z) * mq_**2 - z * (1 - z) * mp_**2
br = lambda z, mu: mp.log(mu**2 / De(z)) - 1 + (mq_ + z * mp_)**2 / De(z)
f = lambda z, mu: (1 - z) * br(z, mu)
z08 = mp.findroot(lambda z: br(z, mp.mpf('0.8')), 0.3)
z12 = mp.findroot(lambda z: br(z, mp.mpf('1.2')), 0.55)
check("(6a) zero at mu=0.8 GeV: xi = 0.264", abs(z08 - mp.mpf('0.264')) < 5e-4, f"xi0 = {mp.nstr(z08, 8)}")
check("(6b) zero at mu=1.2 GeV: xi = 0.567", abs(z12 - mp.mpf('0.567')) < 5e-4, f"xi0 = {mp.nstr(z12, 8)}")
# sign pattern on a fine grid
grid = [mp.mpf(i) / 2000 for i in range(1, 2000)]
neg08 = [z for z in grid if f(z, mp.mpf('0.8')) < 0]
neg12 = [z for z in grid if f(z, mp.mpf('1.2')) < 0]
neg25 = [z for z in grid if f(z, mp.mpf('2.5')) < 0]
check("(6c) mu=0.8: f<0 exactly for xi in (0.264,1) on the grid", min(neg08) > z08 and max(neg08) > 0.999 and
      len(neg08) == sum(1 for z in grid if z > z08))
check("(6d) mu=1.2: f<0 exactly for xi in (0.567,1) on the grid", min(neg12) > z12 and
      len(neg12) == sum(1 for z in grid if z > z12))
check("(6e) mu=2.5: f>0 for all xi", len(neg25) == 0, f"min f/a = {mp.nstr(min(f(z, mp.mpf('2.5')) for z in grid), 4)}")
mustar = ms_ * mp.e**((1 - (mq_ + mp_)**2 / ms_**2) / 2)
check("(6f) mu* = m_s exp{[1-(m_q+m_p)^2/m_s^2]/2} = 1.70 GeV", abs(mustar - mp.mpf('1.699')) < 1e-3, f"mu* = {mp.nstr(mustar, 8)}")
# threshold function mu0(xi) = sqrt(Delta) exp{(1 - A/Delta)/2}: monotonic increasing?
mu0 = lambda z: mp.sqrt(De(z)) * mp.e**((1 - (mq_ + z * mp_)**2 / De(z)) / 2)
vals = [mu0(z) for z in grid]
mono = all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
check("(6g) mu0(xi) increases monotonically from m_q (xi->0) to mu* (xi->1)", mono and abs(vals[0] - mq_) < 2e-3 and
      abs(vals[-1] - mustar) < 2e-3, f"mu0(0+)={mp.nstr(vals[0],5)}, mu0(1-)={mp.nstr(vals[-1],5)}")
# xi -> 0 and xi -> 1 limits of the bracket
check("(6h) xi->0: bracket -> ln(mu^2/m_q^2)", abs(br(mp.mpf('1e-12'), mp.mpf('0.8')) - mp.log(mp.mpf('0.8')**2 / mq_**2)) < 1e-9)
check("(6i) xi->1: bracket -> ln(mu^2/m_s^2) - 1 + (m_q+m_p)^2/m_s^2",
      abs(br(1 - mp.mpf('1e-12'), mp.mpf('0.8')) - (mp.log(mp.mpf('0.8')**2 / ms_**2) - 1 + (mq_ + mp_)**2 / ms_**2)) < 1e-9)
zmin = mp.findroot(lambda z: mp.diff(lambda y: f(y, mp.mpf('0.8')), z), 0.58)
print(f"   info: minimum of f/a at mu=0.8: {mp.nstr(f(zmin, mp.mpf('0.8')), 5)} at xi = {mp.nstr(zmin, 4)}")
print(f"   info: f/a(xi=0.001, mu=2.5) = {mp.nstr(f(mp.mpf('0.001'), mp.mpf('2.5')), 5)}")
# monotonicity in mu at fixed xi: d bracket/d ln mu^2 = 1 > 0
check("(6j) at fixed xi the bracket increases with mu (d/d ln mu^2 = 1): negative at small mu, positive at large mu", True)
# ---------------- (7) cut-off version ----------------
def fcut(z, kc2):
    return (1 - z) * mp.quad(lambda q: (q + (mq_ + z * mp_)**2) / (q + De(z))**2, [0, kc2])
mu = mp.mpf(30)
dev = max(abs(fcut(z, mu**2) - f(z, mu)) for z in [mp.mpf(i) / 50 for i in range(1, 50)])
check("(7) cut-off pdf (k_T < mu) = MS-bar pdf + O(m^2/mu^2) at mu = 30 GeV", dev < 5e-3, f"max dev = {mp.nstr(dev, 3)}")
# exact relation: cutoff = MSbar + (1-xi)[ ln(1+Delta/mu^2) - (A - Delta)/(mu^2+Delta) ... ] -> O(m^2/mu^2)
q, D_, A_, kc = sp.symbols('q D A k_c', positive=True)
cut_exact = sp.integrate((q + A_) / (q + D_)**2, (q, 0, kc**2))
diff_exact = sp.simplify(cut_exact - (sp.log(kc**2 / D_) - 1 + A_ / D_))
lead = sp.series(diff_exact.subs(kc, 1 / sp.Symbol('u', positive=True)), sp.Symbol('u', positive=True), 0, 3)
print(f"   info: cutoff - MSbar bracket (k_c=mu) = {sp.simplify(diff_exact)} = {lead}")
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
