"""
fourd.py -- explicit 4D component machinery for one-loop UV poles of local-operator Green functions.

* Cartesian components, metric diag(1,-1,-1,-1), Dirac representation.
* Loop momentum l = (l0,l1,l2,l3); external momenta are scaled by a book-keeping parameter t.
* UV pole of int d^Dl/(2pi)^D  Num(l,t)/prod_j ((l + a_j)^2):
     expand each propagator  1/((l+a)^2) = sum_k (-1)^k (2 l.a + a^2)^k / L^{k+1}   (L = l^2),
     keep the t^T term with T = omega + 4 (omega = superficial degree), i.e. the part homogeneous of
     degree -4 in l, average over directions
        <l^{mu1}...l^{mu2j}> = L^j sum_{pairings} prod g / (4*6*...*(2j+2))     (D -> 4 is enough for poles)
     and use  int d^Dl/(2pi)^D 1/L^2 |_{UV pole} = i/(16 pi^2) * (1/eps).
  uv_coeff(...) returns c with  pole = i c /(16 pi^2 eps).
  (At one loop the O(eps) parts of the numerator algebra only change finite parts.)
* Plane-wave vertex generator for gauge-field operators with explicit SU(2) colour (f^{abc} = eps^{abc});
  colour-stripped vertices are read off as coefficients of delta^{ab} or f^{abc}.
"""
import itertools
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import sympy.combinatorics
from functools import lru_cache

l0, l1, l2, l3, t = sp.symbols('l0 l1 l2 l3 t')
LV = [l0, l1, l2, l3]
GEN = (l0, l1, l2, l3, t)
METRIC = [1, -1, -1, -1]
I_ = sp.I

# ------------------------------------------------------------------ Dirac matrices
_I2 = sp.eye(2); _Z2 = sp.zeros(2)
_sx = sp.Matrix([[0, 1], [1, 0]]); _sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); _sz = sp.Matrix([[1, 0], [0, -1]])


def _blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


GAM = [_blk(_I2, _Z2, _Z2, -_I2)] + [_blk(_Z2, s, -s, _Z2) for s in (_sx, _sy, _sz)]
GAM_LOW = [METRIC[m] * GAM[m] for m in range(4)]   # gamma_mu


def dot(a, b):
    return sp.expand(a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3])


def lower(a):
    return [METRIC[m] * a[m] for m in range(4)]


def slash(a):
    return a[0] * GAM[0] - a[1] * GAM[1] - a[2] * GAM[2] - a[3] * GAM[3]


def vadd(*vs):
    return [sp.expand(sum(v[m] for v in vs)) for m in range(4)]


def vscale(c, v):
    return [sp.expand(c * x) for x in v]


def basis(mu):
    return [1 if m == mu else 0 for m in range(4)]


# ------------------------------------------------------------------ UV pole extraction
@lru_cache(None)
def _avg_monomial(exps):
    """<l0^a0 l1^a1 l2^a2 l3^a3>/L^j  with sum a = 2j  (4D, Minkowski metric)."""
    if any(e % 2 for e in exps):
        return sp.Integer(0)
    j = sum(exps) // 2
    num = sp.Integer(1)
    for m, e in enumerate(exps):
        num *= sp.factorial2(e - 1) * sp.Integer(METRIC[m]) ** (e // 2)
    den = sp.Integer(1)
    for k in range(j):
        den *= (4 + 2 * k)
    return num / den


def _poly(expr):
    return sp.Poly(sp.expand(expr), *GEN, domain='QQ')


def _trunc(P, T):
    d = {k: v for k, v in P.as_dict().items() if k[4] <= T}
    return sp.Poly.from_dict(d, *GEN, domain='QQ') if d else sp.Poly(0, *GEN, domain='QQ')


def uv_coeff(num, shifts, T):
    """num: sympy expression polynomial in l0..l3, t (rational coefficients)
       shifts: list of 4-vectors a_j (components polynomial in t): propagators 1/((l + a_j)^2)
       T: required power of t (= omega + 4).  Returns rational c (pole = i c/(16 pi^2 eps))."""
    if T < 0:
        return sp.Integer(0)
    # series: dict  k (power of 1/L) -> Poly
    series = {0: _trunc(_poly(num), T)}
    for a in shifts:
        la = dot(LV, a)
        aa = dot(a, a)
        X = _poly(2 * la + aa)
        exp = {}
        Xk = sp.Poly(1, *GEN, domain='QQ')
        for kk in range(0, 2 * T + 2):
            if Xk.is_zero:
                break
            exp[kk + 1] = (-1) ** kk * Xk
            Xk = _trunc(Xk * X, T)
            # stop when the minimal t-degree exceeds T
            if not Xk.is_zero and min(m[4] for m in Xk.as_dict()) > T:
                break
        new = {}
        for k1, P1 in series.items():
            for k2, P2 in exp.items():
                pr = _trunc(P1 * P2, T)
                if pr.is_zero:
                    continue
                new[k1 + k2] = new.get(k1 + k2, sp.Poly(0, *GEN, domain='QQ')) + pr
        series = new
    c = sp.Integer(0)
    for K, Pk in series.items():
        for mon, coef in Pk.as_dict().items():
            if mon[4] != T:
                continue
            deg = sum(mon[:4])
            if deg - 2 * K != -4:
                continue
            c += coef * _avg_monomial(tuple(mon[:4]))
    c = sp.sympify(c)
    assert c.is_Rational, c
    return c


# ------------------------------------------------------------------ plane-wave vertex generator (SU(2) adjoint)
EPS3 = {}
for a_, b_, c_ in itertools.permutations(range(3)):
    EPS3[(a_, b_, c_)] = sp.combinatorics.Permutation([a_, b_, c_]).signature()


def f3(a, b, c):
    return EPS3.get((a, b, c), 0)


class Field:
    """dict: frozenset(insertions) -> data; data = list over colour (3) of 4-vectors (vector field)
       or list over colour of scalars (scalar field)."""

    def __init__(self, d=None, vector=True):
        self.d = d or {}
        self.vector = vector


def gauge_field(ins):
    """ins: list of (label, colour, pol 4-vector (contravariant), momentum 4-vector (incoming))."""
    d = {}
    for lab, col, e, q in ins:
        arr = [[0] * 4 for _ in range(3)]
        arr[col] = list(e)
        d[frozenset([lab])] = arr
    return Field(d, True)


class Ctx:
    def __init__(self, ins, n):
        self.mom = {lab: q for lab, col, e, q in ins}
        self.n = n
        self.nlow = lower(n)

    def Q(self, S):
        return vadd(*[self.mom[s] for s in S]) if S else [0, 0, 0, 0]


def F_add(*Fs):
    vec = Fs[0].vector
    d = {}
    for F in Fs:
        for S, arr in F.d.items():
            if S in d:
                if vec:
                    d[S] = [[d[S][c][m] + arr[c][m] for m in range(4)] for c in range(3)]
                else:
                    d[S] = [d[S][c] + arr[c] for c in range(3)]
            else:
                d[S] = arr
    return Field(d, vec)


def F_scale(F, s):
    if F.vector:
        return Field({S: [[s * x for x in arr[c]] for c in range(3)] for S, arr in F.d.items()}, True)
    return Field({S: [s * arr[c] for c in range(3)] for S, arr in F.d.items()}, False)


def F_ndot(F, ctx):
    return Field({S: [sum(ctx.nlow[m] * arr[c][m] for m in range(4)) for c in range(3)] for S, arr in F.d.items()}, False)


def F_dn(F, ctx):
    """n.d acting on plane waves:  -i n.Q_S"""
    out = {}
    for S, arr in F.d.items():
        fac = -I_ * dot(ctx.n, ctx.Q(S))
        out[S] = [[fac * x for x in arr[c]] for c in range(3)] if F.vector else [fac * arr[c] for c in range(3)]
    return Field(out, F.vector)


def F_dup(Fs, ctx):
    """d^lambda acting on a scalar field -> vector:  -i Q_S^lambda"""
    out = {}
    for S, arr in Fs.d.items():
        Q = ctx.Q(S)
        out[S] = [[-I_ * Q[m] * arr[c] for m in range(4)] for c in range(3)]
    return Field(out, True)


def F_cross(Fs, Fv):
    """(Fs x Fv)^a = eps^{abc} Fs^b Fv^c   (scalar x vector -> vector), disjoint insertion sets."""
    out = {}
    for S1, a1 in Fs.d.items():
        for S2, a2 in Fv.d.items():
            if S1 & S2:
                continue
            S = S1 | S2
            arr = [[sum(f3(a, b, c) * a1[b] * a2[c][m] for b in range(3) for c in range(3)) for m in range(4)] for a in range(3)]
            if S in out:
                out[S] = [[out[S][a][m] + arr[a][m] for m in range(4)] for a in range(3)]
            else:
                out[S] = arr
    return Field(out, True)


def G_plus(A, ctx, g=1):
    """G^{a, +lambda} = n_mu G^{a mu lambda} = n.d A^lambda - d^lambda (n.A) + g eps^{abc} (n.A^b) A^{c lambda}"""
    nA = F_ndot(A, ctx)
    return F_add(F_dn(A, ctx), F_scale(F_dup(nA, ctx), -1), F_scale(F_cross(nA, A), g))


def iDplus(X, A, ctx, g=1):
    """(i D^+ X)^a = i n.d X^a + i g eps^{acb} (n.A^c) X^b  = i n.d X + i g (n.A x X)"""
    nA = F_ndot(A, ctx)
    return F_add(F_scale(F_dn(X, ctx), I_), F_scale(F_cross(nA, X), I_ * g))


def F_contract(F1, F2):
    """sum_a  g_{lambda rho} F1^{a lambda} F2^{a rho}  -> dict S -> scalar"""
    out = {}
    for S1, a1 in F1.d.items():
        for S2, a2 in F2.d.items():
            if S1 & S2:
                continue
            S = S1 | S2
            val = sum(METRIC[m] * a1[c][m] * a2[c][m] for c in range(3) for m in range(4))
            out[S] = out.get(S, 0) + val
    return out


def O_gluon(N, ins, n, g=1):
    """O_g^{(N)} = G^{a+nu} [(iD^+)^{N-2}]^{ab} G^b_nu^{ +} = - g_{lambda rho} G^{a,+lambda} [(iD^+)^{N-2} G]^{a,+rho}
       evaluated on plane-wave insertions; returns the multilinear coefficient (all insertions)."""
    ctx = Ctx(ins, n)
    A = gauge_field(ins)
    G = G_plus(A, ctx, g)
    R = G
    for _ in range(N - 2):
        R = iDplus(R, A, ctx, g)
    res = F_contract(G, R)
    full = frozenset(lab for lab, *_ in ins)
    return sp.expand(-res.get(full, 0))


def L_YM_cubic(ins, g=1):
    """i * (-1/4) G^a_{mu nu} G^{a mu nu}, multilinear coefficient in 3 insertions (vertex Feynman rule)."""
    # build full field strength with lower/upper handling: G^{a mu nu} = d^mu A^nu - d^nu A^mu + g eps A^mu A^nu
    labs = [lab for lab, *_ in ins]
    mom = {lab: q for lab, col, e, q in ins}
    pol = {lab: (col, e) for lab, col, e, q in ins}
    # linear part for insertion i: Lin_i^{a mu nu} = -i (q^mu e^nu - q^nu e^mu) delta^{a c_i}
    def lin(i):
        col, e = pol[i]; q = mom[i]
        arr = [[[0] * 4 for _ in range(4)] for _ in range(3)]
        for m in range(4):
            for v in range(4):
                arr[col][m][v] = -I_ * (q[m] * e[v] - q[v] * e[m])
        return arr

    def quad(i, j):
        ci, ei = pol[i]; cj, ej = pol[j]
        arr = [[[0] * 4 for _ in range(4)] for _ in range(3)]
        for a in range(3):
            fa = f3(a, ci, cj)
            if fa:
                for m in range(4):
                    for v in range(4):
                        arr[a][m][v] = g * fa * ei[m] * ej[v]
        return arr

    def contr(X, Y):
        return sum(METRIC[m] * METRIC[v] * X[a][m][v] * Y[a][m][v] for a in range(3) for m in range(4) for v in range(4))

    tot = 0
    for i in labs:
        others = [j for j in labs if j != i]
        for (j, k) in itertools.permutations(others, 2):
            # G.G with one linear (i) and one quadratic (j,k) factor; factor 2 for which G is linear
            tot += 2 * contr(lin(i), quad(j, k))
    return sp.expand(I_ * sp.Rational(-1, 4) * tot)
