"""N17 (entanglement test) and N18 (gluonic-pole strengths) with explicit SU(N) generators (numpy), N = 2..6.
Independent of research/c_glauber/scripts/colour_factors.py: own generator construction, own index conventions,
explicit colour-singlet hadron wave functions, explicit colour-conservation check of all amplitude tensors.

Conventions: t^a Hermitian, Tr t^a t^b = delta/2.  Quark-gluon vertex inserts t^a on the fermion line
(for an incoming quark of index k entering the hard vertex with index k': factor t^a_{k'k};
for an outgoing quark of index c leaving the hard vertex with index c': t^a_{cc'}).
Antitriplet spectator (outgoing antiquark, index j, wave-function index j'): factor (-t^{aT})_{jj'}.
Catani-Seymour charges for N18: outgoing q: t; outgoing qbar: -t^T; incoming q: -t^T; incoming qbar: t.
Run: python3 -I -u n17_n18_colour.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction

npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + name + ('   [' + detail + ']' if detail else ''), flush=True)

def generators(N):
    """generalized Gell-Mann matrices / 2"""
    T = []
    for j in range(N):
        for k in range(j+1, N):
            m = np.zeros((N, N), complex); m[j, k] = m[k, j] = 1; T.append(m/2)
            m = np.zeros((N, N), complex); m[j, k] = -1j; m[k, j] = 1j; T.append(m/2)
    for l in range(1, N):
        m = np.zeros((N, N), complex)
        for j in range(l): m[j, j] = 1
        m[l, l] = -l
        T.append(m*np.sqrt(2/(l*(l+1)))/2)
    T = np.array(T)
    assert T.shape[0] == N*N - 1
    tr = np.einsum('aij,bji->ab', T, T)
    assert np.allclose(tr, np.eye(N*N-1)/2)
    return T

# =============================================================================================
# N17: two colour-singlet hadrons (q_i sbar_j), colour-neutral hard exchange q1 q2 -> q3 q4
# =============================================================================================
print('=== N17 entanglement test ===')
for N in [2, 3, 4, 5]:
    t = generators(N); NA = N*N - 1
    CF = (N*N - 1)/(2*N); TF = 0.5
    d = np.eye(N)
    psi = d/np.sqrt(N)                       # hadron wave function psi[i (quark), j' (spectator)]
    # tree amplitude A0[c, d4, j, l] : q3 index c, q4 index d4, spectator1 j, spectator2 l
    A0 = np.einsum('ij,kl->ikjl', psi, psi)     # H = delta_{c i} delta_{d k}
    norm0 = np.vdot(A0, A0).real
    def C1(X):   # single gluon from spectator 1 to line X, amplitude x tree*
        tot = 0
        for a in range(NA):
            S1 = -t[a].T
            L = {1: d.copy(), 2: d.copy(), 3: d.copy(), 4: d.copy()}
            L[X] = t[a] @ L[X]
            M1 = L[3] @ L[1]; M2 = L[4] @ L[2]
            T1 = np.einsum('ci,ij,Jj->cJ', M1, psi, S1)
            T2 = np.einsum('dk,kL->dL', M2, psi)
            tot += np.vdot(A0, np.einsum('cJ,dL->cdJL', T1, T2))
        return tot.real/norm0
    def C2(Y):   # single gluon from spectator 2 to Y: implement by symmetry (swap roles 1<->2)
        # gluon from spectator 2: use amp with ins1=None and ins2=Y
        tot = 0
        for b in range(NA):
            S2 = -t[b].T
            L = {1: d.copy(), 2: d.copy(), 3: d.copy(), 4: d.copy()}
            L[Y] = t[b] @ L[Y]
            M1 = L[3] @ L[1]; M2 = L[4] @ L[2]
            T1 = np.einsum('ci,iJ->cJ', M1, psi)
            T2 = np.einsum('dk,kl,Ll->dL', M2, psi, S2)
            A = np.einsum('cJ,dL->cdJL', T1, T2)
            tot += np.vdot(A0, A)
        return tot.real/norm0
    def Cboth(X, Y):
        """both virtual gluons in the amplitude (gluon a: spectator 1 -> line X; gluon b: spectator 2 -> line Y),
        conjugate = tree; colour weight relative to the tree"""
        tot = 0
        for a in range(NA):
            for b in range(NA):
                S1 = -t[a].T; S2 = -t[b].T
                L = {1: d.copy(), 2: d.copy(), 3: d.copy(), 4: d.copy()}
                L[X] = t[a] @ L[X]; L[Y] = t[b] @ L[Y]
                M1 = L[3] @ L[1]; M2 = L[4] @ L[2]
                T1 = np.einsum('ci,ij,Jj->cJ', M1, psi, S1); T2 = np.einsum('dk,kl,Ll->dL', M2, psi, S2)
                A = np.einsum('cJ,dL->cdJL', T1, T2)
                tot += np.vdot(A0, A)
        return tot.real/norm0
    c3, c4, c2 = C1(3), C1(4), C1(2)
    d4, d3, d1 = C2(4), C2(3), C2(1)
    report(abs(c3 + CF) < 1e-12 and abs(d4 + CF) < 1e-12, f'SU({N}): C_1(3) = C_2(4) = -C_F', f'{c3:.6f}, {d4:.6f}, -C_F={-CF:.6f}')
    report(max(abs(c4), abs(c2), abs(d3), abs(d1)) < 1e-12, f'SU({N}): C_1(4) = C_1(2) = C_2(3) = C_2(1) = 0')
    vals = {}
    for X in [3, 4, 2]:
        for Y in [4, 3, 1]:
            vals[(X, Y)] = Cboth(X, Y)
    cross = TF**2*(N*N - 1)/N**2
    ok = abs(vals[(3, 4)] - CF**2) < 1e-12
    ok &= all(abs(vals[(X, Y)] - cross) < 1e-12 for X in [4, 2] for Y in [3, 1])
    ok &= all(abs(vals[(X, Y)]) < 1e-12 for (X, Y) in [(3, 3), (3, 1), (4, 4), (2, 4)])
    tot = sum(vals.values())
    pred = CF**2 + 4*TF**2*(N*N - 1)/N**2
    report(ok and abs(tot - pred) < 1e-12, f'SU({N}) same side: C(3,4)=C_F^2, C(X,Y)=T_F^2(N^2-1)/N^2 for X in{{4,2}},Y in{{3,1}}, mixed 0; sum = C_F^2 + 4T_F^2(N^2-1)/N^2',
           f'sum={tot:.6f} pred={pred:.6f} product={CF**2:.6f}; extra/CF^2={(tot-CF**2)/CF**2:.6f} vs 4/(N^2-1)={4/(N*N-1):.6f}')

# opposite sides of the cut: gluon a (spectator 1 -> X) in the amplitude, gluon b (spectator 2 -> Y) in the conjugate.
# Colour weight: sum_{a,b} <A^{(b)}_Y | A^{(a)}_X> where the final state contains NO gluon (virtual gluons), so the
# two gluon colour indices are summed separately on each side -- each side is a single-gluon amplitude.
print('--- opposite sides of the cut ---')
for N in [2, 3, 4]:
    t = generators(N); NA = N*N - 1; CF = (N*N - 1)/(2*N); TF = 0.5; d = np.eye(N); psi = d/np.sqrt(N)
    A0 = np.einsum('ij,kl->ikjl', psi, psi); norm0 = np.vdot(A0, A0).real
    def single(spect, line):
        tot = np.zeros((N, N, N, N), complex)
        for a in range(NA):
            L = {1: d.copy(), 2: d.copy(), 3: d.copy(), 4: d.copy()}; L[line] = t[a] @ L[line]
            M1 = L[3] @ L[1]; M2 = L[4] @ L[2]
            S1 = -t[a].T if spect == 1 else d; S2 = -t[a].T if spect == 2 else d
            A = np.einsum('cJ,dL->cdJL', np.einsum('ci,ij,Jj->cJ', M1, psi, S1), np.einsum('dk,kl,Ll->dL', M2, psi, S2))
            tot += A   # NOTE: summing over a here is only legitimate because each side has ONE virtual gluon
        return tot
    # A virtual gluon's colour index is summed inside its own amplitude: single() returns the colour-summed amplitude
    vals = {}
    for X in [3, 4, 2]:
        for Y in [4, 3, 1]:
            vals[(X, Y)] = np.vdot(single(2, Y), single(1, X)).real/norm0
    cross = TF**2*(N*N - 1)/N**2
    tot = sum(vals.values()); pred = CF**2 + 4*TF**2*(N*N - 1)/N**2
    ok = abs(vals[(3, 4)] - CF**2) < 1e-12 and all(abs(vals[(X, Y)] - cross) < 1e-12 for X in [4, 2] for Y in [3, 1])
    report(ok and abs(tot - pred) < 1e-12, f'SU({N}) opposite sides: same colour weights, sum = C_F^2 + 4T_F^2(N^2-1)/N^2', f'sum={tot:.6f} pred={pred:.6f}')
print('   SU(3): C_F^2 =', Fraction(16, 9), ' actual =', Fraction(16, 9) + Fraction(4, 4)*Fraction(8, 9), '= 24/9')
# abelian check: charges e_s1 = -e_q1, lines carry charges; weights factorize
e1, e2 = 0.7, -1.3
ch = {1: e1, 3: e1, 2: e2, 4: e2}
w1 = {X: (-e1)*ch[X] for X in [3, 4, 2]}; w2 = {Y: (-e2)*ch[Y] for Y in [4, 3, 1]}
actual = sum(w1[X]*w2[Y] for X in w1 for Y in w2); product = sum(w1.values())*sum(w2.values())
report(abs(actual - product) < 1e-14, 'U(1): two-gluon weight = product of single-exchange weights (no entanglement)', f'{actual:.6f} = {product:.6f}')

# =============================================================================================
# N18: gluonic-pole strengths with the pole rule P = sum_out T - sum_{in, j != a} T = -T_a - 2 T_b
# =============================================================================================
print('=== N18 gluonic-pole strengths ===')
def cs_ops(N, kinds):
    """kinds: dict position -> 'q_in','qb_in','q_out','qb_out'. returns charge matrices acting on that index."""
    t = generators(N)
    ops = {}
    for pos, kd in kinds.items():
        if kd in ('q_out', 'qb_in'):  ops[pos] = t                       # T = t
        else:                         ops[pos] = -np.transpose(t, (0, 2, 1))   # T = -t^T
    return ops
def apply(op, M, pos):   # (op M)[..x..] = sum_x' op[x,x'] M[..x'..]
    M = np.moveaxis(M, pos, 0)
    M = np.tensordot(op, M, axes=([1], [0]))
    return np.moveaxis(M, 0, pos)
def dot_TT(N, M, Mp, ops, p1, p2):
    """<M| T_p1 . T_p2 |M'>"""
    t = generators(N); tot = 0
    for a in range(N*N - 1):
        tot += np.vdot(M, apply(ops[p1][a], apply(ops[p2][a], Mp, p2), p1))
    return tot
results = {}
for N in [2, 3, 4, 5, 6]:
    t = generators(N); NA = N*N - 1; CF = (N*N - 1)/(2*N)
    # index order of every amplitude tensor: [c, d, a, b]  (c,d outgoing; a,b incoming)
    Mt_qq = np.einsum('eca,edb->cdab', t, t)          # qq' -> qq', t-channel: a->c, b->d
    Mu_qq = np.einsum('eda,ecb->cdab', t, t)          # u-channel: a->d, b->c
    Mt_qqb = np.einsum('eca,ebd->cdab', t, t)         # q qbar' -> q qbar', t-channel (antiquark line d->b: t_{b d})
    Ms_qqb = np.einsum('ecd,eba->cdab', t, t)         # q qbar -> q' qbar', s-channel
    kinds_qq = {0: 'q_out', 1: 'q_out', 2: 'q_in', 3: 'q_in'}
    kinds_qqb = {0: 'q_out', 1: 'qb_out', 2: 'q_in', 3: 'qb_in'}
    ops_qq = cs_ops(N, kinds_qq); ops_qqb = cs_ops(N, kinds_qqb)
    # colour conservation check: sum_k T_k M = 0
    for name, M, ops in [('Mt_qq', Mt_qq, ops_qq), ('Mu_qq', Mu_qq, ops_qq), ('Mt_qqb', Mt_qqb, ops_qqb), ('Ms_qqb', Ms_qqb, ops_qqb)]:
        err = max(np.abs(sum(apply(ops[p][a], M, p) for p in range(4))).max() for a in range(NA))
        assert err < 1e-12, (name, err)
    diagrams = {1: (Mt_qq, Mt_qq, ops_qq), 2: (Mu_qq, Mu_qq, ops_qq), 3: (Mt_qq, Mu_qq, ops_qq),
                4: (Mt_qqb, Mt_qqb, ops_qqb), 5: (Ms_qqb, Ms_qqb, ops_qqb), 6: (Ms_qqb, Mt_qqb, ops_qqb)}
    for k, (M, Mp, ops) in diagrams.items():
        Cu = np.vdot(M, Mp)/N**2
        # attachment pole operators (sign s_X): outgoing +T_X, incoming b: -T_b ; contraction with -T_a
        CI = -(-dot_TT(N, M, Mp, ops, 2, 3))/N**2/CF          # <(-T_a).(-T_b)>
        CF1 = -dot_TT(N, M, Mp, ops, 2, 0)/N**2/CF             # <(-T_a).(+T_c)>
        CF2 = -dot_TT(N, M, Mp, ops, 2, 1)/N**2/CF             # <(-T_a).(+T_d)>
        TaTb = dot_TT(N, M, Mp, ops, 2, 3)/np.vdot(M, Mp)
        CG = (CI + CF1 + CF2)/Cu
        CG_formula = 1 + 2*TaTb/CF
        results[(N, k)] = dict(Cu=Cu.real, CI=CI.real, CF1=CF1.real, CF2=CF2.real, CG=CG.real, CGf=CG_formula.real, TaTb=TaTb.real)
# QVY Table I (arXiv:0706.1196v1), as functions of N
def qvy(N):
    return {1: dict(Cu=(N*N-1)/(4*N*N), CI=-1/(2*N*N), CF1=-1/(4*N*N), CF2=(N*N-2)/(4*N*N)),
            2: dict(Cu=(N*N-1)/(4*N*N), CI=-1/(2*N*N), CF1=(N*N-2)/(4*N*N), CF2=-1/(4*N*N)),
            3: dict(Cu=-(N*N-1)/(4*N**3), CI=(N*N+1)/(4*N**3), CF1=1/(4*N**3), CF2=1/(4*N**3)),
            4: dict(Cu=(N*N-1)/(4*N*N), CI=-(N*N-2)/(4*N*N), CF1=-1/(4*N*N), CF2=1/(2*N*N)),
            5: dict(Cu=(N*N-1)/(4*N*N), CI=1/(4*N*N), CF1=(N*N-2)/(4*N*N), CF2=1/(2*N*N)),
            6: dict(Cu=-(N*N-1)/(4*N**3), CI=-1/(4*N**3), CF1=1/(4*N**3), CF2=-(N*N+1)/(4*N**3))}
def bbmp(N):   # BBMP Table I gluonic-pole strengths
    return {1: (N*N-5)/(N*N-1), 2: (N*N-5)/(N*N-1), 3: -(N*N+3)/(N*N-1), 4: -(N*N-3)/(N*N-1), 5: (N*N+1)/(N*N-1), 6: (N*N+1)/(N*N-1)}
claimed_TaTb = lambda N: {1: -1/N, 2: -1/N, 3: -(N*N+1)/(2*N), 4: -(N*N-2)/(2*N), 5: 1/(2*N), 6: 1/(2*N)}
allok = True; worst = 0
for N in [2, 3, 4, 5, 6]:
    q = qvy(N); b = bbmp(N); tt = claimed_TaTb(N)
    for k in range(1, 7):
        r = results[(N, k)]
        # my C_I etc are normalised as C_X/C_F * Cu-type numbers: compare r['CI'] with QVY's C_I (QVY C_X = <M|..|M'>/(N^2 C_F))
        diffs = [abs(r['Cu'] - q[k]['Cu']), abs(r['CI'] - q[k]['CI']), abs(r['CF1'] - q[k]['CF1']), abs(r['CF2'] - q[k]['CF2']),
                 abs(r['CG'] - b[k]), abs(r['CGf'] - b[k]), abs(r['TaTb'] - tt[k])]
        worst = max(worst, max(diffs))
        if max(diffs) > 1e-12:
            allok = False
            print(f'   mismatch N={N} diagram {k}:', r, q[k], b[k])
report(allok, 'QVY Table I (C_u, C_I, C_F1, C_F2 for all 6 diagrams) reproduced graph by graph from the pole rule, N=2..6', f'max |diff| = {worst:.1e}')
report(allok, 'BBMP Table I C_G for all channels = (C_I+C_F1+C_F2)/C_u = 1 + 2<T_a.T_b>/C_F, N=2..6')
N = 3
print('   SU(3) values: ' + ', '.join(f'({k}) C_G={results[(N,k)]["CG"]:.4f} <TaTb>={results[(N,k)]["TaTb"]:.4f}' for k in range(1, 7)))
r1 = results[(3, 1)]
report(abs(r1['CI']/r1['Cu'] + 2/8) < 1e-12 and abs(r1['CF1']/r1['Cu'] + 1/8) < 1e-12 and abs(r1['CF2']/r1['Cu'] - 7/8) < 1e-12,
       'SU(3) diagram (1): C_I/C_u = -1/4, C_F1/C_u = -1/8, C_F2/C_u = 7/8 (= -2/(N^2-1), -1/(N^2-1), (N^2-2)/(N^2-1))')
for N in [2, 4, 6]:
    r1 = results[(N, 1)]
    ok = (abs(r1['CI']/r1['Cu'] + 2/(N*N-1)) < 1e-12 and abs(r1['CF1']/r1['Cu'] + 1/(N*N-1)) < 1e-12
          and abs(r1['CF2']/r1['Cu'] - (N*N-2)/(N*N-1)) < 1e-12)
    report(ok, f'SU({N}) diagram (1) ratios -2/(N^2-1), -1/(N^2-1), (N^2-2)/(N^2-1)')
# SIDIS / DY normalisations
for N in [2, 3, 5]:
    t = generators(N); CF = (N*N - 1)/(2*N)
    M = np.einsum('ca->ca', np.eye(N))   # SIDIS: q(a) -> q(c), colourless photon; positions [c, a]
    opsS = {0: t, 1: -np.transpose(t, (0, 2, 1))}
    tot = sum(np.vdot(M, apply(-opsS[1][a], apply(opsS[0][a], M, 0), 1)) for a in range(N*N-1))/np.vdot(M, M)
    # DY: q(a) qbar(b) -> gamma*: tensor [a, b] = delta_{b a}; P = -T_b
    Md = np.eye(N); opsD = {0: -np.transpose(t, (0, 2, 1)), 1: t}
    totd = sum(np.vdot(Md, apply(-opsD[0][a], apply(-opsD[1][a], Md, 1), 0)) for a in range(N*N-1))/np.vdot(Md, Md)
    report(abs(tot/CF - 1) < 1e-12 and abs(totd/CF + 1) < 1e-12, f'SU({N}): SIDIS C_G = +1, DY C_G = -1 with the same pole rule', f'{(tot/CF).real:.3f}, {(totd/CF).real:.3f}')

print(f'\nSUMMARY: {npass}/{npass+nfail} PASS')
