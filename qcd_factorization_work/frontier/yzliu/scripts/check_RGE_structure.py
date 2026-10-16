import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
a,L,Lb,CF,CA,nf,G2,g2,GS2,c1,c2=sp.symbols('alpha L L_b C_F C_A n_f Gamma2 gamma2 GammaS2 c1 c2')
b=sp.symbols('b')   # d alpha/d ln mu = b alpha^2
# --- matching kernel H: d lnH/d ln mu = Gamma(a) L + gamma(a), L=ln(zeta_z/mu^2) (dL/dln mu=-2)
h1 = c1 + CF/(2*sp.pi)*(L - L**2/2)
A3,A2,A1,A0=sp.symbols('A3 A2 A1 A0'); h2=A3*L**3+A2*L**2+A1*L+A0
lnH=a*h1+a**2*h2
dlnH = sp.diff(lnH,a)*b*a**2 + sp.diff(lnH,L)*(-2)
eq=sp.expand(dlnH - ((CF/sp.pi)*a + G2*a**2)*L - ((-CF/sp.pi)*a + g2*a**2))
sol=sp.solve([sp.expand(eq).coeff(a,1).coeff(L,k) for k in range(2)]+[sp.expand(eq).coeff(a,2).coeff(L,k) for k in range(3)],[A3,A2,A1],dict=True)
print('H two-loop structure:', {k:sp.simplify(v) for k,v in sol[0].items()}, '  (A0=c2 free)')
# --- intrinsic soft function: d lnS_I/d ln mu^2 = -GammaS(a), Lb=ln(mu^2 b^2/b0^2): dLb/dln mu^2=1 ; d alpha/d ln mu^2 = (b/2) alpha^2
B2,B1=sp.symbols('B2 B1')
lnS = -a*CF/sp.pi*Lb + a**2*(B2*Lb**2+B1*Lb+c2)
d = sp.diff(lnS,a)*(b/2)*a**2 + sp.diff(lnS,Lb)
eq2=sp.expand(d + (CF/sp.pi)*a + GS2*a**2)
s2=sp.solve([eq2.coeff(a,2).coeff(Lb,1), eq2.coeff(a,2).coeff(Lb,0)],[B2,B1],dict=True)[0]
print('S_I two-loop: B2 =',sp.simplify(s2[B2]),'  B1 =',s2[B1])
bAPPB = -(sp.Rational(11,3)*CA-sp.Rational(4,3)*nf*sp.Rational(1,2))/(2*sp.pi)   # APPB/PLB beta0 (coefficient of d alpha/d ln mu)
print('  with b = beta0^APPB:  B2 =', sp.simplify(s2[B2].subs(b,bAPPB)), '  ; APPB eq.(81) claims beta0*CF/(2pi) =', sp.simplify(bAPPB*CF/(2*sp.pi)))
# numeric RGE check (one-loop running, nf=4): integrate dlnS/dln mu^2 = -CF/pi*alpha(mu) from mu_b to mu and compare L_b^2 coefficient
mp.mp.dps=30
CFv=mp.mpf(4)/3; b0=mp.mpf(11)-mp.mpf(2)*4/3   # beta0^CTX for nf=4
def alpha(mu2,amu,mu2ref): return amu/(1+b0/(4*mp.pi)*amu*mp.log(mu2/mu2ref))
mu2=mp.mpf(100)
for amu,Lbv in [(mp.mpf('0.2'),mp.mpf('1.0')),(mp.mpf('0.02'),mp.mpf('1.0')),(mp.mpf('0.002'),mp.mpf('1.0'))]:
    mub2=mu2*mp.e**(-Lbv)
    exact=-CFv/mp.pi*mp.quad(lambda t: alpha(mp.e**t,amu,mu2),[mp.log(mub2),mp.log(mu2)])
    oneloop=-CFv/mp.pi*amu*Lbv
    coef=(exact-oneloop)/(amu**2*Lbv**2)
    print('  alpha=%s L_b=%s: numeric L_b^2 coefficient (alpha^2 units): %s ; predicted -CF*beta0^CTX/(8 pi^2)= %s ; APPB(81) would give %s'%(amu,Lbv,mp.nstr(coef,8),mp.nstr(-CFv*b0/(8*mp.pi**2),8),mp.nstr(-CFv*b0/(4*mp.pi**2),8)))
