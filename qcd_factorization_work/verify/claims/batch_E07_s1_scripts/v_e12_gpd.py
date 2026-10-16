import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)
# Dirac matrices (Dirac rep), metric (+,-,-,-)
I2 = np.eye(2); Z2 = np.zeros((2,2))
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]],complex); sz = np.array([[1,0],[0,-1]],complex)
g0 = np.block([[I2,Z2],[Z2,-I2]]).astype(complex)
gs = [np.block([[Z2,s],[-s,Z2]]) for s in (sx,sy,sz)]
G = [g0]+gs
eta = np.diag([1.,-1.,-1.,-1.])
def slash(p): return sum(eta[m,m]*p[m]*G[m] for m in range(4))
def sigma(mu,nu): return 0.5j*(G[mu]@G[nu]-G[nu]@G[mu])
gplus = (G[0]+G[3])/np.sqrt(2)
def sigma_plus(nu): return (sigma(0,nu)+sigma(3,nu))/np.sqrt(2)
def lc_to_cart(vp, vm, vT):   # v^+, v^-, (v^1,v^2) -> (v^0,v^1,v^2,v^3)
    return np.array([(vp+vm)/np.sqrt(2), vT[0], vT[1], (vp-vm)/np.sqrt(2)])
def mink(a,b): return a@eta@b
def bar(X): return g0@X.conj().T@g0
maxdev = 0.0; maxdev_gordon = 0.0
for trial in range(20):
    M = 0.938; Pbp = rng.uniform(2,10); xi = rng.uniform(0.05,0.95); DT = rng.normal(size=2)*rng.uniform(0.1,2)
    Pp, Ppr = (1+xi)*Pbp, (1-xi)*Pbp
    PT, PprT = -DT/2, DT/2
    P = lc_to_cart(Pp, (M**2+PT@PT)/(2*Pp), PT); Ppr_ = lc_to_cart(Ppr, (M**2+PprT@PprT)/(2*Ppr), PprT)
    D = Ppr_-P; t = mink(D,D)
    Dlow = eta@D
    sigD = sum(sigma_plus(n)*Dlow[n] for n in range(4))     # sigma^{+nu} Delta_nu
    H, E = rng.normal(), rng.normal()
    Gam = H*gplus + E*1j*sigD/(2*M)
    tr = 0.5*np.trace(slash(Ppr_)+M*np.eye(4) @ np.eye(4) if False else (slash(Ppr_)+M*np.eye(4))@Gam@(slash(P)+M*np.eye(4))@bar(Gam)).real
    pred = 4*Pbp**2*((1-xi**2)*H**2 - 2*xi**2*H*E - (xi**2 + t/(4*M**2))*E**2)
    maxdev = max(maxdev, abs(tr-pred)/abs(pred))
    # (1/2) sum |G|^2 with G = ubar[H2 g+ + E2 i sig D/2M]u /(xi^2 Pbar^+)  vs  eq.(5) of Guo-Ji-Liu-Yang 2023
    G2 = tr/(xi**4*Pbp**2)
    eq5 = 4/xi**4*((1-t/(4*M**2))*E**2 - 2*E*(H+E) + (1-xi**2)*(H+E)**2)
    maxdev = max(maxdev, abs(G2-eq5)/abs(eq5))
    # Gordon reduction of the C (D-term) structure: (P'slash+M)[ C D+D+/M - C 4xi^2 Pbar^+ (g+ - i sig D/2M)](Pslash+M) = 0
    Dp = (D[0]+D[3])/np.sqrt(2)
    X = (Dp*Dp/M)*np.eye(4) - 4*xi**2*Pbp*(gplus - 1j*sigD/(2*M))
    maxdev_gordon = max(maxdev_gordon, np.abs((slash(Ppr_)+M*np.eye(4))@X@(slash(P)+M*np.eye(4))).max())
print('max rel. deviation, spin-sum identity and Guo-Ji-Liu-Yang (5) [corrected normalisation]:', maxdev)
print('max |Gordon reduction residual| (C-term -> H2 = A+4xi^2 C, E2 = B-4xi^2 C):', maxdev_gordon)
# --------- high-energy limit vs Ryskin (hep-ph/9511228v2 eq.(2)) with Gamma_ee = 16 pi alpha^2 e_Q^2 |psi(0)|^2/M^2 (BBL (4.4d),(A34), N_c=3)
import mpmath as mp
alpha, eQ, als, psi2, MV, W, xg = mp.mpf(1)/137, mp.mpf(2)/3, mp.mpf('0.3'), mp.mpf('0.1'), mp.mpf('3.097'), mp.mpf(100), mp.mpf('2.5')
xi = MV**2/(2*W**2)
for norm, label in [(1, 'corrected (2023) F_g, H_g(xi,xi)=xg'), (mp.mpf(1)/2, '2021 F_g with Tr (H_g = xg/2)')]:
    G2 = (mp.pi/xi*norm*xg)**2
    guo = alpha*eQ**2/(4*W**4)*(16*mp.pi*als)**2/(3*MV**3)*psi2*G2
    Gee = 16*mp.pi*alpha**2*eQ**2*psi2/MV**2
    Qb2 = MV**2/4
    rys = Gee*MV**3*mp.pi**3/(48*alpha)*als**2/Qb2**4*xg**2
    print('  %-40s  Guo(13)+(17) / Ryskin(2) = %s' % (label, mp.nstr(guo/rys, 10)))
