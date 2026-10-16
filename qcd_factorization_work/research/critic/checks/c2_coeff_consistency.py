# One-loop MS-bar coefficient functions (units alpha_s/(2pi)) checked for mutual consistency:
#  DIS F2/x:  C_q = CF[2D1 - 3/2 D0 - (1+z)ln(1-z) - (1+z^2)/(1-z) ln z + 3 + 2z - (9/2+pi^2/3) delta]
#             C_g = TR[(z^2+(1-z)^2) ln((1-z)/z) - 8z^2 + 8z - 1]   (per q or qbar)
#  DY  qqbar: D_qq = CF[4(1+z^2)D1 - 2(1+z^2)/(1-z) ln z + (2pi^2/3 - 8) delta]     (mu=Q)
#      qg   : D_qg = TR[(z^2+(1-z)^2) ln((1-z)^2/z) + 1/2 + 3z - 7/2 z^2]
#  Known DIS-scheme DY results: CF[2(1+z^2)D1 + 3 D0 - 6 - 4z + (1+4pi^2/3) delta],
#                               TR[(z^2+(1-z)^2) ln(1-z) + 3/2 - 5z + 9/2 z^2]
# Check: D_qq - 2 C_q == DIS-scheme qqbar ; D_qg - C_g == DIS-scheme qg ; Adler: <C_q,1> = 0.
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=30
CF=mp.mpf(4)/3; TR=mp.mpf(1)/2; pi=mp.pi
class Dist:
    def __init__(s,delta=0,plus=None,reg=None):
        s.delta=mp.mpf(delta); s.plus=plus or []; s.reg=reg or []
    def act(s,h):
        val=s.delta*h(1)
        for (c,g,k) in s.plus:   # c * g(z) * D_k ;  <g D_k,h> = int (g h - g(1)h(1)) ln^k(1-z)/(1-z)
            val+=c*mp.quad(lambda x:(g(x)*h(x)-g(1)*h(1))*mp.log(1-x)**k/(1-x),[0,1])
        for (c,r) in s.reg:
            val+=c*mp.quad(lambda x:r(x)*h(x),[0,1])
        return val
one=lambda x:1
Cq=Dist(delta=CF*(-(mp.mpf(9)/2+pi**2/3)),
        plus=[(2*CF,one,1),(-mp.mpf(3)/2*CF,one,0)],
        reg=[(CF,lambda x:-(1+x)*mp.log(1-x)-(1+x**2)/(1-x)*mp.log(x)+3+2*x)])
Cg=Dist(reg=[(TR,lambda x:(x**2+(1-x)**2)*mp.log((1-x)/x)-8*x**2+8*x-1)])
Dqq=Dist(delta=CF*(2*pi**2/3-8),plus=[(4*CF,lambda x:1+x**2,1)],
         reg=[(CF,lambda x:-2*(1+x**2)/(1-x)*mp.log(x))])
Dqg=Dist(reg=[(TR,lambda x:(x**2+(1-x)**2)*mp.log((1-x)**2/x)+mp.mpf(1)/2+3*x-mp.mpf(7)/2*x**2)])
DqqDIS=Dist(delta=CF*(1+4*pi**2/3),plus=[(2*CF,lambda x:1+x**2,1),(3*CF,one,0)],reg=[(CF,lambda x:-6-4*x)])
DqgDIS=Dist(reg=[(TR,lambda x:(x**2+(1-x)**2)*mp.log(1-x)+mp.mpf(3)/2-5*x+mp.mpf(9)/2*x**2)])
tests=[(f"z^{n-1}",(lambda n:(lambda x:mp.mpf(x)**(n-1)))(n)) for n in range(1,7)]+[("exp(z)",mp.exp),("cos(3z)",lambda x:mp.cos(3*x))]
print("Adler (first moment of C_q, must vanish):", mp.nstr(Cq.act(one),15))
for name,h in tests:
    d1=Dqq.act(h)-2*Cq.act(h)-DqqDIS.act(h)
    d2=Dqg.act(h)-Cg.act(h)-DqgDIS.act(h)
    print(f"test {name:8s}: qqbar residual {mp.nstr(d1,5)}   qg residual {mp.nstr(d2,5)}")
# Closed form of Mellin moments of C_q in (alpha_s/4pi) units, derived by hand:
def S(k,n): return mp.fsum([mp.mpf(1)/j**k for j in range(1,n+1)])
def closed(n):
    S1,S2=S(1,n),S(2,n)
    return CF*(2*S1**2-2*S2+3*S1-2*S1/(n*(n+1))+mp.mpf(3)/n+mp.mpf(4)/(n+1)+mp.mpf(2)/n**2-9)
def misremembered(n):
    S1,S2=S(1,n),S(2,n)
    return CF*(2*S1**2-2*S2+3*S1-2*S1/(n*(n+1))+mp.mpf(3)/n+mp.mpf(2)/(n+1)+mp.mpf(1)/n**2-9)
for n in range(1,7):
    m=2*Cq.act(lambda x:mp.mpf(x)**(n-1))
    print(f"n={n}: 2<C_q,z^(n-1)>={mp.nstr(m,12)}  closed={mp.nstr(closed(n),12)}  diff={mp.nstr(m-closed(n),3)}  (variant w/ 2/(n+1),1/n^2: {mp.nstr(misremembered(n),8)})")
