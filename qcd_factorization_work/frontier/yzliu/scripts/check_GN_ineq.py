import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp, random
mp.mp.dps=30
random.seed(1)
worst=[0,0,0,0]
for trial in range(4000):
    l=random.randint(0,8); c=random.uniform(0.01,0.49); y=random.uniform(-40,40); lam=10**random.uniform(-3,2.5)
    s=mp.mpc(c,y)
    r1=abs(mp.hyp1f1(2+2*l+2*s,1+2*l+s,-lam))                 # (4.2) claim <=1
    r2=abs(mp.hyp1f1(2+2*l,1+2*l-s,-lam))                     # (4.3) claim <=1
    r3=abs(mp.gamma(-l+s)/mp.gamma(1+2*l-mp.conj(s)))/abs(mp.gamma(-l+c)/mp.gamma(1+2*l-c))   # (4.4) claim <=1
    r4=abs(mp.gamma(2*s+2*l+2)/mp.gamma(1+2*l+s))/(mp.gamma(2*l+2+2*c)/mp.gamma(1+2*l+c))      # (4.5) claim <=1
    for i,r in enumerate([r1,r2,r3,r4]):
        worst[i]=max(worst[i],float(r))
print('max ratios found (each should be <=1):', worst)
