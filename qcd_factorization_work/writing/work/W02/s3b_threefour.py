"""W02 / Ch2 check s3b: one-loop UV poles of the three-gluon and four-gluon vertex functions in a general covariant
gauge (completes VF-QCD-4: dZ_1, dZ_4), with the engine of s3_oneloop_Z.py (oneloop_engine.py).
Three-gluon: external momenta to first order (omega = 1); four-gluon: zero external momenta (omega = 0).
Colour: exact SU(2) (f = epsilon, t = sigma/2) and numerical SU(3) cross-check.
Run: python3 -I s3b_threefour.py
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oneloop_engine import *
import oneloop_engine as E
import numpy as np

def colour_su2():
    f = np.zeros((3, 3, 3))
    for a, b, c in itertools.permutations(range(3)):
        f[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    return np.array([s / 2 for s in sig]), f
def toSym(z, tol=1e-9):
    z = complex(z)
    re = sp.nsimplify(round(z.real, 10), rational=True, tolerance=tol)
    im = sp.nsimplify(round(z.imag, 10), rational=True, tolerance=tol)
    return re + sp.I * im
def contract_e(T, es):
    """not used"""
    pass

# ---------------- three-gluon vertex ----------------
TMAX[0] = 1
k1h = [Fraction(1, 2), Fraction(1, 3), Fraction(-2, 5), Fraction(1, 7)]
k2h = [Fraction(-1, 3), Fraction(3, 4), Fraction(1, 5), Fraction(-1, 2)]
k3h = [-(a + b) for a, b in zip(k1h, k2h)]
k1, k2, k3 = vec(k1h), vec(k2h), vec(k3h)
e1 = cvec([Fraction(2, 3), Fraction(1, 2), Fraction(-1, 1), Fraction(1, 3)])
e2 = cvec([Fraction(1, 5), Fraction(-2, 3), Fraction(1, 2), Fraction(3, 2)])
e3 = cvec([Fraction(-1, 2), Fraction(1, 4), Fraction(2, 3), Fraction(-1, 3)])
def Tcon(T, ea, eb=None, ec=None):
    """contract the first index of T^{mu nu rho} with ea (lower-index contraction via metric)."""
    out = {}
    for n in range(4):
        for r in range(4):
            out[(n, r)] = sum((G[m] * ea[m] * T[(m, n, r)] for m in range(4)), ZERO)
    return out
def neg(v): return [-x for x in v]
def add(*vs): return [sum(x) for x in zip(*vs)]
lv = mom(+1, None)
# gluon triangle: lines v3->v1: l, v1->v2: l+k1, v2->v3: l-k3
q31 = lv; q12 = add(lv, k1); q23 = add(lv, neg(k3))
T1 = Tcon(V3kin(k1, q31, neg(q12)), e1)          # legs (k1,mu1),(l: x,alpha),(-(l+k1): y,beta)
T2 = Tcon(V3kin(k2, q12, neg(q23)), e2)          # legs (k2,mu2),(l+k1: y',beta'),(-(l-k3): z,gamma)
T3 = Tcon(V3kin(k3, q23, neg(q31)), e3)          # legs (k3,mu3),(l-k3: z',gamma'),(-l: x',alpha')
D31 = Dgluon(+1, None); D12 = Dgluon(+1, k1); D23 = Dgluon(+1, neg(k3))
def glue3(Ta, Tb, Tc, Da, Db, Dc):
    """sum over internal indices: Ta[(alpha,beta)] Tb[(beta',gamma)] Tc[(gamma',alpha')] with propagators
       D^{alpha' alpha} (line a), D^{beta beta'} (line b), D^{gamma gamma'} (line c) and metrics."""
    # first contract Ta with Db: X[(alpha, beta')] = sum_beta Ta[(alpha,beta)] G_beta D^{beta beta'} G_beta'
    X = {}
    for a_ in range(4):
        for b2 in range(4):
            X[(a_, b2)] = trunc(sum((Ta[(a_, b_)] * Db[b_][b2] * (G[b_] * G[b2]) for b_ in range(4)), ZERO))
    Y = {}
    for a_ in range(4):
        for c_ in range(4):
            Y[(a_, c_)] = trunc(sum((X[(a_, b2)] * Tb[(b2, c_)] for b2 in range(4)), ZERO))
    Z = {}
    for a_ in range(4):
        for c2 in range(4):
            Z[(a_, c2)] = trunc(sum((Y[(a_, c_)] * Dc[c_][c2] * (G[c_] * G[c2]) for c_ in range(4)), ZERO))
    W = {}
    for a_ in range(4):
        for a2 in range(4):
            W[(a_, a2)] = trunc(sum((Z[(a_, c2)] * Tc[(c2, a2)] for c2 in range(4)), ZERO))
    return trunc(sum((W[(a_, a2)] * Da[a2][a_] * (G[a_] * G[a2]) for a_ in range(4) for a2 in range(4)), ZERO))
Kglu = glue3(T1, T2, T3, D31, D12, D23)            # times g^3 * colour f^{a1xy} f^{a2yz} f^{a3zx} = (C_A/2) f^{a1a2a3}
P_glu = as_sym(pole(Kglu, 1))
# ghost triangles (two orientations), each -1:
# orientation A (ghost v1->v2->v3->v1): v1: -f^{y a1 x} (l+k1).e1 ; v2: -f^{z a2 y} (l-k3).e2 ; v3: -f^{x a3 z} l.e3
iA = trunc(I * invsq(+1, None) * I * invsq(+1, k1)); iA = trunc(iA * I * invsq(+1, neg(k3)))
KghA = trunc((-1) * (-1) ** 3 * trunc(trunc(dot(q12, e1) * dot(q23, e2)) * dot(q31, e3)) * iA)
# orientation B (ghost v1->v3->v2->v1): lines v2->v1: l, v1->v3: l+k1, v3->v2: l-k2
r21 = lv; r13 = add(lv, k1); r32 = add(lv, neg(k2))
iB = trunc(I * invsq(+1, None) * I * invsq(+1, k1)); iB = trunc(iB * I * invsq(+1, neg(k2)))
KghB = trunc((-1) * (-1) ** 3 * trunc(trunc(dot(r13, e1) * dot(r32, e3)) * dot(r21, e2)) * iB)
P_ghA = as_sym(pole(KghA, 1)); P_ghB = as_sym(pole(KghB, 1))
# quark triangles, each -n_f:
# A: Tr[V1 S(l) V3 S(l-k3) V2 S(l+k1)], colour Tr(t^a1 t^a3 t^a2);  B: Tr[V1 S(l) V2 S(l-k2) V3 S(l+k1)], colour Tr(t^a1 t^a2 t^a3)
def Vq(e):
    return msc(I, slash(e))   # i g gamma.e (g = 1); slash uses lower-index contraction gamma^mu e_mu
SA = Squark(+1, None); SB = Squark(+1, neg(k3)); SC = Squark(+1, k1); SD = Squark(+1, neg(k2))
KqA = trunc(-1 * mtr(mmul(mmul(mmul(mmul(mmul(Vq(e1), SA), Vq(e3)), SB), Vq(e2)), SC)))
KqB = trunc(-1 * mtr(mmul(mmul(mmul(mmul(mmul(Vq(e1), SA), Vq(e2)), SD), Vq(e3)), SC)))
P_qA = as_sym(pole(KqA, 1)); P_qB = as_sym(pole(KqB, 1))
# swordfish graphs: 4-vertex with legs (i,j), 3-vertex with leg m; internal lines 4v->3v: l and -l-k_m ; symmetry 1/2
def V4terms(ea, eb):
    """the 4-vertex with legs (a,ea),(b,eb),(c,rho),(d,sigma): returns three (colourtype, kin[rho][sigma]) pieces,
       kin including -i (g^2 stripped); colour types: 'ab|cd' f^{abe}f^{cde}, 'ac|bd' f^{ace}f^{bde}, 'ad|bc' f^{ade}f^{bce}."""
    def gg(u, v):  # u.v for constant vectors
        return dot(u, v)
    def em(e, r):  # e^r (upper index of external polarisation as seen from internal index r): e_mu g^{mu r} -> e^r
        return e[r]
    kab = [[ZERO] * 4 for _ in range(4)]; kac = [[ZERO] * 4 for _ in range(4)]; kad = [[ZERO] * 4 for _ in range(4)]
    for r in range(4):
        for s_ in range(4):
            g_rs = G[r] * ONE if r == s_ else ZERO
            kab[r][s_] = -I * (em(ea, r) * em(eb, s_) - em(ea, s_) * em(eb, r))
            kac[r][s_] = -I * (gg(ea, eb) * g_rs - em(ea, s_) * em(eb, r))
            kad[r][s_] = -I * (gg(ea, eb) * g_rs - em(ea, r) * em(eb, s_))
    return {'ab|cd': kab, 'ac|bd': kac, 'ad|bc': kad}
def swordfish(ei, ej, em_, km):
    """kinematic poles for the three colour structures; legs (i,j) at 4v with internal (x: line A, y: line B),
       3-vertex legs (m, km), (x, alpha, l), (y, beta, -l-km)."""
    T = Tcon(V3kin(km, lv, neg(add(lv, km))), em_)
    DA = Dgluon(+1, None); DB = Dgluon(+1, km)
    V4 = V4terms(ei, ej)
    out = {}
    for typ, kin in V4.items():
        acc = ZERO
        for r, s_, a_, b_ in itertools.product(range(4), repeat=4):
            if DA[r][a_] == ZERO or DB[s_][b_] == ZERO or kin[r][s_] == ZERO: continue
            tv = T[(a_, b_)]
            if tv == ZERO: continue
            acc += trunc(kin[r][s_] * trunc(DA[r][a_] * DB[s_][b_]) * tv * (G[r] * G[a_] * G[s_] * G[b_]))
        out[typ] = as_sym(pole(trunc(R(QQ(1, 2)) * acc), 1))
    return out
SW3 = swordfish(e1, e2, e3, k3)   # 4v legs (1,2), 3v leg 3: colour f^{a1 a2 ..} etc with (c,d) = (x,y); 3v colour f^{a3 x y}
SW1 = swordfish(e2, e3, e1, k1)   # 4v legs (2,3), 3v leg 1: f^{a1 x y}
SW2 = swordfish(e3, e1, e2, k2)   # 4v legs (3,1), 3v leg 2: f^{a2 x y}
# tree (kinematic part, contracted): T(k1,k2,k3) e1 e2 e3 at order t^1
Ttree = V3kin(k1, k2, k3)
tree = trunc(sum((G[m] * G[n] * G[r] * e1[m] * e2[n] * e3[r] * Ttree[(m, n, r)] for m in range(4) for n in range(4) for r in range(4)), ZERO))
tree_s = sum((sp.Rational(int(c.x.numerator), int(c.x.denominator)) for mm, c in tree.terms() if mm[5] == 1), sp.Integer(0))
def colour3(tt, f, a1, a2, a3):
    """colour weights (exact if f, t exact)"""
    F = -1j * f
    w = {}
    w['glu'] = np.einsum('xy,yz,zx->', f[a1], f[a2], f[a3])            # f^{a1xy} f^{a2yz} f^{a3zx}
    # ghost A: f^{y a1 x} f^{z a2 y} f^{x a3 z}; ghost B: (v1->v3->v2): f^{u a1 w} f^{v a3 u} f^{w a2 v}
    w['ghA'] = np.einsum('yx,zy,xz->', f[:, a1, :], f[:, a2, :], f[:, a3, :])
    w['ghB'] = np.einsum('uw,vu,wv->', f[:, a1, :], f[:, a3, :], f[:, a2, :])
    w['qA'] = np.trace(tt[a1] @ tt[a3] @ tt[a2]); w['qB'] = np.trace(tt[a1] @ tt[a2] @ tt[a3])
    # swordfish: 4-vertex legs (a,b,c=x,d=y), 3-vertex f^{am x y}
    def sw(aa, bb, am):
        return {'ab|cd': np.einsum('e,xye,xy->', f[aa, bb, :], f, f[am]),
                'ac|bd': np.einsum('xe,ye,xy->', f[aa, :, :], f[bb, :, :], f[am]),
                'ad|bc': np.einsum('ye,xe,xy->', f[aa, :, :], f[bb, :, :], f[am])}
    w['sw3'] = sw(a1, a2, a3); w['sw1'] = sw(a2, a3, a1); w['sw2'] = sw(a3, a1, a2)
    w['tree'] = f[a1, a2, a3]
    return w
def total3(w, CAval, TF):
    pure = (P_glu * toSym(w['glu']) + P_ghA * toSym(w['ghA']) + P_ghB * toSym(w['ghB'])
            + sum(SW3[k_] * toSym(w['sw3'][k_]) for k_ in SW3) + sum(SW1[k_] * toSym(w['sw1'][k_]) for k_ in SW1)
            + sum(SW2[k_] * toSym(w['sw2'][k_]) for k_ in SW2))
    quark = P_qA * toSym(w['qA']) + P_qB * toSym(w['qB'])
    # sum_pole = (i/(16 pi^2 eps)) g^3 [pure + n_f quark]; counterterm dZ1 * g f^{a1a2a3} tree
    # => dZ1 = - i [pure + n_f quark] / (f tree)
    dz_pure = sp.simplify(-sp.I * pure / (toSym(w['tree']) * tree_s))
    dz_quark = sp.simplify(-sp.I * quark / (toSym(w['tree']) * tree_s))   # per flavour
    return dz_pure, dz_quark
tt2, f2 = colour_su2()
w = colour3(tt2, f2, 0, 1, 2)
dzp, dzq = total3(w, 2, sp.Rational(1, 2))
print('  SU(2): dZ1 pure-gauge part =', dzp, ' ; quark part per flavour =', dzq)
report(sp.simplify(dzp - (sp.Rational(17, 12) - 3 * xs / 4) * 2) == 0, 'three-gluon vertex, SU(2): gluon+ghost graphs give (17/12 - 3 xi/4) C_A')
report(sp.simplify(dzq - (-sp.Rational(4, 3) * sp.Rational(1, 2))) == 0, 'three-gluon vertex, SU(2): quark triangles give -(4/3) T_F per flavour')
tt3, f3 = su(3)
cands = [c for c in itertools.combinations(range(8), 3) if abs(f3[c]) > 1e-9]
for cols in [cands[0], cands[len(cands)//2], cands[-1]]:
    w = colour3(tt3, f3, *cols)
    if abs(w['tree']) < 1e-9: continue
    # numerical colour weights (SU(3) structure constants include sqrt(3)/2): evaluate at xi = 0.37
    xv = 0.37
    num = lambda e: complex(sp.N(e.subs(xs, xv)))
    pure = (num(P_glu) * w['glu'] + num(P_ghA) * w['ghA'] + num(P_ghB) * w['ghB']
            + sum(num(SW3[k_]) * w['sw3'][k_] for k_ in SW3) + sum(num(SW1[k_]) * w['sw1'][k_] for k_ in SW1)
            + sum(num(SW2[k_]) * w['sw2'][k_] for k_ in SW2))
    quark = num(P_qA) * w['qA'] + num(P_qB) * w['qB']
    ts = complex(tree_s)
    dzp = -1j * pure / (w['tree'] * ts); dzq = -1j * quark / (w['tree'] * ts)
    report(abs(dzp - (17 / 12 - 3 * xv / 4) * 3) < 1e-9 and abs(dzq + 2 / 3) < 1e-9,
           f'three-gluon vertex, SU(3), colours {cols}: dZ_1 = (17/12 - 3 xi/4) C_A - (4/3) T_F n_f (numerical colour)')
# Furry: d-parts of the two quark orientations cancel (check P_qA = -P_qB for the kinematic parts)
report(sp.simplify(P_qA + P_qB) == 0, 'quark triangles: kinematic poles of the two orientations are opposite (Furry: only f^abc survives)')

# ---------------- four-gluon vertex at zero external momenta ----------------
TMAX[0] = 0
es = [cvec([Fraction(2, 3), Fraction(1, 2), Fraction(-1, 1), Fraction(1, 3)]),
      cvec([Fraction(1, 5), Fraction(-2, 3), Fraction(1, 2), Fraction(3, 2)]),
      cvec([Fraction(-1, 2), Fraction(1, 4), Fraction(2, 3), Fraction(-1, 3)]),
      cvec([Fraction(1, 1), Fraction(1, 3), Fraction(1, 6), Fraction(-2, 5)])]
Dl = Dgluon(+1, None)
lm = mom(-1, None); z0 = [ZERO] * 4
# gluon box for a cyclic order (o0,o1,o2,o3): vertex at o_i: legs (ext o_i), (incoming line from o_{i-1}: +l), (outgoing: -l)
def gluon_box(order):
    Ts = [Tcon(V3kin(z0, lv, lm), es[o]) for o in order]    # T[(alpha_in, beta_out)]
    # chain: T0[(a, b)] D^{b b'} T1[(b', c)] D^{c c'} T2 ... T3[(d', a')] D^{a' a}
    M = {(a_, b_): Ts[0][(a_, b_)] for a_ in range(4) for b_ in range(4)}
    for Tn in Ts[1:]:
        X = {}
        for a_ in range(4):
            for b2 in range(4):
                X[(a_, b2)] = trunc(sum((M[(a_, b_)] * Dl[b_][b2] * (G[b_] * G[b2]) for b_ in range(4)), ZERO))
        M = {}
        for a_ in range(4):
            for c_ in range(4):
                M[(a_, c_)] = trunc(sum((X[(a_, b2)] * Tn[(b2, c_)] for b2 in range(4)), ZERO))
    tot = trunc(sum((M[(a_, a2)] * Dl[a2][a_] * (G[a_] * G[a2]) for a_ in range(4) for a2 in range(4)), ZERO))
    return as_sym(pole(tot, 0))
orders = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
Pbox = {o: gluon_box(o) for o in orders}
# ghost boxes: each oriented loop: (-1) (-1)^4 prod_i (l.e_i) (i/l^2)^4, colour prod f^{x_{i,i+1} a_i x_{i-1,i}}
il = invsq(+1, None)
ighost4 = trunc(trunc(I * il * I * il) * trunc(I * il * I * il))
Kgh = trunc(-1 * trunc(trunc(dot(lv, es[0]) * dot(lv, es[1])) * trunc(dot(lv, es[2]) * dot(lv, es[3]))) * ighost4)
Pgh = as_sym(pole(Kgh, 0))
# quark boxes: -n_f Tr[V_{o0} S V_{o3} S V_{o2} S V_{o1} S] for arrow o0->o1->o2->o3 ; colour Tr(t^{o0} t^{o3} t^{o2} t^{o1})
S0 = Squark(+1, None)
def quark_box(order):
    m = Mid()
    for o in [order[0], order[3], order[2], order[1]]:
        m = mmul(mmul(m, Vq(es[o])), S0)
    return as_sym(pole(trunc(-1 * mtr(m)), 0))
all_oriented = [(0,) + p for p in itertools.permutations((1, 2, 3))]
Pq4 = {o: quark_box(o) for o in all_oriented}
# triangles with one 4-vertex: legs (i,j) at 4v; loop 4v -> v_k -> v_m -> 4v, all lines carry l
def triangle4(i, j, kk, mm):
    V4 = V4terms(es[i], es[j])    # legs (a,i),(b,j),(c: z' incoming from v_m),(d: x' outgoing to v_k)
    Tk = Tcon(V3kin(z0, lv, lm), es[kk])    # (alpha_in from 4v, beta_out to v_m)
    Tm = Tcon(V3kin(z0, lv, lm), es[mm])    # (beta'_in from v_k, gamma_out to 4v)
    out = {}
    for typ, kin in V4.items():
        acc = ZERO
        # kin[rho][sigma]: rho = c (incoming line from v_m, index gamma'), sigma = d (outgoing line to v_k, index alpha')
        for c_, d_ in itertools.product(range(4), repeat=2):
            if kin[c_][d_] == ZERO: continue
            for a_, b_, b2, g_ in itertools.product(range(4), repeat=4):
                if Dl[d_][a_] == ZERO or Dl[b_][b2] == ZERO or Dl[g_][c_] == ZERO: continue
                x1 = Tk[(a_, b_)]; x2 = Tm[(b2, g_)]
                if x1 == ZERO or x2 == ZERO: continue
                acc += trunc(kin[c_][d_] * trunc(Dl[d_][a_] * x1) * trunc(Dl[b_][b2] * x2) * Dl[g_][c_] *
                             (G[d_] * G[a_] * G[b_] * G[b2] * G[g_] * G[c_]))
        out[typ] = as_sym(pole(trunc(acc), 0))
    return out
pairs = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 0, 2), (2, 3, 0, 1)]
Ptri = {pr: triangle4(*pr) for pr in pairs}
# bubbles: legs (i,j) at vertex A, (k,m) at vertex B; internal lines x (index) and y; symmetry 1/2
def bubble(i, j, kk, mm):
    VA = V4terms(es[i], es[j]); VB = V4terms(es[kk], es[mm])
    out = {}
    for ta, ka in VA.items():
        for tb, kb in VB.items():
            acc = ZERO
            # VA legs (c: x, d: y), VB legs (c: x', d: y'); propagators D^{x x'} D^{y y'}
            for c_, d_, c2, d2 in itertools.product(range(4), repeat=4):
                if ka[c_][d_] == ZERO or kb[c2][d2] == ZERO or Dl[c_][c2] == ZERO or Dl[d_][d2] == ZERO: continue
                acc += trunc(ka[c_][d_] * kb[c2][d2] * trunc(Dl[c_][c2] * Dl[d_][d2]) * (G[c_] * G[c2] * G[d_] * G[d2]))
            out[(ta, tb)] = as_sym(pole(trunc(R(QQ(1, 2)) * acc), 0))
    return out
bpairs = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
Pbub = {bp: bubble(*bp) for bp in bpairs}
def ffw(f, x, y, z, w_):   # f^{x y e} f^{z w e}
    return np.einsum('e,e->', f[x, y, :], f[z, w_, :])
def V4colour_weights(f, a, b, cidx, didx):
    """colour factors of the three structures with legs (a,b,c,d) where c,d may be 'free' internal indices:
       returns arrays over the internal indices."""
    pass
def total4(tt, f, cols):
    a = cols
    F = -1j * f
    n = f.shape[0]
    pure = 0; quark = 0
    # gluon boxes: colour Tr(F^{o0} F^{o1} F^{o2} F^{o3})
    for o in orders:
        cw = np.trace(F[a[o[0]]] @ F[a[o[1]]] @ F[a[o[2]]] @ F[a[o[3]]])
        pure += Pbox[o] * toSym(cw)
    # ghost boxes: each oriented loop colour prod_i f^{x_{i,i+1} a_i x_{i-1,i}} = prod (-i)(F^{a_i})... compute directly
    for o in all_oriented:
        # f^{x01 a0 x30} f^{x12 a1 x01} f^{x23 a2 x12} f^{x30 a3 x23}
        cw = np.einsum('pq,rp,sr,qs->', f[:, a[o[0]], :], f[:, a[o[1]], :], f[:, a[o[2]], :], f[:, a[o[3]], :])
        pure += Pgh * toSym(cw)
    for o in all_oriented:
        cw = np.trace(tt[a[o[0]]] @ tt[a[o[3]]] @ tt[a[o[2]]] @ tt[a[o[1]]])
        quark += Pq4[o] * toSym(cw)
    # triangles: 4-vertex (a_i, a_j, z, x) with f-structures; v_k: f^{a_k x y}; v_m: f^{a_m y z}
    for (i, j, kk, mm), dd in Ptri.items():
        Ck = f[a[kk]]; Cm = f[a[mm]]   # [x,y], [y,z]
        for typ, val in dd.items():
            if typ == 'ab|cd':   # f^{a_i a_j e} f^{z x e}
                cw = np.einsum('e,zxe,xy,yz->', f[a[i], a[j], :], f, Ck, Cm)
            elif typ == 'ac|bd':  # f^{a_i z e} f^{a_j x e}
                cw = np.einsum('ze,xe,xy,yz->', f[a[i], :, :], f[a[j], :, :], Ck, Cm)
            else:                 # f^{a_i x e} f^{a_j z e}
                cw = np.einsum('xe,ze,xy,yz->', f[a[i], :, :], f[a[j], :, :], Ck, Cm)
            pure += val * toSym(cw)
    # bubbles: A legs (a_i,a_j,x,y), B legs (a_k,a_m,x,y)
    def struct(typ, p, q):   # returns tensor over (x,y) for legs (p,q,x,y)
        if typ == 'ab|cd': return np.einsum('e,xye->xy', f[p, q, :], f)
        if typ == 'ac|bd': return np.einsum('xe,ye->xy', f[p, :, :], f[q, :, :])
        return np.einsum('ye,xe->xy', f[p, :, :], f[q, :, :])
    for (i, j, kk, mm), dd in Pbub.items():
        for (ta, tb), val in dd.items():
            cw = np.einsum('xy,xy->', struct(ta, a[i], a[j]), struct(tb, a[kk], a[mm]))
            pure += val * toSym(cw)
    # tree: -i [f^{abe}f^{cde}(e1.e3 e2.e4 - e1.e4 e2.e3) + f^{ace}f^{bde}(e1.e2 e3.e4 - e1.e4 e2.e3) + f^{ade}f^{bce}(e1.e2 e3.e4 - e1.e3 e2.e4)]
    d_ = lambda x, y: sum(G[m] * sp.Rational(int(list(es[x][m].terms())[0][1].x.numerator), int(list(es[x][m].terms())[0][1].x.denominator)) *
                           sp.Rational(int(list(es[y][m].terms())[0][1].x.numerator), int(list(es[y][m].terms())[0][1].x.denominator)) for m in range(4))
    tree4 = -sp.I * (toSym(ffw(f, a[0], a[1], a[2], a[3])) * (d_(0, 2) * d_(1, 3) - d_(0, 3) * d_(1, 2))
                     + toSym(ffw(f, a[0], a[2], a[1], a[3])) * (d_(0, 1) * d_(2, 3) - d_(0, 3) * d_(1, 2))
                     + toSym(ffw(f, a[0], a[3], a[1], a[2])) * (d_(0, 1) * d_(2, 3) - d_(0, 2) * d_(1, 3)))
    # sum_pole = (i/(16pi^2 eps)) g^4 [pure + n_f quark]; counterterm dZ4 * g^2 * tree4 => dZ4 = -i(...)/tree4
    return sp.simplify(-sp.I * pure / tree4), sp.simplify(-sp.I * quark / tree4), tree4
for cols in [(0, 1, 0, 1), (0, 1, 2, 0), (0, 0, 1, 1), (2, 1, 0, 2)]:
    zp, zq, tr4 = total4(tt2, f2, cols)
    if tr4 == 0: continue
    print('  SU(2) colours', cols, ': dZ4 pure =', zp, '; quark per flavour =', zq)
    report(sp.simplify(zp - (sp.Rational(2, 3) - xs) * 2) == 0 and sp.simplify(zq + sp.Rational(2, 3)) == 0,
           f'four-gluon vertex, SU(2), colours {cols}: dZ_4 = (2/3 - xi) C_A - (4/3) T_F n_f')
for cols in [(0, 1, 0, 1), (0, 3, 4, 7), (1, 2, 2, 1), (0, 3, 0, 3)]:
    zp, zq, tr4 = total4(tt3, f3, cols)
    if abs(complex(tr4)) < 1e-9: continue
    report(abs(complex(zp.subs(xs, 0.37)) - (2 / 3 - 0.37) * 3) < 1e-6 and abs(complex(zq) + 2 / 3) < 1e-6,
           f'four-gluon vertex, SU(3), colours {cols}: dZ_4 = (2/3 - xi) C_A - (4/3) T_F n_f (numerical colour)')
print(f'\nSUMMARY: {E.npass}/{E.npass + E.nfail} PASS')
