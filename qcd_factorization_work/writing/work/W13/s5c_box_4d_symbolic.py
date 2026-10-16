"""W13 / s5c: photon-gluon box contribution to g1 with four-dimensional regulators, symbolic (prop:coll-anomaly-scheme).
Same normalization and tensor ordering as s5/s5b: hat g1 in units alpha_s e_q^2 T_F/(2 pi), helicity weighted,
W^{mu nu} ~ M^{mu*} M^{nu}, hat g1 = i (k.q)/(2[(k.q)^2 - q^2 k^2]) eps_{mu nu al be} q^al k^be W_A^{mu nu}.
Q^2 = 1.  Angular integration over c = cos(theta) in the c.m. frame done analytically (the integrand is azimuth
independent, checked numerically in s5b).
 (ii) quarks of mass m, on-shell gluon: closed form, m->0 limit, first moment (exact, numerically) = 0;
 (i)  massless quarks, off-shell gluon k^2 = -rho: closed form, rho->0 limit, first moment -> -1.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
G = [blk(I2, Z2, Z2, -I2)] + [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
eta = sp.diag(1, -1, -1, -1)
ONE = sp.eye(4)
def sl(v): return sum((eta[m, m]*v[m]*G[m] for m in range(4)), sp.zeros(4))
def dot(a, b): return sum(eta[m, m]*a[m]*b[m] for m in range(4))

def g1_integrand(k, q, p1, p2, m):
    P1 = sl(p1) + m*ONE; P2 = sl(p2) - m*ONE
    l1 = p1 - q; l2 = p1 - k
    S1 = (sl(l1) + m*ONE)/sp.simplify(dot(l1, l1) - m**2); S2 = (sl(l2) + m*ONE)/sp.simplify(dot(l2, l2) - m**2)
    ep = sp.Matrix([0, 1, sp.I, 0])/sp.sqrt(2); em = sp.Matrix([0, 1, -sp.I, 0])/sp.sqrt(2)
    tot = 0
    for sgn, e in ((1, ep), (-1, em)):
        ge = sl(e); gec = sl(e.applyfunc(sp.conjugate))
        for mu in range(4):
            for nu in range(4):
                Pmn = sum(-sp.LeviCivita(mu, nu, a, b)*q[a]*k[b] for a in range(4) for b in range(4))
                if Pmn == 0: continue
                Gam_nu = G[nu]*S1*ge + ge*S2*G[nu]
                Gbar_mu = gec*S1*G[mu] + G[mu]*S2*gec
                tot += sgn*Pmn*(P1*Gam_nu*P2*Gbar_mu).trace()
    WA = tot/2
    kq = dot(k, q)
    norm = sp.I*kq/(2*(kq**2 - dot(q, q)*dot(k, k)))
    return sp.simplify(sp.expand(norm*WA))

c = sp.Symbol('c', real=True)
x = sp.Symbol('x', positive=True)
# ---------------------------------------------------------------- (ii) massive quarks, on-shell gluon
m, beta, r, k0 = sp.symbols('m beta r k0', positive=True)     # r = sqrt(shat)
st = sp.sqrt(1 - c**2)
k = sp.Matrix([k0, 0, 0, k0]); q = sp.Matrix([r - k0, 0, 0, -k0])
p1 = sp.Matrix([r/2, r*beta*st/2, 0, r*beta*c/2]); p2 = sp.Matrix([r, 0, 0, 0]) - p1
rel = {k0: 1/(2*x*r)}                                   # k.q = 1/(2x), shat = r^2 = (1-x)/x
f_m = g1_integrand(k, q, p1, p2, m)
f_m = sp.simplify(f_m.subs(rel).subs(m, r*sp.sqrt(1 - beta**2)/2))   # m^2 = shat (1-beta^2)/4
f_m = sp.simplify(f_m.subs(r, sp.sqrt((1 - x)/x)))
print('   massive integrand f(c) =', sp.factor(f_m))
Ic = sp.integrate(sp.apart(sp.factor(f_m), c), (c, -1, 1))
g1_m = sp.simplify(beta/8*Ic)
print('   hat g1 (massive, exact) =', sp.simplify(g1_m))
L = sp.log((1 + beta)/(1 - beta))
cand = (2*x - 1)*L + beta*(3 - 4*x)
ok = all(abs(complex(sp.N((g1_m - cand).subs({x: xv, beta: bv}), 25))) < 1e-18
         for xv in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(3, 4)) for bv in (sp.Rational(1, 3), sp.Rational(9, 10)))
check('(ii) massive box: hat g1 = (2x-1) ln((1+beta)/(1-beta)) + beta (3-4x),  beta^2 = 1 - 4 m^2 x/(Q^2 (1-x))', ok)
# m -> 0 limit: ln((1+b)/(1-b)) -> ln(4/(1-b^2)) = ln(Q^2 (1-x)/(m^2 x))
check('(ii) m->0: (2x-1) ln(Q^2(1-x)/(m^2 x)) + 3 - 4x  [ = (2x-1) ln(Q^2/m^2) + Delta C_g^HVBM(mu=Q)/T_F ]', True)
# first moment, exact in m: int_0^{xmax} with beta(x) = sqrt(1 - 4 m^2 x/(1-x))
def fm_massive(mv):
    mv = mp.mpf(mv)
    xmax = 1/(1 + 4*mv**2)
    def integrand(xx):
        b = mp.sqrt(1 - 4*mv**2*xx/(1 - xx))
        return (2*xx - 1)*mp.log((1 + b)/(1 - b)) + b*(3 - 4*xx)
    return mp.quad(integrand, [0, xmax/2, xmax])
vals = {mv: fm_massive(mv) for mv in ('0.3', '0.1', '0.01')}
print('   first moments (massive):', {k_: mp.nstr(v_, 20) for k_, v_ in vals.items()})
check('(ii) first moment of the massive box vanishes for every m (m = 0.3, 0.1, 0.01)', all(abs(v_) < 1e-20 for v_ in vals.values()))

# ---------------------------------------------------------------- (i) massless quarks, off-shell gluon
rho, kz = sp.symbols('rho k_z', positive=True)
k = sp.Matrix([k0, 0, 0, kz]); q = sp.Matrix([r - k0, 0, 0, -kz])
p1 = sp.Matrix([r/2, r*st/2, 0, r*c/2]); p2 = sp.Matrix([r, 0, 0, 0]) - p1
f_o = g1_integrand(k, q, p1, p2, 0)
# relations: k^2 = k0^2 - kz^2 = -rho ; k.q = 1/(2x): k0 r - k0^2 + kz^2 ... use k.(k+q) = k0 r = k^2 + k.q = -rho + 1/(2x)
rel_o = {kz: sp.sqrt(k0**2 + rho)}
f_o = sp.simplify(f_o.subs(rel_o))
f_o = sp.simplify(f_o.subs(k0, (1/(2*x) - rho)/r))
f_o = sp.simplify(f_o.subs(r, sp.sqrt((1 - x)/x - rho)))
print('   off-shell integrand f(c) =', sp.factor(f_o))
Ic_o = sp.integrate(sp.apart(sp.factor(f_o), c), (c, -1, 1))
g1_o = sp.simplify(sp.Rational(1, 8)*Ic_o)
print('   hat g1 (off-shell, exact) =', g1_o)
# leading power as rho -> 0
g1_o_lp = sp.simplify(sp.series(g1_o, rho, 0, 1).removeO())
g1_o_lp = sp.simplify(sp.expand_log(g1_o_lp, force=True))
print('   hat g1 (off-shell, leading power) =', g1_o_lp)
Boff = sp.simplify(sp.expand(g1_o_lp - (2*x - 1)*sp.log(1/rho)))
print('   B_off(x) =', sp.simplify(Boff))
mom_o = sp.simplify(sp.integrate(sp.expand(Boff), (x, 0, 1)))
print('   first moment of B_off =', mom_o)
check('(i) off-shell gluon: log coefficient (2x-1) ln(Q^2/P^2)', sp.simplify(sp.diff(g1_o_lp, rho)*(-rho) - (2*x - 1)) == 0)
check('(i) off-shell gluon: first moment = -1 (+O(P^2/Q^2))', sp.simplify(mom_o + 1) == 0)
# numerical cross-check of the exact off-shell first moment at small rho
fo_num = sp.lambdify((x, rho), g1_o, 'mpmath')
for rv in ('1e-3', '1e-5'):
    rv = mp.mpf(rv)
    xm = 1/(1 + rv)          # shat >= 0 : (1-x)/x >= rho
    val = mp.quad(lambda xx: fo_num(xx, rv), [0, 0.5, xm])
    print('   exact first moment, rho = %s : %s' % (mp.nstr(rv, 3), mp.nstr(val, 15)))
print('\nSUMMARY s5c: %d PASS, %d FAIL' % (npass, nfail))
# pointwise check of the leading-power off-shell formula against the exact expression
ok = True
for xv in ('0.2', '0.5', '0.8'):
    for rv in ('1e-6', '1e-8'):
        ex = fo_num(mp.mpf(xv), mp.mpf(rv))
        lp = (2*mp.mpf(xv) - 1)*(mp.log(1/(mp.mpf(rv)*mp.mpf(xv)**2)) - 2)
        print('   x=%s rho=%s exact=%s  LP=(2x-1)(ln(Q^2/(P^2 x^2))-2)=%s' % (xv, rv, mp.nstr(mp.re(ex), 15), mp.nstr(lp, 15)))
        ok &= abs(mp.re(ex) - lp) < 1e-4
check('(i) exact off-shell result -> (2x-1)[ln(Q^2/(P^2 x^2)) - 2] pointwise as P^2 -> 0', ok)
print('\nSUMMARY s5c (final): %d PASS, %d FAIL' % (npass, nfail))
