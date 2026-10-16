r"""
w06_ir_degree.py -- writer W06: the IR degree of soft subsets of current-correlator graphs (thm:ee-euclid-ir).

Claim (VF-EE-13, re-derived): let S be a set of internal lines whose momenta vanish simultaneously at a Euclidean
non-exceptional point (q != 0), H the remaining lines.  If H is connected, then in Feynman gauge
      d(S) = 4 L_S - 2 N_g - N_q - 2 N_c + n_ggg(S) + n_ghost(S) = A + A_q/2 >= 2,
where A = number of ends of S-lines at vertices that carry H-lines (attachments), A_q the quark ends among them.
If H has components not containing the current vertices ("hard islands"), each island behaves like an effective
vertex scaling as lambda^{4 - E_g - 3E_q/2 - E_c} (dimensional analysis in the massless theory) and
      d(S) = A_0 + A_{q,0}/2 >= 2  with only the attachments to the component of the current vertices counted.
Extra numerator zeros (ghost vertex with soft outgoing ghost and hard other lines) only increase d.

S1  symbolic: the topological identities imply d = A + A_q/2.
S2  enumeration: for a family of 2-, 3-, 4-loop graphs, every consistent soft set S: direct power counting
    (rank of the soft momentum space from the incidence matrix, propagator and vertex powers, islands) equals
    A_0 + A_{q,0}/2 (+ the numerator surplus), and is >= 2.
Run: python3 -I w06_ir_degree.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
import sympy as sp
import numpy as np

RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# ---------------------------------------------------------------- S1 symbolic
Ng, Nq, Nc, nggg, nqqg, nccg, V4, A, Aq, Ac = sp.symbols('N_g N_q N_c n_ggg n_qqg n_ccg V_4 A A_q A_c')
NS = Ng + Nq + Nc
V3 = nggg + nqqg + nccg
LS = NS - V3 - V4
d = 4 * LS - 2 * Ng - Nq - 2 * Nc + nggg + nccg
# topological relations: line ends
rel_all = sp.Eq(2 * NS, 3 * V3 + 4 * V4 + A)
rel_q = sp.Eq(2 * Nq, 2 * nqqg + Aq)
rel_c = sp.Eq(2 * Nc, 2 * nccg + Ac)
sol = sp.solve([rel_all, rel_q, rel_c], [Ng, Nq, Nc], dict=True)[0]
check('S1  d = 4L_S - 2N_g - N_q - 2N_c + n_ggg + n_ccg = A + A_q/2 (using 2N_S = 3V_3 + 4V_4 + A, 2N_q = 2n_qqg + A_q)',
      sp.simplify(d.subs(sol) - (A + Aq / 2)) == 0)

# ---------------------------------------------------------------- S2 enumeration
# a graph: vertices: dict name -> type in {'J' (current), 'qqg', 'ggg', 'gggg', 'ccg'}
#          edges: list of (type, u, v) with type in {'q','g','c'}; for ghost edges (c): orientation u -> v = ghost flow
#          (the outgoing ghost at vertex v is the edge leaving v along the flow)
def build(edges, vtypes):
    return {'E': edges, 'V': vtypes}


def check_graph(name, G, verbose=False):
    E, Vt = G['E'], G['V']
    verts = list(Vt)
    vidx = {v: i for i, v in enumerate(verts)}
    nE = len(E)
    # incidence matrix (verts x edges), orientation u->v
    Inc = np.zeros((len(verts), nE))
    for j, (t, u, v) in enumerate(E):
        Inc[vidx[u], j] += 1
        Inc[vidx[v], j] -= 1
    J = [v for v in verts if Vt[v] == 'J']
    assert len(J) == 2
    # line-momentum space: k in R^E with Inc k = (external), homogeneous part = null space of Inc (cycle space)
    ns = sp.Matrix(Inc.astype(int)).nullspace()
    C = np.array([[float(x) for x in vec] for vec in ns]).T if ns else np.zeros((nE, 0))  # columns: cycle basis
    L = C.shape[1]
    # particular solution carrying q from J0 to J1 (one unit of "q")
    b = np.zeros(len(verts)); b[vidx[J[0]]] = -1; b[vidx[J[1]]] = 1
    kpart = np.linalg.lstsq(Inc, -b, rcond=None)[0]
    worst = None
    nsets = 0
    allok = True
    for rsz in range(1, nE):
        for S in itertools.combinations(range(nE), rsz):
            S = set(S)
            H = [j for j in range(nE) if j not in S]
            # consistency: there exists a configuration with k_e = 0 (e in S) and k_e != 0 generic (e in H):
            # constraints: kpart + C t has zero components on S
            CS = C[sorted(S), :] if L else np.zeros((len(S), 0))
            kS = kpart[sorted(S)]
            # solve CS t = -kS
            if L:
                t0, *_ = np.linalg.lstsq(CS, -kS, rcond=None)
                if np.linalg.norm(CS @ t0 + kS) > 1e-9:
                    continue          # S cannot be soft (q would have to flow through S)
                # null directions of CS: free soft-compatible configurations; check H lines not forced to zero
                nsS = sp.Matrix(np.round(CS).astype(int)).nullspace() if CS.size else [sp.Matrix(np.eye(L)[:, i]) for i in range(L)]
                Nmat = np.array([[float(x) for x in vec] for vec in nsS]).T if nsS else np.zeros((L, 0))
                kH0 = kpart + C @ t0
                forced = []
                for j in H:
                    row = C[j, :] @ Nmat if Nmat.size else np.zeros(0)
                    if abs(kH0[j]) < 1e-9 and np.linalg.norm(row) < 1e-9:
                        forced.append(j)
                if forced:
                    continue          # not closed: these lines would vanish too
                rankS = np.linalg.matrix_rank(CS) if CS.size else 0
            else:
                if np.linalg.norm(kS) > 1e-9:
                    continue
                rankS = 0
            nsets += 1
            # components of H (as a graph on all vertices touched by H-lines)
            parent = {v: v for v in verts}

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for j in H:
                t, u, v = E[j]
                parent[find(u)] = find(v)
            touchedH = set()
            for j in H:
                touchedH |= {E[j][1], E[j][2]}
            comp0 = find(J[0])
            assert find(J[1]) == comp0
            islands = {}
            for vtx in touchedH:
                cmp_ = find(vtx)
                if cmp_ != comp0:
                    islands.setdefault(cmp_, set()).add(vtx)
            # direct power counting
            prop = sum({'g': 2, 'q': 1, 'c': 2}[E[j][0]] for j in S)
            vert = 0
            surplus = 0
            island_vertices = set().union(*islands.values()) if islands else set()
            for vtx in verts:
                if vtx in island_vertices:
                    continue      # vertex factors inside an island are part of its dimensional scaling
                inc = [j for j in range(nE) if vtx in (E[j][1], E[j][2])]
                allsoft = all(j in S for j in inc)
                if Vt[vtx] == 'ggg' and allsoft:
                    vert += 1
                if Vt[vtx] == 'ccg':
                    # outgoing ghost at vtx: ghost edge with u == vtx
                    outg = [j for j in inc if E[j][0] == 'c' and E[j][1] == vtx]
                    if outg and outg[0] in S:
                        vert += 1
                        if not allsoft:
                            surplus += 1
            isl_pow = 0
            for cmp_, vs in islands.items():
                Eg = Eq = Ec = 0
                for j in S:
                    t, u, v = E[j]
                    for end in (u, v):
                        if end in vs:
                            if t == 'g': Eg += 1
                            if t == 'q': Eq += 1
                            if t == 'c': Ec += 1
                isl_pow += 4 - Eg - sp.Rational(3, 2) * Eq - Ec
            d_direct = 4 * rankS - prop + vert + isl_pow
            # formula: attachments to the external component only
            A0 = Aq0 = 0
            for j in S:
                t, u, v = E[j]
                for end in (u, v):
                    if end in touchedH and find(end) == comp0:
                        A0 += 1
                        if t == 'q':
                            Aq0 += 1
            d_formula = A0 + sp.Rational(Aq0, 2) + surplus
            ok = (sp.nsimplify(d_direct) == d_formula) and d_formula >= 2
            if not ok:
                allok = False
                print('   MISMATCH in %s: S=%s rank=%d direct=%s formula=%s islands=%s' % (name, sorted(S), rankS, d_direct, d_formula, islands))
            if worst is None or d_formula < worst:
                worst = d_formula
    check('S2  %-58s %3d soft sets: direct count = A_0 + A_q0/2 (+surplus), min d = %s' % (name, nsets, worst), allok)
    return allok


# ---- graph library (current vertices J1, J2; quark edges oriented along fermion flow) ----
graphs = {}
# two-loop V: quark loop J1 -a-> T -b-> J2 -c-> B -d-> J1, gluon T-B
graphs['2-loop vertex graph V'] = build([('q', 'J1', 'T'), ('q', 'T', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'), ('g', 'T', 'B')],
                                        {'J1': 'J', 'J2': 'J', 'T': 'qqg', 'B': 'qqg'})
graphs['2-loop self-energy graph S1'] = build([('q', 'J1', 'P1'), ('q', 'P1', 'P2'), ('q', 'P2', 'J2'), ('q', 'J2', 'J1'), ('g', 'P1', 'P2')],
                                              {'J1': 'J', 'J2': 'J', 'P1': 'qqg', 'P2': 'qqg'})
# three-loop: V with quark-loop insertion on the gluon (hard island possible)
graphs['3-loop V + quark bubble on gluon'] = build([('q', 'J1', 'T'), ('q', 'T', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'),
                                                     ('g', 'T', 'X'), ('q', 'X', 'Y'), ('q', 'Y', 'X'), ('g', 'Y', 'B')],
                                                    {'J1': 'J', 'J2': 'J', 'T': 'qqg', 'B': 'qqg', 'X': 'qqg', 'Y': 'qqg'})
graphs['3-loop V + gluon loop on gluon'] = build([('q', 'J1', 'T'), ('q', 'T', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'),
                                                    ('g', 'T', 'X'), ('g', 'X', 'Y'), ('g', 'Y', 'X'), ('g', 'Y', 'B')],
                                                   {'J1': 'J', 'J2': 'J', 'T': 'qqg', 'B': 'qqg', 'X': 'ggg', 'Y': 'ggg'})
graphs['3-loop V + ghost loop on gluon'] = build([('q', 'J1', 'T'), ('q', 'T', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'),
                                                    ('g', 'T', 'X'), ('c', 'X', 'Y'), ('c', 'Y', 'X'), ('g', 'Y', 'B')],
                                                   {'J1': 'J', 'J2': 'J', 'T': 'qqg', 'B': 'qqg', 'X': 'ccg', 'Y': 'ccg'})
# three-loop ladder (two rungs) and crossed ladder
graphs['3-loop ladder (two rungs)'] = build([('q', 'J1', 'T1'), ('q', 'T1', 'T2'), ('q', 'T2', 'J2'), ('q', 'J2', 'B2'), ('q', 'B2', 'B1'), ('q', 'B1', 'J1'),
                                              ('g', 'T1', 'B1'), ('g', 'T2', 'B2')],
                                             {'J1': 'J', 'J2': 'J', 'T1': 'qqg', 'T2': 'qqg', 'B1': 'qqg', 'B2': 'qqg'})
graphs['3-loop crossed ladder'] = build([('q', 'J1', 'T1'), ('q', 'T1', 'T2'), ('q', 'T2', 'J2'), ('q', 'J2', 'B2'), ('q', 'B2', 'B1'), ('q', 'B1', 'J1'),
                                          ('g', 'T1', 'B2'), ('g', 'T2', 'B1')],
                                         {'J1': 'J', 'J2': 'J', 'T1': 'qqg', 'T2': 'qqg', 'B1': 'qqg', 'B2': 'qqg'})
# three-loop non-abelian: three-gluon vertex joining gluons from the quark lines
graphs['3-loop non-abelian (three-gluon vertex)'] = build([('q', 'J1', 'T1'), ('q', 'T1', 'T2'), ('q', 'T2', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'),
                                                            ('g', 'T1', 'X'), ('g', 'T2', 'X'), ('g', 'X', 'B')],
                                                           {'J1': 'J', 'J2': 'J', 'T1': 'qqg', 'T2': 'qqg', 'B': 'qqg', 'X': 'ggg'})
# four-loop singlet: two quark loops (each with one current) joined by three gluons
graphs['4-loop singlet (two quark loops, 3 gluons)'] = build(
    [('q', 'J1', 'a1'), ('q', 'a1', 'a2'), ('q', 'a2', 'a3'), ('q', 'a3', 'J1'),
     ('q', 'J2', 'b1'), ('q', 'b1', 'b2'), ('q', 'b2', 'b3'), ('q', 'b3', 'J2'),
     ('g', 'a1', 'b1'), ('g', 'a2', 'b2'), ('g', 'a3', 'b3')],
    {'J1': 'J', 'J2': 'J', 'a1': 'qqg', 'a2': 'qqg', 'a3': 'qqg', 'b1': 'qqg', 'b2': 'qqg', 'b3': 'qqg'})
# four-loop: V with a gluon loop that contains a quark loop (nested island)
graphs['4-loop V + gluon loop with quark bubble'] = build(
    [('q', 'J1', 'T'), ('q', 'T', 'J2'), ('q', 'J2', 'B'), ('q', 'B', 'J1'),
     ('g', 'T', 'X'), ('g', 'X', 'Y'), ('g', 'Y', 'B'), ('g', 'X', 'U'), ('q', 'U', 'W'), ('q', 'W', 'U'), ('g', 'W', 'Y')],
    {'J1': 'J', 'J2': 'J', 'T': 'qqg', 'B': 'qqg', 'X': 'ggg', 'Y': 'ggg', 'U': 'qqg', 'W': 'qqg'})
allg = True
for nm, G in graphs.items():
    allg &= check_graph(nm, G)
check('S3  all graphs: every consistent soft set has d >= 2 (IR convergent by power counting)', allg)
print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
