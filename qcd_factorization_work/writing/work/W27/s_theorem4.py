#!/usr/bin/env python3
"""
W27 / Ch24 prop:front-commuting -- check of the per-jet homogeneity lemma used in the proof of
Gardi-Herzog-Jones-Ma-Schlenk Theorem 4 (written out in the book in our own derivation):

  For an H/J/S configuration R (J_i connected, only external momentum p_i; S without external momenta;
  every connected soft component S_k attached to H u J), define for every monomial m of the Lee-Pomeransky
  polynomial P = U + F (U: complements of spanning trees, F: complements of spanning 2-trees T2 with
  coefficient -s_{T2}) the per-jet exponents
      e_i(m) = [s_{T2} = p_i^2] - #(edges of Gamma_i = J_i u U_{S_k attached to J_i} not in the tree),
  and A_i = L(Gamma_i~) (loop number with everything outside Gamma_i contracted to one vertex).
  Claim (i): e_i(m) >= -A_i for every monomial and every i.
  Claim (ii): if every S_k is attached to EXACTLY two jets ("jet pairing"), then sum_i e_i(m) = r(m).v_R (the
  single-parameter scaling weight), and the leading monomials (minimal r.v_R) are exactly those with
  e_i = -A_i for all i  =>  P_0^(R) is multi-homogeneous (separate scaling in each p_i^2), the non-leading
  monomials carry k_i = e_i + A_i >= 0.
  Counter-check: for the non-jet-pairing double-soft region of the non-planar two-loop graph (soft vertex
  attached to three jets; GHJMS fig. 8 / eq. (5.25)) P_0 is NOT multi-homogeneous.
"""
import itertools
PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + info) if info else ""))

def components(vertices, edges):
    par = {v: v for v in vertices}
    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for (a, b) in edges:
        ra, rb = f(a), f(b)
        if ra != rb: par[ra] = rb
    comp = {}
    for v in vertices: comp.setdefault(f(v), []).append(v)
    return list(comp.values())

def forests(G, ncomp):
    """all spanning forests with exactly ncomp components (as sets of edge indices)."""
    V, E = G['V'], G['E']
    nE = len(V) - ncomp
    out = []
    for S in itertools.combinations(range(len(E)), nE):
        comps = components(V, [E[i] for i in S])
        if len(comps) == ncomp:
            out.append((set(S), comps))
    return out

def lp_monomials(G):
    """list of (complement edge set, coefficient label) for U and F of a massless graph.
       coefficient label: None for U; ('p', i) if the momentum flowing between the 2-tree components is exactly
       the on-shell momentum p_i; ('hard', ...) otherwise; momentum zero -> term absent."""
    mons = []
    allE = set(range(len(G['E'])))
    for T, comps in forests(G, 1):
        mons.append((frozenset(allE - T), None))
    for T, comps in forests(G, 2):
        c0 = set(comps[0])
        ext = sorted(lab for v, lab in G['ext'] if v in c0)
        ext_other = sorted(lab for v, lab in G['ext'] if v not in c0)
        if not ext or not ext_other:
            continue                         # zero momentum flows between the components
        if len(ext) == 1 and ext[0] in G['onshell']:
            coef = ('p', ext[0])
        elif len(ext_other) == 1 and ext_other[0] in G['onshell']:
            coef = ('p', ext_other[0])
        else:
            coef = ('hard', tuple(ext))
        mons.append((frozenset(allE - T), coef))
    return mons

def loop_number(vertices, edges):
    return len(edges) - len(vertices) + len(components(vertices, edges))

def analyse(G, R, name, expect_pairing):
    """R = dict: 'J': {i: set(edges)}, 'S': set(edges)."""
    E = G['E']; V = G['V']
    jets = R['J']; S = R['S']
    # soft components and the jets they attach to
    svert = set(v for e in S for v in E[e])
    scomps = []
    for comp in components(sorted(svert), [E[e] for e in S]):
        ce = [e for e in S if E[e][0] in comp or E[e][1] in comp]
        scomps.append(set(ce))
    jvert = {i: set(v for e in jets[i] for v in E[e]) for i in jets}
    attach = []
    for ce in scomps:
        cv = set(v for e in ce for v in E[e])
        attach.append({i for i in jets if cv & jvert[i]})
    pairing = all(len(a) == 2 for a in attach)
    # Gamma_i and A_i
    Gam = {}
    A = {}
    for i in jets:
        gi = set(jets[i])
        for ce, at in zip(scomps, attach):
            if i in at: gi |= ce
        Gam[i] = gi
        # contract everything outside Gamma_i: vertices internal to Gamma_i = all incident edges in Gamma_i
        inc = {v: set() for v in V}
        for k, (a, b) in enumerate(E): inc[a].add(k); inc[b].add(k)
        internal = {v for v in V if inc[v] and inc[v] <= gi}
        # vertices of external legs that are not internal are part of sigma anyway
        mapv = lambda v: v if v in internal else 'sigma'
        gv = sorted(internal) + ['sigma']
        ge = [(mapv(E[k][0]), mapv(E[k][1])) for k in gi]
        A[i] = loop_number(gv, ge)
    # region vector weights: jet edges -1, soft edges -2; coefficient p_i^2 -> +1
    mons = lp_monomials(G)
    def rv(m):
        comp, coef = m
        w = -sum(1 for e in comp if any(e in jets[i] for i in jets)) - 2 * sum(1 for e in comp if e in S)
        if coef is not None and coef[0] == 'p': w += 1
        return w
    def evec(m):
        comp, coef = m
        out = {}
        for i in jets:
            out[i] = -len(comp & Gam[i]) + (1 if (coef is not None and coef == ('p', i)) else 0)
        return out
    minrv = min(rv(m) for m in mons)
    lead = [m for m in mons if rv(m) == minrv]
    ok_i = all(evec(m)[i] >= -A[i] for m in mons for i in jets)
    print(f"--- {name}: jets {sorted(jets)}, soft comps attach to {attach}, A = {A}, #monomials = {len(mons)}, "
          f"#leading = {len(lead)}, min r.v = {minrv}")
    check(f"{name}: (i) e_i(m) >= -A_i for every monomial and every jet", ok_i)
    if pairing:
        ok_sum = all(sum(evec(m).values()) == rv(m) for m in mons)
        check(f"{name}: (ii) jet-pairing => sum_i e_i(m) = r(m).v_R for every monomial", ok_sum)
        ok_lead = all(all(evec(m)[i] == -A[i] for i in jets) for m in lead) and \
                  all((m in lead) == all(evec(m)[i] == -A[i] for i in jets) for m in mons)
        check(f"{name}: (ii) leading monomials <=> e_i = -A_i for all i (P_0 multi-homogeneous)", ok_lead)
        check(f"{name}: min r.v_R = -sum_i A_i", minrv == -sum(A.values()))
    else:
        vecs = set(tuple(sorted(evec(m).items())) for m in lead)
        check(f"{name}: NOT jet pairing => leading monomials carry different per-jet exponents "
              f"(P_0 not multi-homogeneous)", len(vecs) > 1, f"distinct exponent vectors: {len(vecs)}")
    check(f"{name}: pairing status as expected", pairing == expect_pairing)
    return lead

# ---- (a) one-loop triangle (Sudakov form factor), soft region: e1 = A-C (J1), e2 = B-C (J2), e3 = A-B (S)
G1 = {'V': ['A', 'B', 'C'], 'E': [('A', 'C'), ('B', 'C'), ('A', 'B')],
      'ext': [('A', 'p1'), ('B', 'p2'), ('C', 'q')], 'onshell': {'p1', 'p2'}}
lead = analyse(G1, {'J': {'p1': {0}, 'p2': {1}}, 'S': {2}}, "triangle, soft region", True)
labs = sorted(("x" + "x".join(str(e + 1) for e in sorted(c))) + (f"*{cf}" if cf else "") for c, cf in lead)
print("   leading monomials:", labs, " (GHJMS eq. (2.27): x3 + (-p1^2)x1x3 + (-p2^2)x2x3 + (-q^2)x1x2)")
analyse(G1, {'J': {'p1': {0}, 'p2': set()}, 'S': set()}, "triangle, collinear-1 region (no soft)", True)

# ---- (b) two-loop planar ladder (vertex), soft region with two soft rungs
# vertices: C (q), A1, A2 (jet 1 side, p1 at A2), B1, B2 (jet 2 side, p2 at B2)
G2 = {'V': ['C', 'A1', 'A2', 'B1', 'B2'],
      'E': [('C', 'A1'), ('A1', 'A2'), ('C', 'B1'), ('B1', 'B2'), ('A1', 'B1'), ('A2', 'B2')],
      'ext': [('C', 'q'), ('A2', 'p1'), ('B2', 'p2')], 'onshell': {'p1', 'p2'}}
analyse(G2, {'J': {'p1': {0, 1}, 'p2': {2, 3}}, 'S': {4, 5}}, "planar 2-loop ladder, double-soft", True)
analyse(G2, {'J': {'p1': {1}, 'p2': {3}}, 'S': {5}}, "planar 2-loop ladder, hard inner loop + soft outer rung", True)

# ---- (c) two-loop non-planar graph of GHJMS fig. 8 with three on-shell legs: h (q), a1,a2,a3 (p_i), soft vertex s
G3 = {'V': ['h', 'a1', 'a2', 'a3', 's'],
      'E': [('h', 'a1'), ('h', 'a2'), ('h', 'a3'), ('s', 'a1'), ('s', 'a2'), ('s', 'a3')],
      'ext': [('h', 'q'), ('a1', 'p1'), ('a2', 'p2'), ('a3', 'p3')], 'onshell': {'p1', 'p2', 'p3'}}
lead3 = analyse(G3, {'J': {'p1': {0}, 'p2': {1}, 'p3': {2}}, 'S': {3, 4, 5}},
                "non-planar 2-loop, double-soft (soft vertex, 3 jets)", False)
print(f"   {len(lead3)} leading monomials, e.g.:",
      sorted(("x" + "x".join(str(e + 1) for e in sorted(c))) + (f"*{cf}" if cf else "") for c, cf in lead3)[:12])
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
