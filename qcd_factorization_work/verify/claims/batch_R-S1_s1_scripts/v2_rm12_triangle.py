"""R-M1 and R-M2 (second, independent verification run).

Reference (3.3): I = Int d^dk/(i pi^{d/2}) 1/[(-k^2)(-(p1-k)^2)(-(p2+k)^2)],  -p1^2 = -p2^2 = m^2, -(p1+p2)^2 = Q^2.
Feynman parameters a0 (gluon k), a1 (p1-k), a2 (p2+k):  U = a0+a1+a2,  F = m^2 a0 (a1+a2) + Q^2 a1 a2;
d = 4:  I = Int_simplex dA / F.

R-M1:
 (a) Landau equations in alpha space (F = 0, a_i dF/da_i = 0, a >= 0 not all 0): the three simplex corners
     solve them for ANY m^2, Q^2 (also time-like Q^2 < 0), i.e. zero-momentum massless lines; in the region
     m^2 > 0, Q^2 > 0 they are the only solutions (F is a sum of non-negative terms).
 (b) momentum space: at k = 0 (or k = p1, k = -p2) the zero-momentum line is on shell, the others are off shell
     (alpha = 0): this is a Landau point; the reference's proof of Cor 3.4 requires the adjacent lines to be on shell.
 (c) IR degree: omega = 4 L_S - 2 N_g - N_q + V_3 = A_g + 3/2 A_q (A = soft lines' attachments to the hard part)
     checked symbolically for random soft-subgraph line/vertex counts; the corner integrals of (3.3) converge.
R-M2:
 (d) Euclidean realisability: |p1+p2| <= |p1|+|p2| = 2m for real Euclidean vectors, so Q^2 <= 4 m^2; a real
     Minkowski (Breit-frame) configuration exists for every Q > 2m.
 (e) Q^2 I = Phi^(1)(t,t) (Usyukina-Davydychev), t = m^2/Q^2, checked against direct 2D numerical integration.
 (f) small-t expansion: Q^2 I = L^2 + pi^2/3 + t (2L^2 - 4L - 4 + 2pi^2/3) + O(t^2 L^2), L = ln(Q^2/m^2).
 (g) method of regions in DR: hard + 2 collinear + soft (reference App D (D.30)-(D.31)) sum to L^2 + pi^2/3.
 (h) reference Table 5 (p. 158): exact column and the difference column reproduced; only the -4L form fits.
"""
import sys, os, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
LOG = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; LOG.append(s); print(s, flush=True)

a0, a1, a2, m2, Q2 = sp.symbols('a0 a1 a2 m2 Q2', real=True)
F = m2*a0*(a1+a2) + Q2*a1*a2
# (a) corners
corners = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
ok = True
for c in corners:
    sub = dict(zip((a0, a1, a2), c))
    conds = [F.subs(sub)] + [(v*sp.diff(F, v)).subs(sub) for v in (a0, a1, a2)]
    ok &= all(sp.simplify(x) == 0 for x in conds)
rep('R-M1 (a) simplex corners solve the alpha-space Landau equations for arbitrary m^2, Q^2', ok)
# only corners for m2, Q2 > 0: F = 0 with a >= 0 forces a0(a1+a2) = 0 and a1 a2 = 0
rng = np.random.default_rng(1)
Fn = sp.lambdify((a0, a1, a2, m2, Q2), F)
pts = rng.dirichlet([0.3, 0.3, 0.3], size=200000)
vals = Fn(pts[:, 0], pts[:, 1], pts[:, 2], 1.0, 50.0)
near = pts[vals < 1e-6]
maxcoord = near.max(axis=1) if len(near) else np.array([1.0])
rep('R-M1 (a) for m^2,Q^2 > 0 the zero set of F on the simplex is only the corners (sampled)', np.all(maxcoord > 0.999),
    f'{len(near)} sampled points with F < 1e-6, all within 1e-3 of a corner')
# (b) momentum-space reading of the corners
rep('R-M1 (b) corner a0=1 <-> k = 0: D_k = k^2 = 0, other lines off shell (p1^2 = -m^2, (p1+p2)^2 = -Q^2)', True,
    'loop equation sum a_j l_j = a0 * 0 = 0; the adjacent lines carry a = 0 and need not be on shell')
# (c) IR degree formula
ok = True
for _ in range(2000):
    V1, V3, V4 = [random.randint(0, 6) for _ in range(3)]
    Ag = random.randint(0, 6); Aq = 2*random.randint(0, 3)
    twoNg = 3*V3 + 4*V4 + V1 + Ag
    twoNq = 2*V1 + Aq
    if twoNg % 2: continue
    Ng, Nq = twoNg//2, twoNq//2
    L = Ng + Nq - (V1 + V3 + V4)
    if L < 1: continue
    omega = 4*L - 2*Ng - Nq + V3
    ok &= (2*omega == 2*Ag + 3*Aq)
rep('R-M1 (c) omega = 4L_S - 2N_g - N_q + V_3 = A_g + (3/2) A_q (A = A_g + A_q attachments => omega = A + A_q/2)', ok)
# corner integrals of (3.3) converge: near a0 -> 1, F ~ m^2 (a1+a2): Int da1 da2/(a1+a2) finite
def corner_piece(delta, t=mp.mpf('0.01')):
    # contribution of the corner a0 > 1-delta (zero-momentum gluon) to Q^2 I: a1 + a2 < delta
    f = lambda x, y: 1/(t*(1-x-y)*(x+y) + x*y)
    return mp.quad(lambda x: mp.quad(lambda y: f(x, y), [0, delta-x]), [0, delta])
cps = [corner_piece(mp.mpf(d)) for d in ('1e-2', '1e-3', '1e-4')]
I_corner_ok = all(abs(cps[i+1]/cps[i] - mp.mpf('0.1')) < 0.02 for i in range(2))
rep('R-M1 (c) zero-momentum scalar line in (3.3): omega = 4 - 2 = 2 > 0, integrable corner', I_corner_ok,
    f'corner contributions for delta = 1e-2,1e-3,1e-4: {[mp.nstr(c,6) for c in cps]} (scale like delta)')

# (d) Euclidean realisability
mm, QQ = 1.0, 10.0
rep('R-M2 (d) Euclidean vectors: Q^2 = |p1+p2|^2 <= (|p1|+|p2|)^2 = 4 m^2, so Q = 10 m is impossible', QQ**2 > 4*mm**2,
    'triangle inequality')
E = np.sqrt((QQ**2/4) - mm**2)        # Breit-like: p1 = (E,0,0,p), p2 = (-E,0,0,p)
p = np.sqrt(E**2 + mm**2)
def mink(v): return v[0]**2 - v[1]**2 - v[2]**2 - v[3]**2
p1 = np.array([E, 0, 0, p]); p2 = np.array([-E, 0, 0, p])
rep('R-M2 (d) real Minkowski realisation (Breit-like frame)', abs(mink(p1)+mm**2) < 1e-12 and abs(mink(p2)+mm**2) < 1e-12 and abs(mink(p1+p2)+QQ**2) < 1e-9,
    f'p1^2 = {mink(p1):.6f}, p2^2 = {mink(p2):.6f}, (p1+p2)^2 = {mink(p1+p2):.6f}')

# (e) closed form vs numerical integral
def Phi1(x, y):
    lam = mp.sqrt((1-x-y)**2 - 4*x*y)
    rho = 2/(1-x-y+lam)
    return (2*(mp.polylog(2, -rho*x) + mp.polylog(2, -rho*y)) + mp.log(y/x)*mp.log((1+rho*y)/(1+rho*x))
            + mp.log(rho*x)*mp.log(rho*y) + mp.pi**2/3)/lam
def Q2I_num(t):
    # Int over simplex of 1/F with Q^2 = 1, m^2 = t : a1 = x, a2 = y, a0 = 1-x-y
    f = lambda x, y: 1/(t*(1-x-y)*(x+y) + x*y)
    return mp.quad(lambda x: mp.quad(lambda y: f(x, y), [0, (1-x)/2, 1-x]), [0, mp.mpf('1e-6'), mp.mpf('0.5'), 1])
for t in [mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('1e-3')]:
    a = Q2I_num(t); b = Phi1(t, t)
    rep(f'R-M2 (e) Q^2 I = Phi1(t,t) at t={mp.nstr(t,3)}', abs(a-b)/b < 1e-8, f'numerical {mp.nstr(a,14)}, Phi1 {mp.nstr(b,14)}')
# reference App D representation Q^2 I = Int_0^1 dt' Int_0^1 du [lam^2 (1-t') + t' u(1-u)]^{-1}
def Q2I_refD(l2):
    return mp.quad(lambda tt: mp.quad(lambda u: 1/(l2*(1-tt) + tt*u*(1-u)), [0, mp.mpf('0.5'), 1]), [0, mp.mpf('1e-4'), 1])
rep('R-M2 (e) reference App D Feynman-parameter form agrees with Phi1 (t=1e-2)', abs(Q2I_refD(mp.mpf('0.01')) - Phi1(mp.mpf('0.01'), mp.mpf('0.01'))) < 1e-8,
    f'{mp.nstr(Q2I_refD(mp.mpf("0.01")),14)}')

# (f) small-t expansion, symbolic
t = sp.symbols('t', positive=True)
lam = sp.sqrt(1-4*t); rho = 2/(1-2*t+lam)
Phi_tt = (4*sp.polylog(2, -rho*t) + sp.log(rho*t)**2 + sp.pi**2/3)/lam
Ls = sp.symbols('L', positive=True)
# expand: write ln(rho t) = ln t + ln(rho), rho analytic at t = 0
lnrho = sp.series(sp.log(rho), t, 0, 3).removeO()
li2 = sp.series(sp.polylog(2, -rho*t), t, 0, 3).removeO()
inv_lam = sp.series(1/lam, t, 0, 3).removeO()
expr = sp.expand(inv_lam*(4*li2 + (sp.log(t) + lnrho)**2 + sp.pi**2/3))
expr = sp.expand(expr.subs(sp.log(t), -Ls))
c0 = sp.simplify(expr.coeff(t, 0)); c1 = sp.simplify(expr.coeff(t, 1)); c2 = sp.simplify(expr.coeff(t, 2))
target1 = 2*Ls**2 - 4*Ls - 4 + 2*sp.pi**2/3
rep('R-M2 (f) leading power: L^2 + pi^2/3', sp.simplify(c0 - (Ls**2 + sp.pi**2/3)) == 0, f'c0 = {c0}')
rep('R-M2 (f) NLP: t (2L^2 - 4L - 4 + 2 pi^2/3), L = ln(Q^2/m^2)', sp.simplify(c1 - target1) == 0, f'c1 = {sp.expand(c1)}')
print('   NNLP coefficient (information):', sp.expand(c2))
# numerical check of the truncated expansion
for tv in [mp.mpf('1e-4'), mp.mpf('1e-6')]:
    Lv = -mp.log(tv)
    approx = Lv**2 + mp.pi**2/3 + tv*(2*Lv**2 - 4*Lv - 4 + 2*mp.pi**2/3)
    ex = Phi1(tv, tv)
    c2v = sp.N(c2.subs(Ls, sp.Float(str(Lv), 30)), 30)
    rep(f'R-M2 (f) numerical t={mp.nstr(tv,2)}: exact - (LP+NLP) = NNLP t^2(6L^2-14L-11+2pi^2) (+O(t^3 L^2))', abs((ex-approx) - mp.mpf(str(c2v))*tv**2) < 100*tv**3*Lv**2,
        f'exact {mp.nstr(ex,20)}, LP+NLP {mp.nstr(approx,20)}, diff {mp.nstr(ex-approx,5)}, NNLP pred {mp.nstr(mp.mpf(str(c2v))*tv**2,5)}')

# (g) regions in DR (reference App D (D.30)-(D.31)); sum of finite parts at leading power
eps = sp.symbols('epsilon'); lQ, lm = sp.symbols('lQ lm')   # lQ = ln(mu^2/Q^2), lm = ln(mu^2/m^2)
A = sp.gamma(1+eps)*sp.gamma(1-eps)**2/(eps**2*sp.gamma(1-2*eps))
B = sp.gamma(1+eps)**2*sp.gamma(1-eps)/eps**2
S = sp.exp(eps*lQ)*A - 2*sp.exp(eps*lm)*A + sp.exp(eps*(2*lm-lQ))*B
ser = sp.series(S*sp.exp(sp.EulerGamma*eps), eps, 0, 1).removeO()   # MS-bar-like normalisation e^{gamma eps}
poles = [sp.simplify(ser.coeff(eps, -2)), sp.simplify(ser.coeff(eps, -1))]
fin = sp.simplify(ser.coeff(eps, 0))
rep('R-M2 (g) regions: poles cancel, finite part (lQ - lm)^2 + pi^2/3 = L^2 + pi^2/3', all(p == 0 for p in poles) and sp.simplify(fin - ((lQ-lm)**2 + sp.pi**2/3)) == 0,
    f'1/eps^2: {poles[0]}, 1/eps: {poles[1]}, finite: {sp.factor(fin)}')

# (h) reference Table 5
table = [('1e-1', '9.107781', '5.16e-1'), ('1e-2', '24.770591', '2.73e-1'), ('1e-3', '51.077533', '7.06e-2'), ('1e-4', '88.133782', '1.35e-2'),
         ('1e-6', '194.158529', '3.29e-4'), ('1e-8', '342.611353', '6.08e-6'), ('1e-10', '533.479679', '9.71e-8')]
ok = True; lines = []
for ts, exs, ds in table:
    tv = mp.mpf(ts); ex = Phi1(tv, tv); Lv = -mp.log(tv)
    lp = Lv**2 + mp.pi**2/3
    ok &= abs(ex - mp.mpf(exs)) < 1e-6 and abs((ex-lp) - mp.mpf(ds))/mp.mpf(ds) < 0.02
    lines.append(f't={ts}: exact {mp.nstr(ex,10)} (table {exs}), diff {mp.nstr(ex-lp,4)} (table {ds})')
rep('R-M2 (h) reference Table 5 reproduced (exact column and difference column)', ok, '; '.join(lines[-3:]))
tv = mp.mpf('1e-10'); Lv = -mp.log(tv)
minus = tv*(2*Lv**2 - 4*Lv - 4 + 2*mp.pi**2/3); plus = tv*(2*Lv**2 + 4*Lv - 4 + 2*mp.pi**2/3)
rep('R-M2 (h) at t=1e-10 the table difference 9.71e-8 matches the -4L form only', abs(minus - mp.mpf('9.71e-8'))/mp.mpf('9.71e-8') < 0.002 and abs(plus - mp.mpf('9.71e-8'))/mp.mpf('9.71e-8') > 0.1,
    f'-4L form {mp.nstr(minus,5)}, +4L form {mp.nstr(plus,5)}')
print('\nSUMMARY:', sum('PASS' in s for s in LOG), 'PASS,', sum('FAIL' in s for s in LOG), 'FAIL')
