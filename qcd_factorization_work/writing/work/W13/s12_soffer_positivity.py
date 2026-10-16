"""W13 / s12: Soffer inequality under LO evolution (prop:coll-soffer, lem:coll-positivity), transversity numbers.
Helicity-basis LO kernels (z<1; s6, Altarelli-Parisi 1977):
  P(q+<-q+) = C_F (1+z^2)/(1-z), P(q-<-q+) = 0;  P(q+<-g+) = T_F z^2, P(q-<-g+) = T_F (1-z)^2;
  P(g+<-q+) = C_F/z, P(g-<-q+) = C_F (1-z)^2/z;  P(g+<-g+) = C_A (1+z^4)/(z(1-z)), P(g-<-g+) = C_A (1-z)^3/z;
  transversity D_T P_qq = C_F [2z/(1-z)_+ + 3/2 delta(1-z)].
Soffer combinations S_pm = q_+ +- h_1.  System (one flavour + its antiquark + gluon):
  dS_pm/dt = [D_TP + (C_F/2)(1-z)] (x) S_pm + (C_F/2)(1-z) (x) S_mp + T_F z^2 (x) g_+ + T_F (1-z)^2 (x) g_-
  dq_-/dt  = P_qq (x) q_- + T_F (1-z)^2 (x) g_+ + T_F z^2 (x) g_-
  dg_pm/dt = sum_{q,qbar} [C_F/z (x) q_pm + C_F (1-z)^2/z (x) q_mp] + P(g+<-g+) (x) g_pm + P(g-<-g+) (x) g_mp
             (q_+ = (S_+ + S_-)/2, plus-distribution and delta terms on the diagonal)
Checks:
 (a) kernel identities: (P_qq + D_TP)/2, (P_qq - D_TP)/2 = C_F (1-z)/2 >= 0 regular; BST criterion |DP_ij| <= P_ij (z<1);
     (P_gg + DP_gg)/2 = C_A (1+z^4)/z [1/(1-z)]_+ + beta0/2 delta in the product convention (moment check).
 (b) numerical LO x-space evolution (t = int alpha_s/(2pi) dln mu^2 from 0 to 0.25) starting from a SATURATED Soffer
     bound (S_- = 0): S_- stays >= 0 (and becomes > 0), all helicity densities stay >= 0;
     control: flipping the sign of the regular coupling (C_F/2)(1-z) -> -(C_F/2)(1-z) produces S_- < 0 at once.
 (c) tensor charge: int D_TP_qq = -C_F/2; exponent -2 gamma/beta0 = 4/27 (n_f=3), 4/23 (n_f=5);
     with VF-QCD-7: delta q(91.19 GeV)/delta q(5 GeV) = (0.1180/0.2123)^(4/23); compare with the NS second moment.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

CF, CA, TF, nf = 4/3, 3.0, 0.5, 3
beta0 = 11 - 2*nf/3
z = sp.Symbol('z', positive=True)
# (a) kernel identities (regular parts, z<1)
Pqq_r = (1 + z**2)/(1 - z); DTP_r = 2*z/(1 - z)
check('(a) (P_qq - D_T P_qq)/C_F = (1-z) for z<1 (both delta terms 3/2)', sp.simplify(Pqq_r - DTP_r - (1 - z)) == 0)
pairs = {'qq': ((1 + z**2)/(1 - z), (1 + z**2)/(1 - z)), 'qg': (z**2 + (1 - z)**2, 2*z - 1),
         'gq': ((1 + (1 - z)**2)/z, 2 - z), 'gg': (2*(z/(1 - z) + (1 - z)/z + z*(1 - z)), 2*(1/(1 - z) - 2*z + 1))}
ok = True
for k, (P, DP) in pairs.items():
    for zv in np.linspace(0.01, 0.99, 99):
        Pv = float(P.subs(z, zv)); DPv = float(DP.subs(z, zv))
        ok &= abs(DPv) <= Pv + 1e-12
check('(a) BST criterion |Delta P_ij(z)| <= P_ij(z) for 0<z<1, all four channels (colour factors dropped)', ok)
# (P_gg + DP_gg)/2 vs C_A (1+z^4)/z [1/(1-z)]_+ + beta0/2 delta : compare Mellin moments N=2..5 (C_A, beta0 symbolic-free)
def mom_plus_product(g, N):   # int z^{N-1} g(z) [1/(1-z)]_+ = int (g(z) z^{N-1} - g(1))/(1-z)
    return sp.integrate(sp.simplify((g*z**(N - 1) - g.subs(z, 1))/(1 - z)), (z, 0, 1))
okm = True
for N in range(2, 6):
    lhs = (mom_plus_product(z, N) + mom_plus_product(sp.Integer(1), N)
           + sp.integrate(z**(N - 1)*((1 - z)/z + z*(1 - z) - 2*z + 1), (z, 0, 1)))     # (P+DP)/(2 C_A) w/o delta
    rhs = mom_plus_product((1 + z**4)/z, N)
    okm &= sp.simplify(lhs - rhs) == 0
check('(a) (P_gg + Delta P_gg)/2 = C_A (1+z^4)/z [1/(1-z)]_+ + (beta0/2) delta(1-z)  (moments N=2..5)', okm)

# (b) numerical LO evolution on an x grid
xg = np.concatenate([np.geomspace(1e-3, 0.5, 70, endpoint=False), 1 - np.geomspace(0.5, 1e-4, 50)])
xg = np.unique(xg)
gl_x, gl_w = np.polynomial.legendre.leggauss(64)
def interp(V, xv):
    # V on grid xg; V(1) = 0; log-linear interpolation in x below the grid end, linear near 1
    xs = np.concatenate([xg, [1.0]]); Vs = np.concatenate([V, [0.0]])
    return np.interp(xv, xs, Vs)
def conv(Vb, kernel_reg=None, Bfun=None, A=0.0, diag_V=None):
    """(K (x) Vb)(x_i) for K = A delta + B(z)[1/(1-z)]_+ + kernel_reg(z); diag_V is the same function for the
    subtraction (plus part only appears on the diagonal so diag_V = Vb)."""
    out = np.zeros_like(xg)
    for i, xv in enumerate(xg):
        zz = 0.5*(1 - xv)*gl_x + 0.5*(1 + xv); ww = 0.5*(1 - xv)*gl_w
        Vxz = interp(Vb, xv/zz)/zz
        tot = 0.0
        if kernel_reg is not None:
            tot += np.sum(ww*kernel_reg(zz)*Vxz)
        if Bfun is not None:
            Vx = Vb[i]
            tot += np.sum(ww*(Bfun(zz)*Vxz - Bfun(1.0)*Vx)/(1 - zz)) + Bfun(1.0)*Vx*np.log(1 - xv)
        tot += A*Vb[i]
        out[i] = tot
    return out
def rhs(state, sign=+1.0):
    Sp, Sm, qm, gp, gm = state          # one quark flavour; antiquark identical copies -> factor 2 in gluon sources
    qp = 0.5*(Sp + Sm)
    reg_cf = lambda zz: sign*0.5*CF*(1 - zz)
    dSp = (conv(Sp, kernel_reg=reg_cf, Bfun=lambda zz: 2*CF*zz, A=1.5*CF) + conv(Sm, kernel_reg=reg_cf)
           + conv(gp, kernel_reg=lambda zz: TF*zz**2) + conv(gm, kernel_reg=lambda zz: TF*(1 - zz)**2))
    dSm = (conv(Sm, kernel_reg=reg_cf, Bfun=lambda zz: 2*CF*zz, A=1.5*CF) + conv(Sp, kernel_reg=reg_cf)
           + conv(gp, kernel_reg=lambda zz: TF*zz**2) + conv(gm, kernel_reg=lambda zz: TF*(1 - zz)**2))
    dqm = (conv(qm, Bfun=lambda zz: CF*(1 + zz**2), A=1.5*CF) + conv(gp, kernel_reg=lambda zz: TF*(1 - zz)**2)
           + conv(gm, kernel_reg=lambda zz: TF*zz**2))
    nq = 2.0*nf      # n_f flavours, quark + antiquark, identical copies (flavour-symmetric toy)
    dgp = (nq*(conv(qp, kernel_reg=lambda zz: CF/zz) + conv(qm, kernel_reg=lambda zz: CF*(1 - zz)**2/zz))
           + conv(gp, Bfun=lambda zz: CA*(1 + zz**4)/zz, A=beta0/2) + conv(gm, kernel_reg=lambda zz: CA*(1 - zz)**3/zz))
    dgm = (nq*(conv(qm, kernel_reg=lambda zz: CF/zz) + conv(qp, kernel_reg=lambda zz: CF*(1 - zz)**2/zz))
           + conv(gm, Bfun=lambda zz: CA*(1 + zz**4)/zz, A=beta0/2) + conv(gp, kernel_reg=lambda zz: CA*(1 - zz)**3/zz))
    return np.array([dSp, dSm, dqm, dgp, dgm])
qp0 = xg**(-0.3)*(1 - xg)**3; qm0 = 0.4*xg**(-0.3)*(1 - xg)**4
gp0 = 1.2*xg**(-0.5)*(1 - xg)**5; gm0 = 0.8*xg**(-0.5)*(1 - xg)**5
h0 = qp0.copy()                        # saturated Soffer bound
state0 = np.array([qp0 + h0, qp0 - h0, qm0, gp0, gm0])
def evolve(state, tmax=0.25, nsteps=50, sign=+1.0):
    st = state.copy(); dt = tmax/nsteps; mins = []
    for k in range(nsteps):
        k1 = rhs(st, sign); k2 = rhs(st + 0.5*dt*k1, sign); k3 = rhs(st + 0.5*dt*k2, sign); k4 = rhs(st + dt*k3, sign)
        st = st + dt/6*(k1 + 2*k2 + 2*k3 + k4)
        mins.append(st.min(axis=1))
    return st, np.array(mins)
mask = xg < 0.95          # avoid the last grid points where the discretization error of the plus term is largest
stf, mins = evolve(state0)
print('   min over x<0.95 of S_- along the evolution (first, last):', mins[0, 1], mins[-1, 1])
check('(b) LO evolution from a saturated Soffer bound: S_- >= 0 for all t (and S_- > 0 at t = 0.25 on x<0.95)',
      mins[:, 1].min() > -1e-6 and (stf[1][mask] > 0).all())
check('(b) all helicity densities (S_+, q_-, g_+, g_-) stay >= 0', mins[:, [0, 2, 3, 4]].min() > -1e-6)
st_bad, mins_bad = evolve(state0, tmax=0.05, nsteps=10, sign=-1.0)
print('   control (wrong-sign regular coupling): min S_- after t=0.05:', st_bad[1][mask].min())
check('(b) control: with the regular q_+ coupling of the wrong sign, S_- becomes negative (the sign matters)',
      st_bad[1][mask].min() < -1e-3)
# (c) tensor charge
gam = sp.Rational(-1, 2)*sp.Rational(4, 3)
ex3 = -2*gam/(11 - sp.Rational(2, 3)*3); ex5 = -2*gam/(11 - sp.Rational(2, 3)*5)
check('(c) LO tensor-charge exponent -2gamma/beta0 = 4/27 (n_f=3), 4/23 (n_f=5)', ex3 == sp.Rational(4, 27) and ex5 == sp.Rational(4, 23))
r_t = (0.1180/0.2123)**float(ex5)
gam2 = -sp.Rational(4, 3)*sp.Rational(4, 3)            # gamma_qq(2) = -4 C_F/3
exNS = float(-2*gam2/(11 - sp.Rational(10, 3)))
r_ns = (0.1180/0.2123)**exNS
print('   delta q(91.19)/delta q(5 GeV) = %.4f ; NS second moment ratio = %.4f (exponent %.4f) ; axial charge (NS) ratio = 1'
      % (r_t, r_ns, exNS))
check('(c) the tensor charge falls by about 10%% between 5 and 91.19 GeV at LO (n_f=5)', abs(r_t - 0.903) < 0.002)
print('\nSUMMARY s12: %d PASS, %d FAIL' % (npass, nfail))
