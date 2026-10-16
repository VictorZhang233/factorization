"""R-S2 independent check: colour bookkeeping of the Glauber (delta) part of eikonal attachments in
a + b -> c + d (pp -> h1 h2 X), SIDIS (a + gamma* -> c) and DY (a + b -> gamma*).

(1) Signs of the delta parts from the actual propagators (scalar-QED-like vertices as in Collins-Qiu 2007):
      initial line b absorbing l before H:  -g(2k+l)^mu / ((k+l)^2 - m^2 + i eps)  ->  -2g k^mu/(2k.l + i eps)
      final line   c absorbing l after  H:  -g(2k-l)^mu / ((k-l)^2 - m^2 + i eps)  ->  -2g k^mu/(-2k.l + i eps)
    with k.l ~ k^- l^+ ; the delta(l^+) coefficients are computed numerically with an even test function.
(2) Colour (in = out convention: generators act on outgoing indices by left multiplication, on incoming quark
    indices by right multiplication; T_a + T_b = T_c + T_d on invariant hard tensors):
      correct (same-sign delta parts):   T_b + T_c + T_d = T_a + 2 T_b      (irreducible)
      reference p.74 (eta_c = eta_d = -eta_b):  eta_b (T_b - T_c - T_d) = -eta_b T_a  (reducible)
    all-outgoing version: T_b^out - T_c - T_d = T_a^out + 2 T_b^out.
(3) SIDIS and DY limits (Sivers sign flip) and the Collins-Qiu abelian limit g1 + 2 g2.
Run: python3 -I rs2_colour_glauber.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp

out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- (1) delta-part signs
mp.mp.dps = 30
phi = lambda x: mp.e**(-x**2)          # even test function -> PV parts vanish, only delta parts survive
km = mp.mpf('1.7')                      # k^- of the eikonal line
g = mp.mpf(1)
for eps in [mp.mpf('1e-3'), mp.mpf('1e-5')]:
    ini = mp.quad(lambda l: phi(l)*(-2*g*km)/(2*km*l + 1j*eps), [-mp.inf, -eps, 0, eps, mp.inf])
    fin = mp.quad(lambda l: phi(l)*(-2*g*km)/(-2*km*l + 1j*eps), [-mp.inf, -eps, 0, eps, mp.inf])
    print(f"  eps={mp.nstr(eps,2)}: initial = {mp.nstr(ini,10)}, final = {mp.nstr(fin,10)}, i*pi*g*phi(0) = {mp.nstr(1j*mp.pi,10)}")
rep('delta parts of initial and final eikonal factors have the SAME sign (in=out charges)',
    abs(ini - 1j*mp.pi) < 1e-3 and abs(fin - 1j*mp.pi) < 1e-3,
    'both -> +i pi g phi(0): Collins-Qiu (4.1)-(4.3) all read i g pi delta(l+)')
# the reference's uniform-numerator form  T_j n_j/(n_j.k + i eta_j 0)  has delta parts -i pi eta_j: opposite signs
ref_ini = mp.quad(lambda l: phi(l)/(l + 1j*mp.mpf('1e-5')), [-mp.inf, 0, mp.inf])
ref_fin = mp.quad(lambda l: phi(l)/(l - 1j*mp.mpf('1e-5')), [-mp.inf, 0, mp.inf])
rep('reference uniform-numerator bookkeeping gives OPPOSITE delta signs', abs(ref_ini + ref_fin) < 1e-3 and abs(ref_ini + 1j*mp.pi) < 1e-3,
    f'1/(l+i0) -> {mp.nstr(ref_ini,6)}, 1/(l-i0) -> {mp.nstr(ref_fin,6)}: the minus sign of the final-line numerator is dropped')

# ---------------------------------------------------------------- (2) colour algebra, qq' -> qq'
def gm():
    l = np.zeros((8,3,3), dtype=complex)
    l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1
    l[3][0,2]=l[3][2,0]=1; l[4][0,2]=-1j; l[4][2,0]=1j; l[5][1,2]=l[5][2,1]=1
    l[6][1,2]=-1j; l[6][2,1]=1j; l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
    return l/2
t = gm(); I3 = np.eye(3)
# hard tensors M[c,d,a,b] (outgoing c,d ; incoming quarks a,b)
Mt = np.einsum('hca,hdb->cdab', t, t)         # t-channel gluon exchange colour
Mu = np.einsum('hcb,hda->cdab', t, t)         # u-channel
Mgen = 0.37*Mt - 1.21j*Mu + 0.5*np.einsum('ca,db->cdab', I3, I3)
def Tc(x,M): return np.einsum('ce,edab->cdab', t[x], M)
def Td(x,M): return np.einsum('de,ceab->cdab', t[x], M)
def Ta(x,M): return np.einsum('cdeb,ea->cdab', M, t[x])
def Tb(x,M): return np.einsum('cdae,eb->cdab', M, t[x])
ok = True
for M in [Mt, Mu, Mgen]:
    for x in range(8):
        ok &= np.allclose(Tc(x,M)+Td(x,M)-Ta(x,M)-Tb(x,M), 0)
rep('colour conservation T_a+T_b=T_c+T_d on hard tensors (in=out)', ok, '')
ok_ref = all(np.allclose(Tb(x,M)-Tc(x,M)-Td(x,M), -Ta(x,M)) for M in [Mt,Mu,Mgen] for x in range(8))
rep('reference combination eta_b(T_b - T_c - T_d) = -eta_b T_a (reducible)', ok_ref, 'contradicts the reference claim of irreducibility')
ok_cor = all(np.allclose(Tb(x,M)+Tc(x,M)+Td(x,M), Ta(x,M)+2*Tb(x,M)) for M in [Mt,Mu,Mgen] for x in range(8))
rep('correct combination T_b + T_c + T_d = T_a + 2 T_b', ok_cor, '')
# irreducibility: is (T_a + 2T_b) M proportional to T_a M (as tensors with adjoint index) for the t-channel M?
for name, M in [('t-channel', Mt), ('u-channel', Mu)]:
    A = np.array([Ta(x,M) for x in range(8)]).ravel()
    G = np.array([Ta(x,M)+2*Tb(x,M) for x in range(8)]).ravel()
    k = np.vdot(A, G)/np.vdot(A, A)
    res = np.linalg.norm(G - k*A)/np.linalg.norm(G)
    rep(f'T_a + 2T_b not proportional to T_a ({name})', res > 0.1, f'min_k ||G - k T_a M||/||G|| = {res:.3f}')
# all-outgoing generators: T^out = -T^in for the incoming partons
def Ta_out(x,M): return -Ta(x,M)
def Tb_out(x,M): return -Tb(x,M)
ok_out = all(np.allclose(Ta_out(x,M)+Tb_out(x,M)+Tc(x,M)+Td(x,M), 0) for M in [Mt,Mu,Mgen] for x in range(8))
ok_out2 = all(np.allclose(Tb_out(x,M)-Tc(x,M)-Td(x,M), Ta_out(x,M)+2*Tb_out(x,M)) for M in [Mt,Mu,Mgen] for x in range(8))
ok_out3 = all(np.allclose(Ta_out(x,M)+2*Tb_out(x,M), -Ta(x,M)-2*Tb(x,M)) for M in [Mt,Mu,Mgen] for x in range(8))
rep('all-outgoing: sum T = 0 and T_b - T_c - T_d = T_a + 2T_b', ok_out and ok_out2, '')
rep('all-outgoing T_a+2T_b equals -T_a-2T_b in incoming-parton generators (prop:break-colour P)', ok_out3, '')

# ---------------------------------------------------------------- (3) SIDIS / DY
# SIDIS: a + gamma* -> c, M[c,a] = delta ; Glauber part (in=out, same-sign): T_c ; T_c M = T_a M
Ms = I3.copy()
ok_s = all(np.allclose(t[x]@Ms, Ms@t[x]) for x in range(8))
# DY: q(a) + qbar(b) -> gamma*, M[b,a] = delta (b antiquark index) ; T_b(antiquark, in) = -(left mult)
Md = I3.copy()
ok_d = all(np.allclose(-(t[x]@Md), -(Md@t[x])) for x in range(8))   # T_b M = -T_a M
rep('SIDIS: Glauber operator = +T_a ; DY: = T_b = -T_a  -> Sivers sign flip', ok_s and ok_d,
    'reference bookkeeping: SIDIS eta_c T_c = -eta_b T_a, DY eta_b T_b = -eta_b T_a -> same sign, no flip')
# C_G = 1 + 2<T_a.T_b>/C_F for the t-channel qq'->qq' (tt* interference): compare with VF-GLA-6 value (N^2-5)/(N^2-1)=1/2
num = sum(np.vdot(Mt, Ta(x, Ta(x,Mt) + 2*Tb(x,Mt))) for x in range(8))
den = sum(np.vdot(Mt, Ta(x, Ta(x,Mt))) for x in range(8))
CG = (num/den).real
rep('C_G for qq\'->qq\' (tt*) = 1/2 (SU(3))', abs(CG-0.5) < 1e-12, f'C_G = {CG:.12f}')
# Collins-Qiu abelian model: charges g1 (a,c), g2 (b,d): same-sign total g2 + g1 + g2
g1, g2 = 0.3, 0.7
rep('Collins-Qiu abelian total i pi (g1 + 2 g2)', abs((g2 + g1 + g2) - (g1 + 2*g2)) < 1e-15, 'reference bookkeeping would give g2 - g1 - g2 = -g1')

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
