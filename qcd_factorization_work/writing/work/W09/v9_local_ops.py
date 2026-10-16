"""W09 / v9: independent symbolic re-derivation of the one-loop UV poles of the local twist-2 operators (prop:pdf-local-anomalous),
Feynman gauge, quark and mixing graphs (A1 vertex, A2 = A3 operator-gluon, B <q|O_g|q>, C1 = C2 <g|O_q|g>), N = 1..12.
Method: D-dimensional traces (w9lib.dtrace) of the integrand numerators, Feynman parameters, shift, extraction of the part of
degree 2 in the loop momentum q (3 propagators) or 0 (2 propagators) -- the only logarithmically UV-divergent pieces for
massless on-shell kinematics (Delta = 0) -- angular average <(a.q)(b.q)> = (a.b) q^2/D, and
  int d^Dq/(2pi)^D q^2/(q^2)^3 |_UV = int d^Dq/(2pi)^D 1/(q^2)^2 |_UV = i/(16 pi^2 eps).
Results in units (alpha_s/2pi)(1/eps) x colour factor, relative to the tree 2(n.p)^N:
  A1 = 1/(N(N+1)),  A2 = A3 = -(S_1(N)-1),  B = (N^2+N+2)/((N-1)N(N+1)),  C1 = C2 = (N^2+N+2)/(N(N+1)(N+2));
with delta Z_2 = -1/2 (Feynman gauge):  A1 + 2 A2 - 1/2 = gamma_qq(N)/C_F.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from w9lib import dtrace, D as Dsym

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

y, x, t = sp.symbols('y x t')
np_ = sp.Symbol('np', positive=True)          # n.p
qq = sp.Symbol('qq')                          # q^2
nq, pq, eq = sp.symbols('nq pq eq')           # n.q, p.q, eps.q

def avg2(expr):
    """degree-2 part in q (coefficient of t^2 after q -> t q) with angular averaging.
    expr is a polynomial in nq, pq, eq, qq.  Pairs: (n.n)=0, (n.p)=np, (p.p)=0, (e.e)=-1, (n.e)=(p.e)=0."""
    e2 = sp.expand(expr.subs({nq: t * nq, pq: t * pq, eq: t * eq, qq: t ** 2 * qq}))
    c2 = sp.expand(e2.coeff(t, 2))
    dots = {('n', 'n'): 0, ('n', 'p'): np_, ('p', 'p'): 0, ('e', 'e'): -1, ('n', 'e'): 0, ('p', 'e'): 0}
    sym = {'n': nq, 'p': pq, 'e': eq}
    out = sp.Integer(0)
    poly = sp.Poly(c2, nq, pq, eq, qq)
    for monom, coeff in poly.terms():
        a, b, c, d = monom
        if d == 1 and a + b + c == 0:
            out += coeff * qq
        elif d == 0 and a + b + c == 2:
            vecs = ['n'] * a + ['p'] * b + ['e'] * c
            v1, v2 = sorted(vecs)
            out += coeff * dots[(v1, v2)] * qq / Dsym
        else:
            raise ValueError('unexpected monomial %s' % (monom,))
    return sp.expand(out)

def S1(n): return sum(sp.Rational(1, j) for j in range(1, n + 1))

for N in range(1, 13):
    # ---- A1: -i g^2 C_F int (1/2)Tr[pslash g^mu kslash nslash kslash g_mu] (n.k)^{N-1} / ((k^2)^2 (p-k)^2)
    # Feynman: 1/(A^2 B) = int dy 2(1-y)/[(k - y p)^2]^3, k = q + y p
    # dot products with k = q + y p:  n.k = nq + y np, p.k = pq (p^2=0), k.k = qq + 2 y pq
    dots = {('k', 'k'): sp.Symbol('kk'), ('k', 'n'): sp.Symbol('kn'), ('k', 'p'): sp.Symbol('kp'),
            ('n', 'n'): 0, ('n', 'p'): np_, ('p', 'p'): 0}
    tr = sp.Rational(1, 2) * dtrace([('v', 'p'), ('i', 'm'), ('v', 'k'), ('v', 'n'), ('v', 'k'), ('i', 'm')], dots)
    sub = {sp.Symbol('kk'): qq + 2 * y * pq, sp.Symbol('kn'): nq + y * np_, sp.Symbol('kp'): pq}
    num = sp.expand(tr.subs(sub) * (nq + y * np_) ** (N - 1))
    c = avg2(num)
    # UV pole: -i g^2 C_F * int dy 2(1-y) c/qq * (i/(16 pi^2 eps))  = (alpha_s/4pi)(C_F/eps) int 2(1-y) c/qq
    val4 = sp.integrate(2 * (1 - y) * sp.simplify(c / qq), (y, 0, 1))
    A1 = sp.simplify((val4 / (2 * np_ ** N) / 2).subs(Dsym, 4))      # /tree, alpha_s/4pi -> alpha_s/2pi
    # ---- A2: i g^2 C_F int (1/2)Tr[pslash nslash kslash nslash] sum_j (n.p)^j (n.k)^{N-2-j} / (l^2 k^2), k = p - l
    # Feynman: 1/(l^2 (p-l)^2) = int dx 1/[(l - x p)^2]^2 ; l = q + x p, k = (1-x) p - q ; degree 0 part
    dots2 = {('k', 'k'): sp.Symbol('kk'), ('k', 'n'): sp.Symbol('kn'), ('k', 'p'): sp.Symbol('kp'),
             ('n', 'n'): 0, ('n', 'p'): np_, ('p', 'p'): 0}
    tr2 = sp.Rational(1, 2) * dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'n')], dots2)
    kn = (1 - x) * np_ - nq
    num2 = sp.expand(tr2.subs({sp.Symbol('kn'): kn, sp.Symbol('kk'): sp.Symbol('kk'), sp.Symbol('kp'): -pq}) *
                     sum(np_ ** j * kn ** (N - 2 - j) for j in range(0, N - 1)))
    num2_0 = sp.expand(num2.subs({nq: 0, pq: 0, eq: 0, qq: 0}))
    # UV pole: i g^2 C_F * int dx num2_0 * (i/(16pi^2 eps)) = -(alpha_s/4pi)(C_F/eps) int dx num2_0
    val4b = -sp.integrate(num2_0, (x, 0, 1))
    A2 = sp.simplify(val4b / (2 * np_ ** N) / 2)
    ok = sp.simplify(A1 - sp.Rational(1, N * (N + 1))) == 0 and sp.simplify(A2 + (S1(N) - 1)) == 0
    gqq = sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * S1(N)
    check('N=%2d: A1 = %s = 1/(N(N+1)),  A2 = A3 = %s = -(S1-1);  A1 + 2A2 - 1/2 = %s = gamma_qq/C_F'
          % (N, A1, A2, sp.simplify(A1 + 2 * A2 - sp.Rational(1, 2))), ok and sp.simplify(A1 + 2 * A2 - sp.Rational(1, 2) - gqq) == 0)

for N in range(2, 13, 2):
    # ---- B: i g^2 C_F int T^{s n} V_{n s}(l,-l) / ((l^2)^2 (l-p)^2),  T = (1/2)Tr[pslash g^s kslash g^n], k = p - l
    # T.V = 8 (n.l)^{N-2}[2 (n.p)(n.l)(p.l) - (n.l)^2 (p.l) - l^2 (n.p)^2]  (contracting the even-N vertex)
    # derive T.V from the trace with the vertex V_{ns} = 2 (n.l)^{N-2}[-(n.l)^2 g_{ns} + n.l (l_n n_s + n_n l_s) - l^2 n_n n_s]
    dots3 = {('k', 'k'): sp.Symbol('kk'), ('k', 'l'): sp.Symbol('kl'), ('k', 'n'): sp.Symbol('kn'), ('k', 'p'): sp.Symbol('kp'),
             ('l', 'l'): sp.Symbol('ll'), ('l', 'n'): sp.Symbol('ln'), ('l', 'p'): sp.Symbol('lp'), ('n', 'n'): 0, ('n', 'p'): np_,
             ('p', 'p'): 0}
    half = sp.Rational(1, 2)
    t_g = half * dtrace([('v', 'p'), ('i', 'a'), ('v', 'k'), ('i', 'a')], dots3)          # g_{ns} contraction: T^s_s
    t_ln = half * dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'l')], dots3)          # T^{s n} l_n n_s : n at s, l at n
    t_nl = half * dtrace([('v', 'p'), ('v', 'l'), ('v', 'k'), ('v', 'n')], dots3)
    t_nn = half * dtrace([('v', 'p'), ('v', 'n'), ('v', 'k'), ('v', 'n')], dots3)
    LN = sp.Symbol('ln'); LL = sp.Symbol('ll')
    TV = 2 * LN ** (N - 2) * (-(LN ** 2) * t_g + LN * (t_ln + t_nl) - LL * t_nn)
    # k = p - l
    subk = {sp.Symbol('kk'): LL - 2 * sp.Symbol('lp'), sp.Symbol('kl'): sp.Symbol('lp') - LL, sp.Symbol('kn'): np_ - LN,
            sp.Symbol('kp'): -sp.Symbol('lp')}
    TV = sp.expand(TV.subs(subk).subs(Dsym, 4))
    TVref = 8 * LN ** (N - 2) * (2 * np_ * LN * sp.Symbol('lp') - LN ** 2 * sp.Symbol('lp') - LL * np_ ** 2)
    okTV = sp.simplify(TV - sp.expand(TVref)) == 0
    # Feynman: 1/(A^2 B) with A = l^2, B = (l-p)^2: weight 2(1-y), l = q + y p
    TVq = sp.expand(TV.subs({LN: nq + y * np_, sp.Symbol('lp'): pq, LL: qq + 2 * y * pq}))
    cB = avg2(TVq)
    valB4 = -sp.integrate(2 * (1 - y) * sp.simplify(cB / qq), (y, 0, 1))   # i * i = -1
    B = sp.simplify((valB4 / (2 * np_ ** N) / 2).subs(Dsym, 4))
    okB = sp.simplify(B - sp.Rational(N ** 2 + N + 2, (N - 1) * N * (N + 1))) == 0
    # ---- C1: -i g^2 T_F int (n.l)^{N-1} Tr[nslash lslash epsslash (l-p)slash epsslash lslash] / ((l^2)^2 (l-p)^2), pol. averaged
    dots4 = {('e', 'e'): -1, ('e', 'l'): sp.Symbol('el'), ('e', 'n'): 0, ('e', 'p'): 0, ('l', 'l'): LL, ('l', 'n'): LN,
             ('l', 'p'): sp.Symbol('lp'), ('n', 'n'): 0, ('n', 'p'): np_, ('p', 'p'): 0, ('e', 'r'): sp.Symbol('er'),
             ('l', 'r'): sp.Symbol('lr'), ('n', 'r'): sp.Symbol('nr'), ('p', 'r'): sp.Symbol('pr'), ('r', 'r'): sp.Symbol('rr')}
    # r = l - p
    trC = dtrace([('v', 'n'), ('v', 'l'), ('v', 'e'), ('v', 'r'), ('v', 'e'), ('v', 'l')], dots4)
    trC = sp.expand(trC.subs({sp.Symbol('er'): sp.Symbol('el'), sp.Symbol('lr'): LL - sp.Symbol('lp'), sp.Symbol('nr'): LN - np_,
                              sp.Symbol('pr'): sp.Symbol('lp'), sp.Symbol('rr'): LL - 2 * sp.Symbol('lp')}))
    trCref = 16 * LN * sp.Symbol('el') ** 2 + 4 * LL * LN - 8 * LN * sp.Symbol('lp') + 4 * np_ * LL
    okC = sp.simplify(trC - trCref) == 0
    numC = sp.expand((trC * LN ** (N - 1)).subs({LN: nq + y * np_, sp.Symbol('lp'): pq, LL: qq + 2 * y * pq, sp.Symbol('el'): eq}))
    cC = avg2(numC)
    valC4 = sp.integrate(2 * (1 - y) * sp.simplify(cC / qq), (y, 0, 1))     # -i * i = +1
    C1 = sp.simplify((valC4 / (2 * np_ ** N) / 2).subs(Dsym, 4))
    okC1 = sp.simplify(C1 - sp.Rational(N ** 2 + N + 2, N * (N + 1) * (N + 2))) == 0
    check('N=%2d: T.V reduction %s; B = %s = (N^2+N+2)/((N-1)N(N+1)); trace(C) reduction %s; C1 = %s = (N^2+N+2)/(N(N+1)(N+2))'
          % (N, okTV, B, okC, C1), okTV and okB and okC and okC1)

print('\nSUMMARY v9: %d PASS, %d FAIL' % (npass, nfail))
