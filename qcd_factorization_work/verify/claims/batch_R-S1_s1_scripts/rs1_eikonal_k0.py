"""R-S1 independent check: two-gluon exchange between two infinite time-like Wilson lines.

Route (different from R3's x_B residues + PV and from N01's k^- residues + Frullani):
symmetric frame v_A = (ch, sh), v_B = (ch, -sh), ch = cosh(Y/2), sh = sinh(Y/2);
k^0 integral by residues, k^3 integral numerically.
  J_sigma = Int dxA dxB [i/(xA+i0)] [i/(sigma xB+i0)] g,   g = 1/((k^2-a+i0)(k^2-b+i0)),
  dxA dxB = sinh(Y) dk0 dk3.  sigma=-1: box (same ordering on both lines), sigma=+1: crossed.
(1) analytic eps->0 residues (derivation in batch_R-S1_s1.md) -> closed forms;
(2) exact k^0 residues at FINITE eps, numerical k^3, eps -> 0 (tests the delta-term of the 2D pinch);
(3) the integral identity  Int ds /((s^2+c^2) sqrt(1+s^2)) = 2Y/sinh Y,  c = cosh(Y/2);
(4) colour: c_box = X^2, c_cross = X^2 + C_A/2 X with explicit SU(3) matrices (3x3, 3x3bar, 8x3, 8x8);
(5) unitarity in b-space: V = 1 + i chi X + (i chi)^2/2 [X^2 + p_opp C_A/2 X]; V^dag V - 1 at O(chi^2)
    = -1/2 C_A chi^2 Re(p_opp) X; p_opp = J_cross/(J_box+J_cross) = -iY/pi -> 0;  reference's equal split
    p_opp = 1/2 -> -1/4 C_A chi^2 X (its (E.51)); the AMPLITUDE deviation for p_opp=1/2 is -1/8 C_A chi^2 X
    (this is the quantity reader R4 computed).
Run: python3 -I rs1_eikonal_k0.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import mpmath as mp
mp.mp.dps = 25

out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"
    out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- (3) identity
for Y in [0.1, 1.0, 3.7, 8.0]:
    c = mp.cosh(mp.mpf(Y)/2)
    lhs = mp.quad(lambda s: 1/((s**2+c**2)*mp.sqrt(1+s**2)), [-mp.inf, 0, mp.inf])
    rhs = 2*mp.mpf(Y)/mp.sinh(Y)
    rep(f'identity Y={Y}', abs(lhs-rhs) < 1e-18*abs(rhs)+1e-20, f'lhs={mp.nstr(lhs,15)} rhs={mp.nstr(rhs,15)}')

# ---------------------------------------------------------------- (1) eps->0 residues in k0, numerical k3
def J_eps0(a, b, Y, sigma):
    a, b, Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    ch, sh = mp.cosh(Y/2), mp.sinh(Y/2)
    def gluon_part(k3):
        # residues at k0 = -E_a + i0, -E_b + i0 (upper half plane), eikonal product at those points
        Ea, Eb = mp.sqrt(k3**2+a), mp.sqrt(k3**2+b)
        PA = k3**2 + a*ch**2   # (vA.k)(vB.k) at k0=-Ea
        PB = k3**2 + b*ch**2
        # Res g at k0=-Ea: 1/((-2Ea)(a-b)); at -Eb: 1/((-2Eb)(b-a))
        return 2j*mp.pi*(1/((-2*Ea)*(a-b)*PA) + 1/((-2*Eb)*(b-a)*PB))
    G = mp.quad(gluon_part, [-mp.inf, 0, mp.inf])
    if sigma == +1:
        # integrand -g/((vA.k+i0)(vB.k+i0)): both eikonal poles in LHP; close up -> gluon poles only
        val = -G
    else:
        # integrand g/((vA.k+i0)(vB.k-i0)): B-eikonal pole k0=-t k3+i0 in UHP as well
        # residue of 1/(vB.k) is 1/ch ; vA.k there = -2 sh k3 (+i0) ; g there = 1/((k3^2/ch^2+a)(k3^2/ch^2+b))
        # Int dk3 g/( -2 sh k3 + i0) = PV(0, g even) - i pi g(0)/(2 sh)
        eik = 2j*mp.pi*(1/ch)*(-1j*mp.pi/(2*sh*a*b))
        val = G + eik
    return mp.sinh(Y)*val

def closed(a, b, Y):
    a, b, Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    return 2*mp.pi/(a*b)*(mp.pi+1j*Y), -2j*mp.pi*Y/(a*b)

worst = 0
for (a,b,Y) in [(1.0,2.5,1.0),(0.7,0.3,6.0),(2.0,0.1,0.4),(1.3,1.31,2.0),(0.05,7.0,2.2),(3.3,3.0,9.0)]:
    Jb, Jc = J_eps0(a,b,Y,-1), J_eps0(a,b,Y,+1)
    cb, cc = closed(a,b,Y)
    e = max(abs(Jb-cb)/abs(cb), abs(Jc-cc)/abs(cc))
    worst = max(worst, e)
    print(f"  a={a} b={b} Y={Y}: J_box={mp.nstr(Jb,12)} J_cross={mp.nstr(Jc,12)}  p_opp={mp.nstr(Jc/(Jb+Jc),12)} (-iY/pi={mp.nstr(-1j*Y/mp.pi,12)})")
rep('k0-residue route reproduces closed forms', worst < 1e-15, f'max rel dev {mp.nstr(worst,3)}')

# ---------------------------------------------------------------- (2) finite eps: exact k0 residues, numeric k3
def J_fin(a, b, Y, sigma, eps):
    a, b, Y, eps = mp.mpf(a), mp.mpf(b), mp.mpf(Y), mp.mpf(eps)
    ch, sh = mp.cosh(Y/2), mp.sinh(Y/2)
    ie = 1j*eps
    def f(k3):
        # integrand in k0: F(k0) = pref * 1/((ch k0 - sh k3 + ie)(sigma*(ch k0 + sh k3) + ie)) * 1/((k0^2-k3^2-a+ie)(k0^2-k3^2-b+ie))
        # times i*i (eikonal numerators).  Sum residues in UHP (integrand ~ k0^-6).
        pa = -mp.sqrt(k3**2+a-ie); pb = -mp.sqrt(k3**2+b-ie)   # UHP gluon poles
        def F_noPole(k0, which):
            eA = ch*k0 - sh*k3 + ie
            eB = sigma*(ch*k0 + sh*k3) + ie
            ga = (k0**2-k3**2-a+ie); gb = (k0**2-k3**2-b+ie)
            if which == 'a':   # remove factor (k0-pa): ga = (k0-pa)(k0+pa)
                return -1/(eA*eB*(k0+pa)*gb)
            if which == 'b':
                return -1/(eA*eB*ga*(k0+pb))
            if which == 'B':   # eB = sigma*ch*(k0 - k0B)
                return -1/(eA*sigma*ch*ga*gb)
        res = F_noPole(pa,'a') + F_noPole(pb,'b')
        k0A = (sh*k3 - ie)/ch            # A-eikonal pole: always LHP
        k0B = (-sh*k3*sigma - ie)/(sigma*ch)   # B pole: sigma=-1 -> (sh k3 + ... ) check sign below
        if mp.im(k0B) > 0:
            res += F_noPole(k0B,'B')
        return 2j*mp.pi*res
    # k3 integral: sharp structure near k3=0 of width eps
    pts = [-mp.inf, -1, -10*eps, -eps, 0, eps, 10*eps, 1, mp.inf]
    return mp.sinh(Y)*mp.quad(f, pts)

for (a,b,Y) in [(1.0,2.5,1.0),(0.7,0.3,3.0)]:
    cb, cc = closed(a,b,Y)
    for eps in [1e-3, 1e-4, 1e-5]:
        Jb, Jc = J_fin(a,b,Y,-1,eps), J_fin(a,b,Y,+1,eps)
        print(f"  a={a} b={b} Y={Y} eps={eps:g}: J_box={mp.nstr(Jb,10)} (closed {mp.nstr(cb,10)}), J_cross={mp.nstr(Jc,10)} (closed {mp.nstr(cc,10)})")
    rep(f'finite-eps -> closed form (a={a},b={b},Y={Y})', abs(Jb-cb)/abs(cb) < 1e-3 and abs(Jc-cc)/abs(cc) < 1e-3,
        f'rel dev at eps=1e-5: box {mp.nstr(abs(Jb-cb)/abs(cb),3)}, cross {mp.nstr(abs(Jc-cc)/abs(cc),3)}; Re J_cross={mp.nstr(mp.re(Jc),3)}')

# ---------------------------------------------------------------- (4) colour algebra
def gm():
    l = np.zeros((8,3,3), dtype=complex)
    l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1
    l[3][0,2]=l[3][2,0]=1; l[4][0,2]=-1j; l[4][2,0]=1j; l[5][1,2]=l[5][2,1]=1
    l[6][1,2]=-1j; l[6][2,1]=1j; l[7][0,0]=l[7][1,1]=1/np.sqrt(3); l[7][2,2]=-2/np.sqrt(3)
    return l/2
tF = gm()
f = np.zeros((8,8,8))
for a in range(8):
    for b in range(8):
        cm = tF[a]@tF[b]-tF[b]@tF[a]
        for c in range(8):
            f[a,b,c] = np.real(-2j*np.trace(cm@tF[c]))
tA = np.array([-1j*f[a] for a in range(8)])        # adjoint (T^a)_{bc} = -i f^{abc}
tAF = np.array([-tF[a].T for a in range(8)])       # antifundamental
reps = {'3': tF, '3bar': tAF, '8': tA}
CA = 3.0
for (rA, rB) in [('3','3'), ('3','3bar'), ('8','3'), ('8','8')]:
    TA, TB = reps[rA], reps[rB]
    dA, dB = TA.shape[1], TB.shape[1]
    X = sum(np.kron(TA[a], TB[a]) for a in range(8))
    # path ordering: later attachment on the left.  Line A: T^a (later) T^b (earlier).
    cbox = sum(np.kron(TA[a]@TA[b], TB[a]@TB[b]) for a in range(8) for b in range(8))
    ccr  = sum(np.kron(TA[a]@TA[b], TB[b]@TB[a]) for a in range(8) for b in range(8))
    ok = np.allclose(cbox, X@X) and np.allclose(ccr, X@X + CA/2*X)
    rep(f'colour {rA} x {rB}', ok, f'max dev box {np.abs(cbox-X@X).max():.1e}, cross {np.abs(ccr-X@X-CA/2*X).max():.1e}')
    # reference proof of (E.51): sum {T^a,T^b}{T'^a,T'^b} = 4X^2 + C_A X
    S = sum(np.kron(TA[a]@TA[b]+TA[b]@TA[a], TB[a]@TB[b]+TB[b]@TB[a]) for a in range(8) for b in range(8))
    rep(f'(E.51) anticommutator sum {rA} x {rB}', np.allclose(S, 4*X@X + CA*X), '')

    # ---------------------------------------------------------- (5) unitarity bookkeeping
    chi = 0.137
    Id = np.eye(dA*dB)
    for popp, label in [(0.0,'common ordering'), (0.5,'equal split (reference)'), (-1j*2.3/np.pi, 'exact eikonal, Y=2.3'), (1.0,'crossed only')]:
        V = Id + 1j*chi*X + (1j*chi)**2/2*(X@X + popp*CA/2*X)
        R = V.conj().T@V - Id
        pred = -0.5*CA*chi**2*np.real(popp)*X
        # remove O(chi^3), O(chi^4) pieces: compare at second order by finite-difference in chi
        def V2(ch):
            return Id + 1j*ch*X + (1j*ch)**2/2*(X@X + popp*CA/2*X)
        def R2(ch):
            Vv = V2(ch); return Vv.conj().T@Vv - Id
        h = 1e-3
        sec = (R2(h) + R2(-h))/(2*h**2)      # coefficient of chi^2 (odd powers cancel; chi^4 term O(h^2))
        ok = np.allclose(sec, -0.5*CA*np.real(popp)*X, atol=1e-5)
        if rA == '3' and rB == '3':
            rep(f'V^dag V residual coefficient, {label}', ok, f'p_opp={popp}: chi^2-coefficient = -1/2 C_A Re(p_opp) X')
    if rA == '3' and rB == '3':
        dev = (1j*chi)**2/2*(0.5*CA/2*X)
        rep('amplitude deviation for equal split = -1/8 C_A chi^2 X (R4 quantity)', np.allclose(dev, -CA*chi**2/8*X), '')

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
