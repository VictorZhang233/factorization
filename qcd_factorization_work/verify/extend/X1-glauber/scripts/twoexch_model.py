# Two spectator-spectator (SS) Glauber exchanges between ONE spectator of jet A and ONE spectator of jet B,
# amplitude side, scalar spectator model (Ex. E.23 extended), exact connecting propagators.
# Computes the joint ordering weights W(piA,piB) = I(piA,piB)/sum I and p_opp = W(12,21)+W(21,12).
#
# Conventions: k_e flows from B into A (amplitude side).  Jet A sees k_e^- , jet B sees p_e = -k_e^+.
# Colour-ordered covariant jet functions ([12] = insertion 1 nearer the hadron vertex along the spectator):
#   J_A^[12](k1,k2) = i^3 / [ (k1+k2-beta+i0) (alpha0-k1-k2+i0) (alpha1-k2+i0) ]
#   J_A^[21](k1,k2) = i^3 / [ (k1+k2-beta+i0) (alpha0-k1-k2+i0) (alpha2-k1+i0) ]
# Glauber propagators R_e(k) = 1/(2 k_e^+ k_e^- - a_e + i0), a_e = k_Te^2.
# Step 1 (exact): k^- integrals by residues at fixed k^+ (quadrant formulas, see REPORT Lemma L3).
# Step 2 (exact for finite eta): inner k_2^+ integral over half-lines by the log-residue formula.
# Step 3: outer k_1^+ integral numerically (mpmath), finite eta, then eta -> 0 extrapolation.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
I = mp.mpc(0, 1)

def E(pT, m, pplus):
    return (pT[0]**2 + pT[1]**2 + m**2) / (2*pplus)

def jet_params(lam, M, ma, ms, xs, sT, k1T, k2T):
    """energies of the scalar spectator jet (all in units where P^+ = 1)."""
    P = M**2/2
    sub = lambda u, v: (u[0]-v[0], u[1]-v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1-xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    d0 = P - Ea - Es0                 # soft-free initial state {a, s0}
    d10 = P - Ea - Es1                # d_1(k1) = d10 + k1   (state {a, s1})
    d20 = P - Ea - Es2                # d_2(k2) = d20 + k2
    beta = Ea + Es - P                # d_12(K) = K - beta   (state {a, s})
    al0 = Es - Es0; al1 = Es - Es1; al2 = Es - Es2   # final states f0 = al0-K, f1 = al1-k2, f2 = al2-k1
    return dict(d0=d0, d10=d10, d20=d20, beta=beta, al0=al0, al1=al1, al2=al2)

def int_halfline(C, m, facs, sign):
    """ Int over x in (0,inf) (sign=+1) or (-inf,0) (sign=-1) of C * x^m / prod_j (g_j x - h_j).
        Simple poles assumed; uses Int_0^inf f = -sum Res[f(z) log(-z)]. """
    if sign < 0:   # x = -u
        facs = [(-g, h) for (g, h) in facs]
        C = C * ((-1)**m);
    # now integral over u in (0,inf) of C u^m / prod (g u - h)
    poles = [h/g for (g, h) in facs]
    tot = mp.mpc(0)
    for j, c in enumerate(poles):
        res = C * c**m / facs[j][0]
        for i2, (g, h) in enumerate(facs):
            if i2 != j:
                res = res / (g*c - h)
        tot += -res * mp.log(-c)
    return tot

def F_A_terms(y, pa, a1, a2, eta, colour):
    """ A-side result of the exact k^- integrals, as a list of (C, m, facs) in the variable x = k2^+,
        for fixed y = k1^+ ; returns dict sign_x -> list. colour in {'12','21'}. """
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    ie = I*eta
    i3 = I**3
    z1 = (a1 - ie)/(2*y)
    out = {+1: [], -1: []}
    if y > 0:
        # (+,+) : F = -(1/(4 y x)) J^(V..)(z1,z2)
        if colour == '12':
            # J^(V12) = i^3/[d0 (al0 - z1 - z2 + ie)(al1 - z2 + ie)],  z2 = (a2-ie)/(2x)
            # -> -(1/(4yx)) i^3 *4x^2 /[d0 (2(al0-z1+ie)x-(a2-ie)) (2(al1+ie)x-(a2-ie))]
            C = -i3/(y*d0)
            out[+1].append((C, 1, [(2*(al0 - z1 + ie), a2 - ie), (2*(al1 + ie), a2 - ie)]))
        else:
            # J^(V21) = i^3/[d0 (al0-z1-z2+ie)(al2 - z1 + ie)]
            C = -i3/(4*y*d0*(al2 - z1 + ie)) * 2
            out[+1].append((C, 0, [(2*(al0 - z1 + ie), a2 - ie)]))
        # (+,-) : only [21]: F = r1 r2 J^(2V1)(z1,z2) = (1/(4yx)) i^3/[d0 (d20+z2+ie)(al2-z1+ie)]
        if colour == '21':
            C = i3/(4*y*d0*(al2 - z1 + ie)) * 2
            out[-1].append((C, 0, [(2*(d20 + ie), -(a2 - ie))]))
    else:
        # (-,+) : only [12]: F = r1 r2 J^(1V2) = (1/(4yx)) i^3/[d0 (d10+z1+ie)(al1 - z2 + ie)]
        if colour == '12':
            C = i3/(4*y*d0*(d10 + z1 + ie)) * 2
            out[+1].append((C, 0, [(2*(al1 + ie), a2 - ie)]))
        # (-,-) : F = -r1 r2 J^(..V)
        if colour == '12':
            # J^(12V) = i^3/[d0 (d10+z1+ie)(z1+z2-beta+ie)]
            C = -i3/(4*y*d0*(d10 + z1 + ie)) * 2
            out[-1].append((C, 0, [(2*(z1 - beta + ie), -(a2 - ie))]))
        else:
            # J^(21V) = i^3/[d0 (d20+z2+ie)(z1+z2-beta+ie)]
            C = -i3/(4*y*d0) * 4
            out[-1].append((C, 1, [(2*(d20 + ie), -(a2 - ie)), (2*(z1 - beta + ie), -(a2 - ie))]))
    return out

def J_B_terms(y, pb, eta, colour):
    """ B-side colour-ordered jet function at p1=-y, p2=-x, as (C, m, facs) in x. """
    d0, d10, d20, beta, al0, al1, al2 = (pb[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    ie = I*eta; i3 = I**3
    # (p1+p2-beta+ie) = (-y-x-beta+ie) = -(x - (-y-beta+ie));  (al0-p1-p2+ie) = (x + y + al0 + ie)
    f1 = (-1, (y + beta - ie))          # -x - y - beta + ie  = (-1)*x - (y+beta-ie)
    f2 = (1, -(y + al0 + ie))           #  x + y + al0 + ie
    if colour == '12':
        f3 = (1, -(al1 + ie))            #  al1 - p2 + ie = al1 + x + ie
        return [(i3, 0, [f1, f2, f3])]
    else:
        C = i3/(al2 + y + ie)            #  al2 - p1 + ie = al2 + y + ie
        return [(C, 0, [f1, f2])]

def inner(y, pa, pb, a1, a2, eta, cA, cB):
    FA = F_A_terms(y, pa, a1, a2, eta, cA)
    JB = J_B_terms(y, pb, eta, cB)
    tot = mp.mpc(0)
    for sx in (+1, -1):
        for (C1, m1, f1) in FA[sx]:
            for (C2, m2, f2) in JB:
                tot += int_halfline(C1*C2, m1 + m2, f1 + f2, sx)
    return tot

def Ival(pa, pb, a1, a2, eta, cA, cB, ymax=1e6, ymin=1e-12):
    f = lambda t, s: inner(s*mp.e**t, pa, pb, a1, a2, eta, cA, cB) * mp.e**t
    tmin, tmax = mp.log(ymin), mp.log(ymax)
    pts = list(mp.linspace(tmin, tmax, 60))
    val = mp.mpc(0)
    for s in (+1, -1):
        val += mp.quad(lambda t: f(t, s), pts)
    return val / (2*mp.pi)**2

if __name__ == '__main__':
    import itertools
    def run(lam, eta_rel, verbose=True):
        sc = lambda v: (lam*v[0], lam*v[1])
        k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
        pa = jet_params(lam, 0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
        # jet B: receives -k ; its spectator transverse momenta shift by +k. Parametrize with its own numbers.
        k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
        pb = jet_params(lam, 0.8*lam, 0.6*lam, 0.5*lam, 0.55, sc((-0.25, 0.4)), k1Tm, k2Tm)
        a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
        eta = eta_rel*lam**2
        res = {}
        for cA, cB in itertools.product(('12','21'), repeat=2):
            res[(cA, cB)] = Ival(pa, pb, a1, a2, eta, cA, cB)
        N = sum(res.values())
        N0 = (I/pa['d0'])*(I/pb['d0'])/(a1*a2)
        popp = (res[('12','21')] + res[('21','12')])/N
        if verbose:
            print(f"lam={lam}, eta/lam^2={eta_rel}:  N/N0 = {mp.nstr(N/N0, 10)}")
            for k, v in res.items():
                print(f"    W{k} = {mp.nstr(v/N, 10)}")
            print(f"    p_opp = {mp.nstr(popp, 12)}")
        return N/N0, popp
    for lam in (0.1, 0.03, 0.01):
        for er in (1e-2, 3e-3, 1e-3):
            run(lam, er)
