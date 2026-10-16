# Check of L1(b): is the relative error O(N 2^{N+1} M lambda_J/kappa) valid for general complex poles?
# N=2, both insertions final (Im z<0), single-state gaps, one colour order (sector (12)).
import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=30
def run(p1,p2,A1,A2,r1=1,r2=1,c=1,label=''):
    P=p1+p2
    kappa=min(abs(P),abs(p2))
    lamJ=max(abs(A1),abs(A2))
    assert kappa>=2*lamJ, (kappa,lamJ)
    # exact (L1(a)): (-i r1)(-i r2) J^(12)(p1,p2),  J^(12)(k)=c*[i/(A1-k1-k2)]*[i/(A2-k2)]
    J=c*(1j/(A1-P))*(1j/(A2-p2))
    exact=(-1j*r1)*(-1j*r2)*J
    R0=(r1/(-p1))*(r2/(-p2))
    w=p1*p2/(P*p2)          # race weight of sector (12)
    lead=R0*w*c
    rel=abs(exact-lead)/abs(R0)
    bound=2*2**3*abs(c)*lamJ/kappa
    print(f"{label} p1={p1} p2={p2} kappa={kappa:.4g} lamJ={lamJ}: |w|={abs(w):.4g}  rel.err/|R(0)|={rel:.4g}  stated bound={bound:.4g}  bound*|w|={bound*abs(w):.4g}  stated bound holds: {rel<=bound}")
    # direct numerical check of L1(a) at finite eta (gap +i eta), iterated integrals
    return rel,bound
# (i) Glauber-like real same-sign poles (application case): bound must hold
run(1.0-1e-12j, 0.7-1e-12j, -0.05,-0.05,label='(i) real same-sign')
# (ii) complex poles in the same half plane with opposite real parts
run(1.0-0.01j, -0.99-0.01j, -0.005,-0.005,label='(ii) complex')
run(10.0-0.5j, -9.0-0.5j, -0.4,-0.4,label='(iii) complex')
# numerical confirmation of L1(a) for case (iii): inner k1 integral by residue (LHP closing, only pole k1=p1),
# outer k2 integral by direct quadrature at finite eta
for eta in [mp.mpf('0.05'),mp.mpf('0.01')]:
    p1=mp.mpc(10,-0.5); p2=mp.mpc(-9,-0.5); A1=mp.mpf(-0.4); A2=mp.mpf(-0.4)
    g=lambda k2: (-1j)*(1j/(A1-p1-k2+1j*eta))*(1j/(A2-k2+1j*eta))/(k2-p2)
    val=mp.quad(g,[-mp.inf,-50,-9,-1,0,1,9,50,mp.inf])/(2*mp.pi)
    pred=(-1j)*(-1j)*(1j/(A1-p1-p2+1j*eta))*(1j/(A2-p2+1j*eta))
    print('eta=',eta,' L1(a) quadrature:',mp.nstr(val,12),' formula:',mp.nstr(pred,12))
