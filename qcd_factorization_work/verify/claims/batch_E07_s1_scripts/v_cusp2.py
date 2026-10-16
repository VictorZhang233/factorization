import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
z2, z3, pi = mp.zeta(2), mp.zeta(3), mp.pi
# Everything in units (alpha_s/pi)^2, colour-stripped by C_F; two-loop part split as  CA*X_A + TF*nf*X_f.
# Normalisation: one loop Gamma^(1) = C_F (g coth g - 1)  [Korchemsky-Radyushkin; Liu: theta coth theta - 1]

# (a) Becher-Neubert 0904.1021 eqs.(11),(13)-(15): Gamma_hh = C_F gcusp(beta) + 2 gamma^Q
def BN(beta):
    e = mp.exp(-2*beta); c = mp.coth(beta)
    br = c**2*(mp.polylog(3,e)+beta*mp.polylog(2,e)-z3+pi**2/6*beta+beta**3/3) \
       + c*(mp.polylog(2,e)-2*beta*mp.log(1-e)-pi**2/6*(1+beta)-beta**2-beta**3/3) + pi**2/6+z3+beta**2
    g1A, g1f = (mp.mpf(268)/9-4*pi**2/3)/16, -(mp.mpf(80)/9)/16       # gamma_1^cusp/(16) per CA, per TF nf
    gQA, gQf = (2*pi**2/3-mp.mpf(98)/9-4*z3)/16, (mp.mpf(40)/9)/16     # gamma_1^Q/(16 C_F)
    XA = g1A*beta*c + br/2 + 2*gQA
    Xf = g1f*beta*c + 2*gQf
    return XA, Xf
# (b) Kidonakis 0903.2561 eq.(9): Gamma^(2) = K/2 Gamma^(1) + C_F C_A {...}, K = CA(67/18-z2) - 10/9 TF nf
def KID(g):
    e = mp.exp(-2*g); c = mp.coth(g)
    G1 = g*c-1
    br = mp.mpf(1)/2 + z2/2 + g**2/2 - c**2/2*(z3 - z2*g - g**3/3 - g*mp.polylog(2,e) - mp.polylog(3,e)) \
         - c/2*(z2 + z2*g + g**2 + g**3/3 + 2*g*mp.log(1-e) - mp.polylog(2,e))
    XA = (mp.mpf(67)/36 - z2/2)*G1 + br
    Xf = -(mp.mpf(5)/9)*G1
    return XA, Xf
# (c) Grozin-Henn-Korchemsky-Marquard 1510.07803 eqs.(5.2),(5.3),(5.5), x = e^{i phi} (Eucl.), x=e^{-phiM} (Mink.)
def H1(y): return -mp.log(1-y)
def H11(y): return mp.log(1-y)**2/2
def H111(y): return -mp.log(1-y)**3/6
def H01(y): return mp.polylog(2,y)
def H101(y): return mp.quad(lambda s: y*mp.polylog(2,s*y)/(1-s*y), [0,1])   # straight path 0->y
def A1(x):
    y = 1-x**2; xi = (1+x**2)/(1-x**2); return xi*H1(y)/2
def A2(x):
    y = 1-x**2; xi = (1+x**2)/(1-x**2); return (pi**2/3+H11(y)/2) + xi*(-H01(y)-H11(y)/2)
def A3(x):
    y = 1-x**2; xi = (1+x**2)/(1-x**2)
    return xi*(-pi**2/6*H1(y)-H111(y)/4) + xi**2*(H101(y)/2+H111(y)/4)
def lim1(f):   # A_i(1): limit x->1 (numerically, Richardson-type check)
    return mp.limit(f, 1)
A1_1, A2_1, A3_1 = lim1(A1), lim1(A2), lim1(A3)
def GHKM(x):
    t1 = A1(x)-A1_1; t2 = A2(x)-A2_1; t3 = A3(x)-A3_1
    XA = (t2+t3)/2 + mp.mpf(67)/36*t1
    Xf = -(mp.mpf(5)/9)*t1
    return XA, Xf, t1
print('A_i(1):', mp.nstr(A1_1,12), mp.nstr(A2_1,12), mp.nstr(A3_1,12))
print('--- Minkowski hyperbolic angle beta (x=e^{-beta}) ---')
for b in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(3), mp.mpf(8), mp.mpf(20)]:
    a = BN(b); k = KID(b); g = GHKM(mp.exp(-b))
    print(' beta=%s  BN: XA=%s Xf=%s | KID: XA=%s Xf=%s | GHKM: XA=%s Xf=%s' % (b, mp.nstr(a[0],14), mp.nstr(a[1],14), mp.nstr(k[0],14), mp.nstr(k[1],14), mp.nstr(mp.re(g[0]),14), mp.nstr(mp.re(g[1]),14)))
print('--- large-angle constant: X(beta) - (light-like cusp)*beta, beta=30 ---')
b = mp.mpf(30)
KA = mp.mpf(67)/36 - pi**2/12; Kf = -mp.mpf(5)/9
for name, val in [('BN', BN(b)), ('KID', KID(b)), ('GHKM', GHKM(mp.exp(-b))[:2])]:
    print('  %s: const_A = %s  const_f = %s' % (name, mp.nstr(mp.re(val[0])-KA*b, 15), mp.nstr(mp.re(val[1])-Kf*b, 15)))
print('  claimed gamma_HH^(2): const_A = -49/36+pi^2/12-z3/2 =', mp.nstr(-mp.mpf(49)/36+pi**2/12-z3/2, 15), ' const_f = +5/9 =', mp.nstr(mp.mpf(5)/9, 15))
print('--- Euclidean angle phi: beta -> -i*phi (x = e^{i phi}); approach pi/2 from below ---')
for ph in [mp.mpf('0.7'), mp.mpf('1.2'), pi/2 - mp.mpf('1e-6'), pi/2-mp.mpf('1e-10')]:
    a = BN(-1j*ph); a2 = BN(1j*ph); k = KID(-1j*ph); g = GHKM(mp.exp(1j*ph))
    print(' phi=%s  BN(-i phi): XA=%s | BN(+i phi): XA=%s | KID: XA=%s | GHKM: XA=%s ; one-loop Ã1=%s' % (mp.nstr(ph,12), mp.nstr(a[0],12), mp.nstr(a2[0],12), mp.nstr(k[0],12), mp.nstr(g[0],12), mp.nstr(g[2],10)))
print('  closed form at pi/2 (from Kidonakis with coth(i pi/2)=0): XA = -(67/36 - z2/2) + 1/2 - pi^2/24 =', mp.nstr(-(mp.mpf(67)/36-z2/2)+mp.mpf(1)/2-pi**2/24, 15), ' = pi^2/24 - 49/36 =', mp.nstr(pi**2/24-mp.mpf(49)/36,15))
print('  Gamma(pi/2) - gamma_HH  (C_F C_A part) = z3/2 - pi^2/24 =', mp.nstr(z3/2-pi**2/24, 15))
