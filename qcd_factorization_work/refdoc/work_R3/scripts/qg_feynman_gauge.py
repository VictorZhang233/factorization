# q(p1) + g(k) -> gamma*(q) + q(p2): s-channel graph (d) and u/t-channel graph (e) of refdoc Fig. 34.
# Feynman gauge, polarization sums -g for gluon and -g + q q/Q^2 -> just -g (current conserved) for gamma*.
# Which pieces carry the collinear 1/t singularity, t = (k - p2)^2 (outgoing quark || incoming gluon)?
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
I2=np.eye(2); Z2=np.zeros((2,2))
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
g=[np.block([[Z2,I2],[I2,Z2]]).astype(complex)]+[np.block([[Z2,si],[-si,Z2]]) for si in s]
eta=np.diag([1,-1,-1,-1.])
def sl(p): return sum(eta[m,m]*p[m]*g[m] for m in range(4))
def dot(a,b): return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
rng=np.random.default_rng(1)
def kin(sh, Q2, cth):
    # CM frame of p1 + k
    E=np.sqrt(sh)/2
    p1=np.array([E,0,0,E]); k=np.array([E,0,0,-E])
    # final: gamma* (mass^2 Q2) and massless quark p2
    p2E=(sh-Q2)/(2*np.sqrt(sh)); sth=np.sqrt(1-cth**2)
    p2=np.array([p2E,p2E*sth,0,p2E*cth]); q=p1+k-p2
    return p1,k,p2,q
def msq(p1,k,p2,q):
    # amplitude M^{mu nu} = ubar(p2) [ g^mu S(p1+k) g^nu + g^nu S(p1-q) g^mu ] u(p1), mu: photon, nu: gluon
    res={'dd':0,'ee':0,'de':0}
    Pd=p1+k; Pe=p1-q
    Sd=sl(Pd)/dot(Pd,Pd); Se=sl(Pe)/dot(Pe,Pe)
    for mu in range(4):
        for nu in range(4):
            Md = g[mu]@Sd@g[nu]; Me = g[nu]@Se@g[mu]
            w = eta[mu,mu]*eta[nu,nu]   # (-g)(-g) contraction weights with lowered indices
            # sum over spins: Tr[ p2slash M p1slash Mbar ], Mbar = g0 M^dag g0
            def tr(A,B): return np.trace(sl(p2)@A@sl(p1)@(g[0]@B.conj().T@g[0]))
            res['dd'] += w*tr(Md,Md); res['ee'] += w*tr(Me,Me); res['de'] += w*2*tr(Md,Me).real
    return {k_: np.real(v) for k_,v in res.items()}
sh, Q2 = 10.0, 3.0
print(" cos(theta)   t          t*|d|^2      t*|e|^2      t*2Re(de)     t*total")
for cth in [0.0, -0.9, -0.99, -0.999, -0.9999]:
    p1,k,p2,q = kin(sh,Q2,cth)
    t = dot(k-p2,k-p2); u=dot(p1-p2,p1-p2)
    r = msq(p1,k,p2,q)
    tot = r['dd']+r['ee']+r['de']
    print(f" {cth:8.4f} {t:10.5f}  {t*r['dd']:12.6f} {t*r['ee']:12.6f} {t*r['de']:12.6f} {t*tot:12.6f}")
# compare total with known crossed formula  sum|M|^2 / (e^2 g^2 ...) = -8 (s/t + t/s + 2 u Q^2/(s t)) (up to colour/coupling factors)
p1,k,p2,q = kin(sh,Q2,0.3); t=dot(k-p2,k-p2); u=dot(p1-p2,p1-p2); r=msq(p1,k,p2,q)
print("total / [-8 (s/t + t/s + 2uQ^2/(st))] =", (r['dd']+r['ee']+r['de'])/(-8*(sh/t+t/sh+2*u*Q2/(sh*t))))
