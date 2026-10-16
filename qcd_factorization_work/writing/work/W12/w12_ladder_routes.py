"""W12 (Ch10) -- (1) chain algebra of ex:disall-ladder; (2) counterexamples behind prop:disall-two-routes(b),(c).

(1) Totally ordered regions R2 < R1 < RH, approximators acting on different factors of
    Gamma = H0 * K2 * K1:  T2 on H0 (h = T2 H0), T1 on K2 (k = T1 K2), TH on K1 (l = TH K1); idempotent,
    commuting.  Check C_2, C_1, C_H, r and the expansion of C_H into T^[2] - Hhat^[1] f^[1] - H^[0] f^[2].
(2) (b) real-segment bounds give no Taylor (moment) bounds:  R(w) = lam^a sin(w/lam) is <= lam^a on the real
    axis while its n-th Taylor coefficient is lam^{a-n}/n! (odd n);
    (c) small moments do not give a small discontinuity:  r(x) = sin(Q^2 x) on [0,1] has
    |int_0^1 x^n r dx| <= 2/Q^2 for every n >= 0, hence the dispersion integral
    R(w) = sum_{n even} 4 w^{n-1} int x^{n-2} r is O(1/Q^2) on the whole disc |w| <= rho < 1,
    but sup |r| = 1 (VF-MISC-3).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

print('(1) chain algebra of the two-rung ladder')
h, dh, k, dk, l, dl = sp.symbols('h dh k dk l dl')    # H0 = h + dh, K2 = k + dk, K1 = l + dl
H0, K2, K1 = h + dh, k + dk, l + dl
def T2(expr):   # acts on H0 only: replace H0 -> h  (i.e. dh -> 0 and keep h)
    return sp.expand(expr).subs(dh, 0)
def T1(expr):
    return sp.expand(expr).subs(dk, 0)
def TH(expr):
    return sp.expand(expr).subs(dl, 0)
G = sp.expand(H0 * K2 * K1)
C2 = T2(G)
C1 = T1(G - C2)
CH = TH(G - C2 - C1)
r = sp.expand(G - C2 - C1 - CH)
print('   C_2 = h K2 K1          :', sp.simplify(C2 - h * K2 * K1) == 0)
print('   C_1 = dH0 k K1         :', sp.simplify(C1 - dh * k * K1) == 0)
print('   C_H = dH0 dK2 l        :', sp.simplify(CH - dh * dk * l) == 0)
print('   r   = dH0 dK2 dK1      :', sp.simplify(r - dh * dk * dl) == 0)
print('   r = (1-TH)(1-T1)(1-T2) Gamma :', sp.simplify(r - sp.expand((G - T2(G)) - T1(G - T2(G)) - TH((G - T2(G)) - T1(G - T2(G))))) == 0)
# expansion of C_H with dH0 = H0 - h, dK2 = K2 - k:
CH_exp = sp.expand((H0 - h) * (K2 - k) * l)
print('   C_H = H0 K2 l - h K2 l - H0 k l + h k l :', sp.simplify(CH_exp - (H0 * K2 * l - h * K2 * l - H0 * k * l + h * k * l)) == 0)
print('   single chain term TH(1-T2)Gamma = dH0 K2 l :', sp.simplify(TH(G - T2(G)) - dh * K2 * l) == 0)

print('(2b) real segment vs Taylor coefficients: R(w) = lam^a sin(w/lam)')
for lam in (0.1, 0.01):
    a = 1
    sup_real = lam ** a
    coeffs = [lam ** (a - n) / mp.factorial(n) for n in (1, 3, 5)]
    print('   lam=%g: sup on [-rho,rho] <= %g ; Taylor coefficients n=1,3,5: %s' % (lam, sup_real, [mp.nstr(c, 4) for c in coeffs]))

print('(2c) moments of r(x) = sin(Q^2 x)  (exact recursion, 500-digit arithmetic)')
mp.mp.dps = 500
def moments(a, nmax):
    a = mp.mpf(a)
    I = [(1 - mp.cos(a)) / a]; J = [mp.sin(a) / a]
    for n in range(1, nmax + 1):
        In = -mp.cos(a) / a + n / a * J[n - 1]
        Jn = mp.sin(a) / a - n / a * I[n - 1]
        I.append(In); J.append(Jn)
    return I
for Q2 in (10, 100, 1000):
    I = moments(Q2, 400)
    worst = max(abs(v) * Q2 for v in I)
    rho = mp.mpf('0.9')
    def R(w):
        return sum(4 * w ** (n - 1) * I[n - 2] for n in range(2, 400, 2))
    supR = max(abs(R(rho * mp.e ** (1j * th))) for th in [2 * mp.pi * j / 32 for j in range(32)])
    print('   Q^2=%5d: max_{n<=400} Q^2 |M_n| = %s (<= 2) ;  max_{|w|=0.9} |R(w)| = %s ; sup|r| = 1' % (Q2, mp.nstr(worst, 5), mp.nstr(supR, 4)))
