"""R-M2 independent check: the reference's (3.3)
   I = int d^4k/(i pi^2) 1/[(-k^2)(-(p1-k)^2)(-(p2+k)^2)],  p1^2 = p2^2 = -m^2,  (p1+p2)^2 = -Q^2,  Q >> m.
(1) Kinematics: real Euclidean vectors need Q <= 2m (triangle inequality); an explicit real Minkowski realization
    with Q >> m exists (so the point is in the all-spacelike region, F > 0, but is not Euclidean-realizable).
(2) Feynman parameters: Q^2 I = int_simplex 1/(t a0 (a1+a2) + a1 a2), t = m^2/Q^2 (d = 4; finite).
    Computed here as a 1D integral after doing the radial integral exactly (independent coding), at 40 digits.
(3) Series of the closed form Phi^(1)(t,t) (Usyukina-Davydychev ladder function) with sympy to O(t^2):
       Q^2 I = L^2 + pi^2/3 + t (2L^2 - 4L - 4 + 2pi^2/3) + O(t^2 L^2),  L = ln(Q^2/m^2),
    and numerical agreement of Phi^(1)(t,t) with the parameter integral.
(4) Reproduce the reference's Table 5 (p.158) values of Q^2 I and of "L^2 + pi^2/3".
Run: python3 -I rm2_sudakov_triangle.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- (1) kinematics
m, Q = 1.0, 30.0
# Minkowski (+,-,-,-): p1 = (E, 0,0, P), p2 = (-E, 0,0, P) ... choose p1, p2 spacelike with p1^2 = p2^2 = -m^2
# take p1 = (a, 0, 0, b), p2 = (-a, 0, 0, b): p^2 = a^2 - b^2 = -m^2, (p1+p2)^2 = -(2b)^2 = -Q^2 -> b = Q/2
b = Q/2; a = np.sqrt(b**2 - m**2)
mink = lambda v: v[0]**2 - v[1]**2 - v[2]**2 - v[3]**2
p1 = np.array([a, 0, 0, b]); p2 = np.array([-a, 0, 0, b])
ok = abs(mink(p1)+m**2) < 1e-9 and abs(mink(p2)+m**2) < 1e-9 and abs(mink(p1+p2)+Q**2) < 1e-9
rep('real Minkowski realization of p1^2=p2^2=-m^2, (p1+p2)^2=-Q^2 with Q=30m', ok, f'p1={p1}, p2={p2}')
# Euclidean: |p1|=|p2|=m, |p1+p2|=Q  =>  Q <= 2m ; Gram determinant check
G = np.array([[m**2, (Q**2-2*m**2)/2], [(Q**2-2*m**2)/2, m**2]])   # Euclidean Gram matrix p_i.p_j (would-be)
rep('Euclidean realization impossible for Q > 2m (Gram matrix not PSD)', np.linalg.eigvalsh(G).min() < 0,
    f'Gram eigenvalues {np.linalg.eigvalsh(G)} (Euclidean vectors require PSD Gram matrix, i.e. Q <= 2m)')

# ---------------------------------------------------------------- (2) parameter integral
def Q2I(t):
    t = mp.mpf(t)
    # a0 = 1-r, a1 = r u, a2 = r(1-u), Jacobian r :  F = r [ t(1-r) + r u(1-u) ]
    # int_0^1 dr 1/(t(1-r) + r c) = ln(c/t)/(c-t),  c = u(1-u)
    def g(u):
        c = u*(1-u)
        d = c - t
        if abs(d) < mp.mpf(10)**(-30):
            return 1/t
        return mp.log(c/t)/d
    u0 = (1 - mp.sqrt(1-4*t))/2
    return 2*mp.quad(g, [0, u0/2, u0, (u0+mp.mpf(1)/2)/2, mp.mpf(1)/2])

def Phi1(x, y):
    x, y = mp.mpf(x), mp.mpf(y)
    lam = mp.sqrt((1-x-y)**2 - 4*x*y)
    rho = 2/(1-x-y+lam)
    return (2*(mp.polylog(2, -rho*x) + mp.polylog(2, -rho*y)) + mp.log(y/x)*mp.log((1+rho*y)/(1+rho*x))
            + mp.log(rho*x)*mp.log(rho*y) + mp.pi**2/3)/lam

worst = 0
for t in ['1e-1', '1e-2', '1e-4', '1e-6', '1e-8', '1e-10', '1e-12']:
    v = Q2I(t); ph = Phi1(t, t)
    worst = max(worst, abs(v-ph)/abs(v))
rep('Q^2 I (parameter integral) = Phi^(1)(t,t) at t=1e-1..1e-12', worst < 1e-25, f'max rel dev {mp.nstr(worst,3)}')
# asymmetric check of the closed form against a 2D parameter integral at a generic point
def Q2I_xy(x, y):
    # F/Q^2 = x a0 a1 + y a0 a2 + a1 a2  (p1^2/p3^2 = x, p2^2/p3^2 = y), simplex
    f = lambda a1, a2: 1/(x*(1-a1-a2)*a1 + y*(1-a1-a2)*a2 + a1*a2)
    return mp.quad(lambda a1: mp.quad(lambda a2: f(a1, a2), [0, 1-a1]), [0, 1])
mp.mp.dps = 15
v = Q2I_xy(mp.mpf('0.03'), mp.mpf('0.11')); ph = Phi1('0.03', '0.11')
rep('closed form Phi^(1)(x,y) matches 2D parameter integral at (0.03,0.11)', abs(v-ph)/abs(v) < 1e-8, f'{mp.nstr(v,12)} vs {mp.nstr(ph,12)}')
mp.mp.dps = 40

# ---------------------------------------------------------------- (3) series expansion
ts, L = sp.symbols('t L', positive=True)
lam = sp.sqrt(1-4*ts); rho = 2/(1-2*ts+lam)
# Phi(t,t) = (4 Li2(-rho t) + ln^2(rho t) + pi^2/3)/lam ; expand with ln t = -L
Li2ser = sum((-rho*ts)**k/k**2 for k in range(1, 5))
lnrho = sp.series(sp.log(rho), ts, 0, 4).removeO()
expr = (4*Li2ser + (-L + lnrho)**2 + sp.pi**2/3)/lam
ser = sp.series(expr, ts, 0, 3).removeO()
c0 = sp.simplify(ser.coeff(ts, 0)); c1 = sp.simplify(sp.expand(ser).coeff(ts, 1)); c2 = sp.simplify(sp.expand(ser).coeff(ts, 2))
print('  coefficient t^0:', sp.expand(c0)); print('  coefficient t^1:', sp.expand(c1)); print('  coefficient t^2:', sp.expand(c2))
rep('t^0 coefficient = L^2 + pi^2/3', sp.simplify(c0 - (L**2 + sp.pi**2/3)) == 0, '')
rep('t^1 coefficient = 2L^2 - 4L - 4 + 2pi^2/3', sp.simplify(c1 - (2*L**2 - 4*L - 4 + 2*sp.pi**2/3)) == 0, '')
rep('t^2 coefficient = 6L^2 - 14L - 11 + 2pi^2 (cross-check with c_regions after L -> -L)', sp.simplify(c2 - (6*L**2 - 14*L - 11 + 2*sp.pi**2)) == 0, '')
# numerical remainder after NLP
print('  t        Q2I                     LP+t*NLP                 (Q2I-LP-tNLP)/(t^2 L^2)')
rat = []
for t in ['1e-2', '1e-4', '1e-6', '1e-8', '1e-10']:
    tt = mp.mpf(t); LL = mp.log(1/tt)
    v = Q2I(t)
    approx = LL**2 + mp.pi**2/3 + tt*(2*LL**2 - 4*LL - 4 + 2*mp.pi**2/3)
    rr = (v - approx)/(tt**2*LL**2); rat.append(rr)
    print(f"  {t:6s} {mp.nstr(v,20):>24} {mp.nstr(approx,20):>24} {mp.nstr(rr,8):>12}")
rep('remainder after NLP is O(t^2 L^2)', all(abs(x) < 10 for x in rat), 'ratio bounded (-> 6, the NNLP L^2 coefficient)')
# wrong-sign variant (+4L) fails
tt = mp.mpf('1e-10'); LL = mp.log(1/tt); v = Q2I('1e-10')
d_minus = v - (LL**2 + mp.pi**2/3); pred_minus = tt*(2*LL**2 - 4*LL - 4 + 2*mp.pi**2/3); pred_plus = tt*(2*LL**2 + 4*LL - 4 + 2*mp.pi**2/3)
rep('at t=1e-10 the difference 9.71e-8 is reproduced by -4L, not +4L', abs(d_minus - pred_minus) < 1e-12 and abs(d_minus - pred_plus) > 1e-8,
    f'diff={mp.nstr(d_minus,6)}, -4L form {mp.nstr(pred_minus,6)}, +4L form {mp.nstr(pred_plus,6)}')

# ---------------------------------------------------------------- (4) reference Table 5 (p.158)
table5 = {'1e-1': (9.107781, 8.591766), '1e-2': (24.770591, 24.497461), '1e-3': (51.077533, 51.006951),
          '1e-4': (88.133782, 88.120238), '1e-6': (194.158529, 194.158200), '1e-8': (342.611353, 342.611347),
          '1e-10': (533.479679, 533.479679)}
ok = True
for t, (ex, lp) in table5.items():
    v = Q2I(t); LL = mp.log(1/mp.mpf(t))
    ok &= abs(v - ex) < 1e-6 and abs(LL**2 + mp.pi**2/3 - lp) < 1e-6
rep('reference Table 5 values reproduced (its App D already contains pi^2/3)', ok, '')

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
