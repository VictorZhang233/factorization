"""Engine extracted from s3_oneloop_Z.py (W02): one-loop UV poles (MS-bar renormalization constants) in a general covariant gauge xi,
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
