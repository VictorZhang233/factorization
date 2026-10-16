"""
moments.py -- Mellin moments  X_N = int_0^1 dz z^(N-1) X(z)  of the O(alpha_s) MS-bar coefficient functions
(normalisation of dis_nlo.py:  F_2/x = sum_q e_q^2 [ q + qbar + (as/2pi)(C_2^q (x) (q+qbar) + 2 C_2^g (x) g) ],
F_L/x likewise with C_L), in closed form with harmonic sums S_k(N) = sum_{j=1}^N j^-k, and checks:

 1. closed forms  <->  numerical Mellin transforms of the x-space distributions computed in dis_nlo.py
    (integer N = 1..10 and non-integer N via S_1(N) = psi(N+1)+gE, S_2(N) = zeta2 - psi'(N+1));
 2. literature (N-space): Vermaseren-Vogt-Moch, Nucl. Phys. B724 (2005) 3 [hep-ph/0504242], eqs. (A.3),(A.4),
    which quote the first-order results of Bardeen-Buras-Duke-Muta 1978 in the normalisation
    x^-1 F_2 = C_ns (x) q_ns + <e^2>(C_q (x) q_s + C_g (x) g),  C = sum_n a_s^n c^(n), a_s = alpha_s/(4 pi).
    Conversion:  c^(1)_{2,q} = 2 C_2^q ,  c^(1)_{2,g} = 4 n_f C_2^g  (T_F = 1/2) ;
    for F_L, Moch-Vermaseren-Vogt, Phys. Lett. B606 (2005) 123 [hep-ph/0411112], eq. (3):
    c^(1)_{L,ns} = 4 C_F x ,  c^(1)_{L,g} = 8 n_f x(1-x)  ->  2 C_L^q, 4 n_f C_L^g ;
 3. x-space literature forms of the same papers (eqs. (4.3),(4.4) and (B.3),(B.4) of hep-ph/0504242);
 4. first-moment (N = 1) sum rules: Adler (no correction) and the Bjorken sum rule for F_1^{nubar}-F_1^{nu},
    factor 1 - (2/3) alpha_s/pi  [BBDM 1978 as reported by T. Muta, Proc. 19th ICHEP Tokyo 1978, p. 235];
 5. a numerical x-space convolution test with toy PDFs (numpy/mpmath): moments of (C (x) f)(x) = C_N f_N.
"""
import sys, os, io, contextlib
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import dis_nlo as m
from distributions import Dist, z

CF, TF = m.CF, m.TF
R = m.RESULTS
N = sp.Symbol('N', positive=True)
ok_all = True


def report(name, ok):
    global ok_all
    ok_all &= bool(ok)
    print(f'  [{"PASS" if ok else "FAIL"}] {name}')


def S(k, n):
    return sum(sp.Rational(1, j ** k) for j in range(1, n + 1))


def S11(n):
    return sum(sp.Rational(1, i) * S(1, i) for i in range(1, n + 1))


# ------------------------------------------------------------------ closed forms (alpha_s/2pi normalisation)
def C2q_N(n):
    s1, s2 = S(1, n), S(2, n)
    return CF * (s1 ** 2 - s2 + sp.Rational(3, 2) * s1 - s1 / (n * (n + 1)) + sp.Rational(3, 2) / n
                 + sp.Rational(2, n + 1) + sp.Rational(1, n ** 2) - sp.Rational(9, 2))


def C2g_N(n):
    s1 = S(1, n)
    return TF * (-sp.Rational(n * n + n + 2, n * (n + 1) * (n + 2)) * s1 + sp.Rational(1, n ** 2) - sp.Rational(1, n)
                 + sp.Rational(6, (n + 1) * (n + 2)))


def CLq_N(n):
    return CF * sp.Rational(2, n + 1)


def CLg_N(n):
    return TF * sp.Rational(4, (n + 1) * (n + 2))


def Pqq_N(n):
    return CF * (sp.Rational(3, 2) + sp.Rational(1, n * (n + 1)) - 2 * S(1, n))


def Pqg_N(n):
    return TF * sp.Rational(n * n + n + 2, n * (n + 1) * (n + 2))


# analytic continuation (real N > 0), mpmath
def S1c(x): return mp.digamma(x + 1) + mp.euler
def S2c(x): return mp.zeta(2) - mp.psi(1, x + 1)


def C2q_c(x, cf=mp.mpf(4) / 3):
    s1, s2 = S1c(x), S2c(x)
    return cf * (s1 ** 2 - s2 + 1.5 * s1 - s1 / (x * (x + 1)) + 1.5 / x + 2 / (x + 1) + 1 / x ** 2 - 4.5)


def C2g_c(x, tf=mp.mpf(1) / 2):
    s1 = S1c(x)
    return tf * (-(x * x + x + 2) / (x * (x + 1) * (x + 2)) * s1 + 1 / x ** 2 - 1 / x + 6 / ((x + 1) * (x + 2)))


print('=' * 78)
print('Closed forms used (alpha_s/2pi normalisation, S_k = S_k(N)):')
print('  C_2^q(N) = C_F[S1^2 - S2 + 3/2 S1 - S1/(N(N+1)) + 3/(2N) + 2/(N+1) + 1/N^2 - 9/2]')
print('  C_2^g(N) = T_F[-(N^2+N+2)/(N(N+1)(N+2)) S1 + 1/N^2 - 1/N + 6/((N+1)(N+2))]')
print('  C_L^q(N) = 2 C_F/(N+1),   C_L^g(N) = 4 T_F/((N+1)(N+2))')
print('  P_qq(N)  = C_F[3/2 + 1/(N(N+1)) - 2 S1],   P_qg(N) = T_F (N^2+N+2)/(N(N+1)(N+2))')

print('=' * 78)
print('1. closed forms vs numerical Mellin transform of the x-space results of dis_nlo.py')
subsCF = {CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}
xspace = {'C2q': R['C2q'], 'C2g': R['C2g'], 'CLq': R['CLq'], 'CLg': R['CLg'], 'Pqq': R['Pqq'], 'Pqg': R['Pqg']}
closed = {'C2q': C2q_N, 'C2g': C2g_N, 'CLq': CLq_N, 'CLg': CLg_N, 'Pqq': Pqq_N, 'Pqg': Pqg_N}
worst = 0
for key, dist in xspace.items():
    dnum = Dist(dist.delta.subs(subsCF), {k: v.subs(subsCF) for k, v in dist.plus.items()}, dist.reg.subs(subsCF))
    for n in list(range(1, 11)):
        num = dnum.mellin(n, prec=30)
        ex = sp.N(closed[key](n).subs(subsCF), 30)
        worst = max(worst, abs(num - mp.mpf(str(ex))))
report(f'integer N = 1..10, all six functions  (max |diff| = {mp.nstr(worst, 3)})', worst < 1e-18)
worst = 0
dq = Dist(R['C2q'].delta.subs(subsCF), {k: v.subs(subsCF) for k, v in R['C2q'].plus.items()}, R['C2q'].reg.subs(subsCF))
dg = Dist(R['C2g'].delta.subs(subsCF), {}, R['C2g'].reg.subs(subsCF))
for x in ('1.5', '2.25', '3.7', '6.1'):
    worst = max(worst, abs(dq.mellin(mp.mpf(x), prec=30) - C2q_c(mp.mpf(x))),
                abs(dg.mellin(mp.mpf(x), prec=30) - C2g_c(mp.mpf(x))))
report(f'non-integer N (analytic continuation, digamma)  (max |diff| = {mp.nstr(worst, 3)})', worst < 1e-18)

print('=' * 78)
print('2. literature, N-space: hep-ph/0504242 eqs. (A.3),(A.4)  [a_s = alpha_s/(4pi), g_qq = N+ + N-,')
print('   g_qg = 2N+2 - 4N+ - N- + 3 (shift operators acting on the harmonic sums), first-order results of BBDM]')


def c2q_MVV(n):
    F = lambda i: (S11(i) + 2 * S(1, i) - S(2, i)) if i >= 0 else None
    gqqF = F(n + 1) + F(n - 1)
    return CF * (9 * (S(1, n) - 1) + 2 * gqqF - 7 * (S(1, n - 1) + S(1, n)))


def c2g_MVV(n, nf):
    F = lambda i: S11(i) + 4 * S(1, i) - S(2, i)
    gqgF = 2 * F(n + 2) - 4 * F(n + 1) - F(n - 1) + 3 * F(n)
    return nf * (-2 * gqgF - 6 * (S(1, n - 1) - S(1, n)))


nf = sp.Symbol('n_f')
okq = all(sp.simplify(c2q_MVV(n) - 2 * C2q_N(n)) == 0 for n in range(1, 21))
okg = all(sp.simplify(c2g_MVV(n, nf) - 4 * nf * C2g_N(n).subs(TF, sp.Rational(1, 2))) == 0 for n in range(1, 21))
report('c^(1)_{2,q}(N) [MVV A.3] = 2 C_2^q(N)        for N = 1..20 (exact rationals)', okq)
report('c^(1)_{2,g}(N) [MVV A.4] = 4 n_f C_2^g(N)    for N = 1..20 (T_F = 1/2)', okg)
print('   e.g. N=2:  C_2^q = %s,  C_2^g = %s ;  N=4: C_2^q = %s, C_2^g = %s' %
      (C2q_N(2), C2g_N(2), C2q_N(4), C2g_N(4)))

print('=' * 78)
print('3. literature, x-space: hep-ph/0504242 eqs. (4.3),(4.4),(B.3),(B.4); hep-ph/0411112 eq. (3)')
x1 = 1 - z
L0, L1 = sp.log(z), sp.log(1 - z)
z2 = sp.zeta(2)
# (4.3): CF{4D1 - 3D0 - (9+4z2) delta - 2(1+x)(L1-L0) - 4 L0/(1-x) + 6 + 4x}
lit43 = Dist(delta=-(9 + 4 * z2), plus={1: 4, 0: -3}, reg=-2 * (1 + z) * (L1 - L0) - 4 * L0 / x1 + 6 + 4 * z).scale(CF)
# (4.4): nf{(2 - 4x x1)(L1 - L0) - 2 + 16 x x1}
lit44 = Dist(reg=nf * ((2 - 4 * z * x1) * (L1 - L0) - 2 + 16 * z * x1))
# (B.3): CF{(9+5x)/2 - (1/2) p_qq (3 + 4H0 + 4H1) - delta (9 + 4 z2)},  p_qq = 2/(1-x) - 1 - x (plus-distr.),
#        H0 = ln x, H1 = -ln(1-x)
# p_qq*(3 + 4 ln x - 4 ln(1-x)) = 2(3 - 4 L1)/(1-x) [-> 6 D0 - 8 D1] + 8 L0/(1-x) - (1+x)(3 + 4L0 - 4L1)
litB3 = Dist(delta=-(9 + 4 * z2), plus={0: -3, 1: 4},
             reg=(9 + 5 * z) / 2 - sp.Rational(1, 2) * (8 * L0 / x1 - (1 + z) * (3 + 4 * L0 - 4 * L1))).scale(CF)
litB4 = Dist(reg=nf * (6 - 2 * (1 - 2 * z + 2 * z ** 2) * (4 + L0 - L1)))
report('c^(1)_{2,ns}(x) [4.3] = 2 C_2^q(x)', (lit43 - R['C2q'].scale(2)).is_zero())
report('c^(1)_{2,q}(x)  [B.3] = 2 C_2^q(x)', (litB3 - R['C2q'].scale(2)).is_zero())
C2g_half = Dist(reg=R['C2g'].reg.subs(TF, sp.Rational(1, 2)))
report('c^(1)_{2,g}(x)  [4.4] = 4 n_f C_2^g(x)', (lit44 - C2g_half.scale(4 * nf)).is_zero())
report('c^(1)_{2,g}(x)  [B.4] = 4 n_f C_2^g(x)', (litB4 - C2g_half.scale(4 * nf)).is_zero())
report('c^(1)_{L,ns} = 4 C_F x = 2 C_L^q ;  c^(1)_{L,g} = 8 n_f x(1-x) = 4 n_f C_L^g  [hep-ph/0411112 eq.(3)]',
       sp.simplify(2 * R['CLq'].reg - 4 * CF * z) == 0 and
       sp.simplify(4 * nf * R['CLg'].reg.subs(TF, sp.Rational(1, 2)) - 8 * nf * z * (1 - z)) == 0)
# "whole-bracket plus" form  C_F [ (1+z^2)/(1-z) (ln((1-z)/z) - 3/4) + (9+5z)/4 ]_+ :
# g(z) = 2 ln(1-z)/(1-z) - (3/2)/(1-z) + r(z)  with r regular  ->  [g]_+ = 2 D1 - 3/2 D0 + r - delta * int_0^1 r
gfull = (1 + z ** 2) / (1 - z) * (sp.log((1 - z) / z) - sp.Rational(3, 4)) + (9 + 5 * z) / 4
r_reg = sp.simplify(gfull - (2 * L1 / (1 - z) - sp.Rational(3, 2) / (1 - z)))
int_r = sp.nsimplify(sp.N(sp.Integral(r_reg, (z, 0, 1)), 40), [sp.pi ** 2])
wb = Dist(delta=-int_r, plus={1: 2, 0: -sp.Rational(3, 2)}, reg=r_reg).scale(CF)
print('   int_0^1 r(z) dz =', int_r)
report('whole-bracket plus form C_F[(1+z^2)/(1-z)(ln((1-z)/z)-3/4)+(9+5z)/4]_+ = C_2^q', (wb - R['C2q']).is_zero())

print('=' * 78)
print('4. first moments (N = 1)')
report('Adler sum rule: C_2^q(N=1) = 0  (no O(as) correction)', C2q_N(1) == 0)
C1_1 = C2q_N(1) - CLq_N(1)        # 2 F_1 = F_2/x - F_L/x  -> C_1 = C_2 - C_L
print('   C_1^q(N=1) = C_2^q(1) - C_L^q(1) =', C1_1, ' -> 1 + (as/2pi)(-C_F) = 1 - (2/3) as/pi for C_F = 4/3')
report('Bjorken sum rule  int dx (F_1^nubar - F_1^nu) = 2[1 - (2/3) as/pi]  (BBDM/Muta 1978)',
       sp.simplify(C1_1.subs(CF, sp.Rational(4, 3)) / 2 + sp.Rational(2, 3)) == 0)
report('Gluon: C_2^g(N=1) = %s, C_L^g(N=1) = %s (no constraint; quoted for completeness)' % (C2g_N(1), CLg_N(1)), True)

print('=' * 78)
print('5. x-space convolution with toy PDFs (numerical):  int x^(N-1) (C (x) f)(x) dx = C_N f_N')
mp.mp.dps = 15
cf, tf = mp.mpf(4) / 3, mp.mpf(1) / 2
a_, b_ = mp.mpf('0.6'), mp.mpf('3.0')
f = lambda t: t ** a_ * (1 - t) ** b_                          # toy PDF
fN = lambda n: mp.beta(n + a_, b_ + 1)
reg_q = sp.lambdify(z, R['C2q'].reg.subs(subsCF), 'mpmath')
dl_q = mp.mpf(sp.N(R['C2q'].delta.subs(subsCF), 25))
pl_q = {k: mp.mpf(sp.N(v.subs(subsCF), 25)) for k, v in R['C2q'].plus.items()}


def conv_q(x):
    """(C_2^q (x) f)(x) = int_x^1 dxi/xi C(x/xi) f(xi), plus-distributions handled with the boundary term
       int_x^1 dz [g(z)]_+ h(z) = int_x^1 dz g(z)(h(z)-h(1)) - h(1) int_0^x g(z) dz,  h(z) = f(x/z)/z."""
    h = lambda zz: f(x / zz) / zz
    res = dl_q * f(x)
    tiny = mp.mpf(10) ** (-mp.mp.dps + 3)
    res += mp.quad(lambda zz: reg_q(zz) * h(zz) if 1 - zz > tiny else mp.mpf(0), [x, 1])
    for k, c in pl_q.items():
        g = lambda zz: mp.log(1 - zz) ** k / (1 - zz)
        G0x = -mp.log(1 - x) if k == 0 else -mp.log(1 - x) ** 2 / 2       # int_0^x g
        res += c * (mp.quad(lambda zz: g(zz) * (h(zz) - h(1)) if 1 - zz > tiny else mp.mpf(0), [x, 1])
                    - h(1) * G0x)
    return res


worst = 0
for n in (2, 3, 5):
    lhs = mp.quad(lambda x: x ** (n - 1) * conv_q(x), [0, mp.mpf('0.5'), 1])
    rhs = mp.mpf(sp.N(C2q_N(n).subs(subsCF), 25)) * fN(n)
    worst = max(worst, abs(lhs / rhs - 1))
report(f'C_2^q (x) f for N = 2,3,5  (max rel. diff = {mp.nstr(worst, 3)})', worst < 1e-8)

print('=' * 78)
print('MOMENT CHECKS:', 'ALL PASS' if ok_all else 'SOME FAILED')
