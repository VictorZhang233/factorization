# Large-N Mellin moments of plus distributions and consistency of the threshold exponent with the O(as) DY D1 term.
#  <D0,z^{N-1}> = -S1(N-1) -> -ln Nbar ; <D1,z^{N-1}> = (S1(N-1)^2+S2(N-1))/2 -> (ln^2 Nbar + zeta2)/2 ; ln Nbar = ln N + gamma_E
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=30
def D(k,N): return mp.quad(lambda z:(z**(N-1)-1)*mp.log(1-z)**k/(1-z),[0,1-mp.mpf(1)/N,1])
for N in [10,100,1000]:
    S1=mp.harmonic(N-1); S2=mp.zeta(2)-mp.zeta(2,N)
    lN=mp.log(N)+mp.euler
    print(f"N={N}: <D0>={mp.nstr(D(0,N),12)} (-S1={mp.nstr(-S1,12)}, -lnNbar={mp.nstr(-lN,8)}); <D1>={mp.nstr(D(1,N),12)} ((S1^2+S2)/2={mp.nstr((S1**2+S2)/2,12)}, asympt={mp.nstr((lN**2+mp.zeta(2))/2,8)})")
# Exponent  ln Delta_N = int_0^1 dz (z^{N-1}-1)/(1-z) * 2 int_{Q^2}^{(1-z)^2 Q^2} dq^2/q^2 A  (fixed coupling, mu_F=Q)
#          = 4 A <D1>.  With A = CF as/pi: 4 A <D1> = (as/2pi) * 8 CF <D1>, i.e. the D1 coefficient 8 CF of D_qq (units as/2pi):
#          4 CF (1+z^2) D1 -> 8 CF D1 at z->1.  Consistent.
print("Exponent check: 4*A/(as/2pi) with A=CF*as/pi equals 8*CF:", mp.almosteq(4*(mp.mpf(4)/3)*2, 8*mp.mpf(4)/3))
