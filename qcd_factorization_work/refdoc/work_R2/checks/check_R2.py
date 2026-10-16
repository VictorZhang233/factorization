import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

z, n, eps = sp.symbols('z n epsilon', positive=True)
CF = sp.Rational(4,3)
results = []
def rep(name, ok, extra=''):
    results.append((name, ok, extra))
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + str(extra) if extra else ''))

# 1. NNLO R-ratio coefficient (4.4)
z3 = mp.zeta(3)
r2_0 = mp.mpf(365)/24 - 11*z3
r2_nf = mp.mpf(11)/12 - mp.mpf(2)/3*z3
rep('(4.4) r2 = 1.9857 - 0.1153 nf', abs(r2_0-1.9857)<5e-5 and abs(r2_nf-0.1153)<5e-5, (mp.nstr(r2_0,8), mp.nstr(r2_nf,8)))
# general gauge group form check (SU(3))
CA, TF = 3, mp.mpf(1)/2
cf = mp.mpf(4)/3
# R = R0[1 + 3/4 CF a + a^2(-3/32 CF^2 + CF CA (123/32 - 11/4 z3) + CF TF nf(-11/8 + z3))]
c0 = -mp.mpf(3)/32*cf**2 + cf*CA*(mp.mpf(123)/32 - mp.mpf(11)/4*z3)
cnf = cf*TF*(-mp.mpf(11)/8 + z3)
rep('(4.4) group-theory form reproduces SU(3) numbers', abs(c0-r2_0)<1e-20 and abs(cnf+r2_nf)<1e-20)

# 2. one-loop e+e- real+virtual (units sigma0 CF as/(2pi))
real = sp.Rational(19,2) - sp.pi**2
virt = -8 + sp.pi**2
s = sp.simplify(real+virt)
rep('Sec.4.2 real+virtual finite part = 3/2 -> sigma0*as/pi', s == sp.Rational(3,2) and sp.simplify(s*CF/2) == 1, s)

# 3. Adler normalisation: Pi = -(R0/(12 pi^2)) ln(Q^2/mu^2) -> D = R0 ; R = 12 pi Im Pi
Q2, mu2, R0, sv = sp.symbols('Q2 mu2 R0 s', positive=True)
Pi = -R0/(12*sp.pi**2)*sp.log(Q2/mu2)
D = sp.simplify(-12*sp.pi**2*Q2*sp.diff(Pi, Q2))
# continuation Q2 -> -s - i0 : log(Q2/mu2) -> log(s/mu2) - i pi
ImPi = sp.im(-R0/(12*sp.pi**2)*(sp.log(sv/mu2) - sp.I*sp.pi))
rep('(4.2),(4.5) Adler/R normalisation at parton level', sp.simplify(D-R0)==0 and sp.simplify(12*sp.pi*ImPi - R0)==0)

# 4. dispersion relations (4.3), (4.6): numeric check with a toy positive spectral density
rho = lambda t: (1 + 0.3*mp.sin(t))/(1+t)**0.5   # grows slower than s, integrable /s^2
def PiS(zc, Q0sq=1.0):
    # once-subtracted: Pi(z)-Pi(-Q0^2) = (z+Q0^2)/pi * int ImPi/((s+Q0^2)(s-z)), ImPi = pi rho
    f = lambda t: mp.pi*rho(t)/((t+Q0sq)*(t-zc))
    return (zc+Q0sq)/mp.pi*mp.quad(f,[0,1,10,100,mp.inf])
sval, Dl = mp.mpf(3), mp.mpf(0.7)
lhs = 12*mp.pi*mp.im(PiS(sval+1j*Dl))
Rf = lambda t: 12*mp.pi*mp.pi*rho(t)
rhs = Dl/mp.pi*mp.quad(lambda t: Rf(t)/((t-sval)**2+Dl**2),[0,1,sval,10,100,mp.inf])
rep('(4.6) smeared R = 12 pi Im Pi(s+i Delta)', abs(lhs-rhs)<1e-15, (mp.nstr(lhs,12), mp.nstr(rhs,12)))

# 5. tree-level OPE: T2 = 4 e^2 sum_{n even} w^{n-1} = 4 e^2 w/(1-w^2); disc at w=1 -> F2 = e^2 delta(1-x)
w = sp.symbols('omega')
T2 = 4*w/(1-w**2)
ser = sp.series(T2, w, 0, 10).removeO()
ok = all(ser.coeff(w, k) == (4 if (k % 2 == 1) else 0) for k in range(0, 10))
res = sp.residue(T2, w, 1)   # T2 ~ (-2)/(w-1) ... residue
# disc = T(w+i0)-T(w-i0) = -2 pi i * Res_{w=1}  for 1/(w-1-i0) convention -> compute directly
# T2 near 1: 2/(1-w) ; 1/(1-w-i0) - 1/(1-w+i0) = 2 pi i delta(1-w) -> disc = 4 pi i delta ; (5.1): disc = 4 pi i F2
rep('Example 5.2: T2 Taylor coefficients 4 at odd powers, residue -> F2 = e^2 delta', ok and res == -2, res)

# 6. P_qq moments (5.12)
def Pqq_moment(N):
    # int z^{N-1} [ (1+z^2)/(1-z)_+ + 3/2 delta(1-z) ]
    g = lambda t: (t**(N-1)*(1+t**2) - 2)/(1-t)
    return mp.quad(g,[0,1]) + mp.mpf(3)/2
ok = True
for N in range(1,9):
    S1 = sum(mp.mpf(1)/k for k in range(1,N+1))
    form = mp.mpf(3)/2 + mp.mpf(1)/(N*(N+1)) - 2*S1
    ok = ok and abs(Pqq_moment(N)-form) < 1e-20
rep('(5.12) Mellin moments of P_qq^(0)/C_F, N=1..8', ok, (mp.nstr(Pqq_moment(1),5), mp.nstr(Pqq_moment(2),8)))
# intermediate step in proof: int z^{n-1}(1+z^2)/(1-z)_+ = -S_{n-1} - S_{n+1}
ok = True
for N in range(1,9):
    lhs = mp.quad(lambda t: (t**(N-1)*(1+t**2) - 2)/(1-t),[0,1])
    rhs = -sum(mp.mpf(1)/k for k in range(1,N)) - sum(mp.mpf(1)/k for k in range(1,N+2))
    ok = ok and abs(lhs-rhs)<1e-20
rep('proof of (5.12): plus-moment = -S_{n-1}-S_{n+1}', ok)

# 7. DIS coefficient function (7.6) moments vs independent closed form (c_dis table)
def plus_moment(g_reg, sing, N):
    """int z^{N-1}[ g_reg(z) + sing-part ] where sing = list of (coef, k) meaning coef*[ln^k(1-z)/(1-z)]_+"""
    val = mp.quad(lambda t: t**(N-1)*g_reg(t), [0,1])
    for coef,k in sing:
        val += coef*mp.quad(lambda t: (t**(N-1)-1)*mp.log(1-t)**k/(1-t), [0,1])
    return val
def cq_moment(N):
    greg = lambda t: -(1+t)*mp.log(1-t) - (1+t**2)/(1-t)*mp.log(t) + 3 + 2*t
    return plus_moment(greg, [(2,1),(-mp.mpf(3)/2,0)], N) - (mp.mpf(9)/2 + mp.pi**2/3)
def cq_closed(N):
    S1 = sum(mp.mpf(1)/k for k in range(1,N+1)); S2 = sum(mp.mpf(1)/k**2 for k in range(1,N+1))
    return S1**2 - S2 + mp.mpf(3)/2*S1 - S1/(N*(N+1)) + mp.mpf(3)/(2*N) + mp.mpf(2)/(N+1) + mp.mpf(1)/N**2 - mp.mpf(9)/2
ok = all(abs(cq_moment(N)-cq_closed(N))<1e-15 for N in range(1,9))
rep('(7.6) c_q/C_F moments = BBDM closed form (alpha_s/2pi units), N=1..8', ok,
    [mp.nstr(cq_moment(N),10) for N in (1,2,3)])
def cg_moment(N):
    return mp.quad(lambda t: t**(N-1)*((t**2+(1-t)**2)*mp.log((1-t)/t) - 1 + 8*t*(1-t)), [0,1])
def cg_closed(N):
    S1 = sum(mp.mpf(1)/k for k in range(1,N+1))
    return -(N**2+N+2)/mp.mpf(N*(N+1)*(N+2))*S1 + mp.mpf(1)/N**2 - mp.mpf(1)/N + mp.mpf(6)/((N+1)*(N+2))
ok = all(abs(cg_moment(N)-cg_closed(N))<1e-15 for N in range(1,9))
rep('(7.7) C_{2,g}/T_F moments = closed form, N=1..8', ok, [mp.nstr(cg_moment(N),10) for N in (2,4)])

# 8. DY c_q^DY (p.51) : check  Delta^MSbar - 2 C_q = Delta^DIS (moments), DIS-scheme form from our critic
def cdy_moment(N):
    greg = lambda t: 4*((1+t**2)-2)*mp.log(1-t)/(1-t) - 2*(1+t**2)/(1-t)*mp.log(t)
    # 4(1+z^2)D_1 = 8 D_1 + 4 (z^2-1) ln(1-z)/(1-z)
    return plus_moment(greg, [(8,1)], N) + (2*mp.pi**2/3 - 8)
def cdis_moment(N):
    greg = lambda t: 2*((1+t**2)-2)*mp.log(1-t)/(1-t) - 6 - 4*t
    return plus_moment(greg, [(4,1),(3,0)], N) + (1 + 4*mp.pi**2/3)
ok = all(abs(cdy_moment(N) - 2*cq_moment(N) - cdis_moment(N)) < 1e-15 for N in range(1,9))
rep('c_q^DY (p.51): Delta^MSbar - 2 C_q = Delta^DIS-scheme (N=1..8)', ok)

# 9. phase space kinematics in Prop 7.4 proof: t = -(s+Q^2) y = -Q^2 y / z
Q2s, zz, y = sp.symbols('Q2 z y', positive=True)
shat = Q2s*(1-zz)/zz
Ep = (shat+Q2s)/(2*sp.sqrt(shat)); Ek = sp.sqrt(shat)/2
twopk = 2*Ep*Ek*2*y   # 2 Ep Ek (1-cos) = 4 Ep Ek y
rep('Prop 7.4: 2p.k = (s+Q^2) y = Q^2 y/z', sp.simplify(twopk - Q2s*y/zz)==0)
# two-body phase space integral normalisation
I0 = sp.gamma(1-eps)**2/sp.gamma(2-2*eps)
rep('Prop 7.4: int dy [y(1-y)]^-eps = Gamma(1-eps)^2/Gamma(2-2eps)', sp.simplify(sp.integrate((y*(1-y))**(-sp.Rational(1,10)),(y,0,1)) - I0.subs(eps,sp.Rational(1,10)))==0)

# 10. PDF one-loop normalisation: g^2 mu^{2eps} pi^{1-eps}/((2pi)^{3-2eps} Gamma(1-eps)) = (as/2pi)(4 pi mu^2)^eps/Gamma(1-eps)
alphas, mu = sp.symbols('alpha_s mu', positive=True)
lhs = 4*sp.pi*alphas*mu**(2*eps)*sp.pi**(1-eps)/((2*sp.pi)**(3-2*eps)*sp.gamma(1-eps))
rhs = alphas/(2*sp.pi)*(4*sp.pi*mu**2)**eps/sp.gamma(1-eps)
rep('Prop 7.1 proof: normalisation factor', sp.simplify(sp.expand_power_base(sp.powsimp(lhs/rhs, force=True), force=True))==1)
# (4pi)^eps/(Gamma(1-eps) eps) = 1/eps - gamma + ln 4pi + O(eps)
ex = sp.series((4*sp.pi)**eps/(sp.gamma(1-eps)*eps), eps, 0, 1).removeO()
rep('Prop 7.1 proof: (4pi)^eps/(Gamma(1-eps) eps) = 1/eps_hat + O(eps)', sp.simplify(ex - (1/eps - sp.EulerGamma + sp.log(4*sp.pi)))==0)
# sum of graphs: (1-eps)(1-x)+2x/(1-x) = (1+x^2)/(1-x) - eps(1-x)
x = sp.symbols('x')
rep('Prop 7.1: (a)+(b)+(c) = (1+x^2)/(1-x) - eps(1-x)', sp.simplify((1-eps)*(1-x)+2*x/(1-x) - ((1+x**2)/(1-x)-eps*(1-x)))==0)
# kinematics: k^2 = -kT^2/(1-xi)
kT2, xi, pp = sp.symbols('kT2 xi pplus', positive=True)
kminus = -kT2/(2*(1-xi)*pp)
rep('Prop 7.1 proof: k^2 = 2 xi p+ k- - kT^2 = -kT^2/(1-xi)', sp.simplify(2*xi*pp*kminus - kT2 + kT2/(1-xi))==0)

# 11. explicit 4D Dirac traces for graphs (a),(b)
import numpy as np
I2 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
g0 = np.block([[I2,0*I2],[0*I2,-I2]]).astype(complex)
gs = [np.block([[0*I2,s_],[-s_,0*I2]]).astype(complex) for s_ in (sx,sy,sz)]
G = [g0]+gs
metric = np.diag([1,-1,-1,-1])
def slash(v): return sum(metric[m,m]*v[m]*G[m] for m in range(4))
gp = (G[0]+G[3])/np.sqrt(2)
rng = np.random.default_rng(1)
p = np.array([1.3,0,0,1.3])  # p+ = sqrt2*1.3, p-=0
k = rng.normal(size=4)
dot = lambda a,b: a@metric@b
kplus = (k[0]+k[3])/np.sqrt(2); pplus = (p[0]+p[3])/np.sqrt(2)
lhs = 0.25*np.trace(gp@slash(k)@sum(metric[m,m]*G[m]@slash(p)@G[m] for m in range(4))@slash(k))
rhs = -(4-2)/4*np.trace(gp@(2*dot(p,k)*slash(k) - dot(k,k)*slash(p)))
rep('Graph (a) trace identity (4D numeric)', abs(lhs-rhs)<1e-10)
lhs_b = 0.25*np.trace(gp@slash(k)@gp@slash(p)); rhs_b = 2*kplus*pplus
rep('Graph (b) trace: (1/4)Tr[g+ k g+ p] = 2 k+ p+', abs(lhs_b-rhs_b)<1e-10)
gm = (G[0]-G[3])/np.sqrt(2)
rep('Tr[g+ g-] = 4 (Lemma 6.1 projector)', abs(np.trace(gp@gm)-4)<1e-12)

print('\nSUMMARY: %d/%d PASS' % (sum(1 for r in results if r[1]), len(results)))
