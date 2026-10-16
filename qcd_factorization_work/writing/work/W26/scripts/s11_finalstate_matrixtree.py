# W26 / Ch23 -- s11: lem:yzliu-final-state (VF-YZL-12) and lem:yzliu-matrix-tree (Liu:2023pjb eq. (2.10), App. A)
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np

# ---------- (1) final-state sum identity ----------
# I_n = int dE/(2 pi i) e^{-nu|E|/sqrt2} [prod 1/(E-E_k-i eta) - prod 1/(E-E_k+i eta)] = sum_k e^{-nu E_k/sqrt2} prod_{j!=k} 1/(E_k-E_j)
mp.mp.dps = 30
def lhs(Es, nu, eta):
    def f(E):
        p1 = mp.mpf(1); p2 = mp.mpf(1)
        for Ek in Es:
            p1 *= 1/(E - Ek - 1j*eta); p2 *= 1/(E - Ek + 1j*eta)
        return mp.e**(-nu*abs(E)/mp.sqrt(2))*(p1 - p2)/(2j*mp.pi)
    pts = sorted(set([-mp.inf, mp.mpf(0)] + [Ek + d for Ek in Es for d in (-10*eta, -eta, 0, eta, 10*eta)] + [mp.inf]))
    return mp.quad(f, pts, maxdegree=10)
def rhs(Es, nu):
    s = mp.mpf(0)
    for k, Ek in enumerate(Es):
        pr = mp.mpf(1)
        for j, Ej in enumerate(Es):
            if j != k: pr *= 1/(Ek - Ej)
        s += mp.e**(-nu*Ek/mp.sqrt(2))*pr
    return s
random.seed(7)
for nE in (1, 2, 3, 4, 5):
    Es = [mp.mpf(random.uniform(0.3, 3.0)) for _ in range(nE)]
    nu = mp.mpf('0.8')
    L1 = lhs(Es, nu, mp.mpf('1e-6')); R = rhs(Es, nu)
    print('n=%d: lhs = %s ; rhs = %s ; |diff| = %.1e' % (nE, mp.nstr(L1, 12), mp.nstr(R, 12), abs(L1 - R)))
# partial fractions (exact, sympy) for n=3, and the i0 -> 2 pi i delta mechanism
import sympy as sp
E = sp.Symbol('E'); e = sp.symbols('e1:4')
lhs_pf = sp.prod([1/(E - ek) for ek in e])
rhs_pf = sum(sp.prod([1/(e[k] - e[j]) for j in range(3) if j != k])/(E - e[k]) for k in range(3))
print('partial fractions n=3:', sp.simplify(lhs_pf - rhs_pf) == 0)

# ---------- (2) coordinate-space parametric functions: Schur complement vs spanning-tree formula, positivity ----------
# P_ee' = d_eV (d_VV)^{-1} d_Ve'  (Liu App. A eq. (A.6), rescaled alpha -> 1/(4 alpha)), claimed (A.7):
#  P_ee' = sum_{paths L: e -> e' through internal vertices} prod_{l in L} a_l * sum_{T in T1(G/(E u L))} prod_{l in T} a_l
#          / sum_{T in T1(G/E)} prod_{l in T} a_l
def spanning_tree_sum(nodes, edges, w):
    # Kirchhoff: weighted spanning trees of multigraph (nodes list, edges list of (u,v,idx))
    idx = {n: i for i, n in enumerate(nodes)}
    N = len(nodes)
    if N == 1: return 1.0
    Lm = np.zeros((N, N))
    for (u, v, k) in edges:
        if u == v: continue
        i, j = idx[u], idx[v]
        Lm[i, i] += w[k]; Lm[j, j] += w[k]; Lm[i, j] -= w[k]; Lm[j, i] -= w[k]
    return np.linalg.det(Lm[1:, 1:])
def contract(nodes, edges, group, newname):
    nn = [n for n in nodes if n not in group] + [newname]
    ne = []
    for (u, v, k) in edges:
        uu = newname if u in group else u; vv = newname if v in group else v
        if uu != vv: ne.append((uu, vv, k))       # tadpoles deleted
    return nn, ne
def simple_paths(edges, start, end, internal):
    # paths start -> end whose intermediate vertices are internal (and distinct), as edge-index lists
    adj = {}
    for (u, v, k) in edges:
        adj.setdefault(u, []).append((v, k)); adj.setdefault(v, []).append((u, k))
    out = []
    def dfs(node, visited, path):
        for (nb, k) in adj.get(node, []):
            if nb == end and node != start:
                out.append(path + [k]); continue
            if nb in internal and nb not in visited:
                dfs(nb, visited | {nb}, path + [k])
    dfs(start, {start}, [])
    return out
rng = np.random.default_rng(3)
maxdev = 0.0; minP = 1e9
for trial in range(40):
    nint = rng.integers(2, 6); next_ = 3
    internal = ['v%d' % i for i in range(nint)]; external = ['E%d' % i for i in range(next_)]
    nodes = internal + external
    edges = []; k = 0
    # random connected graph without external-external lines, each external vertex attached to >= 1 internal vertex
    for i in range(nint - 1):
        edges.append((internal[i], internal[i + 1], k)); k += 1
    for ext in external:
        edges.append((ext, internal[rng.integers(0, nint)], k)); k += 1
    for _ in range(rng.integers(0, 4)):
        u, v = rng.choice(internal, 2, replace=True)
        if u != v: edges.append((u, v, k)); k += 1
    w = {j: float(rng.uniform(0.2, 2.0)) for j in range(k)}
    # Laplacian of the full graph
    idx = {n: i for i, n in enumerate(nodes)}
    D = np.zeros((len(nodes), len(nodes)))
    for (u, v, j) in edges:
        a, b = idx[u], idx[v]
        D[a, a] += w[j]; D[b, b] += w[j]; D[a, b] -= w[j]; D[b, a] -= w[j]
    Vi = [idx[n] for n in internal]
    dVV = D[np.ix_(Vi, Vi)]
    detGE = spanning_tree_sum(*contract(nodes, edges, set(external), 'E*'), w)
    for (e1, e2) in itertools.combinations(external, 2):
        dEV1 = D[idx[e1], Vi]; dEV2 = D[idx[e2], Vi]
        Pschur = dEV1 @ np.linalg.solve(dVV, dEV2)
        num = 0.0
        for path in simple_paths(edges, e1, e2, set(internal)):
            verts = set()
            for j in path:
                u, v, _ = edges[[ee[2] for ee in edges].index(j)]
                verts |= {u, v}
            nn, ne = contract(nodes, edges, set(external) | (verts & set(internal)), 'X*')
            num += np.prod([w[j] for j in path])*spanning_tree_sum(nn, ne, w)
        Ptree = num/detGE
        maxdev = max(maxdev, abs(Pschur - Ptree)/max(1e-12, abs(Ptree)))
        minP = min(minP, Pschur)
print('random graphs: max relative deviation Schur complement vs path/spanning-tree formula = %.2e ; min P_ee\' = %.3e (>= 0)'
      % (maxdev, minP))
# also the Gaussian reduction identity: exponent after integrating internal vertices = -sum_{e<e'} P_ee' (x_e-x_e')^2
print('PASS' if maxdev < 1e-9 and minP >= 0 else 'FAIL')
