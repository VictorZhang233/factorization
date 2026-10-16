"""Review r3_1 (X2-subtraction, round 3) -- independent re-computation of numerical claims of the fix-round-2 report.
(1) Thm 4.3 / Num-2loop: exact two-loop planar off-shell vertex from the Usyukina-Davydychev closed form
    Phi2(t,t) = -(6/lam)[Li4(-1/(rho t)) - Li4(-rho t)], t = m2/Q^2, lam = sqrt(1-4t), rho = 2/(1-2t+lam);
    units Qt = 1 (Q^2 = (1+m2)^2), int Gamma = Phi2/Q^4, P(L) = L^4/4 + pi^2 L^2/2 + 7 pi^4/60,
    int r = int Gamma - P, NLP formula -m2 (L^4/2 + pi^2 L^2 + 12 + 7 pi^4/30).
(2) Thm 3.5: one-loop int r in Qt and Q units.
(3) Prop 5.1'(d): c1(x) = 4 int_0^1 xi^(1/2) (1-xi)^(3/2) / (1-xi/x)^2.
(4) Prop 3.1': closed forms of the four triangle Collins terms at the two parameter points of PART D, and
    the eps -> 0 limit of their sum (must be Lt^2 + pi^2/3).
(5) Prop 3.14: x0, x0', c, residues.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40

print("(1) two-loop planar vertex (Qt = 1)")
def phi(Lp, t):
    lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    if Lp == 1:
        return -(2/lam)*(mp.polylog(2, -1/(rho*t)) - mp.polylog(2, -rho*t))
    return -(6/lam)*(mp.polylog(4, -1/(rho*t)) - mp.polylog(4, -rho*t))
for m2 in [mp.mpf('0.04'), mp.mpf('0.01'), mp.mpf('0.0025'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5'), mp.mpf('1e-6')]:
    Q2 = (1 + m2)**2; t = m2/Q2
    L = mp.log(1/m2)
    IG = phi(2, t)/Q2**2
    IG_closed = (1 + m2)*(12*mp.polylog(4, -m2) + L**4/4 + mp.pi**2*L**2/2 + 7*mp.pi**4/60)/((1 - m2)*(1 + m2)**4)
    P = L**4/4 + mp.pi**2*L**2/2 + 7*mp.pi**4/60
    r = IG - P
    nlp = -m2*(L**4/2 + mp.pi**2*L**2 + 12 + 7*mp.pi**4/30)
    print(f"   m2={mp.nstr(m2,3):>8}: int Gamma = {mp.nstr(IG, 10):>14} (closed form rel.dev {mp.nstr(abs(IG/IG_closed-1),2)})"
          f"   int r = {mp.nstr(r, 8):>14}   ratio to NLP = {mp.nstr(r/nlp, 8)}")

print("\n(2) one-loop int r (Thm 3.5)")
for m2 in [mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]:
    Q2 = (1 + m2)**2; t = m2/Q2; L = mp.log(1/m2)
    IG = phi(1, t)/Q2
    r = IG - (L**2 + mp.pi**2/3)
    r_closed = (4*mp.polylog(2, -m2) + (L**2 + mp.pi**2/3)*m2**2)/(1 - m2**2)
    # Q units: quantity Q^2 * int r expressed through mQ2 = m2/Q2 and LQ = ln(Q2/m2)
    mQ = m2/Q2; LQ = mp.log(Q2/m2)
    lhsQ = r*Q2                       # dimensionless Q^2 int r  (int r has dimension 1/Qt^2 = 1/Q^2 * Q^2/Qt^2)
    expQ = -4*mQ + mQ**2*(LQ**2 - 15 + mp.pi**2/3)
    print(f"   m2={mp.nstr(m2,2)}: int r = {mp.nstr(r, 12)} (closed rel.dev {mp.nstr(abs(r/r_closed-1),2)});"
          f"  Q-unit residual (Q^2 int r - expansion)/(mQ^3 LQ^2) = {mp.nstr((lhsQ - expQ)/(mQ**3*LQ**2), 6)}")

print("\n(3) c1(x)")
for xv in [2, mp.mpf('1.3'), 5]:
    c1 = 4*mp.quad(lambda xi: mp.sqrt(xi)*(1 - xi)**mp.mpf(1.5)/(1 - xi/xv)**2, [0, 1])
    print(f"   c1({xv}) = {mp.nstr(c1, 10)}")

print("\n(4) triangle Collins terms, closed forms (mu = 1)")
def closed(P, Pp, m2, e):
    Qt2 = 2*P*Pp
    CS = mp.gamma(e)**2*mp.gamma(1 - e)*(Qt2/m2**2)**e/Qt2
    CC = mp.gamma(e)*mp.gamma(-e)*mp.gamma(1 - e)/mp.gamma(1 - 2*e)*m2**(-e)/Qt2
    CH = mp.gamma(1 + e)*mp.gamma(1 - e)**2/(e**2*mp.gamma(1 - 2*e))*Qt2**(-e)/Qt2
    return CS, CC, CH
for pt in [(mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1'), mp.mpf('0.3')), (1/mp.sqrt(2), 1/mp.sqrt(2), mp.mpf('0.01'), mp.mpf('0.2'))]:
    CS, CC, CH = closed(*pt)
    print(f"   P,P',m2,eps = {[mp.nstr(v,4) for v in pt]}: C_S = {mp.nstr(CS, 20)}, C_C1 = C_C2 = {mp.nstr(CC, 20)}, C_H = {mp.nstr(CH, 20)}")
for m2 in [mp.mpf('1e-2'), mp.mpf('1e-4')]:
    P = Pp = 1/mp.sqrt(2)
    Lt = mp.log(1/m2)
    vals = []
    for e in [mp.mpf('1e-6'), mp.mpf('1e-8'), mp.mpf('1e-10')]:
        CS, CC, CH = closed(P, Pp, m2, e)
        vals.append(CS + 2*CC + CH)
    print(f"   m2={mp.nstr(m2,2)}: sum C_R at eps=1e-6,1e-8,1e-10: {[mp.nstr(v,14) for v in vals]};  Lt^2+pi^2/3 = {mp.nstr(Lt**2 + mp.pi**2/3, 14)}")

print("\n(5) Prop 3.14 numbers (M2 = 1e-3, Y = 3, kappa = 0.01, P = P' = 1/sqrt2)")
M2 = mp.mpf('1e-3'); Y = 3; kap = mp.mpf('0.01'); P = Pp = 1/mp.sqrt(2)
S = M2 + kap; e = mp.e**(-2*Y)
x0 = mp.sqrt(S/(2*e)); x0p = mp.sqrt(S*e/2)
c = 1/(2*P*Pp*S*(1 - e**2)); res = -1/(4*P*Pp*S*(1 - e**2))
print(f"   x0 = {mp.nstr(x0, 12)}, x0' = {mp.nstr(x0p, 12)}, c = {mp.nstr(c, 12)}, residue at x0 and -x0' = {mp.nstr(res, 12)}")
# direct check: x*rho at x = +-1e-9 from the closed forms (eta -> 0)
rho_pos = lambda x: 1/(P*(S - 2*e*x**2)*(2*Pp*x*(1 - e**2)))
rho_neg = lambda x: 1/(Pp*(S - 2*x**2/e)*(2*P*x*(1 - e**2)))
print(f"   x*rho(x=+1e-9) = {mp.nstr(1e-9*rho_pos(mp.mpf('1e-9')), 12)},  x*rho(x=-1e-9) = {mp.nstr(-1e-9*rho_neg(mp.mpf('-1e-9')), 12)}")
# residues of the x>0 and x<0 forms at x0 and -x0'
h = mp.mpf('1e-12')
print(f"   numerical residue at x0: {mp.nstr(h*rho_pos(x0 + h), 10)};  at -x0': {mp.nstr(h*rho_neg(-x0p + h), 10)}")
