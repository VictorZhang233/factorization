"""N14 (i): checks behind 'Assumption E.18(iii) (alpha_i = beta_i, Hermiticity of the cut rules) is provable'.
Conventions: Peskin-Schroeder (P&S) Feynman rules, all Lagrangian coefficients real (incl. L_FP = cbar(-d.D)c).
Lemma E.24 needs: a vertex left of the cut has factor -i v, the same vertex (same forward-graph momenta, same
on-shell numerators) right of the cut has +i v.

(a) quark-gluon vertex: conjugate side (Dirac conjugation in the forward-graph trace) gamma^0 V^dagger gamma^0 = -V.
(b) three-gluon vertex: real and odd in the momenta; in the forward-graph orientation the conjugate-side momenta are
    minus the physical momenta of M^*, so V_conj = V(-p)^* = -V(p).
(c) Veltman's largest-time (circling) rule, which is what Lemma E.24 encodes: circled vertex = (i*coefficient)^* times
    the SAME momentum factors -> = -V for every real-coefficient vertex (incl. the P&S ghost vertex).
(d) ghost vertex in the 'physical M^*' picture (momentum reversal + reversed ghost arrow): V_conj = -V_amp - g f q^mu
    (fails vertex by vertex), but closed ghost loops summed over both orientations agree with the circling rule.
Run: python3 -I -u n14_cut_rules.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(3)
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + name + ('   [' + detail + ']' if detail else ''), flush=True)

# Dirac matrices (Dirac rep), metric (+,-,-,-)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gam = [g0] + gs
eta = np.diag([1., -1., -1., -1.])
# SU(3) generators and structure constants
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2])/np.sqrt(3)
t = lam/2
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = t[a] @ t[b] - t[b] @ t[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j*np.trace(comm @ t[c]))
report(np.allclose(np.einsum('abc->bca', f), f) and np.allclose(f, -np.einsum('abc->bac', f)), 'f^{abc} totally antisymmetric, [t^a,t^b] = i f^{abc} t^c')
g = 0.83

# (a) quark-gluon vertex
ok = True
for mu in range(4):
    for a in range(8):
        V = 1j*g*np.kron(gam[mu], t[a])
        Vc = np.kron(g0, np.eye(3)) @ V.conj().T @ np.kron(g0, np.eye(3))
        ok &= np.allclose(Vc, -V)
report(ok, '(a) quark-gluon: gamma0 (i g gamma^mu t^a)^dagger gamma0 = -(i g gamma^mu t^a): -iv | +iv with the same v')

# (b) three-gluon vertex (P&S): g f^{abc}[g^{mu nu}(k-p)^rho + g^{nu rho}(p-q)^mu + g^{rho mu}(q-k)^nu], all momenta incoming
def V3(k, p, q):
    # returns array [a,b,c,mu,nu,rho] (upper indices, metric eta)
    gm = eta
    T = (np.einsum('mn,r->mnr', gm, k - p) + np.einsum('nr,m->mnr', gm, p - q) + np.einsum('rm,n->mnr', gm, q - k))
    return g*np.einsum('abc,mnr->abcmnr', f, T)
k = rng.normal(size=4); p = rng.normal(size=4); q = -k - p
Va = V3(k, p, q); Vb = V3(-k, -p, -q)
report(np.allclose(Va.imag, 0) and np.allclose(Vb, -Va), '(b) three-gluon vertex real and odd: conjugate side V(-p)^* = -V(p)')

# (c) circling rule for the ghost vertex (P&S: -g f^{abc} p^mu, p = outgoing ghost momentum): real coefficient
#     -> circled vertex = (i*coeff)^* * (same momentum factor) = -V
def Vgh(a, b, c, pout):
    return -g*f[a, b, c]*pout
pout = rng.normal(size=4)
coeff_times_i = 1j*(-g*f[1, 4, 6])          # i * Lagrangian coefficient
mom = -1j*pout                               # derivative factor (-i p) on the antighost leg
unc = coeff_times_i*mom; circ = np.conj(coeff_times_i)*mom
report(np.allclose(unc.imag, 0) and np.allclose(circ, -unc) and np.allclose(unc, Vgh(1, 4, 6, pout)),
       '(c) circling rule: P&S ghost vertex is real; circled = -uncircled (alpha=beta) with momentum factors unchanged')

# (d) 'physical M^*' picture for the ghost vertex: momentum reversal + reversed ghost arrow
#     forward graph: ghost enters along a (k_a), leaves along b (k_b), gluon q in, k_a + q = k_b
ka = rng.normal(size=4); qg = rng.normal(size=4); kb = ka + qg
ca, cg, cb = 0, 1, 2      # f^{123} != 0
V_amp = -g*f[cb, cg, ca]*kb
V_Mstar = -g*f[ca, cg, cb]*ka               # in M^*: arrow b->a, outgoing ghost momentum (physical) = k_a
V_conj_phys = np.conj(V_Mstar)
diff = V_conj_phys - (-V_amp)
report(np.allclose(diff, -g*f[cb, cg, ca]*qg) and not np.allclose(diff, 0),
       '(d) ghost vertex in the M^* picture: V_conj = -V_amp - g f q^mu (alpha != beta vertex by vertex)')
# closed ghost loop: sum over both orientations, M^*-rule (+g f k_in) vs circling rule (+g f k_out)
def loop_value(qs, eps_list, rule):
    n = len(qs)
    l = np.array([0.3, -0.7, 0.2, 0.5])          # loop momentum (ghost entering vertex 0 in orientation 1)
    total = 0
    for orient in (+1, -1):
        # orientation +1: ghost momenta k_i entering vertex i, k_{i+1} = k_i + q_i leaving
        # orientation -1: reversed arrow: entering momentum at vertex i is -k_{i+1}, leaving -k_i
        ks = [l]
        for i in range(n): ks.append(ks[-1] + qs[i])
        val = np.zeros((8,)*n, complex)
        for cols in itertools.product(range(8), repeat=n):     # internal ghost colours a_0..a_{n-1}; gluon colours fixed below
            pass
        # contract colours explicitly: gluon colours b_i fixed to random choices
        bcol = [0, 1, 2] if n == 3 else [1, 3, 6, 2]     # colour choices with non-vanishing loop colour factor
        amp = 0
        for acol in itertools.product(range(8), repeat=n):
            term = 1.0
            for i in range(n):
                a_in = acol[i]; a_out = acol[(i+1) % n]
                if orient == +1:
                    kin, kout = ks[i], ks[i+1]
                    cin, cout = a_in, a_out
                else:
                    kin, kout = -ks[i+1], -ks[i]
                    cin, cout = a_out, a_in
                mom = kout if rule == 'circ' else kin
                term *= g*f[cout, bcol[i], cin]*np.dot(eta @ mom, eps_list[i])
                if term == 0: break
            amp += term
        props = np.prod([1j/np.dot(eta @ kk, kk) for kk in ks[:n]])
        total += amp*props
    return total
for n in (3, 4):
    qs = [rng.normal(size=4) for _ in range(n-1)]; qs.append(-sum(qs))
    eps_list = [rng.normal(size=4) for _ in range(n)]
    a = loop_value(qs, eps_list, 'circ'); b = loop_value(qs, eps_list, 'mstar')
    report(np.isclose(a, b) and abs(a) > 1e-8, f'(d) closed ghost loop with {n} gluons: sum over orientations, M^*-rule = circling rule', f'{a:.6e} vs {b:.6e}')

print(f'\nSUMMARY: {npass}/{npass+nfail} PASS')
