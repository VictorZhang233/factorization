"""X2 fix round 2 / r2_spacelike_poles.py -- complete real-base pole structure of the space-like-regulated soft term
C_S = 1/(G h1Y h2Y) of model (M3) (corrects X2-Prop3.14(b),(c); review r2_1).

G   = M2 + kap - 2 x k- - i eta wG
h1Y = 2P (k- - e x)   - i eta w1                      e = exp(-2Y)
h2Y = 2P'(x - e k-)   - sigma * i eta w2              sigma = +1: assignment of t16/r1_spacelike (both -i0, inherited
                                                       from the light-like eikonals h1 = 2Pk- - i0, h2 = 2P'k+ - i0)
                                                       sigma = -1: Collins (10.68) sign pattern transplanted verbatim
rho(x) = (1/(i pi)) int dk- C_S  (own exact residue code at finite eta; for sigma=+1 cross-checked with the engine).
(1) closed forms; (2) base poles and their sides at finite eta (roots of the residue denominators); (3) the real-axis
integral at finite eta converges, as eta -> 0, to  PV + i pi sum_{poles above} Res - i pi sum_{poles below} Res;
(4) compatibility of each assignment with the symmetric Glauber deformation of (M3), k+ -> k+ - i delta,
k- -> k- - i delta (the t1 pole in k- and the t2 pole in k+ lie in the upper half planes)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import mpmath as mp
mp.mp.dps = 40
P = Pp = 1/mp.sqrt(2)
WG, W1, W2 = mp.mpf('1.03'), mp.mpf('1.17'), mp.mpf('0.83')

def factors(xv, kv, M2, Y, eta, sigma):
    e = mp.e**(-2*Y)
    # each factor = a + b k-   (a complex, includes -i eta w)
    return [(M2 + kv - 1j*eta*WG, -2*xv),
            (-2*P*e*xv - 1j*eta*W1, 2*P),
            (2*Pp*xv - sigma*1j*eta*W2, -2*Pp*e)]

def rho(xv, kv, M2, Y, eta, sigma):
    """(1/(i pi)) * int dk- prod 1/(a_j + b_j k-), exact residues (eta > 0)."""
    fs = factors(xv, kv, M2, Y, eta, sigma)
    poles = []
    for j, (aj, bj) in enumerate(fs):
        kj = -aj/bj
        res = 1/bj
        for i, (ai, bi) in enumerate(fs):
            if i != j:
                res /= (ai + bi*kj)
        poles.append((kj, res))
    up = [r for (kk, r) in poles if mp.im(kk) > 0]
    lo = [r for (kk, r) in poles if mp.im(kk) < 0]
    if len(up) <= len(lo):
        return 2*sum(up) if up else mp.mpf(0)          # (2 pi i / i pi) sum Res(upper)
    return -2*sum(lo)

def closed(xv, kv, M2, Y, sigma):
    """eta -> 0 closed forms (real x away from the poles)."""
    e = mp.e**(-2*Y); S = M2 + kv
    if sigma == 1:
        if xv > 0:
            return 1/(P*(S - 2*e*xv**2)*(2*Pp*xv*(1 - e**2)))
        return 1/(Pp*(S - 2*xv**2/e)*(2*P*xv*(1 - e**2)))
    if xv > 0:
        return xv/(P*Pp*(S - 2*e*xv**2)*(2*xv**2 - e*S))
    return mp.mpf(0)

M2, Y, kv = mp.mpf('1e-3'), mp.mpf(3), mp.mpf('0.01')
e = mp.e**(-2*Y); S = M2 + kv
x0 = mp.sqrt(S/(2*e)); x0p = mp.sqrt(S*e/2)
print(f"M2={M2}, Y={Y}, kap={kv}:  x0 = sqrt((M2+kap)e^(2Y)/2) = {mp.nstr(x0, 10)},  x0' = sqrt((M2+kap)e^(-2Y)/2) = {mp.nstr(x0p, 10)}")

print("\n(1) closed forms vs exact residues at eta = 1e-30 (both assignments); engine cross-check for sigma=+1")
import t16_massive_regulated as T16
for sigma in (1, -1):
    for xv in [mp.mpf('-0.3'), -2*x0p, -x0p/2, mp.mpf('-1e-5'), mp.mpf('1e-5'), x0p/2, 2*x0p, x0/2, 2*x0]:
        r = rho(xv, kv, M2, Y, mp.mpf('1e-30'), sigma); c = closed(xv, kv, M2, Y, sigma)
        extra = ''
        if sigma == 1:
            eng = T16.rho('C_S', np.array([float(xv)]), np.array([float(kv)]), float(M2), float(Y), -1)[0]
            extra = f"  engine {eng:+.10e}"
        print(f"   sigma={sigma:+d} x={mp.nstr(xv, 6):>12}: residues {mp.nstr(mp.re(r), 12):>20}  closed {mp.nstr(c, 12):>20}{extra}")
c0 = 1/(2*P*Pp*S*(1 - e**2))
print(f"   sigma=+1: x*rho at x=+-1e-9: {mp.nstr(1e-9*mp.re(rho(mp.mpf('1e-9'), kv, M2, Y, mp.mpf('1e-40'), 1)), 12)}, "
      f"{mp.nstr(-1e-9*mp.re(rho(mp.mpf('-1e-9'), kv, M2, Y, mp.mpf('1e-40'), 1)), 12)} (sign-adjusted);  c = 1/(2PP'(M2+kap)(1-e^-4Y)) = {mp.nstr(c0, 12)}")

print("\n(2) base poles at finite eta = 1e-7: complex roots of 1/rho(z), rho continued from the real region it serves")
def rho_sel(z, eta, sigma, region):
    """analytic continuation in z of the residue sum used on the real region ('pos': x>0, 'neg': x<0)"""
    fs = factors(z, kv, M2, Y, eta, sigma)
    if sigma == 1:
        sel, sgn = ([1], 2) if region == 'pos' else ([2], -2)      # x>0: close up on h1Y; x<0: close down on h2Y
    else:
        if region == 'neg':
            return mp.mpf(0)                                        # all three poles upper: rho = 0
        sel, sgn = ([0], -2)                                        # x>0: close down on G
    tot = 0
    for j in sel:
        aj, bj = fs[j]; kj = -aj/bj; res = 1/bj
        for i, (ai, bi) in enumerate(fs):
            if i != j:
                res /= (ai + bi*kj)
        tot += res
    return sgn*tot
def roots_quadratic(c2, c1, c0):
    if c2 == 0:
        return [-c0/c1]
    d = mp.sqrt(c1**2 - 4*c2*c0)
    return [(-c1 + d)/(2*c2), (-c1 - d)/(2*c2)]
def base_pole_roots(sigma, eta, region):
    """exact complex poles in z of the region-selected residue sum at finite eta (explicit polynomials)"""
    ee = e; I = 1j
    if sigma == 1 and region == 'pos':      # residue at h1Y pole k1 = e z + i eta w1/(2P)
        return (roots_quadratic(-2*ee, -I*eta*W1/P, S - I*eta*WG)                          # G(k1) = 0
                + [I*eta*(W2 + Pp*ee*W1/P)/(2*Pp*(1 - ee**2))])                            # h2Y(k1) = 0
    if sigma == 1 and region == 'neg':      # residue at h2Y pole k2 = (2P'z - i eta w2)/(2P'e)
        return (roots_quadratic(-2/ee, I*eta*W2/(Pp*ee), S - I*eta*WG)                      # G(k2) = 0
                + [I*eta*(W1 + P*W2/(Pp*ee))/(2*P*(1/ee - ee))])                            # h1Y(k2) = 0
    if sigma == -1 and region == 'pos':     # residue at G pole: rho = z/([..][..])
        return (roots_quadratic(-2*P*ee, -I*eta*W1, P*(S - I*eta*WG))
                + roots_quadratic(2*Pp, I*eta*W2, -Pp*ee*(S - I*eta*WG)))
    return []
def find_pole(xp, sigma, eta, region):
    rts = base_pole_roots(sigma, eta, region)
    return min(rts, key=lambda z: abs(z - xp))
CAND = {1: [('x = 0 (seen from x>0)', mp.mpf(0), 'pos'), ('x = 0 (seen from x<0)', mp.mpf(0), 'neg'),
            ("x = -x0'", -x0p, 'neg'), ('x = +x0', x0, 'pos')],
        -1: [("x = +x0'", x0p, 'pos'), ('x = +x0', x0, 'pos')]}
for sigma in (1, -1):
    print(f"   sigma={sigma:+d}:")
    for lab, xp, region in CAND[sigma]:
        z = find_pole(xp, sigma, mp.mpf('1e-7'), region)
        side = 'ABOVE the real axis (x_p + i0)' if mp.im(z) > 0 else 'BELOW the real axis (x_p - i0)'
        print(f"      {lab:24s}: pole at {mp.nstr(mp.re(z), 12):>16} {mp.nstr(mp.im(z), 4):>11} i  -> {side}")
print("   sigma=-1: x = 0 is not a pole (rho ~ -x/(P P' e (M2+kap)^2) -> 0), and rho = 0 identically for x < 0.")

print("\n(3) real-axis integrals at finite eta vs the distributional limit PV +- i pi Res, one interval per pole")
RES = {1: [('x=0', mp.mpf(0), c0, (mp.mpf('-0.002'), mp.mpf('0.002'))),
           ("x=-x0'", -x0p, -1/(2*S*(1 - e**2))/(2*P*Pp), (mp.mpf('-0.4'), mp.mpf('-0.002'))),
           ('x=x0', x0, -1/(2*S*(1 - e**2))/(2*P*Pp), (mp.mpf(1), mp.mpf(3)))],
       -1: [("x=x0'", x0p, 1/(4*P*Pp*S*(1 - e**2)), (mp.mpf('0.002'), mp.mpf('0.1'))),
            ('x=x0', x0, -1/(4*P*Pp*S*(1 - e**2)), (mp.mpf(1), mp.mpf(3)))]}
def closed_hp(t, sigma):
    with mp.workdps(120):
        return +closed(t, kv, M2, Y, sigma)
for sigma in (1, -1):
    print(f"   sigma={sigma:+d}:")
    for lab, xp, r, (a_, b_) in RES[sigma]:
        # check the residue numerically:  r = lim (x - x_p) rho(x)
        dxx = mp.mpf('1e-15')*(1 + abs(xp))
        rnum = (closed_hp(xp + dxx, sigma)*dxx + closed_hp(xp - dxx, sigma)*(-dxx))/2
        reg = lambda t: closed(t, kv, M2, Y, sigma) - r/(t - xp)
        dl = mp.mpf('1e-14')*(1 + abs(xp))       # excised symmetric interval: its PV contribution is 2*dl*reg(xp) = O(1e-12)
        pv = mp.quad(reg, [a_, xp - dl]) + mp.quad(reg, [xp + dl, b_]) + r*mp.log(abs((b_ - xp)/(a_ - xp)))
        lim_up = pv + 1j*mp.pi*r; lim_lo = pv - 1j*mp.pi*r
        vals = []
        for eta in ['1e-6', '1e-8', '1e-10']:
            etv = mp.mpf(eta)
            region = 'pos' if (xp > 0 or (xp == 0 and False)) else 'neg'
            pts = [a_, b_]
            for reg_ in (['pos', 'neg'] if xp == 0 else [region]):
                zp = find_pole(xp, sigma, etv, reg_)
                wdt = abs(mp.im(zp))
                for fct in (0, mp.mpf('0.01'), mp.mpf('0.1'), 1, 10, 100, 10**3, 10**4, 10**5):
                    pts += [xp - fct*wdt, xp + fct*wdt]
            pts = sorted(set(p for p in pts if a_ <= p <= b_))
            vals.append(mp.quad(lambda t: rho(t, kv, M2, Y, etv, sigma), pts))
        d_up = abs(vals[-1] - lim_up); d_lo = abs(vals[-1] - lim_lo)
        verdict = 'pole ABOVE (+i0)' if d_up < d_lo else 'pole BELOW (-i0)'
        print(f"      {lab:7s} on [{mp.nstr(a_,3)},{mp.nstr(b_,3)}]: Res = {mp.nstr(r, 10)} (numerical {mp.nstr(rnum, 10)})")
        print(f"              PV + i pi Res = {mp.nstr(lim_up, 12)};  PV - i pi Res = {mp.nstr(lim_lo, 12)}")
        print(f"              finite eta 1e-6, 1e-8, 1e-10: {', '.join(mp.nstr(v, 12) for v in vals)}  -> {verdict}")

print("\n(4) compatibility with the symmetric Glauber deformation of (M3): k+ -> k+ - i d, k- -> k- - i d  (d > 0)")
print("    (t1 = kap + 2(P-k+)k- - i0 has its k- pole at -kap/2(P-k+) + i0; t2 = kap + 2P'k+ - 2k+k- - i0 has its k+ pole")
print("     at -kap/2(P'-k-) + i0: both lie in the upper half planes, so the Glauber region is left by Im k+- < 0.)")
for lab, (alpha, beta), i0sign in [('h1Y = 2P(k- - e k+) - i0', (-2*P*e, 2*P), -1),
                                   ("h2Y = 2P'(k+ - e k-) - i0  [sigma=+1]", (2*Pp, -2*Pp*e), -1),
                                   ("h2Y = 2P'(k+ - e k-) + i0  [sigma=-1]", (2*Pp, -2*Pp*e), +1),
                                   ('t1 (Glauber region, k+- small)', (0, 2*P), -1),
                                   ('t2 (Glauber region, k+- small)', (2*Pp, 0), -1)]:
    imdef = -alpha - beta        # Im of the factor per unit d along the deformation
    ok = (np.sign(float(imdef)) == i0sign)
    print(f"   {lab:42s}: Im(factor)/d = {mp.nstr(imdef, 6):>10}, prescription sign {i0sign:+d} -> {'compatible' if ok else 'OBSTRUCTS the deformation'}")
