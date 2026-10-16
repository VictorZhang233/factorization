"""W02 / Ch2 + App J check s4: tree-level q qbar -> g g with the Feynman rules of def:prelim-feynman-rules:
 (1) k1_mu A^{mu nu} = (g^2 f^{abc}/Q^2)(k2^2 g^{nu s} - k2^nu k2^s) J_{c s}  (off-shell gluons), A = sum of graphs (= iM);
 (2) k1_mu k2_nu A^{mu nu} = 0; k1_mu eps2_nu A = 0 for a physical on-shell gluon 2;
 (3) k1_mu kbar2_nu A^{mu nu} = (k2.kbar2) A_gh, A_gh = g^2 f^{abc} k1.J_c / Q^2 = amplitude q qbar -> c^a(k1) cbar^b(k2);
 (4) sum_phys |A|^2 = sum_{-g,-g} |A|^2 - 2 sum |A_gh|^2 ;  (1/36) sum_phys |A|^2 = g^4[32/27 (t^2+u^2)/(tu) - 8/3 (t^2+u^2)/s^2];
 (5) App J: closed ghost loops: 'outgoing-momentum' rule summed over both orientations = 'incoming-momentum' rule summed
     over both orientations (pointwise in the loop momentum); circled real-coefficient vertices = - uncircled;
     ghost vertex read as physical M^*:  V_conj = -V_amp - g f q^mu.
Run: python3 -I s4_qqgg_ghosts.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(11)
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
eta = np.diag([1., -1, -1, -1])
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gam = [g0] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
def sl(p): return sum(eta[m, m] * p[m] * gam[m] for m in range(4))
def dot(a, b): return a @ eta @ b
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j; lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j; lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam / 2
f = np.zeros((8, 8, 8))
for a, b, c in itertools.product(range(8), repeat=3):
    f[a, b, c] = np.real(-2j * np.trace((T[a] @ T[b] - T[b] @ T[a]) @ T[c]))
g = 1.0
def spinors(p):
    """massless u(p, s), v(p, s) via projection (any normalisation with sum u ubar = pslash)"""
    P = sl(p)
    us = []; vs = []
    for chi in (np.array([1, 0, 0, 0], complex), np.array([0, 1, 0, 0], complex), np.array([0, 0, 1, 0], complex), np.array([0, 0, 0, 1], complex)):
        us.append(P @ chi)
    # orthonormalise w.r.t. ubar u... use completeness instead: return the matrix pslash for traces
    return P
def V3(k, mu, a, p, nu, b, q, rho, c):
    """three-gluon vertex, all momenta incoming, Lorentz indices upper (as numbers)"""
    gm = eta
    return g * f[a, b, c] * (gm[mu, nu] * (k - p)[rho] + gm[nu, rho] * (p - q)[mu] + gm[rho, mu] * (q - k)[nu])
def S(p): return 1j * sl(p) / dot(p, p)
def Dg(k, xi=1.0):
    return -1j / dot(k, k) * (np.linalg.inv(eta) - (1 - xi) * np.outer(k, k) / dot(k, k))
def amplitude_matrix(p1, p2, k1, k2, a, b, xi=1.0):
    """A^{mu nu}_{ab} as a Dirac (x colour) matrix sandwiched later between vbar(p2) ... u(p1); returns [mu][nu] of
       matrices in Dirac x colour space (12x12)."""
    A = np.zeros((4, 4, 12, 12), complex)
    Q = p1 + p2
    for mu in range(4):
        for nu in range(4):
            # t-channel: vbar (i g gamma^nu t^b) S(p1-k1) (i g gamma^mu t^a) u
            M = np.kron(1j * g * gam[nu] @ S(p1 - k1) @ (1j * g * gam[mu]), T[b] @ T[a])
            # u-channel
            M += np.kron(1j * g * gam[mu] @ S(p1 - k2) @ (1j * g * gam[nu]), T[a] @ T[b])
            # s-channel: vbar (i g gamma^r t^c) u * D_{r s}(Q) * V3[(Q, s, c), (-k1, mu, a), (-k2, nu, b)]
            Dq = Dg(Q, xi)
            for c in range(8):
                if f[c, a, b] == 0: continue
                for r in range(4):
                    for s in range(4):
                        if Dq[r, s] == 0: continue
                        v = V3(Q, s, c, -k1, mu, a, -k2, nu, b)
                        if v == 0: continue
                        M += np.kron(1j * g * gam[r], T[c]) * (eta[r, r] * Dq[r, s] * eta[s, s]) * v
            A[mu, nu] = M
    return A
def contract(A, e1, e2):
    """A^{mu nu} e1_mu e2_nu (e given with upper components; lower via metric)"""
    return sum(A[m, n] * (eta[m, m] * e1[m]) * (eta[n, n] * e2[n]) for m in range(4) for n in range(4))
def Jc(p1, p2, c, e):
    """J_c . e  matrix = gamma.e t^c"""
    return np.kron(sl(e), T[c])
# ---------------- random kinematics ----------------
def massless(E, th, ph):
    return E * np.array([1, np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
p1 = massless(3.0, 0.4, 0.9); p2 = massless(2.0, 2.2, 3.5)
Q = p1 + p2
# external spinors: work with traces; build |A|^2 sums via traces with pslash, and amplitudes via random spinors
def u_spinor(p):
    P = sl(p); w, V = np.linalg.eig(P @ g0)
    # pick eigenvectors of pslash gamma0 ... simpler: u = pslash chi for a fixed chi (not normalised) -- fine for linear identities
    return P @ np.array([1, 0.3, -0.2j, 0.5], complex)
def v_spinor(p):
    return sl(p) @ np.array([0.2, 1, 0.4j, -0.3], complex)
up = u_spinor(p1); vp = v_spinor(p2)
vbar = vp.conj() @ g0
colq = rng.normal(size=3) + 1j * rng.normal(size=3); colqb = rng.normal(size=3) + 1j * rng.normal(size=3)
def sand(M):
    return np.kron(vbar, colqb.conj()) @ M @ np.kron(up, colq)
# (1) off-shell identity
k1 = rng.normal(size=4); k2 = Q - k1
a, b = 0, 1
A = amplitude_matrix(p1, p2, k1, k2, a, b)
ok = True
for nu in range(4):
    lhs = sand(sum(A[m, nu] * eta[m, m] * k1[m] for m in range(4)))
    rhs = 0
    for c in range(8):
        if f[a, b, c] == 0: continue
        for s_ in range(4):
            coeff = g**2 * f[a, b, c] / dot(Q, Q) * (dot(k2, k2) * (eta[nu, s_] if True else 0) - k2[nu] * k2[s_])
            # J_{c s} = vbar gamma_s t^c u  (lower index s): gamma_s = eta_ss gamma^s
            rhs += coeff * sand(np.kron(eta[s_, s_] * gam[s_], T[c])) * 1.0
    ok &= np.isclose(lhs, rhs)
report(ok, '(1) k1_mu A^{mu nu} = (g^2 f^abc/Q^2)(k2^2 g^{nu s} - k2^nu k2^s) J_{c s}  (off-shell gluons; A = sum of graphs)')
lhs2 = sand(sum(A[m, n] * eta[m, m] * k1[m] * eta[n, n] * k2[n] for m in range(4) for n in range(4)))
report(abs(lhs2) < 1e-10, '(2) k1_mu k2_nu A^{mu nu} = 0 for off-shell gluons and on-shell quarks')
# on-shell gluons
def onshell_pair(Q):
    # Q in c.m. frame? construct back-to-back massless k1, k2 with k1 + k2 = Q
    M = np.sqrt(dot(Q, Q)); beta = Q[1:] / Q[0]
    th, ph = 1.1, 0.7
    kc = M / 2 * np.array([1, np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    kc2 = M / 2 * np.array([1, -np.sin(th) * np.cos(ph), -np.sin(th) * np.sin(ph), -np.cos(th)])
    # boost from rest frame of Q
    bb = beta; b2 = bb @ bb; gm_ = 1 / np.sqrt(1 - b2)
    def boost(v):
        t0 = v[0]; x = v[1:]
        bp = bb @ x
        t1 = gm_ * (t0 + bp)
        x1 = x + ((gm_ - 1) * bp / b2 + gm_ * t0) * bb
        return np.concatenate([[t1], x1])
    return boost(kc), boost(kc2)
k1, k2 = onshell_pair(Q)
report(abs(dot(k1, k1)) < 1e-9 and abs(dot(k2, k2)) < 1e-9 and np.allclose(k1 + k2, Q), 'on-shell kinematics: k1^2 = k2^2 = 0, k1 + k2 = p1 + p2')
def kbar(k):
    return np.array([k[0], -k[1], -k[2], -k[3]])
def transverse(k):
    """two real polarisation vectors with e.k = e.kbar = 0, e.e = -1"""
    n = k[1:] / np.linalg.norm(k[1:])
    t1 = np.cross(n, [0.3, 0.1, 0.9]); t1 /= np.linalg.norm(t1); t2 = np.cross(n, t1)
    return [np.concatenate([[0], t1]), np.concatenate([[0], t2])]
eps1 = transverse(k1); eps2 = transverse(k2)
ok = True
for a, b in [(0, 1), (2, 4), (3, 3), (7, 5)]:
    A = amplitude_matrix(p1, p2, k1, k2, a, b)
    for e2 in eps2:
        ok &= abs(sand(contract(A, k1, e2))) < 1e-9
report(ok, '(2) on shell: k1_mu eps2_nu A^{mu nu} = 0 for physical gluon 2 (single longitudinal gluon decouples)')
# (3) unphysical pair and the ghost amplitude
ok = True
for a, b in [(0, 1), (2, 4), (3, 6)]:
    A = amplitude_matrix(p1, p2, k1, k2, a, b)
    lhs = sand(contract(A, k1, kbar(k2)))
    Agh = sum(g**2 * f[a, b, c] / dot(Q, Q) * sand(np.kron(sl(k1), T[c])) for c in range(8))
    ok &= np.isclose(lhs, dot(k2, kbar(k2)) * Agh)
report(ok, '(3) k1_mu kbar2_nu A^{mu nu} = (k2.kbar2) A_gh,  A_gh = g^2 f^abc (k1.J_c)/Q^2 (sign fixed by the rules)')
# Feynman-rule derivation of A_gh: [vbar (i g gamma^r t^c) u] (-i g_{rs}/Q^2) (-g f^{a c b} k1^s)
ok = True
for a, b in [(0, 1), (2, 4)]:
    Agh_rule = sum(sand(np.kron(1j * g * sl(k1), T[c])) * (-1j / dot(Q, Q)) * (-g * f[a, c, b]) for c in range(8))
    Agh = sum(g**2 * f[a, b, c] / dot(Q, Q) * sand(np.kron(sl(k1), T[c])) for c in range(8))
    ok &= np.isclose(Agh_rule, Agh)
report(ok, '(3) A_gh from the ghost-gluon vertex -g f^{a c b} k1 (outgoing ghost a, momentum k1) agrees')
# (4) polarisation sums with traces over spins and colours
def sum_abs2(e1list, e2list, metric_sum=False):
    tot = 0
    for a in range(8):
        for b in range(8):
            A = amplitude_matrix(p1, p2, k1, k2, a, b)
            if metric_sum:
                # sum_{mu nu mu' nu'} A^{mu nu} (-g_{mu mu'}) (-g_{nu nu'}) A^{mu' nu' *}
                for m in range(4):
                    for n in range(4):
                        M = A[m, n] * eta[m, m] * eta[n, n]
                        # spin/colour sum: Tr[ M (p1slash x 1) Mbar (p2slash x 1) ]
                        Mb = np.kron(g0, np.eye(3)) @ A[m, n].conj().T @ np.kron(g0, np.eye(3))
                        tot += np.trace(M @ np.kron(sl(p1), np.eye(3)) @ Mb @ np.kron(sl(p2), np.eye(3))) * 1.0
            else:
                for e1 in e1list:
                    for e2 in e2list:
                        M = contract(A, e1, e2)
                        Mb = np.kron(g0, np.eye(3)) @ M.conj().T @ np.kron(g0, np.eye(3))
                        tot += np.trace(M @ np.kron(sl(p1), np.eye(3)) @ Mb @ np.kron(sl(p2), np.eye(3)))
    return tot.real
def sum_ghost2():
    tot = 0
    for a in range(8):
        for b in range(8):
            M = sum(g**2 * f[a, b, c] / dot(Q, Q) * np.kron(sl(k1), T[c]) for c in range(8))
            Mb = np.kron(g0, np.eye(3)) @ M.conj().T @ np.kron(g0, np.eye(3))
            tot += np.trace(M @ np.kron(sl(p1), np.eye(3)) @ Mb @ np.kron(sl(p2), np.eye(3)))
    return tot.real
phys = sum_abs2(eps1, eps2)
metric = sum_abs2(None, None, metric_sum=True)
gh = sum_ghost2()
report(np.isclose(phys, metric - 2 * gh), '(4) sum_phys |A|^2 = sum_{-g,-g} |A|^2 - 2 sum |A_gh|^2',
       f'{phys:.10f} vs {metric - 2 * gh:.10f}; ghost part {gh:.6f}')
s = dot(Q, Q); tt_ = dot(p1 - k1, p1 - k1); uu = dot(p1 - k2, p1 - k2)
ckr = g**4 * (32 / 27 * (tt_**2 + uu**2) / (tt_ * uu) - 8 / 3 * (tt_**2 + uu**2) / s**2)
report(np.isclose(phys / 36, ckr), '(4) (1/36) sum_phys |A|^2 = g^4 [32/27 (t^2+u^2)/(tu) - 8/3 (t^2+u^2)/s^2]  (VF-WL-9, CKR 1977)',
       f'{phys / 36:.12f} vs {ckr:.12f}')
report(not np.isclose(phys, metric), '(4) without the ghost subtraction the -g sum is NOT the physical sum')
# gauge-parameter independence of the physical sum (s-channel gluon propagator in general xi)
def sum_phys_xi(xi):
    tot = 0
    for a in range(8):
        for b in range(8):
            A = amplitude_matrix(p1, p2, k1, k2, a, b, xi)
            for e1 in eps1:
                for e2 in eps2:
                    M = contract(A, e1, e2)
                    Mb = np.kron(g0, np.eye(3)) @ M.conj().T @ np.kron(g0, np.eye(3))
                    tot += np.trace(M @ np.kron(sl(p1), np.eye(3)) @ Mb @ np.kron(sl(p2), np.eye(3)))
    return tot.real
report(np.isclose(sum_phys_xi(0.0), phys) and np.isclose(sum_phys_xi(3.0), phys), 'physical |A|^2 independent of xi (Landau, Feynman, xi = 3)')
# (5) ghost loops: out-rule vs in-rule summed over orientations; vertex conjugation
def ghost_loop(qs, es, cols, rule, orient, l):
    n = len(qs)
    ks = [l]
    for i in range(n): ks.append(ks[-1] + qs[i])   # ks[i] enters vertex i, ks[i+1] leaves (orientation +1)
    val = 0
    for xs_ in itertools.product(range(8), repeat=n):
        term = 1.0
        for i in range(n):
            if orient == +1:
                kin, kout = ks[i], ks[i + 1]; cin, cout = xs_[i], xs_[(i + 1) % n]
            else:
                kin, kout = -ks[i + 1], -ks[i]; cin, cout = xs_[(i + 1) % n], xs_[i]
            p_ = kout if rule == 'out' else kin
            term *= -g * f[cout, cols[i], cin] * dot(p_, es[i])
            if term == 0: break
        val += term
    props = np.prod([1j / dot(kk, kk) for kk in ks[:n]])
    return -val * props
for n in (3, 4):
    qs = [rng.normal(size=4) for _ in range(n - 1)]; qs.append(-sum(qs))
    es = [rng.normal(size=4) for _ in range(n)]
    cols = [0, 1, 2] if n == 3 else [0, 1, 3, 4]
    l = rng.normal(size=4)
    out_p = ghost_loop(qs, es, cols, 'out', +1, l); out_m = ghost_loop(qs, es, cols, 'out', -1, l)
    in_p = ghost_loop(qs, es, cols, 'in', +1, l); in_m = ghost_loop(qs, es, cols, 'in', -1, l)
    report(np.isclose(in_m, out_p) and np.isclose(in_p, out_m) and abs(out_p + out_m) > 1e-8 and not np.isclose(out_p, in_p),
           f'(5) {n}-gluon ghost loop: in-rule(reversed) = out-rule pointwise, so both rules agree after summing orientations',
           f'out+out = {out_p + out_m:.6e}, in+in = {in_p + in_m:.6e}')
# vertex conjugation rules
ok = True
for mu in range(4):
    for a in range(8):
        V = 1j * g * np.kron(gam[mu], T[a])
        Vc = np.kron(g0, np.eye(3)) @ V.conj().T @ np.kron(g0, np.eye(3))
        ok &= np.allclose(Vc, -V)
report(ok, '(5) quark-gluon vertex: gamma0 (i g gamma^mu t^a)^dagger gamma0 = -(i g gamma^mu t^a)')
kk = rng.normal(size=4); pp = rng.normal(size=4); qq = -kk - pp
ok = True
for (m, n_, r) in itertools.product(range(4), repeat=3):
    for (a, b, c) in [(0, 1, 2), (3, 4, 7), (1, 5, 6)]:
        v = V3(kk, m, a, pp, n_, b, qq, r, c); vneg = V3(-kk, m, a, -pp, n_, b, -qq, r, c)
        ok &= np.isclose(np.imag(v), 0) and np.isclose(vneg, -v)
report(ok, '(5) three-gluon vertex real and odd in the momenta: V(-k)^* = -V(k)')
ka = rng.normal(size=4); qg = rng.normal(size=4); kb = ka + qg
ca, cg, cb = 0, 1, 2
Vamp = -g * f[cb, cg, ca] * kb                     # outgoing ghost cb with momentum kb
Vmstar = np.conj(-g * f[ca, cg, cb] * ka)          # M^* reading: arrow reversed, physical outgoing momentum ka
report(np.allclose(Vmstar, -Vamp - g * f[cb, cg, ca] * qg) and not np.allclose(Vmstar, -Vamp),
       '(5) ghost vertex read as physical M^*: V_conj = -V_amp - g f q^mu (not -V_amp vertex by vertex)')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
