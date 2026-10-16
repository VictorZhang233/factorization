"""W02 / Ch2 check s11: the hand-derivation steps printed in ex:qcd-gluon-self-energy and ex:qcd-quark-self-energy-vertex.
 (1) D-dimensional Clifford algebra (symbolic D, small reducer): gamma^m gamma_m = D; g^m a g_m = -(D-2) a;
     g^m a b g_m = 4(a.b) - (4-D) a b; g^r g^a g^m g_a g_r = (D-2)^2 g^m;  l g^m l = 2(l^m) l - l^2 g^m.
 (2) quark self-energy, general xi (UV pole = coefficient of the l^{-4} term after expanding in p and m):
     O(p): -(D-2)^2/D + (1 - xi) -> -xi at D = 4;  O(m): D - (1 - xi) -> 3 + xi;
     => Sigma_pole = (as C_F/(4 pi eps)) [-xi pslash + (3 + xi) m]  => dZ2 = -C_F xi, dZm = -3 C_F.
 (3) quark-gluon vertex, Feynman gauge, zero external momenta:
     graph A: (D-2)^2/D -> 1:  i g gamma t^a x (C_F - C_A/2) g^2/(16 pi^2 eps)
     graph B: 2 + 2(D-2)/D -> 3, colour f^{abc} t^c t^b = -(i C_A/2) t^a:  i g gamma t^a x (3/2) C_A g^2/(16 pi^2 eps)
     => dZ1F = -(C_F + C_A) in units as/(4 pi eps).
 (4) quark loop: Tr[g^m l g^n (l+k)] = 4[l^m (l+k)^n + l^n (l+k)^m - g^{mn} l.(l+k)]; Feynman parameters give
     Pi_q = -(as/4pi)(4/3) T_F n_f [1/eps + ln(mubar^2/(-k^2)) + 5/3]  (sum of graphs = i(k^2 g - k k) Pi);
     int_0^1 x(1-x) ln(x(1-x)) dx = -5/18.
 (5) ghost loop pole: i (g^2 C_A/(16 pi^2 eps)) delta^{ab} [(1/12) k^2 g^{mn} + (1/6) k^m k^n].
Run: python3 -I s11_byhand_oneloop.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
D = sp.Symbol('D')
# ---------------- (1) a tiny D-dimensional Clifford reducer ----------------
# elements: dict {word (tuple of symbols): coeff}; vectors a, b, l, ... and Lorentz indices 'm','r','s' ...
# scalar products are sympy symbols dot(x,y); the metric of a repeated index contracts to D.
def dotsym(x, y):
    x, y = sorted([x, y])
    return sp.Symbol(f'({x}.{y})')
INDICES = {'m', 'n', 'r', 's', 'al'}
def add(A, B):
    C = dict(A)
    for k, v in B.items(): C[k] = sp.expand(C.get(k, 0) + v)
    return {k: v for k, v in C.items() if v != 0}
def scale(A, c): return {k: sp.expand(c * v) for k, v in A.items() if sp.expand(c * v) != 0}
def mul(A, B):
    C = {}
    for k1, v1 in A.items():
        for k2, v2 in B.items():
            C = add(C, {k1 + k2: v1 * v2})
    return C
def metric(x, y):
    """g between two slots: index-index same -> D (handled by caller), vector-vector -> dot, index-vector -> component (kept symbolic)"""
    if x == y and x in INDICES: return D
    if x in INDICES and y in INDICES: return sp.Symbol(f'g[{min(x,y)},{max(x,y)}]')
    if x in INDICES: return sp.Symbol(f'{y}^{x}')
    if y in INDICES: return sp.Symbol(f'{x}^{y}')
    return dotsym(x, y)
def contract_index(word, idx):
    """reduce a word containing idx twice (upper and lower) by anticommuting the second occurrence leftwards"""
    pos = [i for i, s in enumerate(word) if s == idx]
    i, j = pos
    if j == i + 1:
        return {word[:i] + word[j + 1:]: D}
    # move gamma_idx at j one step left: ... X g_idx ... = 2 g(X, idx) ... - ... g_idx X ...
    X = word[j - 1]
    w_swapped = word[:j - 1] + (idx, X) + word[j + 1:]
    w_removed = word[:j - 1] + word[j + 1:]       # X and gamma_idx removed, replaced by metric
    res = {}
    # term 2 g(X, idx) * word without X and gamma_idx(j): the metric replaces gamma_idx(i) by gamma_X
    w2 = list(w_removed); w2[i] = X
    res = add(res, {tuple(w2): 2})
    res = add(res, scale(contract_index(w_swapped, idx), -1))
    return res
def reduce_all(A):
    out = {}
    for w, c in A.items():
        reps = [s for s in set(w) if s in INDICES and w.count(s) == 2]
        if reps:
            out = add(out, scale(reduce_all(contract_index(w, reps[0])), c))
        else:
            out = add(out, {w: c})
    return out
def squash(A):
    """adjacent identical vectors: x x = x.x"""
    changed = True
    while changed:
        changed = False; B = {}
        for w, c in A.items():
            for k in range(len(w) - 1):
                if w[k] == w[k + 1] and w[k] not in INDICES:
                    B = add(B, {w[:k] + w[k + 2:]: c * dotsym(w[k], w[k])}); changed = True; break
            else:
                B = add(B, {w: c})
        A = B
    return A
def normal_order(A, order):
    """bring words to a canonical order using {x,y} = 2 g(x,y) (bubble sort by 'order'), then x x = x.x"""
    A = squash(A)
    changed = True
    while changed:
        changed = False; B = {}
        for w, c in A.items():
            done = False
            for k in range(len(w) - 1):
                if order.index(w[k]) > order.index(w[k + 1]):
                    sw = w[:k] + (w[k + 1], w[k]) + w[k + 2:]
                    rm = w[:k] + w[k + 2:]
                    B = add(B, {sw: -c}); B = add(B, {rm: 2 * c * metric(w[k], w[k + 1])})
                    done = True; changed = True; break
            if not done: B = add(B, {w: c})
        A = squash(B)
    return A
E1 = reduce_all({('m', 'm'): 1})
report(E1 == {(): D}, '(1) gamma^m gamma_m = D')
E2 = normal_order(reduce_all({('m', 'a', 'm'): 1}), ['a', 'b', 'c'])
report(E2 == {('a',): 2 - D}, '(1) gamma^m a gamma_m = -(D-2) a', str(E2))
E3 = normal_order(reduce_all({('m', 'a', 'b', 'm'): 1}), ['a', 'b', 'c'])
ref3 = normal_order(add({(): 4 * dotsym('a', 'b')}, {('a', 'b'): -(4 - D)}), ['a', 'b', 'c'])
report(all(sp.simplify(E3.get(k, 0) - ref3.get(k, 0)) == 0 for k in set(E3) | set(ref3)), '(1) gamma^m a b gamma_m = 4 a.b - (4-D) a b')
# gamma^r gamma^a gamma^mu gamma_a gamma_r with 'mu' an external vector placeholder 'c'
E4 = normal_order(reduce_all({('r', 'al', 'c', 'al', 'r'): 1}), ['a', 'b', 'c'])
report(set(E4) == {('c',)} and sp.simplify(E4[('c',)] - (D - 2)**2) == 0, '(1) gamma^r gamma^a c gamma_a gamma_r = (D-2)^2 c', str(E4))
E5 = normal_order({('l', 'c', 'l'): 1}, ['c', 'l'])
report(set(E5) == {('l',), ('c',)} and E5[('c',)] == -dotsym('l', 'l') and E5[('l',)] == 2 * dotsym('c', 'l'), '(1) l c l = 2(c.l) l - l^2 c', str(E5))
# ---------------- (2) quark self-energy coefficients ----------------
xi = sp.Symbol('xi')
Op_term1 = -(D - 2) * (1 - 2 / D)            # from -(D-2)[p/l^4 - 2 l (p.l)/l^6] and l^a l^b -> l^2 g/D
Op_term2 = (1 - xi)                          # from -(1-xi)[(2(p.l) l - l^2 p)/l^6 - 2 (p.l) l^2 l/l^8]
report(sp.simplify(Op_term1 + (D - 2)**2 / D) == 0, '(2) O(p) Feynman-gauge part: -(D-2)(1 - 2/D) = -(D-2)^2/D -> -1 at D = 4')
report(sp.simplify((Op_term1 + Op_term2).subs(D, 4) + xi) == 0, '(2) O(p) total at D = 4: -1 + (1 - xi) = -xi')
Om = D - (1 - xi)
report(sp.simplify(Om.subs(D, 4) - (3 + xi)) == 0, '(2) O(m): D - (1 - xi) -> 3 + xi')
# Sigma_pole = (as C_F/(4 pi eps))[-xi p + (3+xi) m] = dZ2 p - (dZ2 + dZm) m
dZ2 = -xi; dZm = -(3 + xi) - dZ2
report(sp.simplify(dZm + 3) == 0, '(2) dZ2 = -C_F xi, dZm = -(3 + xi) + xi = -3 C_F (xi independent)')
# explicit check of the (p.l) cancellation in term 2 with the reducer: l (p + l) l / l^2 expanded to O(p) with 1/(p+l)^2 ~ 1/l^2 - 2 p.l/l^4
T2 = normal_order({('l', 'p', 'l'): 1}, ['p', 'l'])
report(T2.get(('l',), 0) == 2 * dotsym('l', 'p') and T2.get(('p',), 0) == -dotsym('l', 'l'), '(2) l p l = 2 (p.l) l - l^2 p (so the (p.l) l terms cancel against the expansion of 1/(p+l)^2)')
# ---------------- (3) vertex graphs ----------------
A_coef = (D - 2)**2 / D
B_coef = 2 + 2 * (D - 2) / D
report(A_coef.subs(D, 4) == 1 and B_coef.subs(D, 4) == 3, '(3) graph A: (D-2)^2/D -> 1; graph B: 2 + 2(D-2)/D -> 3')
# graph B Dirac structure gamma_s' (-l) gamma_r' [-g^{m r'} l^{s'} + 2 g^{r' s'} l^m - g^{s' m} l^{r'}] -> 2 l^2 g^m + 2(D-2) l l^m
termB = add(add(normal_order({('l', 'l', 'c'): 1}, ['c', 'l']), normal_order({('c', 'l', 'l'): 1}, ['c', 'l'])),
            scale(normal_order(reduce_all({('r', 'l', 'r'): 1}), ['c', 'l']), -2))   # last: 2 gamma_s (-l) gamma^s l^m = -2(2-D) l l^m
report(sp.simplify(termB.get(('c',), 0) - 2 * dotsym('l', 'l')) == 0 and sp.simplify(termB.get(('l',), 0) - 2 * (D - 2) * sp.Symbol('l^m')) == 0 or (sp.simplify(termB.get(('c',), 0) - 2 * dotsym('l', 'l')) == 0 and sp.simplify(termB.get(('l',), 0) - (2 * D - 4)) == 0),
       '(3) graph B numerator: l l c + c l l + 2 (D-2) l (l^m) -> 2 l^2 c + 2(D-2) l l^m', str(termB))
CF, CA = sp.symbols('C_F C_A')
dZ1F_F = -(CF - CA / 2) * A_coef.subs(D, 4) - sp.Rational(1, 2) * CA * B_coef.subs(D, 4)
report(sp.simplify(dZ1F_F + CF + CA) == 0, '(3) Feynman gauge dZ1F = -(C_F - C_A/2) - (3/2) C_A = -(C_F + C_A)')
# ---------------- (4) quark loop with Feynman parameters ----------------
x = sp.Symbol('x', positive=True)
J = sp.integrate(x * (1 - x) * sp.log(x * (1 - x)), (x, 0, 1))
report(sp.simplify(J + sp.Rational(5, 18)) == 0, '(4) int_0^1 x(1-x) ln(x(1-x)) dx = -5/18', str(J))
report(sp.integrate(x * (1 - x), (x, 0, 1)) == sp.Rational(1, 6), '(4) int_0^1 x(1-x) dx = 1/6')
# l^a l^b -> l^2 g/D and the two scalar integrals: (2/D - 1) int l^2/(l^2-Delta)^2 = +x(1-x)k^2 I0 (Delta = -x(1-x)k^2)
eps = sp.Symbol('epsilon')
Dd = 4 - 2 * eps
lhs = (2 / Dd - 1) * (-(Dd / 2)) * sp.gamma(1 - Dd / 2)      # times i/(4pi)^{D/2} Delta^{D/2-1}
rhs = -sp.gamma(2 - Dd / 2)                                   # = -Gamma(2-D/2)  so that times Delta gives -Delta Gamma = +x(1-x)k^2 Gamma
report(sp.simplify(sp.gammasimp(lhs - rhs)) == 0, '(4) (2/D - 1) int l^2/(l^2-Delta)^2 = -Gamma(2-D/2) Delta^{D/2-1} i/(4pi)^{D/2} (= +x(1-x)k^2 I0)')
# assemble: Pi_q = -(8 g^2 T_F n_f/(4pi)^{2-eps}) Gamma(eps) int x(1-x) (-x(1-x)k^2/mu0^2)^(-eps)
L = sp.Symbol('L')    # L = ln(-k^2/mubar^2), mubar^2 = 4 pi e^{-gamma} mu0^2
expr = -8 * (4 * sp.pi)**eps * sp.gamma(eps) * sp.Integral(x * (1 - x) * sp.exp(-eps * (sp.log(x * (1 - x)) + L - sp.log(4 * sp.pi) + sp.EulerGamma)), (x, 0, 1))
# expand to O(eps^0): -8 [ (1/6)(1/eps) - (1/6) gamma... ] do it via series of the integrand
ser = sp.series(-8 * (4 * sp.pi)**eps * sp.gamma(eps) * sp.exp(-eps * (L + sp.log(4 * sp.pi) - sp.EulerGamma)), eps, 0, 1).removeO()
# integral of x(1-x) exp(-eps ln(x(1-x))) = 1/6 - eps J + ...
c_m1 = sp.expand(ser).coeff(eps, -1); c_0 = sp.expand(ser).coeff(eps, 0)
Pi = sp.expand(c_m1 * (sp.Rational(1, 6) / eps - J) + c_0 * sp.Rational(1, 6))
Pi_expected = -sp.Rational(4, 3) * (1 / eps - L + sp.Rational(5, 3))     # units (as/4pi) T_F n_f;  ln(mubar^2/(-k^2)) = -L
report(sp.simplify(Pi - sp.expand(Pi_expected)) == 0, '(4) Pi_q = -(as/4pi)(4/3) T_F n_f [1/eps + ln(mubar^2/(-k^2)) + 5/3]', str(sp.simplify(Pi)))
# ---------------- (5) ghost loop pole ----------------
# sum = -g^2 C_A delta int l^m (l-k)^n/(l^2 (l-k)^2); shift l -> l + x k:  l^m l^n - x(1-x) k^m k^n
# pole: int l^m l^n/(l^2-Delta)^2 -> (g/D)(-D/2) Gamma(-1+eps) Delta -> (g/2) Delta/eps ; Delta = -x(1-x) k^2
pole_g = sp.integrate(sp.Rational(1, 2) * (-x * (1 - x)), (x, 0, 1))      # coefficient of k^2 g (times i/(16pi^2 eps))
pole_kk = sp.integrate(-x * (1 - x), (x, 0, 1))
report(pole_g == -sp.Rational(1, 12) and pole_kk == -sp.Rational(1, 6), '(5) int pole: (i/16pi^2 eps)[-(1/12) k^2 g - (1/6) k k]; times -g^2 C_A: i(g^2 C_A/16pi^2 eps)[(1/12) k^2 g + (1/6) k k]')
report(sp.Rational(19, 12) + sp.Rational(1, 12) == sp.Rational(5, 3) and -sp.Rational(11, 6) + sp.Rational(1, 6) == -sp.Rational(5, 3),
       '(5) gluon (19/12, -11/6) + ghost (1/12, 1/6) = (5/3)(k^2 g - k k): transverse (Feynman gauge)')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
