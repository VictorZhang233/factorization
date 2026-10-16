"""X2 fix round 2 / r2_triangle_identification.py -- EXACT identification of the fibered and covariant values of the
one-loop triangle's Collins terms (replaces the use of Lemma 2.7 for C_C1, C_C2, C_H; reviews r2_1 (ID), r2_2 F3).

Conventions (M1): x = k+, kap = |k_T|^2, u = x/P, Qt^2 = 2PP', a = m2/P', w = 2x + a, e2 = m2 + 2P'x, h2 = 2P'x.
Fibered value  I^fib_F = (mu^{2eps}/Gamma(1-eps)) int dx dkap kap^{-eps} rho_F(x,kap)     (X2-Prop3.1 densities)
Covariant value I^cov_F = mu^{2eps} int d^dk/(i pi^{d/2}) F, DEFINED by the Feynman/Schwinger-parameter representation
of the WHOLE integrand F (numerator included), d = 4 - 2eps.

PART A (fibered side, analytic).  kappa-integrals (0<eps<1, alpha,beta>0):
   K1(al)    = int_0^oo dk k^-eps/(k+al)          = g al^-eps,                          g = Gamma(eps)Gamma(1-eps)
   K2(al,be) = int_0^oo dk k^-eps/((k+al)(k+be)) = g (al^-eps - be^-eps)/(be - al)    (partial fractions)
 Each density part has the form c/((k+al)(k+be)) or c/(k+al); after the kappa-integral the x-integral is one of
   J0 = int_0^1 du u^{-1-eps}[(1-u)^{-eps} - 1] = B(-eps,1-eps) + 1/eps   (converges for eps<1; = analytic continuation)
   J1 = int_1^oo du u^{-1-eps} = 1/eps ,   J2 = int_0^oo ds s^{-eps}/(1+s) = g.
PART B (covariant side, analytic): whole-integrand parametrization; all parameter integrals converge for 0<eps<1.
PART C: symbolic equality of A and B (gammasimp).  PART D: independent numerics (direct 2D fibered quadrature without
the kappa formula; direct 3D parametric quadrature without the lambda formulas).  PART E: hypothesis (I2) of Lemma 2.7
fails for the composite C_C1 (its two residue pieces are separately non-integrable).  PART F: identification of Gamma
itself at eps = 1/10 and 3/10 (fibered 2D quadrature vs covariant Feynman-parameter 2D quadrature; numerical only)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

eps = sp.Symbol('epsilon', positive=True)
x, k, u, s, P, Pp, m2, lam1, lam2, X = sp.symbols('x kappa u s P Pp m2 lambda1 lambda2 X', positive=True)
g = sp.gamma(eps)*sp.gamma(1 - eps)
Qt2 = 2*P*Pp
a = m2/Pp

def kappa_reduce(rho):
    """rho rational in kappa with simple linear factors: return the exact kappa-integral as an expression in x,
    using K1/K2.  Returns (reduced, (c, alpha, beta))."""
    num, den = sp.fraction(sp.together(rho))
    dpoly = sp.Poly(sp.expand(den), k)
    roots = sp.roots(dpoly)                      # roots in kappa:  kappa = -alpha
    lead = dpoly.LC()
    assert sp.Poly(sp.expand(num), k).degree() == 0, "numerator must be kappa-independent"
    c = sp.simplify(num/lead)
    als = []
    for r, mult in roots.items():
        assert mult == 1
        als.append(sp.simplify(-r))
    if len(als) == 1:
        return sp.simplify(c*g*als[0]**(-eps)), (c, als[0], None)
    al, be = als
    return sp.simplify(c*g*(al**(-eps) - be**(-eps))/(be - al)), (c, al, be)

print("PART A: fibered values (kappa-integral exactly, then Beta-type x-integrals)")
A_ = x*m2*(1 - x/P) + P*k; B_ = x*m2 + P*k; e2 = m2 + 2*Pp*x; h2 = 2*Pp*x; w = 2*x + a
dens = {
 'C_S  (x>0)':       1/(B_*e2),
 'C_C1 (0<x<P)':     x*m2/(Qt2*A_*B_),
 'C_C1 (x>P)':       -1/(h2*B_),
 'C_C2 (x>0)':       -1/(P*e2*(e2 + k)),
 'C_C2 (sliver)':    (a*u)/(P*((a - a*u)*Pp*a*u + a*k)*(Pp*a*u + k))*a/2,     # in u: x = a(u-1)/2, w = a u, dx = (a/2) du
 'C_H  (0<x<P)':     -x/(P*(h2 + k)*(h2*(P - x) + P*k)),
 'C_H  (x>P)':       1/(P*(h2 + k)*h2),
}
# claimed reduced integrands after the kappa-integral (in the natural variable), and the resulting x-integrals
claims = {
 'C_S  (x>0)':    (lambda R: R.subs(x, m2*s/(2*Pp))*m2/(2*Pp),  g/Qt2*(m2**2/Qt2)**(-eps)*s**(-eps)/(1 + s)),
 'C_C1 (0<x<P)':  (lambda R: R.subs(x, P*u)*P,                  g/Qt2*(m2)**(-eps)*u**(-1 - eps)*((1 - u)**(-eps) - 1)),
 'C_C1 (x>P)':    (lambda R: R.subs(x, P*u)*P,                  -g/Qt2*(m2)**(-eps)*u**(-1 - eps)),
 'C_C2 (x>0)':    (lambda R: R,                                 -g/P*(m2 + 2*Pp*x)**(-1 - eps)),
 'C_C2 (sliver)': (lambda R: R,                                 g/Qt2*(m2)**(-eps)*u**(-1 - eps)*((1 - u)**(-eps) - 1)),
 'C_H  (0<x<P)':  (lambda R: R.subs(x, P*u)*P,                  -g*Qt2**(-1 - eps)*u**(-1 - eps)*((1 - u)**(-eps) - 1)),
 'C_H  (x>P)':    (lambda R: R.subs(x, P*u)*P,                  g*Qt2**(-1 - eps)*u**(-1 - eps)),
}
for nm, rho in dens.items():
    R, (c, al, be) = kappa_reduce(rho)
    tr, claim = claims[nm]
    lhs = sp.expand_power_base(sp.powsimp(sp.expand(tr(R)), force=True), force=True)
    diff = sp.simplify(sp.expand_power_base(sp.powsimp(lhs - claim, force=True), force=True))
    if diff != 0:   # numeric spot check with random values if simplify is inconclusive
        import random
        vals = {P: sp.Rational(7, 10), Pp: sp.Rational(13, 10), m2: sp.Rational(1, 10), eps: sp.Rational(3, 10),
                u: sp.Rational(37, 100), s: sp.Rational(29, 10), x: sp.Rational(11, 10)}
        dnum = sp.N((lhs - claim).subs(vals), 30)
        status = f"spot check |diff| = {mp.nstr(abs(complex(dnum)), 3)}"
    else:
        status = "symbolically equal"
    print(f"   {nm:15s} alpha = {sp.simplify(al)},  beta = {sp.simplify(be) if be is not None else '-'}   reduced integrand: {status}")
# the x-integrals (natural variable ranges): C_S s in (0,oo); C_C1 u in (0,1) and (1,oo); C_C2 x in (0,oo), sliver u in (0,1)
J0 = sp.beta(-eps, 1 - eps) + 1/eps          # int_0^1 u^{-1-eps}[(1-u)^{-eps}-1] du
J1 = 1/eps                                    # int_1^oo u^{-1-eps} du
J2 = g                                        # int_0^oo s^{-eps}/(1+s) ds
norm = 1/sp.gamma(1 - eps)                    # mu = 1
fib = {
 'C_S':  norm*g/Qt2*(m2**2/Qt2)**(-eps)*J2,
 'C_C1': norm*(g/Qt2*m2**(-eps)*J0 - g/Qt2*m2**(-eps)*J1),
 'C_C2': norm*(-g/P*m2**(-eps)/(2*Pp*eps) + g/Qt2*m2**(-eps)*J0),
 'C_H':  norm*(-g*Qt2**(-1 - eps)*J0 + g*Qt2**(-1 - eps)*J1),
}
# numerical confirmation of J0, J1 (by quadrature) at several eps, 30 digits
mp.mp.dps = 40
for ev in ['0.05', '0.1', '0.3', '0.7']:
    e_ = mp.mpf(ev)
    q0 = (mp.quad(lambda t: t**(-1 - e_)*((1 - t)**(-e_) - 1), [0, mp.mpf(1)/2])      # t = 1 - v on (1/2,1); v = w^(1/(1-eps)) removes v^-eps
          + mp.quad(lambda w_: (1 - w_**(1/(1 - e_)))**(-1 - e_)/(1 - e_), [0, (mp.mpf(1)/2)**(1 - e_)])
          - mp.quad(lambda v: (1 - v)**(-1 - e_), [0, mp.mpf(1)/2]))
    print(f"   J0(eps={ev}): quadrature {mp.nstr(q0, 25)}   B(-eps,1-eps)+1/eps {mp.nstr(mp.beta(-e_, 1 - e_) + 1/e_, 25)}")

print("\nPART B: covariant values from the whole-integrand parametric representation")
# light-cone dot product, vectors as (plus, minus); transverse parts vanish for all external vectors here
dot = lambda p, q: p[0]*q[1] + p[1]*q[0]
p1 = (P, -m2/(2*P)); p2 = (m2/(2*Pp), -Pp); n1 = (P, 0); n2 = (0, Pp)
lin = lambda c1, v1, c2, v2: (c1*v1[0] + c2*v2[0], c1*v1[1] + c2*v2[1])
def add(*vs):
    return (sum(v[0] for v in vs), sum(v[1] for v in vs))
xx = sp.Symbol('x_F', positive=True)
# C_S = 1/(Dg e1 e2):  1/(A B1 B2) = 2 int dl1 dl2 (A + l1 B1 + l2 B2)^-3 ;  V = l1 n1 + l2 n2, Delta = V^2 + m2(l1+l2)
V = add(lin(lam1, n1, 0, n1), lin(lam2, n2, 0, n2))
Delta_S = sp.expand(dot(V, V) + m2*(lam1 + lam2))
print("   C_S : Delta =", sp.factor(Delta_S))
# l-integral: 2 * Gamma(3-d/2)/Gamma(3) Delta^{d/2-3} = Gamma(1+eps) Delta^{-1-eps}
# int_0^oo dl2 (c + K l2)^{-1-eps} = c^{-eps}/(eps K)  with c = m2 l1, K = Qt2 l1 + m2;  then
# int_0^oo dl1 (m2 l1)^{-eps}/(eps (Qt2 l1 + m2)) = m2^{-eps} (m2/Qt2)^{-eps} g /(eps Qt2)
assert sp.simplify(sp.expand(Delta_S) - sp.expand((m2*lam1) + lam2*(Qt2*lam1 + m2))) == 0
IS = sp.gamma(1 + eps)*m2**(-eps)*(m2/Qt2)**(-eps)*g/(eps*Qt2)
print("   C_S : int =", sp.gammasimp(sp.simplify(IS)))
# C_C1 = (e1 - t1)/(Dg h2 t1 e1) with e1 - t1 = (m2/P) k+ + k^2 ;  1/(Dg t1 h2 e1) = 6 int dx dl1 dl2 [x t1 + (1-x) Dg + l1 h2 + l2 e1]^-4
V = add(lin(xx, p1, 0, p1), lin(lam1, n2, lam2, n1))
Delta_C1 = sp.expand(dot(V, V) + m2*(xx + lam2))
print("   C_C1: Delta =", sp.factor(Delta_C1))
# numerator after k = l + V: (m2/P)(l+ + V+) + l^2 + 2 l.V + V^2  -> even part  l^2 + [ (m2/P) V+ + V^2 ]
Nconst = sp.expand(m2/P*V[0] + dot(V, V))
print("   C_C1: even part of numerator = l^2 + (", sp.factor(Nconst), "),  equals l^2 + Delta:", sp.simplify(Nconst - Delta_C1) == 0)
# l-integrals (Euclidean, -l^2 = lE^2): int l^2/(-l^2+D)^4 = -(d/2)Gamma(3-d/2)/6 D^{d/2-3};  int 1/(-l^2+D)^4 = Gamma(4-d/2)/6 D^{d/2-4}
dh = 2 - eps
lint = lambda D: -dh*sp.gamma(3 - dh)/6*D**(dh - 3) + D*sp.gamma(4 - dh)/6*D**(dh - 4)
red = sp.gammasimp(sp.simplify(6*lint(sp.Symbol('D', positive=True))/sp.Symbol('D', positive=True)**(-1 - eps)))
print("   C_C1: 6*int d^dl (l^2+D)/(-l^2+D)^4 = D^{-1-eps} *", red)
fC1 = red*((xx + lam2)*(m2*(1 - xx) + Qt2*lam1))**(-1 - eps)
assert sp.simplify(Delta_C1 - (xx + lam2)*(m2*(1 - xx) + Qt2*lam1)) == 0
# lambda-integrals: x^{-eps}/eps and (m2(1-x))^{-eps}/(eps Qt2);  x-integral: B(1-eps,1-eps)
IC1 = red*m2**(-eps)/(eps**2*Qt2)*sp.beta(1 - eps, 1 - eps)
print("   C_C1: int =", sp.gammasimp(sp.simplify(IC1)))
# C_H = Dg/(t1^ h1 t2^ h2), t1^ = -k^2 + 2 n1.k, t2^ = -k^2 + 2 n2.k (massless on-shell legs p1^ = n1, p2^ = -n2)
V = add(lin(xx + lam1, n1, 0, n1), lin(1 - xx + lam2, n2, 0, n2))
Delta_H = sp.expand(dot(V, V))
print("   C_H : Delta = V^2 =", sp.factor(Delta_H))
linth = lambda D: dh*sp.gamma(3 - dh)/6*D**(dh - 3) - D*sp.gamma(4 - dh)/6*D**(dh - 4)     # numerator -l^2 - V^2, V^2 = D
redH = sp.gammasimp(sp.simplify(6*linth(sp.Symbol('D', positive=True))/sp.Symbol('D', positive=True)**(-1 - eps)))
print("   C_H : 6*int d^dl (-l^2-D)/(-l^2+D)^4 = D^{-1-eps} *", redH)
assert sp.simplify(Delta_H - Qt2*(xx + lam1)*(1 - xx + lam2)) == 0
# lambda-integrals: x^{-eps}/eps and (1-x)^{-eps}/eps;  x-integral: B(1-eps,1-eps)
IH = redH*Qt2**(-1 - eps)/eps**2*sp.beta(1 - eps, 1 - eps)
print("   C_H : int =", sp.gammasimp(sp.simplify(IH)))
cov = {'C_S': IS, 'C_C1': IC1, 'C_C2': IC1.subs({P: Pp, Pp: P}, simultaneous=True), 'C_H': IH}
claimed = {'C_S': sp.gamma(eps)**2*sp.gamma(1 - eps)*(Qt2/m2**2)**eps/Qt2,
           'C_C1': sp.gamma(eps)*sp.gamma(-eps)*sp.gamma(1 - eps)/sp.gamma(1 - 2*eps)*m2**(-eps)/Qt2,
           'C_C2': sp.gamma(eps)*sp.gamma(-eps)*sp.gamma(1 - eps)/sp.gamma(1 - 2*eps)*m2**(-eps)/Qt2,
           'C_H': sp.gamma(1 + eps)*sp.gamma(1 - eps)**2/(eps**2*sp.gamma(1 - 2*eps))*Qt2**(-eps)/Qt2}

print("\nPART C: fibered (A) = covariant (B) = closed form, symbolically")
for nm in ['C_S', 'C_C1', 'C_C2', 'C_H']:
    def chk(e1, e2):
        d = sp.gammasimp(sp.simplify(sp.expand_power_base(sp.powsimp(e1 - e2, force=True), force=True)))
        if d == 0:
            return 'exact'
        vals = {P: sp.Rational(4, 5), Pp: sp.Rational(13, 10), m2: sp.Rational(1, 10), eps: sp.Rational(3, 10)}
        return f'numeric |diff| = {mp.nstr(abs(complex(sp.N((e1 - e2).subs(vals), 40))), 3)}'
    print(f"   {nm:5s}: fibered - covariant: {chk(fib[nm], cov[nm]):>28};   covariant - claimed: {chk(cov[nm], claimed[nm])}")
    print(f"          covariant closed form = {sp.gammasimp(sp.simplify(sp.expand_func(cov[nm])))}")

print("\nPART D: independent numerics (no kappa formula; no lambda formulas)")
mp.mp.dps = 20
def fib_direct(nm, Pv, Ppv, m2v, ev):
    Qv = 2*Pv*Ppv; av = m2v/Ppv
    def rho(xv, kv):
        if nm == 'C_S':
            return 1/((xv*m2v + Pv*kv)*(m2v + 2*Ppv*xv)) if xv > 0 else 0
        if nm == 'C_C1':
            if 0 < xv < Pv:
                return xv*m2v/(Qv*(xv*m2v*(1 - xv/Pv) + Pv*kv)*(xv*m2v + Pv*kv))
            return -1/((2*Ppv*xv)*(xv*m2v + Pv*kv)) if xv >= Pv else 0
        if nm == 'C_C2':
            if xv > 0:
                e = m2v + 2*Ppv*xv; return -1/(Pv*e*(e + kv))
            wv = 2*xv + av; return wv/(Pv*((av - wv)*Ppv*wv + av*kv)*(Ppv*wv + kv))
        if nm == 'C_H':
            hv = 2*Ppv*xv
            if 0 < xv < Pv:
                return -xv/(Pv*(hv + kv)*(hv*(Pv - xv) + Pv*kv))
            return 1/(Pv*(hv + kv)*hv)
    fk = lambda xv: mp.quad(lambda lk: rho(xv, mp.e**lk)*mp.e**(lk*(1 - ev)), [-mp.inf, mp.log(m2v) - 10, mp.log(m2v), 0, 10, mp.inf])
    tot = mp.quad(lambda lx: fk(mp.e**lx)*mp.e**lx, [-mp.inf, mp.log(m2v) - 10, mp.log(m2v), mp.log(Pv)]) \
        + mp.quad(lambda lx: fk(mp.e**lx)*mp.e**lx, [mp.log(Pv), mp.log(Pv) + 5, mp.inf])
    if nm == 'C_C2':
        tot += mp.quad(fk, [-av/2, -av/4, 0])
    return tot/mp.gamma(1 - ev)
def cov_direct(nm, Pv, Ppv, m2v, ev):
    """direct quadrature of the parametric integrals BEFORE the lambda-integrations (scipy, double precision)"""
    import numpy as np
    from scipy import integrate
    Pv, Ppv, m2v, ev = float(Pv), float(Ppv), float(m2v), float(ev)
    Qv = 2*Pv*Ppv; G1 = float(mp.gamma(1 + ev))
    if nm == 'C_S':
        f = lambda t2, t1: G1*(np.exp(t1 + t2)*Qv + m2v*(np.exp(t1) + np.exp(t2)))**(-1 - ev)*np.exp(t1 + t2)
        return integrate.nquad(f, [[-60, 40], [-60, 40]], opts={'limit': 200, 'epsrel': 1e-11, 'epsabs': 0})[0]
    if nm == 'C_C1':
        f = lambda t2, t1, xf: G1*(2*ev - 1)*((xf + np.exp(t2))*(m2v*(1 - xf) + Qv*np.exp(t1)))**(-1 - ev)*np.exp(t1 + t2)
    if nm == 'C_H':
        f = lambda t2, t1, xf: G1*(1 - 2*ev)*((xf + np.exp(t1))*(1 - xf + np.exp(t2))*Qv)**(-1 - ev)*np.exp(t1 + t2)
    return integrate.nquad(f, [[-60, 40], [-60, 40], [0, 1]], opts={'limit': 200, 'epsrel': 1e-10, 'epsabs': 0})[0]
for (Pv, Ppv, m2v, ev) in [(mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1'), mp.mpf('0.3')),
                          (1/mp.sqrt(2), 1/mp.sqrt(2), mp.mpf('0.01'), mp.mpf('0.2'))]:
    print(f"   P={mp.nstr(Pv,4)} P'={mp.nstr(Ppv,4)} m2={mp.nstr(m2v,3)} eps={mp.nstr(ev,3)}")
    sub = {P: Pv, Pp: Ppv, m2: m2v, eps: ev}
    for nm in ['C_S', 'C_C1', 'C_C2', 'C_H']:
        cf = mp.mpf(sp.N(claimed[nm].subs(sub), 35))
        fd = fib_direct(nm, Pv, Ppv, m2v, ev)
        line = f"      {nm:5s}: closed form {mp.nstr(cf, 20):>26}   fibered 2D quadrature rel.dev {mp.nstr(abs(fd/cf - 1), 3):>9}"
        if nm != 'C_C2' and Pv == mp.mpf('0.8'):
            cd = cov_direct(nm, Pv, Ppv, m2v, ev)
            line += f"   covariant parametric quadrature rel.dev {abs(cd/float(cf) - 1):.1e}"
        print(line, flush=True)

print("\nPART E: Lemma 2.7 hypothesis (I2) fails for C_C1 = T1 + T2 (sum of moduli of its two residue pieces)")
mp.mp.dps = 20
Pv = Ppv = 1/mp.sqrt(2); m2v = mp.mpf('0.01'); ev = mp.mpf('0.1'); gv = mp.gamma(ev)*mp.gamma(1 - ev)
K1 = lambda al: gv*al**(-ev)
for d in ['1e-4', '1e-8', '1e-12', '1e-16']:
    d = mp.mpf(d)
    G = mp.quad(lambda xv: (K1(xv*m2v*(1 - xv/Pv)/Pv) + K1(xv*m2v/Pv))/Pv/(2*Ppv*xv), [d, 10*d, m2v, Pv/2, Pv])
    print(f"   int_delta^P dx int dkap kap^-eps (|1/(A h2)| + |1/(B h2)|), delta={mp.nstr(d,2):>6}: {mp.nstr(G, 8)}")
print("   -> grows like delta^-eps/eps: G is not integrable, (I2) fails; the identification above is by direct computation.")

print("\nPART F: identification of Gamma itself (numerical; Lemma 2.7 needs (I1), not verified)")
mp.mp.dps = 20
def gamma_fib(Pv, Ppv, m2v, ev):
    Qv = 2*Pv*Ppv; av = m2v/Ppv
    def rho(xv, kv):
        if 0 < xv < Pv:
            uu = xv/Pv; A = xv*m2v*(1 - uu) + Pv*kv; e = m2v + 2*Ppv*xv
            D2 = e*(1 + m2v/Qv + kv/(Qv*(1 - uu))) + kv
            return 1/(A*D2)
        if -av/2 < xv <= 0:
            wv = 2*xv + av; km = Ppv + kv/wv
            Dg = kv - 2*xv*km; D1 = kv + 2*(Pv - xv)*(km + m2v/(2*Pv))
            return 2/(wv*Dg*D1)
        return 0
    fk = lambda xv: mp.quad(lambda lk: rho(xv, mp.e**lk)*mp.e**(lk*(1 - ev)), [-mp.inf, mp.log(m2v) - 8, mp.log(m2v), 0, 8, mp.inf])
    tot = mp.quad(lambda lx: fk(mp.e**lx)*mp.e**lx, [-mp.inf, mp.log(m2v) - 8, mp.log(m2v), mp.log(Pv) - 1, mp.log(Pv)])
    tot += mp.quad(fk, [-av/2, -av/4, 0])
    return tot/mp.gamma(1 - ev)
def gamma_cov(Pv, Ppv, m2v, ev):
    Qt2v = 2*Pv*Ppv; Q2 = (Qt2v + m2v)**2/Qt2v
    f = lambda x1, x2: mp.gamma(1 + ev)*((1 - x1 - x2)*(x1 + x2)*m2v + x1*x2*Q2)**(-1 - ev)
    return mp.quad(lambda x1: mp.quad(lambda x2: f(x1, x2), [0, (1 - x1)/2, 1 - x1]), [0, mp.mpf(1)/2, 1])
for (Pv, Ppv, m2v, ev) in [(mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1'), mp.mpf('0.3')),
                          (1/mp.sqrt(2), 1/mp.sqrt(2), mp.mpf('0.01'), mp.mpf('0.1'))]:
    fb = gamma_fib(Pv, Ppv, m2v, ev); cv = gamma_cov(Pv, Ppv, m2v, ev)
    print(f"   P={mp.nstr(Pv,4)} P'={mp.nstr(Ppv,4)} m2={mp.nstr(m2v,3)} eps={mp.nstr(ev,3)}: fibered {mp.nstr(fb, 15)}  covariant {mp.nstr(cv, 15)}  rel.dev {mp.nstr(abs(fb/cv - 1), 3)}", flush=True)
