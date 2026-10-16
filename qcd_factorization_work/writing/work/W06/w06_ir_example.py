r"""
w06_ir_example.py -- writer W06: worked example for thm:ee-euclid-ir (printed in sec:ee-euclid).

Two-loop gluon-exchange graph V of the current correlator (fig:ee-oneloop (d)):
  current vertices J1 (q in), J2 (q out); quark-gluon vertices a, b;
  quark lines  q1 = J1->a,  q2 = a->J2,  q3 = J2->b,  q4 = b->J1;  gluon g = a-b.
For every set S of internal lines that can vanish simultaneously at a Euclidean point q != 0 with all other lines
generic (closure: a vertex with all but one line soft forces the last one soft; the hard lines H must carry q from J1
to J2), we list
   L_S  = number of independent soft loop momenta (rank of the soft momentum space),
   d_dir = 4 L_S - 2 N_g - N_q           (direct power counting; no 3-gluon/ghost vertex here),
   A, A_q = attachments (ends of soft lines at vertices that also carry hard lines), quark ends among them,
   d_formula = A + A_q/2,
and check d_dir == d_formula >= 2.  The same is done for the self-energy graph S1 (gluon loop on q1..q2), where
a "hard island" (the self-energy subgraph with soft external lines) appears and is merged into S.
Run: python3 -I w06_ir_example.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
import sympy as sp

RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name)


def analyse(name, verts, edges):
    """verts: list of vertex names (first two are J1, J2); edges: dict line -> (type, u, v)."""
    lines = list(edges)
    vidx = {v: i for i, v in enumerate(verts)}
    # incidence matrix
    Inc = sp.zeros(len(verts), len(lines))
    for j, l in enumerate(lines):
        t, u, v = edges[l]
        Inc[vidx[u], j] += 1
        Inc[vidx[v], j] -= 1
    out = []
    for r in range(1, len(lines)):
        for S in itertools.combinations(lines, r):
            S = set(S)
            H = [l for l in lines if l not in S]
            # soft momentum space: line momenta k_S with the H-momenta free; conservation at every vertex
            # all of whose lines are soft (fully soft vertex) gives a constraint on soft momenta only.
            # closure: no vertex may have exactly one hard line (it would be forced soft).
            ok = True
            for v in verts:
                inc = [l for l in lines if v in edges[l][1:]]
                nh = sum(1 for l in inc if l in H)
                ext = v in verts[:2]
                if nh == 1 and not ext:
                    ok = False
                if ext and nh == 0:
                    ok = False          # q enters/leaves at a current vertex: needs a hard line there
            if not ok:
                continue
            # H must connect J1 and J2 (q flows through hard lines); find components of H
            adj = {v: set() for v in verts}
            for l in H:
                t, u, v = edges[l]
                adj[u].add(v); adj[v].add(u)
            comp = {verts[0]}
            stack = [verts[0]]
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if y not in comp:
                        comp.add(y); stack.append(y)
            if verts[1] not in comp:
                continue
            # hard island: H-lines not in the component of J1 (merged into S)
            island = [l for l in H if edges[l][1] not in comp]
            S2 = S | set(island)
            Hc = [l for l in H if l not in island]
            # rank of soft momentum space: number of soft loops = N_S - (rank of constraints)
            # constraints: conservation at vertices all of whose lines are in S2
            fully_soft = [v for v in verts if all((l in S2) for l in lines if v in edges[l][1:])
                          and any(v in edges[l][1:] for l in lines)]
            NS = len(S2)
            LS = NS - len(fully_soft)
            Ng = sum(1 for l in S2 if edges[l][0] == 'g')
            Nq = sum(1 for l in S2 if edges[l][0] == 'q')
            d_dir = 4 * LS - 2 * Ng - Nq
            # attachments: ends of S2-lines at vertices carrying a line of Hc
            A = Aq = 0
            for l in S2:
                t, u, v = edges[l]
                for w in (u, v):
                    if any((w in edges[h][1:]) for h in Hc):
                        A += 1
                        if t == 'q':
                            Aq += 1
            d_f = sp.Rational(A) + sp.Rational(Aq, 2)
            out.append((tuple(sorted(S)), tuple(sorted(island)), LS, Nq, Ng, A, Aq, d_dir, d_f))
    print(f'--- {name}: {len(out)} consistent soft sets')
    for (S, isl, LS, Nq, Ng, A, Aq, dd, df) in out:
        tag = f' (+island {isl})' if isl else ''
        print(f'   S={S}{tag}: L_S={LS} N_q={Nq} N_g={Ng} A={A} A_q={Aq}  d_dir={dd}  A+A_q/2={df}')
    check(f'{name}: direct count = A + A_q/2 for every set', all(o[7] == o[8] for o in out))
    check(f'{name}: min d = 2 (single soft gluon between hard lines)', min(o[7] for o in out) == 2)
    return out


# graph V (fig:ee-oneloop (d))
V = analyse('V (gluon exchange across the quark loop)', ['J1', 'J2', 'a', 'b'],
            {'q1': ('q', 'J1', 'a'), 'q2': ('q', 'a', 'J2'), 'q3': ('q', 'J2', 'b'), 'q4': ('q', 'b', 'J1'),
             'g': ('g', 'a', 'b')})
sets = {o[0]: o for o in V}
check('V: {g} has A=2, A_q=0, d=2', sets[('g',)][5:8] == (2, 0, 2))
check('V: {q_i} has A=A_q=2, d=3', all(sets[(q,)][5:8] == (2, 2, 3) for q in ('q1', 'q2', 'q3', 'q4')))
check('V: {q1,q2,g} and {q3,q4,g} have A=3, A_q=2, d=4 (one fully soft vertex, L_S=2)',
      sets[('g', 'q1', 'q2')][2] == 2 and sets[('g', 'q1', 'q2')][5:8] == (3, 2, 4)
      and sets[('g', 'q3', 'q4')][5:8] == (3, 2, 4))
check('V: {q1,q3} and {q2,q4} have A=A_q=4, d=6',
      sets[('q1', 'q3')][5:8] == (4, 4, 6) and sets[('q2', 'q4')][5:8] == (4, 4, 6))
check('V: exactly 9 consistent soft sets', len(V) == 9)

# graph S1 (self-energy on the quark line J1 -> J2): q1 = J1->a, q2 = a->b (inside), q3 = b->J2, q4 = J2->J1, g = a-b
S1 = analyse('S1 (self-energy insertion)', ['J1', 'J2', 'a', 'b'],
             {'q1': ('q', 'J1', 'a'), 'q2': ('q', 'a', 'b'), 'q3': ('q', 'b', 'J2'), 'q4': ('q', 'J2', 'J1'),
              'g': ('g', 'a', 'b')})

npass = sum(1 for _, c in RES if c)
print(f'\nSUMMARY: {npass}/{len(RES)} checks passed')
