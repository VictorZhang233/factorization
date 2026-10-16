# W26 / Ch23 -- s03: two-loop angle-dependent cusp anomalous dimension; gamma_HH^(2) (prop:yzliu-sI-twoloop, VF-YZL-3)
# and the Euclidean right-angle mismatch (thm:yzliu-soft-hqet status paragraph, VF-YZL-17).
# Source formula: Becher-Neubert, PRD 79 (2009) 125004 [arXiv:0904.1021], eqs. (13)-(15) (rendered page 4 checked):
#   Gamma_hh(beta) = C_F gamma_cusp(beta, a) + 2 gamma^Q(a),  cosh beta = v.v'
#   gamma_cusp(beta) = gamma_cusp(a) beta coth beta + (C_A/2)(a/pi)^2 { coth^2 b [Li3(e^-2b) + b Li2(e^-2b) - z3 + pi^2/6 b + b^3/3]
#                      + coth b [Li2(e^-2b) - 2 b ln(1-e^-2b) - pi^2/6 (1+b) - b^2 - b^3/3] + pi^2/6 + z3 + b^2 }
#   gamma^Q_0 = -2 C_F, gamma^Q_1 = C_F C_A (2pi^2/3 - 98/9 - 4 z3) + 40/9 C_F T_F n_f   [(a/4pi)^n normalisation]
# Independent cross-check: anomalous-dimension algebra of Ji-Liu-Su JHEP 08 (2023) 037 App. A, gamma_HH = 2 gamma_HL - gamma_s.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
z2, z3, pi2 = mp.zeta(2), mp.zeta(3), mp.pi**2

def Bbr(b):                      # C_A bracket of BN eq. (15)
    e = mp.e**(-2*b); c = mp.coth(b)
    return (c**2*(mp.polylog(3, e) + b*mp.polylog(2, e) - z3 + pi2/6*b + b**3/3)
            + c*(mp.polylog(2, e) - 2*b*mp.log(1 - e) - pi2/6*(1 + b) - b**2 - b**3/3) + pi2/6 + z3 + b**2)

# coefficients in (alpha_s/pi)^2 units, C_F stripped
G1cusp = 1                                       # gamma_cusp^(1) = C_F alpha/pi
G2cusp_CA = mp.mpf(67)/36 - pi2/12               # gamma_cusp^(2) C_F C_A
G2cusp_TFnf = -mp.mpf(5)/9                       # gamma_cusp^(2) C_F T_F n_f
gQ1 = -mp.mpf(1)/2                               # gamma^Q_0/(4) : -2 C_F (a/4pi) = -C_F/2 (a/pi)
gQ2_CA = (2*pi2/3 - mp.mpf(98)/9 - 4*z3)/16
gQ2_TFnf = mp.mpf(40)/9/16

def Ghh1(b):  # one loop, C_F stripped: beta coth beta - 1
    return G1cusp*b*mp.coth(b) + 2*gQ1
def Ghh2_CA(b):
    return G2cusp_CA*b*mp.coth(b) + Bbr(b)/2 + 2*gQ2_CA
def Ghh2_TFnf(b):
    return G2cusp_TFnf*b*mp.coth(b) + 2*gQ2_TFnf

for b in [mp.mpf('1e-3'), mp.mpf('1e-2')]:
    print('zero recoil: beta=%s  one-loop %s  two-loop C_F C_A %s  C_F T_F n_f %s'
          % (mp.nstr(b, 3), mp.nstr(Ghh1(b), 6), mp.nstr(Ghh2_CA(b), 6), mp.nstr(Ghh2_TFnf(b), 6)))
# large-angle constants
b = mp.mpf(60)
c1 = Ghh1(b) - G1cusp*b
c2CA = Ghh2_CA(b) - G2cusp_CA*b
c2nf = Ghh2_TFnf(b) - G2cusp_TFnf*b
ex2CA = -mp.mpf(49)/36 + pi2/12 - z3/2
print('gamma_HH^(1)            : %s  (expected -1, i.e. -alpha_s C_F/pi)' % mp.nstr(c1, 20))
print('gamma_HH^(2) C_F C_A    : %s  expected -49/36+pi^2/12-z3/2 = %s' % (mp.nstr(c2CA, 25), mp.nstr(ex2CA, 25)))
print('gamma_HH^(2) C_F T_F n_f: %s  expected 5/9 = %s' % (mp.nstr(c2nf, 20), mp.nstr(mp.mpf(5)/9, 20)))
# JLS App. A cross-check
u = 1/mp.mpf(16)
gHL_CA = (mp.mpf(110)/27 + pi2/18 - 18*z3)*u; gHL_nf = (mp.mpf(4)/27 + pi2/9)*u
gs_CA = (mp.mpf(808)/27 - 11*pi2/9 - 28*z3)*u; gs_nf = (-mp.mpf(112)/27 + 2*pi2/9)*u
print('JLS (A.6): 2 gHL - gs : C_F C_A %s ; C_F n_f %s (= 5/18, i.e. (5/9) T_F n_f with T_F=1/2)'
      % (mp.nstr(2*gHL_CA - gs_CA, 25), mp.nstr(2*gHL_nf - gs_nf, 20)))
# Euclidean right angle: cosh beta = 0  <=>  beta = i pi/2 (coth = 0)
bE = 1j*mp.pi/2
GE_CA = Ghh2_CA(bE); GE_nf = Ghh2_TFnf(bE); GE_1 = Ghh1(bE)
print('Gamma^(1)(pi/2) = %s (=-1: equals gamma_HH^(1))' % mp.nstr(GE_1, 15))
print('Gamma^(2)(pi/2): C_F C_A %s (expected pi^2/24-49/36 = %s) ; C_F T_F n_f %s (expected 5/9)'
      % (mp.nstr(GE_CA, 20), mp.nstr(pi2/24 - mp.mpf(49)/36, 20), mp.nstr(GE_nf, 15)))
mism = GE_CA - ex2CA
print('mismatch Gamma^(2)(pi/2) - gamma_HH^(2) = %s C_F C_A (alpha_s/pi)^2 ; z3/2 - pi^2/24 = %s'
      % (mp.nstr(mism, 15), mp.nstr(z3/2 - pi2/24, 15)))
ok = (abs(c1 + 1) < 1e-20 and abs(c2CA - ex2CA) < 1e-20 and abs(c2nf - mp.mpf(5)/9) < 1e-20
      and abs(2*gHL_CA - gs_CA - ex2CA) < 1e-30 and abs(2*gHL_nf - gs_nf - mp.mpf(5)/18) < 1e-30
      and abs(GE_CA - (pi2/24 - mp.mpf(49)/36)) < 1e-25 and abs(mism - (z3/2 - pi2/24)) < 1e-25
      and abs(Ghh2_CA(mp.mpf('1e-3'))) < 1e-5)
print('PASS' if ok else 'FAIL')
