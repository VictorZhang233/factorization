# Round-2 reviewer #1: INDEPENDENT real-contour check of T2'(c) (two-sided analytic regulators, fully coincident
# pattern).  No contour rotation.  Jet A localized (L1/L1' weights with an A-side Lorentzian k^- regulator K^-
# on each gluon, or none); a Lorentzian k^+ regulator K^+ on each gluon; jet B = scalar-model 'base' set,
#   J_B^[12](p) = i^3/[(P - beta + i d)(al0 - P + i d)(al1 - p2 + i d)],  J_B^[21]: (al2 - p1 + i d) instead,
# P = p1 + p2, p = -k^+ (real axis, finite width d, d -> 0 numerically).
#   I(piA, piB) = int d^2u/(2pi)^2 W^[piA]_{K^-}(u) chi^+(u1) chi^+(u2) J_B^[piB](-u),  p_opp = (I(12,21)+I(21,12))/N.
# Inner u2 integral: exact partial fractions (principal Log); outer u1: mpmath quad with break points.
# Target values (fix_r1_logs/regulator_indep_B.log, rotated contour): K^+ = 100 lambda_B:
#   no K^- : 0.013880-1.564651i ; K^+K^-/a = 1000: 0.013749-1.550427i ; 1: 0.149117-0.217115i ; 1e-3: 0.499493+0.000001i
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
I_ = mp.mpc(0, 1)

def E(pT, m, x):
    return (mp.mpf(pT[0])**2 + mp.mpf(pT[1])**2 + mp.mpf(m)**2)/(2*mp.mpf(x))

def jet_params(M, ma, ms, xs, sT, k1T, k2T):
    P = mp.mpf(M)**2/2
    sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1 - xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P - Ea - Es0, beta=Ea + Es - P, al0=Es - Es0, al1=Es - Es1, al2=Es - Es2)

k1T, k2T = (0.8, 0.1), (-0.3, 0.9)
pb = jet_params(0.8, 0.6, 0.5, 0.55, (-0.25, 0.4), (-0.8, -0.1), (0.3, -0.9))
a1 = mp.mpf(0.8)**2 + mp.mpf(0.1)**2; a2 = mp.mpf(0.3)**2 + mp.mpf(0.9)**2
lamB = abs(pb['d0']); Jcal = I_/pb['d0']; aa = mp.sqrt(a1*a2)

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
    n, roots = R
    # nudge (removable) coincident roots apart by a negligible amount (40-digit arithmetic)
    roots = list(roots)
    for i in range(len(roots)):
        for j in range(i):
            if abs(roots[i] - roots[j]) < mp.mpf('1e-30')*(1 + abs(roots[i])):
                roots[i] += mp.mpf('1e-28')*(1 + abs(roots[i]))
    tot = mp.mpc(0)
    for k_, c in enumerate(roots):
        den = mp.mpc(1)
        for j, cj in enumerate(roots):
            if j != k_:
                den *= (c - cj)
        r = peval(n, c)/den
        tot += (-r*mp.log(-c)) if side > 0 else (r*mp.log(c))
    return tot

def u2_weight_options(K, q2):
    tz = 'F' if q2 > 0 else 'B'
    if K is None:
        return [(tz, ('z',), ([mp.mpc(1)], []))]
    kap = a2/(2*K)
    uz = ([mp.mpc(1), 0, 0], [I_*kap, -I_*kap])
    up = ([I_*kap/2], [-I_*kap])
    um = ([-I_*kap/2], [I_*kap])
    return [(tz, ('z',), uz), ('B', ('c', I_*K), up), ('F', ('c', -I_*K), um)]

def u1_weight_options(u1, K):
    z1 = a1/(2*u1)
    tz = 'F' if u1 > 0 else 'B'
    if K is None:
        return [(tz, z1, mp.mpc(1))]
    return [(tz, z1, K**2/(z1**2 + K**2)), ('B', I_*K, z1/(2*(z1 - I_*K))), ('F', -I_*K, z1/(2*(z1 + I_*K)))]

def race_factor(order, t1, p1, t2, p2desc):
    """race weight of colour order '12' or '21' as rational function of u2"""
    one, zero = ([mp.mpc(1)], []), ([mp.mpc(0)], [])
    if t1 == 'B' and t2 == 'F':
        return one if order == '12' else zero
    if t1 == 'F' and t2 == 'B':
        return zero if order == '12' else one
    first_is_1 = (t1 == 'F' and order == '12') or (t1 == 'B' and order == '21')
    # first_is_1: weight p1/(p1+p2); else p2/(p1+p2)
    if p2desc[0] == 'z':
        cr = -a2/(2*p1)
        return ([mp.mpc(1), mp.mpc(0)], [cr]) if first_is_1 else ([-cr], [cr])
    p2 = p2desc[1]
    return ([p1/(p1 + p2)], []) if first_is_1 else ([p2/(p1 + p2)], [])

def outer_integrand(u1, Kp, Km, d, combos):
    iD = I_*d
    ca = -u1 - pb['beta'] + iD
    cc = -pb['al0'] - u1 - iD
    cb1 = -pb['al1'] - iD
    C2 = 1/(pb['al2'] + u1 + iD)
    JB = {'12': (I_, ([mp.mpc(1)], [ca, cc, cb1])),
          '21': (I_*C2, ([mp.mpc(1)], [ca, cc]))}
    chi1 = 1 if Kp is None else Kp**2/(u1**2 + Kp**2)
    chi2R = ([mp.mpc(1)], []) if Kp is None else ([Kp**2], [I_*Kp, -I_*Kp])
    K1 = None if Km is None else Km*(1 + mp.mpf('1e-12'))
    out = {}
    for (oA, oB) in combos:
        pre, JBR = JB[oB]
        tot = mp.mpc(0)
        for q2 in (1, -1):
            if oA == 'one':
                tot += halfline_int(rmul(chi2R, JBR), q2)
                continue
            for (t1, p1, w1) in u1_weight_options(u1, K1):
                for (t2, p2desc, w2R) in u2_weight_options(Km, q2):
                    rf = race_factor(oA, t1, p1, t2, p2desc)
                    if len(rf[0]) == 1 and rf[0][0] == 0:
                        continue
                    tot += w1*halfline_int(rmul(rmul(rmul(w2R, rf), chi2R), JBR), q2)
        out[(oA, oB)] = pre*chi1*tot
    return out

def compute(Kp, Km, d):
    combos = [('12', '12'), ('12', '21'), ('21', '12'), ('21', '21')]
    special = [-pb['beta'], -pb['al0'], pb['al1'] - pb['beta'], pb['al1'] - pb['al0'], -pb['al2'], mp.mpf(0)]
    pos = sorted([x for x in special if x > 0]); neg = sorted([x for x in special if x < 0])
    def brk(centres, lo, hi):
        b = [lo, hi]
        for c in centres:
            for h in (-10*d, -d, 0, d, 10*d):
                x = c + h
                if lo < x < hi:
                    b.append(x)
        return sorted(set(b))
    big = [mp.mpf(10)**e for e in range(1, 9)]
    bp = brk(pos, mp.mpf(0), mp.mpf(10)) + big + [mp.inf]
    bn = [-mp.inf] + [-x for x in reversed(big)] + brk(neg, mp.mpf(-10), mp.mpf(0))
    res = {}
    for cmb in combos:
        f = lambda u, cmb=cmb: outer_integrand(u, Kp, Km, d, [cmb])[cmb]
        res[cmb] = (mp.quad(f, bp, maxdegree=8) + mp.quad(f, bn, maxdegree=8))/(2*mp.pi)**2
    N = sum(res.values())
    return N/Jcal, (res[('12', '21')] + res[('21', '12')])/N

if __name__ == '__main__':
    print(f"jet B base: al0={mp.nstr(pb['al0'],6)} al1={mp.nstr(pb['al1'],6)} al2={mp.nstr(pb['al2'],6)} "
          f"beta={mp.nstr(pb['beta'],6)} d0={mp.nstr(pb['d0'],6)}; a1={mp.nstr(a1,4)} a2={mp.nstr(a2,4)}", flush=True)
    Kp_r = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf(100)
    Kms = sys.argv[2].split(',') if len(sys.argv) > 2 else ['none', '1000', '1', '0.001']
    ds = sys.argv[3].split(',') if len(sys.argv) > 3 else ['1e-3', '1e-4', '1e-5']
    Kp = Kp_r*lamB
    for Kms_ in Kms:
        Km = None if Kms_ == 'none' else mp.mpf(Kms_)*aa/Kp
        for d in ds:
            nn, po = compute(Kp, Km, mp.mpf(d))
            print(f"  K^+ = {mp.nstr(Kp_r,4)} lambda_B, K^+K^-/a = {Kms_:>6s}, d = {d}: N/Jcal = {mp.nstr(nn, 8)}  "
                  f"p_opp = {mp.nstr(po, 8)}", flush=True)
