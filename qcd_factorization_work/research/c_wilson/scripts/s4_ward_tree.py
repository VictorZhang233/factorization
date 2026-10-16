"""
s4_ward_tree.py -- item (4): tree-level Ward identities with explicit Dirac matrices, spinors, SU(3).

(a) elementary identities
     S(p+k) (i g kslash) S(p) = g [S(p+k) - S(p)]                         (any p, k, m)
     ubar(p') i g kslash S(p'-k) = g ubar(p'),   S(p+k) i g kslash u(p) = -g u(p)   (external on-shell ends)
     q1_mu V^{mu nu rho}_{abc}(q1,q2,q3) = g f^{abc}[(q3^2 g - q3 q3)^{nu rho} - (q2^2 g - q2 q2)^{nu rho}]
(b) one scalar-polarized gluon (k^mu, colour a, k flowing in) inserted in all n+1 positions of an open quark line
     ubar(p') V_n S ... S V_1 u(p) with on-shell ends:  abelian sum = 0;  non-abelian:
        sum = g sum_r [line with gluon r -> momentum q_r + k, colour [t^a, t^{b_r}]]
(c) gamma*(q) -> q(p1) qbar(p2) g(k): eps -> k gives zero on shell (massless/massive); squared matrix element
     sum|M|^2 = 8 N_c C_F g^2 (x1^2+x2^2)/((1-x1)(1-x2)) (unit photon coupling, -g photon sum) [ERT/ESW]
(d) antiquark leg off shell (open Dirac index X, p2^2 != 0):
        term on the on-shell quark alone:  -g t^a ubar(p1) gamma^nu X       (hard part H: exact, eikonal form)
        full sum:  -g t^a ubar(p1) gamma^nu S(-p2-k) S(-p2)^{-1} X          (endpoint/contact term)
(e) DIS seed of the PDF Wilson line: H^mu = ubar(p') i g gamma^mu t^a S(p'-k) Gamma (k flowing in, incoming quark
     leg off shell):  k_mu H^mu = g t^a ubar(p') Gamma = g t^a H_0 ;  with the K projector
     k^mu n^alpha/(n.k - i0): H.K = [g t^a n^alpha/(n.k - i0)] H_0 = first-order term of W_n[inf,0] times H_0
(f) two K-gluons on the DIS hard part: exact
        k1_mu k2_nu H^{mu nu}_{ab} = g^2 t^b t^a H_0 + i g^2 [t^a,t^b] ubar kslash_2 S(p'-k1-k2) Gamma
     and for exactly collinear khat_i (khat_i^2 = 0, khat_1 || khat_2):
        = (n.k1)(n.k2) * [second-order term of W_n[inf,0]] * H_0 ,   n = (0,1,0_T)  (n.k = k^+)
(g) non-abelian q(p1) qbar(p2) -> g*(k1,a,mu) g*(k2,b,nu) (t, u, s channels; on-shell quarks, off-shell gluons):
        k1_mu A^{mu nu}_{ab} = (g^2 f^{abc}/Q^2) (k2^2 g^{nu s} - k2^nu k2^s) J_{c s},  J_c = vbar gamma t^c u
     => 0 for physical gluon 2; k1 k2 A = 0 even off shell; k1 kbar2 A = (k2.kbar2) A_ghost != 0;
     sum_phys |A|^2 = sum_{-g,-g} |A|^2 - 2 sum |A_ghost|^2; spin/colour-averaged physical result equals
     g^4 [32/27 (t^2+u^2)/(t u) - 8/3 (t^2+u^2)/s^2]  (Combridge et al. 1977; ESW Table 7.1).
(h) gamma* -> q qbar g*(k1,a) g*(k2,b), all 8 tree diagrams:
        k1_mu A^{mu nu}_{ab} = (i g f^{abc}/Q^2)(k2^nu k2^s - k2^2 g^{nu s}) A^c_s(Q)   [A^c_s(Q): one-gluon amplitude]
     => k1_mu k2_nu A^{mu nu} = 0 for off-shell gluons (BRST statement for two longitudinal gluons).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *

R = Report('s4_ward_tree')
g = 1.0
rng = np.random.default_rng(2718)


def boost_from_rest(Q, pstar):
    """boost pstar (given in the rest frame of Q) to the frame where Q has its given momentum"""
    M = np.sqrt(mdot(Q, Q)); beta = Q[1:] / Q[0]; gam = Q[0] / M
    b2 = beta @ beta
    E = pstar[0]; pv = pstar[1:]
    bp = beta @ pv
    E2 = gam * (E + bp)
    pv2 = pv + ((gam - 1) * bp / b2 + gam * E) * beta if b2 > 0 else pv
    return np.concatenate([[E2], pv2])


def two_body(Q, m1, m2, rng):
    M = np.sqrt(mdot(Q, Q))
    pst = np.sqrt((M**2 - (m1 + m2)**2) * (M**2 - (m1 - m2)**2)) / (2 * M)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    a = np.concatenate([[np.sqrt(m1**2 + pst**2)], pst * n])
    b = np.concatenate([[np.sqrt(m2**2 + pst**2)], -pst * n])
    return boost_from_rest(Q, a), boost_from_rest(Q, b)


# ===================================================================================== (a)
print('--- (a) elementary identities ---')
for M in [0.0, 0.7]:
    p = rand_vec(rng); k = rand_vec(rng)
    lhs = S_quark(p + k, M) @ (1j * g * slash(k)) @ S_quark(p, M)
    R.check(f'(a) S(p+k) i g kslash S(p) = g[S(p+k)-S(p)]  (m={M})', rel(lhs, g * (S_quark(p + k, M) - S_quark(p, M))), 1e-12)
    R.check(f'(a) S explicit == i/(pslash-m)  (m={M})', rel(S_quark(p, M), S_quark_explicit(p, M)), 1e-12)
    pp = rand_massive(rng, M) if M > 0 else rand_massless(rng); k = rand_vec(rng)
    for s in range(2):
        R.check(f'(a) ubar(p\') i g kslash S(p\'-k) = g ubar(p\')  (m={M}, s={s})',
                rel(bar(u_spinor(pp, s, M)) @ (1j * g * slash(k)) @ S_quark(pp - k, M), g * bar(u_spinor(pp, s, M))), 1e-12)
        R.check(f'(a) S(p+k) i g kslash u(p) = -g u(p)  (m={M}, s={s})',
                rel(S_quark(pp + k, M) @ (1j * g * slash(k)) @ u_spinor(pp, s, M), -g * u_spinor(pp, s, M)), 1e-12)
        R.check(f'(a) vbar(p) i g kslash S(-p-k) = +g vbar(p)  (m={M}, s={s})',
                rel(bar(v_spinor(pp, s, M)) @ (1j * g * slash(k)) @ S_quark(-pp - k, M), g * bar(v_spinor(pp, s, M))), 1e-12)
        R.check(f'(a) S(-p+k) i g kslash v(p) = -g v(p)  (m={M}, s={s})',
                rel(S_quark(-pp + k, M) @ (1j * g * slash(k)) @ v_spinor(pp, s, M), -g * v_spinor(pp, s, M)), 1e-12)
# three-gluon vertex contracted with q1
q1 = rand_vec(rng); q2 = rand_vec(rng); q3 = -q1 - q2
errmax = 0
for (a, b, c) in [(0, 1, 2), (3, 4, 7), (1, 5, 6), (2, 3, 6)]:
    V = V3(a, q1, b, q2, c, q3, g)
    lhs = np.einsum('m,mnr->nr', lower(q1), V)
    Pi = lambda q: mdot(q, q) * METRIC - np.outer(q, q)        # (q^2 g^{nu rho} - q^nu q^rho)
    rhs = g * FABC[a, b, c] * (Pi(q3) - Pi(q2))
    if abs(FABC[a, b, c]) > 0:
        errmax = max(errmax, rel(lhs, rhs))
R.check('(a) q1_mu V^{mu nu rho}(q1,q2,q3) = g f^{abc}[Pi(q3) - Pi(q2)],  Pi(q) = q^2 g - q q', errmax, 1e-12)

# ===================================================================================== (b)
print('--- (b) K-gluon inserted in all positions of an open on-shell quark line ---')
for M in [0.0, 0.5]:
    for n in [1, 2, 3]:
        pin = rand_massive(rng, M) if M > 0 else rand_massless(rng)
        qs = [rand_vec(rng, 0.7) for _ in range(n)]
        epss = [rand_vec(rng, 1.0, cplx=True) for _ in range(n)]
        bs = list(rng.integers(0, 8, size=n))
        # outgoing momentum fixed by conservation: choose k such that p' = pin + sum q + k is on shell
        # -> pick p' on shell first, then k = p' - pin - sum(q)
        pout = rand_massive(rng, M) if M > 0 else rand_massless(rng)
        k = pout - pin - sum(qs)
        a = 5
        sp_, sp2 = 0, 1
        uin = u_spinor(pin, sp_, M); ubo = bar(u_spinor(pout, sp2, M))

        def line_amp(verts, moms, cols_):
            """ubar(pout) V_last S ... S V_1 u(pin) as (scalar, colour matrix) with momenta flowing in"""
            X = uin.copy(); C = I3.copy(); l = pin.copy()
            for i, (V, q, T) in enumerate(zip(verts, moms, cols_)):
                X = V @ X; C = T @ C
                l = l + q
                if i < len(verts) - 1:
                    X = S_quark(l, M) @ X
            return ubo @ X, C

        verts = [1j * g * slash(e) for e in epss]
        # generic colour matrices c^b t^b (the identity is linear in each colour matrix; single generators can give
        # identically vanishing colour products, which would make the test vacuous)
        cols = [np.einsum('b,bij->ij', rng.normal(size=8), TA) for b in bs]
        Tk = np.einsum('b,bij->ij', rng.normal(size=8), TA)
        tot_s = 0; tot_c = np.zeros((3, 3), dtype=complex); tot_ab = 0; scale = 0
        for r in range(n + 1):
            vv = verts[:r] + [1j * g * slash(k)] + verts[r:]
            mm = qs[:r] + [k] + qs[r:]
            cc = cols[:r] + [Tk] + cols[r:]
            s_, C_ = line_amp(vv, mm, cc)
            tot_c += s_ * C_
            tot_ab += s_
            scale = max(scale, np.abs(s_ * C_).max())
        R.check(f'(b) abelian: sum over {n+1} insertions = 0  (m={M}, n={n})', abs(tot_ab) / max(abs(s_), 1e-300), 1e-11)
        # non-abelian prediction: g sum_r line with vertex r carrying q_r + k and colour [t^a, t^{b_r}]
        pred = np.zeros((3, 3), dtype=complex)
        for r in range(n):
            mm = qs[:r] + [qs[r] + k] + qs[r + 1:]
            cc = cols[:r] + [Tk @ cols[r] - cols[r] @ Tk] + cols[r + 1:]
            s_, C_ = line_amp(verts, mm, cc)
            pred += g * s_ * C_
        R.check(f'(b) non-abelian: sum = g sum_r [gluon r -> (q_r+k, [T_K,T_r])]  (m={M}, n={n}, generic colour matrices)',
                np.abs(tot_c - pred).max() / scale, 1e-11, '(normalized to one insertion)')

# ===================================================================================== (c)
print('--- (c) gamma* -> q qbar g ---')


def amp_qqg(p1, p2, k, M, s1, s2, X=None, part='both'):
    """Dirac part, Lorentz indices (mu = gluon, nu = photon): A[mu][nu]; colour t^a factored out.
       X = right spinor (default v(p2)); for an off-shell antiquark leg supply X and off-shell p2."""
    ub = bar(u_spinor(p1, s1, M))
    vv = v_spinor(p2, s2, M) if X is None else X
    A = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        for nu in range(4):
            t1 = ub @ (1j * g * GAM[mu]) @ S_quark(p1 + k, M) @ GAM[nu] @ vv
            t2 = ub @ GAM[nu] @ S_quark(-p2 - k, M) @ (1j * g * GAM[mu]) @ vv
            A[mu, nu] = {'both': t1 + t2, 'quark': t1, 'antiquark': t2}[part]
    return A


def contract_first(vec, A):
    """vec_mu A^{mu nu} (A with upper indices)"""
    return np.einsum('m,mn->n', lower(vec), A)


for M in [0.0, 0.6]:
    worst = 0
    for trial in range(4):
        p1 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
        p2 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
        k = rand_massless(rng)
        for s1 in range(2):
            for s2 in range(2):
                A = amp_qqg(p1, p2, k, M, s1, s2)
                At = amp_qqg(p1, p2, k, M, s1, s2, part='quark')
                worst = max(worst, np.abs(contract_first(k, A)).max() / np.abs(contract_first(k, At)).max())
    R.check(f'(c) k_mu A^{{mu nu}} = 0 on shell, all nu, spins (m={M}); normalized to one diagram', worst, 1e-12)

# squared matrix element vs (x1^2+x2^2)/((1-x1)(1-x2))
vals = []
for trial in range(5):
    p1 = rand_massless(rng); p2 = rand_massless(rng); k = rand_massless(rng)
    q = p1 + p2 + k; Q2 = mdot(q, q)
    x1 = 2 * mdot(p1, q) / Q2; x2 = 2 * mdot(p2, q) / Q2
    tot = 0
    for s1 in range(2):
        for s2 in range(2):
            A = amp_qqg(p1, p2, k, 0.0, s1, s2)
            # photon: -g_{nu nu'} ; gluon: -g_{mu mu'} (abelian-like single gluon: allowed by (c))
            tot += np.real(np.einsum('mn,ab,ma,nb->', np.conj(A), A, -METRIC, -METRIC))
    tot *= 4.0  # colour: Tr(t^a t^a) = N_c C_F = 4
    vals.append(tot / (8 * 4.0 * g**2 * (x1**2 + x2**2) / ((1 - x1) * (1 - x2))))
R.check('(c) sum|M|^2 == 8 N_c C_F g^2 (x1^2+x2^2)/((1-x1)(1-x2))  [ERT/ESW]  (ratio-1)', max(abs(np.array(vals) - 1)), 1e-12)

# ===================================================================================== (d)
print('--- (d) antiquark leg off shell ---')
for M in [0.0, 0.6]:
    p1 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    p2 = rand_vec(rng)            # off shell
    k = rand_vec(rng)             # gluon momentum (any)
    X = rng.normal(size=4) + 1j * rng.normal(size=4)
    for s1 in range(2):
        A1 = amp_qqg(p1, p2, k, M, s1, 0, X=X, part='quark')
        A = amp_qqg(p1, p2, k, M, s1, 0, X=X, part='both')
        ub = bar(u_spinor(p1, s1, M))
        pred1 = np.array([-g * ub @ GAM[nu] @ X for nu in range(4)])
        predall = np.array([-g * ub @ GAM[nu] @ S_quark(-p2 - k, M) @ np.linalg.inv(S_quark(-p2, M)) @ X for nu in range(4)])
        R.check(f'(d) on-shell-quark term: k.A = -g ubar gamma^nu X  (m={M}, s={s1})', rel(contract_first(k, A1), pred1), 1e-12)
        R.check(f'(d) full sum: k.A = -g ubar gamma^nu S(-p2-k) S(-p2)^-1 X  (m={M}, s={s1})', rel(contract_first(k, A), predall), 1e-12)
        # with X = S(-p2) J (the off-shell leg includes its propagator), the sum is -g ubar gamma S(-p2-k) J
        J = rng.normal(size=4) + 1j * rng.normal(size=4)
        A2 = amp_qqg(p1, p2, k, M, s1, 0, X=S_quark(-p2, M) @ J, part='both')
        pred2 = np.array([-g * ub @ GAM[nu] @ S_quark(-p2 - k, M) @ J for nu in range(4)])
        R.check(f'(d) X = S(-p2)J: k.A = -g ubar gamma^nu S(-p2-k) J  (gluon removed, momentum routed)  (m={M}, s={s1})',
                rel(contract_first(k, A2), pred2), 1e-12)

# ===================================================================================== (e)
print('--- (e) DIS seed of the PDF Wilson line ---')
nB = NB  # n.k = k^+  (Collins' w_2)
for M in [0.0, 0.5]:
    pp = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    k = rand_vec(rng)
    Gam = slash(rand_vec(rng, cplx=True))     # arbitrary hard vertex (e.g. photon)
    for s in range(2):
        ub = bar(u_spinor(pp, s, M))
        H = [ub @ (1j * g * GAM[mu]) @ S_quark(pp - k, M) @ Gam for mu in range(4)]     # H^mu (row spinors)
        kH = sum(lower(k)[mu] * H[mu] for mu in range(4))
        R.check(f'(e) k_mu H^mu = g t^a H_0 exactly  (m={M}, s={s})', rel(kH, g * ub @ Gam), 1e-12)
        # K-projection: H_mu K^{mu alpha} = (k.H) n^alpha/(n.k) ; compare with W_n[inf,0] first order (k into line)
        for alpha in range(4):
            HK = kH * nB[alpha] / mdot(nB, k)
            Wrule = (1j * g * nB[alpha]) * (-1j / mdot(nB, k))     # i g n^alpha * (-i)/(n.k - i0)
            if abs(nB[alpha]) > 0:
                R.check(f'(e) H.K^(alpha={alpha}) == [i g n^alpha (-i)/(n.k-i0)] H_0  (W_n[inf,0], 1st order)', rel(HK, Wrule * ub @ Gam), 1e-12)

# ===================================================================================== (f)
print('--- (f) two K-gluons on the DIS hard part ---')
a_, b_ = 1, 6
Ta, Tb = TA[a_], TA[b_]
comm = Ta @ Tb - Tb @ Ta
for M in [0.0, 0.5]:
    for coll in [False, True]:
        pp = rand_massive(rng, M) if M > 0 else rand_massless(rng)
        if coll:   # exactly collinear light-like khat_i = (k_i^+, 0, 0_T)
            k1 = lc(rng.uniform(0.2, 1.0), 0.0); k2 = lc(rng.uniform(0.2, 1.0), 0.0)
        else:
            k1 = rand_vec(rng); k2 = rand_vec(rng)
        K = k1 + k2
        Gam = slash(rand_vec(rng, cplx=True))
        s = 0
        ub = bar(u_spinor(pp, s, M))
        # H^{mu nu}: both orderings on the outgoing quark line (colour x Dirac); contract with k1_mu k2_nu
        def Hcontr(e1, e2):
            A_ = ub @ (1j * g * slash(e1)) @ S_quark(pp - k1, M) @ (1j * g * slash(e2)) @ S_quark(pp - K, M) @ Gam
            B_ = ub @ (1j * g * slash(e2)) @ S_quark(pp - k2, M) @ (1j * g * slash(e1)) @ S_quark(pp - K, M) @ Gam
            return np.kron(Ta @ Tb, A_[None, :]) + np.kron(Tb @ Ta, B_[None, :])
        lhs = Hcontr(k1, k2)
        H0 = ub @ Gam
        exact = g**2 * np.kron(Tb @ Ta, H0[None, :]) + np.kron(comm, (1j * g**2 * ub @ slash(k2) @ S_quark(pp - K, M) @ Gam)[None, :])
        R.check(f'(f) exact: k1 k2 H = g^2 t^b t^a H0 + i g^2 [t^a,t^b] ubar k2slash S(p\'-K) Gamma  (m={M}, collinear={coll})',
                rel(lhs, exact), 1e-12)
        if coll:
            n = NB
            W2 = g**2 * (np.kron(Tb @ Ta, H0[None, :]) / (mdot(n, K) * mdot(n, k2))
                         + np.kron(Ta @ Tb, H0[None, :]) / (mdot(n, K) * mdot(n, k1)))    # n^alpha n^beta stripped
            # future-pointing rule: (ig)^2 [t^b t^a (-i/n.K)(-i/n.k2) + t^a t^b (-i/n.K)(-i/n.k1)] = g^2[...]
            R.check(f'(f) collinear: k1 k2 H == (n.k1)(n.k2) W_n[inf,0]^(2) H0  (m={M})', rel(lhs, mdot(n, k1) * mdot(n, k2) * W2), 1e-12)
            # the abelian part alone would give g^2 H0 (eikonal identity); the commutator term is the path ordering
            R.check(f'(f) collinear: commutator coefficient == n.k2/n.K  (m={M})',
                    abs((1j * ub @ slash(k2) @ S_quark(pp - K, M) @ Gam)[np.argmax(np.abs(H0))] / H0[np.argmax(np.abs(H0))] - mdot(n, k2) / mdot(n, K)), 1e-12)

# ===================================================================================== (g)
print('--- (g) non-abelian q qbar -> g* g* ---')


def amp_qq_gg(p1, p2, k1, k2, M, s1, s2, a, b):
    """A^{mu nu}_{ab} (upper indices) = t + u + s channel; incoming u(p1), vbar(p2); outgoing gluons k1(a,mu), k2(b,nu).
       Returns (A, J) where J[c][sigma] = vbar gamma^sigma t^c u (colour contracted with the quark colour indices
       as a 3x3 matrix element: we return colour-matrix-valued amplitudes)."""
    u = u_spinor(p1, s1, M); vb = bar(v_spinor(p2, s2, M))
    Q = p1 + p2
    A = np.zeros((4, 4, 3, 3), dtype=complex)
    St = S_quark(p1 - k1, M); Su = S_quark(p1 - k2, M)
    Jd = np.array([vb @ GAM[sg] @ u for sg in range(4)])        # Dirac part of the current (colour separate)
    for mu in range(4):
        for nu in range(4):
            tch = vb @ (1j * g * GAM[nu]) @ St @ (1j * g * GAM[mu]) @ u
            uch = vb @ (1j * g * GAM[mu]) @ Su @ (1j * g * GAM[nu]) @ u
            A[mu, nu] += tch * (TA[b] @ TA[a]) + uch * (TA[a] @ TA[b])
    # s channel: vbar (i g gamma_sigma t^c) u * (-i g^{sigma rho}/Q^2) * V_{rho mu nu}(c,Q; a,-k1; b,-k2)
    for c in range(8):
        if FABC[c, a, b] == 0:
            continue
        V = V3(c, Q, a, -k1, b, -k2, g)          # V^{rho mu nu} upper indices
        cur = (1j * g) * lower(Jd)                # i g vbar gamma_sigma u (lower index)
        # contraction: cur_sigma (-i g^{sigma rho}/Q^2) V_rho^{mu nu}  -> cur_sigma (-i/Q^2) V^{sigma mu nu}
        A += np.einsum('s,smn->mn', cur, V)[:, :, None, None] * (-1j / mdot(Q, Q)) * TA[c][None, None, :, :]
    return A, Jd


def contract(A, e1=None, e2=None):
    """contract A^{mu nu} (upper) with e1_mu and/or e2_nu (vectors given with upper indices)"""
    out = A
    if e1 is not None:
        out = np.einsum('m,mn...->n...', lower(e1), out)
        if e2 is not None:
            out = np.einsum('n,n...->...', lower(e2), out)
    elif e2 is not None:
        out = np.einsum('n,mn...->m...', lower(e2), out)
    return out


for M in [0.0, 0.6]:
    p1 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    p2 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    Q = p1 + p2
    k1 = rand_vec(rng); k2 = Q - k1                     # off-shell gluons
    for (a, b) in [(0, 1), (3, 5), (1, 6)]:
        A, Jd = amp_qq_gg(p1, p2, k1, k2, M, 0, 1, a, b)
        lhs = contract(A, e1=k1)                          # [nu, i, j]
        pred = np.zeros_like(lhs)
        for c in range(8):
            if FABC[a, b, c] == 0:
                continue
            Jc = Jd[:, None, None] * TA[c][None, :, :]    # J^sigma_c (upper) as colour matrices
            pred += g**2 * FABC[a, b, c] / mdot(Q, Q) * (mdot(k2, k2) * Jc - np.einsum('n,s,sij->nij', k2, lower(k2), Jc))
        R.check(f'(g) k1_mu A^(mu nu) = (g^2 f^abc/Q^2)(k2^2 J^nu - k2^nu k2.J)  (m={M}, a={a}, b={b}, off-shell gluons)',
                rel(lhs, pred), 1e-12)
        R.check(f'(g) k1_mu k2_nu A^(mu nu) = 0 off shell (m={M}, a={a}, b={b})',
                np.abs(contract(A, e1=k1, e2=k2)).max() / np.abs(lhs).max(), 1e-12)

# on-shell gluons: physical polarization sums, ghosts, and the textbook cross section
print('--- (g) on-shell gluons: ghosts and unitarity ---')


def ghost_amp(p1, p2, k1, k2, M, s1, s2, a, b):
    """q(p1) qbar(p2) -> ghost c^a(k1) [outgoing ghost], antighost cbar^b(k2): gluon s-channel, PS ghost vertex
       -g f^{a d b} p^mu with p = k1 (outgoing ghost momentum), d = gluon colour, b = colour of the ghost line
       entering the vertex (the outgoing antighost)."""
    u = u_spinor(p1, s1, M); vb = bar(v_spinor(p2, s2, M))
    Q = p1 + p2
    Jd = np.array([vb @ GAM[sg] @ u for sg in range(4)])
    out = np.zeros((3, 3), dtype=complex)
    for d in range(8):
        if FABC[a, d, b] == 0:
            continue
        vert = ghost_vertex(a, d, b, k1, g)                     # upper index
        out += (1j * g) * mdot(Jd, vert) * (-1j / mdot(Q, Q)) * TA[d]
    return out


worst_ward = 0; worst_kk = 0; worst_ghostrel = 0
ratio_unit = []; ratio_lit = []
for trial in range(4):
    k1 = rand_massless(rng); k2 = rand_massless(rng)
    Q = k1 + k2
    p1, p2 = two_body(Q, 0.0, 0.0, rng)
    s_ = mdot(Q, Q); t_ = mdot(p1 - k1, p1 - k1); u_ = mdot(p1 - k2, p1 - k2)
    sum_phys = 0; sum_gg = 0; sum_gh = 0
    for s1 in range(2):
        for s2 in range(2):
            for a in range(8):
                for b in range(8):
                    A, Jd = amp_qq_gg(p1, p2, k1, k2, 0.0, s1, s2, a, b)
                    for e2 in phys_pols(k2):
                        worst_ward = max(worst_ward, np.abs(contract(A, e1=k1, e2=e2)).max())
                    worst_kk = max(worst_kk, np.abs(contract(A, e1=k1, e2=k2)).max())
                    # -g,-g polarization sums
                    sum_gg += np.real(np.einsum('mnij,abij,ma,nb->', np.conj(A), A, METRIC, METRIC))
                    for e1 in phys_pols(k1):
                        for e2 in phys_pols(k2):
                            x = contract(A, e1=e1, e2=e2)
                            sum_phys += np.real(np.sum(np.abs(x)**2))
                    G = ghost_amp(p1, p2, k1, k2, 0.0, s1, s2, a, b)
                    sum_gh += np.real(np.sum(np.abs(G)**2))
                    # BRST relation  k1_mu kbar2_nu A = (k2.kbar2) A_ghost   (up to an overall convention sign)
                    lhs = contract(A, e1=k1, e2=kbar(k2))
                    if np.abs(G).max() > 1e-8:
                        rr = lhs / (mdot(k2, kbar(k2)) * G + 1e-300)
                        mask = np.abs(G) > 1e-6 * np.abs(G).max()
                        worst_ghostrel = max(worst_ghostrel, np.abs(np.abs(rr[mask]) - 1).max())
    ratio_unit.append(sum_phys / (sum_gg - 2 * sum_gh))
    print(f'    trial {trial}: s={s_:.4f} t={t_:.4f} u={u_:.4f}  sum_gg/sum_phys={sum_gg/sum_phys:.6f}  '
          f'2 sum_gh/sum_phys={2*sum_gh/sum_phys:.6f}  ratio-1={ratio_unit[-1]-1:.2e}')
    lit = g**4 * (32.0 / 27.0 * (t_**2 + u_**2) / (t_ * u_) - 8.0 / 3.0 * (t_**2 + u_**2) / s_**2)
    ratio_lit.append(sum_phys / 36.0 / lit)
R.check('(g) k1_mu A^{mu nu} eps2_nu = 0 for physical on-shell gluon 2 (all spins, colours)', worst_ward, 1e-12)
R.check('(g) k1_mu k2_nu A^{mu nu} = 0 (on shell)', worst_kk, 1e-12)
R.check('(g) |k1 kbar2 A| = |k2.kbar2| |A_ghost|  (BRST relation; ghost amplitude with PS vertex)', worst_ghostrel, 1e-10)
R.check('(g) sum_phys |A|^2 == sum_{-g,-g}|A|^2 - 2 sum|A_ghost|^2  (ratio-1; round-off from cancelling unphysical terms)', max(abs(np.array(ratio_unit) - 1)), 1e-9)
R.check('(g) (1/36) sum_phys |A|^2 == g^4[32/27 (t^2+u^2)/(tu) - 8/3 (t^2+u^2)/s^2]  [Combridge et al.; ESW Tab.7.1] (ratio-1)',
        max(abs(np.array(ratio_lit) - 1)), 1e-12)

# ===================================================================================== (h)
print('--- (h) gamma* -> q qbar g* g*: two longitudinal off-shell gluons ---')


def amp_one_gluon(p1, p2, Q_, M, s1, s2, Tc):
    """gamma*(nu_photon fixed by Gam) -> q(p1) qbar(p2) g*(Q_, sigma) : returns A^sigma (upper) as colour matrix x scalar
       with photon vertex Gam (global)."""
    ub = bar(u_spinor(p1, s1, M)); vv = v_spinor(p2, s2, M)
    out = np.zeros((4, 3, 3), dtype=complex)
    for sg in range(4):
        t1 = ub @ (1j * g * GAM[sg]) @ S_quark(p1 + Q_, M) @ Gam @ vv
        t2 = ub @ Gam @ S_quark(-p2 - Q_, M) @ (1j * g * GAM[sg]) @ vv
        out[sg] = (t1 + t2) * Tc
    return out


def amp_qq_g1g2(p1, p2, k1, k2, M, s1, s2, a, b):
    """gamma* -> q(p1) qbar(p2) g*(k1,a,mu) g*(k2,b,nu): 6 quark-line orderings + 2 three-gluon diagrams.
       Returns A^{mu nu} (upper) as 4x4x3x3."""
    ub = bar(u_spinor(p1, s1, M)); vv = v_spinor(p2, s2, M)
    A = np.zeros((4, 4, 3, 3), dtype=complex)
    # quark line from vbar... : ubar(p1) [vertices in order from the ubar end] v(p2); momentum along the fermion
    # arrow starts at p1 (outgoing quark) at the ubar end; each emitted outgoing gluon/photon adds to it when
    # moving towards v: propagator momentum = p1 + (sum of emitted momenta to the left)
    for order in itertools.permutations(['g1', 'g2', 'ph']):
        for mu in range(4):
            for nu in range(4):
                X = ub.copy(); C = I3.copy(); l = p1.copy()
                for i, el in enumerate(order):
                    if el == 'g1':
                        X = X @ (1j * g * GAM[mu]); C = C @ TA[a]; l = l + k1
                    elif el == 'g2':
                        X = X @ (1j * g * GAM[nu]); C = C @ TA[b]; l = l + k2
                    else:
                        X = X @ Gam; l = l + qph
                    if i < 2:
                        X = X @ S_quark(l, M)
                A[mu, nu] += (X @ vv) * C
    # three-gluon vertex: gluon (Q = k1 + k2, c, sigma) from the quark line splits into k1, k2
    Q_ = k1 + k2
    for c in range(8):
        if FABC[c, a, b] == 0:
            continue
        one = amp_one_gluon(p1, p2, Q_, M, s1, s2, TA[c])          # A^sigma (upper)
        V = V3(c, Q_, a, -k1, b, -k2, g)                            # V^{rho mu nu}
        # one_sigma (-i g^{sigma rho}/Q^2) V_rho^{mu nu}
        A += np.einsum('sij,smn->mnij', np.einsum('s,sij->sij', np.diag(METRIC), one), V) * (-1j / mdot(Q_, Q_))
    return A


Gam = slash(rand_vec(rng, cplx=True))    # photon polarization contracted (arbitrary)
for M in [0.0, 0.6]:
    p1 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    p2 = rand_massive(rng, M) if M > 0 else rand_massless(rng)
    k1 = rand_vec(rng); k2 = rand_vec(rng)
    qph = -(p1 + p2 + k1 + k2)     # photon momentum flowing OUT of the quark line in the 'ph' vertex bookkeeping
    # (the photon is incoming with momentum p1+p2+k1+k2; along the fermion arrow it subtracts)
    for (a, b) in [(0, 1), (2, 4), (5, 6)]:
        A = amp_qq_g1g2(p1, p2, k1, k2, M, 0, 1, a, b)
        lhs = contract(A, e1=k1)
        Q_ = k1 + k2
        pred = np.zeros_like(lhs)
        for c in range(8):
            if FABC[a, b, c] == 0:
                continue
            one = amp_one_gluon(p1, p2, Q_, M, 0, 1, TA[c])           # A^sigma_c (upper)
            k2one = np.einsum('s,sij->ij', lower(k2), one)
            pred += 1j * g * FABC[a, b, c] / mdot(Q_, Q_) * (k2[:, None, None] * k2one[None] - mdot(k2, k2) * one)
        R.check(f'(h) k1_mu A^(mu nu) = (i g f^abc/Q^2)(k2^nu k2.A_c(Q) - k2^2 A_c^nu(Q))  (m={M}, a={a}, b={b})',
                rel(lhs, pred), 1e-11)
        R.check(f'(h) k1_mu k2_nu A^(mu nu) = 0, gamma* q qbar g* g*, off-shell gluons (m={M}, a={a}, b={b})',
                np.abs(contract(A, e1=k1, e2=k2)).max() / np.abs(lhs).max(), 1e-11)

R.summary()
