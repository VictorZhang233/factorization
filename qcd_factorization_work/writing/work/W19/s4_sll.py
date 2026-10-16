r"""
W19 / Ch16 -- s4_sll.py : super-leading logarithms (prop:jets-sll); checks of the quoted results.

Quoted (VF-GLA-13, VF-FRO-7):
  FKS 2006 eq. (3.24): sigma_1 = -sigma_0 (2 as/pi)^4 ln^5(Q/Q0) pi^2 Y (3N^2-4)/480   (qq -> qq, one gluon
                      outside the gap on one side; both sides: /240, FKS 2008 eq. (2.22));
  BNS 2021: tower sigma_n ~ (as/4pi)^{n+3} L^{2n+3}; q qbar singlet exchange, forward:
            sum_n sigma_n = -sigma_B (4 C_F/(3pi)) as^3 L^3 dY 2F2(1,1;2,5/2;-w), w = N_c as L^2/pi.
Checks
 S1  2F2(1,1;2,5/2;-w) = sum_n (-w)^n / ((n+1) (5/2)_n)   (series vs mpmath hyp2f2);
 S2  the n = 1 term is +sigma_B 4/(15 pi^2) C_F N_c as^4 L^5 dY; the n = 0 term is single-logarithmic (as^3 L^3);
 S3  large w: w 2F2/ln w -> 3/2 (1.497 at w = 1e8); refined: 2F2 ~ (3/2)(ln w - psi(3/2))/w;
 S4  power counting: tower as^m L^{2m-3} (m = n+3 >= 4) exceeds the LL counting as^m L^m exactly for m >= 4;
 S5  FKS coefficient for N = 3: (2/pi)^4 pi^2 (3N^2-4)/480 = 23/(30 pi^2) ~ 0.0777; vanishes like 3/N^2 relative
     to (as N)^4 at large N (absent at large N_c); BNS first SLL also O(1/N_c^2) relative to (as N_c)^4.
Run:  python3 -I s4_sll.py
"""
import sys, os, math
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

RES = []
def check(name, cond, info=''):
    RES.append((name, bool(cond)))
    print(('PASS  ' if cond else 'FAIL  ') + name + (('   [' + info + ']') if info else ''))

mp.mp.dps = 30
ok = True
for w in [mp.mpf('0.1'), mp.mpf('1'), mp.mpf('3')]:
    ser = mp.nsum(lambda n: (-w) ** n / ((n + 1) * mp.rf(mp.mpf(5) / 2, n)), [0, mp.inf])
    ok &= abs(ser - mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -w)) < 1e-25
check('S1  2F2(1,1;2,5/2;-w) = sum (-w)^n/((n+1)(5/2)_n)', ok)

aS, L, dY, sB, CF, Nc = sp.symbols('alpha_s L DeltaY sigma_B C_F N_c', positive=True)
w = Nc * aS * L ** 2 / sp.pi
n1 = -sB * 4 * CF / (3 * sp.pi) * aS ** 3 * L ** 3 * dY * (-w) / (2 * sp.Rational(5, 2))
check('S2  n=1 term = +sigma_B 4/(15 pi^2) C_F N_c as^4 L^5 dY',
      sp.simplify(n1 - sB * sp.Rational(4, 15) / sp.pi ** 2 * CF * Nc * aS ** 4 * L ** 5 * dY) == 0)

wv = mp.mpf(10) ** 8
val = wv * mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -wv) / mp.log(wv)
refined = mp.mpf(3) / 2 * (mp.log(wv) - mp.digamma(mp.mpf(3) / 2)) / wv
check('S3  w 2F2/ln w at w=1e8 = %s (-> 3/2); refined asymptotic rel. err %s' %
      (mp.nstr(val, 6), mp.nstr(abs(refined / mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -wv) - 1), 3)),
      abs(val - mp.mpf('1.497')) < 5e-4 and abs(refined / mp.hyp2f2(1, 1, 2, mp.mpf(5) / 2, -wv) - 1) < 1e-6)

check('S4  2m-3 > m  <=>  m >= 4 (first SLL at four loops, as^4 L^5)',
      all(((2 * m - 3) > m) == (m >= 4) for m in range(1, 30)))

N = sp.symbols('N', positive=True)
cFKS = (2 / sp.pi) ** 4 * sp.pi ** 2 * (3 * N ** 2 - 4) / 480
check('S5a FKS coefficient at N=3: 23/(30 pi^2) = %.5f' % float(cFKS.subs(N, 3)),
      sp.simplify(cFKS.subs(N, 3) - sp.Rational(23, 30) / sp.pi ** 2) == 0)
check('S5b relative to (as N)^4 the FKS and BNS first SLLs vanish like 1/N^2 at large N',
      sp.limit(cFKS / N ** 4 * N ** 2, N, sp.oo) == sp.Rational(3, 1) * 16 / 480 / sp.pi ** 2 and
      sp.limit((sp.Rational(4, 15) / sp.pi ** 2 * (N ** 2 - 1) / (2 * N) * N) / N ** 4, N, sp.oo) == 0)
check('S5c both sides of the gap: (3N^2-4)/240 = 2 x (3N^2-4)/480', sp.simplify(2 * (3 * N ** 2 - 4) / 480 - (3 * N ** 2 - 4) / 240) == 0)

print()
print('SUMMARY: %d/%d checks passed' % (sum(p for _, p in RES), len(RES)))
