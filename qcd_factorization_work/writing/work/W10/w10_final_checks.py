# W10 final checks: formulas touched in the last revision pass
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
ok=True
def report(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ')+name); ok = ok and cond
# (1) k_mu D^{mu nu} for D = -i/(k^2)[ (g - kk/k^2)/(1+Pi) + xi kk/k^2 ]
k0,k1,k2,k3,xi,Pi=sp.symbols('k0 k1 k2 k3 xi Pi')
g=sp.diag(1,-1,-1,-1)
kup=sp.Matrix([k0,k1,k2,k3]); klow=g*kup
ksq=(kup.T*g*kup)[0]
D=sp.zeros(4,4)
for m in range(4):
    for n in range(4):
        ginv=g[m,n]
        D[m,n]=(-sp.I/ksq)*((ginv-kup[m]*kup[n]/ksq)/(1+Pi)+xi*kup[m]*kup[n]/ksq)
kD=[sp.simplify(sum(klow[m]*D[m,n] for m in range(4))) for n in range(4)]
report('k_mu D^{mu nu} = -i xi k^nu/k^2', all(sp.simplify(kD[n]-(-sp.I*xi*kup[n]/ksq))==0 for n in range(4)))
# (2) LCOPT cut-sum identity, integrated with dE/(2 pi): N=1 -> 1, N=2,3 -> 0
import mpmath as mp
def cutsum(E, d, eps):
    N=len(d); a=[E-x for x in d]; tot=0
    for c in range(N):
        t=1
        for f in range(c+1,N): t*=1/(a[f]-1j*eps)
        t*=2*eps/(a[c]**2+eps**2)
        for f in range(c): t*=1/(a[f]+1j*eps)
        tot+=t
    return tot
def rhs(E,d,eps):
    p1=1; p2=1
    for x in d: p1*=1/(E-x+1j*eps); p2*=1/(E-x-1j*eps)
    return 1j*p1-1j*p2
d3=[0.3,-0.7,1.1]
report('cut-sum identity pointwise', all(abs(cutsum(E,d3,0.05)-rhs(E,d3,0.05))<1e-12 for E in [-2.0,-0.4,0.25,0.9,3.0]))
for N,expect in [(1,1.0),(2,0.0),(3,0.0)]:
    d=d3[:N]
    val=mp.quad(lambda E: cutsum(E,d,0.05), [-mp.inf,-1,0,1,2,mp.inf])/(2*mp.pi)
    report('integral N=%d -> %g (got %s)'%(N,expect,mp.nstr(val,8)), abs(val-expect)<1e-6)
# (3) P_A = g_T + n_A n_B : H.P_A.J = H^- J^+ - H_T.J_T ; light-front v^+-=(v0+-v3)/sqrt2
def lf(v): return ((v[0]+v[3])/sp.sqrt(2),(v[0]-v[3])/sp.sqrt(2))
H=sp.symbols('H0:4'); J=sp.symbols('J0:4')
Hp,Hm=lf(H); Jp,Jm=lf(J)
nA=sp.Matrix([1/sp.sqrt(2),0,0,1/sp.sqrt(2)])   # n_A=(1^+,0^-,0_T)
nB=sp.Matrix([1/sp.sqrt(2),0,0,-1/sp.sqrt(2)])  # n_B=(0^+,1^-,0_T)
Hv=sp.Matrix(H); Jv=sp.Matrix(J)
dot=lambda a,b:(a.T*g*b)[0]
HnA=dot(Hv,nA); nBJ=dot(nB,Jv)
gT=-(H[1]*J[1]+H[2]*J[2])
report('n_A.v=v^-, n_B.v=v^+', sp.simplify(HnA-Hm)==0 and sp.simplify(nBJ-Jp)==0)
report('H.P_A.J = H^-J^+ - H_T.J_T', sp.simplify(HnA*nBJ+gT-(Hm*Jp-(H[1]*J[1]+H[2]*J[2])))==0)
print('ALL PASS' if ok else 'SOME FAILED')
