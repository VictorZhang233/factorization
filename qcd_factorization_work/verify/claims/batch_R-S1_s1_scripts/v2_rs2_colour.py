"""R-S2 (second, independent verification run): colour bookkeeping of one Glauber gluon from the
spectator of hadron A attaching to the other partons j in {b, c, d} of a 2->2 hard process a b -> c d,
explicit SU(N) colour tensors (N = 3, also N = 2, 4), qq' -> qq'.

Conventions.  "in = out": T_j acts on the colour index of parton j as the generator of its own
representation; colour conservation reads T_a + T_b = T_c + T_d on invariant tensors.
Eikonal factor of a gluon with momentum k flowing INTO line j (uniform numerator for an A-collinear k):
   incoming j:  + T_j / (n.k + i0)      outgoing j:  - T_j / (n.k - i0)
(the relative minus sign for an outgoing line comes from (p-k)^2 - m^2 = -2p.k).  delta-parts:
   1/(x+i0) -> -i pi delta(x),   -1/(x-i0) -> -i pi delta(x):  SAME sign for initial and final lines.
Reference p. 74 instead writes sum_j eta_j T_j/(n.k + i eta_j 0) with in = out conservation.

Checks:
 (1) T_a+T_b = T_c+T_d on the invariant subspace (in = out);
 (2) reference combination eta_b T_b + eta_c T_c + eta_d T_d (eta_c = eta_d = -eta_b) = -eta_b T_a on invariants;
 (3) correct pole part  -(T_b + T_c + T_d) = -(T_a + 2 T_b)  is NOT proportional to T_a;
     all-outgoing form T_b' - T_c - T_d = T_a' + 2 T_b' with T_a' = -T_a, T_b' = -T_b;
 (4) SIDIS / DY: correct bookkeeping gives opposite signs (Sivers flip); reference bookkeeping gives the same;
 (5) gluonic-pole strength C_G = <T_a.P>/<T_a.P_SIDIS> = 1 + 2<T_a.T_b>/C_F, qq'->qq' t-channel (tt*):
     (N^2-5)/(N^2-1) = 1/2 for SU(3);
 (6) abelian analogue = Collins-Qiu eqs. (4.1)-(4.3): charges g_b = g2 (initial, eq. 4.2), g_d = g2 (final, 4.1),
     g_c = g1 (final, 4.3), g_a = g1: correct bookkeeping -> g1 + 2 g2; reference bookkeeping -> -g1.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
LOG = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; LOG.append(s); print(s, flush=True)

def suN(N):
    g = []
    for i in range(N):
        for j in range(i+1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = .5; g.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -.5j; m[j, i] = .5j; g.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex); m[np.arange(k), np.arange(k)] = 1; m[k, k] = -k
        g.append(m/np.sqrt(2*k*(k+1)))
    return np.array(g)

for N in (2, 3, 4):
    t = suN(N); ng = N*N-1; CF = (N*N-1)/(2*N)
    d = np.eye(N)
    # amplitude tensors M[a,b,c,d] (a,b incoming, c,d outgoing quark colour indices)
    M1 = np.einsum('ac,bd->abcd', d, d)            # a->c, b->d colour flow
    M2 = np.einsum('ad,bc->abcd', d, d)            # a->d, b->c
    Mt = np.einsum('xca,xdb->abcd', t, t)          # one-gluon t-channel exchange (a->c, b->d)
    # generators acting on leg indices (adjoint index x free):
    def Ta(M): return np.einsum('xpa,pbcd->xabcd', t, M)    # incoming leg: M^{a'..} t_{a'a}
    def Tb(M): return np.einsum('xpb,apcd->xabcd', t, M)
    def Tc(M): return np.einsum('xcp,abpd->xabcd', t, M)    # outgoing leg: t_{cc'} M_{..c'..}
    def Td(M): return np.einsum('xdp,abcp->xabcd', t, M)
    ok1 = all(np.allclose(Ta(M)+Tb(M), Tc(M)+Td(M)) for M in (M1, M2, Mt))
    rep(f'SU({N}) (1) in=out conservation on invariants', ok1)
    # (2) reference combination with eta_b = +1, eta_c = eta_d = -1
    ok2 = all(np.allclose(Tb(M)-Tc(M)-Td(M), -Ta(M)) for M in (M1, M2, Mt))
    rep(f'SU({N}) (2) reference eta_bT_b+eta_cT_c+eta_dT_d = -eta_b T_a (reducible)', ok2)
    # (3) correct pole part G = -(T_b+T_c+T_d) = -(T_a+2T_b); is it k*T_a for some k?  test on Mt
    G = -(Tb(Mt)+Tc(Mt)+Td(Mt)); A = Ta(Mt)
    ok3a = np.allclose(G, -(Ta(Mt)+2*Tb(Mt)))
    k = np.vdot(A.ravel(), G.ravel())/np.vdot(A.ravel(), A.ravel())
    resid = np.linalg.norm(G - k*A)/np.linalg.norm(G)
    rep(f'SU({N}) (3) correct pole part -(T_a+2T_b) irreducible', ok3a and resid > 0.3,
        f'||G - kT_a||/||G|| = {resid:.3f} at best k = {k.real:.3f}')
    # all-outgoing form
    Tap = lambda M: -Ta(M); Tbp = lambda M: -Tb(M)
    ok3b = np.allclose(Tbp(Mt)-Tc(Mt)-Td(Mt), Tap(Mt)+2*Tbp(Mt)) and np.allclose(Tap(Mt)+Tbp(Mt)+Tc(Mt)+Td(Mt), 0)
    rep(f'SU({N}) (3b) all-outgoing: T_b\'-T_c-T_d = T_a\'+2T_b\', sum T\' = 0', ok3b)
    # (4) SIDIS (a -> c, only j = c, final) and DY (a + b -> singlet, only j = b, initial).
    # Pole parts written as coefficients of (-i pi delta): correct bookkeeping gives T_j for incoming AND
    # outgoing j (in = out); the reference gives eta_j T_j.
    S = d                                       # SIDIS colour tensor S[a,c] = delta_ac
    TaS = np.einsum('xpa,pc->xac', t, S); TcS = np.einsum('xcp,ap->xac', t, S)
    D_ = d/np.sqrt(N)                           # DY: a (quark) b (antiquark) -> colour singlet, D[a,b]
    TaD = np.einsum('xpa,pb->xab', t, D_)
    TbD = -np.einsum('xbq,aq->xab', t, D_)      # incoming antiquark: generator -t^T acting on index b
    okDYcons = np.allclose(TaD + TbD, 0)
    P_sidis = TcS; P_dy = TbD                   # correct
    flip = np.allclose(P_sidis, TaS) and np.allclose(P_dy, -TaD) and okDYcons
    R_sidis = -TcS; R_dy = +TbD                 # reference: eta_c = -1 (final), eta_b = +1 (initial)
    noflip = np.allclose(R_sidis, -TaS) and np.allclose(R_dy, -TaD)
    rep(f'SU({N}) (4) Sivers: correct SIDIS +T_a vs DY -T_a (flip); reference -T_a in both (no flip)', flip and noflip,
        f'DY conservation T_a+T_b=0: {okDYcons}')
    # (5) gluonic-pole strength for qq'->qq' t-channel amplitude: C_G = 1 + 2<T_a.T_b>/C_F
    TaTb = np.einsum('xpa,xqb,pqcd->abcd', t, t, Mt)
    TaTb_exp = np.vdot(Mt.ravel(), TaTb.ravel()).real/np.vdot(Mt.ravel(), Mt.ravel()).real
    CG = 1 + 2*TaTb_exp/CF
    # direct: <T_a . P>/<T_a . P_SIDIS> with P = -T_a - 2T_b (in = out), P_SIDIS = -T_a
    TaP = -(np.einsum('xpa,xqp,qbcd->abcd', t, t, Mt) + 2*TaTb)
    num = np.vdot(Mt.ravel(), TaP.ravel()).real/np.vdot(Mt.ravel(), Mt.ravel()).real
    CG2 = num/(-CF)
    rep(f'SU({N}) (5) C_G(qq\'->qq\', tt*) = (N^2-5)/(N^2-1)', abs(CG-(N*N-5)/(N*N-1)) < 1e-12 and abs(CG2-CG) < 1e-12,
        f'C_G = {CG:.6f} (direct {CG2:.6f}), formula {(N*N-5)/(N*N-1):.6f}')

# (6) abelian Collins-Qiu
g1, g2 = 0.731, 1.37
charges = {'b': g2, 'c': g1, 'd': g2}; ga = g1
correct = charges['b'] + charges['c'] + charges['d']           # same-sign delta parts, in = out
reference = charges['b'] - charges['c'] - charges['d']         # eta_b = +1, eta_c = eta_d = -1
rep('(6) abelian Collins-Qiu (4.1)-(4.3): total i pi (g1 + 2 g2)', abs(correct-(g1+2*g2)) < 1e-15 and abs(correct-(ga+2*charges['b'])) < 1e-15,
    f'correct bookkeeping {correct:.4f} = g1+2g2 = {g1+2*g2:.4f}; reference bookkeeping {reference:.4f} = -g1 = {-g1:.4f}')
print('\nSUMMARY:', sum('PASS' in s for s in LOG), 'PASS,', sum('FAIL' in s for s in LOG), 'FAIL')
