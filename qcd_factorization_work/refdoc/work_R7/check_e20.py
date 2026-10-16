import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=30
def e20(a,b,eps):
    f=lambda x: 1/((x-a+1j*eps)*(x-b-1j*eps))/(2*mp.pi)
    pts=sorted([a,b]); return mp.quad(f,[-mp.inf,pts[0]-1,pts[0],pts[1],pts[1]+1,mp.inf])
for (a,b) in [(0.3,1.1),(-0.7,0.2),(1.3,-0.4),(2.0,-3.0)]:
    for eps in [1e-3,1e-5]:
        val=e20(a,b,eps); pred=1j/(b-a+2j*eps)
        print(a,b,eps,mp.nstr(val,10),mp.nstr(pred,10),'PASS' if abs(val-pred)<1e-6*abs(pred)+1e-8 else 'FAIL')
