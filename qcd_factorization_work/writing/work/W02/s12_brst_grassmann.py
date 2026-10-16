"""W02 / Ch2 + App J check s12: BRST algebra with an explicit Grassmann algebra (SU(2): f = epsilon, t = sigma/2), at one
spacetime point; derivatives of fields are independent generators, s commutes with d.  s acts from the LEFT as an odd
derivation.  Conventions (def:prelim-brst):
   s A^a_mu = (D_mu c)^a = d_mu c^a + g f^{abc} A^b_mu c^c,   s c^a = -(g/2) f^{abc} c^b c^c,
   s psi = i g c^a t^a psi,   s psibar = -i g c^a psibar t^a,   s cbar^a = B^a,   s B^a = 0.
Checks: s^2 = 0 on A, dA, c, dc, psi, psibar, cbar, B; s(psibar psi) = 0 (fixes the sign of s psibar);
s G^a_{mu nu} = g f^{abc} G^b_{mu nu} c^c (hence s(G^a G^a) = 0); s(D_mu psi) = i g c^a t^a D_mu psi;
s Psi = B.dA + (xi/2) B B - cbar^a d^mu (D_mu c)^a  with Psi = cbar^a (d.A^a + (xi/2) B^a), i.e. L_gf + L_FP;
d L/d xi = (1/2) B B = s((1/2) cbar^a B^a).
Run: python3 -I s12_brst_grassmann.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
g, xi = sp.symbols('g xi')
NA = 3; NC = 2; MU = range(4)
eta = [1, -1, -1, -1]
f = lambda a, b, c: sp.LeviCivita(a, b, c)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
t = [s_ / 2 for s_ in sig]
# ---------------- odd generators ----------------
odd_names = []
for a in range(NA): odd_names.append(f'c{a}')
for a in range(NA):
    for m in MU: odd_names.append(f'dc{a}_{m}')
for a in range(NA):
    for m in MU:
        for n in MU:
            if m <= n: odd_names.append(f'ddc{a}_{m}{n}')
for i in range(NC): odd_names.append(f'psi{i}')
for i in range(NC):
    for m in MU: odd_names.append(f'dpsi{i}_{m}')
for i in range(NC): odd_names.append(f'psib{i}')
for a in range(NA): odd_names.append(f'cb{a}')
ORD = {n: k for k, n in enumerate(odd_names)}
def ddc(a, m, n): return f'ddc{a}_{min(m,n)}{max(m,n)}'
# ---------------- even variables ----------------
A = [[sp.Symbol(f'A{a}_{m}') for m in MU] for a in range(NA)]
dA = [[[sp.Symbol(f'dA{a}_{m}{n}') for n in MU] for m in MU] for a in range(NA)]    # dA[a][m][n] = d_n A^a_m
B = [sp.Symbol(f'B{a}') for a in range(NA)]
EVEN = [x for row in A for x in row] + [x for r1 in dA for r2 in r1 for x in r2] + B
# ---------------- algebra ----------------
def canon(mono):
    """sort a tuple of odd generators; return (sign, sorted) or (0, None) if a generator repeats"""
    if len(set(mono)) < len(mono): return 0, None
    lst = list(mono); sign = 1
    for i in range(len(lst)):                 # bubble sort counting transpositions
        for j in range(len(lst) - 1 - i):
            if ORD[lst[j]] > ORD[lst[j + 1]]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]; sign = -sign
    return sign, tuple(lst)
def add(X, Y):
    Z = dict(X)
    for k, v in Y.items():
        Z[k] = sp.expand(Z.get(k, 0) + v)
    return {k: v for k, v in Z.items() if v != 0}
def scal(X, c): return {k: sp.expand(c * v) for k, v in X.items() if sp.expand(c * v) != 0}
def mul(X, Y):
    Z = {}
    for k1, v1 in X.items():
        for k2, v2 in Y.items():
            sgn, mono = canon(k1 + k2)
            if sgn: Z = add(Z, {mono: sgn * v1 * v2})
    return Z
def odd(name): return {(name,): sp.Integer(1)}
def even(expr): return {(): sp.expand(expr)} if sp.expand(expr) != 0 else {}
# ---------------- s on generators ----------------
S_even = {}; S_odd = {}
for a in range(NA):
    for m in MU:
        val = odd(f'dc{a}_{m}')
        for b in range(NA):
            for c in range(NA):
                if f(a, b, c) != 0: val = add(val, scal(odd(f'c{c}'), g * f(a, b, c) * A[b][m]))
        S_even[A[a][m]] = val
        for n in MU:      # s(d_n A^a_m) = d_n d_m c^a + g f^{abc}(d_n A^b_m c^c + A^b_m d_n c^c)
            val = odd(ddc(a, m, n))
            for b in range(NA):
                for c in range(NA):
                    if f(a, b, c) != 0:
                        val = add(val, scal(odd(f'c{c}'), g * f(a, b, c) * dA[b][m][n]))
                        val = add(val, scal(odd(f'dc{c}_{n}'), g * f(a, b, c) * A[b][m]))
            S_even[dA[a][m][n]] = val
for a in range(NA):
    S_even[B[a]] = {}
    val = {}
    for b in range(NA):
        for c in range(NA):
            if f(a, b, c) != 0: val = add(val, scal(mul(odd(f'c{b}'), odd(f'c{c}')), -g / 2 * f(a, b, c)))
    S_odd[f'c{a}'] = val
    for m in MU:   # s(d_m c^a) = -(g/2) f^{abc}(d_m c^b c^c + c^b d_m c^c)
        val = {}
        for b in range(NA):
            for c in range(NA):
                if f(a, b, c) != 0:
                    val = add(val, scal(mul(odd(f'dc{b}_{m}'), odd(f'c{c}')), -g / 2 * f(a, b, c)))
                    val = add(val, scal(mul(odd(f'c{b}'), odd(f'dc{c}_{m}')), -g / 2 * f(a, b, c)))
        S_odd[f'dc{a}_{m}'] = val
        for n in MU:
            if m > n: continue
            val = {}
            for b in range(NA):
                for c in range(NA):
                    if f(a, b, c) != 0:
                        for x, y in [(ddc(b, m, n), f'c{c}'), (f'dc{b}_{m}', f'dc{c}_{n}'), (f'dc{b}_{n}', f'dc{c}_{m}'), (f'c{b}', ddc(c, m, n))]:
                            val = add(val, scal(mul(odd(x), odd(y)), -g / 2 * f(a, b, c)))
            S_odd[ddc(a, m, n)] = val
    S_odd[f'cb{a}'] = even(B[a])
for i in range(NC):
    val = {}
    for a in range(NA):
        for j in range(NC):
            if t[a][i, j] != 0: val = add(val, scal(mul(odd(f'c{a}'), odd(f'psi{j}')), sp.I * g * t[a][i, j]))
    S_odd[f'psi{i}'] = val
    for m in MU:    # s(d_m psi) = i g t (d_m c psi + c d_m psi)
        val = {}
        for a in range(NA):
            for j in range(NC):
                if t[a][i, j] != 0:
                    val = add(val, scal(mul(odd(f'dc{a}_{m}'), odd(f'psi{j}')), sp.I * g * t[a][i, j]))
                    val = add(val, scal(mul(odd(f'c{a}'), odd(f'dpsi{j}_{m}')), sp.I * g * t[a][i, j]))
        S_odd[f'dpsi{i}_{m}'] = val
    val = {}
    for a in range(NA):
        for j in range(NC):
            if t[a][j, i] != 0: val = add(val, scal(mul(odd(f'c{a}'), odd(f'psib{j}')), -sp.I * g * t[a][j, i]))
    S_odd[f'psib{i}'] = val
def s_op(X):
    out = {}
    for mono, coeff in X.items():
        for v in coeff.free_symbols:
            if v in S_even:
                dv = sp.diff(coeff, v)
                if dv != 0: out = add(out, mul(scal(S_even[v], dv), {mono: sp.Integer(1)}))
        for j, x in enumerate(mono):
            sign = (-1)**j
            term = mul(mul({mono[:j]: sp.Integer(1)}, S_odd[x]), {mono[j + 1:]: sp.Integer(1)})
            out = add(out, scal(term, sign * coeff))
    return out
# ---------------- s^2 = 0 ----------------
tests = [('A^a_mu', even(A[a][m])) for a in range(NA) for m in (0, 2)] + [('d_n A^a_mu', even(dA[1][2][3]))]
tests += [('c^a', odd(f'c{a}')) for a in range(NA)] + [('d_mu c^a', odd('dc2_1'))]
tests += [('psi', odd('psi0')), ('psi', odd('psi1')), ('psibar', odd('psib0')), ('cbar', odd('cb1')), ('B', even(B[2]))]
ok = True; bad = []
for name, X in tests:
    r = s_op(s_op(X))
    if r: ok = False; bad.append(name)
report(ok, 's^2 = 0 on A, d A, c, d c, psi, psibar, cbar, B (SU(2), explicit Grassmann algebra)', ','.join(bad))
# s(psibar psi) = 0 (sign of s psibar)
X = {}
for i in range(NC): X = add(X, mul(odd(f'psib{i}'), odd(f'psi{i}')))
report(s_op(X) == {}, 's(psibar_i psi_i) = 0 with s psibar = -i g c^a psibar t^a (the sign is fixed by gauge invariance)')
# s G = g f G c
def G(a, m, n):
    expr = dA[a][n][m] - dA[a][m][n]
    for b in range(NA):
        for c in range(NA):
            expr += g * f(a, b, c) * A[b][m] * A[c][n]
    return expr
ok = True
for a in range(NA):
    for (m, n) in [(0, 1), (2, 3), (1, 3)]:
        lhs = s_op(even(G(a, m, n)))
        rhs = {}
        for b in range(NA):
            for c in range(NA):
                if f(a, b, c) != 0: rhs = add(rhs, scal(odd(f'c{c}'), g * f(a, b, c) * G(b, m, n)))
        ok &= (add(lhs, scal(rhs, -1)) == {})
report(ok, 's G^a_{mu nu} = g f^{abc} G^b_{mu nu} c^c (so s(G^a G^a) = 2 g f^{abc} G^a G^b c^c = 0)')
GG = sum(G(a, 0, 1) * G(a, 0, 1) for a in range(NA))
report(s_op(even(GG)) == {}, 's(G^a_{01} G^a_{01}) = 0 explicitly')
# covariance of D_mu psi
def Dpsi(i, m):
    X = odd(f'dpsi{i}_{m}')
    for a in range(NA):
        for j in range(NC):
            if t[a][i, j] != 0: X = add(X, scal(odd(f'psi{j}'), -sp.I * g * A[a][m] * t[a][i, j]))
    return X
ok = True
for i in range(NC):
    for m in (0, 3):
        lhs = s_op(Dpsi(i, m))
        rhs = {}
        for a in range(NA):
            for j in range(NC):
                if t[a][i, j] != 0: rhs = add(rhs, scal(mul(odd(f'c{a}'), Dpsi(j, m)), sp.I * g * t[a][i, j]))
        ok &= (add(lhs, scal(rhs, -1)) == {})
report(ok, 's(D_mu psi) = i g c^a t^a D_mu psi (so s(psibar Gamma D psi) = 0 for colour-singlet Gamma)')
# s Psi = L_gf + L_FP
dotA = [sum(eta[m] * dA[a][m][m] for m in MU) for a in range(NA)]       # d^mu A^a_mu
Psi = {}
for a in range(NA): Psi = add(Psi, mul(odd(f'cb{a}'), even(dotA[a] + xi / 2 * B[a])))
lhs = s_op(Psi)
Lgf = even(sum(B[a] * dotA[a] + xi / 2 * B[a]**2 for a in range(NA)))
def dDc(a):  # d^mu (D_mu c)^a = d^mu d_mu c^a + g f^{abc}(d^mu A^b_mu c^c + A^{b mu} d_mu c^c)
    X = {}
    for m in MU:
        X = add(X, scal(odd(ddc(a, m, m)), eta[m]))
        for b in range(NA):
            for c in range(NA):
                if f(a, b, c) != 0:
                    X = add(X, scal(odd(f'c{c}'), g * f(a, b, c) * eta[m] * dA[b][m][m]))
                    X = add(X, scal(odd(f'dc{c}_{m}'), g * f(a, b, c) * eta[m] * A[b][m]))
    return X
LFP = {}
for a in range(NA): LFP = add(LFP, scal(mul(odd(f'cb{a}'), dDc(a)), -1))
report(add(lhs, scal(add(Lgf, LFP), -1)) == {}, 's Psi = B^a d.A^a + (xi/2) B^a B^a - cbar^a d^mu(D_mu c)^a = L_gf + L_FP,  Psi = cbar^a(d.A^a + (xi/2)B^a)')
# s L_FP? (s^2 Psi = 0): s(L_gf + L_FP) = 0
report(s_op(add(Lgf, LFP)) == {}, 's(L_gf + L_FP) = s^2 Psi = 0')
# xi derivative
Psi_xi = {}
for a in range(NA): Psi_xi = add(Psi_xi, mul(odd(f'cb{a}'), even(B[a] / 2)))
report(add(s_op(Psi_xi), scal(even(sum(B[a]**2 for a in range(NA)) / 2), -1)) == {}, 'd(L_gf)/d xi = (1/2) B^a B^a = s((1/2) cbar^a B^a)')
# eliminating B: B = -d.A/xi gives L_gf = -(d.A)^2/(2 xi)
Bsol = [-dotA[a] / xi for a in range(NA)]
Lgf_e = sum(Bsol[a] * dotA[a] + xi / 2 * Bsol[a]**2 for a in range(NA))
report(sp.simplify(Lgf_e + sum(dotA[a]**2 for a in range(NA)) / (2 * xi)) == 0, 'eliminating B^a = -d.A^a/xi: L_gf = -(d.A^a)^2/(2 xi)')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
