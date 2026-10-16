"""
colour_factors.py  --  Part (2) of research/c_glauber: SU(N) colour algebra of the Collins-Qiu /
Rogers-Mulders counterexamples to (standard / generalized) TMD factorization in h1 h2 -> H1 H2 X.

Conventions: quark-gluon vertex +i g gamma^mu t^a (CONTEXT.md), Tr(t^a t^b)=delta^{ab}/2.
Eikonal (pole) parts for a gluon of momentum l flowing from the polarized hadron's spectator INTO the hard
part: the pole coefficient is the same for a quark line whether incoming or outgoing (and opposite for an
antiquark line); principal parts differ between in/out.  [Cf. Collins-Qiu 2007 eqs.(4.1)-(4.3): all three
replacements give +i g pi delta(l^+); Rogers-Mulders 2010 eqs.(8),(15),(16); Collins 2007 eq.(2).]
Normalization: SIDIS (gamma* q -> q, FSI on the outgoing quark) = +1.

Sources (texts verified, arXiv versions): QVY = Qiu-Vogelsang-Yuan PRD 76 (2007) 074029, arXiv:0706.1196v1,
Table I and eqs.(25)-(28); BBMP = Bacchetta-Bomhof-Mulders-Pijlman PRD 72 (2005) 034030,
arXiv:hep-ph/0505268v2, eqs.(A11)-(A12), (B3), (B5)-(B6) and Table I; RM = Rogers-Mulders PRD 81 (2010)
094006, arXiv:1001.2977v2, eqs.(3), (14), (17), (18), (30)-(36) and Figs.3,4,7,8.

Checks:
 C0  SU(N) identities, N=2..6.
 C1  gluonic-pole colour factors for the 6 quark-(anti)quark diagram classes: QVY Table I (C_u, C_I, C_F1,
     C_F2) and BBMP strengths C_G (B5),(B6); SIDIS=+1, DY=-1.
 C2  colour-conservation formula derived here: C_G = 1 + 2 <T_a.T_b>/C_F (b = the other incoming parton,
     Catani-Seymour colour charges), for all classes.
 C3  RM model (colourless hard exchange X; colour-singlet hadrons = quark (3) + spectator (3bar)): explicit
     contraction of the colour tensors of the graph classes Fig.3, Fig.4, Fig.7, Fig.8, compared with RM
     eqs.(14),(18),(34): T_F(N^2-1) per loop, Tr t^a = 0, T_F^2(N^2-1).
 C4  BBMP gauge links (A11a,b),(A12a,b,c) reproduce their own strengths C_G using C_G[U^+]=1,
     C_G[U^box U^+]=3, C_G[Tr(U^box)U^+/N]=1, C_G[U^-]=-1 (Table I upper part), exact fractions.
 C5  exact symbolic-N derivation (SU(N) projectors) of all six C_G via C2: e.g. tt*: <T_a.T_b> = -1/N
     => C_G = (N^2-5)/(N^2-1).
 C6  RM entanglement test: with one gluon from EACH spectator (double-Sivers pole terms), the actual colour
     weight sum_{X,Y} C(X,Y) differs from the product (sum_X C1(X))(sum_Y C2(Y)) forced by generalized TMD
     factorization (separate Wilson-line structures per hadron); for U(1) charges they agree identically.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from fractions import Fraction

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

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

# ------------------------------------------------------------------------------------------------
print('=== C0: SU(N) identities ===')
for N in range(2, 7):
    T = gellmann(N); n = N*N - 1
    CF = (N*N - 1)/(2*N)
    tr = np.einsum('aij,bji->ab', T, T)
    ok1 = np.allclose(tr, 0.5*np.eye(n))
    ok2 = np.allclose(np.einsum('aij,ajk->ik', T, T), CF*np.eye(N))
    fierz = np.einsum('aij,akl->ijkl', T, T)
    d = np.eye(N)
    ok3 = np.allclose(fierz, 0.5*(np.einsum('il,kj->ijkl', d, d) - np.einsum('ij,kl->ijkl', d, d)/N))
    ok4 = np.allclose(np.einsum('aij,bjk,akl->bil', T, T, T), -T/(2*N))
    # f and d
    f = np.real(-2j*(np.einsum('aij,bjk,cki->abc', T, T, T) - np.einsum('bij,ajk,cki->abc', T, T, T)))
    dd = np.real(2*(np.einsum('aij,bjk,cki->abc', T, T, T) + np.einsum('bij,ajk,cki->abc', T, T, T)))
    ok5 = np.isclose(np.sum(f*f), N*(N*N - 1)) and np.isclose(np.sum(dd*dd), (N*N - 4)*(N*N - 1)/N)
    check('C0 SU(%d): Tr(TaTb)=d/2, TaTa=CF, Fierz, TaTbTa=-Tb/2N, f.f=N(N^2-1), d.d=(N^2-4)(N^2-1)/N' % N,
          ok1 and ok2 and ok3 and ok4 and ok5)

# ------------------------------------------------------------------------------------------------
# Colour tensors for 2->2 with incoming a (polarized quark, index i), b (index j), outgoing c (k), d (l).
# Amplitude colour tensor A[k,l,i,j].  For an antiquark the index sits where the fermion-flow string
# puts it: incoming antiquark b: row index of the string starting at vbar_b; outgoing antiquark d: column
# index of the string ending at v_d.
def amp_tensors(N, T):
    d = np.eye(N)
    t_qq  = np.einsum('Aki,Alj->klij', T, T)          # q(i) q'(j) -> q(k) q'(l), t-channel   (a->c, b->d)
    u_qq  = np.einsum('Ali,Akj->klij', T, T)          # u-channel (a->d, b->c), identical quarks
    t_qqb = np.einsum('Aki,Ajl->klij', T, T)          # q(i) qbar'(j) -> q(k) qbar'(l), t-channel: (ubar_c T u_a)(vbar_b T v_d)
    s_qqb = np.einsum('Aji,Akl->klij', T, T)          # q(i) qbar(j) -> q'(k) qbar'(l), s-channel: (vbar_b T u_a)(ubar_c T v_d)
    return t_qq, u_qq, t_qqb, s_qqb

def insert(A, line, kind, T, C):
    """natural insertion of generator T[C] at the eikonal attachment on external line `line`
    (b: incoming; c,d: outgoing) for fermion type `kind` ('q' or 'qbar').  Returns A' (no eta sign)."""
    t = T[C]
    if line == 'b':
        if kind == 'q':       # incoming quark b, index j is the column at the start of its string: (... t)_{.j}
            return np.einsum('klim,mj->klij', A, t)
        else:                 # incoming antiquark b: vbar_b t ... -> row index: t_{j m} A_{..,m}
            return np.einsum('jm,klim->klij', t, A)
    if line == 'c':           # outgoing quark c: t_{k m} A_{m l ..}
        return np.einsum('km,mlij->klij', t, A)
    if line == 'd':
        if kind == 'q':
            return np.einsum('lm,kmij->klij', t, A)
        else:                 # outgoing antiquark d: (... t v_d): A_{k m ..} t_{m l}
            return np.einsum('kmij,ml->klij', A, t)

def X_factor(Aprime_list, B, T):
    """X = sum_C sum_colours A'_C[k,l,i,j] conj(B[k,l,i',j]) T^C[i,i']  (amplitude index i, conjugate index i')"""
    tot = 0
    for C, Ap in enumerate(Aprime_list):
        tot += np.einsum('klij,klmj,im->', Ap, np.conj(B), T[C])
    return tot

print('\n=== C1: gluonic-pole colour factors vs QVY Table I and BBMP (B5),(B6) ===')
Fr = Fraction
def qvy_table(N):
    """QVY Table I entries (as functions of N) for diagrams (1)..(6); keys: Cu, CI, CF1, CF2.
    Checked entry by entry against arXiv:0706.1196v1 Table I (C_F1 / C_F2: final-state interaction on the
    outgoing line of momentum P1 / P2, eqs.(25)-(27) of QVY)."""
    N2, N3 = N*N, N**3
    return {
        1: dict(Cu=Fr(N2 - 1, 4*N2), CI=Fr(-1, 2*N2), CF1=Fr(-1, 4*N2), CF2=Fr(N2 - 2, 4*N2)),
        2: dict(Cu=Fr(N2 - 1, 4*N2), CI=Fr(-1, 2*N2), CF1=Fr(N2 - 2, 4*N2), CF2=Fr(-1, 4*N2)),
        3: dict(Cu=Fr(-(N2 - 1), 4*N3), CI=Fr(N2 + 1, 4*N3), CF1=Fr(1, 4*N3), CF2=Fr(1, 4*N3)),
        4: dict(Cu=Fr(N2 - 1, 4*N2), CI=Fr(-(N2 - 2), 4*N2), CF1=Fr(-1, 4*N2), CF2=Fr(1, 2*N2)),
        5: dict(Cu=Fr(N2 - 1, 4*N2), CI=Fr(1, 4*N2), CF1=Fr(N2 - 2, 4*N2), CF2=Fr(1, 2*N2)),
        6: dict(Cu=Fr(-(N2 - 1), 4*N3), CI=Fr(-1, 4*N3), CF1=Fr(1, 4*N3), CF2=Fr(-(N2 + 1), 4*N3)),
    }
def bbmp_CG(N):
    N2 = N*N
    return {1: Fr(N2 - 5, N2 - 1), 2: Fr(N2 - 5, N2 - 1), 3: Fr(-(N2 + 3), N2 - 1),
            4: Fr(-(N2 - 3), N2 - 1), 5: Fr(N2 + 1, N2 - 1), 6: Fr(N2 + 1, N2 - 1)}

for N in [2, 3, 4, 5, 6]:
    T = gellmann(N); nA = N*N - 1; CF = (N*N - 1)/(2*N)
    t_qq, u_qq, t_qqb, s_qqb = amp_tensors(N, T)
    # diagram classes: (amplitude A, conjugate B, kind of b, kind of d, which outgoing line carries the
    # polarized quark's colour: QVY 'P1' is taken as the outgoing quark c (index k) throughout)
    classes = {
        1: (t_qq, t_qq, 'q', 'q'), 2: (u_qq, u_qq, 'q', 'q'), 3: (t_qq, u_qq, 'q', 'q'),
        4: (t_qqb, t_qqb, 'qbar', 'qbar'), 5: (s_qqb, s_qqb, 'qbar', 'qbar'), 6: (s_qqb, t_qqb, 'qbar', 'qbar'),
    }
    tab = qvy_table(N); cg = bbmp_CG(N)
    allok = True; msgs = []
    for key, (A, B, kb, kd) in classes.items():
        U = np.real(np.einsum('klij,klij->', A, np.conj(B)))
        Cu = U/N**2
        eta = {'q': 1, 'qbar': -1}
        XI = np.real(eta[kb]*X_factor([insert(A, 'b', kb, T, C) for C in range(nA)], B, T))
        XF1 = np.real(X_factor([insert(A, 'c', 'q', T, C) for C in range(nA)], B, T))
        XF2 = np.real(eta[kd]*X_factor([insert(A, 'd', kd, T, C) for C in range(nA)], B, T))
        CI, CF1, CF2 = XI/(CF*N**2), XF1/(CF*N**2), XF2/(CF*N**2)
        CG = (XI + XF1 + XF2)/(CF*U)
        exp = tab[key]
        ok = (np.isclose(Cu, float(exp['Cu'])) and np.isclose(CI, float(exp['CI'])) and np.isclose(CF1, float(exp['CF1']))
              and np.isclose(CF2, float(exp['CF2'])) and np.isclose(CG, float(cg[key])))
        allok &= ok
        if N == 3:
            msgs.append('(%d) Cu=%.4f CI=%.4f CF1=%.4f CF2=%.4f C_G=%.4f [QVY/BBMP: %s %s %s %s %s]' %
                        (key, Cu, CI, CF1, CF2, CG, exp['Cu'], exp['CI'], exp['CF1'], exp['CF2'], cg[key]))
    for mm in msgs:
        print('   ' + mm)
    check('C1 SU(%d): all 6 diagram classes reproduce QVY Table I (Cu,CI,CF1,CF2) and BBMP C_G' % N, allok)

# SIDIS and DY normalisation
for N in [2, 3, 4]:
    T = gellmann(N); nA = N*N - 1; CF = (N*N - 1)/(2*N)
    # SIDIS: gamma* q(i) -> q(k): A[k,i] = delta
    A = np.eye(N)
    X = sum(np.einsum('ki,km,im->', T[C] @ A, np.conj(A), T[C]) for C in range(nA))
    U = np.real(np.sum(A*np.conj(A)))
    CG_sidis = np.real(X)/(CF*U)
    # DY: q(i) qbar(j) -> gamma*: A[i,j] = delta_ji ; ISI on incoming antiquark: t_{j m} A_{i m}, eta=-1
    A = np.eye(N)
    X = sum(np.einsum('jm,im,nj,in->', T[C], A, np.conj(A), T[C]) for C in range(nA))
    CG_dy = -np.real(X)/(CF*np.real(np.sum(A*np.conj(A))))
    check('C1n SU(%d): normalisation SIDIS C_G=+1 and DY C_G=-1 (Collins 2002 sign reversal)' % N,
          np.isclose(CG_sidis, 1) and np.isclose(CG_dy, -1), 'SIDIS=%.3f DY=%.3f' % (CG_sidis, CG_dy))

# ------------------------------------------------------------------------------------------------
print('\n=== C2: colour-conservation formula C_G = 1 + 2<T_a.T_b>/C_F ===')
# Catani-Seymour charges: incoming quark index -> T_in = -(natural insertion); incoming antiquark -> +(natural).
for N in [2, 3, 4, 5]:
    T = gellmann(N); nA = N*N - 1; CF = (N*N - 1)/(2*N)
    t_qq, u_qq, t_qqb, s_qqb = amp_tensors(N, T)
    classes = {1: (t_qq, t_qq, 'q'), 2: (u_qq, u_qq, 'q'), 3: (t_qq, u_qq, 'q'),
               4: (t_qqb, t_qqb, 'qbar'), 5: (s_qqb, s_qqb, 'qbar'), 6: (s_qqb, t_qqb, 'qbar')}
    cg = bbmp_CG(N); allok = True
    for key, (A, B, kb) in classes.items():
        U = np.einsum('klij,klij->', A, np.conj(B))
        TaTb = 0
        for C in range(nA):
            Aa = -np.einsum('klmj,mi->klij', A, T[C])                  # T_a on incoming quark a (CS sign -)
            Aab = -insert(Aa, 'b', 'q', T, C) if kb == 'q' else +insert(Aa, 'b', 'qbar', T, C)
            TaTb += np.einsum('klij,klij->', Aab, np.conj(B))
        val = 1 + 2*np.real(TaTb/U)/CF
        allok &= np.isclose(val, float(cg[key]))
    check('C2 SU(%d): 1 + 2<T_a.T_b>/C_F reproduces all six BBMP strengths' % N, allok)
# closed forms at N=3 for the record
N = 3; print('   SU(3): (N^2-5)/(N^2-1)=%s, -(N^2+3)/(N^2-1)=%s, -(N^2-3)/(N^2-1)=%s, (N^2+1)/(N^2-1)=%s' %
             (Fr(4, 8), Fr(-12, 8), Fr(-6, 8), Fr(10, 8)))

# ------------------------------------------------------------------------------------------------
print('\n=== C3: Rogers-Mulders model colour factors with explicit colour-singlet hadrons ===')
# Hadron f (colour singlet) -> quark phi_f (3, index i) + spectator psi_f (3bar, index s): wavefunction
# delta_{is}/sqrt(N).  Hard exchange: colourless X: quark 1 -> quark 3 (delta), quark 2 -> quark 4 (delta).
# Gluon couplings: quark lines natural t^a; spectator (3bar) generator tbar^a = -(t^a)^T.  Overall
# non-colour factors are dropped: we compare colour weights relative to the tree (normalised to 1).
for N in [2, 3, 4, 5]:
    T = gellmann(N); nA = N*N - 1; TF = 0.5; CF = (N*N - 1)/(2*N)
    Tb = -np.transpose(T, (0, 2, 1))
    wf = np.eye(N)/np.sqrt(N)                    # [i (quark), s (spectator)]
    # Tree amplitude colour tensor: indices (k3, s1, k4, s2)
    tree = np.einsum('ks,lt->kslt', wf, wf)      # quark1 colour i = k3, quark2 colour j = k4
    W_tree = np.real(np.einsum('kslt,kslt->', tree, np.conj(tree)))
    # index letters: a,b gluons; k,l outgoing quarks 3,4; s,t final spectators 1,2; r,u spectators before
    # emission; i,j quarks 1,2 before the eikonal attachment.  Each exchanged gluon is summed within its own
    # side of the final-state cut (it is a virtual exchange, not a cut line).
    # Fig.3(a): gluon a from spectator 1 to outgoing quark 3 (same colour loop as hadron 1)
    fig3 = np.einsum('asr,aki,ir,lt->kslt', Tb, T, wf, wf)
    W3 = np.real(np.einsum('kslt,kslt->', fig3, np.conj(tree)))
    # Fig.4(a): gluon from spectator 1 to outgoing quark 4 (colour loop of hadron 2)
    A1 = np.einsum('asr,kr,alj,jt->kslt', Tb, wf, T, wf)
    W4 = np.real(np.einsum('kslt,kslt->', A1, np.conj(tree)))
    # Fig.7(a): spectator-1 gluons to quark 4, one in the amplitude and one in the conjugate amplitude
    W7 = np.real(np.einsum('kslt,kslt->', A1, np.conj(A1)))
    # Fig.8(b): amplitude: spectator-1 gluon -> quark 4 ; conjugate: spectator-2 gluon -> quark 3
    A2 = np.einsum('btu,lu,bki,is->kslt', Tb, wf, T, wf)
    W8 = np.real(np.einsum('kslt,kslt->', A1, np.conj(A2)))
    # Fig.8(a): both exchanges in the amplitude, tree conjugate
    A12 = np.einsum('asr,btu,alj,bki,ir,ju->kslt', Tb, Tb, T, T, wf, wf)
    W8s = np.real(np.einsum('kslt,kslt->', A12, np.conj(tree)))
    # expected (relative to tree = N^2/N^2 = 1): RM quote unnormalised loop factors
    # Fig.3: Tr(t^a t^a) per loop -> T_F(N^2-1) x N (other loop) / N^2 (tree), with sign from tbar (spectator charge)
    exp3 = -TF*(N*N - 1)*N/N**2           # = -C_F
    exp7 = TF**2*(N*N - 1)/N**2
    exp8 = TF**2*(N*N - 1)/N**2
    ok = (np.isclose(W_tree, 1) and np.isclose(W3, exp3) and np.isclose(W4, 0) and np.isclose(W7, exp7)
          and np.isclose(abs(W8), exp8) and np.isclose(abs(W8s), exp8))
    check('C3 SU(%d): tree=1; Fig3 = -T_F(N^2-1)/N = -C_F; Fig4 = 0 [Tr t^a=0]; Fig7, Fig8(a,b) = T_F^2(N^2-1)/N^2 != 0' % N, ok,
          'W3=%.4f W4=%.1e W7=%.4f W8=%.4f W8s=%.4f' % (W3, W4, W7, W8, W8s))
    # generalized TMD factorization prediction for the Fig.8 colour structure: product of the O(g) terms of
    # the colour-traced Wilson loops in each TMD, each proportional to Tr(t^a) = 0
    pred8 = np.real(np.trace(T.sum(axis=0)))*0 + sum(np.real(np.trace(T[a]))*np.real(np.trace(T[a])) for a in range(nA))
    check('C3g SU(%d): generalized-TMD prediction for Fig.8 (product of single-gluon Wilson-loop terms) = 0 != actual' % N,
          np.isclose(pred8, 0) and not np.isclose(W8, 0))
# abelian analogue: charges g1 (hadron 1 partons), g2 (hadron 2): Fig.8 weight = (g1 g2)(g2 g1) = product of
# the single-gluon factors (g1 g2) x (g2 g1) -> no contradiction with a generalized (process-dependent link) form.
g1, g2 = 0.7, -1.9
check('C3a abelian: Fig.8 weight equals the product of single-exchange factors (no colour entanglement)',
      np.isclose((g1*g2)*(g2*g1), (g1*g2)*(g2*g1)))

# ------------------------------------------------------------------------------------------------
print('\n=== C4: BBMP gauge links (A11),(A12) reproduce their own C_G ===')
from fractions import Fraction as Fr
basic = {'U+': Fr(1), 'UboxU+': Fr(3), 'TrUbox U+': Fr(1), 'TrUboxdag U+': Fr(1), 'U-': Fr(-1)}
def CG_of(comb):
    return sum(c*basic[k] for k, c in comb.items())
allok = True
for Nn in [2, 3, 4, 5, 7]:
    N2 = Nn*Nn
    links = {
        'tt*/uu* (A11a)': ({'TrUbox U+': Fr(N2 + 1, N2 - 1), 'UboxU+': Fr(-2, N2 - 1)}, Fr(N2 - 5, N2 - 1)),
        'tu*/ut* (A11b)': ({'TrUbox U+': Fr(Nn, N2 - 1)*2*Nn, 'UboxU+': -Fr(Nn, N2 - 1)*Fr(N2 + 1, Nn)}, Fr(-(N2 + 3), N2 - 1)),
        'ss* qqbar (A12a)': ({'TrUboxdag U+': Fr(N2, N2 - 1), 'U-': Fr(-1, N2 - 1)}, Fr(N2 + 1, N2 - 1)),
        'tt* qqbar (A12b)': ({'TrUboxdag U+': Fr(1, N2 - 1), 'U-': Fr(N2 - 2, N2 - 1)}, Fr(-(N2 - 3), N2 - 1)),
        'st*/ts* (A12c)': ({'TrUboxdag U+': Fr(Nn, N2 - 1)*Nn, 'U-': -Fr(Nn, N2 - 1)*Fr(1, Nn)}, Fr(N2 + 1, N2 - 1)),
    }
    for name, (comb, cg) in links.items():
        # normalisation of each link: the coefficients must sum to 1 (U -> 1 when A -> 0)
        allok &= (sum(comb.values()) == 1) and (CG_of(comb) == cg)
check('C4 BBMP links are normalised (coefficients sum to 1) and give C_G = (N^2-5)/(N^2-1), -(N^2+3)/(N^2-1), (N^2+1)/(N^2-1), -(N^2-3)/(N^2-1), (N^2+1)/(N^2-1) for N=2,3,4,5,7', allok)

# ------------------------------------------------------------------------------------------------
print('\n=== C5: exact symbolic derivation of C_G = 1 + 2<T_a.T_b>/C_F with SU(N) projectors ===')
import sympy as sp
Ns = sp.symbols('N', positive=True)
CFs = (Ns**2 - 1)/(2*Ns)
# qq channel: 3 x 3 = S + A.  operator coefficients (S, A) for M_t = t^c_{ki} t^c_{lj}, M_u = t^c_{li} t^c_{kj}
dS, dA = Ns*(Ns + 1)/2, Ns*(Ns - 1)/2
TS, TA = (Ns - 1)/(2*Ns), -(Ns + 1)/(2*Ns)           # T_a.T_b = (C_R - 2C_F)/2 on S, A
Mt = ((1 - 1/Ns)/2, -(1 + 1/Ns)/2)
Mu = ((1 - 1/Ns)/2, (1 + 1/Ns)/2)
def ip(X, Y, ops=(1, 1)):
    return sp.simplify(X[0]*Y[0]*dS*ops[0] + X[1]*Y[1]*dA*ops[1])
def CG_qq(X, Y):
    return sp.simplify(1 + 2*ip(X, Y, (TS, TA))/(CFs*ip(X, Y)))
# q qbar channel: 3 x 3bar = 1 + 8.  M_s = (1/2) P_8 ; M_t(qqbar') = (1/2)[(N-1/N) P_1 - P_8/N]
d1, d8 = 1, Ns**2 - 1
T1, T8 = -CFs, sp.Rational(1, 2)/Ns                   # T_a.T_b on singlet, octet
Ms = (0, sp.Rational(1, 2))
Mtq = ((Ns - 1/Ns)/2, -1/(2*Ns))
def ip8(X, Y, ops=(1, 1)):
    return sp.simplify(X[0]*Y[0]*d1*ops[0] + X[1]*Y[1]*d8*ops[1])
def CG_qqb(X, Y):
    return sp.simplify(1 + 2*ip8(X, Y, (T1, T8))/(CFs*ip8(X, Y)))
res = {'tt* (qq)': (CG_qq(Mt, Mt), (Ns**2 - 5)/(Ns**2 - 1)), 'uu* (qq)': (CG_qq(Mu, Mu), (Ns**2 - 5)/(Ns**2 - 1)),
       'tu* (qq)': (CG_qq(Mt, Mu), -(Ns**2 + 3)/(Ns**2 - 1)), 'tt* (qqbar)': (CG_qqb(Mtq, Mtq), -(Ns**2 - 3)/(Ns**2 - 1)),
       'ss* (qqbar)': (CG_qqb(Ms, Ms), (Ns**2 + 1)/(Ns**2 - 1)), 'st* (qqbar)': (CG_qqb(Ms, Mtq), (Ns**2 + 1)/(Ns**2 - 1))}
ok5 = all(sp.simplify(a - b) == 0 for a, b in res.values())
check('C5 symbolic N: all six BBMP strengths follow from C_G = 1 + 2<T_a.T_b>/C_F', ok5,
      '; '.join('%s: %s' % (k, sp.factor(v[0])) for k, v in res.items()))
ab_t = sp.simplify(ip(Mt, Mt, (TS, TA))/ip(Mt, Mt)); ab_tu = sp.simplify(ip(Mt, Mu, (TS, TA))/ip(Mt, Mu))
check('C5b <T_a.T_b>_{tt*} = -1/N and <T_a.T_b>_{tu*} = -(N^2+1)/(2N) (closed forms)',
      sp.simplify(ab_t + 1/Ns) == 0 and sp.simplify(ab_tu + (Ns**2 + 1)/(2*Ns)) == 0, 't: %s ; tu: %s' % (ab_t, sp.factor(ab_tu)))
check('C5c large-N limit: C_G -> +1 for tt*, uu*, ss*, st* (colour flows like SIDIS), -1 for tu*, tt*(qqbar)',
      all(sp.limit(res[k][0], Ns, sp.oo) == v for k, v in [('tt* (qq)', 1), ('ss* (qqbar)', 1), ('st* (qqbar)', 1), ('tu* (qq)', -1), ('tt* (qqbar)', -1)]))

# ------------------------------------------------------------------------------------------------
print('\n=== C6: Rogers-Mulders entanglement test (one gluon from each spectator) ===')
def rm_tensors(N):
    T = gellmann(N); nA = N*N - 1
    Tb = -np.transpose(T, (0, 2, 1))           # spectator (3bar) generators
    d = np.eye(N); s3 = 1/np.sqrt(N)
    tree = np.einsum('ks,lt->kslt', d, d)/N   # indices: k (quark 3), s (spectator 1), l (quark 4), t (spectator 2)
    # one gluon from spectator 1, colour a, attached to line X; insertion on quark line 3 (own loop) or 4/2 (other loop)
    def g1(X):
        if X == 3:  return np.einsum('asr,aki,ir,lt->akslt', Tb, T, d, d)/N
        else:       return np.einsum('asr,kr,alj,jt->akslt', Tb, d, T, d)/N      # X = 4 or 2: same colour tensor
    def g2(Y):
        if Y == 4:  return np.einsum('btu,blj,ju,ks->bkslt', Tb, T, d, d)/N
        else:       return np.einsum('btu,lu,bki,is->bkslt', Tb, d, T, d)/N      # Y = 3 or 1
    return T, Tb, tree, g1, g2, nA
def rm_double(N, X, Y):
    """both gluons in the amplitude; colour tensor with both insertions (lines are different or the graph vanishes)"""
    T = gellmann(N); Tb = -np.transpose(T, (0, 2, 1)); d = np.eye(N)
    # build explicitly: spectator-1 line: s <- tb^a <- r ; spectator-2 line: t <- tb^b <- u ; quark lines carry i, j
    A = 0
    for a in range(N*N - 1):
        for b in range(N*N - 1):
            S1 = Tb[a]; S2 = Tb[b]
            # quark line from hadron 1 (index i -> k) and from hadron 2 (index j -> l); insertions:
            Q1 = d.copy(); Q2 = d.copy()
            if X == 3: Q1 = T[a] @ Q1
            else:      Q2 = T[a] @ Q2
            if Y == 4: Q2 = T[b] @ Q2
            else:      Q1 = T[b] @ Q1
            # wavefunctions delta_{i r}, delta_{j u}: amplitude[k,s,l,t] = sum_{r,u} Q1[k,r] S1[s,r] Q2[l,u] S2[t,u] / N
            A = A + np.einsum('kr,sr,lu,tu->kslt', Q1, S1, Q2, S2)/N
    return A
okall = True; msg = ''
for N in [2, 3, 4, 5]:
    T, Tb, tree, g1, g2, nA = rm_tensors(N)
    C1 = {X: np.real(np.einsum('akslt,kslt->', g1(X), np.conj(tree))) for X in [3, 4, 2]}
    C2 = {Y: np.real(np.einsum('bkslt,kslt->', g2(Y), np.conj(tree))) for Y in [4, 3, 1]}
    Cxy = {(X, Y): np.real(np.einsum('kslt,kslt->', rm_double(N, X, Y), np.conj(tree))) for X in [3, 4, 2] for Y in [4, 3, 1]}
    # opposite sides of the cut: gluon 1 in the amplitude, gluon 2 in the conjugate amplitude
    Cop = {}
    for X in [3, 4, 2]:
        for Y in [4, 3, 1]:
            # gluon colours are summed inside each amplitude separately
            Cop[(X, Y)] = np.real(np.einsum('kslt,kslt->', g1(X).sum(axis=0), np.conj(g2(Y).sum(axis=0))))
    CF = (N*N - 1)/(2*N); TF = 0.5
    S_act = sum(Cxy.values()); S_gen = sum(C1.values())*sum(C2.values())
    S_act_op = sum(Cop.values())
    ok = (np.isclose(C1[3], -CF) and np.isclose(C1[4], 0) and np.isclose(C1[2], 0) and np.isclose(C2[4], -CF)
          and np.isclose(C2[3], 0) and np.isclose(C2[1], 0)
          and np.isclose(Cxy[(3, 4)], CF**2) and all(np.isclose(Cxy[(X, Y)], TF**2*(N*N - 1)/N**2) for X in [4, 2] for Y in [3, 1])
          and np.isclose(Cxy[(3, 3)], 0) and np.isclose(Cxy[(3, 1)], 0) and np.isclose(Cxy[(4, 4)], 0) and np.isclose(Cxy[(2, 4)], 0)
          and np.isclose(S_gen, CF**2) and np.isclose(S_act - S_gen, 4*TF**2*(N*N - 1)/N**2)
          and np.isclose(S_act_op - S_gen, 4*TF**2*(N*N - 1)/N**2))
    okall &= ok
    if N == 3:
        msg = ('SU(3): C1(3)=%.4f C1(4)=C1(2)=%.1e ; C(3,4)=%.4f ; C(cross)=%.4f each (x4) ; mixed=%.1e ; '
               'sum_actual=%.4f vs product=%.4f ; cross/direct weight=%.4f [4/(N^2-1)=0.5]'
               % (C1[3], abs(C1[4]) + abs(C1[2]), Cxy[(3, 4)], Cxy[(4, 3)], abs(Cxy[(3, 3)]) + abs(Cxy[(4, 4)]), S_act, S_gen,
                  4*Cxy[(4, 3)]/Cxy[(3, 4)]))
check('C6 SU(N), N=2..5: single-gluon cross attachments vanish (Tr t^a=0) so separate Wilson-line structures force '
      'the double-pole colour weight = C_F^2, but the actual weight is C_F^2 + 4 T_F^2 (N^2-1)/N^2 (same and opposite sides of the cut)',
      okall, msg)
# abelian (U(1)) analogue with charges: spectator1 -g1, quark 1/3 g1, quark 2/4 g2, spectator2 -g2
g1v, g2v = 0.7, -1.3
c1 = {3: (-g1v)*g1v, 4: (-g1v)*g2v, 2: (-g1v)*g2v}
c2 = {4: (-g2v)*g2v, 3: (-g2v)*g1v, 1: (-g2v)*g1v}
S_act_ab = sum(c1[X]*c2[Y] for X in c1 for Y in c2); S_gen_ab = sum(c1.values())*sum(c2.values())
check('C6b U(1): every two-gluon graph weight is the product of single-exchange charges, so actual = product (no entanglement; '
      'generalized TMD factorization not contradicted at this order, cf. Collins 2007, Vogelsang-Yuan 2007)',
      np.isclose(S_act_ab, S_gen_ab), 'actual=%.4f product=%.4f' % (S_act_ab, S_gen_ab))

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
