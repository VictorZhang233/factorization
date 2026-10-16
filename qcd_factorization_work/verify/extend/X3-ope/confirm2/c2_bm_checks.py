#!/usr/bin/env python3
"""
Independent checks for Prop. F.5 (X3-ope_final2.md), written before reading fix1_*.py.

(A) Longitudinal-vertex identity (my alternative route to claim (a) for every covariant gauge):
    with BM damping on every line,  -i[g-(1-xi) pp/(p^2+i eta)]/(p^2+i eta) = D_F + (1-xi) D_F V D_F,
    D_F = -i g/(p^2+i eta), V_{ab} = -i p_a p_b  (a 2-point vertex of dimension = IR degree 4).
    So each general-xi graph at fixed order is a polynomial in (1-xi) whose coefficients are graphs with
    simple-pole (Feynman) lines and extra delta=4 internal vertices: exactly the setting of BM I Thm 1 (+ II.3).
(B) Homogeneity lemma, step 2(iii), at TWO loops (the author checked one loop):
    phi^4 sunset self-energy at p=0, all lines damped (Euclidean mass^2 m2 ~ eta), MS subtraction of the three
    one-loop bubble subdivergences.  Checks: locality (pole coefficients independent of ln(m2/mu2));
    c0(eta,mu,4) = eta * P(ln(mu^2/eta)) with deg P = 2 = h_H; analyticity at D=4; uniform vanishing
    ~ eta^{(1-r h_H)/2} on |D-4|=r.
(C) Step 2(iv): insertions of IR counterterms c0 ~ eta P(ln) into an IR-divergent reduced graph vanish:
    one and two insertions on a soft line (log and power IR divergence), and a double-pole (general-xi type)
    numerator; BM's damping as complex mass m2 = -i eta.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

ok_all = True
def report(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {extra}", flush=True)

# ------------------------------------------------------------------ (A)
p0, p1, p2, p3, eta, xi = sp.symbols('p0 p1 p2 p3 eta xi')
g = sp.diag(1, -1, -1, -1)
pu = sp.Matrix([p0, p1, p2, p3])           # p^mu
pl = g*pu                                   # p_mu
p2s = (pu.T*g*pu)[0]
den = p2s + sp.I*eta
prop_xi = -sp.I*(g.inv() - (1-xi)*pu*pu.T/den)/den          # D^{mu nu}
DF = -sp.I*g.inv()/den
V = -sp.I*pl*pl.T                                            # V_{ab}
rhs = DF + (1-xi)*DF*V*DF
report("(A) general-xi damped propagator = D_F + (1-xi) D_F V D_F, V_ab = -i p_a p_b",
       sp.simplify(prop_xi - rhs) == sp.zeros(4, 4))
print("    V has two gluon fields + two derivatives: canonical dimension = IR degree = 1+1+2 = 4 (BM I II.2/II.3 admissible);"
      " a 1PI subgraph containing V contains both of its lines, and omega is unchanged (-2 per line pair +2 at V).")

# ------------------------------------------------------------------ (B)
mp.mp.dps = 30
def K(D):
    """K(D) = int_{simplex} U^{-D/2}, U = x1x2+x2x3+x3x1, continued to Re(D) < 6 via one subtraction.
       Sector decomposition: K = 6 int_0^1 dv int_0^1 ds s^{1-D/2} h(s,v), h = (1+v+sv)^{-D/2}(1+s+sv)^{D-3}."""
    h = lambda s, v: (1+v+s*v)**(-D/2)*(1+s+s*v)**(D-3)
    a = 2 - D/2                          # int_0^1 s^{a-1} ds = 1/a
    pole = mp.quad(lambda v: (1+v)**(-D/2), [0, 1]) / a
    reg = mp.quad(lambda v, s: s**(a-1)*(h(s, v)-h(0, v)), [0, 1], [0, 1])
    return 6*(pole + reg)

def sunset(D, m2, mu2):    # mu^{2(4-D)} int int d^Dk d^Dl / pi^D  1/((k^2+m2)(l^2+m2)((k+l)^2+m2))
    return mu2**(4-D)*mp.gamma(3-D)*m2**(D-3)*K(D)

def tadpole(D, m2, mu2):   # mu^{4-D} int d^Dl/pi^{D/2} 1/(l^2+m2)
    return mu2**((4-D)/2)*mp.gamma(1-D/2)*m2**(D/2-1)

def Rbar(eps, m2, mu2):   # sunset minus the three one-loop bubble counterterms (pole of bubble = 1/eps, MS)
    D = 4-2*eps
    return sunset(D, m2, mu2) - 3*(1/eps)*tadpole(D, m2, mu2)

def laurent(f, rho=mp.mpf('0.1'), M=32, kmin=-3, kmax=3):
    pts = [rho*mp.expj(2*mp.pi*(j+mp.mpf(1)/2)/M) for j in range(M)]
    vals = [f(e) for e in pts]
    return {k: sum(v*e**(-k) for v, e in zip(vals, pts))/M for k in range(kmin, kmax+1)}

L1 = laurent(lambda e: Rbar(e, mp.mpf(1), mp.mpf(1)))
L2 = laurent(lambda e: Rbar(e, mp.mpf(1), mp.mpf('7.3')))
loc = abs(L1[-2]-L2[-2]) + abs(L1[-1]-L2[-1])
report("(B1) locality: pole part of Rbar (after subdivergence subtraction) is independent of ln(m2/mu2)",
       loc < 1e-12, f"|d a_-2|+|d a_-1| = {mp.nstr(loc, 3)};  a_-3 = {mp.nstr(abs(L1[-3]), 2)}, a_-2 = {mp.nstr(L1[-2].real, 12)}, a_-1 = {mp.nstr(L1[-1].real, 12)}")
a_m2, a_m1 = L1[-2], L1[-1]

def c0(eps, m2, mu2):      # IR counterterm coefficient c0 = -(1-C) Rbar at p=0 (T^1 of a scalar fn of p^2 = value at 0)
    return -(Rbar(eps, m2, mu2) - m2*(a_m2/eps**2 + a_m1/eps))

# D=4 value: c0(m2, mu2, 4) = -[eps^0 coefficient]; expect m2 * quadratic polynomial in ln(mu2/m2)
vals = []
for lam in [mp.mpf(1), mp.mpf(3), mp.mpf(10), mp.mpf(30), mp.mpf(100)]:
    Lx = laurent(lambda e: c0(e, mp.mpf(1), lam), kmin=-2, kmax=0)
    vals.append((mp.log(lam), Lx[0], abs(Lx[-1])+abs(Lx[-2])))
xs = [v[0] for v in vals]; ys = [v[1].real for v in vals]
# fit quadratic through first 3, check 4th, 5th
A = mp.matrix([[1, x, x**2] for x in xs[:3]]); coef = mp.lu_solve(A, mp.matrix(ys[:3]))
resid = max(abs(coef[0]+coef[1]*x+coef[2]*x**2 - y) for x, y in zip(xs[3:], ys[3:]))
poles_left = max(v[2] for v in vals)
report("(B2) c0(eta,mu,4) = eta*P(ln(mu^2/eta)) with deg P = 2 (= h_H), and c0 analytic at D=4",
       resid < 1e-15 and poles_left < 1e-15 and abs(coef[2]) > 1e-3,
       f"P(L) = {mp.nstr(coef[0], 10)} + {mp.nstr(coef[1], 10)} L + {mp.nstr(coef[2], 10)} L^2;  resid {mp.nstr(resid, 2)}; residual poles {mp.nstr(poles_left, 2)}")
# scaling: c0(lambda^2 eta, lambda mu) = lambda^2 c0(eta, mu) at D=4 (joint homogeneity of degree Omega-j = 2)
Lx1 = laurent(lambda e: c0(e, mp.mpf('0.37'), mp.mpf('2.1')), kmin=-2, kmax=0)[0]
Lx2 = laurent(lambda e: c0(e, mp.mpf('0.37')*9, mp.mpf('2.1')*9), kmin=-2, kmax=0)[0]
report("(B3) joint homogeneity at D=4: c0(lam^2 eta, lam^2 mu^2) = lam^2 c0(eta, mu^2)", abs(Lx2-9*Lx1) < 1e-15*abs(Lx1)*1e3,
       f"ratio = {mp.nstr(Lx2/Lx1, 15)}")
# uniform vanishing on |D-4| = r: sup |c0| <= K eta^{(1 - r h_H)/2}, h_H = 2 ; here r = 0.2 (|eps| = 0.1)
r = mp.mpf('0.2'); sups = []
for et in [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]:
    sup = max(abs(c0(r/2*mp.expj(2*mp.pi*j/12), et, mp.mpf(1))) for j in range(12))
    sups.append((et, sup))
slopes = [mp.log(sups[i+1][1]/sups[i][1])/mp.log(sups[i+1][0]/sups[i][0]) for i in range(len(sups)-1)]
expo = (1 - r*2)/2
report("(B4) uniform vanishing on |D-4|=0.2: sup|c0| decays at least like eta^{(1-r h_H)/2} = eta^0.3",
       all(s >= expo - 0.05 for s in slopes) and sups[-1][1] < sups[0][1],
       f"local exponents d ln sup / d ln eta = {[mp.nstr(s, 4) for s in slopes]}")

# ------------------------------------------------------------------ (C)
# Reduced graph: one-loop bubble at Euclidean p^2 = 1 with the IR counterterm vertex c0 inserted k times on the
# line carrying k (soft line).  J_a = int d^4k/pi^2 1/((k^2+m2)^a ((k-p)^2+m2)) = Gamma(a-1)/Gamma(a) int_0^1 x^{a-1}
#   (x(1-x)p^2 + m2)^{1-a} dx  (a >= 2).   Damping: m2 = -i eta.  c0 = eta * P(ln(mu^2/eta)) (from B2, complexified).
BRK = [mp.mpf(0)] + [mp.mpf(10)**(-k) for k in range(15, 2, -3)] + [mp.mpf('0.5')] + [1-mp.mpf(10)**(-k) for k in range(3, 16, 2)] + [mp.mpf(1)]
def J(a, m2, P2=mp.mpf(1)):
    # soft line (k^2+m2)^a carries Feynman weight x^{a-1}; the IR divergence sits at x -> 1
    return mp.gamma(a-1)/mp.gamma(a)*mp.quad(lambda x: x**(a-1)*(x*(1-x)*P2 + m2)**(1-a), BRK)
def Jdp(a, m2, P2=mp.mpf(1)):
    """double-pole (general-xi type) numerator: int d^4k/pi^2 (k.p)^2/(k^2)/((k^2+m2)^a((k-p)^2+m2)) ~ same IR power;
       evaluated via (k.p)^2/k^2 <= p^2: here we use the exact replacement k^mu k^nu/(k^2+m2) in the soft line,
       i.e. numerator (k.p)^2/(k^2+m2): J'_a = int (k.p)^2/((k^2+m2)^{a+1}((k-p)^2+m2))."""
    # Feynman parameters: shift k = l + x p: (k.p)^2 -> (l.p)^2 + x^2 p^4 ; <(l.p)^2> = l^2 p^2/4
    b = a+1
    # weights: (1-x) for (k^2+m2)^b, x for ((k-p)^2+m2); shift k = l + x p; IR divergence at x -> 0
    f = lambda x: (1-x)**(b-1)*(mp.gamma(b-1)/mp.gamma(b)*(x**2*P2**2)*(x*(1-x)*P2+m2)**(1-b)
                            + mp.gamma(b-2)/mp.gamma(b)*(P2/4)*2*(x*(1-x)*P2+m2)**(2-b))
    return mp.quad(f, BRK)
Pc = lambda L: coef[0] + coef[1]*L + coef[2]*L**2
rows = []
for et in [mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7'), mp.mpf('1e-9')]:
    m2 = -1j*et
    c = m2*Pc(mp.log(1/m2))                  # c0 ~ eta P(ln(mu^2/eta)), mu = 1, complex damping
    one = abs(c*J(2, m2)); two = abs(c**2*J(3, m2)); dp = abs(c**2*Jdp(3, m2))
    rows.append((et, one, two, dp, abs(J(2, m2)), abs(J(3, m2))))
for rr in rows:
    print(f"    eta={mp.nstr(rr[0],2)}: |J2|={mp.nstr(rr[4],4)} (log-div)  |J3|={mp.nstr(rr[5],4)} (power-div ~1/eta)"
          f"  |c0 J2|={mp.nstr(rr[1],4)}  |c0^2 J3|={mp.nstr(rr[2],4)}  |c0^2 J3'(double pole)|={mp.nstr(rr[3],4)}")
dec = all(rows[i+1][1] < rows[i][1] and rows[i+1][2] < rows[i][2] and rows[i+1][3] < rows[i][3] for i in range(len(rows)-1))
small = rows[-1][1] < 1e-6 and rows[-1][2] < 1e-6 and rows[-1][3] < 1e-6
report("(C) IR-counterterm insertions vanish as eta->0 although the reduced graphs diverge (log and 1/eta)", dec and small)

print("\nOVERALL:", "PASS" if ok_all else "FAIL")
