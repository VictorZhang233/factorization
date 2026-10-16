"""
s3_eikonal_approx.py -- item (3): eikonal approximation of soft gluons on an energetic on-shell quark line.

For m soft gluons (momenta k_j = lambda * khat_j flowing INTO the quark line, arbitrary polarizations eps_j,
colours a_j) attached to an external line of momentum p (p^2 = M^2, M = 0 or M > 0):

  incoming quark   u(p)   : S(p+K_m) igeps_m ... S(p+K_1) igeps_1 u(p)
                           -> prod_j [ -g p.eps_j/(p.K_j + i0) ] t^{a_m}..t^{a_1} u(p)       = W_p[0,-inf]
  outgoing quark   ubar(p): ubar igeps_m S(p-K'_m) ... igeps_1 S(p-K'_1)
                           -> ubar t^{a_m}..t^{a_1} prod_j [ +g p.eps_j/(p.K'_j - i0) ]      = W_p[inf,0]
  incoming antiquark vbar : vbar igeps_1 S(-p-K_1) ... igeps_m S(-p-K_m)
                           -> vbar t^{a_1}..t^{a_m} prod_j [ +g p.eps_j/(p.K_j + i0) ]       = W_p[-inf,0]
  outgoing antiquark v(p) : S(-p+K'_1) igeps_1 ... S(-p+K'_m) igeps_m v
                           -> prod_j [ -g p.eps_j/(p.K'_j - i0) ] t^{a_1}..t^{a_m} v(p)       = W_p[0,inf]
  with K_j = k_1+...+k_j (gluon 1 = earliest, nearest the far past), K'_j = k_j+...+k_m (gluon m = latest).

Checks: relative error -> 0 linearly in lambda (fitted slope ~1), for each line type, M = 0 and M = 0.4,
m = 1, 2, 3; the eikonal factors coincide EXACTLY with the Wilson-line rules of s1 (vertex i g t^a v^mu,
propagator i/(v.l+i0)) for the four lines W_p[0,-inf], W_p[inf,0], W_p[-inf,0], W_p[0,inf] (colour- and
Dirac-matrix level, summed over all m! orderings for m = 3); literature: soft-bremsstrahlung form
(Peskin-Schroeder Sec. 6.1, converted g t^a <-> -e).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcdtools import *

R = Report('s3_eikonal_approx')
g = 1.0
rng = np.random.default_rng(314)


def chain(kind, p, M, ks, epss, s):
    """exact Dirac part (row or column spinor) of the m-gluon chain, gluons in attachment order 1..m"""
    m = len(ks)
    if kind == 'q_in':
        X = u_spinor(p, s, M)
        for j in range(m):
            X = S_quark(p + sum(ks[:j + 1]), M) @ (1j * g * slash(epss[j])) @ X
        return X
    if kind == 'q_out':
        X = bar(u_spinor(p, s, M))
        for j in reversed(range(m)):
            X = X @ (1j * g * slash(epss[j])) @ S_quark(p - sum(ks[j:]), M)
        return X
    if kind == 'qb_in':
        X = bar(v_spinor(p, s, M))
        for j in range(m):
            X = X @ (1j * g * slash(epss[j])) @ S_quark(-p - sum(ks[:j + 1]), M)
        return X
    if kind == 'qb_out':
        X = v_spinor(p, s, M)
        for j in reversed(range(m)):
            X = S_quark(-p + sum(ks[j:]), M) @ (1j * g * slash(epss[j])) @ X
        return X


def eikonal(kind, p, M, ks, epss, s):
    m = len(ks)
    fac = 1.0 + 0j
    for j in range(m):
        if kind in ('q_in', 'qb_in'):
            K = sum(ks[:j + 1])
        else:
            K = sum(ks[j:])
        sgn = {'q_in': -1, 'q_out': +1, 'qb_in': +1, 'qb_out': -1}[kind]
        fac *= sgn * g * mdot(p, epss[j]) / mdot(p, K)
    base = {'q_in': u_spinor(p, s, M), 'q_out': bar(u_spinor(p, s, M)),
            'qb_in': bar(v_spinor(p, s, M)), 'qb_out': v_spinor(p, s, M)}[kind]
    return fac * base


def wilson_rule(kind, p, ks, epss):
    """Wilson-line rule of s1, line along v = +-p (direction of the line from a to b):
       vertex i g (v.eps), propagator i/(v.l + i0), l along the orientation, l = 0 at infinity."""
    m = len(ks)
    line = {'q_in': 'past', 'q_out': 'future', 'qb_in': 'pastc', 'qb_out': 'futc'}[kind]
    vsign = {'past': +1, 'future': +1, 'pastc': -1, 'futc': -1}[line]
    v = vsign * p
    # gluons in attachment (time) order 1..m; the infinite end is in the far past for past/pastc lines.
    fac = 1.0 + 0j
    for j in range(m):
        fac *= 1j * g * mdot(v, epss[j])
    # propagators: past line W[0,-inf] (a=-inf -> b=0): after gluon j (time order) l = K_j along v
    if line == 'past':
        for j in range(m):
            fac *= 1j / mdot(v, sum(ks[:j + 1]))
    elif line == 'future':   # a=0 -> b=+inf: before gluon j l = -(k_j+..+k_m)
        for j in range(m):
            fac *= 1j / mdot(v, -sum(ks[j:]))
    elif line == 'pastc':    # a=0 -> b=-inf (orientation -p): time order 1 (earliest) is nearest b.
        # segment between gluon j and j+1 (in time order), flowing from a=0 towards b=-inf along v:
        # l = -(k_1+..+k_j) (momentum conservation with l = 0 at b)
        for j in range(m):
            fac *= 1j / mdot(v, -sum(ks[:j + 1]))
    elif line == 'futc':     # a=+inf -> b=0 (orientation -p): latest gluon m nearest a; l = k_j+..+k_m
        for j in range(m):
            fac *= 1j / mdot(v, sum(ks[j:]))
    return fac


def colour(kind, cols):
    M = I3.copy()
    seq = cols[::-1] if kind in ('q_in', 'q_out') else cols
    for T in seq:
        M = M @ T
    return M


def rand_future_timelike(rng):
    kv = rng.normal(size=3)
    return np.concatenate([[np.linalg.norm(kv) + rng.uniform(0.1, 1.0)], kv])


lams = [1e-2, 1e-3, 1e-4, 1e-5]
for kind in ['q_in', 'q_out', 'qb_in', 'qb_out']:
    for M in [0.0, 0.4]:
        for m in [1, 2, 3]:
            for kin in ['timelike', 'generic']:
                p = rand_massive(rng, M, 1.0) if M > 0 else rand_massless(rng, E=1.3)
                if kin == 'timelike':     # well-conditioned: all p.K_j > 0 and O(1)
                    khat = [rand_future_timelike(rng) for _ in range(m)]
                else:                     # generic off-shell (virtual) momenta of either sign
                    khat = [rand_vec(rng, 1.0) for _ in range(m)]
                epss = [rand_vec(rng, 1.0, cplx=True) for _ in range(m)]
                errs = []
                for lam in lams:
                    ks = [lam * k for k in khat]
                    e = max(rel(chain(kind, p, M, ks, epss, s), eikonal(kind, p, M, ks, epss, s)) for s in range(2))
                    errs.append(e)
                slope = np.polyfit(np.log10(lams[1:]), np.log10(errs[1:]), 1)[0]
                # conditioning: smallest |p.K_j| / (|p^0| |K_j^0|) among the cumulative sums
                Ks = [sum(khat[:j + 1]) for j in range(m)] + [sum(khat[j:]) for j in range(m)]
                cond = min(abs(mdot(p, K)) / (np.abs(p).max() * np.abs(K).max()) for K in Ks)
                R.check(f'(3) {kind:6s} M={M} m={m} {kin:8s}: rel.err at lambda=1e-5 (slope {slope:.2f}, min|p.K|/|p||K| = {cond:.1e})',
                        errs[-1], 1e-3)
                R.flag(f'(3) {kind:6s} M={M} m={m} {kin:8s}: error scales linearly in lambda (slope in [0.85,1.15])', 0.85 < slope < 1.15)
            # eikonal factor == Wilson-line rule (exact, any lambda)
            ks = [0.01 * k for k in khat]
            fe = eikonal(kind, p, M, ks, epss, 0)
            base = {'q_in': u_spinor(p, 0, M), 'q_out': bar(u_spinor(p, 0, M)),
                    'qb_in': bar(v_spinor(p, 0, M)), 'qb_out': v_spinor(p, 0, M)}[kind]
            idx = np.argmax(np.abs(base))
            R.check(f'(3) {kind:6s} M={M} m={m}: eikonal factor == Wilson-line rule (s1)',
                    abs(fe[idx] / base[idx] - wilson_rule(kind, p, ks, epss)) / abs(fe[idx] / base[idx]), 1e-12)

# full colour x Dirac sum over orderings for m = 3 (massive, lambda = 1e-3)
print('\n--- sum over all 3! orderings, colour x Dirac ---')
for kind in ['q_in', 'q_out', 'qb_in', 'qb_out']:
    M = 0.4
    p = rand_massive(rng, M, 1.0)
    khat = [rand_future_timelike(rng) for _ in range(3)]
    epss = [rand_vec(rng, 1.0, cplx=True) for _ in range(3)]
    cols = [TA[a] for a in rng.integers(0, 8, size=3)]
    lam = 1e-5
    ks = [lam * k for k in khat]
    full = 0; wl = 0
    for perm in itertools.permutations(range(3)):
        kp = [ks[i] for i in perm]; ep = [epss[i] for i in perm]; cp = [cols[i] for i in perm]
        full = full + np.kron(colour(kind, cp), chain(kind, p, M, kp, ep, 0)[None, :])
        base = {'q_in': u_spinor(p, 0, M), 'q_out': bar(u_spinor(p, 0, M)),
                'qb_in': bar(v_spinor(p, 0, M)), 'qb_out': v_spinor(p, 0, M)}[kind]
        wl = wl + np.kron(colour(kind, cp), (wilson_rule(kind, p, kp, ep) * base)[None, :])
    R.check(f'(3) {kind:6s} sum over orderings (colour x Dirac) == Wilson-line 3rd-order term', rel(full, wl), 1e-4,
            '(lambda = 1e-5)')

# literature cross-check: soft limit of gamma* -> q(p1) qbar(p2) g(k)
print('\n--- soft bremsstrahlung form (Peskin-Schroeder Sec. 6.1, converted) ---')
p1 = rand_massless(rng, E=1.1); p2 = rand_massless(rng, E=0.9)
khat = rand_massless(rng, E=1.0)
nu = 2
errs = []
for lam in [1e-2, 1e-3, 1e-4]:
    k = lam * khat
    for pol in phys_pols(k):
        eps_ = pol  # real transverse polarization (eps^* = eps)
        for s1 in range(2):
            for s2 in range(2):
                ub = bar(u_spinor(p1, s1)); v = v_spinor(p2, s2)
                # outgoing gluon: k flows OUT of the quark line; Dirac parts (colour t^a factors out)
                amp = ub @ ((1j * g * slash(eps_)) @ S_quark(p1 + k) @ GAM[nu] + GAM[nu] @ S_quark(-p2 - k) @ (1j * g * slash(eps_))) @ v
                born = ub @ GAM[nu] @ v
                soft = g * (mdot(p2, eps_) / mdot(p2, k) - mdot(p1, eps_) / mdot(p1, k)) * born
                if abs(born) > 1e-6:
                    errs.append(abs(amp - soft) / abs(soft))
R.check('(3) gamma*->q qbar g soft limit == g (p2.eps/p2.k - p1.eps/p1.k) t^a A_0 (PS 6.1 with g t^a <-> -e)',
        max(errs[-8:]), 1e-3)

R.summary()
