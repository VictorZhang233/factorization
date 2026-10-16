import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
k1,k2,k,a1,a2=sp.symbols('k1 k2 k a1 a2')
Es,Esk2,Esk12,Ea,Pm=sp.symbols('E_s E_sk2 E_sk12 E_a P_m',real=True)   # E(s-k2), E(s-k1-k2)
beta=Ea+Es-Pm; al0=Es-Esk12; al1=Es-Esk2
d0=Pm-Ea-Esk12; d10=Pm-Ea-Esk2
I=sp.I
# LCOPT sector terms for colour order [12] (spectator absorbs k1 then k2), common factor i/d0 = Jcal
both_init = (I/d0)*(I/(d10+k1))*(I/(k1+k2-beta))
mixed     = (I/d0)*(I/(d10+k1))*(I/(al1-k2))
both_fin  = (I/d0)*(I/(al0-k1-k2))*(I/(al1-k2))
cov = I**3/((k1+k2-beta)*(al0-k1-k2)*(al1-k2))
print('covariant J^[12] == sum of three LCOPT sectors:', sp.simplify(both_init+mixed+both_fin-cov)==0)
# rho_12 from L3: F_A^[12](-k,k) = -(1/(4k^2)) J^(1V2)(z1,z2), z1=-a1/(2k), z2=a2/(2k); rho = (a1 a2/Jcal) F
Jcal=I/d0
z1=-a1/(2*k); z2=a2/(2*k)
F=-(1/(4*k**2))*mixed.subs({k1:z1,k2:z2})
rho=sp.simplify(a1*a2/Jcal*F)
print('rho_12(k) =',sp.factor(rho))
print('rho_12(0) =',sp.limit(rho,k,0))
kp=a2/(2*al1)
res=sp.simplify(sp.residue(rho,k,kp)) if False else sp.simplify(sp.limit((k-kp)*rho,k,kp))
ratio=sp.simplify(res/kp)
print('Res_{k_p} rho_12 / k_p =',sp.factor(ratio))
D10=sp.symbols('D10',positive=True); AL1=sp.symbols('AL1',positive=True)
# substitute d10=-D10 (<0), al1=AL1>0
r2=sp.simplify(ratio.subs({Pm: Ea+Esk2-D10}).subs({Es: Esk2+AL1}))
print('with d10=-|d10|, alpha1>0:', sp.factor(r2), '  report: -a1*alpha1/(a1*alpha1+a2*|d10|)')
print('difference:', sp.simplify(r2 - (-a1*AL1/(a1*AL1+a2*D10))))
