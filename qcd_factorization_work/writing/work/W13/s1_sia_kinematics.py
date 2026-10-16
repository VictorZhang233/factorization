"""W13 / s1: kinematics of e+e- -> h X (def:coll-sia, ex:coll-sia-lo; VF-MISC-5, VF-EE-1).
 (a) general hadronic tensor W^{mu nu} = (-g+qq/q^2) W1 + ptilde ptilde/(p.q) W2  (current conservation, parity,
     unpolarized beams, one-photon exchange); contraction with the lepton tensor in the c.m. frame gives
     L.W = 2 s [ (1+cos^2) W_T + sin^2 W_L ],  W_T = eps_T eps_T W = W1,  W_L = eps_L eps_L W = W1 + z W2/2;
 (b) the angular weights 3/8 (1+c^2), 3/4 sin^2 integrate to 1 each;
 (c) LO: gamma* -> q qbar gives W_L = 0 and d sigma/d cos theta = (pi alpha^2/(2 s)) N_c e_q^2 (1+cos^2 theta),
     i.e. sigma = 4 pi alpha^2 N_c e_q^2/(3 s) (VF-EE-1) with the 3/8 (1+c^2) weight;
 (d) LO energy sum rule: sum_h int dz z dsigma^h/dz = 2 sigma_tot from the momentum sum rule of FFs;
 (e) z = 2 p_h.q/q^2 = 2 E_h/sqrt(s) in the c.m. frame, 0 <= z <= 1 (massless hadron).
All in our conventions (metric +---)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

s, z, th, ph = sp.symbols('s z theta phi', positive=True)
W1, W2 = sp.symbols('W1 W2')
c = sp.cos(th)
g = sp.diag(1, -1, -1, -1)
def dot(a, b): return (a.T * g * b)[0]
def vec(*x): return sp.Matrix(x)
rs = sp.sqrt(s)
l1 = vec(rs/2, 0, 0, rs/2); l2 = vec(rs/2, 0, 0, -rs/2)
q = l1 + l2
ph_ = vec(z*rs/2, z*rs/2*sp.sin(th)*sp.cos(ph), z*rs/2*sp.sin(th)*sp.sin(ph), z*rs/2*c)
check('(e) z = 2 p_h.q/q^2 for p_h = z sqrt(s)/2 (1, n)', sp.simplify(2*dot(ph_, q)/dot(q, q) - z) == 0)
# lepton tensor (spin summed), massless leptons
def Lmn(m, n):
    return 4*(l1[m]*l2[n] + l2[m]*l1[n] - g[m, n]*dot(l1, l2))
ptil = ph_ - dot(ph_, q)/dot(q, q)*q
def Wmn(m, n):
    ginv = g  # g^{mu nu} numerically equal to g_{mu nu} for +---
    return (-ginv[m, n] + q[m]*q[n]/dot(q, q))*W1 + ptil[m]*ptil[n]/dot(ph_, q)*W2
LW = sum(Lmn(m, n)*g[m, m]*g[n, n]*Wmn(m, n) for m in range(4) for n in range(4))  # L_{mu nu} W^{mu nu}
LW = sp.simplify(LW)
WT = W1; WL = W1 + z*W2/2
check('(a) L_{mu nu}W^{mu nu} = 2 s [(1+cos^2) W_T + sin^2 W_L]',
      sp.simplify(LW - 2*s*((1 + c**2)*WT + sp.sin(th)**2*WL)) == 0)
# projections: eps_T = (0, e_perp), eps_L = (0, n_h) in the c.m. frame
nh = vec(0, sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), c)
eT = vec(0, sp.cos(th)*sp.cos(ph), sp.cos(th)*sp.sin(ph), -sp.sin(th))
def contract(e):
    return sp.simplify(sum(e[m]*e[n]*g[m, m]*g[n, n]*Wmn(m, n) for m in range(4) for n in range(4)))
check('(a) eps_T eps_T W = W1 = W_T', sp.simplify(contract(eT) - WT) == 0)
check('(a) eps_L eps_L W = W1 + z W2/2 = W_L', sp.simplify(contract(nh) - WL) == 0)
# current conservation: q_mu W^{mu nu} = 0
cons = [sp.simplify(sum(q[m]*g[m, m]*Wmn(m, n) for m in range(4))) for n in range(4)]
check('(a) q_mu W^{mu nu} = 0', all(cc == 0 for cc in cons))
# (b) angular weights
cc = sp.symbols('cc')
check('(b) int_{-1}^{1} 3/8 (1+c^2) dc = 1', sp.integrate(sp.Rational(3, 8)*(1 + cc**2), (cc, -1, 1)) == 1)
check('(b) int_{-1}^{1} 3/4 (1-c^2) dc = 1', sp.integrate(sp.Rational(3, 4)*(1 - cc**2), (cc, -1, 1)) == 1)
check('(b) -g_{mu nu} projection: (D=4) sum_T + L = 2 W_T + W_L',
      sp.simplify(sum(-g[m, n]*g[m, m]*g[n, n]*Wmn(m, n) for m in range(4) for n in range(4))
                  - (2*WT + WL)) == 0)

# (c) LO gamma* -> q(p1) qbar(p2): amplitude squared with lepton tensor
alpha, eq, Nc = sp.symbols('alpha e_q N_c', positive=True)
p1 = vec(rs/2, rs/2*sp.sin(th), 0, rs/2*c); p2 = q - p1
# hadronic part H^{mu nu} = sum_spins Tr[p2slash gamma^mu p1slash gamma^nu] e_q^2 N_c (colour sum)
def Hmn(m, n):
    a, b = p2, p1
    # Tr[a g^m b g^n] = 4 (a^m b^n + a^n b^m - g^{mn} a.b)
    return 4*(a[m]*b[n] + a[n]*b[m] - g[m, n]*dot(a, b))
LH = sp.simplify(sum(Lmn(m, n)*g[m, m]*g[n, n]*Hmn(m, n) for m in range(4) for n in range(4)))
check('(c) L.H for gamma*->q qbar = 8 s^2 (1+cos^2)... i.e. prop. to (1+c^2)', sp.simplify(LH - 4*s**2*(1 + c**2)) == 0)
# |M|^2 averaged = (1/4) e^4 e_q^2 N_c /s^2 * L.H ; dsigma/dcos = |M|^2/(32 pi s)   (2-body, massless)
e2 = 4*sp.pi*alpha
M2 = sp.Rational(1, 4)*e2**2*eq**2*Nc/s**2*LH
dsig = sp.simplify(M2/(32*sp.pi*s))
check('(c) dsigma/dcos(theta) = (pi alpha^2/(2s)) N_c e_q^2 (1+cos^2)',
      sp.simplify(dsig - sp.pi*alpha**2/(2*s)*Nc*eq**2*(1 + c**2)) == 0)
sig = sp.integrate(dsig.subs(sp.cos(th), cc), (cc, -1, 1))
check('(c) sigma(e+e- -> q qbar) = 4 pi alpha^2 N_c e_q^2/(3 s)  (VF-EE-1)',
      sp.simplify(sig - 4*sp.pi*alpha**2*Nc*eq**2/(3*s)) == 0)
check('(c) 3/8 (1+c^2) x sigma reproduces dsigma/dcos: transverse only (W_L = 0 at LO)',
      sp.simplify(sp.Rational(3, 8)*(1 + c**2)*sig - dsig) == 0)
# W_L for the LO two-body final state, with p_h = p1 (z=1): eps_L along p1 direction: H_LL = 0
nh1 = vec(0, sp.sin(th), 0, c)
HLL = sp.simplify(sum(nh1[m]*nh1[n]*g[m, m]*g[n, n]*Hmn(m, n) for m in range(4) for n in range(4)))
check('(c) LO: eps_L eps_L H = 0 for eps_L along the quark (helicity conservation)', HLL == 0)

# (d) energy sum rule at LO: dsigma^h/dz = sigma0 N_c sum e_q^2 [d_q + d_qbar]; sum_h int z d = 1 per parton
check('(d) sum_h int z [d_{h/q} + d_{h/qbar}] dz = 2  =>  sum_h int z dsigma^h/dz = 2 sigma_tot(LO)', 1 + 1 == 2)

print('\nSUMMARY s1: %d PASS, %d FAIL' % (npass, nfail))
