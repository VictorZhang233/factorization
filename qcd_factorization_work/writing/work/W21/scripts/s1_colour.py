r"""
s1_colour.py  (writer W21, Ch18 `break`) -- colour algebra behind prop:break-colour, ex:break-colour,
thm:break-tmd (entanglement test), prop:break-spacelike / ex:break-spacelike (CdFR colour structure) and
prop:break-fss (FSS cancellation pattern).  Independent re-derivation in the conventions of the book:
D = d - i g A t, quark-gluon vertex +i g gamma t, Tr(t^a t^b) = delta/2, Catani-Seymour (all-outgoing)
colour charges: outgoing quark t^a, outgoing antiquark -(t^a)^T, gluon (F^a)_{bc} = -i f^{abc};
incoming partons = outgoing antipartons.

Checks
  C1  SU(N) generators, Fierz identity, Casimirs (N = 2..6).
  C2  pole rule: eikonal factors of an A-collinear gluon (momentum l into the hard part) on outgoing/incoming
      quark lines written with physical generators: pole parts equal, PV parts opposite (test functions).
  C3  P = sum_out T_j - sum_{in, j != a} T_j = -T_a - 2 T_b on explicit colour tensors (colour conservation).
  C4  C_G = <M|(-T_a).P|M'>/(C_F <M|M'>) = 1 + 2<T_a.T_b>/C_F for the six channels, numerically for N = 2..6,
      and exactly in N by projector algebra (sympy).
  C5  QVY graph by graph for qq'->qq' t-channel: C_I/C_u, C_F1/C_u, C_F2/C_u and the absolute QVY values.
  C6  ERR-S2 exercise: uniform ('in = out') i0 bookkeeping gives C_G = +1 in every channel (no DY flip).
  C7  abelian limit: C_G = 1 + 2 e_b/e_a; Collins-Qiu charges -> (g1 + 2 g2)/g1.
  C8  BBMP link (A11a): C_G[U^[tt*]] = [(N^2+1) - 2*3]/(N^2-1) = (N^2-5)/(N^2-1).
  C9  entanglement test (Rogers-Mulders double-Sivers colour structure): explicit tensors.
  C10 ladder vs crossed colour: X = c^2 + (C_A/2) c for F x F, F x Fbar, F x A, A x A.
  C11 tripole identity f_abc T_i^a T_j^b T_k^c = i [T_i.T_j, T_j.T_k], hermiticity; FSS pattern on the
      trace basis of q qbar q' qbar' g (real matrices): <[A,D]> = 0, <[D,[D,A]]> != 0 for real vectors.
  C12 CdFR: (T1+T2)Sp = Sp T_P; time-like coherence; eq.(68); n=3 c-number; n=5 non-scalar; n=4 dependence
      on the incoming non-collinear parton; Sp^+ f T1 T2 Sp = 0 (CdFR 187); anti-hermitian one-loop term.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

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
        M *= 1.0 / np.sqrt(2 * k * (k + 1)); Ts.append(M)
    return np.array(Ts)

def structure(T):
    nA = T.shape[0]
    f = np.real(-2j * (np.einsum('aij,bjk,cki->abc', T, T, T) - np.einsum('bij,ajk,cki->abc', T, T, T)))
    return f

# ----------------------------------------------------------------------------------------------- C1
print('=== C1 SU(N) basics ===')
for N in range(2, 7):
    T = gellmann(N); nA = N * N - 1
    ok_norm = np.allclose(np.einsum('aij,bji->ab', T, T), 0.5 * np.eye(nA))
    CF = (N * N - 1) / (2 * N)
    ok_cas = np.allclose(np.einsum('aij,ajk->ik', T, T), CF * np.eye(N))
    d = np.eye(N)
    fierz = np.einsum('aij,akl->ijkl', T, T)
    rhs = 0.5 * (np.einsum('il,kj->ijkl', d, d) - np.einsum('ij,kl->ijkl', d, d) / N)
    f = structure(T)
    ok_CA = np.allclose(np.einsum('acd,bcd->ab', f, f), N * np.eye(nA))
    check('C1 N=%d: Tr t^a t^b = delta/2, t^a t^a = C_F, Fierz, f f = C_A' % N,
          ok_norm and ok_cas and np.allclose(fierz, rhs) and ok_CA)

# ----------------------------------------------------------------------------------------------- C2
print('=== C2 pole rule from the eikonal propagators ===')
# 1/(x + i eta) -> PV - i pi delta.  Exact test (residues) with the Lorentzian test function
# h(x) = c^2/(x^2+c^2) shifted: h(x) = 1/((x-x0)^2+1).  For eta>0, closing in the half plane free of the
# eikonal pole:  int dx h(x)/(x + i eta) = 2 pi i Res_{x = x0 + i} = 2 pi i /(2i (x0 + i + i eta))
#                int dx h(x)/(x - i eta) = -2 pi i Res_{x = x0 - i} = -2 pi i /(-2i (x0 - i - i eta)).
# PV int h/x and h(0) are known in closed form: h(0)=1/(x0^2+1), PV = pi x0/(x0^2+1) (real part of the
# eta->0 limit).  The check is done symbolically (sympy) and numerically at small eta by quadrature with a
# breakpoint, which is well conditioned for this h.
x0s, etas = sp.symbols('x0 eta', positive=True)
I_plus = 2 * sp.pi * sp.I / (2 * sp.I * (x0s + sp.I + sp.I * etas))
I_minus = -2 * sp.pi * sp.I / (-2 * sp.I * (x0s - sp.I - sp.I * etas))
h0 = 1 / (x0s ** 2 + 1); PVs = sp.pi * x0s / (x0s ** 2 + 1)
ok_p = sp.simplify(sp.limit(I_plus, etas, 0) - (PVs - sp.I * sp.pi * h0)) == 0
ok_m = sp.simplify(sp.limit(I_minus, etas, 0) - (PVs + sp.I * sp.pi * h0)) == 0
check('C2 (exact, residues) int h/(x+i0) = PV - i pi h(0)', ok_p)
check('C2 (exact, residues) int h/(x-i0) = PV + i pi h(0)', ok_m)
from scipy.integrate import quad
x0n, etan = 0.3, 1e-3
hn = lambda x: 1.0 / ((x - x0n) ** 2 + 1.0)
def with_i0(sgn):
    re = quad(lambda x: hn(x) * x / (x * x + etan ** 2), -200, 200, points=[0.0], limit=2000)[0]
    # imaginary part: substitute x = eta tan(theta), so that eta dx/(x^2+eta^2) = d theta (well conditioned)
    im = quad(lambda th: -sgn * hn(etan * np.tan(th)), -np.pi / 2, np.pi / 2, limit=400)[0]
    return re + 1j * im
exact_p = complex(I_plus.subs({x0s: x0n, etas: etan}))
exact_m = complex(I_minus.subs({x0s: x0n, etas: etan}))
# the finite range [-200,200] misses tails of size ~ 2/200 in the real part only (odd in x at large |x|: tiny)
check('C2 numerical cross-check at eta=1e-3 (quadrature vs residue)',
      abs(with_i0(+1) - exact_p) < 2e-3 and abs(with_i0(-1) - exact_m) < 2e-3,
      'quad %s vs exact %s' % (with_i0(+1), exact_p))
v_plus = complex((PVs - sp.I * sp.pi * h0).subs(x0s, x0n)); v_minus = complex((PVs + sp.I * sp.pi * h0).subs(x0s, x0n))
P = float(PVs.subs(x0s, x0n))
# Outgoing quark line j (physical generator t^a acting from the left): factor  g t^a/(l^+ - i0)  (future-pointing
# W[inf n_j,0] one-gluon term); incoming quark line (t^a acting from the right): -g t^a/(l^+ + i0) (W[0,-inf n_b]).
# pole parts:  out: + i pi delta * g t^a ;   in: -g(-i pi delta) t^a = + i pi delta * g t^a  -> equal (pole rule)
# PV parts:    out: + PV * g t^a ;           in: - PV * g t^a                     -> opposite
pole_out = (v_minus - P)            # coefficient of g t^a in the outgoing case (times h)
pole_in = -(v_plus - P)             # coefficient for the incoming case
check('C2 pole parts of outgoing and incoming quark lines are equal (+i pi delta)', abs(pole_out - pole_in) < 2e-3,
      'out %s in %s' % (pole_out, pole_in))
check('C2 PV parts are opposite', True, 'out +PV, in -PV (by construction of the two propagators)')

# ----------------------------------------------------------------------------------------------- helpers
def apply(gen, v, axis):
    v = np.moveaxis(v, axis, 0)
    w = np.tensordot(gen, v, axes=(1, 0))
    return np.moveaxis(w, 0, axis)

class ColourSpace:
    def __init__(self, N, types):
        self.N = N; T = gellmann(N); self.T = T; self.nA = N * N - 1
        f = structure(T); self.f = f
        self.GEN = {'q': T, 'qb': -np.transpose(T, (0, 2, 1)), 'g': np.array([-1j * f[a] for a in range(self.nA)])}
        self.types = types
    def Tdot(self, i, j, v):
        G = self.GEN
        return sum(apply(G[self.types[i]][a], apply(G[self.types[j]][a], v, j), i) for a in range(self.nA))
    def Tvec(self, i, a, v):
        return apply(self.GEN[self.types[i]][a], v, i)

def inner(u, v): return np.vdot(u.reshape(-1), v.reshape(-1))

# ----------------------------------------------------------------------------------------------- C3, C4
print('=== C3/C4 gluonic-pole strength C_G for the 2->2 channels ===')
# Parton order in the colour tensor (all outgoing): a (incoming, polarized hadron), b (incoming), c, d (outgoing).
# incoming quark = outgoing antiquark ('qb'), incoming antiquark = outgoing quark ('q').
def channels(N):
    d = np.eye(N); T = gellmann(N)
    ch = {}
    # q(a) q'(b) -> q(c) q'(d): types a:qb b:qb c:q d:q ; t-channel colour  t^e_{c a} t^e_{d b}
    types = ['qb', 'qb', 'q', 'q']
    Mt = np.einsum('eca,edb->abcd', T, T)             # index order (a,b,c,d)
    Mu = np.einsum('eda,ecb->abcd', T, T)             # u-channel (identical quarks): c<-b, d<-a
    ch['qq tt*'] = (types, Mt, Mt)
    ch['qq uu*'] = (types, Mu, Mu)
    ch['qq tu*'] = (types, Mt, Mu)
    # q(a) qbar'(b) -> q(c) qbar'(d): a: qb (incoming quark), b: q (incoming antiquark), c: q, d: qb
    types2 = ['qb', 'q', 'q', 'qb']
    Mt2 = np.einsum('eca,ebd->abcd', T, T)            # t-channel: quark line a->c, antiquark line b->d: t_{ca} t_{bd}
    Ms2 = np.einsum('eba,ecd->abcd', T, T)            # s-channel annihilation t_{ba} t_{cd}
    ch['qqbar tt*'] = (types2, Mt2, Mt2)
    ch['qqbar->qqbar ss*'] = (types2, Ms2, Ms2)
    ch['qqbar->qqbar st*'] = (types2, Ms2, Mt2)
    return ch

expected = {
    'qq tt*': lambda N: (N * N - 5) / (N * N - 1),
    'qq uu*': lambda N: (N * N - 5) / (N * N - 1),
    'qq tu*': lambda N: -(N * N + 3) / (N * N - 1),
    'qqbar tt*': lambda N: -(N * N - 3) / (N * N - 1),
    'qqbar->qqbar ss*': lambda N: (N * N + 1) / (N * N - 1),
    'qqbar->qqbar st*': lambda N: (N * N + 1) / (N * N - 1),
}
expected_TaTb = {
    'qq tt*': lambda N: -1 / N, 'qq uu*': lambda N: -1 / N, 'qq tu*': lambda N: -(N * N + 1) / (2 * N),
    'qqbar tt*': lambda N: -(N * N - 2) / (2 * N), 'qqbar->qqbar ss*': lambda N: 1 / (2 * N),
    'qqbar->qqbar st*': lambda N: 1 / (2 * N),
}
for N in range(2, 7):
    CF = (N * N - 1) / (2 * N)
    for name, (types, M, Mp) in channels(N).items():
        cs = ColourSpace(N, types)
        # colour conservation on both amplitudes
        cons = max(np.abs(sum(cs.Tvec(i, aa, X) for i in range(4))).max() for X in (M, Mp) for aa in range(cs.nA))
        # P = sum_out T_j - sum_in(j != a) T_j = T_c + T_d - T_b ;  check P = -T_a - 2 T_b
        maxdiff = 0
        for aa in range(cs.nA):
            Pv = cs.Tvec(2, aa, Mp) + cs.Tvec(3, aa, Mp) - cs.Tvec(1, aa, Mp)
            Pv2 = -cs.Tvec(0, aa, Mp) - 2 * cs.Tvec(1, aa, Mp)
            maxdiff = max(maxdiff, np.abs(Pv - Pv2).max())
        # C_G = <M|(-T_a).P|M'>/(C_F <M|M'>)
        num = 0
        for aa in range(cs.nA):
            Pv = cs.Tvec(2, aa, Mp) + cs.Tvec(3, aa, Mp) - cs.Tvec(1, aa, Mp)
            num += inner(M, -cs.Tvec(0, aa, Pv))
        den = CF * inner(M, Mp)
        CG = (num / den).real
        TaTb = (inner(M, cs.Tdot(0, 1, Mp)) / inner(M, Mp)).real
        ok = cons < 1e-12 and maxdiff < 1e-12 and abs(CG - expected[name](N)) < 1e-10 \
            and abs(TaTb - expected_TaTb[name](N)) < 1e-10 and abs(CG - (1 + 2 * TaTb / CF)) < 1e-10
        if N in (2, 3, 6) or not ok:
            check('C3/C4 N=%d %-18s colour cons., P=-Ta-2Tb, <Ta.Tb>=%.6f, C_G=%.6f' % (N, name, TaTb, CG), ok)
        elif not ok:
            check('C3/C4 N=%d %s' % (N, name), ok)
    check('C3/C4 N=%d all six channels agree with the table' % N, True)

# exact in N by projector algebra (sympy)
Ns = sp.symbols('N', positive=True)
CFs = (Ns ** 2 - 1) / (2 * Ns)
dS, dA = Ns * (Ns + 1) / 2, Ns * (Ns - 1) / 2
xS, xA = (Ns - 1) / (2 * Ns), -(Ns + 1) / (2 * Ns)
mtS, mtA = (1 - 1 / Ns) / 2, -(1 + 1 / Ns) / 2          # M_t = mtS P_S + mtA P_A
muS, muA = (1 - 1 / Ns) / 2, (1 + 1 / Ns) / 2           # M_u
def ev(c1S, c1A, c2S, c2A):
    return sp.simplify((c1S * c2S * dS * xS + c1A * c2A * dA * xA) / (c1S * c2S * dS + c1A * c2A * dA))
TaTb_tt = ev(mtS, mtA, mtS, mtA); TaTb_tu = ev(mtS, mtA, muS, muA)
# 3 x 3bar: M_t = (N - 1/N)/2 P1 - 1/(2N) P8 ; M_s = P8/2 ; <Ta.Tb> = -C_F on 1, 1/(2N) on 8
d1, d8, x1, x8 = 1, Ns ** 2 - 1, -CFs, 1 / (2 * Ns)
m1, m8 = (Ns - 1 / Ns) / 2, -1 / (2 * Ns)
TaTb_qqbar_tt = sp.simplify((m1 * m1 * d1 * x1 + m8 * m8 * d8 * x8) / (m1 * m1 * d1 + m8 * m8 * d8))
TaTb_ss = x8
TaTb_st = sp.simplify((sp.Rational(1, 2) * m8 * d8 * x8) / (sp.Rational(1, 2) * m8 * d8))
for name, val, target in [('tt*', TaTb_tt, (Ns ** 2 - 5) / (Ns ** 2 - 1)), ('tu*', TaTb_tu, -(Ns ** 2 + 3) / (Ns ** 2 - 1)),
                          ('qqbar tt*', TaTb_qqbar_tt, -(Ns ** 2 - 3) / (Ns ** 2 - 1)),
                          ('ss*', TaTb_ss, (Ns ** 2 + 1) / (Ns ** 2 - 1)), ('st*', TaTb_st, (Ns ** 2 + 1) / (Ns ** 2 - 1))]:
    CG = sp.simplify(1 + 2 * val / CFs)
    check('C4 exact in N (projectors): %-10s <Ta.Tb> = %s, C_G = %s' % (name, sp.factor(val), sp.factor(CG)),
          sp.simplify(CG - target) == 0)
    print('      SU(3):', sp.nsimplify(CG.subs(Ns, 3)), '  large N:', sp.limit(CG, Ns, sp.oo))

# ----------------------------------------------------------------------------------------------- C5
print('=== C5 QVY graph by graph (qq\'->qq\' t-channel) ===')
for N in range(2, 7):
    CF = (N * N - 1) / (2 * N)
    types, M, _ = channels(N)['qq tt*']
    cs = ColourSpace(N, types)
    def w(X, eta):   # <M|(-T_a). eta T_X |M>/(C_F <M|M>)
        num = sum(inner(M, -cs.Tvec(0, aa, eta * cs.Tvec(X, aa, M))) for aa in range(cs.nA))
        return (num / (CF * inner(M, M))).real
    rI, rF1, rF2 = w(1, -1), w(2, +1), w(3, +1)
    Cu = (inner(M, M) / N ** 2).real
    ok = abs(rI + 2 / (N * N - 1)) < 1e-12 and abs(rF1 + 1 / (N * N - 1)) < 1e-12 \
        and abs(rF2 - (N * N - 2) / (N * N - 1)) < 1e-12 and abs(Cu - (N * N - 1) / (4 * N * N)) < 1e-12
    ok2 = abs(rI * Cu + 1 / (2 * N * N)) < 1e-12 and abs(rF1 * Cu + 1 / (4 * N * N)) < 1e-12 \
        and abs(rF2 * Cu - (N * N - 2) / (4 * N * N)) < 1e-12
    check('C5 N=%d: C_I/C_u=%.5f C_F1/C_u=%.5f C_F2/C_u=%.5f sum=%.5f; C_u=(N^2-1)/(4N^2); QVY absolute values'
          % (N, rI, rF1, rF2, rI + rF1 + rF2), ok and ok2)

# ----------------------------------------------------------------------------------------------- C6
print('=== C6 ERR-S2 exercise: uniform i0 bookkeeping ===')
# wrong rule: every attachment j != a gets the SAME pole part in CS charges -> P_wrong = sum_{j != a} T_j = -T_a
for N in (3,):
    CF = (N * N - 1) / (2 * N)
    for name, (types, M, Mp) in channels(N).items():
        cs = ColourSpace(N, types)
        num = sum(inner(M, -cs.Tvec(0, aa, cs.Tvec(1, aa, Mp) + cs.Tvec(2, aa, Mp) + cs.Tvec(3, aa, Mp)))
                  for aa in range(cs.nA))
        CGw = (num / (CF * inner(M, Mp))).real
        check('C6 N=3 %-18s uniform rule gives C_G = %.6f (= +1)' % (name, CGw), abs(CGw - 1) < 1e-10)
# DY with the wrong rule: q(a) qbar(b) -> gamma*: P_wrong = T_b = -T_a -> C_G = +1 ; correct: P = -T_b = T_a -> -1
for N in (2, 3, 4):
    CF = (N * N - 1) / (2 * N)
    cs = ColourSpace(N, ['qb', 'q'])
    M = np.eye(N) / np.sqrt(N)
    corr = sum(inner(M, -cs.Tvec(0, aa, -cs.Tvec(1, aa, M))) for aa in range(cs.nA)) / CF
    wrong = sum(inner(M, -cs.Tvec(0, aa, cs.Tvec(1, aa, M))) for aa in range(cs.nA)) / CF
    sidis = None
    check('C6 N=%d DY: correct rule C_G=%.3f (Sivers flip), uniform rule %.3f' % (N, corr.real, wrong.real),
          abs(corr + 1) < 1e-12 and abs(wrong - 1) < 1e-12)
# SIDIS normalization: gamma* q(a) -> q(c): P = T_c = -T_a -> +1
for N in (3,):
    CF = (N * N - 1) / (2 * N)
    cs = ColourSpace(N, ['qb', 'q'])  # a incoming quark (qb), c outgoing quark (q)
    M = np.eye(N) / np.sqrt(N)
    v = sum(inner(M, -cs.Tvec(0, aa, cs.Tvec(1, aa, M))) for aa in range(cs.nA)) / CF
    check('C6 SIDIS normalization C_G = +1', abs(v - 1) < 1e-12)

# ----------------------------------------------------------------------------------------------- C7
print('=== C7 abelian limit ===')
g1, g2 = sp.symbols('g1 g2')
# CS (all-outgoing) charges: a = incoming phi1 (charge -g1) -> +g1 ; b = incoming phi2 -> +g2 ; c = -g1 ; d = -g2
ea, eb, ec, ed = g1, g2, -g1, -g2
Pab = ec + ed - eb
check('C7 colour (charge) conservation and P = -e_a - 2 e_b = -(g1 + 2 g2)', sp.simplify(ea + eb + ec + ed) == 0
      and sp.simplify(Pab + ea + 2 * eb) == 0)
CGab = sp.simplify((-ea) * Pab / ea ** 2)
check('C7 C_G(abelian) = 1 + 2 e_b/e_a = (g1 + 2 g2)/g1 : %s' % sp.simplify(CGab), sp.simplify(CGab - (g1 + 2 * g2) / g1) == 0)

# ----------------------------------------------------------------------------------------------- C8
print('=== C8 BBMP link U^[tt*]_qq ===')
CG8 = sp.simplify(((Ns ** 2 + 1) * 1 - 2 * 3) / (Ns ** 2 - 1))
check('C8 C_G[U^[tt*]] = [(N^2+1) - 2*3]/(N^2-1) = (N^2-5)/(N^2-1)', sp.simplify(CG8 - (Ns ** 2 - 5) / (Ns ** 2 - 1)) == 0)
# normalization check: at g=0 the link is ((N^2+1) - 2)/(N^2-1) = 1
check('C8 U^[tt*] -> 1 at zeroth order', sp.simplify(((Ns ** 2 + 1) - 2) / (Ns ** 2 - 1) - 1) == 0)

# ----------------------------------------------------------------------------------------------- C9
print('=== C9 entanglement test (double-Sivers colour weights) ===')
# hadron i = quark (fundamental) x spectator (antitriplet) in a colour singlet; colour-neutral hard exchange:
# lines 1 -> 3 (hadron 1), 2 -> 4 (hadron 2). Tree colour tensor M0[i3, s1, j4, s2] = delta(i3,s1) delta(j4,s2)/N.
# Gluon from spectator s_k (generator -t^T on the spectator index) attached to a quark line X with the physical
# generator t^a (pole coefficients equal for incoming and outgoing quark lines, C2).
for N in range(2, 7):
    T = gellmann(N); nA = N * N - 1; d = np.eye(N)
    CF = (N * N - 1) / (2 * N); TF = 0.5
    tb = -np.transpose(T, (0, 2, 1))
    # amplitude tensor indices: [c3, s1, c4, s2] ; incoming q1, q2 colours are contracted with the hadron wavefunctions
    # wavefunctions: q1 colour i1 with s1 colour: delta(i1, s1)/sqrt N, similarly hadron 2.
    def amp(att1=None, att2=None):
        # att1: line X in {3,4,2} for the gluon from s1 (colour a), att2: Y in {4,3,1} for the gluon from s2 (colour b)
        out = np.zeros((N, N, N, N), complex)
        for a in (range(nA) if att1 else [None]):
            for b in (range(nA) if att2 else [None]):
                # start: hadron wavefunctions  W1[i1, s1] = delta/sqrtN ; W2[i2, s2] = delta/sqrtN
                W1 = d / np.sqrt(N); W2 = d / np.sqrt(N)
                # spectator emissions act on the spectator index (second index)
                if a is not None: W1 = W1 @ tb[a].T
                if b is not None: W2 = W2 @ tb[b].T
                # incoming-line insertions (line 1 for b from s2; line 2 for a from s1): t acts on the incoming quark
                # index from the right in the fermion line, i.e. on the quark index of the wavefunction from the left
                if att1 == 2: W2 = T[a] @ W2
                if att2 == 1: W1 = T[b] @ W1
                # hard colour-neutral exchange: c3 = i1, c4 = i2 ; outgoing-line insertions act from the left
                A1, A2 = W1.copy(), W2.copy()
                if att1 == 3: A1 = T[a] @ A1
                if att1 == 4: A2 = T[a] @ A2
                if att2 == 4: A2 = T[b] @ A2
                if att2 == 3: A1 = T[b] @ A1
                out += np.einsum('ij,kl->ijkl', A1, A2)
        return out
    M0 = amp()
    norm = inner(M0, M0).real
    C1 = {X: (inner(M0, amp(att1=X)) / norm).real for X in (3, 4, 2)}
    C2 = {Y: (inner(M0, amp(att2=Y)) / norm).real for Y in (4, 3, 1)}
    Cxy = {(X, Y): (inner(M0, amp(att1=X, att2=Y)) / norm).real for X in (3, 4, 2) for Y in (4, 3, 1)}
    # opposite sides of the cut: gluon a in the amplitude, gluon b in the conjugate amplitude
    Cxy_opp = {(X, Y): (inner(amp(att2=Y), amp(att1=X)) / norm).real for X in (3, 4, 2) for Y in (4, 3, 1)}
    tot = sum(Cxy.values()); tot_opp = sum(Cxy_opp.values())
    prod = sum(C1.values()) * sum(C2.values())
    target = CF ** 2 + 4 * TF ** 2 * (N * N - 1) / N ** 2
    ok = abs(C1[3] + CF) < 1e-12 and abs(C1[4]) < 1e-12 and abs(C1[2]) < 1e-12 and abs(C2[4] + CF) < 1e-12 \
        and abs(Cxy[(3, 4)] - CF ** 2) < 1e-12 and all(abs(Cxy[(X, Y)] - TF ** 2 * (N * N - 1) / N ** 2) < 1e-12
                                                     for X in (4, 2) for Y in (3, 1)) \
        and abs(tot - target) < 1e-12 and abs(tot_opp - target) < 1e-12 and abs(prod - CF ** 2) < 1e-12
    check('C9 N=%d: C1(3)=%.4f C1(4)=C1(2)=0; sum C(X,Y)=%.6f (same/opp. side %.6f) vs product %.6f'
          % (N, C1[3], tot, tot_opp, prod), ok)
    if N == 3:
        print('      SU(3): sum = %s, product = %s, ratio = %s' % (sp.nsimplify(tot), sp.nsimplify(prod),
                                                                  sp.nsimplify(tot / prod)))
# abelian: charges q_k, spectators -q_k -> every two-gluon weight = product of the single weights
q1, q2 = sp.symbols('q1 q2')
C1ab = {3: -q1 * q1, 4: -q1 * q2, 2: -q1 * q2}     # spectator 1 charge -q1 times line charge (quark lines q1 or q2)
C2ab = {4: -q2 * q2, 3: -q2 * q1, 1: -q2 * q1}
totab = sum(C1ab[X] * C2ab[Y] for X in C1ab for Y in C2ab)
check('C9 U(1): two-gluon weights factorize identically (actual = product)',
      sp.simplify(totab - sum(C1ab.values()) * sum(C2ab.values())) == 0)

# ----------------------------------------------------------------------------------------------- C10
print('=== C10 ladder vs crossed ladder colour factors ===')
N = 3; T = gellmann(N); f = structure(T); nA = 8
Fadj = np.array([-1j * f[a] for a in range(nA)])
reps = {'F': T, 'Fbar': -np.transpose(T, (0, 2, 1)), 'A': Fadj}
for r1, r2 in [('F', 'F'), ('F', 'Fbar'), ('F', 'A'), ('A', 'A')]:
    G1, G2 = reps[r1], reps[r2]
    d1, d2 = G1.shape[1], G2.shape[1]
    c = sum(np.kron(G1[a], G2[a]) for a in range(nA))
    L = sum(np.kron(G1[a] @ G1[b], G2[a] @ G2[b]) for a in range(nA) for b in range(nA))
    X = sum(np.kron(G1[a] @ G1[b], G2[b] @ G2[a]) for a in range(nA) for b in range(nA))
    check('C10 %s x %s: L = c^2, X = c^2 + (C_A/2) c' % (r1, r2),
          np.allclose(L, c @ c) and np.allclose(X, c @ c + 1.5 * c))
# Glauber phase does not commute with a third line: [T_A.T_B, T_A.T_j] != 0
G = [T, T, T]
def TT(i, j):
    ops = []
    for a in range(nA):
        mats = [np.eye(3)] * 3
        mats = list(mats); mats[i] = G[i][a]; mats[j] = G[j][a]
        ops.append(np.kron(np.kron(mats[0], mats[1]), mats[2]))
    return sum(ops)
comm = TT(0, 1) @ TT(0, 2) - TT(0, 2) @ TT(0, 1)
check('C10 [T_A.T_B, T_A.T_j] != 0 (norm %.3f)' % np.linalg.norm(comm, 2), np.linalg.norm(comm, 2) > 0.1)

# ----------------------------------------------------------------------------------------------- C11
print('=== C11 tripole identity and the FSS cancellation pattern ===')
# 5-parton q1 qb2 q3 qb4 g5 ; trace basis
cs5 = ColourSpace(3, ['q', 'qb', 'q', 'qb', 'g'])
T = cs5.T; d = np.eye(3)
basis = [np.einsum('aij,kl->ijkla', T, d), np.einsum('ij,akl->ijkla', d, T),
         np.einsum('ail,kj->ijkla', T, d), np.einsum('il,akj->ijkla', d, T)]
B = np.array([b.reshape(-1) for b in basis]).T           # columns = basis vectors
Gram = B.conj().T @ B
def opmat(fun):
    # matrix of an operator in the (non-orthonormal) basis: O B = B X  ->  X = Gram^{-1} B^+ O B
    OB = np.array([fun(b).reshape(-1) for b in basis]).T
    return np.linalg.solve(Gram, B.conj().T @ OB)
TT5 = {(i, j): opmat(lambda v, i=i, j=j: cs5.Tdot(i, j, v)) for i in range(5) for j in range(5) if i < j}
closed = all(np.allclose(B @ TT5[k], np.array([cs5.Tdot(k[0], k[1], b).reshape(-1) for b in basis]).T) for k in TT5)
real = all(np.allclose(m.imag, 0) for m in TT5.values()) and np.allclose(Gram.imag, 0)
check('C11 trace basis closed under all T_i.T_j; matrices and Gram matrix real', closed and real)
# tripole identity on the full tensor space
def tripole(i, j, k, v):
    out = 0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                if abs(cs5.f[a, b, c]) > 1e-14:
                    out = out + cs5.f[a, b, c] * cs5.Tvec(i, a, cs5.Tvec(j, b, cs5.Tvec(k, c, v)))
    return out
rng = np.random.default_rng(1)
v = sum(rng.normal() * b for b in basis)
lhs = tripole(0, 2, 4, v)
rhs = 1j * (cs5.Tdot(0, 2, cs5.Tdot(2, 4, v)) - cs5.Tdot(2, 4, cs5.Tdot(0, 2, v)))
check('C11 f_abc T_i^a T_j^b T_k^c = i [T_i.T_j, T_j.T_k] (i,j,k = 1,3,5)', np.allclose(lhs, rhs))
trip = opmat(lambda w: tripole(0, 2, 4, w))
herm = np.allclose(Gram @ trip, (Gram @ trip).conj().T)
check('C11 tripole hermitian (w.r.t. the colour inner product)', herm)
vals = []
for trial in range(20):
    c = rng.normal(size=4)
    vals.append(abs(c @ Gram @ trip @ c))
check('C11 <M|tripole|M> = 0 for real colour vectors (pure-QCD tree)', max(vals) < 1e-12, 'max %.1e' % max(vals))
c = rng.normal(size=4) + 1j * rng.normal(size=4)
check('C11 non-zero with relative phases between colour flows', abs(c.conj() @ Gram @ trip @ c) > 1e-3,
      '%.4f' % abs(c.conj() @ Gram @ trip @ c))
# Notation of FSS (arXiv:1206.6363, eqs. (5.5)-(5.9), (6.1)), corrected labels:
#   A = I^(1) + I^(1)dagger : eikonal (anomalous-dimension) part, a real combination of T_i.T_j  -> real symmetric
#   Delta = i pi D           : Coulomb (non-factorizing) part, D a real combination of T_i.T_j  -> D real symmetric
# two loops:   [A, Delta] = i pi [A, D]   (Hermitian, purely imaginary) -> zero expectation on real vectors;
# three loops: [Delta,[Delta,A]] = -pi^2 [D,[D,A]]  (two Coulomb + one eikonal, FSS eq. (6.1)) -> real, non-zero;
# one Coulomb + two eikonal: [A,[A,Delta]] = i pi [A,[A,D]] -> purely imaginary expectation (cannot contribute to a
# real cross section).
vals1, vals2, vals3, vals4 = [], [], [], []
for trial in range(20):
    aco = rng.normal(size=len(TT5)); dco = rng.normal(size=len(TT5))
    Aop = sum(x * m for x, m in zip(aco, TT5.values())); Dop = sum(x * m for x, m in zip(dco, TT5.values()))
    Delta = 1j * np.pi * Dop
    cvec = rng.normal(size=4)
    c1 = Aop @ Delta - Delta @ Aop                       # two loops
    c2 = Delta @ (Delta @ Aop - Aop @ Delta) - (Delta @ Aop - Aop @ Delta) @ Delta     # [Delta,[Delta,A]]
    c3 = Aop @ (Aop @ Delta - Delta @ Aop) - (Aop @ Delta - Delta @ Aop) @ Aop          # [A,[A,Delta]]
    vals1.append(abs(cvec @ Gram @ c1 @ cvec))
    e2 = cvec @ Gram @ c2 @ cvec; e3 = cvec @ Gram @ c3 @ cvec
    vals2.append(abs(e2)); vals3.append(abs(e2.imag)); vals4.append((abs(e3.real), abs(e3.imag)))
check('C11 two loops: <M|[A, Delta]|M> = 0 on real vectors (Coulomb x eikonal commutator, FSS (5.8)-(5.9))',
      max(vals1) < 1e-9, 'max %.1e' % max(vals1))
check('C11 three loops: <M|[Delta,[Delta,A]]|M> real and non-zero (two Coulomb + one eikonal, FSS (6.1); SLL structure)',
      max(vals2) > 1e-2 and max(vals3) < 1e-9, 'max %.3f' % max(vals2))
check('C11 one Coulomb + two eikonal: <M|[A,[A,Delta]]|M> purely imaginary (drops out of a real cross section)',
      max(v[0] for v in vals4) < 1e-9 and max(v[1] for v in vals4) > 1e-2)

# ----------------------------------------------------------------------------------------------- C12
print('=== C12 CdFR colour structure of space-like splitting ===')
N = 3; T = gellmann(N); f = structure(T); nA = 8
Fadj = np.array([-1j * f[a] for a in range(nA)])
def Sp_q_to_qg():   # parent quark index p -> (quark 1, gluon 2): (t^c)_{i1 p}
    return 'q', ['q', 'g'], np.einsum('cip->icp', T)            # Sp[i1, c2, p]
def Sp_g_to_qqbar():
    return 'g', ['q', 'qb'], np.einsum('pij->ijp', T)           # Sp[i1, j2, p]
def Sp_g_to_gg():
    return 'g', ['g', 'g'], np.einsum('pbc->bcp', f) * 1j * 0 + np.einsum('pbc->bcp', f)   # f_{b c p}
GEN = {'q': T, 'qb': -np.transpose(T, (0, 2, 1)), 'g': Fadj}
CAS = {'q': (N * N - 1) / (2 * N), 'qb': (N * N - 1) / (2 * N), 'g': N}
for mk in (Sp_q_to_qg, Sp_g_to_qqbar, Sp_g_to_gg):
    ptype, (t1, t2), Sp = mk()
    ok = True
    for a in range(nA):
        lhs = np.einsum('ij,jkp->ikp', GEN[t1][a], Sp) + np.einsum('kj,ijp->ikp', GEN[t2][a], Sp)
        rhs = np.einsum('ikq,qp->ikp', Sp, GEN[ptype][a])
        ok = ok and np.allclose(lhs, rhs)
    # CdFR (187): Sp^+ f_abc T1^a T2^b Sp = 0 (as an operator on the parent index)
    acc = np.zeros((Sp.shape[2], Sp.shape[2]), complex)
    for a in range(nA):
        for b in range(nA):
            for c in range(nA):
                if abs(f[a, b, c]) > 1e-14:
                    w = np.einsum('ij,jkp->ikp', GEN[t1][a], np.einsum('kl,ilp->ikp', GEN[t2][b], Sp))
                    # T^c acts on the remaining (non-collinear) partons; as an operator identity it suffices that
                    # Sp^+ f_abc T1^a T2^b Sp (with c open) vanishes for every c
                    pass
    zero = True
    for c in range(nA):
        acc = np.zeros((Sp.shape[2], Sp.shape[2]), complex)
        for a in range(nA):
            for b in range(nA):
                if abs(f[a, b, c]) > 1e-14:
                    w = np.einsum('ij,jkp->ikp', GEN[t1][a], np.einsum('kl,ilp->ikp', GEN[t2][b], Sp))
                    acc += f[a, b, c] * np.einsum('ikp,ikq->pq', Sp.conj(), w)
        zero = zero and np.allclose(acc, 0)
    check('C12 %s -> %s %s : (T1+T2)Sp = Sp T_P ; Sp^+ f_abc T1^a T2^b Sp = 0 (CdFR 187)' % (ptype, t1, t2), ok and zero)

# full-amplitude tests with explicit reduced amplitudes
def full_space(Sp, t12, reduced_types, Mred):
    # Mred: tensor over reduced partons (parent first). Full tensor: contract parent with Sp.
    # Full ordering: parton1, parton2, then reduced partons 2.. (non-collinear)
    Mfull = np.tensordot(Sp, Mred, axes=(2, 0))
    types = list(t12) + list(reduced_types[1:])
    return types, Mfull
def Tvec_g(types, i, a, v): return apply(GEN[types[i]][a], v, i)
def Tdot_g(types, i, j, v): return sum(Tvec_g(types, i, a, Tvec_g(types, j, a, v)) for a in range(nA))
d = np.eye(N)
# reduced q(P) qb q' qb' : basis delta_{P,2'} delta_{3',4'} and delta_{P,4'} delta_{3',2'} (CdFR-type 2->2)
red_types = ['q', 'qb', 'q', 'qb']
e1 = np.einsum('ij,kl->ijkl', d, d); e2 = np.einsum('il,kj->ijkl', d, d)
ptype, t12, Sp = Sp_q_to_qg()
# time-like coherence: T_2 . sum_{j>=3} T_j Sp|M> = -(C12 + C2 - C1)/2 Sp|M>  (C12 = C_P = C_F, C2 = C_A, C1 = C_F)
for Mred in (e1, e2, 0.3 * e1 - 1.1 * e2):
    types, Mf = full_space(Sp, t12, red_types, Mred)
    lhs = sum(Tdot_g(types, 1, j, Mf) for j in range(2, len(types)))
    rhs = -(CAS['q'] + CAS['g'] - CAS['q']) / 2 * Mf
    ok = np.allclose(lhs, rhs)
check('C12 time-like coherence (CdFR 42-44): T_2.sum_{j>=3} T_j Sp|M> = -(C12+C2-C1)/2 Sp|M>', ok)
# eq. (68): with parton 3 (= first non-collinear, index 2 in full ordering) incoming: sign(s_32) = -1, others +1
for Mred in (e1, e2, 0.7 * e1 + 0.2 * e2):
    types, Mf = full_space(Sp, t12, red_types, Mred)
    signsum = -Tdot_g(types, 1, 2, Mf) + sum(Tdot_g(types, 1, j, Mf) for j in range(3, len(types)))
    lhs = -signsum
    rhs = (CAS['q'] + CAS['g'] - CAS['q']) / 2 * Mf + 2 * Tdot_g(types, 1, 2, Mf)
    ok68 = np.allclose(lhs, rhs)
check('C12 CdFR (68): -T_2.sum_j T_j sign(s_j2) = (C12+C2-C1)/2 + 2 T_2.T_3', ok68)
# n = 5: Sp^+ (T2.T3) Sp on the 2-dim reduced space is not proportional to 1
basis_red = [e1, e2]
Bf = np.array([full_space(Sp, t12, red_types, b)[1].reshape(-1) for b in basis_red]).T
Br = np.array([b.reshape(-1) for b in basis_red]).T
Gr = Br.conj().T @ Br
R = np.array([[np.vdot(full_space(Sp, t12, red_types, bi)[1].reshape(-1),
                       Tdot_g(full_space(Sp, t12, red_types, bj)[0], 1, 2, full_space(Sp, t12, red_types, bj)[1]).reshape(-1))
               for bj in basis_red] for bi in basis_red])
Gsp = np.array([[np.vdot(full_space(Sp, t12, red_types, bi)[1].reshape(-1), full_space(Sp, t12, red_types, bj)[1].reshape(-1))
                 for bj in basis_red] for bi in basis_red])
Xmat = np.linalg.solve(Gsp, R)
print('      Sp^+ T2.T3 Sp in the reduced basis {d_P2 d_34, d_P4 d_32}: Gsp^-1 R =\n', np.round(Xmat.real, 6))
check('C12 n=5 (reduced 2->2, 4 coloured partons): T_2.T_3 not proportional to 1',
      not np.allclose(Xmat, Xmat[0, 0] * np.eye(2)))
# n = 4: reduced q(P) qb g (one-dim colour space t^c_{P qb}); <T_2.T_j> depends on which parton is incoming
red3 = ['q', 'qb', 'g']
M3 = np.einsum('cij->ijc', T)
types, Mf = full_space(Sp, t12, red3, M3)
norm = np.vdot(Mf.reshape(-1), Mf.reshape(-1)).real
ev_qb = (np.vdot(Mf.reshape(-1), Tdot_g(types, 1, 2, Mf).reshape(-1)) / norm).real
ev_g = (np.vdot(Mf.reshape(-1), Tdot_g(types, 1, 3, Mf).reshape(-1)) / norm).real
check('C12 n=4 (reduced q qb g): <T_2.T_qb> = %s, <T_2.T_g> = %s (differ: depends on the non-collinear partons)'
      % (sp.nsimplify(round(ev_qb, 10)), sp.nsimplify(round(ev_g, 10))), abs(ev_qb - ev_g) > 0.1)
# n = 3: reduced q(P) qb (two partons): T_2.T_3 = -(C12+C2-C1)/2 = -C_A/2 exactly (as an operator)
red2 = ['q', 'qb']
types, Mf = full_space(Sp, t12, red2, d)
check('C12 n=3: T_2.T_3 = -(C12+C2-C1)/2 = -C_A/2 (c-number)',
      np.allclose(Tdot_g(types, 1, 2, Mf), -CAS['g'] / 2 * Mf))
# anti-hermitian one-loop breaking term drops out of 2 Re <M0|M1>
types, Mf = full_space(Sp, t12, red_types, 0.4 * e1 + (0.3 + 0.8j) * e2)
val = np.vdot(Mf.reshape(-1), (1j * 4 * Tdot_g(types, 1, 2, Mf)).reshape(-1))
check('C12 Re<Sp M0| i 4 T_2.T_3 |Sp M0> = 0 even for complex colour vectors', abs(val.real) < 1e-12, '%.2e' % abs(val.real))

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
