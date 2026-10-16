"""
spacelike_colour.py  --  Part (4) of research/c_glauber: colour algebra behind the violation of strict
collinear factorization in space-like collinear limits (Catani-de Florian-Rodrigo 2012, CdFR: JHEP 07 (2012)
026, arXiv:1112.4405v2) and the cancellation pattern in squared amplitudes (Forshaw-Seymour-Siodmok 2012, FSS:
JHEP 11 (2012) 066, arXiv:1206.6363v2).  All equation numbers below refer to these arXiv versions; the texts
were checked: CdFR eqs.(35)-(46), (65)-(68), (178)-(192); FSS eqs.(5.5)-(5.9), (6.1).

Colour-charge operators T_k^a act on n-parton colour tensors (all partons outgoing, Catani-Seymour
convention: outgoing quark t^a, outgoing antiquark -(t^a)^T, gluon (T^a_adj)_{bc} = -i f^{abc}; incoming
partons are treated as outgoing antipartons).

S1  colour conservation sum_k T_k |M> = 0 on singlet tensors; CdFR eq.(40) (T1+T2) Sp = Sp T_P.
S2  time-like coherence, CdFR eqs.(42)-(44): T_2 . sum_{j>=3} T_j  Sp|M> = -(C12+C2-C1)/2 Sp|M>.
S3  CdFR eq.(68): -T_2.sum_j T_j sign(s_j2) = (C12+C2-C1)/2 + 2 T_2.T_3   (s_23<0<s_j2, j>=4).
S4  non-factorization: Sp^+ (T_2.T_3) Sp is NOT proportional to the identity on the reduced colour space when
    n>=4 QCD partons (reduced space dim>=2), while it IS for n=3 (CdFR eq.(46)).
S5  FSS: f_abc T_i^a T_j^b T_k^c = i [T_i.T_j , T_j.T_k] (hermitian); in the trace basis all T_i.T_j are real;
    the CdFR two-loop tripole has zero expectation value on real-coefficient (pure-QCD tree) colour vectors and
    non-zero for complex relative phases (e.g. an s-channel W/Z width); the double commutator (three-loop
    structure) is non-zero on real vectors.
S6  CdFR eq.(187): Sp^+ f_abc T_1^a T_2^b Sp = 0 (colour conservation in the splitting).
S7  one-loop anti-hermitian breaking term i*delta_I drops out of 2 Re <M0|M1> (CdFR Sec.7.2: P^(1) strictly factorized).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

N = 3
def gellmann(N):
    Ts = []
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), complex); M[i, j] = M[j, i] = 0.5; Ts.append(M)
            M = np.zeros((N, N), complex); M[i, j] = -0.5j; M[j, i] = 0.5j; Ts.append(M)
    for k in range(1, N):
        M = np.zeros((N, N), complex)
        for i in range(k):
            M[i, i] = 1.0
        M[k, k] = -k
        M *= 1.0/np.sqrt(2*k*(k + 1)); Ts.append(M)
    return np.array(Ts)
T = gellmann(N); nA = N*N - 1
f = np.real(-2j*(np.einsum('aij,bjk,cki->abc', T, T, T) - np.einsum('bij,ajk,cki->abc', T, T, T)))
Tadj = np.array([-1j*f[a] for a in range(nA)])
CF, CA = (N*N - 1)/(2*N), N
GEN = {'q': T, 'qb': -np.transpose(T, (0, 2, 1)), 'g': Tadj}
CAS = {'q': CF, 'qb': CF, 'g': CA}
DIM = {'q': N, 'qb': N, 'g': nA}

def apply(gen, v, axis):
    """apply matrix gen (d x d) on tensor axis"""
    v = np.moveaxis(v, axis, 0)
    w = np.tensordot(gen, v, axes=(1, 0))
    return np.moveaxis(w, 0, axis)

def TdotT(types, i, j, v):
    return sum(apply(GEN[types[i]][a], apply(GEN[types[j]][a], v, j), i) for a in range(nA))

def inner(u, v):
    return np.vdot(u.reshape(-1), v.reshape(-1))

# ---------------- singlet bases ----------------
d = np.eye(N)
def basis_qqbar_qqbar():          # q1 qb2 q3 qb4
    e1 = np.einsum('ij,kl->ijkl', d, d)          # delta_{12} delta_{34}
    e2 = np.einsum('il,kj->ijkl', d, d)          # delta_{14} delta_{32}
    return ['q', 'qb', 'q', 'qb'], [e1, e2]
def basis_qqbar_qqbar_g():        # q1 qb2 q3 qb4 g5
    e1 = np.einsum('aij,kl->ijkla', T, d); e2 = np.einsum('ij,akl->ijkla', d, T)
    e3 = np.einsum('ail,kj->ijkla', T, d); e4 = np.einsum('il,akj->ijkla', d, T)
    return ['q', 'qb', 'q', 'qb', 'g'], [e1, e2, e3, e4]
def basis_qqbar_g():              # q1 qb2 g3
    return ['q', 'qb', 'g'], [np.einsum('aij->ija', T)]

print('=== S1: colour conservation ===')
for maker in [basis_qqbar_g, basis_qqbar_qqbar, basis_qqbar_qqbar_g]:
    types, B = maker()
    ok = True
    for e in B:
        tot = sum(sum(apply(GEN[types[k]][a], e, k) for k in range(len(types))) for a in range(nA)) if False else None
        for a in range(nA):
            s = sum(apply(GEN[types[k]][a], e, k) for k in range(len(types)))
            ok &= np.allclose(s, 0)
    check('S1 sum_k T_k^a |e> = 0 for the singlet basis of %s' % ' '.join(types), ok)

# splitting q(P) -> q(1) g(2): reduced space has parent P as first parton (an outgoing quark)
def split_q_to_qg(vred, types_red):
    # vred axes: (P, rest...) ; output axes: (1, 2, rest...)
    out = np.tensordot(np.transpose(T, (1, 0, 2)), vred, axes=(2, 0))   # T[a, i1, iP] -> (i1, a, rest)
    return out, ['q', 'g'] + types_red[1:]
def split_g_to_qqbar(vred, types_red):
    # g(P, colour c) -> q(1) qb(2): colour T^c_{i1 j2}
    out = np.tensordot(np.transpose(T, (1, 2, 0)), vred, axes=(2, 0))   # (i1, j2, rest)
    return out, ['q', 'qb'] + types_red[1:]
def split_g_to_gg(vred, types_red):
    # g(P,c) -> g(1,a) g(2,b): colour i f^{c a b}  (any normalization)
    out = np.tensordot(np.transpose(1j*f, (1, 2, 0)), vred, axes=(2, 0))
    return out, ['g', 'g'] + types_red[1:]

rng = np.random.default_rng(3)
# check CdFR (40): (T1 + T2)^a Sp v = Sp T_P^a v   on generic (non-singlet) reduced tensors
for split, Ptype in [(split_q_to_qg, 'q'), (split_g_to_qqbar, 'g'), (split_g_to_gg, 'g')]:
    types_red = [Ptype, 'qb', 'g'] if Ptype == 'q' else [Ptype, 'q', 'qb']
    shape = [DIM[t] for t in types_red]
    v = rng.normal(size=shape) + 1j*rng.normal(size=shape)
    sv, types = split(v, types_red)
    ok = True
    for a in range(nA):
        lhs = apply(GEN[types[0]][a], sv, 0) + apply(GEN[types[1]][a], sv, 1)
        rhs, _ = split(apply(GEN[Ptype][a], v, 0), types_red)
        ok &= np.allclose(lhs, rhs)
    check('S1b CdFR (40): (T_1+T_2) Sp = Sp T_P for splitting %s' % split.__name__, ok)

print('\n=== S2: time-like coherence (CdFR 42-44) ===')
cases = [(split_q_to_qg, basis_qqbar_qqbar, 'q'), (split_q_to_qg, basis_qqbar_g, 'q'),
         (split_g_to_qqbar, basis_qqbar_g, 'g'), (split_g_to_gg, basis_qqbar_g, 'g')]
for split, maker, Ptype in cases:
    types_red, B = maker()
    if types_red[0] != Ptype:
        # put a parton of the parent type first by permuting the basis (g is the last axis for qqbar_g)
        perm = [types_red.index(Ptype)] + [k for k in range(len(types_red)) if k != types_red.index(Ptype)]
        B = [np.transpose(e, perm) for e in B]; types_red = [types_red[k] for k in perm]
    coeffs = rng.normal(size=len(B)) + 1j*rng.normal(size=len(B))
    M = sum(c*e for c, e in zip(coeffs, B))
    v, types = split(M, types_red)
    lhs = sum(TdotT(types, 1, j, v) for j in range(2, len(types)))
    C12 = CAS[Ptype]; C1 = CAS[types[0]]; C2 = CAS[types[1]]
    ok = np.allclose(lhs, -0.5*(C12 + C2 - C1)*v)
    check('S2 %s with reduced %s: T_2.sum_{j>=3}T_j Sp|M> = -(C12+C2-C1)/2 Sp|M> = %.3f Sp|M>  (non-collinear partons act coherently as the parent)'
          % (split.__name__, ' '.join(types_red), -0.5*(C12 + C2 - C1)), ok)

print('\n=== S3/S4: space-like collinear limit in hadron-hadron collisions ===')
# reduced process (all outgoing): P = q (crossed: incoming antiquark... the physical assignment only enters via
# the signs s_j2), 3 = qbar, 4 = q', 5 = qbar'.  Physical SL configuration of CdFR eq.(66): parton 3 incoming
# (s_23 < 0), partons 4,5 outgoing (s_j2 > 0).
types_red, B = basis_qqbar_qqbar()
Bs = [];
for e in B:
    v, types = split_q_to_qg(e, types_red); Bs.append(v)
types = ['q', 'g', 'qb', 'q', 'qb']       # 1, 2, 3, 4, 5
C12, C1, C2 = CF, CF, CA
ok68 = True
for trial in range(3):
    c = rng.normal(size=2) + 1j*rng.normal(size=2)
    v = c[0]*Bs[0] + c[1]*Bs[1]
    sgn = {2: -1, 3: +1, 4: +1}          # axis index of partons 3,4,5 -> sign(s_j2): 3 incoming (-), 4,5 outgoing (+)
    lhs = -sum(sgn[j]*TdotT(types, 1, j, v) for j in [2, 3, 4])
    rhs = 0.5*(C12 + C2 - C1)*v + 2*TdotT(types, 1, 2, v)
    ok68 &= np.allclose(lhs, rhs)
check('S3 CdFR (68): -T_2.sum_j T_j sign(s_j2) = (C12+C2-C1)/2 + 2 T_2.T_3 on Sp|M>', ok68)
# S4: reduced matrix of T2.T3 between Sp e_r
G = np.array([[inner(a, b) for b in Bs] for a in Bs])
R = np.array([[inner(a, TdotT(types, 1, 2, b)) for b in Bs] for a in Bs])
Mred = np.linalg.solve(G, R)
offdiag = abs(Mred[0, 1]) + abs(Mred[1, 0]); diffdiag = abs(Mred[0, 0] - Mred[1, 1])
print('   Sp^+ (T2.T3) Sp in the reduced basis {delta12 delta34, delta14 delta32}: G^-1 R =\n', np.round(Mred, 6))
check('S4a n=5 (reduced 2->2 with 4 coloured partons): T_2.T_3 is NOT proportional to 1 on the reduced space -> strict collinear factorization violated',
      offdiag + diffdiag > 1e-6)
# n=4 coloured partons from the reduced q(P) qbar g amplitude: the breaking term 4 T_2.T_3 involves the colour of
# the *incoming* non-collinear parton 3 and cannot be removed by colour conservation; its value depends on which
# non-collinear parton is incoming (here the qbar or the g) -> the one-loop splitting matrix is process dependent.
types_red3, B3 = basis_qqbar_g()
v3, types3 = split_q_to_qg(B3[0], types_red3)          # partons: 0=q(1), 1=g(2), 2=qb, 3=g
nrm = inner(v3, v3)
t23_qb = (inner(v3, TdotT(types3, 1, 2, v3))/nrm).real   # incoming non-collinear parton = qbar
t23_g = (inner(v3, TdotT(types3, 1, 3, v3))/nrm).real    # incoming non-collinear parton = gluon
check('S4b q qbar g reduced amplitude: <T_2.T_j> for the incoming non-collinear parton j = qbar vs g differ (%.4f vs %.4f): the space-like one-loop splitting depends on the non-collinear colours'
      % (t23_qb, t23_g), abs(t23_qb - t23_g) > 1e-6)
# the 3-QCD-parton case of CdFR eq.(46): reduced q(P) qbar(3) + colourless: T_2.T_3 = -T_2.(T_1+T_2) = -(C12+C2-C1)/2
e_qq = d.copy()                                         # q(P) qbar(3) singlet
vq, typesq = split_q_to_qg(e_qq, ['q', 'qb'])
wq = TdotT(typesq, 1, 2, vq)
check('S4c CdFR (46): n=3 QCD partons, T_2.T_3 = -(C12+C2-C1)/2 = -C_A/2 (unit matrix: no colour correlation, only the i0 differs)',
      np.allclose(wq, -0.5*CA*vq))

print('\n=== S5: FSS cancellation pattern in squared amplitudes ===')
types5, B5 = basis_qqbar_qqbar_g()
# trace basis: check that all T_i.T_j are real matrices in this basis
G5 = np.array([[inner(a, b) for b in B5] for a in B5])
okreal = np.allclose(G5.imag, 0)
mats = {}
for i, j in itertools.combinations(range(5), 2):
    R5 = np.array([[inner(a, TdotT(types5, i, j, b)) for b in B5] for a in B5])
    O = np.linalg.solve(G5, R5)
    # verify the basis is closed under T_i.T_j
    for s in range(4):
        recon = sum(O[r, s]*B5[r] for r in range(4))
        okreal &= np.allclose(recon, TdotT(types5, i, j, B5[s]))
    okreal &= np.allclose(O.imag, 0)
    mats[(i, j)] = O.real
check('S5a q qbar q\' qbar\' g: trace basis closed under every T_i.T_j and all matrices (and the Gram matrix) are real', okreal)
# operator identity f_abc T_i^a T_j^b T_k^c = i [T_i.T_j, T_j.T_k]
v = sum((rng.normal() + 1j*rng.normal())*b for b in B5)
i_, j_, k_ = 1, 2, 3
trip = sum(f[a, b, c]*apply(GEN[types5[i_]][a], apply(GEN[types5[j_]][b], apply(GEN[types5[k_]][c], v, k_), j_), i_)
           for a in range(nA) for b in range(nA) for c in range(nA) if abs(f[a, b, c]) > 1e-12)
comm = 1j*(TdotT(types5, i_, j_, TdotT(types5, j_, k_, v)) - TdotT(types5, j_, k_, TdotT(types5, i_, j_, v)))
check('S5b operator identity f_abc T_i^a T_j^b T_k^c = i[T_i.T_j, T_j.T_k] (i,j,k distinct)', np.allclose(trip, comm))
def trip_op(vec):
    return 1j*(TdotT(types5, i_, j_, TdotT(types5, j_, k_, vec)) - TdotT(types5, j_, k_, TdotT(types5, i_, j_, vec)))
u = sum((rng.normal() + 1j*rng.normal())*b for b in B5)
check('S5c the tripole operator is hermitian', np.isclose(inner(u, trip_op(v)), np.conj(inner(v, trip_op(u)))))
vals_real = []
for t in range(5):
    c = rng.normal(size=4)
    vr = sum(ci*b for ci, b in zip(c, B5))
    vals_real.append(abs(inner(vr, trip_op(vr))))
check('S5d <M|tripole|M> = 0 for every real-coefficient colour vector (pure-QCD tree; FSS eq.(5.8))', max(vals_real) < 1e-12,
      'max=%.1e' % max(vals_real))
c = rng.normal(size=4).astype(complex); c[1] *= np.exp(0.7j)            # relative phase between colour flows
vc = sum(ci*b for ci, b in zip(c, B5))
val_c = inner(vc, trip_op(vc))
check('S5e with a relative phase between colour flows (e.g. s-channel W/Z width) the expectation value is non-zero',
      abs(val_c) > 1e-3, '<tripole> = %.4f' % val_c.real)
# commutator of two real-symmetric-type operators vs double commutator on real vectors
A = lambda x: TdotT(types5, 0, 2, x) + 0.37*TdotT(types5, 1, 4, x)     # 'eikonal-like' real colour operator
D = lambda x: TdotT(types5, 1, 2, x)                                      # Coulomb colour structure
vals1 = []; vals2 = []
for t in range(5):
    cr = rng.normal(size=4); vr = sum(ci*b for ci, b in zip(cr, B5))
    c1 = A(D(vr)) - D(A(vr))
    c2 = D(D(A(vr)) - A(D(vr))) - (D(A(D(vr))) - A(D(D(vr))))          # [D,[D,A]]
    vals1.append(abs(inner(vr, c1))); vals2.append(abs(inner(vr, c2)))
check('S5f <M|[A,D]|M> = 0 on real vectors (two-loop Coulomb x eikonal term cancels in pure QCD; FSS Sec.5)', max(vals1) < 1e-12,
      'max=%.1e' % max(vals1))
check('S5g <M|[D,[D,A]]|M> != 0 on real vectors (three-loop double-commutator survives: FSS eq.(6.1), SLL structure)',
      max(vals2) > 1e-3, 'max=%.3f' % max(vals2))

print('\n=== S6: CdFR (187) ===')
for split, Ptype, rest in [(split_q_to_qg, 'q', ['qb', 'g']), (split_g_to_qqbar, 'g', ['q', 'qb']), (split_g_to_gg, 'g', ['q', 'qb'])]:
    types_red = [Ptype] + rest
    shape = [DIM[t] for t in types_red]
    ok = True
    for trial in range(2):
        x = rng.normal(size=shape) + 1j*rng.normal(size=shape)
        y = rng.normal(size=shape) + 1j*rng.normal(size=shape)
        sx, types = split(x, types_red); sy, _ = split(y, types_red)
        for cidx in range(nA):
            op = sum(f[a, b, cidx]*apply(GEN[types[0]][a], apply(GEN[types[1]][b], sy, 1), 0)
                     for a in range(nA) for b in range(nA) if abs(f[a, b, cidx]) > 1e-12)
            ok &= abs(inner(sx, op)) < 1e-10
    check('S6 %s: Sp^+ f_abc T_1^a T_2^b Sp = 0' % split.__name__, ok)

print('\n=== S7: one-loop breaking term is anti-hermitian and cancels in 2Re<M0|M1> ===')
H = lambda x: 4*TdotT(types, 1, 2, x)          # hermitian colour operator of CdFR (67); breaking term = i*fI*H/eps
vals = []
for t in range(5):
    cc = rng.normal(size=2) + 1j*rng.normal(size=2)
    v = cc[0]*Bs[0] + cc[1]*Bs[1]
    vals.append(abs((inner(v, 1j*H(v))).real))
check('S7 Re<Sp M0| i*(4 T_2.T_3) |Sp M0> = 0 for arbitrary (even complex) tree colour vectors (P^(1) strictly factorized)', max(vals) < 1e-12)

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
