"""
rv22_algebra.py -- independent checks by adversarial reviewer #2 (round 2) of the revised X3 report.
Written from scratch (does not import the X3 scripts).

(A) Lemma F.7(a): D-dimensional T2 projector, derived from a general tensor T = A g + B pp + C pq + C' qp + E qq
    (p^2 = 0, q^2 = -Q^2, p.q = nu) with left/right transversality imposed symbolically.
(B) Lemma F.7(b): for the n-th naive term (homogeneous of degree n in p on the light cone) only n = 0, 1 can
    produce non-positive powers of nu in T2 = beta_n nu^(n-1); check beta_0 = beta_1 = 0 symbolically in D for
    the most general transverse polynomial tensor, so that "the general case is the same linear algebra" is not
    needed (for n >= 2 the power nu^(n-1) is already regular).
(C) Tree-level quark forward Compton amplitude in D dimensions (trace formula, Tr 1 = 4): T2 is D-independent and
    equals 4 w/(1-w^2) up to the overall sign convention of T.
(D) Gluon physical polarisation tensor d_ab(p,q): d.p = d.q = 0, trace 2 - D.
(E) Evanescent structures: the contraction Gamma^(n)_{mu1..mun} Gamma^(n) mu1..mun = (-1)^{n(n-1)/2} D(D-1)..(D-n+1)
    (Euclidean Clifford algebra), checked with explicit gamma matrices in D = 4, 5, 6, 7; for n = 5 it vanishes at
    D = 4 only.  Hence D-dimensional operators built with Gamma^(5) (x) Gamma^(5) have tree vertices O(D-4):
    Lemma A.3's tree-level injectivity fails for them at D = 4 (relevant to Theorem A (A4)/(A5)).
Run: python3 -I rv22_algebra.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

D, Q, nu, w = sp.symbols('D Q nu omega', positive=True)
A, B, C, Cp, E = sp.symbols('A B C Cp E')

# ---------------------------------------------------------------- (A) projector
# scalar products: p.p = 0, p.q = nu, q.q = -Q^2 ; tensors represented by coefficient vectors over the basis
# {g, pp, pq, qp, qq}; contraction rules for q_mu T^{mu nu} (coefficient of p^nu and q^nu):
def left_q(Tc):
    A_, B_, C_, Cp_, E_ = Tc
    # q_mu g^{mu nu} = q^nu ; q_mu p^mu p^nu = nu p^nu ; q_mu p^mu q^nu = nu q^nu ; q_mu q^mu p^nu = -Q^2 p^nu ;
    # q_mu q^mu q^nu = -Q^2 q^nu
    coef_p = B_ * nu + Cp_ * (-Q**2)
    coef_q = A_ + C_ * nu + E_ * (-Q**2)
    return sp.simplify(coef_p), sp.simplify(coef_q)

def right_q(Tc):
    A_, B_, C_, Cp_, E_ = Tc
    # T^{mu nu} q_nu: g -> q^mu ; pp -> nu p^mu ; pq -> -Q^2 p^mu ; qp -> nu q^mu ; qq -> -Q^2 q^mu
    coef_p = B_ * nu + C_ * (-Q**2)
    coef_q = A_ + Cp_ * nu + E_ * (-Q**2)
    return sp.simplify(coef_p), sp.simplify(coef_q)

def S1(Tc):   # p_mu p_nu T^{mu nu}
    A_, B_, C_, Cp_, E_ = Tc
    return sp.simplify(A_ * 0 + B_ * 0 + C_ * 0 + Cp_ * 0 + E_ * nu**2)

def S2(Tc):   # g_mu nu T^{mu nu}
    A_, B_, C_, Cp_, E_ = Tc
    return sp.simplify(A_ * D + B_ * 0 + (C_ + Cp_) * nu + E_ * (-Q**2))

Tgen = (A, B, C, Cp, E)
eqs = list(left_q(Tgen)) + list(right_q(Tgen))
sol = sp.solve(eqs, [A, C, Cp, E], dict=True)
print("(A) transversality solution (B free, plus one more):", sol)
# expected: transverse space is 2-dim: T = -T1 gtilde + T2 Phat Phat / nu
T1, T2 = sp.symbols('T1 T2')
gt = (1, 0, 0, 0, 1 / Q**2)                      # gtilde = g - qq/q^2 = g + qq/Q^2
# Phat = p - (p.q/q^2) q = p + (nu/Q^2) q
PP = (0, 1, nu / Q**2, nu / Q**2, nu**2 / Q**4)  # Phat^mu Phat^nu
Tdec = tuple(sp.simplify(-T1 * a + T2 * b / nu) for a, b in zip(gt, PP))
print("(A) decomposition is transverse:", [sp.simplify(x) for x in left_q(Tdec) + right_q(Tdec)] == [0, 0, 0, 0])
proj = sp.simplify(Q**4 * ((D - 1) * S1(Tdec) - nu**2 / Q**2 * S2(Tdec)) / ((D - 2) * nu**3))
print("(A) Q^4[(D-1)S1 - (nu^2/Q^2)S2]/((D-2)nu^3) - T2 =", sp.simplify(proj - T2))
okA = sp.simplify(proj - T2) == 0

# ---------------------------------------------------------------- (B) degrees 0 and 1 (and 2,3 for illustration)
def general_degree_n(n):
    """most general tensor in span{g,pp,pq,qp,qq} homogeneous of degree n in p on the light cone, with
    polynomial coefficients: g, qq carry nu^n ; pq, qp carry nu^(n-1) ; pp carries nu^(n-2) (absent if negative)"""
    a, b, c, cp, e = sp.symbols('a%d b%d c%d cp%d e%d' % ((n,) * 5))
    A_ = a * nu**n
    E_ = e * nu**n
    C_ = c * nu**(n - 1) if n >= 1 else 0
    Cp_ = cp * nu**(n - 1) if n >= 1 else 0
    B_ = b * nu**(n - 2) if n >= 2 else 0
    return (A_, B_, C_, Cp_, E_), [a, b, c, cp, e]

okB = True
for n in range(0, 5):
    Tn, syms = general_degree_n(n)
    cons = [sp.expand(x) for x in left_q(Tn) + right_q(Tn)]
    # each constraint is a polynomial in nu, Q; require all coefficients to vanish
    eqs = []
    for x in cons:
        if x == 0:
            continue
        eqs += sp.Poly(x, nu).coeffs()          # coefficients may depend on Q (Q is a parameter, not a variable)
    unknowns = [s for s in syms if any(s in sp.sympify(x).free_symbols for x in Tn)]
    s_ = sp.solve(eqs, unknowns, dict=True)
    s_ = s_[0] if s_ else {}
    Tn_t = tuple(sp.simplify(sp.sympify(x).subs(s_)) for x in Tn)
    T2n = sp.simplify(Q**4 * ((D - 1) * S1(Tn_t) - nu**2 / Q**2 * S2(Tn_t)) / ((D - 2) * nu**3))
    print("(B) n=%d: free coefficients after transversality: %s ; T2 = %s" % (n, sorted(set().union(*[sp.sympify(x).free_symbols for x in Tn_t]) - {nu, Q}, key=str), T2n))
    if n in (0, 1):
        okB = okB and (T2n == 0)
print("(B) beta_0 = beta_1 = 0 for the most general transverse polynomial tensors (symbolic D):", okB)

# ---------------------------------------------------------------- (C) tree-level quark Compton amplitude in D dims
# (1/2) Tr[pslash gamma^mu kslash gamma^nu] = 2 (p^mu k^nu + p^nu k^mu - g^{mu nu} p.k), Tr 1 = 4, D-independent
# s-channel k = p+q, denominator (p+q)^2 = 2nu - Q^2 ; u-channel: mu<->nu, k = p-q, denominator (p-q)^2 = -2nu - Q^2
def trace_tensor(kp, kq):
    """2 (p^mu k^nu + p^nu k^mu - g p.k) with k = kp p + kq q, as coefficients over {g,pp,pq,qp,qq}"""
    pk = kq * nu                     # p.k = kp p.p + kq p.q
    return (-2 * pk, 2 * (kp + kp), 2 * kq, 2 * kq, 0)
Ts = trace_tensor(1, 1)
Tu = trace_tensor(1, -1)
Ttree = tuple(sp.simplify(a / (2 * nu - Q**2) + b / (-2 * nu - Q**2)) for a, b in zip(Ts, Tu))
transv = [sp.simplify(x) for x in left_q(Ttree) + right_q(Ttree)]
T2tree = sp.simplify(Q**4 * ((D - 1) * S1(Ttree) - nu**2 / Q**2 * S2(Ttree)) / ((D - 2) * nu**3))
T2tree_w = sp.simplify(T2tree.subs(nu, w * Q**2 / 2))
print("(C) tree level: transverse:", transv == [0, 0, 0, 0], "; T2 =", T2tree_w, "; D-independent:", sp.diff(T2tree_w, D) == 0,
      "; equals -4w/(1-w^2):", sp.simplify(T2tree_w + 4 * w / (1 - w**2)) == 0)
okC = transv == [0, 0, 0, 0] and sp.diff(T2tree_w, D) == 0 and sp.simplify(T2tree_w + 4 * w / (1 - w**2)) == 0

# ---------------------------------------------------------------- (D) gluon polarisation tensor
# d_ab = -g_ab + (p_a q_b + q_a p_b)/nu - q^2 p_a p_b / nu^2  with q^2 = -Q^2
dcoef = (-1, Q**2 / nu**2, 1 / nu, 1 / nu, 0)     # over {g, pp, pq, qp, qq}
dp_left = left_q  # reuse structure: contraction with p instead of q
def contract_p_right(Tc):
    A_, B_, C_, Cp_, E_ = Tc
    # T^{ab} p_b: g -> p^a ; pp -> 0 ; pq -> nu p^a ; qp -> 0 ; qq -> nu q^a
    return sp.simplify(A_ + C_ * nu), sp.simplify(E_ * nu)
print("(D) d.p (coefficients of p^a, q^a):", contract_p_right(dcoef), "; d.q:", right_q(dcoef),
      "; trace:", sp.simplify(S2(dcoef)))
okD = contract_p_right(dcoef) == (0, 0) and right_q(dcoef) == (0, 0) and sp.simplify(S2(dcoef) - (2 - D)) == 0

# ---------------------------------------------------------------- (E) evanescent Gamma^(n) contraction
def euclid_gammas(Dim):
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    k = Dim // 2
    gs = []
    for j in range(k):
        for s in (s1, s2):
            m = np.array([[1]], dtype=complex)
            for l in range(k):
                m = np.kron(m, s3 if l < j else (s if l == j else I2))
            gs.append(m)
    if Dim % 2 == 1:
        m = np.array([[1]], dtype=complex)
        for l in range(k):
            m = np.kron(m, s3)
        gs.append(m)
    return gs[:Dim]

def antisym_product(gs, idx):
    """normalised antisymmetrised product gamma^[i1..in] (average over permutations with sign)"""
    n = len(idx)
    dim = gs[0].shape[0]
    tot = np.zeros((dim, dim), dtype=complex)
    for perm in itertools.permutations(range(n)):
        sign = np.linalg.det(np.eye(n)[list(perm)])
        m = np.eye(dim, dtype=complex)
        for p_ in perm:
            m = m @ gs[idx[p_]]
        tot += sign * m
    import math
    return tot / math.factorial(n)

okE = True
for Dim in (4, 5, 6, 7):
    gs = euclid_gammas(Dim)
    cliff = all(np.allclose(gs[a] @ gs[b] + gs[b] @ gs[a], 2 * (a == b) * np.eye(gs[0].shape[0])) for a in range(Dim) for b in range(Dim))
    for n in (3, 5):
        tot = np.zeros_like(gs[0])
        for idx in itertools.product(range(Dim), repeat=n):
            if len(set(idx)) < n:
                continue
            G = antisym_product(gs, idx)
            tot += G @ G
        pred = (-1) ** (n * (n - 1) // 2) * np.prod([Dim - k for k in range(n)])
        ok = np.allclose(tot, pred * np.eye(gs[0].shape[0]))
        okE = okE and ok and cliff
        print("(E) D=%d n=%d: Clifford ok=%s ; Gamma^(n).Gamma^(n) = %s * 1 (predicted (-1)^{n(n-1)/2} D!/(D-n)! = %s) : %s"
              % (Dim, n, cliff, np.round(tot[0, 0].real, 6), pred, ok))
print("(E) n=5 contraction polynomial: ", sp.factor((-1) ** (5 * 4 // 2) * sp.prod([D - k for k in range(5)])),  # sign fixed (X3 final): (-1)^10 = +1
      " -> vanishes at D = 4 only (evanescent); tree vertices of Gamma^(5)xGamma^(5) four-quark operators are O(D-4)")

print("\nSUMMARY  A:%s  B:%s  C:%s  D:%s  E:%s" % (okA, okB, okC, okD, okE))
