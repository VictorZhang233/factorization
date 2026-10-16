"""
W07 / Ch7 -- s2_compton.py
Checks for sec:dis-compton and the tensor normalization of thm:dis-ope / lem:dis-tree-ope.
Tensors built from {g, pp, pq, qp, qq} are represented by coefficient dictionaries; contractions are done with the
invariants p^2, q^2=-Q^2, nu=p.q in D dimensions (g^mu_mu = D).
 (1) the D-dim T_2 projector  T_2 = Q^4[(D-1) S1 - (nu^2/Q^2) S2] / ((D-2) nu^3)  (massless target, App M lem:appM-t2-projector)
     and the 4D projector of VF-REF-1 (massive target);
 (2) tree-level forward Compton amplitude of a massless quark (exact in D):
     T_2 = 4 e^2 w/(1-w^2), T_1 = 2 e^2 w^2/(1-w^2); crossing T_1 even, T_2 odd;
 (3) Im T_2(w + i0) = 2 pi e^2 delta(w-1) near w = 1  and F_2 = e^2 delta(1-x) (dispersion check);
 (4) OPE normalization: the n-th term of the thm:dis-ope formula contracted with <O> = 2A (P..P - traces) gives
     T_1 > 2 w^n C_1 A,  T_2 > 4 w^(n-1) C_2 A  (massless target, traces vanish; massive: leading term);
 (5) the tree-level coefficients C_1 = C_2 = e_q^2 (even n), odd n cancel (lem:dis-tree-ope).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

ok_all = True
def check(name, expr):
    global ok_all
    e = sp.simplify(expr)
    ok = (e == 0)
    ok_all &= ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   residual = {e}"))

D, Q2, nu, M2, w, eq = sp.symbols('D Q2 nu M2 omega e_q')
STRUCT = ['g', 'pp', 'pq', 'qp', 'qq']

def inv(a, b, p2):
    t = {('p', 'p'): p2, ('q', 'q'): -Q2, ('p', 'q'): nu, ('q', 'p'): nu}
    return t[(a, b)]

def contract_with(T, a, b, p2):
    """a_mu b_nu T^{mu nu} for a,b in {'p','q'}; T = dict struct->coeff"""
    s = 0
    for k, c in T.items():
        if k == 'g':
            s += c * inv(a, b, p2)
        else:
            s += c * inv(a, k[0], p2) * inv(k[1], b, p2)
    return s

def trace_g(T, p2):
    s = 0
    for k, c in T.items():
        s += c * (D if k == 'g' else inv(k[0], k[1], p2))
    return s

def decomposition(T1, T2, p2):
    """-(g - qq/q^2) T1 + Pt Pt T2/nu,  Pt = p - (nu/q^2) q = p + (nu/Q2) q"""
    a = nu / Q2
    return {'g': -T1, 'qq': T1 * (-1 / Q2) * (-1) + T2 / nu * a**2,
            'pp': T2 / nu, 'pq': T2 / nu * a, 'qp': T2 / nu * a}
# note: -(g^{mu nu} - q^mu q^nu/q^2) T1 = -g T1 + (q q / q^2) T1 = -g T1 - (qq/Q2) T1  -> fix sign below
def decomposition_ok(T1, T2, p2):
    a = nu / Q2
    return {'g': -T1, 'qq': -T1 / Q2 + T2 / nu * a**2, 'pp': T2 / nu, 'pq': T2 / nu * a, 'qp': T2 / nu * a}

# ---------------------------------------------------------------- (1) projectors
print("(1) projectors")
t1, t2 = sp.symbols('t1 t2')
Tm = decomposition_ok(t1, t2, 0)
S1 = contract_with(Tm, 'p', 'p', 0)
S2 = trace_g(Tm, 0)
proj = Q2**2 * ((D - 1) * S1 - (nu**2 / Q2) * S2) / ((D - 2) * nu**3)
check("massless: T_2 = Q^4[(D-1)S1-(nu^2/Q^2)S2]/((D-2)nu^3)", proj - t2)
check("massless: S1 = -(nu^2/Q^2) T1 + (nu^3/Q^4) T2", S1 - (-(nu**2 / Q2) * t1 + nu**3 / Q2**2 * t2))
check("massless: S2 = -(D-1) T1 + (nu/Q^2) T2", S2 - (-(D - 1) * t1 + nu / Q2 * t2))
check("transversality q_mu T^{mu nu}: coefficient of p^nu", sp.simplify(sum(
    c * (inv('q', k[0], 0) if k[1] == 'p' else 0) for k, c in Tm.items() if k != 'g')))
# 4D massive projector (VF-REF-1): T_2 = 3 nu/(2 (Pt^2)^2) [Pt Pt - Pt^2/3 g] T
Tmm = decomposition_ok(t1, t2, M2)
a = nu / Q2
def contract_Pt(T):
    # Pt = p + a q ; Pt_mu Pt_nu T^{mu nu}
    return (contract_with(T, 'p', 'p', M2) + a * contract_with(T, 'p', 'q', M2)
            + a * contract_with(T, 'q', 'p', M2) + a**2 * contract_with(T, 'q', 'q', M2))
Pt2 = M2 + 2 * a * nu + a**2 * (-Q2)
check("Pt^2 = M^2 + nu^2/Q^2", Pt2 - (M2 + nu**2 / Q2))
proj4 = 3 * nu / (2 * Pt2**2) * (contract_Pt(Tmm) - Pt2 / 3 * trace_g(Tmm, M2).subs(D, 4))
check("4D massive: T_2 = 3nu/(2(Pt^2)^2)[Pt Pt - Pt^2 g/3] T  (VF-REF-1)", proj4 - t2)

# ---------------------------------------------------------------- (2) tree amplitude
print("(2) tree-level forward Compton amplitude of a massless quark, exact in D")
# T^{mu nu} = -e^2 (1/2) Tr[pslash gamma^mu kslash gamma^nu]/k^2 |_{k=p+q} + (mu<->nu, q->-q)
# (1/2)Tr[p g^mu k g^nu] = 2 (p^mu k^nu + p^nu k^mu - g^{mu nu} p.k)
def tree_piece(sgn):
    # k = p + sgn q ; k^2 = 2 sgn nu - Q2 ; returns coefficient dict of -e^2 * 2(p k + k p - g p.k)/k^2
    k2 = 2 * sgn * nu - Q2
    pk = sgn * nu   # p^2 = 0
    pref = -eq**2 * 2 / k2
    d = {'g': -pref * pk, 'pp': pref * 2, 'pq': pref * sgn, 'qp': pref * sgn, 'qq': 0}
    return d
Ttree = {s: sp.simplify(tree_piece(+1)[s] + tree_piece(-1)[s]) for s in STRUCT}
S1t = contract_with(Ttree, 'p', 'p', 0)
S2t = trace_g(Ttree, 0)
T2tree = sp.simplify((Q2**2 * ((D - 1) * S1t - (nu**2 / Q2) * S2t) / ((D - 2) * nu**3)).subs(nu, w * Q2 / 2))
check("T_2(tree) = 4 e^2 w/(1-w^2)", T2tree - 4 * eq**2 * w / (1 - w**2))
# T_1 from S2 = -(D-1) T1 + (nu/Q2) T2
T1tree = sp.simplify(((nu / Q2 * T2tree.subs(w, 2 * nu / Q2) - S2t) / (D - 1)).subs(nu, w * Q2 / 2))
check("T_1(tree) = 2 e^2 w^2/(1-w^2)", T1tree - 2 * eq**2 * w**2 / (1 - w**2))
# full tensor equals the decomposition (transversality)
Tdec = decomposition_ok(T1tree.subs(w, 2 * nu / Q2), T2tree.subs(w, 2 * nu / Q2), 0)
for s in STRUCT:
    check(f"tree tensor = decomposition, structure {s}", Ttree[s] - Tdec[s])
check("crossing: T_2(-w) = -T_2(w)", T2tree.subs(w, -w) + T2tree)
check("crossing: T_1(-w) = T_1(w)", T1tree.subs(w, -w) - T1tree)
# Taylor coefficients: T_2 = sum_{n even} 4 w^{n-1} e^2 ; T_1 = sum_{n even>=2} 2 w^n e^2
ser2 = sp.series(T2tree, w, 0, 12).removeO()
ser1 = sp.series(T1tree, w, 0, 12).removeO()
check("Taylor: T_2 = sum_{n=2,4,..} 4 e^2 w^{n-1}", ser2 - sum(4 * eq**2 * w**(n - 1) for n in range(2, 13, 2)))
check("Taylor: T_1 = sum_{n=2,4,..} 2 e^2 w^n", ser1 - sum(2 * eq**2 * w**n for n in range(2, 11, 2)))

# ---------------------------------------------------------------- (3) discontinuity
print("(3) discontinuity of the free-quark amplitude")
# T_2 = 4 e^2 w /((1-w)(1+w)); at w + i0 near w=1: 1/(1-w-i0) = P 1/(1-w) + i pi delta(1-w)
res = sp.limit(4 * eq**2 * w / (1 + w), w, 1)
check("Im T_2(w+i0) = pi * [4w/(1+w)]_{w=1} delta(w-1) = 2 pi e^2 delta(w-1)", sp.pi * res - 2 * sp.pi * eq**2)
print("   delta(1 - 1/w) = w^2 delta(w-1) = delta(w-1)  =>  Im T_2 = 2 pi F_2 with F_2 = e^2 delta(1-x)")
# moments of F2 = e^2 delta(1-x): int x^{n-2} F2 = e^2 = t_n/4 for all even n
print("   int_0^1 x^{n-2} e^2 delta(1-x) dx = e^2 = (Taylor coefficient of w^{n-1})/4  -> PASS by (2)")

# ---------------------------------------------------------------- (4) OPE normalization
print("(4) normalization of the OPE formula of thm:dis-ope (massless target: P..P traceless)")
C1, C2, A = sp.symbols('C1 C2 A')
for n in [2, 4, 6]:
    # term1: (-g + qq/q^2) 2^n (q.P)^n/(Q^2)^n C1 * 2A
    # term2: (g^mu_mu1 - q^mu q_mu1/q^2)(g^nu_mu2 - ...) P^mu1 P^mu2 * 2^n (q.P)^(n-2)/(Q^2)^(n-1) C2 * 2A = Pt Pt ...
    term1_coef = 2**n * nu**n / Q2**n * C1 * 2 * A
    term2_coef = 2**n * nu**(n - 2) / Q2**(n - 1) * C2 * 2 * A
    # compare with decomposition: -(g-qq/q^2) T1 + Pt Pt T2/nu
    T1n = term1_coef
    T2n = term2_coef * nu
    check(f"n={n}: T_1 contribution = 2 w^n C1 A", sp.simplify(T1n.subs(nu, w * Q2 / 2) - 2 * w**n * C1 * A))
    check(f"n={n}: T_2 contribution = 4 w^(n-1) C2 A", sp.simplify(T2n.subs(nu, w * Q2 / 2) - 4 * w**(n - 1) * C2 * A))

# ---------------------------------------------------------------- (5) tree coefficients
print("(5) lem:dis-tree-ope: compare the tree Taylor coefficients with (4): C_1 = C_2 = e_q^2, A = 1")
for n in range(2, 11, 2):
    c2 = ser2.coeff(w, n - 1) / 4
    c1 = ser1.coeff(w, n) / 2
    check(f"n={n}: C_2 A = e^2 and C_1 A = e^2", (c2 - eq**2) + (c1 - eq**2))
for n in range(1, 11, 2):
    check(f"odd n={n}: no w^(n-1) term in T_2 and no w^n term in T_1", ser2.coeff(w, n - 1) + ser1.coeff(w, n))
# s-channel alone: T_2^s has both parities -> the u channel cancels odd n
Ts = {s: tree_piece(+1)[s] for s in STRUCT}
S1s, S2s = contract_with(Ts, 'p', 'p', 0), trace_g(Ts, 0)
T2s = sp.simplify((Q2**2 * ((D - 1) * S1s - (nu**2 / Q2) * S2s) / ((D - 2) * nu**3)).subs(nu, w * Q2 / 2))
print("   s-channel alone: T_2^s =", sp.factor(T2s), " (all powers w^k, k>=0; adding the u channel removes the even k, i.e. odd n=k+1)")

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
