import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
import sympy as sp

# 1. B.8 Mellin transforms of plus distributions
def S(k,N): return sum(1.0/j**k for j in range(1,N+1))
for N in [2,3,5,8]:
    I1 = integrate.quad(lambda z: (z**(N-1)-1)/(1-z), 0,1)[0]
    I2 = integrate.quad(lambda z: (z**(N-1)-1)*np.log(1-z)/(1-z), 0,1, limit=200)[0]
    print("N=",N," [1/(1-z)]+ :",I1, -S(1,N-1), "  [ln(1-z)/(1-z)]+ :",I2, 0.5*(S(1,N-1)**2+S(2,N-1)))

# 2. Example C.27: int d^4k 1/(k^2+m^2)^3 = pi^2/(2 m^2)
m=1.0
# 4D radial: d^4k = 2 pi^2 k^3 dk
I = integrate.quad(lambda k: 2*np.pi**2*k**3/(k**2+m**2)**3, 0, np.inf)[0]
print("int d^4k Delta^3 =",I," pi^2/2 =",np.pi**2/2)

# 3. Example C.27: F(q)=int d^4k Delta(q-k) Delta(k)^3 and G(q)=int [Delta(q-k)-Delta(q)] Delta(k)^3
# Use 4D angular average of 1/((q-k)^2+m^2): for 4D, <1/((q-k)^2+m^2)>_angles = 2/(a+sqrt(a^2-4q^2k^2)) with a=q^2+k^2+m^2
def angavg(q,k):
    a=q*q+k*k+m*m
    return 2.0/(a+np.sqrt(a*a-4*q*q*k*k))
def F(q):
    f=lambda k: 2*np.pi**2*k**3*angavg(q,k)/(k*k+m*m)**3
    return integrate.quad(f,0,q,limit=400)[0]+integrate.quad(f,q,np.inf,limit=400)[0]
def G(q):
    Dq=1.0/(q*q+m*m)
    f=lambda k: 2*np.pi**2*k**3*(angavg(q,k)-Dq)/(k*k+m*m)**3
    return integrate.quad(f,0,q,limit=400)[0]+integrate.quad(f,q,np.inf,limit=400)[0]
for q in [10.,30.,100.,300.,1000.]:
    Fq=F(q); Gq=G(q)
    print("q=%7.1f  F*q^2*2m^2/pi^2=%.6f   G*q^4=%.5f   G*q^4/ln(q^2)=%.5f"%(q, Fq*q*q*2/np.pi**2, Gq*q**4, Gq*q**4/np.log(q*q)))
