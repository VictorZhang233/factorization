#!/usr/bin/env python3
"""
Independent check of the Theorem F status paragraph (comparison with SSS 2019 sec. 7 Prop. 6) and of Lemma F.0:
 * forward kinematics: p at P1, -p at P2, q at J1, -q at J2, p^2=0, q^2=-Q^2, p.q = omega Q^2/2;
 * my own Symanzik polynomials by brute-force enumeration of spanning trees / 2-forests;
 * F = Q^2 (F0 + omega F1): coefficients of F1 in {0,+-1}, mon(F1) subset mon(F0) (Lemma F.0);
 * whether BOTH signs of c_p c_q occur (then no choice t = +-omega gives SSS's positive coefficients);
 * Newton polytope of U + F0 + t F1 in R^{N+1}: facets with inward normal having t-component > 0
   ("essential" in SSS's sense) -- expected: only the base facet {w_{N+1}=0}, normal (0,...,0,1).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

def components(V, edges):
    parent = {v: v for v in V}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    acyclic = True
    for (a, b) in edges:
        ra, rb = find(a), find(b)
        if ra == rb: acyclic = False
        else: parent[ra] = rb
    comps = {}
    for v in V: comps.setdefault(find(v), set()).add(v)
    return acyclic, list(comps.values())

def symanzik(V, E):
    N = len(E); al = sp.symbols(f'a0:{N}', positive=True)
    w = sp.symbols('omega'); Q2 = sp.Integer(1)
    ext = {'P1': 'p', 'P2': '-p', 'J1': 'q', 'J2': '-q'}
    U = 0; F0 = 0; F1 = 0
    for k in [len(V)-1, len(V)-2]:
        for S in itertools.combinations(range(N), k):
            acyc, comps = components(V, [E[i] for i in S])
            if not acyc: continue
            mon = sp.Mul(*[al[i] for i in range(N) if i not in S])
            if k == len(V)-1 and len(comps) == 1:
                U += mon
            if k == len(V)-2 and len(comps) == 2:
                T1 = comps[0]
                cp = (1 if 'P1' in T1 else 0) - (1 if 'P2' in T1 else 0)
                cq = (1 if 'J1' in T1 else 0) - (1 if 'J2' in T1 else 0)
                # -s_T = -(cp p + cq q)^2 = Q^2 (cq^2 - cp cq omega)   [p^2=0, q^2=-Q^2, 2p.q = omega Q^2]
                F0 += cq**2 * mon
                F1 += -cp*cq * mon
    return al, sp.expand(U), sp.expand(F0), sp.expand(F1)

def check_graph(name, V, E):
    al, U, F0, F1 = symanzik(V, E)
    N = len(E)
    P0 = sp.Poly(F0, *al); P1 = sp.Poly(F1, *al); PU = sp.Poly(U, *al)
    c1 = dict(P1.terms()); c0 = dict(P0.terms())
    coeffs_ok = all(v in (1, -1) for v in c1.values()) and all(v == 1 for v in c0.values())
    subset_ok = all(m in c0 for m in c1)
    signs = sorted(set(int(v) for v in c1.values()))
    # Newton polytope of U + F0 + t F1
    pts = [list(m) + [0] for m in PU.monoms()] + [list(m) + [0] for m in P0.monoms()] + [list(m) + [1] for m in P1.monoms()]
    pts = np.array(sorted(set(map(tuple, pts))), dtype=float)
    base = np.array([p[:-1] for p in pts if p[-1] == 0])
    # dimension of base polytope (affine rank)
    rb = np.linalg.matrix_rank(base[1:] - base[0])
    hull = ConvexHull(pts, qhull_options='QJ' if False else '')
    eqs = []
    for e in hull.equations:   # e[:-1].x + e[-1] <= 0 inside; outward normal e[:-1]
        nrm = -e[:-1] / np.linalg.norm(e[:-1])  # inward normal
        if not any(np.allclose(nrm, q, atol=1e-8) for q in eqs): eqs.append(nrm)
    ess = [q for q in eqs if q[-1] > 1e-9]
    only_base = (len(ess) == 1 and np.allclose(ess[0], np.eye(N+1)[-1], atol=1e-8))
    print(f"--- {name}: N={N} lines, L={len(E)-len(V)+1} loops")
    print(f"    F1 coefficients in {{+-1}}, F0 coefficients 1: {coeffs_ok};  mon(F1) subset mon(F0): {subset_ok}")
    print(f"    signs of -c_p c_q present in F1: {signs}  ->  {'SIGN-INDEFINITE (both 1-omega and 1+omega monomials)' if len(signs)==2 else 'single sign'}")
    print(f"    base polytope Newt(U+F0) affine dim = {rb} (full = {N});  #facets of Newt(U+F0+tF1) = {len(eqs)};"
          f"  facets with inward t-normal > 0: {len(ess)};  only the base facet: {only_base}")
    return coeffs_ok and subset_ok and only_base and rb == N, len(signs) == 2

graphs = {
 'one-loop box (P1-J1-J2-P2-P1)': (['P1', 'J1', 'J2', 'P2'], [('P1','J1'), ('J1','J2'), ('J2','P2'), ('P2','P1')]),
 'one-loop crossed box (P1-J2-J1-P2-P1)': (['P1', 'J1', 'J2', 'P2'], [('P1','J2'), ('J2','J1'), ('J1','P2'), ('P2','P1')]),
 'two-loop planar ladder': (['P1', 'v1', 'J1', 'J2', 'v2', 'P2'],
     [('P1','v1'), ('v1','J1'), ('J1','J2'), ('J2','v2'), ('v2','P2'), ('v1','v2'), ('P1','P2')]),
 'two-loop non-planar (crossed gluons)': (['P1', 'c', 'J1', 'd', 'J2', 'P2'],
     [('P1','c'), ('c','J1'), ('J1','d'), ('d','J2'), ('J2','P2'), ('P1','d'), ('c','P2')]),
 'two-loop quark self-energy insertion on the s-channel line + gluon P1-P2': (['P1', 'J1', 'x', 'y', 'J2', 'P2'],
     [('P1','J1'), ('J1','x'), ('x','y'), ('x','y'), ('y','J2'), ('J2','P2'), ('P2','P1')]),
}
allok = True; indefinite = []
for name, (V, E) in graphs.items():
    ok, ind = check_graph(name, V, E)
    allok &= ok
    if ind: indefinite.append(name)
print("\nSign-indefinite graphs:", indefinite)
print("OVERALL (F.0 structure + only the base facet is essential, for every graph):", "PASS" if allok else "FAIL")
