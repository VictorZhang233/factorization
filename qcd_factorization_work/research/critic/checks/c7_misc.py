# (a) Longitudinal structure function with target mass, from the CONTEXT tensor W^{mu nu}.
# (b) One-loop Sudakov form factor vs evolution equation  d lnF/d lnQ^2 = (K+G)/2, mu dK/dmu = -gamma_K = -mu dG/dmu.
# (c) One-loop Collins-Soper kernel and gamma_K.
# (d) SCET light-cone conventions vs light-front ones.
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
M,nu,Q,F1,F2=sp.symbols('M nu Q F1 F2',positive=True)
g=sp.diag(1,-1,-1,-1); qv=sp.sqrt(nu**2+Q**2)
P=sp.Matrix([M,0,0,0]); q=sp.Matrix([nu,0,0,qv])
dot=lambda u,v:(u.T*g*v)[0]
Pq=dot(P,q); q2=dot(q,q)
Pt=P-(Pq/q2)*q
W=lambda mu,nn: (-g[mu,nn]+q[mu]*q[nn]/q2)*F1 + Pt[mu]*Pt[nn]*F2/Pq          # contravariant W^{mu nu}
lower=lambda v: g*v
eL=sp.Matrix([qv,0,0,nu])/Q; eT=sp.Matrix([0,1,0,0])
contract=lambda e: sp.simplify(sum(lower(e)[i]*lower(e)[j]*W(i,j) for i in range(4) for j in range(4)))
x=sp.symbols('x',positive=True)
WL=sp.simplify(contract(eL).subs(nu,Q**2/(2*M*x))); WT=contract(eT)
print("eps_L^2 =",sp.simplify(dot(eL,eL)),"; q.eps_L =",sp.simplify(dot(q,eL)))
print("W_T =",WT)
print("2x W_L =",sp.factor(sp.simplify(2*x*WL)),"  -> F_L = (1+4M^2x^2/Q^2)F2 - 2xF1 :",
      sp.simplify(2*x*WL-((1+4*M**2*x**2/Q**2)*F2-2*x*F1))==0)
# (b)
eps,a,CF,mu,Q2=sp.symbols('epsilon alpha_s C_F mu Q2',positive=True)
lnF=a*CF/(4*sp.pi)*(mu**2/Q2)**eps*(-2/eps**2-3/eps-8+sp.pi**2/6)
dlnF=sp.series(sp.diff(lnF,Q2)*Q2,eps,0,1).removeO()
K=a*CF/(4*sp.pi)*4/eps; G=sp.expand(2*dlnF-K)
print("2 dlnF/dlnQ^2 =",sp.simplify(sp.expand(2*dlnF)),";  G =",sp.simplify(G))
gammaK=sp.simplify(mu*sp.diff(G,mu)); print("mu dG/dmu =",gammaK," (expect 2 C_F alpha_s/pi)")
# mu dK/dmu with d alpha_s/d ln mu = -2 eps alpha_s + O(alpha_s^2) in D=4-2eps:
print("mu dK/dmu =",sp.simplify(sp.diff(K,a)*(-2*eps*a))," (expect -2 C_F alpha_s/pi)")
# (c)
b=sp.symbols('b_T',positive=True); b0=2*sp.exp(-sp.EulerGamma)
Kt=-a*CF/sp.pi*sp.log(mu**2*b**2/b0**2)
print("K~(b) one loop: d/dln mu =",sp.simplify(mu*sp.diff(Kt,mu)),"; equals -(a CF/pi)[ln(mu^2 b^2) - ln4 + 2gamma_E]:",
      sp.simplify(sp.expand_log(Kt+a*CF/sp.pi*(sp.log(mu**2*b**2)-sp.log(4)+2*sp.EulerGamma),force=True))==0)
# (d)
p0,p3=sp.symbols('p0 p3'); pplus=(p0+p3)/sp.sqrt(2); pminus=(p0-p3)/sp.sqrt(2)
nbar_p=p0+p3; n_p=p0-p3   # n=(1,0,0,1), nbar=(1,0,0,-1), metric (+,-,-,-)
print("nbar.p - sqrt2 p^+ =",sp.simplify(nbar_p-sp.sqrt(2)*pplus),"; n.p - sqrt2 p^- =",sp.simplify(n_p-sp.sqrt(2)*pminus))
