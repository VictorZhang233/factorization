# Test closed form suggested by eikonal_box.py:  J_box = (2 pi/(a b)) (pi + i Y),  J_cross = -(2 pi/(a b)) i Y
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'eikonal_box.py')).read().split("for (a,b,Y)")[0])
worst = 0
for (a,b,Y) in [(1.0,2.5,0.05),(1.0,2.5,0.3),(2.0,0.1,1.7),(0.4,0.9,4.4),(3.3,3.0,9.0),(0.05,7.0,2.2)]:
    a,b,Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    Jb = J(inner_box,a,b,Y); Jc = J(inner_cross,a,b,Y)
    pb = 2*mp.pi/(a*b)*(mp.pi + 1j*Y); pc = -2*mp.pi/(a*b)*1j*Y
    e = max(abs(Jb-pb)/abs(pb), abs(Jc-pc)/abs(pc))
    worst = max(worst, e)
    print(f"a={float(a):5.2f} b={float(b):5.2f} Y={float(Y):5.2f}: J_box={mp.nstr(Jb,10)}  J_cross={mp.nstr(Jc,10)}  rel.dev from closed form {mp.nstr(e,3)}")
print("max relative deviation:", mp.nstr(worst,3))
