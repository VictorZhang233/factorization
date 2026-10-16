"""W02 / Ch2 check s3: one-loop UV poles (MS-bar renormalization constants) in a general covariant gauge xi,
computed from the Feynman rules of def:prelim-feynman-rules by large-loop-momentum expansion.

Method.  For a one-loop graph of superficial degree omega, write every propagator 1/(l+q)^2 as a series in the
external momenta (q = t*qhat) and keep the t^omega term: it is homogeneous of degree -4 in l, the lower terms are
scaleless power divergences (zero in DR) and the higher ones are UV finite.  The angular average
l^{mu1}..l^{mu2n} -> (l^2)^n/(D(D+2)..(D+2n-2)) * sum of pairings of g (D -> 4 for the pole) and
int d^Dl/(2pi)^D (l^2)^{-2} = i/(16 pi^2 eps) + finite give the pole.  All vertex and propagator factors (with
their i's) are included, so the sum of graphs is i*Gamma_1PI; the counterterm vertices follow from
delta L = L(bare) - L(renormalised) with psi_0 = Z2^{1/2} psi, A_0 = Z3^{1/2} A, c_0 = Zt3^{1/2} c, and
Z_{1F}, Zt_1, Z_1, Z_4 the vertex constants (def:qcd-renormalization).  Results in units g^2/(16 pi^2 eps) =
alpha_s/(4 pi eps).  Colour factors are inserted per graph and checked numerically with SU(2), SU(3).
Run: python3 -I s3_oneloop_Z.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction
from sympy.polys.domains import QQ_I, QQ
from sympy.polys.rings import ring
import sympy as sp

R, l0, l1, l2, l3, iL, t, xi = ring('l0,l1,l2,l3,iL,t,xi', QQ_I)
LV = [l0, l1, l2, l3]
ONE = R(1); ZERO = R(0); I = R(QQ_I(0, 1))
G = [1, -1, -1, -1]
npass = nfail = 0
def report(ok, name):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)

TMAX = [2]
def trunc(p):
    return R({m: c for m, c in p.terms() if m[5] <= TMAX[0]})
def mul(a, b):
    return trunc(a * b)
def dot(a, b):
    return sum((G[m] * a[m] * b[m] for m in range(4)), ZERO)
def vec(c):            # rational external vector times t
    return [R(QQ(Fraction(x))) * t for x in c]
def cvec(c):           # rational constant vector (no t)
    return [R(QQ(Fraction(x))) for x in c]
def mom(sig, qhat):    # sig*l + t*qhat
    return [sig * LV[m] + (qhat[m] if qhat is not None else ZERO) for m in range(4)]
def invsq(sig, qhat, msq=None):
    """1/((sig l + q)^2 - m^2), q = t*qhat (vector of ring elements already containing t)."""
    if qhat is None:
        X = ZERO
    else:
        lq = dot(LV, qhat)
        X = 2 * sig * lq + dot(qhat, qhat)
    if msq is not None:
        X = X - msq
    res = ZERO; term = iL
    for n in range(TMAX[0] + 1):
        res = res + term
        term = trunc(-term * X * iL)
    return trunc(res)
# ---------------- Dirac algebra ----------------
def M0(): return [[ZERO] * 4 for _ in range(4)]
def Mid():
    m = M0()
    for i in range(4): m[i][i] = ONE
    return m
s1 = [[0, 1], [1, 0]]; s2 = [[0, -1j], [1j, 0]]; s3 = [[1, 0], [0, -1]]
def toR(z):
    z = complex(z); return R(QQ_I(Fraction(z.real).limit_denominator(10), Fraction(z.imag).limit_denominator(10)))
def gamma(mu):
    m = M0()
    if mu == 0:
        for i in range(4): m[i][i] = ONE if i < 2 else -ONE
        return m
    s = [s1, s2, s3][mu - 1]
    for i in range(2):
        for j in range(2):
            m[i][2 + j] = toR(s[i][j]); m[2 + i][j] = toR(-s[i][j])
    return m
GAM = [gamma(mu) for mu in range(4)]
def madd(a, b): return [[a[i][j] + b[i][j] for j in range(4)] for i in range(4)]
def msc(c, a): return [[trunc(c * a[i][j]) for j in range(4)] for i in range(4)]
def mmul(a, b):
    return [[trunc(sum((a[i][k] * b[k][j] for k in range(4)), ZERO)) for j in range(4)] for i in range(4)]
def slash(v):
    m = M0()
    for mu in range(4):
        m = madd(m, msc(G[mu] * v[mu], GAM[mu]))
    return m
def mtr(a): return trunc(sum((a[i][i] for i in range(4)), ZERO))
def Squark(sig, qhat, mass=None):
    """quark propagator i(qslash + m)/(q^2 - m^2); mass = t*mhat (ring element) or None."""
    q = mom(sig, qhat)
    num = slash(q)
    if mass is not None:
        num = madd(num, msc(mass, Mid()))
    den = invsq(sig, qhat, None if mass is None else trunc(mass * mass))
    return msc(I * den, num)
def Dgluon(sig, qhat):
    """gluon propagator D^{mu nu}(q) = -i/q^2 [g^{mu nu} - (1-xi) q^mu q^nu / q^2] (upper indices)."""
    q = mom(sig, qhat); iq = invsq(sig, qhat)
    D = [[ZERO] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            v = (G[m] * ONE if m == n else ZERO) - trunc((1 - xi) * q[m] * q[n] * iq)
            D[m][n] = trunc(-I * iq * v)
    return D
def V3kin(k, p, q):
    """kinematic part of the three-gluon vertex (all momenta incoming), coupling and f stripped: T^{mu nu rho}."""
    T = {}
    for m in range(4):
        for n in range(4):
            for r in range(4):
                v = ZERO
                if m == n: v += G[m] * (k[r] - p[r])
                if n == r: v += G[n] * (p[m] - q[m])
                if r == m: v += G[r] * (q[n] - k[n])
                T[(m, n, r)] = v
    return T
# ---------------- angular average and pole ----------------
def dfact(n):
    r = 1
    while n > 1: r *= n; n -= 2
    return r
AVG = {}
def avg_mon(a):
    if a in AVG: return AVG[a]
    if any(x % 2 for x in a):
        AVG[a] = Fraction(0); return AVG[a]
    n = sum(a) // 2
    num = 1
    for x in a: num *= dfact(x - 1)
    den = 1
    for j in range(n): den *= (4 + 2 * j)
    sgn = (-1) ** ((a[1] + a[2] + a[3]) // 2)
    AVG[a] = Fraction(sgn * num, den)
    return AVG[a]
def pole(p, order):
    """coefficient c such that the UV pole of int d^Dl/(2pi)^D p|_{t^order} is c * i/(16 pi^2 eps); c in QQ_I[xi]."""
    res = ZERO
    for m, c in p.terms():
        if m[5] != order: continue
        a = m[:4]; d = sum(a); k = m[4]
        if d - 2 * k != -4: continue
        w = avg_mon(a)
        if w == 0: continue
        res += R({(0, 0, 0, 0, 0, 0, m[6]): c * QQ_I(QQ(w.numerator, w.denominator), 0)})
    return res
def as_sym(p):
    x = sp.Symbol('xi')
    out = 0
    for m, c in p.terms():
        out += (sp.Rational(int(c.x.numerator), int(c.x.denominator)) + sp.I * sp.Rational(int(c.y.numerator), int(c.y.denominator))) * x**m[6]
    return sp.expand(out)
xs = sp.Symbol('xi')
CA, CF, TFnf = sp.symbols('C_A C_F T_Fn_f')

# ================= colour factors (checked numerically) =================
def su(N):
    gens = []
    for i in range(N):
        for j in range(i + 1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 1; gens.append(m / 2)
            m = np.zeros((N, N), complex); m[i, j] = -1j; m[j, i] = 1j; gens.append(m / 2)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k; gens.append(m / np.sqrt(2 * k * (k + 1)))
    tt = np.array(gens); n = len(tt)
    f = np.zeros((n, n, n))
    for a, b, c in itertools.product(range(n), repeat=3):
        f[a, b, c] = np.real(-2j * np.trace((tt[a] @ tt[b] - tt[b] @ tt[a]) @ tt[c]))
    return tt, f
for N in (2, 3):
    tt, f = su(N); n = len(tt)
    # ghost loop in gluon self-energy: f^{c a d} f^{d b c} = -C_A delta^{ab}
    report(np.allclose(np.einsum('cad,dbc->ab', f, f), -N * np.eye(n)), f'SU({N}) colour: ghost loop f^cad f^dbc = -C_A delta^ab')
    # ghost self-energy: f^{yxz} f^{wxy} = -C_A delta^{wz}
    report(np.allclose(np.einsum('yxz,wxy->wz', f, f), -N * np.eye(n)), f'SU({N}) colour: ghost self-energy f^yxz f^wxy = -C_A delta')
    # quark-gluon vertex graph B: f^{abc} t^c t^b = -(i C_A/2) t^a
    report(np.allclose(np.einsum('abc,cij,bjk->aik', f, tt, tt), -0.5j * N * tt), f'SU({N}) colour: f^abc t^c t^b = -(i C_A/2) t^a')
    # ghost vertex graph A: f^{w x y2} f^{y2 a y1} f^{y1 x z} = (C_A/2) f^{w a z}
    cA = np.einsum('wxp,paq,qxz->waz', f, f, f)
    report(np.allclose(cA, -0.5 * N * f), f'SU({N}) colour: ghost vertex graph A  f^wxy2 f^y2ay1 f^y1xz = -(C_A/2) f^waz')
    # ghost vertex graph B: f^{w u y} f^{y x z} f^{a x u} = c f^{waz}
    cB = np.einsum('wuy,yxz,axu->waz', f, f, f)
    report(np.allclose(cB, -0.5 * N * f), f'SU({N}) colour: ghost vertex graph B  f^wuy f^yxz f^axu = -(C_A/2) f^waz')

results = {}
# ================= quark self-energy (omega = 1), with mass ======================================
TMAX[0] = 1
phat = [Fraction(3, 2), Fraction(1, 3), Fraction(-1, 2), Fraction(2, 5)]
p = vec(phat)
mh = R(QQ(Fraction(7, 3))) * t          # mass of order t
Mtot = M0()
S = Squark(+1, p, mh)                     # quark momentum l + p
D = Dgluon(+1, None)                      # gluon momentum l (route: quark p+l, gluon -l: D even)
for mu in range(4):
    for nu in range(4):
        if D[mu][nu] == ZERO: continue
        term = mmul(mmul(msc(I, GAM[mu]), S), msc(I, GAM[nu]))       # (i g gamma^mu) S (i g gamma^nu), g = 1
        Mtot = madd(Mtot, msc(G[mu] * G[nu] * D[mu][nu], term))
# Mtot = sum of graphs / (g^2 C_F) = -i Sigma / (g^2 C_F)
Mp = [[pole(Mtot[i][j], 1) for j in range(4)] for i in range(4)]
# decompose: Mp = A pslash_hat + B mhat 1 (coefficients of the pole i/(16pi^2 eps))
psl = slash(cvec(phat)); p2 = dot(cvec(phat), cvec(phat))
trA = mtr(mmul(Mp, psl)); trB = mtr(Mp)
A = as_sym(trA) / (4 * as_sym(p2)); B = as_sym(trB) / (4 * sp.Rational(7, 3))
# -i Sigma_pole = (i/(16pi^2 eps)) g^2 C_F (A pslash + B m)  =>  Sigma_pole = -(g^2 C_F/(16pi^2 eps)) (A pslash + B m)
# counterterm: Sigma_pole = dZ2 pslash - (dZ2 + dZm) m
dZ2 = sp.simplify(-A * CF); dZm = sp.simplify(B * CF - dZ2)
results['Z2'] = dZ2; results['Zm'] = dZm
print('  dZ2 =', dZ2, '   dZm =', dZm)
report(sp.simplify(dZ2 - (-CF * xs)) == 0, 'quark field: dZ_2 = -C_F xi  (VF-QCD-4, VF-PDF-14)')
report(sp.simplify(dZm - (-3 * CF)) == 0, 'quark mass: dZ_m = -3 C_F (xi independent)')

# ================= gluon self-energy (omega = 2) =======================================================
TMAX[0] = 2
khat = [Fraction(2, 3), Fraction(-1, 2), Fraction(1, 4), Fraction(1, 5)]
k = vec(khat); kc = cvec(khat); k2 = dot(kc, kc)
# quark loop: -n_f T_F (ig)^2 Tr[gamma^nu S(l+k) gamma^mu S(l)]
Sq1 = Squark(+1, k); Sq0 = Squark(+1, None)
Piq = [[ZERO] * 4 for _ in range(4)]
for mu in range(4):
    for nu in range(4):
        tr = mtr(mmul(mmul(mmul(GAM[nu], Sq1), GAM[mu]), Sq0))
        Piq[mu][nu] = trunc(-1 * (I * I) * tr)     # times T_F n_f g^2
# gluon loop: 1/2 g^2 C_A T1^{mu r s} G_r G_s D^{r r'}(l) D^{s s'}(k-l) G_r' G_s' T2^{nu r' s'}
negk = [-x for x in k]
lm = mom(-1, None)                       # -l
lmk = [LV[m] - k[m] for m in range(4)]   # l - k
T1 = V3kin(k, lm, lmk)                   # legs (k,mu),(-l,rho),(l-k,sigma)
lp = mom(+1, None); kml = [k[m] - LV[m] for m in range(4)]
T2 = V3kin(negk, lp, kml)                # legs (-k,nu),(l,rho'),(k-l,sigma')
Dl = Dgluon(+1, None); Dkl = Dgluon(-1, k)
Pig = [[ZERO] * 4 for _ in range(4)]
for mu in range(4):
    for nu in range(4):
        acc = ZERO
        for r, s, r2, s2 in itertools.product(range(4), repeat=4):
            if Dl[r][r2] == ZERO or Dkl[s][s2] == ZERO: continue
            a = T1[(mu, r, s)]; b = T2[(nu, r2, s2)]
            if a == ZERO or b == ZERO: continue
            acc += trunc(trunc(a * b) * trunc(Dl[r][r2] * Dkl[s][s2]) * (G[r] * G[s] * G[r2] * G[s2]))
        Pig[mu][nu] = trunc(R(QQ(1, 2)) * acc)     # times C_A g^2
# ghost loop: (-1) (-g f^{cad} l^mu)(-g f^{dbc} (l-k)^nu) (i/l^2)(i/(l-k)^2); colour -C_A delta
ighost0 = invsq(+1, None); ighost1 = invsq(+1, negk)
Pigh = [[ZERO] * 4 for _ in range(4)]
for mu in range(4):
    for nu in range(4):
        Pigh[mu][nu] = trunc(-1 * (-1) * trunc(LV[mu] * lmk[nu]) * trunc(I * ighost0 * I * ighost1))   # times C_A g^2 (colour -1 included)
def poletensor(P, order):
    return [[as_sym(pole(P[m][n], order)) for n in range(4)] for m in range(4)]
Pq = poletensor(Piq, 2); Pg = poletensor(Pig, 2); Pgh = poletensor(Pigh, 2)
kup = [sp.Rational(x.numerator, x.denominator) for x in khat]
k2s = sum(G[m] * kup[m]**2 for m in range(4))
def transverse_coeff(P):
    # P^{mu nu} =? c (k^2 g^{mu nu} - k^mu k^nu); return c or None
    c = sp.simplify(P[1][2] / (-kup[1] * kup[2]))
    ok = all(sp.simplify(P[m][n] - c * ((G[m] if m == n else 0) * k2s - kup[m] * kup[n])) == 0 for m in range(4) for n in range(4))
    return c, ok
cq, okq = transverse_coeff(Pq)
report(okq, 'gluon self-energy, quark loop: pole proportional to (k^2 g - k k)')
# gluon and ghost loops separately are not transverse; their sum is
cg, okg = transverse_coeff(Pg); cgh, okgh = transverse_coeff(Pgh)
Psum = [[sp.simplify(Pg[m][n] + Pgh[m][n]) for n in range(4)] for m in range(4)]
cs, oks = transverse_coeff(Psum)
report((not okg) and (not okgh) and oks, 'gluon self-energy: gluon loop and ghost loop separately NOT transverse, their sum transverse')
# i Pi_pole = (i/(16pi^2 eps)) g^2 [...] (k^2 g - kk) ; counterterm -i dZ3 (k^2 g - kk) => dZ3 = coefficient
dZ3 = sp.simplify(cq * TFnf + cs * CA)
results['Z3'] = dZ3
print('  dZ3 =', dZ3)
report(sp.simplify(dZ3 - ((sp.Rational(13, 6) - xs / 2) * CA - sp.Rational(4, 3) * TFnf)) == 0,
       'gluon field: dZ_3 = (13/6 - xi/2) C_A - (4/3) T_F n_f  (VF-QCD-4, VF-PDF-14)')
# ================= ghost self-energy ======================================================================
TMAX[0] = 2
phg = [Fraction(5, 4), Fraction(1, 2), Fraction(-1, 3), Fraction(1, 6)]
pg = vec(phg); pgc = cvec(phg)
pml = [pg[m] - LV[m] for m in range(4)]            # internal ghost p - l
Dl = Dgluon(+1, None)
ig = invsq(-1, pg)                                   # 1/(p-l)^2
acc = ZERO
for a_, b_ in itertools.product(range(4), repeat=2):
    if Dl[a_][b_] == ZERO: continue
    acc += trunc(trunc(pml[a_] * pg[b_]) * Dl[a_][b_] * (G[a_] * G[b_]))
GH = trunc((-1) * (-1) * (-1) * trunc(acc * I * ig))   # (-g)^2 * colour(-C_A) -> factor -1 (times C_A g^2)
cgh2 = as_sym(pole(GH, 2))
pg2 = sum(G[m] * sp.Rational(phg[m].numerator, phg[m].denominator)**2 for m in range(4))
# diagrams_pole = (i/(16pi^2 eps)) C_A g^2 cgh2 ; counterterm i dZt3 p^2 => dZt3 = -cgh2/p^2 * C_A
dZt3 = sp.simplify(-cgh2 / pg2 * CA)
results['Zt3'] = dZt3
print('  dZt3 =', dZt3)
report(sp.simplify(dZt3 - (3 - xs) / 4 * CA) == 0, 'ghost field: dZt_3 = (3 - xi)/4 C_A  (VF-QCD-4)')

# ================= quark-gluon vertex (omega = 0, zero external momenta) ======================================
TMAX[0] = 0
S0 = Squark(+1, None); Sm0 = Squark(-1, None); Dl = Dgluon(+1, None)
VA = {}; VB = {}
for mu in range(4):
    accA = M0(); accB = M0()
    # graph A: (i gamma^s) S(l) (i gamma^mu) S(l) (i gamma^r) G_r G_s D^{rs}(l); colour (C_F - C_A/2)
    mid = mmul(mmul(S0, msc(I, GAM[mu])), S0)
    for r in range(4):
        for s_ in range(4):
            if Dl[r][s_] == ZERO: continue
            accA = madd(accA, msc(G[r] * G[s_] * Dl[r][s_], mmul(mmul(msc(I, GAM[s_]), mid), msc(I, GAM[r]))))
    # graph B: (i gamma^s) S(-l) (i gamma^r) G_r D^{r r'}(l) G_r' G_s D^{s s'}(l) G_s' T^{mu r' s'}(0, l, -l); colour -(i C_A/2)
    T = V3kin([ZERO] * 4, mom(+1, None), mom(-1, None))
    for r, s_ in itertools.product(range(4), repeat=2):
        line = mmul(mmul(msc(I, GAM[s_]), Sm0), msc(I, GAM[r]))
        for r2, s2 in itertools.product(range(4), repeat=2):
            if Dl[r][r2] == ZERO or Dl[s_][s2] == ZERO: continue
            tv = T[(mu, r2, s2)]
            if tv == ZERO: continue
            fac = trunc(trunc(Dl[r][r2] * Dl[s_][s2]) * tv * (G[r] * G[r2] * G[s_] * G[s2]))
            accB = madd(accB, msc(fac, line))
    VA[mu] = [[as_sym(pole(accA[i][j], 0)) for j in range(4)] for i in range(4)]
    VB[mu] = [[as_sym(pole(accB[i][j], 0)) for j in range(4)] for i in range(4)]
def coeff_gamma(Mpole, mu):
    # Mpole = c gamma^mu ? compare all entries
    gm = [[as_sym(GAM[mu][i][j]) for j in range(4)] for i in range(4)]
    idx = [(i, j) for i in range(4) for j in range(4) if gm[i][j] != 0][0]
    c = sp.simplify(Mpole[idx[0]][idx[1]] / gm[idx[0]][idx[1]])
    ok = all(sp.simplify(Mpole[i][j] - c * gm[i][j]) == 0 for i in range(4) for j in range(4))
    return c, ok
cA_, okA = coeff_gamma(VA[0], 0); cB_, okB = coeff_gamma(VB[0], 0)
okall = all(coeff_gamma(VA[m], m) == (cA_, True) and coeff_gamma(VB[m], m) == (cB_, True) for m in range(4))
report(okA and okB and okall, 'quark-gluon vertex: both graphs have poles proportional to gamma^mu (all mu)')
# sum_pole = (i/(16pi^2 eps)) g^3 [cA (C_F - C_A/2) + cB (-i C_A/2)] gamma^mu t^a ; counterterm i g dZ1F gamma^mu t^a
dZ1F = sp.simplify(-(cA_ * (CF - CA / 2) + cB_ * (-sp.I * CA / 2)))
results['Z1F'] = dZ1F
print('  graph A pole coefficient:', sp.simplify(-cA_), '  graph B:', sp.simplify(-cB_ * (-sp.I)), ' (per colour factor)')
print('  dZ1F =', dZ1F)
report(sp.simplify(dZ1F - (-(xs * CF + (3 + xs) / 4 * CA))) == 0, 'quark-gluon vertex: dZ_1F = -(xi C_F + (3+xi)/4 C_A)  (VF-QCD-4)')
report(sp.simplify(dZ1F.subs(xs, 1) - (-(CF + CA))) == 0, 'Feynman gauge: dZ_1F = -(C_F + C_A)  (writer re-derivation requested in VF-QCD-4)')

# ================= ghost-gluon vertex (pole proportional to outgoing ghost momentum p') ==========================
TMAX[0] = 0
pp = cvec([Fraction(3, 5), Fraction(-2, 3), Fraction(1, 4), Fraction(1, 2)])   # p' (constant vector)
negl = mom(-1, None); Dl = Dgluon(+1, None); ig0 = invsq(+1, None)
GVA = [ZERO] * 4; GVB = [ZERO] * 4
for mu in range(4):
    # graph A: v1: -f (-l)^alpha ; v2: -f (-l)^mu ; v3: -f p'^beta ; gluon D^{alpha beta}(l) G G; two ghost props (i/l^2)^2
    acc = ZERO
    for a_, b_ in itertools.product(range(4), repeat=2):
        if Dl[a_][b_] == ZERO: continue
        acc += trunc(trunc(negl[a_] * pp[b_]) * Dl[a_][b_] * (G[a_] * G[b_]))
    GVA[mu] = trunc((-1) ** 3 * trunc(acc * negl[mu]) * trunc(I * ig0 * I * ig0))          # times colour -(C_A/2) f^{waz}, g^3
    # graph B: v1: -f (-l)^alpha ; v2: -f p'^beta ; 3-vertex f^{a x u} T^{mu rho sigma}(0, l, -l); D^{alpha rho}(l), D^{sigma beta}(l)
    T = V3kin([ZERO] * 4, mom(+1, None), mom(-1, None))
    acc = ZERO
    for a_, r, s_, b_ in itertools.product(range(4), repeat=4):
        if Dl[a_][r] == ZERO or Dl[s_][b_] == ZERO: continue
        tv = T[(mu, r, s_)]
        if tv == ZERO: continue
        acc += trunc(trunc(negl[a_] * pp[b_]) * trunc(Dl[a_][r] * Dl[s_][b_]) * tv * (G[a_] * G[r] * G[s_] * G[b_]))
    GVB[mu] = trunc((-1) ** 2 * trunc(acc * I * ig0))                                       # times colour -(C_A/2) f^{waz}, g^3
cGA = [as_sym(pole(GVA[m], 0)) for m in range(4)]; cGB = [as_sym(pole(GVB[m], 0)) for m in range(4)]
ppu = [sp.Rational(int(c.x.numerator), int(c.x.denominator)) for c in [list(x.terms())[0][1] for x in pp]]
xA = sp.simplify(cGA[0] / ppu[0]); xB = sp.simplify(cGB[0] / ppu[0])
report(all(sp.simplify(cGA[m] - xA * ppu[m]) == 0 and sp.simplify(cGB[m] - xB * ppu[m]) == 0 for m in range(4)),
       "ghost-gluon vertex: both graph poles proportional to p'^mu (outgoing ghost momentum)")
# sum_pole = (i/(16pi^2 eps)) g^3 f^{waz} p'^mu [-xA C_A/2 - xB C_A/2]; tree -g f p'^mu; counterterm dZt1 * tree
# => (i)(...) + dZt1 (-1) = 0 -> dZt1 = i (-xA - xB) C_A/2
print('  ghost vertex: graph A pole coefficient xA =', xA, ', graph B xB =', xB)
dZt1 = sp.simplify(sp.I * (-xA * CA / 2 - xB * CA / 2))
results['Zt1'] = dZt1
print('  dZt1 =', dZt1)
report(sp.simplify(dZt1 - (-xs / 2 * CA)) == 0, 'ghost-gluon vertex: dZt_1 = -(xi/2) C_A  (VF-QCD-4)')

# ================= Slavnov-Taylor relations and beta_0 =================
dZg_qg = sp.simplify(results['Z1F'] - results['Z2'] - results['Z3'] / 2)
dZg_gh = sp.simplify(results['Zt1'] - results['Zt3'] - results['Z3'] / 2)
b0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TFnf
print('  dZg (quark-gluon route) =', dZg_qg, ';  dZg (ghost route) =', dZg_gh)
report(sp.simplify(dZg_qg + b0 / 2) == 0 and sp.simplify(dZg_gh + b0 / 2) == 0,
       'two ST routes give dZ_g = -beta_0/2 = -(11/6) C_A + (2/3) T_F n_f, xi independent (from directly computed graphs)')
import json
with open('s3_results.json', 'w') as fh:
    json.dump({k_: str(v) for k_, v in results.items()}, fh, indent=1)
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
