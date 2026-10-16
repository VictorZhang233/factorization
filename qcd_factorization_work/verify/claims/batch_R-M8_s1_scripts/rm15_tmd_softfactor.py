# R-M15: which soft-factor arguments make the product of unsubtracted TMDs equal to f_A f_B of Collins' (10.4)?
# One loop, b-space, logs of the factors (products -> sums).  Exact one-loop rapidity dependence of the soft factor
# with non-light-like Wilson lines (Collins 2011; research/c_tmd/scripts/soft_factor.py re-derives it):
#     ln S(y1, y2) = kappa * [ Y coth Y - sigma ],   Y = y1 - y2,   kappa = -(alpha_s C_F/pi) ln(mu^2 b^2/b0^2)
# Unsubtracted TMDs: ln f_A^unsub(y_PA - y_B) = F_A + kappa*(y_PA - y_B) + O(e^{-2(y_PA-y_B)}) (equal slope = (T2));
# similarly ln f_B^unsub(y_A - y_PB) = F_B + kappa*(y_A - y_PB).  "+inf" / "-inf" in a soft factor are represented by
# independent large cutoffs LA, LB (as in the definition (10.4), where +inf cancels inside S(+inf,y_n)/S(+inf,y_B)).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
kappa, sigma = mp.mpf('-0.37'), mp.mpf(0)          # any kappa; sigma = 0 (space-like, self-energies omitted) or 1
FA, FB = mp.mpf('0.11'), mp.mpf('-0.23')
yPA, yPB, yn = mp.mpf('3.1'), mp.mpf('-2.7'), mp.mpf('0.4')

def lnS(y1, y2):
    Y = y1 - y2
    return kappa * (Y * mp.coth(Y) - sigma)
def lnfA(yB):
    Y = yPA - yB
    return FA + kappa * Y * mp.coth(Y)              # exact form irrelevant; asymptotic slope kappa is what matters
def lnfB(yA):
    Y = yA - yPB
    return FB + kappa * Y * mp.coth(Y)

def collins_product(yA, yB, LA, LB):
    # (10.4): f_A = f_A^unsub(yPA-yB) sqrt(S(+inf,yn)/(S(+inf,yB) S(yn,yB))), f_B analogously with S(yn,-inf), S(yA,-inf), S(yA,yn)
    a = lnfA(yB) + (lnS(LA, yn) - lnS(LA, yB) - lnS(yn, yB)) / 2
    b = lnfB(yA) + (lnS(yn, LB) - lnS(yA, LB) - lnS(yA, yn)) / 2
    return a + b
def printed(yA, yB, LA, LB):        # f f S(+inf,-inf)/[S(+inf,-inf) S(+inf,-inf)]
    return lnfA(yB) + lnfB(yA) + lnS(LA, LB) - 2 * lnS(LA, LB)
def claimed(yA, yB, LA, LB):        # ERR-M15 'correct': f f S(yA,yB)/[S(+inf,yB) S(yA,-inf)]
    return lnfA(yB) + lnfB(yA) + lnS(yA, yB) - lnS(LA, yB) - lnS(yA, LB)
def corrected(yA, yB, LA, LB):      # f f S(+inf,-inf)/[S(+inf,yB) S(yA,-inf)]
    return lnfA(yB) + lnfB(yA) + lnS(LA, LB) - lnS(LA, yB) - lnS(yA, LB)
def simple(yA, yB, LA, LB):         # f f / S(yA,yB)
    return lnfA(yB) + lnfB(yA) - lnS(yA, yB)

asym = FA + FB + kappa * (yPA - yPB) + kappa * sigma   # expected finite limit
print('expected limit of ln(f_A f_B) = F_A + F_B + kappa (yPA - yPB + sigma) =', mp.nstr(asym, 15))
print()
print('(a) independent cutoffs:  LA = yA + D, LB = yB - D  (D = 5, 20)  -- the +-inf of the soft factors are NOT the regulators')
hdr = '%8s %8s %5s | %14s %14s %14s %14s %14s' % ('yA', 'yB', 'D', 'Collins(10.4)', 'printed', 'claimed', 'corrected', 'ff/S(yA,yB)')
print(hdr)
for (yA, yB) in [(10, -10), (20, -20), (40, -40)]:
    for D in [5, 20]:
        yA_, yB_ = mp.mpf(yA), mp.mpf(yB)
        LA, LB = yA_ + D, yB_ - D
        vals = [f(yA_, yB_, LA, LB) for f in (collins_product, printed, claimed, corrected, simple)]
        print('%8s %8s %5s | ' % (yA, yB, D) + ' '.join('%14s' % mp.nstr(v, 9) for v in vals))
print()
print('(b) cutoffs identified with the regulators: LA = yA, LB = yB')
for (yA, yB) in [(10, -10), (40, -40)]:
    yA_, yB_ = mp.mpf(yA), mp.mpf(yB)
    vals = [f(yA_, yB_, yA_, yB_) for f in (collins_product, printed, claimed, corrected, simple)]
    print('%8s %8s       | ' % (yA, yB) + ' '.join('%14s' % mp.nstr(v, 9) for v in vals))
print()
# algebraic statement with exactly linear ln S = a + kappa Y (large rapidity gaps):
import sympy as sp
k, a, yA, yB, LA, LB, yPA_, yPB_, F1, F2, yn_ = sp.symbols('kappa a y_A y_B L_A L_B y_PA y_PB F_A F_B y_n')
lS = lambda y1, y2: a + k * (y1 - y2)
fA = F1 + k * (yPA_ - yB); fB = F2 + k * (yA - yPB_)
expr = {
 'Collins (10.4) product': fA + fB + (lS(LA, yn_) - lS(LA, yB) - lS(yn_, yB)) / 2 + (lS(yn_, LB) - lS(yA, LB) - lS(yA, yn_)) / 2,
 'printed  S(+,-)/[S(+,-)S(+,-)]': fA + fB + lS(LA, LB) - 2 * lS(LA, LB),
 'claimed  S(yA,yB)/[S(+,yB)S(yA,-)]': fA + fB + lS(yA, yB) - lS(LA, yB) - lS(yA, LB),
 'corrected S(+,-)/[S(+,yB)S(yA,-)]': fA + fB + lS(LA, LB) - lS(LA, yB) - lS(yA, LB),
 'ff/S(yA,yB)': fA + fB - lS(yA, yB),
}
for name, e in expr.items():
    print('%-38s = %s' % (name, sp.simplify(sp.expand(e))))
print()
print('=> with independent +-inf (as in the definition (10.4)) the printed and the ERR-M15 "correct" form are IDENTICAL')
print('   (both = ff/S(+inf,-inf), divergent as L_A - L_B -> inf); the form with S(+inf,-inf) in the numerator and')
print('   S(+inf,yB) S(yA,-inf) in the denominator, or simply ff/S(yA,yB), equals the Collins product.')
