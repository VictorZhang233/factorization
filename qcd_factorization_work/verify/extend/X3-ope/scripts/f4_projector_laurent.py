"""
f4_projector_laurent.py -- checks for Lemma F.7 of the revised X3 report (projection of the forward partonic
amplitude onto T2 in D dimensions; cancellation of the negative powers of nu = p.q).

Abstract D-dimensional tensor algebra with p^2 = 0, a = p.q (= nu), b = q^2 (= -Q^2):
  T^{mu nu} = A g + B p p + C (p q + q p) + E q q + F (p q - q p).
 (a) contractions S1 = p_mu p_nu T, S2 = g_{mu nu} T and the transversality conditions q_mu T^{mu nu} = 0 = T^{mu nu} q_nu;
     with T = -(g - qq/q^2) T1 + Ph Ph T2/nu, Ph = p - (a/b) q, one has
         T2 = nu B = Q^4 [ (D-1) S1 - (nu^2/Q^2) S2 ] / ( (D-2) nu^3 ),   T1 = q^2 E - nu^2 B/q^2,   E = S1/nu^2.
 (b) for a covariant tensor homogeneous of degree n in p (A = al a^n, B = be a^(n-2), C = ga a^(n-1), E = e a^n,
     F = ph a^(n-1)) the transversality conditions force C, A, F, and the projector combination equals be a^(n-1):
     no negative power of nu survives (n = 0..8).
 (c) tree-level quark target in D dimensions (s- and u-channel handbag, spin sum (1/2) pslash, overall factor -1 from
     i * i): S1 = 0, S2 = 2(D-2) omega^2/(1-omega^2), and the projector gives T2 = 4 omega/(1-omega^2),
     T1 = 2 omega^2/(1-omega^2), independently of D; transversality holds.
 (d) physical gluon polarization sum with reference vector q:
     d_{ab}(p,q) = -g_{ab} + (p_a q_b + q_a p_b)/(p.q) - q^2 p_a p_b/(p.q)^2 :
     d.p = 0, d.q = 0, d^a_a = -(D-2) (D-2 physical polarizations with eps.eps* = -1), and d is invariant
     under p -> lambda p (homogeneous of degree 0).
Run:  python3 -I f4_projector_laurent.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

D, a, b, lam, om, Q2 = sp.symbols('D a b lambda omega Q2')
A, B, C, E, F = sp.symbols('A B C E F')

# ---- abstract tensor algebra: rank-2 tensors as dict over the basis {g, pp, pq, qp, qq}; vectors as dict {p, q}
def contract_pp(T):            # p_mu p_nu T^{mu nu}
    return T.get('g', 0) * 0 + T.get('pp', 0) * 0 + (T.get('pq', 0) + T.get('qp', 0)) * 0 + T.get('qq', 0) * a ** 2

def contract_g(T):             # g_{mu nu} T^{mu nu}
    return T.get('g', 0) * D + T.get('pp', 0) * 0 + (T.get('pq', 0) + T.get('qp', 0)) * a + T.get('qq', 0) * b

def left_q(T):                 # q_mu T^{mu nu} = alpha p^nu + beta q^nu
    al = T.get('pp', 0) * a + T.get('qp', 0) * b
    be = T.get('g', 0) + T.get('pq', 0) * a + T.get('qq', 0) * b
    return {'p': al, 'q': be}

def right_q(T):                # T^{mu nu} q_nu
    al = T.get('pp', 0) * a + T.get('pq', 0) * b
    be = T.get('g', 0) + T.get('qp', 0) * a + T.get('qq', 0) * b
    return {'p': al, 'q': be}

def tensor(Av, Bv, Cv, Ev, Fv):
    return {'g': Av, 'pp': Bv, 'pq': Cv + Fv, 'qp': Cv - Fv, 'qq': Ev}

# (a) structural identities
T = tensor(A, B, C, E, F)
conds = [left_q(T)['p'], left_q(T)['q'], right_q(T)['p'], right_q(T)['q']]
sol = sp.solve(conds, [A, C, F], dict=True)[0]
S1 = sp.simplify(contract_pp(T).subs(sol))
S2 = sp.simplify(contract_g(T).subs(sol))
nu = a
Qsq = -b
T2_proj = sp.simplify(Qsq ** 2 * ((D - 1) * S1 - (nu ** 2 / Qsq) * S2) / ((D - 2) * nu ** 3))
print("(a) transversality solution:", sol)
print("(a) projector T2 - nu*B =", sp.simplify(T2_proj - nu * B), "; E - S1/nu^2 =", sp.simplify(E - S1 / nu ** 2))
# decomposition T = -(g - qq/b) T1 + Ph Ph T2/nu, Ph = p - (a/b) q  ->  compare components
T1s, T2s = sp.symbols('T1s T2s')
Tdec = {'g': -T1s, 'qq': T1s / b + (a / b) ** 2 * T2s / nu, 'pp': T2s / nu,
        'pq': -(a / b) * T2s / nu, 'qp': -(a / b) * T2s / nu}
Ttr = {k: sp.simplify(v.subs(sol)) for k, v in T.items()}
s12 = sp.solve([sp.simplify(Tdec[k] - Ttr[k]) for k in ('g', 'pp')], [T1s, T2s], dict=True)[0]
consistent = all(sp.simplify((Tdec[k] - Ttr[k]).subs(s12)) == 0 for k in Tdec)
print("(a) decomposition: T2 =", sp.simplify(s12[T2s]), "; T1 =", sp.simplify(s12[T1s]),
      "; all five components consistent:", consistent)

# (b) homogeneous tensors of degree n: no negative powers of nu
al_, be_, ga_, e_, ph_ = sp.symbols('alpha beta gamma e phi')
okb = True
for n in range(0, 9):
    Bn = be_ * a ** (n - 2) if n >= 2 else 0
    Tn = tensor(al_ * a ** n, Bn, ga_ * a ** (n - 1) if n >= 1 else 0, e_ * a ** n, ph_ * a ** (n - 1) if n >= 1 else 0)
    cn = [sp.expand(c) for c in (left_q(Tn)['p'], left_q(Tn)['q'], right_q(Tn)['p'], right_q(Tn)['q'])]
    unknowns = [s for s in (al_, ga_, ph_) if any(c.has(s) for c in cn)]
    sn = sp.solve(cn, unknowns, dict=True)
    sn = sn[0] if sn else {}
    S1n = sp.expand(contract_pp(Tn).subs(sn))
    S2n = sp.expand(contract_g(Tn).subs(sn))
    T2n = sp.simplify(Qsq ** 2 * ((D - 1) * S1n - (nu ** 2 / Qsq) * S2n) / ((D - 2) * nu ** 3))
    expect = be_ * a ** (n - 1) if n >= 2 else 0
    good = sp.simplify(T2n - expect) == 0
    okb &= good
    print("(b) n=%d : T2 from projector = %s ; polynomial in nu (no negative powers): %s" % (n, sp.factor(T2n), good))
print("(b) all degrees:", okb)

# (c) tree-level quark handbag in D dimensions.  Tr[pslash g^mu kslash g^nu] = 4 (p^mu k^nu + p^nu k^mu - g^{mu nu} p.k)
#     s-channel k = p + q, denominator (p+q)^2 = 2a + b ; u-channel q -> -q.  Spin average 1/2, overall factor -1.
def trace_tensor(sign):          # (1/2) Tr[pslash g^mu (p + sign q)slash g^nu]  with p^2 = 0
    k_p, k_q = 1, sign           # k = p + sign q
    pk = sign * a                # p.k
    Tt = {'g': -pk, 'pp': 2 * k_p, 'pq': k_q, 'qp': k_q, 'qq': 0}
    return {kk: 2 * v for kk, v in Tt.items()}    # (1/2)*4 = 2
Ts = trace_tensor(+1)
Tu = trace_tensor(-1)
den_s = 2 * a + b
den_u = -2 * a + b
Ttree = {kk: -(Ts[kk] / den_s + Tu[kk] / den_u) for kk in Ts}
lq, rq = left_q(Ttree), right_q(Ttree)
transverse = all(sp.simplify(v) == 0 for v in (lq['p'], lq['q'], rq['p'], rq['q']))
S1t = sp.simplify(contract_pp(Ttree))
S2t = sp.simplify(contract_g(Ttree))
T2t = sp.simplify(Qsq ** 2 * ((D - 1) * S1t - (nu ** 2 / Qsq) * S2t) / ((D - 2) * nu ** 3))
to_om = {a: om * Q2 / 2, b: -Q2}
T2om = sp.simplify(T2t.subs(to_om))
T1om = sp.simplify((b * S1t / a ** 2 - a ** 2 * (T2t / a) / b).subs(to_om))
S2om = sp.simplify(S2t.subs(to_om))
print("(c) tree level: transverse:", transverse, "; S1 =", S1t, "; S2 =", sp.factor(S2om))
print("(c) tree level: T2 =", sp.factor(T2om), "; T2 - 4w/(1-w^2) =", sp.simplify(T2om - 4 * om / (1 - om ** 2)),
      "; T1 =", sp.factor(T1om), "; T1 - 2w^2/(1-w^2) =", sp.simplify(T1om - 2 * om ** 2 / (1 - om ** 2)))
print("(c) Taylor series of T2:", sp.series(T2om, om, 0, 8))

# (d) physical gluon projector with reference vector q (indices contracted abstractly)
#     d_{ab} = -g + (pq + qp)/a - b pp/a^2 ;  contract with p^b, q^b, g^{ab}
d = {'g': -1, 'pq': 1 / a, 'qp': 1 / a, 'pp': -b / a ** 2, 'qq': 0}
def contract_vec_right(Tt, vec):          # T_{ab} v^b, v = p or q ; result as vector {p:, q:}
    if vec == 'p':
        return {'p': Tt['g'] + Tt['qp'] * a + Tt['pp'] * 0, 'q': Tt['pq'] * 0 + Tt['qq'] * a}
    return {'p': Tt['pp'] * a + Tt['pq'] * b, 'q': Tt['g'] + Tt['qp'] * a + Tt['qq'] * b}
dp = {k: sp.simplify(v) for k, v in contract_vec_right(d, 'p').items()}
dq = {k: sp.simplify(v) for k, v in contract_vec_right(d, 'q').items()}
trd = sp.simplify(contract_g(d))
scal = {'g': -1, 'pq': lam / (lam * a), 'qp': lam / (lam * a), 'pp': -b * lam ** 2 / (lam * a) ** 2, 'qq': 0}
hom = all(sp.simplify(scal[k] - d[k]) == 0 for k in d)
print("(d) gluon projector: d.p =", dp, "; d.q =", dq, "; trace =", trd, "; degree-0 homogeneous in p:", hom)
