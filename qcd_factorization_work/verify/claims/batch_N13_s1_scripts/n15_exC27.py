"""N15 -- reference Ex. C.27: I(q) = int d^4k [Delta(q-k) - Delta(q)] Delta(k)^3, Delta(k) = 1/(k^2+m^2) (Euclidean).
Claim: kappa*I = -kappa*pi^2/(2 q^4) + O(m^2 q^-6 ln q): no log at O(q^-4), m-independent leading coefficient.
Independent route (not used by R5's check1.py): Feynman parameters give
   F(q) = int d^4k Delta(q-k) Delta(k)^3 = (pi^2/2) int_0^1 dx x^2 / (x(1-x) q^2 + m^2)^2,
   int d^4k Delta(k)^3 = pi^2/(2 m^2),
so I = (pi^2/2) [ J(Q) - 1/(m^2 (Q + m^2)) ], J(Q) = int_0^1 x^2/(x(1-x)Q+m^2)^2, Q = q^2.
We (1) check the Feynman-parameter formula against a direct radial x angular 4D integration (mpmath, high precision),
(2) obtain J in closed form, expand at large Q, (3) check numerically at high precision.
Also: (4) the 'F3 lesson' exponent a = beta_R/3 = 1/243 for the (S,S) region of the two-loop planar vertex,
derived from per-line modes (beta_R = 3^{h(R)-h*}, reference Def D.5 as summarised in R6 notes).
Run: python3 -I n15_exC27.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + name + ('   [' + detail + ']' if detail else ''))

# (1) Feynman-parameter formula vs direct 4D integration (m = 1)
m = mp.mpf(1)
def F_feyn(q):
    return mp.pi**2/2 * mp.quad(lambda x: x**2/(x*(1-x)*q**2 + m**2)**2, [0, 1])
def F_direct(q):
    # 4D: d^4k = k^3 dk dOmega_3, Omega_3 = 2 pi^2; angular measure (2/pi) sin^2(th) dth normalised to 1
    def ang(k):
        return mp.quad(lambda th: (2/mp.pi)*mp.sin(th)**2/(q**2 + k**2 - 2*q*k*mp.cos(th) + m**2), [0, mp.pi])
    f = lambda k: 2*mp.pi**2 * k**3 * ang(k)/(k**2 + m**2)**3
    return mp.quad(f, [0, q, 2*q, mp.inf])
for q in [mp.mpf('0.7'), mp.mpf(3)]:
    a, b = F_feyn(q), F_direct(q)
    report(abs(a/b - 1) < mp.mpf('1e-12'), f'Feynman-parameter formula for F(q) vs direct 4D integral, q={q}', f'{mp.nstr(a,15)} vs {mp.nstr(b,15)}')
I3 = mp.quad(lambda k: 2*mp.pi**2*k**3/(k**2+m**2)**3, [0, mp.inf])
report(abs(I3 - mp.pi**2/2) < mp.mpf('1e-30'), 'int d^4k Delta^3 = pi^2/(2m^2)', mp.nstr(I3, 20))
# 4D mean-value property used in the harmonicity argument: <1/(q-k)^2>_angles = 1/max(q,k)^2 (massless)
for (q, k) in [(mp.mpf(2), mp.mpf(7)/10), (mp.mpf(7)/10, mp.mpf(2))]:
    av = mp.quad(lambda th: (2/mp.pi)*mp.sin(th)**2/(q**2 + k**2 - 2*q*k*mp.cos(th)), [0, mp.pi])
    report(abs(av - 1/max(q, k)**2) < mp.mpf('1e-25'), f'4D angular mean of 1/(q-k)^2 = 1/max(q,k)^2 at q={q},k={k}', mp.nstr(av, 20))

# (2) closed form and large-Q expansion (m = 1; restore m by dimensions: I(q;m) = m^-4 I(q/m;1))
x, Q = sp.symbols('x Q', positive=True)
Jexpr = sp.integrate(x**2/(x*(1-x)*Q + 1)**2, (x, 0, 1))
Jexpr = sp.simplify(Jexpr)
print('   J(Q) closed form:', Jexpr)
Iover = sp.pi**2/2*(Jexpr - 1/(Q + 1))
# expansion in 1/Q: substitute Q = 1/u
u = sp.symbols('u', positive=True)
ser = sp.series(sp.simplify(Iover.subs(Q, 1/u)), u, 0, 4).removeO()
ser = sp.expand(sp.simplify(ser))
print('   I(q) large-q expansion (m=1, u = 1/q^2):', ser)
lead = sp.limit(Iover*Q**2, Q, sp.oo)
report(sp.simplify(lead + sp.pi**2/2) == 0, 'q^4 I -> -pi^2/2 (m-independent, no log)', str(lead))
nlp = sp.simplify(sp.limit((Iover*Q**2 + sp.pi**2/2)*Q/sp.log(Q), Q, sp.oo))
nlp2 = sp.simplify(sp.limit((Iover*Q**2 + sp.pi**2/2)*Q - nlp*sp.log(Q), Q, sp.oo))
print(f'   next term: (m^2/q^6) * [ {nlp} * ln(q^2/m^2) + {nlp2} ]')
report(nlp != 0 and sp.limit((Iover*Q**2 + sp.pi**2/2)*Q/sp.log(Q)**2, Q, sp.oo) == 0,
       'first correction is O(m^2 q^-6 ln q) (single log, nonzero coefficient)', f'coefficient of m^2 ln(q^2/m^2)/q^6 = {nlp}')

# (3) high-precision numerics of the exact combination, compared with the two-term expansion
f_exact = sp.lambdify(Q, Iover, 'mpmath')
for qv in [10, 30, 100, 1000, 10**4]:
    Qv = mp.mpf(qv)**2
    val = f_exact(Qv)
    two = -mp.pi**2/2/Qv**2 + (float(nlp)*mp.log(Qv) + float(nlp2))/Qv**3
    print(f'   q={qv:>6}: q^4 I = {mp.nstr(val*Qv**2, 15)};  q^4 I + pi^2/2 = {mp.nstr(val*Qv**2 + mp.pi**2/2, 6)};  two-term rel. err = {mp.nstr((val-two)/val, 3)}')
val = f_exact(mp.mpf(10)**8)
two4 = -mp.pi**2/2 + (float(nlp)*mp.log(mp.mpf(10)**8) + float(nlp2))/mp.mpf(10)**8
report(abs(val*mp.mpf(10)**16 - two4) < mp.mpf('1e-12') and abs(val*mp.mpf(10)**16 + mp.pi**2/2) < mp.mpf('1e-5'), 'q=10^4: q^4 I = -pi^2/2 + (m^2/q^2)(-2pi^2 ln q^2 + 7pi^2/2) to 1e-12', mp.nstr(val*mp.mpf(10)**16, 15))
# direct quadrature of the exact combination (Feynman parameters, mpmath) at q=100 as an extra check
qv = mp.mpf(100)
Jnum = mp.quad(lambda xx: xx**2/(xx*(1-xx)*qv**2 + 1)**2, [0, mp.mpf(1)/qv**2, mp.mpf('0.5'), 1 - 1/qv**2, 1])
Inum = mp.pi**2/2*(Jnum - 1/(qv**2 + 1))
report(abs(Inum/f_exact(qv**2) - 1) < mp.mpf('1e-20'), 'closed form vs quadrature at q=100', f'{mp.nstr(Inum*qv**4, 20)}')

# (4) F3 lesson: per-line modes of the 9 leading regions of the two-loop planar vertex
lines = ['k1', 'k2', 'p1-k2', 'p1-k1-k2', 'p2+k2', 'p2+k1+k2']
modes = {
 ('H','H'):   dict(zip(lines, ['H','H','H','H','H','H'])),
 ('H','C1'):  dict(zip(lines, ['H','C1','C1','H','H','H'])),
 ('H','C2'):  dict(zip(lines, ['H','C2','H','H','C2','H'])),
 ('C1','C1'): dict(zip(lines, ['C1','C1','C1','C1','H','H'])),
 ('C2','C2'): dict(zip(lines, ['C2','C2','H','H','C2','C2'])),
 ('H','S'):   dict(zip(lines, ['H','S','C1','H','C2','H'])),
 ('C1','S'):  dict(zip(lines, ['C1','S','C1','C1','C2','H'])),
 ('C2','S'):  dict(zip(lines, ['C2','S','C1','H','C2','C2'])),
 ('S','S'):   dict(zip(lines, ['S','S','C1','C1','C2','C2'])),
}
le = {('S','S'):1,('S','C1'):1,('S','C2'):1,('S','H'):1,('C1','C1'):1,('C1','H'):1,('C2','C2'):1,('C2','H'):1,('H','H'):1}
def leq(R, Rp):
    return all((modes[R][l], modes[Rp][l]) in le for l in lines)
regs = list(modes)
less = {(a, b) for a in regs for b in regs if a != b and leq(a, b)}
cover = {(a, b) for (a, b) in less if not any((a, c) in less and (c, b) in less for c in regs)}
print('   covering relations (%d):' % len(cover), sorted(cover))
report(len(cover) == 12 and (('C1','C1'), ('H','C1')) in cover, 'Hasse diagram: 12 covering relations incl. (C1,C1) < (H,C1)')
from functools import lru_cache
@lru_cache(None)
def h(R):
    below = [a for (a, b) in less if b == R]
    return 0 if not below else 1 + max(h(a) for a in below)
Rmax = ('H','H')
hstar = 1 + max(h(R) for R in regs if R != Rmax)
beta = {R: sp.Rational(3)**(h(R) - hstar) for R in regs if R != Rmax}
a_SS = beta[('S','S')]/3
print('   h:', {R: h(R) for R in regs}, ' h* =', hstar)
print('   beta_R:', beta)
report(a_SS == sp.Rational(1, 243), 'a_(S,S) = beta_(S,S)/3 = 1/243', str(a_SS))
# one-loop triangle for comparison: regions H, C1, C2, S with S < C_i < H
print('   one-loop triangle: h(S)=0, h(C)=1, h*=2 -> beta_S=1/9, beta_C=1/3, a_S = 1/27, a_C = 1/9')

print(f'\nSUMMARY: {npass}/{npass+nfail} PASS')
