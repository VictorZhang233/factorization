# Round-2 reviewer #1: INDEPENDENT real-contour computation of the half-coincident weight W_12 (T3(b),(d),(f)).
# No contour rotation (L5) is used.  Jet A is localized (L1/L1' weights, possibly with an A-side analytic k^-
# regulator chi^- = K^2/(k^2+K^2) on each gluon), jet B is the scalar-model half-coincident jet
#     J_B(p) = i^3 / [(p1 + p2 - beta + i d)(al1 - p1 + i d)(al2 - p2 + i d)],   p = -k^+,
# evaluated on the REAL k^+ axis with a FINITE width d, then d -> 0 is taken numerically.
#     W_12 = (1/Jcal_B) int d^2u/(2pi)^2  W^[12]_K(u) J_B(-u),      Jcal_B = i/d0,  d0 = al1 + al2 - beta.
# Inner u2 integral: exact partial fractions on each half line (principal Log), outer u1 integral: mpmath quad
# with break points at the d-width peaks.  Parameters = 'author' set of scripts/halfcoinc.py (lambda = 1).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40

def E(pT, m, x):
    return (pT[0]**2 + pT[1]**2 + m**2)/(2*x)

def model(variant='author'):
    if variant == 'author':
        k1T, k2T = (0.8, 0.1), (-0.3, 0.9)
        MB, mb, m1, m2 = 1.1, 0.5, 0.4, 0.6; x1, x2 = 0.3, 0.35
        s1T, s2T = (-0.2, 0.3), (0.25, -0.15)
    else:   # 'Basym' of scripts/halfcoinc_sym.py
        k1T, k2T = (0.8, 0.1), (0.1, 0.8)
        MB, mb, m1, m2 = 1.1, 0.5, 0.4, 0.4; x1, x2 = 0.3, 0.3
        s1T, s2T = (-0.2, 0.3), (0.5, -0.4)
    xb = 1 - x1 - x2
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    return dict(al1=mp.mpf(al1), al2=mp.mpf(al2), beta=mp.mpf(beta), a1=mp.mpf(a1), a2=mp.mpf(a2),
                d0=mp.mpf(al1 + al2 - beta))

# rational function in u2:  num (list of coefficients, highest first) / prod (u2 - roots)
def rmul(A, B):
    (na, ra), (nb, rb) = A, B
    n = [mp.mpc(0)]*(len(na) + len(nb) - 1)
    for i, x in enumerate(na):
        for j, y in enumerate(nb):
            n[i + j] += x*y
    return (n, ra + rb)

def peval(n, x):
    s = mp.mpc(0)
    for c in n:
        s = s*x + c
    return s

def halfline_int(R, side):
    """int over u2 in (0,inf) (side=+1) or (-inf,0) (side=-1) of R = (num, roots); deg(den)-deg(num) >= 2"""
    n, roots = R
    tot = mp.mpc(0)
    for k_, c in enumerate(roots):
        den = mp.mpc(1)
        for j, cj in enumerate(roots):
            if j != k_:
                den *= (c - cj)
        r = peval(n, c)/den
        tot += (-r*mp.log(-c)) if side > 0 else (r*mp.log(c))
    return tot

def weight_terms(u, a, K, q):
    """list of (type, p as function of nothing (complex number) or 'z', rational factor in the variable) for one line.
       Returned as (type, pval, R) where R is the u-weight as a rational function of the same line's variable u
       (only used for the u2 line); for the u1 line the weights are numbers."""
    raise NotImplementedError

def u2_weight_options(a2, K, q2):
    """for line 2: list of (type, p2 descriptor, rational weight in u2).  p2 descriptor: ('z',) or ('c', value)."""
    tz = 'F' if q2 > 0 else 'B'
    if K is None:
        return [(tz, ('z',), ([mp.mpc(1)], []))]
    kap = a2/(2*K)
    uz = ([mp.mpc(1), 0, 0], [mp.mpc(0, 1)*kap, -mp.mpc(0, 1)*kap])        # u2^2/((u2-i kap)(u2+i kap))
    up = ([mp.mpc(0, 1)*kap/2], [-mp.mpc(0, 1)*kap])                          # (i kap/2)/(u2 + i kap): pole +iK (B)
    um = ([-mp.mpc(0, 1)*kap/2], [mp.mpc(0, 1)*kap])                          # (-i kap/2)/(u2 - i kap): pole -iK (F)
    return [(tz, ('z',), uz), ('B', ('c', mp.mpc(0, 1)*K), up), ('F', ('c', -mp.mpc(0, 1)*K), um)]

def u1_weight_options(u1, a1, K):
    z1 = a1/(2*u1)
    tz = 'F' if u1 > 0 else 'B'
    if K is None:
        return [(tz, z1, mp.mpc(1))]
    return [(tz, z1, K**2/(z1**2 + K**2)), ('B', mp.mpc(0, 1)*K, z1/(2*(z1 - mp.mpc(0, 1)*K))),
            ('F', -mp.mpc(0, 1)*K, z1/(2*(z1 + mp.mpc(0, 1)*K)))]

def race12_factor(t1, p1, t2, p2desc, a2):
    """race weight of colour order (12) as a rational function of u2 (p2 = z2 = a2/(2 u2) or a constant)"""
    if t1 == 'B' and t2 == 'F':
        return ([mp.mpc(1)], [])
    if t1 == 'F' and t2 == 'B':
        return ([mp.mpc(0)], [])
    if p2desc[0] == 'z':
        cr = -a2/(2*p1)
        if t1 == 'F':                      # p1/(p1+p2) = u2/(u2 - cr)
            return ([mp.mpc(1), mp.mpc(0)], [cr])
        else:                              # p2/(p1+p2) = (-cr)/(u2 - cr)
            return ([-cr], [cr])
    p2 = p2desc[1]
    if t1 == 'F':
        return ([p1/(p1 + p2)], [])
    return ([p2/(p1 + p2)], [])

def outer_integrand(u1, m, K, d, which):
    """which = 'W12' (colour order 12) or 'N' (weight 1)."""
    al1, al2, beta, a1, a2 = m['al1'], m['al2'], m['beta'], m['a1'], m['a2']
    iD = mp.mpc(0, d)
    C1 = 1/(al1 + u1 + iD)
    ca = -u1 - beta + iD; cb = -al2 - iD
    JBu2 = ([mp.mpc(1)], [ca, cb])           # times i*C1
    tot = mp.mpc(0)
    q1 = 1 if u1 > 0 else -1
    for q2 in (1, -1):
        if which == 'N':
            tot += halfline_int(JBu2, q2)
            continue
        # line-1 regulator scale slightly detuned (1e-12 relative) to avoid exactly coincident poles
        K1 = None if K is None else K*(1 + mp.mpf('1e-12'))
        for (t1, p1, w1) in u1_weight_options(u1, a1, K1):
            for (t2, p2desc, w2R) in u2_weight_options(a2, K, q2):
                rf = race12_factor(t1, p1, t2, p2desc, a2)
                if rf[0] == [0] or (len(rf[0]) == 1 and rf[0][0] == 0):
                    continue
                Rtot = rmul(rmul(w2R, rf), JBu2)
                tot += w1*halfline_int(Rtot, q2)
    return mp.mpc(0, 1)*C1*tot

def compute(m, K, d, which):
    al1, al2, beta = m['al1'], m['al2'], m['beta']
    pts_pos = sorted(set([mp.mpf(0)] + [x for x in (-al1,) if x > 0]))
    pts_neg = sorted(set([x for x in (al2 - beta, -beta) if x < 0]))
    def brk(centres, lo, hi):
        b = [lo]
        for c in centres:
            for h in (-10*d, -d, 0, d, 10*d):
                x = c + h
                if lo < x < hi:
                    b.append(x)
        b.append(hi)
        return sorted(set(b))
    f = lambda u: outer_integrand(u, m, K, d, which)
    bp = brk([x for x in pts_pos if x > 0], mp.mpf(0), mp.mpf(50)) + [mp.inf]
    bn = [-mp.inf] + brk(pts_neg, mp.mpf(-50), mp.mpf(0))
    Ipos = mp.quad(f, bp, maxdegree=8)
    Ineg = mp.quad(f, bn, maxdegree=8)
    return (Ipos + Ineg)/(2*mp.pi)**2

if __name__ == '__main__':
    variant = sys.argv[1] if len(sys.argv) > 1 else 'author'
    Klist = sys.argv[2].split(',') if len(sys.argv) > 2 else ['none']
    m = model(variant)
    lamB = abs(m['d0']); a = mp.sqrt(m['a1']*m['a2'])
    Jcal = mp.mpc(0, 1)/m['d0']
    print(f"[{variant}] al1={mp.nstr(m['al1'],6)} al2={mp.nstr(m['al2'],6)} beta={mp.nstr(m['beta'],6)} "
          f"d0={mp.nstr(m['d0'],6)} a1={mp.nstr(m['a1'],4)} a2={mp.nstr(m['a2'],4)}", flush=True)
    for Ks in Klist:
        K = None if Ks == 'none' else mp.mpf(Ks)*a/lamB
        for d in ('1e-3', '1e-4', '1e-5', '1e-6'):
            dd = mp.mpf(d)
            N = compute(m, None, dd, 'N')
            W = compute(m, K, dd, 'W12')
            print(f"  K^- = {Ks:>6s} x a/lambda_B, d = {d}:  N/Jcal_B = {mp.nstr(N/Jcal, 10)}   "
                  f"W12 (normalized by Jcal_B) = {mp.nstr(W/Jcal, 10)}   W12/N = {mp.nstr(W/N, 10)}", flush=True)
