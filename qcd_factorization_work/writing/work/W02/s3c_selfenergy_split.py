"""W02 / Ch2 check s3c: split of the one-loop gluon self-energy pole into g^{mu nu} k^2 and k^mu k^nu parts per graph
(for ex:qcd-gluon-self-energy).  Uses oneloop_engine (same conventions as s3_oneloop_Z.py).
Run: python3 -I s3c_selfenergy_split.py"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oneloop_engine import *
TMAX[0] = 2
khat = [Fraction(2, 3), Fraction(-1, 2), Fraction(1, 4), Fraction(1, 5)]
k = vec(khat); negk = [-x for x in k]
lm = mom(-1, None); lmk = [LV[m] - k[m] for m in range(4)]
T1 = V3kin(k, lm, lmk); lp = mom(+1, None); kml = [k[m] - LV[m] for m in range(4)]
T2 = V3kin(negk, lp, kml); Dl = Dgluon(+1, None); Dkl = Dgluon(-1, k)
def gl(mu, nu):
    acc = ZERO
    for r, s, r2, s2 in itertools.product(range(4), repeat=4):
        if Dl[r][r2] == ZERO or Dkl[s][s2] == ZERO: continue
        a = T1[(mu, r, s)]; b = T2[(nu, r2, s2)]
        if a == ZERO or b == ZERO: continue
        acc += trunc(trunc(a * b) * trunc(Dl[r][r2] * Dkl[s][s2]) * (G[r] * G[s] * G[r2] * G[s2]))
    return as_sym(pole(trunc(R(QQ(1, 2)) * acc), 2))
ig0 = invsq(+1, None); ig1 = invsq(+1, negk)
def gh(mu, nu):
    return as_sym(pole(trunc(-1 * (-1) * trunc(LV[mu] * lmk[nu]) * trunc(I * ig0 * I * ig1)), 2))
Sq1 = Squark(+1, k); Sq0 = Squark(+1, None)
def qk(mu, nu):
    tr = mtr(mmul(mmul(mmul(GAM[nu], Sq1), GAM[mu]), Sq0))
    return as_sym(pole(trunc(-1 * (I * I) * tr), 2))
ku = [sp.Rational(x.numerator, x.denominator) for x in khat]
k2 = sum(G[m] * ku[m]**2 for m in range(4))
def split(fun):
    # P^{mu nu} = A k^2 g^{mu nu} + B k^mu k^nu ; determine from (1,2) and (1,1) components
    B = sp.simplify(fun(1, 2) / (ku[1] * ku[2]))
    A = sp.simplify((fun(1, 1) - B * ku[1]**2) / (G[1] * k2))
    ok = all(sp.simplify(fun(m, n) - (A * k2 * (G[m] if m == n else 0) + B * ku[m] * ku[n])) == 0 for m in range(4) for n in range(4))
    return A, B, ok
for name, fun, col in [('gluon loop (times C_A)', gl, 'C_A'), ('ghost loop (times C_A)', gh, 'C_A'), ('quark loop (times T_F n_f)', qk, 'T_F n_f')]:
    A, B, ok = split(fun)
    # i Pi_pole = (i/(16pi^2 eps)) g^2 [A k^2 g + B k k] col
    print(f'{name}: pole coefficient of k^2 g^mu nu = {sp.factor(A)}, of k^mu k^nu = {sp.factor(B)}   [structure check {ok}]')
    print(f'      Feynman gauge: {A.subs(sp.Symbol("xi"),1)} , {B.subs(sp.Symbol("xi"),1)}')
