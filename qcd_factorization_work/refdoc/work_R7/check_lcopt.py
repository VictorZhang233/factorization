"""Check Lemma E.15 / eq. (E.13) of the reference document (LCOPT from Feynman integrals).

For a graph J (vertices, lines oriented along l^+>0), reduced numerators N_l = 1, finite eta0:
  I_J/(2 pi delta(sum q)) = int prod_loops du/(2pi) prod_l i/(2 l^+ (l^-(u) - E_l)),
  E_l = (lT^2+m^2 - i eta0)/(2 l^+)
should equal
  prod_l 1/(2 l^+) * sum_{pi in Ord(J)} prod_{i=1}^{N-1} i/D_i,
  D_i = Q_i - sum_{l in S_i} E_l,  Q_i = sum_{j<=i} q_{pi(j)}.
Loop integrals: first loop variable by exact residues (closing in the UHP), remaining by mpmath quadrature.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
mp.mp.dps = 30

def spanning_tree_and_loops(N, lines):
    # simple union-find spanning tree; returns tree line indices and chord indices
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    tree, chords = [], []
    for idx, (t, h) in enumerate(lines):
        rt, rh = find(t), find(h)
        if rt != rh:
            parent[rt] = rh; tree.append(idx)
        else:
            chords.append(idx)
    return tree, chords

def line_minus_linear_forms(N, lines, q):
    """Express each line minus component as  a_l . u + b_l  (u = chord variables) using
    vertex conservation  q_v + sum_{h(l)=v} l^- - sum_{t(l)=v} l^- = 0 (last vertex dropped)."""
    tree, chords = spanning_tree_and_loops(N, lines)
    n = len(chords)
    L = len(lines)
    # unknowns: tree line minus components; equations: N-1 vertex conservations
    A = np.zeros((N - 1, len(tree)))
    Bu = np.zeros((N - 1, n))
    Bq = np.zeros(N - 1)
    for v in range(N - 1):
        Bq[v] = -q[v]
        for j, lt in enumerate(tree):
            t, h = lines[lt]
            if h == v: A[v, j] += 1
            if t == v: A[v, j] -= 1
        for c, lc in enumerate(chords):
            t, h = lines[lc]
            if h == v: Bu[v, c] -= 1
            if t == v: Bu[v, c] += 1
    Ainv = np.linalg.inv(A)
    forms = [None] * L
    for c, lc in enumerate(chords):
        a = np.zeros(n); a[c] = 1.0
        forms[lc] = (a, 0.0)
    Tu = Ainv @ Bu
    Tq = Ainv @ Bq
    for j, lt in enumerate(tree):
        forms[lt] = (Tu[j], Tq[j])
    return forms, n

def direct_integral(N, lines, plus, ET, q, eta):
    forms, n = line_minus_linear_forms(N, lines, q)
    E = [mp.mpc(ET[l], -eta) / (2 * plus[l]) for l in range(len(lines))]
    # integrand: prod_l i/(2 l^+ (a_l.u + b_l - E_l)); as factors (coef, a, c) meaning 1/(a.u + c)
    pref = mp.mpf(1)
    for l in range(len(lines)):
        pref *= mp.mpc(0, 1) / (2 * plus[l])
    factors = [(np.array(forms[l][0], dtype=float), mp.mpf(forms[l][1]) - E[l]) for l in range(len(lines))]
    # integrate u_0 by residues in the UHP: integral du/(2pi) f = i * sum Res_UHP
    def after_first(urest):
        # urest: values for u_1..u_{n-1}
        tot = mp.mpc(0)
        lin = []
        for (a, c) in factors:
            const = c + sum(mp.mpf(a[j]) * urest[j - 1] for j in range(1, n))
            lin.append((mp.mpf(a[0]), const))
        dep = [k for k, (a0, c) in enumerate(lin) if a0 != 0]
        assert len(dep) >= 2, "u0 appears in fewer than 2 factors"
        for k in dep:
            a0, c = lin[k]
            pole = -c / a0
            if mp.im(pole) > 0:
                res = 1 / a0
                for m, (am, cm) in enumerate(lin):
                    if m == k: continue
                    res /= (am * pole + cm)
                tot += res
        return mp.mpc(0, 1) * tot
    if n == 1:
        return pref * after_first([])
    elif n == 2:
        f = lambda u1: after_first([u1])
        val = mp.quad(f, [-mp.inf, -50, -5, -1, 0, 1, 5, 50, mp.inf]) / (2 * mp.pi)
        return pref * val
    else:
        raise NotImplementedError

def lcopt_sum(N, lines, plus, ET, q, eta):
    E = [mp.mpc(ET[l], -eta) / (2 * plus[l]) for l in range(len(lines))]
    tot = mp.mpc(0)
    nord = 0
    for perm in itertools.permutations(range(N)):
        pos = {v: i for i, v in enumerate(perm)}
        if any(pos[t] >= pos[h] for (t, h) in lines):
            continue
        nord += 1
        term = mp.mpc(1)
        Q = mp.mpf(0)
        for i in range(N - 1):
            Q += q[perm[i]]
            S = [l for l, (t, h) in enumerate(lines) if pos[t] <= i < pos[h]]
            assert len(S) > 0
            D = Q - sum(E[l] for l in S)
            term *= mp.mpc(0, 1) / D
        tot += term
    pref = mp.mpf(1)
    for l in range(len(lines)):
        pref *= 1 / (2 * mp.mpf(plus[l]))
    return pref * tot, nord

rng = np.random.default_rng(7)
graphs = {
    'bubble (2 lines v0->v1)': (2, [(0, 1), (0, 1)]),
    'triangle acyclic': (3, [(0, 1), (0, 2), (1, 2)]),
    'box (2 orderings)': (4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
    'directed 3-cycle (Ord empty)': (3, [(0, 1), (1, 2), (2, 0)]),
    'two-loop: box + diagonal 0->3': (4, [(0, 1), (0, 2), (1, 3), (2, 3), (0, 3)]),
    'two-loop kite (1 ordering)': (4, [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]),
    'two-loop sunset': (2, [(0, 1), (0, 1), (0, 1)]),
    'two-loop 5 vertices': (5, [(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (3, 4)]),
}
allok = True
for name, (N, lines) in graphs.items():
    L = len(lines)
    plus = [float(x) for x in rng.uniform(0.3, 2.0, L)]
    ET = [float(x) for x in rng.uniform(0.2, 1.5, L)]
    qv = list(rng.uniform(-1.0, 1.0, N - 1))
    qv.append(-sum(qv))
    qv = [float(x) for x in qv]
    eta = 0.37
    d = direct_integral(N, lines, plus, ET, qv, eta)
    s, nord = lcopt_sum(N, lines, plus, ET, qv, eta)
    rel = abs(d - s) / max(abs(s), mp.mpf('1e-30')) if nord > 0 else abs(d)
    ok = rel < 1e-10
    allok &= ok
    print(f"{name:34s} |Ord|={nord}  direct={mp.nstr(d, 12)}  LCOPT={mp.nstr(s, 12)}  diff={mp.nstr(rel, 3)}  {'PASS' if ok else 'FAIL'}")
print('ALL PASS' if allok else 'SOME FAIL')
