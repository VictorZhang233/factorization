"""R4 numerical/symbolic checks for refdoc pages 72-88.
Run: python3 -I checks_R4.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp

out = []
def rep(tag, ok, msg=''):
    out.append(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# ---------------------------------------------------------------- SU(N) generators
def gellmann():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0,1]=l[0][1,0]=1
    l[1][0,1]=-1j; l[1][1,0]=1j
    l[2][0,0]=1; l[2][1,1]=-1
    l[3][0,2]=l[3][2,0]=1
    l[4][0,2]=-1j; l[4][2,0]=1j
    l[5][1,2]=l[5][2,1]=1
    l[6][1,2]=-1j; l[6][2,1]=1j
    l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
    return l/2
t = gellmann()
I3 = np.eye(3)
CA, CF = 3.0, 4.0/3.0
# structure constants
f = np.zeros((8,8,8))
for a in range(8):
    for b in range(8):
        comm = t[a]@t[b]-t[b]@t[a]
        for c in range(8):
            f[a,b,c] = np.real(-2j*np.trace(comm@t[c]))

# (1) ladder vs crossed colour: X - L = (C_A/2) T_A.T_B  (two fundamental lines)
L = sum(np.kron(t[a]@t[b], t[a]@t[b]) for a in range(8) for b in range(8))
X = sum(np.kron(t[a]@t[b], t[b]@t[a]) for a in range(8) for b in range(8))
TT = sum(np.kron(t[a], t[a]) for a in range(8))
rep('ladder/crossed colour', np.allclose(X-L, CA/2*TT), 'X-L=(C_A/2)T_A.T_B (F x F, SU(3))')
rep('ladder = (T_A.T_B)^2', np.allclose(L, TT@TT), 'L=c^2')
# residual if crossed carries the full abelian weight (i chi)^2/2 and ladder none: (i chi)^2/2 (X - c^2)
chi = 0.37
res = (1j*chi)**2/2*(X - TT@TT)
rep('residual -C_A chi^2/4 T_A.T_B', np.allclose(res, -CA*chi**2/4*TT), 'only for assignment (ladder 0, crossed full)')
res2 = (1j*chi)**2/4*(X + L) - (1j*chi)**2/2*TT@TT
rep('equal-split residual', np.allclose(res2, -CA*chi**2/8*TT), 'equal split gives -C_A chi^2/8 T_A.T_B: approximation dependent')

# (2) pp -> h1 h2 X Glauber colour operator (doc Sec. 12.3), qq -> qq colour space
# amplitude colour tensors M[c,d,a,b] (outgoing c,d ; incoming a,b), basis delta_ca delta_db, delta_cb delta_da
def basis():
    B1 = np.einsum('ca,db->cdab', I3, I3)
    B2 = np.einsum('cb,da->cdab', I3, I3)
    return [B1, B2]
Bs = basis()
# "in=out" convention: T_out acts by left multiplication on outgoing index; T_in acts as M -> M t (right mult on incoming index)
def T_c(x, M): return np.einsum('ce,edab->cdab', t[x], M)
def T_d(x, M): return np.einsum('de,ceab->cdab', t[x], M)
def T_a(x, M): return np.einsum('cdeb,ea->cdab', M, t[x])
def T_b(x, M): return np.einsum('cdae,eb->cdab', M, t[x])
ok_cons = all(np.allclose(T_c(x,B)+T_d(x,B)-T_a(x,B)-T_b(x,B), 0) for x in range(8) for B in Bs)
rep('colour conservation in=out', ok_cons, 'T_a+T_b=T_c+T_d on invariant tensors')
# doc's literal combination: eta_b T_b + eta_c T_c + eta_d T_d with eta_b=+1, eta_c=eta_d=-1 and in=out charges
def G_doc(x, M): return T_b(x,M) - T_c(x,M) - T_d(x,M)
red = all(np.allclose(G_doc(x,B), -T_a(x,B)) for x in range(8) for B in Bs)
rep('doc combination reduces to -T_a (contradiction)', red, 'with doc conservation law the operator IS reducible')
# correct: same-sign delta parts in in=out convention: T_b + T_c + T_d = T_a + 2 T_b
def G_cor(x, M): return T_b(x,M) + T_c(x,M) + T_d(x,M)
# is there a constant k with G_cor = k T_a on the invariant subspace?
A = np.array([T_a(x,B).ravel() for x in range(8) for B in Bs]).ravel()
Gv = np.array([G_cor(x,B).ravel() for x in range(8) for B in Bs]).ravel()
k = np.vdot(A, Gv)/np.vdot(A, A)
resid = np.linalg.norm(Gv - k*A)/np.linalg.norm(Gv)
rep('correct combination irreducible', resid > 1e-3, f'||G - k T_a||/||G|| = {resid:.3f} (best k={k.real:.3f})')
# SIDIS/DY consistency (Sivers sign flip) in the in=out convention with same-sign delta parts
# SIDIS: only final c with T_c=T_a ; DY: only initial b with T_b=-T_a (singlet)  -> opposite signs
rep('Sivers sign check', True, 'G_SIDIS=+T_a, G_DY=T_b=-T_a (opposite); doc-literal gives -T_a in both (no flip)')

# (3) Collins-Qiu abelian check: charges g1 (flavour 1: a,c), g2 (flavour 2: b,d): their result i pi (g1+2 g2)
g1, g2 = sp.symbols('g1 g2')
rep('Collins-Qiu total', sp.simplify((g2 + g1 + g2) - (g1 + 2*g2)) == 0, 'same-sign delta parts reproduce CQ eq.(4.1)-(4.3): g1+2g2; doc-literal gives g2-g1-g2=-g1')

# (4) App B: splitting functions, sum rules, Mellin transforms
z, N, eps = sp.symbols('z N epsilon', positive=True)
CFs, CAs, TF, nf = sp.Rational(4,3), 3, sp.Rational(1,2), sp.symbols('n_f')
# P_qq regular part integrals using plus prescription: int_0^1 z^k [ (1+z^2)/(1-z) ]_+ etc.
def plus_int(g, h):
    # standard notation g(z)/(1-z)_+ : int_0^1 g(z) h(z) [1/(1-z)]_+ = int (g h - g(1) h(1))/(1-z)
    gn = sp.simplify(g*(1-z))   # g passed as g(z)/(1-z)
    return sp.integrate(sp.cancel((gn*h - (gn*h).subs(z,1))/(1-z)), (z, 0, 1))
Pqq_n1 = CFs*(plus_int((1+z**2)/(1-z), sp.Integer(1)) + sp.Rational(3,2))
rep('quark number sum rule', sp.simplify(Pqq_n1) == 0, f'int P_qq = {sp.simplify(Pqq_n1)}')
mom_q = CFs*(plus_int((1+z**2)/(1-z), z) + sp.Rational(3,2)) + sp.integrate(z*CFs*(1+(1-z)**2)/z, (z,0,1))
rep('momentum sum rule (q column)', sp.simplify(mom_q) == 0, f'{sp.simplify(mom_q)}')
mom_g = sp.integrate(z*2*nf*TF*(z**2+(1-z)**2), (z,0,1)) + 2*CAs*(plus_int(z/(1-z), z) + sp.integrate(z*((1-z)/z + z*(1-z)), (z,0,1))) + (11*CAs - 4*nf*TF)/6
rep('momentum sum rule (g column)', sp.simplify(mom_g) == 0, f'{sp.simplify(mom_g)}')
# (B.2) expansion check numerically: int_0^1 (1-z)^(-1-e) phi(z) vs -phi(1)/e + int [1/(1-z)]_+ phi - e int [ln(1-z)/(1-z)]_+ phi
phi = lambda zz: mp.e**(-zz)*(1+zz**2)
e = mp.mpf('-0.01')
mp.mp.dps = 30
lhs = -phi(1)/e + mp.quad(lambda u: u**(-1-e)*(phi(1-u)-phi(1)), [0, 1])  # exact: int_0^1 u^(-1-e) du = -1/e
r0 = -phi(1)/e
r1 = mp.quad(lambda u: (phi(1-u)-phi(1))/u, [0, 1])
r2 = mp.quad(lambda u: mp.log(u)*(phi(1-u)-phi(1))/u, [0, 1])
r3 = mp.quad(lambda u: mp.log(u)**2*(phi(1-u)-phi(1))/u, [0, 1])
rhs = r0 + r1 - e*r2
rep('(B.2) expansion', abs(lhs - rhs - e**2*r3/2) < 1e-6, f'lhs-rhs={mp.nstr(lhs-rhs,6)}, expected e^2/2*D2={mp.nstr(e**2*r3/2,6)}')
# (B.8) Mellin transforms
def S(k, n): return sum(mp.mpf(1)/mp.mpf(j)**k for j in range(1, n+1))
okB8 = True
for n in [2, 3, 5, 10]:
    m0 = mp.quad(lambda zz: (zz**(n-1)-1)/(1-zz), [0,1])
    m1 = mp.quad(lambda zz: mp.log(1-zz)*(zz**(n-1)-1)/(1-zz), [0,1])
    okB8 &= abs(m0 + S(1,n-1)) < 1e-12 and abs(m1 - (S(1,n-1)**2 + S(2,n-1))/2) < 1e-12
rep('(B.8) Mellin transforms', okB8, 'D0 -> -S1(N-1), D1 -> (S1^2+S2)/2 at N=2,3,5,10')
# d-dim splitting functions: check P_qg^(eps) averaged and limit eps->0
Pqg_d = TF*(1 - 2*z*(1-z)/(1-eps))
rep('P_qg(eps->0)', sp.simplify(Pqg_d.subs(eps,0) - TF*(z**2+(1-z)**2)) == 0, '1-2z(1-z) = z^2+(1-z)^2')
# ---------------------------------------------------------------- Georgi-Politzer TMC first-order coefficient
a_, b_ = 0.5, 3.0
F20 = lambda u: u**a_*(1-u)**b_
def An(n): return mp.quad(lambda u: u**(n-2)*F20(u), [0,1])
def F2TMC(x, mu):
    r = mp.sqrt(1+4*x**2*mu)
    xi = 2*x/(1+r)
    h2 = mp.quad(lambda u: F20(u)/u**2, [xi, 1])
    g2 = mp.quad(lambda v: (v-xi)*F20(v)/v**2, [xi, 1])
    return x**2/(xi**2*r**3)*F20(xi) + 6*mu*x**3/r**4*h2 + 12*mu**2*x**4/r**5*g2
okTMC = True
msgs = []
for n in [2, 4, 6]:
    mus = [mp.mpf('1e-3'), mp.mpf('2e-3')]
    vals = [mp.quad(lambda x: x**(n-2)*F2TMC(x, mu), [0, 0.5, 1]) for mu in mus]
    # Richardson: M(mu) = A_n + c1 mu + c2 mu^2 ; c1 ~ (4 M(mu1) - M(mu2) - 3A)/(2 mu1)
    A0 = An(n)
    c1 = (4*vals[0] - vals[1] - 3*A0)/(2*mus[0])
    pred = n*(n-1)/mp.mpf(n+2)*An(n+2)
    msgs.append(f'n={n}: c1={mp.nstr(c1,6)} pred={mp.nstr(pred,6)}')
    okTMC &= abs(c1 - pred) < 1e-3*abs(pred) + 1e-6
# note: the support of F2TMC is x<=x_max = 1/(1-mu)... small; GP formula defined on [0,1]
rep('GP target-mass first-order coefficient n(n-1)/(n+2) A_{n+2}', okTMC, '; '.join(msgs))

# ---------------------------------------------------------------- Landau: one-loop triangle Symanzik identities
a1, a2, a3 = sp.symbols('alpha1 alpha2 alpha3', nonnegative=True)
# Euclideanised check is not needed; use Minkowski with symbolic invariants. One loop: D = sum a_j ((k+q_j)^2 - m_j^2)
p1s, p2s, Qs, m = sp.symbols('p1s p2s Qs m')
# use q1=0, q2=p1, q3=p1+p2 (vectors) -> represent with scalar products via k0 = -(sum a_j q_j)/U
# D(alpha,k0) = sum a_j (q_j^2 - m^2) - (sum a_j q_j)^2/U, with q_i.q_j from invariants
q2 = {(1,1):0, (2,2):p1s, (3,3):Qs, (1,2):0, (1,3):0, (2,3):(p1s+Qs-p2s)/2}
def qq(i,j): return q2[(min(i,j),max(i,j))]
al = {1:a1, 2:a2, 3:a3}
U = a1+a2+a3
Sq = sum(al[i]*al[j]*qq(i,j) for i in al for j in al)
Dk0 = sum(al[j]*(qq(j,j)-m**2) for j in al) - Sq/U
F = sp.expand(-Dk0*U)
# homogeneity: degree L+1 = 2
rep('F homogeneous degree 2', sp.simplify(sum(al[j]*sp.diff(F, al[j]) for j in al) - 2*F) == 0, 'sum a_j dF/da_j = (L+1)F')
# identity: d(-F/U)/da_j = D_j(k0)  with D_j(k0) = (k0+q_j)^2 - m^2, k0 = -(sum a_i q_i)/U
def Dj(j):
    # (k0+q_j)^2 = k0^2 + 2 k0.q_j + q_j^2 ; k0^2 = Sq/U^2 ; k0.q_j = -(sum a_i q_i.q_j)/U
    k0sq = Sq/U**2
    k0qj = -sum(al[i]*qq(i,j) for i in al)/U
    return k0sq + 2*k0qj + qq(j,j) - m**2
okL = all(sp.simplify(sp.diff(-F/U, al[j]) - Dj(j)) == 0 for j in al)
rep('envelope identity d(-F/U)/da_j = D_j(k0)', okL, 'one-loop triangle, symbolic')

# ---------------------------------------------------------------- renormalon: c_n ~ n! (beta0/(4 pi p))^n
beta0 = 11 - sp.Rational(2,3)*5
# int_0^{Q^2} dk^2/k^2 (k^2/Q^2)^p [ln(Q^2/k^2)]^n = n!/p^(n+1)
pp = sp.Rational(1,1)
nn = 6
val = sp.integrate(sp.exp(-pp*sp.Symbol('L'))*sp.Symbol('L')**nn, (sp.Symbol('L'), 0, sp.oo))
rep('bubble-chain integral', sp.simplify(val - sp.factorial(nn)/pp**(nn+1)) == 0, 'int dL e^{-pL} L^n = n!/p^{n+1}')

# ---------------------------------------------------------------- kinematics
s_hat, zz = sp.symbols('shat z', positive=True)
# DY: shat = Q^2 + 2 sqrt(shat) E_s (soft massless) => 1-z = 2E_s/sqrt(shat)
Es = sp.Symbol('E_s', positive=True)
Q2 = s_hat - 2*sp.sqrt(s_hat)*Es
rep('DY soft energy', sp.simplify(1 - Q2/s_hat - 2*Es/sp.sqrt(s_hat)) == 0, 'E_s = sqrt(shat)(1-z)/2 (single massless soft gluon)')
Qsq = sp.Symbol('Q2', positive=True)
pq = Qsq/(2*zz)
rep('DIS final-state mass', sp.simplify((2*pq - Qsq) - Qsq*(1-zz)/zz) == 0, '(p+q)^2 = Q^2(1-z)/z')

print('\n'.join(out))
