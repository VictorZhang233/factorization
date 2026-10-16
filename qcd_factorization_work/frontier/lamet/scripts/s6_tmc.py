#!/usr/bin/env python3
"""s6: exact target-mass correction of the quasi-PDF (Chen, Cohen, Ji, Lin, Zhang, NPB 911 (2016) 246, App. B):
   moments  <x^{n-1}>_qtilde / <x^{n-1}>_q = K_n = sum_i binom(n-i,i) c^i ,  c = M^2/(4 P_z^2)
   closed form  qtilde(x) = [ f+/2 q(2x/f+) - f-/2 q(-2x/f-) ] / sqrt(1+4c),  f(+/-) = sqrt(1+4c) +/- 1.
Check: (i) K_n identity with the 'Fibonacci' form, (ii) moments of the closed form reproduce K_n, (iii) the inverse
series of Chen et al. reconstructs q numerically, (iv) particle number conserved."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate
PASS=0; FAIL=0
def check(n, ok):
    global PASS, FAIL
    print(("PASS " if ok else "FAIL ")+n); PASS+=ok; FAIL+=(not ok)
c=sp.symbols('c',positive=True); s=sp.sqrt(1+4*c); fp=s+1; fm=s-1
for n in range(1,13):
    Kn=sum(sp.binomial(n-i,i)*c**i for i in range(0,n//2+1))
    clos=((fp/2)**(n+1)-(-1)**(n-1)*(fm/2)**(n+1))/s
    check("K_%d = closed-form moment ratio"%n, sp.simplify(sp.expand(Kn-clos))==0)
# numerical: q(x) = x^{-0.5}(1-x)^3 on [0,1] (valence-like), c=0.1
cv=0.1; sv=np.sqrt(1+4*cv); fpv=sv+1; fmv=sv-1
q=lambda x: x**-0.5*(1-x)**3 if 0<x<1 else 0.0
qt=lambda x: (fpv/2*q(2*x/fpv)-fmv/2*q(-2*x/fmv))/sv
n0=integrate.quad(qt,-5,0,limit=200)[0]+integrate.quad(qt,0,fpv/2,limit=200,points=[0])[0]
nq=integrate.quad(q,0,1)[0]
check("particle number conserved: int qtilde = int q (%.10f vs %.10f)"%(n0,nq), abs(n0-nq)<1e-8)
for n in (2,3,4):
    mt=integrate.quad(lambda x: x**(n-1)*qt(x),-5,fpv/2,limit=400,points=[0])[0]
    mq=integrate.quad(lambda x: x**(n-1)*q(x),0,1)[0]
    Kn=sum(float(sp.binomial(n-i,i))*cv**i for i in range(0,n//2+1))
    check("moment n=%d: ratio %.10f vs K_n %.10f"%(n,mt/mq,Kn), abs(mt/mq-Kn)<1e-7)
# inverse series (Chen et al. eq. for q in terms of qtilde)
def q_rec(x, N=40):
    tot=0.0
    for k in range(N):
        a=fmv**k/fpv**(k+1)
        arg=fpv**(k+1)*x/(2*fmv**k)
        tot+=a*((1+(-1)**k)*qt(arg)+(1-(-1)**k)*qt(-arg))
    return sv*tot
for xv in (0.2,0.5,0.8):
    check("inverse series reconstructs q(%.1f): %.10f vs %.10f"%(xv,q_rec(xv),q(xv)), abs(q_rec(xv)-q(xv))<1e-9)
# ---------------- gamma^0 (index perpendicular to z): new all-order closed form ----------------
# moments of qtilde_{gamma^0}: Kperp_N = sum_i binom(N-i,i) (N-2i)/N c^i  (derived from u.d/dz of the traceless tensor,
# u=e_0, u.z=0);  identity Kperp_N = K_N - (2c/N) dK_N/dc ;  => qtilde_perp = qtilde_par - 2c int_0^1 dy/y d_c qtilde_par(x/y)
for n in range(1,13):
    Kn=sum(sp.binomial(n-i,i)*c**i for i in range(0,n//2+1))
    Kp=sum(sp.binomial(n-i,i)*sp.Rational(n-2*i,n)*c**i for i in range(0,n//2+1))
    check("Kperp_%d = K_%d - (2c/%d) dK/dc"%(n,n,n), sp.simplify(sp.expand(Kp-(Kn-2*c/n*sp.diff(Kn,c))))==0)
check("Kperp_2 = 1 (no TMC of <x> for gamma^0: g^{0z}=0)", sp.simplify(sum(sp.binomial(2-i,i)*sp.Rational(2-2*i,2)*c**i for i in range(2)))==1)
def qpar(x,cc):
    s_=np.sqrt(1+4*cc); fp_=s_+1; fm_=s_-1
    return (fp_/2*q(2*x/fp_)-fm_/2*q(-2*x/fm_))/s_
def dc_qpar(x,cc,h=1e-6):
    return (qpar(x,cc+h)-qpar(x,cc-h))/(2*h)
def qperp(x,cc):
    # A[g](x) = int_0^1 dy/y g(x/y); g = d_c qpar has support (-fm/2, fp/2)
    s_=np.sqrt(1+4*cc); fp_=s_+1; fm_=s_-1
    if x>0:
        lo=min(1.0,2*x/fp_)
    else:
        lo=min(1.0,2*abs(x)/fm_)
    if lo>=1.0: Ag=0.0
    else: Ag=integrate.quad(lambda y: dc_qpar(x/y,cc)/y, lo, 1, limit=400)[0]
    return qpar(x,cc)-2*cc*Ag
cv2=0.1
for n in (1,2,3,4):
    s_=np.sqrt(1+4*cv2); fp_=s_+1; fm_=s_-1
    mt=integrate.quad(lambda x: x**(n-1)*qperp(x,cv2),-fm_/2,0,limit=200)[0]+integrate.quad(lambda x: x**(n-1)*qperp(x,cv2),0,fp_/2,limit=200,points=[0.02,0.5])[0]
    mq=integrate.quad(lambda x: x**(n-1)*q(x),0,1)[0]
    Kp=sum(float(sp.binomial(n-i,i))*(n-2*i)/n*cv2**i for i in range(0,n//2+1))
    check("gamma^0 closed form: moment n=%d ratio %.8f vs Kperp %.8f"%(n,mt/mq,Kp), abs(mt/mq-Kp)<2e-5)
# O(c) expansion vs Braun-Vladimirov-Zhang eq. (target-perp):  qtilde_perp = q - c (x q' + 3 q) + 2c int_x^1 dy/y q(x/y)
dq=lambda x: -0.5*x**-1.5*(1-x)**3-3*x**-0.5*(1-x)**2
for xv in (0.3,0.6):
    cc=1e-4
    num=(qperp(xv,cc)-q(xv))/cc
    bvz=-(xv*dq(xv)+3*q(xv))+2*integrate.quad(lambda y: q(xv/y)/y, xv, 1)[0]
    check("gamma^0 O(c) term vs BVZ (target-perp) at x=%.1f: %.6f vs %.6f"%(xv,num,bvz), abs(num-bvz)<2e-3*max(1,abs(bvz)))
    nump=(qpar(xv,cc)-q(xv))/cc
    bvzp=-(xv*dq(xv)+q(xv))
    check("gamma^z O(c) term vs BVZ (target-parallel) at x=%.1f: %.6f vs %.6f"%(xv,nump,bvzp), abs(nump-bvzp)<2e-3*max(1,abs(bvzp)))
print("\nSUMMARY s6: %d PASS, %d FAIL"%(PASS,FAIL))
