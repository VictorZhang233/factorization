"""
ope_check.py -- independent check of the Mellin moments through the OPE / forward Compton amplitude.

Method (large-momentum / hard-region expansion): the forward amplitude T^{mu nu}(p,q) for an on-shell
massless parton (p^2 = 0) is Taylor-expanded in p at fixed q (bookkeeping parameter lam: p -> lam p).
For p^2 = 0 every non-hard region is scaleless and vanishes in DR, so the Taylor coefficients of the
projected amplitude in omega = 2p.q/Q^2 = 1/x are the EXACT (all orders in eps) Mellin moments of the
bare partonic structure function, i.e. the bare OPE coefficient functions times the (scaleless, hence
tree-level) partonic operator matrix elements.  The coefficients are compared, exactly as rational
functions of eps, with the moments of the D-dim cut calculation (real + virtual) of dis_nlo.py.

All loop integrals reduce to   int d^Dl/(2pi)^D (p.l)^a / [ (l^2)^alpha ((l+s q)^2)^beta ]
  = i (4pi)^{-D/2} K_G (-s p.q)^a (-1)^(alpha+beta) Gamma(alpha+beta-D/2) Gamma(a+D/2-alpha) Gamma(D/2-beta)
                       / [Gamma(alpha) Gamma(beta) Gamma(a+D-alpha-beta)] / K_G      (Q^2 = 1)
with K_G = Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps) (p^2 = 0 kills all tensor structures except q's).
"""
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import dirac_d as dd
from itertools import permutations

eps, lam = sp.symbols('epsilon lam')
pl, pq, ll, Mq, om = sp.symbols('pl pq ll M omega')
Dv = 4 - 2 * eps
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6


def Gr(n, s):
    """Gamma(n + s eps)/Gamma(1 + s eps) for integer n, as a rational function of eps"""
    n = int(n)
    if n >= 1:
        return sp.prod([k + s * eps for k in range(1, n)])
    return 1 / sp.prod([k + s * eps for k in range(n, 1)])


def Jhat(alpha, beta, a, s):
    if alpha <= 0 or beta <= 0:
        return sp.Integer(0)                       # scaleless
    return ((-s * pq) ** a * (-1) ** (alpha + beta) * Gr(alpha + beta - 2, 1) * Gr(a + 2 - alpha, -1)
            * Gr(2 - beta, -1) / (sp.factorial(alpha - 1) * sp.factorial(beta - 1) * Gr(a + 4 - alpha - beta, -2)))


def vec(l=0, p=0, q=0):
    d = {}
    if l: d['l'] = l
    if p: d['p'] = p * lam
    if q: d['q'] = q
    return d


def series_inv(base, X, n, K):
    """(base + lam*X)^(-n) expanded to lam^K"""
    return sum(sp.binomial(n + k - 1, k) * (-lam * X) ** k / base ** (n + k) for k in range(K + 1))


def truncate(expr, K):
    P = sp.Poly(sp.expand(expr), lam)
    return sum(c * lam ** m[0] for m, c in P.terms() if m[0] <= K)


def diagram(slots, loop_dens, ext_dens, s, K, sign):
    """
    slots: trace slots (Tr 1 = 4), p entries carry lam.
    loop_dens: list of (a, sq, power): ((l + a p + sq q)^2)^power with sq in {0, s}
    ext_dens : list of (a, sq, power): ((a p + sq q)^2)^power  (no loop momentum)
    returns  sum_K  coefficient(lam^K) after loop integration (K_G and i(4pi)^{-D/2} stripped)
    """
    dd.set_dots({('p', 'p'): 0, ('q', 'q'): -1, ('p', 'q'): pq, ('l', 'p'): pl, ('l', 'l'): ll,
                 ('l', 'q'): sp.Symbol('lq')})
    num = sign * dd.tr(slots).subs(dd.D, Dv)
    # l.q in terms of propagators: (l+s q)^2 = l^2 + 2 s l.q - 1
    num = sp.expand(num.subs(sp.Symbol('lq'), s * (Mq - ll + 1) / 2))
    integrand = truncate(num, K)
    for (a, sq, pw) in loop_dens:
        base = ll if sq == 0 else Mq
        X = 2 * a * (pl + sq * pq)                  # 2 a p.(l + sq q), p^2 = 0
        integrand = truncate(integrand * series_inv(base, X, pw, K), K)
    for (a, sq, pw) in ext_dens:
        # (a p + sq q)^2 = 2 a sq lam p.q - sq^2
        base = -sq ** 2
        X = 2 * a * sq * pq
        integrand = truncate(integrand * series_inv(base, X, pw, K), K)
    if not loop_dens:                               # tree level: nothing to integrate
        return sp.expand(integrand)
    # integrate monomial by monomial
    res = 0
    for term in sp.Add.make_args(sp.expand(integrand)):
        c, rest = term.as_independent(lam, pl, pq, ll, Mq, as_Add=False)
        pw = rest.as_powers_dict()
        kk = pw.get(lam, 0)
        a = pw.get(pl, 0)
        b = pw.get(pq, 0)
        al = -pw.get(ll, 0)
        be = -pw.get(Mq, 0)
        res += c * lam ** kk * pq ** b * Jhat(al, be, a, s)
    return sp.expand(res)


def to_omega(expr):
    """lam^K pq^K -> (omega/2)^K ; check homogeneity"""
    out = 0
    for term in sp.Add.make_args(sp.expand(expr)):
        c, rest = term.as_independent(lam, pq, as_Add=False)
        pw = rest.as_powers_dict()
        assert pw.get(lam, 0) == pw.get(pq, 0), term
        out += c * (om / 2) ** pw.get(pq, 0)
    return sp.expand(out)


# ------------------------------------------------------------------------------ quark target
def quark_amplitudes(K):
    I = dd.I
    P = vec(p=1)
    res = {}
    for proj in ('g', 'pp'):
        if proj == 'g':
            mu, nu, sgn = I('m'), I('m'), -1
        else:
            mu, nu, sgn = vec(p=1), vec(p=1), 1
        Kp = K if proj == 'g' else K + 2
        tree = diagram([P, mu, vec(p=1, q=1), nu], [], [(1, 1, 1)], -1, Kp, sgn)
        box = diagram([P, I('a'), vec(p=1, l=-1), mu, vec(p=1, q=1, l=-1), nu, vec(p=1, l=-1), I('a')],
                      [(0, 0, 1), (-1, 0, 2), (-1, -1, 1)], [], -1, Kp, sgn)
        v1 = diagram([P, mu, vec(p=1, q=1), I('a'), vec(p=1, q=1, l=-1), nu, vec(p=1, l=-1), I('a')],
                     [(0, 0, 1), (-1, -1, 1), (-1, 0, 1)], [(1, 1, 1)], -1, Kp, sgn)
        v2 = diagram([P, I('a'), vec(p=1, l=-1), mu, vec(p=1, q=1, l=-1), I('a'), vec(p=1, q=1), nu],
                     [(0, 0, 1), (-1, 0, 1), (-1, -1, 1)], [(1, 1, 1)], -1, Kp, sgn)
        se = diagram([P, mu, vec(p=1, q=1), I('a'), vec(p=1, q=1, l=-1), I('a'), vec(p=1, q=1), nu],
                     [(0, 0, 1), (-1, -1, 1)], [(1, 1, 2)], -1, Kp, sgn)
        res[proj] = dict(tree=to_omega(tree), box=to_omega(box), v1=to_omega(v1), v2=to_omega(v2),
                         se=to_omega(se))
    return res


# ------------------------------------------------------------------------------ gluon target
def gluon_amplitude(K):
    """sum over the 6 orderings of the quark box; returns projected results (with -g_{rho sigma})"""
    I = dd.I
    out = {}
    for proj in ('g', 'pp'):
        Kp = K if proj == 'g' else K + 2
        tot = 0
        for perm in permutations(['gin_', 'gout', 'gamin', 'gamout'][1:]):
            order = ['gin'] + [x.strip('_') for x in perm]
            order = [o if o != 'gout' else 'gout' for o in order]
            mom = {'gin': (1, 0), 'gamin': (0, 1), 'gamout': (0, -1), 'gout': (-1, 0)}
            # momenta on propagators: P0 = l, P1 = l + p_{v1}, ...
            cum = [(0, 0)]
            for v in order[:-1]:
                cum.append((cum[-1][0] + mom[v][0], cum[-1][1] + mom[v][1]))
            sq_vals = {c[1] for c in cum if c[1] != 0}
            assert len(sq_vals) <= 1
            s = sq_vals.pop() if sq_vals else 1
            if proj == 'g':
                vx = {'gin': I('r'), 'gout': I('r'), 'gamin': I('m'), 'gamout': I('m')}
                sgn = (-1) * (-1)           # -g_{mu nu} and -g_{rho sigma}
            else:
                vx = {'gin': I('r'), 'gout': I('r'), 'gamin': vec(p=1), 'gamout': vec(p=1)}
                sgn = -1                    # -g_{rho sigma}
            # Tr[ G_v4 S(P3) G_v3 S(P2) G_v2 S(P1) G_v1 S(P0) ]
            slots = []
            for k in (3, 2, 1, 0):
                slots.append(vx[order[k]])
                a, b = cum[k]
                slots.append(vec(l=1, p=a, q=b))
            dens = []
            for (a, b) in cum:
                dens.append((a, b, 1))
            # merge identical denominators
            merged = {}
            for (a, b, pw) in dens:
                merged[(a, b)] = merged.get((a, b), 0) + pw
            dens = [(a, b, pw) for (a, b), pw in merged.items()]
            tot += diagram(slots, dens, [], s, Kp, sgn)
        out[proj] = to_omega(tot)
    return out


def coeffs(expr, nmax):
    return [sp.factor(sp.expand(expr).coeff(om, n)) for n in range(0, nmax + 1)]


# ------------------------------------------------------------------------------ exact moments of the cut result
def m2q(N):
    c = [2 - 7 * eps + eps ** 2, 2 * eps, 2]
    real = sum(c[j] * Gr(N + j, 1) / sp.factorial(N + j - 1) for j in range(3)) / (2 * eps ** 2 * (1 - 2 * eps))
    virt = 1 / eps - 2 / (eps ** 2 * (1 - 2 * eps))
    return sp.factor(real + virt)


def mLq(N):
    return sp.factor(2 * (1 - eps) * Gr(N + 1, 1) / ((1 - 2 * eps) * sp.factorial(N + 1)))


def m2g(N):
    d = [1 - 3 * eps + 4 * eps ** 2 - 2 * eps ** 3, -2, 2]
    return sp.factor(-2 / (eps * (1 - 2 * eps) * (1 - eps) ** 2) *
                     sum(d[j] * Gr(N + j, 1) / sp.factorial(N + j) for j in range(3)))


def mLg(N):
    return sp.factor(8 * Gr(N + 1, 1) / ((1 - 2 * eps) * sp.factorial(N + 2)))


if __name__ == '__main__':
    t0 = time.time()
    allok = True
    print(f'Hard-region expansion of the forward Compton amplitude, N = 1..{NMAX}')
    qa = quark_amplitudes(NMAX)
    print(f'  quark diagrams done ({time.time() - t0:.1f}s)')
    # projectors on the omega-expansion: Pi_2 = [ -g + (3-2eps)(4/omega^2) pp ]/(1-eps) ; Pi_L = (8/omega^2) pp
    tree2 = sp.expand((qa['g']['tree'] + (3 - 2 * eps) * 4 * qa['pp']['tree'] / om ** 2) / (1 - eps))
    one = {k: sp.expand(qa['g'][k] + (3 - 2 * eps) * 4 * qa['pp'][k] / om ** 2) / (1 - eps)
           for k in ('box', 'v1', 'v2', 'se')}
    loop2 = sp.expand(sum(one.values()))
    loopL = sp.expand(8 * sum(qa['pp'][k] for k in ('box', 'v1', 'v2', 'se')) / om ** 2)
    ct = coeffs(tree2, NMAX)
    c2 = coeffs(loop2, NMAX)
    cL = coeffs(loopL, NMAX)
    print('  tree coefficients (Pi_2, N=0..):', ct)
    print('  quark target: compare  Pi(one-loop)_N / Pi(tree)_N  with  2 x exact moment of cut result')
    for N in range(1, NMAX + 1):
        r2 = sp.simplify(c2[N] / ct[N] - 2 * m2q(N))
        rL = sp.simplify(cL[N] / ct[N] - 2 * mLq(N))
        ok = (r2 == 0) and (rL == 0)
        allok &= ok
        print(f'   N={N}:  F2: {"PASS" if r2 == 0 else "FAIL " + str(r2)}   FL: {"PASS" if rL == 0 else "FAIL " + str(rL)}')
    t1 = time.time()
    ga = gluon_amplitude(NMAX)
    print(f'  gluon diagrams done ({time.time() - t1:.1f}s)')
    g2 = coeffs(sp.expand((ga['g'] + (3 - 2 * eps) * 4 * ga['pp'] / om ** 2) / (1 - eps)), NMAX)
    gL = coeffs(sp.expand(8 * ga['pp'] / om ** 2), NMAX)
    print('  gluon target (6 orderings, crossing even): compare (2/(D-2)) Pi(box)_N / (2 x Pi(tree)_N) with 2 x moment')
    for N in range(1, NMAX + 1):
        if N % 2 == 1:
            ok = (sp.simplify(g2[N]) == 0) and (sp.simplify(gL[N]) == 0)
            allok &= ok
            print(f'   N={N}:  odd moment vanishes: {"PASS" if ok else "FAIL"}')
            continue
        r2 = sp.simplify((2 / (Dv - 2)) * g2[N] / (2 * ct[N]) - 2 * m2g(N))
        rL = sp.simplify((2 / (Dv - 2)) * gL[N] / (2 * ct[N]) - 2 * mLg(N))
        ok = (r2 == 0) and (rL == 0)
        allok &= ok
        print(f'   N={N}:  F2: {"PASS" if r2 == 0 else "FAIL " + str(r2)}   FL: {"PASS" if rL == 0 else "FAIL " + str(rL)}')
    print('OPE CHECK:', 'ALL PASS' if allok else 'FAILURES', f'({time.time() - t0:.1f}s)')
