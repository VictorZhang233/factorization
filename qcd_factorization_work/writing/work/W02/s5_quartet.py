"""W02 / Ch2 check s5: Kugo-Ojima quartet mechanism for one light-like momentum mode (ex:qcd-brst-quartet,
prop:qcd-brst-cohomology).  Free theory, Feynman gauge, Kugo-Ojima hermitian ghosts (cbar_PS = -i cbar_KO).
One-particle states: |e1>,|e2> (transverse), |K> = k.a^dag|0>, |H> = eta.a^dag|0> (k.eta = 1, eta^2 = 0),
|C> = c^dag|0>, |Cb> = cbar^dag|0>.  Gram: <ei|ej> = delta, <K|H> = <H|K> = -1, <C|Cb> = i, <Cb|C> = -i.
Free BRST charge Q = -sum_k [c^dag (k.a) + (k.a^dag) c]:  Q|H> = |C>, Q|Cb> = -i|K>, Q e_i = Q K = Q C = 0.
Homotopy R: R|C> = |H>, R|K> = i|Cb>.  Checks on the truncated Fock space (total quanta <= NMAX):
Q^2 = 0, Q self-adjoint, {Q,R} = N_quartet, cohomology = transverse sector, Gram >= 0 on ker Q with null space im Q.
Run: python3 -I s5_quartet.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)

# --- explicit one-particle check from the field-theory commutators ---
eta = np.diag([1., -1, -1, -1]); dot = lambda a, b: a @ eta @ b
k = np.array([2.0, 0, 0, 2.0]); kb = np.array([2.0, 0, 0, -2.0]); etav = kb / dot(k, kb)
e1 = np.array([0, 1.0, 0, 0]); e2 = np.array([0, 0, 1.0, 0])
basis_vec = {'e1': e1, 'e2': e2, 'K': k, 'H': etav}
gram_glu = {(x, y): -dot(basis_vec[x], basis_vec[y]) for x in basis_vec for y in basis_vec}   # <a(e)|a(e')> = -e.e'
report(np.isclose(gram_glu[('e1', 'e1')], 1) and np.isclose(gram_glu[('K', 'K')], 0) and np.isclose(gram_glu[('H', 'H')], 0)
       and np.isclose(gram_glu[('K', 'H')], -1) and np.isclose(gram_glu[('e1', 'K')], 0), 'gluon one-particle Gram from [a_mu, a_nu^dag] = -g_mu nu')
# Q on one-gluon states: [Q, a^dag(e)] = (e.k) c^dag
Qglu = {x: dot(basis_vec[x], k) for x in basis_vec}
report(np.isclose(Qglu['H'], 1) and all(np.isclose(Qglu[x], 0) for x in ('e1', 'e2', 'K')), 'Q|a(e)> = (e.k)|C>: only the eta-polarised gluon is not BRST closed')

# --- truncated Fock space ---
BOS = ['e1', 'e2', 'K', 'H']; FER = ['C', 'Cb']
g1 = np.zeros((6, 6), complex)   # one-particle Gram in order e1 e2 K H C Cb
g1[0, 0] = g1[1, 1] = 1; g1[2, 3] = g1[3, 2] = -1; g1[4, 5] = 1j; g1[5, 4] = -1j
NMAX = 4
states = []
for nb in itertools.product(range(NMAX + 1), repeat=4):
    for nf in itertools.product(range(2), repeat=2):
        if sum(nb) + sum(nf) <= NMAX:
            states.append(nb + nf)
idx = {s: i for i, s in enumerate(states)}
dim = len(states)
def modes_list(s):
    out = []
    for i, n in enumerate(s):
        out += [i] * n
    return out
def perm_sum(left, right):
    """inner product <prod left|prod right>: bosons by permanent, fermions by determinant (same particle numbers)"""
    lb = [m for m in left if m < 4]; rb = [m for m in right if m < 4]
    lf = [m for m in left if m >= 4]; rf = [m for m in right if m >= 4]
    if len(lb) != len(rb) or len(lf) != len(rf): return 0
    pb = 0
    for p in itertools.permutations(range(len(rb))):
        v = 1
        for i, j in enumerate(p): v *= np.conj(1) * g1[lb[i], rb[j]]
        pb += v
    if len(lf) == 0: return pb
    M = np.array([[g1[a, b] for b in rf] for a in lf])
    return pb * np.linalg.det(M)
Gm = np.zeros((dim, dim), complex)
for s in states:
    for s2 in states:
        Gm[idx[s], idx[s2]] = perm_sum(modes_list(s), modes_list(s2))
report(np.allclose(Gm, Gm.conj().T), 'Fock-space Gram matrix is hermitian (indefinite)')
def apply_derivation(op_one, s, odd=True):
    """apply an odd derivation defined on creation operators (op_one: mode -> list of (coeff, mode)) to the
       monomial state s = (bosons)(c^dag)^{nC}(cbar^dag)^{nCb}|0>; returns dict state->coeff"""
    out = {}
    nb = list(s[:4]); nC, nCb = s[4], s[5]
    # bosonic factors (even): derivative of a^dag_i^{n_i} gives n_i a^dag_i^{n_i - 1} op(a^dag_i)
    for i in range(4):
        if nb[i] == 0 or i not in op_one: continue
        for coeff, m in op_one[i]:
            nb2 = nb.copy(); nb2[i] -= 1
            if m < 4:
                nb2[m] += 1; new = tuple(nb2) + (nC, nCb); sign = 1
            elif m == 4:        # produces c^dag: insert at the left of the fermion part
                if nC == 1: continue
                new = tuple(nb2) + (1, nCb); sign = 1
            else:               # produces cbar^dag: place after c^dag (no odd factor passed if it goes to the right end)
                if nCb == 1: continue
                new = tuple(nb2) + (nC, 1); sign = (-1) ** nC   # move cbar^dag past c^dag
            out[new] = out.get(new, 0) + nb[i] * coeff * sign
    # fermionic factor c^dag (position: first odd factor), sign (+1)
    if nC == 1 and 4 in op_one:
        for coeff, m in op_one[4]:
            if m < 4:
                nb2 = nb.copy(); nb2[m] += 1; new = tuple(nb2) + (0, nCb); sign = 1
            else:
                continue
            out[new] = out.get(new, 0) + coeff * sign
    if nCb == 1 and 5 in op_one:
        for coeff, m in op_one[5]:
            if m < 4:
                nb2 = nb.copy(); nb2[m] += 1; new = tuple(nb2) + (nC, 0); sign = (-1) ** nC   # passes c^dag
            else:
                continue
            out[new] = out.get(new, 0) + coeff * sign
    return out
Qone = {3: [(1, 4)], 5: [(-1j, 2)]}            # Q a_H^dag = c^dag ; Q cbar^dag = -i a_K^dag
Rone = {4: [(1, 3)], 2: [(1j, 5)]}             # R c^dag = a_H^dag ; R a_K^dag = i cbar^dag
def op_matrix(one):
    M = np.zeros((dim, dim), complex)
    for s in states:
        for s2, c in apply_derivation(one, s).items():
            if s2 in idx: M[idx[s2], idx[s]] += c
    return M
Q = op_matrix(Qone); Rm = op_matrix(Rone)
report(np.allclose(Q @ Q, 0), f'Q^2 = 0 on the Fock space (dim {dim}, up to {NMAX} quanta)')
report(np.allclose(Q.conj().T @ Gm, Gm @ Q), 'Q is self-adjoint w.r.t. the indefinite inner product: <Qx|y> = <x|Qy>')
Nq = np.diag([float(s[2] + s[3] + s[4] + s[5]) for s in states])
report(np.allclose(Q @ Rm + Rm @ Q, Nq), '{Q, R} = N_quartet (number of K, H, C, Cb quanta)')
# cohomology dimension by particle number
ok = True; details = []
for ntot in range(NMAX + 1):
    sub = [idx[s] for s in states if sum(s) == ntot]
    Qs = Q[np.ix_(sub, sub)]
    r = np.linalg.matrix_rank(Qs, tol=1e-9)
    dimker = len(sub) - r; dimim = r
    coh = dimker - dimim
    ntrans = sum(1 for s in states if sum(s) == ntot and s[2] + s[3] + s[4] + s[5] == 0)
    ok &= (coh == ntrans); details.append(f'n={ntot}: dim H = {coh}, transverse states = {ntrans}')
report(ok, 'ker Q / im Q has the dimension of the transverse-gluon Fock space at every particle number', '; '.join(details))
# positivity on ker Q
ok = True
for ntot in range(1, NMAX + 1):
    sub = [idx[s] for s in states if sum(s) == ntot]
    Qs = Q[np.ix_(sub, sub)]; Gs = Gm[np.ix_(sub, sub)]
    # basis of ker Q
    u, sv, vh = np.linalg.svd(Qs)
    ker = vh[np.sum(sv > 1e-9):].conj().T
    Gk = ker.conj().T @ Gs @ ker
    ev = np.linalg.eigvalsh((Gk + Gk.conj().T) / 2)
    nzero = np.sum(np.abs(ev) < 1e-9); npos = np.sum(ev > 1e-9); nneg = np.sum(ev < -1e-9)
    rank_im = np.linalg.matrix_rank(Qs, tol=1e-9)
    ntrans = sum(1 for s in states if sum(s) == ntot and s[2] + s[3] + s[4] + s[5] == 0)
    ok &= (nneg == 0 and nzero == rank_im and npos == ntrans)
report(ok, 'Gram >= 0 on ker Q; its null space is exactly im Q; positive directions = transverse states')
# one-mode quartet Gram signature
qq = [idx[s] for s in [(0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)]]
ev = np.linalg.eigvalsh(Gm[np.ix_(qq, qq)])
report(np.sum(ev > 1e-9) == 2 and np.sum(ev < -1e-9) == 2, 'one-particle quartet {K,H,C,Cb}: Gram signature (2,2), no definite norm', str(np.round(ev, 6)))
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
