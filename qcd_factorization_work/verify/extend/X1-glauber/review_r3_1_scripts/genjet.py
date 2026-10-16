# X1 review round 3, reviewer 1 -- general two-insertion jets of class (J) + (Sp) + (Sp') + (R) + NF,
# NOT of the "factorized" form used by fix_r2_scripts/l8_bounds.py and by the scalar model.
#
# Sectors (operation orders) and gap momenta (p1, p2 = insertion energies, P = p1 + p2):
#   colour order [12]:  BB = (1,2,V): gaps (p1 init, P init)   BF = (1,V,2): (p1 init, p2 fin)   FF = (V,1,2): (P fin, p2 fin)
#   colour order [21]:  BBp= (2,1,V): gaps (p2 init, P init)   BFp= (2,V,1): (p2 init, p1 fin)   FFp= (V,2,1): (P fin, p1 fin)
# initial-gap factor i/(A + K), final-gap factor i/(A' - K); A, A' < 0 (bound state; NF).
# (Sp') (adjacent-pair hypothesis): sectors that differ by swapping two adjacent operations have their terms with a
# single-state gap between those two operations in bijection, with equal c_t and equal gap function in the other gap.
# The six adjacent swaps form a hexagon  BB -(2V)- BF -(1V)- FF -(12)- FFp -(2V)- BFp -(1V)- BBp -(12)- BB.
# Building blocks (all satisfy (Sp') and contribute the same Jcal to every sector, hence (Sp)):
#   * hexagon orbits: one term per sector, single-state gaps, energies attached to the six states {1,2,12,V,1V,2V};
#   * winding cycles: twelve terms going twice around the hexagon with DIFFERENT energies on the two turns
#     (not a sum of hexagon orbits, not factorized);
#   * two-chains: a pair of terms on one hexagon edge sharing a MULTI-state "other" gap (single-state gaps between the
#     swapped operations);
#   * isolated terms with both gaps multi-state (unconstrained).
import numpy as np

SECTORS = ('BB', 'BF', 'FF', 'BBp', 'BFp', 'FFp')
# gap types: (type of gap 1, type of gap 2); momentum labels
GAPTYPE = dict(BB=('i', 'i'), BF=('i', 'f'), FF=('f', 'f'), BBp=('i', 'i'), BFp=('i', 'f'), FFp=('f', 'f'))
GAPMOM = dict(BB=('p1', 'P'), BF=('p1', 'p2'), FF=('P', 'p2'), BBp=('p2', 'P'), BFp=('p2', 'p1'), FFp=('P', 'p1'))
COLOUR = dict(BB='12', BF='12', FF='12', BBp='21', BFp='21', FFp='21')


def gapfac(As, typ, K):
    out = 1.0
    for A in As:
        out = out*(1j/(A + K) if typ == 'i' else 1j/(A - K))
    return out


class Jet:
    def __init__(self):
        self.terms = {s: [] for s in SECTORS}   # list of (c, As_gap1, As_gap2)
        self.phase = 1.0

    def add(self, s, c, g1, g2):
        self.terms[s].append((c, list(g1), list(g2)))

    def all_A(self):
        out = []
        for s in SECTORS:
            for (c, g1, g2) in self.terms[s]:
                out += list(g1) + list(g2)
        return np.array(out)

    def lam_mu(self):
        A = np.abs(self.all_A())
        return A.max(), A.min()

    def Jcal(self, s):
        return sum(c for (c, g1, g2) in self.terms[s] if len(g1) == 1 and len(g2) == 1)

    def norms(self):
        lam, mu = self.lam_mu()
        M = 0.0; Mf = 0.0
        for s in SECTORS:
            m = sum(abs(c)*lam**(-(len(g1) + len(g2) - 2)) for (c, g1, g2) in self.terms[s])
            mf = sum(abs(c)*mu**(-(len(g1) + len(g2) - 2)) for (c, g1, g2) in self.terms[s])
            M = max(M, m); Mf = max(Mf, mf)
        return M, Mf

    def sector(self, s, p1, p2):
        P = p1 + p2
        mom = dict(p1=p1, p2=p2, P=P)
        t1, t2 = GAPTYPE[s]; k1, k2 = GAPMOM[s]
        out = 0.0
        for (c, g1, g2) in self.terms[s]:
            out = out + c*gapfac(g1, t1, mom[k1])*gapfac(g2, t2, mom[k2])
        return out

    def colour(self, col, p1, p2):
        return sum(self.sector(s, p1, p2) for s in SECTORS if COLOUR[s] == col)

    def g(self, P):
        """g(P) = sum over BB^[12] terms with single-state first gap of c phi_2(P)
                 + sum over FF^[12] terms with single-state second gap of c phi_1(P)"""
        out = 0.0
        for (c, g1, g2) in self.terms['BB']:
            if len(g1) == 1:
                out = out + c*gapfac(g2, 'i', P)
        for (c, g1, g2) in self.terms['FF']:
            if len(g2) == 1:
                out = out + c*gapfac(g1, 'f', P)
        return out

    def g21(self, P):
        out = 0.0
        for (c, g1, g2) in self.terms['BBp']:
            if len(g1) == 1:
                out = out + c*gapfac(g2, 'i', P)
        for (c, g1, g2) in self.terms['FFp']:
            if len(g2) == 1:
                out = out + c*gapfac(g1, 'f', P)
        return out


def check_spprime(jet, tol=1e-12):
    """structural check of (Sp'): for each adjacent swap, multiset equality of (c, other-gap) over terms whose gap
    between the swapped operations is single-state."""
    # edge: (sector X, index of gap between swapped ops in X, sector Y, index in Y); other gap = 1 - index
    edges = [('BB', 1, 'BF', 1),    # swap (2,V): BB gap2 (after 1,2) <-> BF gap2 (after 1,V); other gap = gap1 (p1)
             ('BF', 0, 'FF', 0),    # swap (1,V): BF gap1 <-> FF gap1; other gap = gap2 (p2 final)
             ('FF', 1, 'FFp', 1),   # swap (1,2): FF gap2 <-> FFp gap2; other = gap1 (P final)
             ('FFp', 0, 'BFp', 0),  # swap (2,V): FFp gap1 <-> BFp gap1; other = gap2 (p1 final)
             ('BFp', 1, 'BBp', 1),  # swap (1,V): BFp gap2 <-> BBp gap2; other = gap1 (p2 init)
             ('BBp', 0, 'BB', 0)]   # swap (1,2): BBp gap1 <-> BB gap1; other = gap2 (P init)
    ok = True
    for (X, iX, Y, iY) in edges:
        def keyset(S, i):
            ks = []
            for (c, g1, g2) in jet.terms[S]:
                gs = (g1, g2)
                if len(gs[i]) == 1:
                    other = tuple(np.round(sorted(gs[1 - i]), 12))
                    ks.append((round(c.real, 12), round(c.imag, 12), other))
            return sorted(ks)
        kx = keyset(X, iX); ky = keyset(Y, iY)
        if kx != ky:
            ok = False
    return ok


def random_general_jet(rng, mu, lam=1.0, n_orbit=2, n_wind=1, n_chain=4, n_iso=2, nmulti_max=3, phase=1.0):
    """random general (Sp') jet; c_t = phase * real * (-i)^d_t, so that every c_t i^(n_t) has the same phase and the
    jet is a fixed phase times a real rational function (Assumption R); energies in [-lam, -mu] (NF)"""
    jet = Jet(); jet.phase = phase
    U = lambda: -rng.uniform(mu, lam)
    Um = lambda n: list(-rng.uniform(mu, lam, size=n))
    # hexagon orbits
    for o in range(n_orbit):
        c = phase*rng.normal()
        e = {k: U() for k in ('1', '2', '12', 'V', '1V', '2V')}
        jet.add('BB', c, [e['1']], [e['12']]); jet.add('BF', c, [e['1']], [e['1V']]); jet.add('FF', c, [e['V']], [e['1V']])
        jet.add('FFp', c, [e['V']], [e['2V']]); jet.add('BFp', c, [e['2']], [e['2V']]); jet.add('BBp', c, [e['2']], [e['12']])
    # winding cycles (twice around the hexagon, different energies on the two turns)
    for w in range(n_wind):
        c = phase*rng.normal()
        e = [{k: U() for k in ('1', '2', '12', 'V', '1V', '2V')} for _ in range(2)]
        for t in range(2):
            E = e[t]; Enext = e[1 - t]
            jet.add('BB', c, [E['1']], [E['12']]); jet.add('BF', c, [E['1']], [E['1V']]); jet.add('FF', c, [E['V']], [E['1V']])
            jet.add('FFp', c, [E['V']], [E['2V']]); jet.add('BFp', c, [E['2']], [E['2V']])
            jet.add('BBp', c, [E['2']], [Enext['12']])   # (1,2)-swap partner of BB on the NEXT turn
    # two-chains with a shared multi-state other gap
    edges = [('BB', 'BF', 'g1'), ('BF', 'FF', 'g2'), ('FF', 'FFp', 'g1'), ('FFp', 'BFp', 'g2'), ('BFp', 'BBp', 'g1'),
             ('BBp', 'BB', 'g2')]
    for ch in range(n_chain):
        X, Y, which = edges[int(rng.integers(0, 6))]
        n = int(rng.integers(2, nmulti_max + 1))
        c = phase*rng.normal()*lam**(n - 1)*(-1j)**(n - 1)    # (R): c_t i^(n_t) must have a common phase
        shared = Um(n)
        if (X, Y) == ('BB', 'BF'):
            jet.add('BB', c, shared, [U()]); jet.add('BF', c, shared, [U()])
        elif (X, Y) == ('BF', 'FF'):
            jet.add('BF', c, [U()], shared); jet.add('FF', c, [U()], shared)
        elif (X, Y) == ('FF', 'FFp'):
            jet.add('FF', c, shared, [U()]); jet.add('FFp', c, shared, [U()])
        elif (X, Y) == ('FFp', 'BFp'):
            jet.add('FFp', c, [U()], shared); jet.add('BFp', c, [U()], shared)
        elif (X, Y) == ('BFp', 'BBp'):
            jet.add('BFp', c, shared, [U()]); jet.add('BBp', c, shared, [U()])
        else:
            jet.add('BBp', c, [U()], shared); jet.add('BB', c, [U()], shared)
    # isolated multi-multi terms
    for it in range(n_iso):
        s = SECTORS[int(rng.integers(0, 6))]
        n1 = int(rng.integers(2, nmulti_max + 1)); n2 = int(rng.integers(2, nmulti_max + 1))
        c = phase*rng.normal()*lam**(n1 + n2 - 2)*(-1j)**(n1 + n2 - 2)   # (R)
        jet.add(s, c, Um(n1), Um(n2))
    # lambda and mu used in the bounds are the actual max/min |A| of the jet (Jet.lam_mu), not the sampling range
    return jet


def check_R(jet, ntest=50, seed=5):
    """(R): J^(sigma)(p) / (fixed phase) real for real p (away from poles); returns max |Im| / |value| after removing
    the phase of the single-state Jcal (times i^2)"""
    rng = np.random.default_rng(seed)
    ph = jet.Jcal('BB')*(1j)**2
    ph = ph/abs(ph)
    worst = 0.0
    for s in SECTORS:
        for _ in range(ntest):
            p1, p2 = rng.normal(size=2)*3
            v = jet.sector(s, p1 + 0j, p2 + 0j)/ph
            worst = max(worst, abs(v.imag)/max(abs(v), 1e-300))
    return worst
