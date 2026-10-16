"""E25 -- gauge and BRST properties of the BPS collinear gluon Lagrangian, BPS 2002 eq. (24) = label (Lcg)
of arXiv:hep-ph/0109045v2 (= PRD 65 (2002) 054022):

  L = 1/(2 g^2) tr{[iD^mu + g A^mu, iD^nu + g A^nu]}^2                      (L_F, field strength)
      + 2 tr{ cbar [iD_mu, [iD^mu + g A^mu, c]] }                           (L_gh, ghost)
      + 1/alpha tr{ [iD_mu, A^mu] }^2                                       (L_gf, gauge fixing)

with iD^mu = n^mu/2 Pbar + P_perp^mu + nbar^mu/2 i n.D_us  (BPS eq. (17)).  Continuum representation:
label + residual derivatives are combined into ordinary derivatives acting on collinear fields; the
usoft field enters only as B^mu = nbar^mu/2 b(x), b = n.A_us, depending on nbar.x = t+z only
(multipole expansion: nbar.d b = d_perp b = 0), so [iD^mu, X] = i d^mu X + g [B^mu, X] on adjoint X.

Gauge group SU(2) (T^a = sigma^a/2).  Fields are random quadratic polynomials around a random point;
since no expression below differentiates any product more than twice, truncated Taylor jets of total
degree 2 are exact for the value at the point.  Ghosts are Grassmann-valued (explicit Grassmann
algebra with generators 1..6; theta = generator 0 is the BRST parameter, generator 7 a second one).
Floating point (complex128); "zero" means |.| < 1e-9 * scale, nonzero results are O(1-1000).

Transformations (BPS Table I, D = d - i g A convention):
  collinear  U = 1 + i w(x):   dA^mu = -(i/g)[Pi^mu, w],  Pi = iD + gA;  dB = 0;
                               ghosts: option 1 adjoint dc = i[w,c], dcbar = i[w,cbar]
                               (the row commented out in the BPS source), option 2 inert.
  usoft      V = 1 + i be(t+z): dB^mu = i[be, B^mu] + (1/g) d^mu be;  dA = i[be, A];  dc = i[be,c] ...
  BRST       X -> X + theta sX:  s A^mu = -(i/g)[Pi^mu, c],  s c = i c c,  s cbar = (i/(alpha g)) [iD_mu, A^mu].
Run: python3 -I e25_ghost_gauge.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

rng = np.random.default_rng(20261010)
eta = np.array([1., -1., -1., -1.])
nbar = np.array([1., 0., 0., -1.])
g = 1.4
alpha = 1.5

# ------------------------------------------------------------------ truncated Taylor jets (deg <= 2)
MONS = [(0, 0, 0, 0)] + [tuple(int(i == k) for i in range(4)) for k in range(4)] + \
       [tuple(sum(1 for q in pair if q == i) for i in range(4)) for pair in itertools.combinations_with_replacement(range(4), 2)]
IDX = {m: i for i, m in enumerate(MONS)}
NM = len(MONS)
MULT = np.full((NM, NM), -1, dtype=int)
for i, a in enumerate(MONS):
    for j, b in enumerate(MONS):
        s = tuple(p + q for p, q in zip(a, b))
        if sum(s) <= 2:
            MULT[i, j] = IDX[s]
DER = []  # DER[v] = list of (src, dst, factor)
for v in range(4):
    lst = []
    for i, m in enumerate(MONS):
        if m[v] > 0:
            mm = list(m); mm[v] -= 1
            lst.append((i, IDX[tuple(mm)], m[v]))
    DER.append(lst)


def jmul(a, b):
    out = np.zeros(NM, complex)
    nza = np.nonzero(a)[0]; nzb = np.nonzero(b)[0]
    for i in nza:
        for j in nzb:
            k = MULT[i, j]
            if k >= 0:
                out[k] += a[i] * b[j]
    return out


def jder(a, v):
    out = np.zeros(NM, complex)
    for src, dst, f in DER[v]:
        out[dst] += f * a[src]
    return out


def rand_jet():
    return rng.normal(size=NM) + 0j


def rand_jet_usoft():
    # quadratic polynomial in u = dt + dz : c0 + c1 u + c2 u^2
    c0, c1, c2 = rng.normal(size=3)
    a = np.zeros(NM, complex)
    a[IDX[(0, 0, 0, 0)]] = c0
    a[IDX[(1, 0, 0, 0)]] = c1; a[IDX[(0, 0, 0, 1)]] = c1
    a[IDX[(2, 0, 0, 0)]] = c2; a[IDX[(0, 0, 0, 2)]] = c2; a[IDX[(1, 0, 0, 1)]] = 2 * c2
    return a


# ------------------------------------------------------------------ Grassmann algebra over jets
class Gr:
    __slots__ = ('d',)

    def __init__(self, d=None):
        self.d = d or {}

    def __add__(self, o):
        d = {k: v.copy() for k, v in self.d.items()}
        for k, v in o.d.items():
            d[k] = d[k] + v if k in d else v.copy()
        return Gr(d)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, c):
        return Gr({k: c * v for k, v in self.d.items()})

    def __mul__(self, o):
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                if set(k1) & set(k2):
                    continue
                seq = k1 + k2
                inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
                k = tuple(sorted(seq))
                p = jmul(v1, v2) * (-1) ** inv
                d[k] = d[k] + p if k in d else p
        return Gr(d)

    def der(self, v):
        return Gr({k: jder(val, v) for k, val in self.d.items()})

    def value(self):
        """values at the point: {monomial: complex}"""
        return {k: v[0] for k, v in self.d.items()}


def gscalar(jet):
    return Gr({(): jet})


def mzero():
    return [[Gr(), Gr()], [Gr(), Gr()]]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def mscale(c, A):
    return [[A[i][j].scale(c) for j in range(2)] for i in range(2)]


def mmul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def comm(A, B):
    return msub(mmul(A, B), mmul(B, A))


def mder(A, v):
    return [[A[i][j].der(v) for j in range(2)] for i in range(2)]


def tr(A):
    return A[0][0] + A[1][1]


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
TG = [s / 2 for s in SIG]


def from_comp(comp):
    """comp[a]: Gr; returns sum_a comp[a] T^a"""
    M = mzero()
    for a in range(3):
        for i in range(2):
            for j in range(2):
                if TG[a][i, j] != 0:
                    M[i][j] = M[i][j] + comp[a].scale(TG[a][i, j])
    return M


def grass_lin(gens):
    """random Grassmann-odd function sum_k phi_k(x) eta_k"""
    return Gr({(k,): rand_jet() for k in gens})


def make_fields():
    A = [from_comp([gscalar(rand_jet()) for _ in range(3)]) for mu in range(4)]
    b = from_comp([gscalar(rand_jet_usoft()) for _ in range(3)])
    B = [mscale(nbar[mu] / 2, b) for mu in range(4)]
    c = from_comp([grass_lin((1, 2, 3)) for _ in range(3)])
    cb = from_comp([grass_lin((4, 5, 6)) for _ in range(3)])
    return A, B, c, cb


def Dcomm(B, mu, M):  # [iD^mu, M], upper index
    return madd(mscale(1j * eta[mu], mder(M, mu)), mscale(g, comm(B[mu], M)))


def Picomm(A, B, mu, M):
    return madd(Dcomm(B, mu, M), mscale(g, comm(A[mu], M)))


def Fmunu(A, B, mu, nu):
    C = [madd(A[r], B[r]) for r in range(4)]
    t1 = mscale(1j * g * eta[mu], mder(C[nu], mu))
    t2 = mscale(1j * g * eta[nu], mder(C[mu], nu))
    return madd(msub(t1, t2), mscale(g * g, comm(C[mu], C[nu])))


def L_F(A, B):
    tot = Gr()
    for mu in range(4):
        for nu in range(4):
            F = Fmunu(A, B, mu, nu)
            tot = tot + tr(mmul(F, F)).scale(eta[mu] * eta[nu])
    return tot.scale(1 / (2 * g * g))


def Gfix(A, B):
    G = mzero()
    for mu in range(4):
        G = madd(G, mscale(eta[mu], Dcomm(B, mu, A[mu])))
    return G


def L_gf(A, B):
    G = Gfix(A, B)
    return tr(mmul(G, G)).scale(1 / alpha)


def L_gh(A, B, c, cb):
    tot = mzero()
    for mu in range(4):
        tot = madd(tot, mscale(eta[mu], Dcomm(B, mu, Picomm(A, B, mu, c))))
    return tr(mmul(cb, tot)).scale(2)


# ------------------------------------------------------------------ helpers
def shift4(F, dF, e):
    return [madd(F[m], mscale(e, dF[m])) for m in range(4)]


def first_order(fun, args0, argsd, h=0.5):
    """central difference d/de fun(args0 + e argsd) at e=0 (exact up to O(h^2) for these polynomials:
    the dependence on e is polynomial of low degree, so we use a 5-point stencil, exact to degree 4)"""
    def at(e):
        args = []
        for a0, ad in zip(args0, argsd):
            if len(a0) == 4:                     # list of 4 matrices (a 2x2 matrix has length 2)
                args.append(shift4(a0, ad, e))
            else:
                args.append(madd(a0, mscale(e, ad)))
        return fun(*args).value()
    stencil = [(-2, 1 / 12), (-1, -8 / 12), (1, 8 / 12), (2, -1 / 12)]
    vals = {}
    for k, wgt in stencil:
        for mono, v in at(k * h).items():
            vals[mono] = vals.get(mono, 0) + wgt * v / h
    return vals


def maxabs(vals):
    return max([abs(v) for v in vals.values()] + [0.0])


def report(name, vals, expect_zero, scale):
    m = maxabs(vals)
    zero = m < 1e-7 * max(1.0, scale)
    ok = zero == expect_zero
    print('  %-60s max|.| = %10.3e  -> %-8s (%s)' % (name, m, 'zero' if zero else 'NONZERO', 'PASS' if ok else 'FAIL'))
    return ok


if __name__ == '__main__':
    allok = True
    for trial in range(3):
        A, B, c, cb = make_fields()
        w = from_comp([gscalar(rand_jet()) for _ in range(3)])
        be = from_comp([gscalar(rand_jet_usoft()) for _ in range(3)])
        scale = max(maxabs(L_F(A, B).value()), maxabs(L_gh(A, B, c, cb).value()), maxabs(L_gf(A, B).value()))
        print('trial %d (typical size of L terms: %.2e)' % (trial, scale))
        zero4 = [mzero() for _ in range(4)]
        dA_c = [mscale(-1j / g, Picomm(A, B, mu, w)) for mu in range(4)]
        dc_c, dcb_c = mscale(1j, comm(w, c)), mscale(1j, comm(w, cb))
        dA_u = [mscale(1j, comm(be, A[mu])) for mu in range(4)]
        dB_u = [madd(mscale(1j, comm(be, B[mu])), mscale(eta[mu] / g, mder(be, mu))) for mu in range(4)]
        dc_u, dcb_u = mscale(1j, comm(be, c)), mscale(1j, comm(be, cb))
        # consistency: dB_u has only the nbar^mu/2 structure (be depends on t+z only)
        okform = all(maxabs(mder(be, k)[i][j].value()) < 1e-12 for k in (1, 2) for i in range(2) for j in range(2)) and \
            all(abs(v) < 1e-12 for i in range(2) for j in range(2)
                for v in (madd(dB_u[0], dB_u[3])[i][j].value().values()))
        print('  usoft parameter depends on nbar.x only, dB^mu proportional to nbar^mu:', okform)
        allok &= okform
        allok &= report('collinear: delta L_F', first_order(L_F, [A, B], [dA_c, zero4]), True, scale)
        allok &= report('collinear: delta L_gh (ghosts adjoint)', first_order(L_gh, [A, B, c, cb], [dA_c, zero4, dc_c, dcb_c]), False, scale)
        allok &= report('collinear: delta L_gh (ghosts inert)', first_order(L_gh, [A, B, c, cb], [dA_c, zero4, mzero(), mzero()]), False, scale)
        allok &= report('collinear: delta L_gf', first_order(L_gf, [A, B], [dA_c, zero4]), False, scale)
        allok &= report('usoft:     delta L_F', first_order(L_F, [A, B], [dA_u, dB_u]), True, scale)
        allok &= report('usoft:     delta L_gh', first_order(L_gh, [A, B, c, cb], [dA_u, dB_u, dc_u, dcb_u]), True, scale)
        allok &= report('usoft:     delta L_gf', first_order(L_gf, [A, B], [dA_u, dB_u]), True, scale)
        # Free-field illustration: A = B = 0, ghosts adjoint -> delta L_gh = 2 tr(cbar [[iD_mu, i w], [i d^mu, c]]) != 0
        A0 = [mzero() for _ in range(4)]; B0 = [mzero() for _ in range(4)]
        dA0 = [mscale(-1j / g, Picomm(A0, B0, mu, w)) for mu in range(4)]
        allok &= report('collinear, free fields A=B=0: delta L_gh', first_order(L_gh, [A0, B0, c, cb], [dA0, zero4, dc_c, dcb_c]), False, scale)
        # BRST
        th = Gr({(0,): np.eye(1, NM, 0, dtype=complex)[0]}); thM = [[th, Gr()], [Gr(), th]]
        sA = [mscale(-1j / g, Picomm(A, B, mu, c)) for mu in range(4)]
        sc = mscale(1j, mmul(c, c))
        scb = mscale(1j / (alpha * g), Gfix(A, B))
        A2 = [madd(A[mu], mmul(thM, sA[mu])) for mu in range(4)]
        c2, cb2 = madd(c, mmul(thM, sc)), madd(cb, mmul(thM, scb))
        dLF = (L_F(A2, B) - L_F(A, B)).value()
        dLgf = (L_gf(A2, B) - L_gf(A, B)).value()
        dLgh = (L_gh(A2, B, c2, cb2) - L_gh(A, B, c, cb)).value()
        sumv = {k: dLgf.get(k, 0) + dLgh.get(k, 0) for k in set(dLgf) | set(dLgh)}
        allok &= report('BRST: s L_F', dLF, True, scale)
        allok &= report('BRST: s L_gf alone', dLgf, False, scale)
        allok &= report('BRST: s L_gh alone', dLgh, False, scale)
        allok &= report('BRST: s (L_gf + L_gh)', sumv, True, scale)
        # nilpotency on A
        th2 = Gr({(7,): np.eye(1, NM, 0, dtype=complex)[0]}); th2M = [[th2, Gr()], [Gr(), th2]]
        A3 = [madd(A[mu], mmul(th2M, sA[mu])) for mu in range(4)]
        c3 = madd(c, mmul(th2M, sc))
        m = 0.0
        for mu in range(4):
            dd = msub(mscale(-1j / g, Picomm(A3, B, mu, c3)), sA[mu])
            m = max(m, max(maxabs(dd[i][j].value()) for i in range(2) for j in range(2)))
        nil = m < 1e-9
        print('  %-60s max|.| = %10.3e  -> %-8s (%s)' % ('nilpotency: s(s A^mu) = 0 with s c = i c c', m, 'zero' if nil else 'NONZERO', 'PASS' if nil else 'FAIL'))
        allok &= nil
        # negative control: s c = -i c c breaks nilpotency
        c4 = madd(c, mmul(th2M, mscale(-1, sc)))
        m2 = 0.0
        for mu in range(4):
            dd = msub(mscale(-1j / g, Picomm(A3, B, mu, c4)), sA[mu])
            m2 = max(m2, max(maxabs(dd[i][j].value()) for i in range(2) for j in range(2)))
        print('  %-60s max|.| = %10.3e  (negative control, expected nonzero: %s)' % ('nilpotency with the wrong sign s c = -i c c', m2, 'PASS' if m2 > 1e-6 else 'FAIL'))
        allok &= m2 > 1e-6
    print('E25 checks:', 'ALL PASS' if allok else 'SOME FAIL')
