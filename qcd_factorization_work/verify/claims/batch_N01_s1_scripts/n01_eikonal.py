# Independent check of N01 (two-gluon exchange between two infinite time-like Wilson lines).
# Route: light-cone variables, exact k^- residues at FINITE eps, numerical k^+ integral, eps -> 0 extrapolation.
# v_A = (e^{Y/2}, e^{-Y/2})/sqrt2 in (+,-) components, v_B = (e^{-Y/2}, e^{Y/2})/sqrt2; v_A.v_B = cosh Y.
# Normalization of refdoc/work_R3/scripts/eikonal_box.py:
#   J_box   = int dxA dxB [i/(xA+i0)][i/(-xB+i0)] g,  J_cross = int dxA dxB [i/(xA+i0)][i/(xB+i0)] g,
#   g = 1/((k_par^2-a+i0)(k_par^2-b+i0)), xA = v_A.k, xB = v_B.k, dxA dxB = sinh(Y) dk^+ dk^-.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
mp.mp.dps = 30
s2 = mp.sqrt(2)

def inner(kp, a, b, Y, eps, kind):
    """int dk^- of 1/[D_A D_B D_a D_b] (no i factors), exact residues, finite eps.
       D_A = v_A.k + i eps; D_B = -v_B.k + i eps (box) or v_B.k + i eps (cross); D_a = 2k+k- - a + i eps."""
    eY2 = mp.e**(Y/2); emY2 = mp.e**(-Y/2)
    # linear factors in k^-:  D = c*(k^- - r)
    facs = []
    facs.append((eY2/s2, -mp.e**(-Y)*kp - 1j*s2*emY2*eps))              # D_A
    if kind == 'box':
        facs.append((-emY2/s2, -mp.e**(Y)*kp + 1j*s2*eY2*eps))         # D_B = -(e^{-Y/2}k^- + e^{Y/2}k^+)/s2 + i eps
    else:
        facs.append((emY2/s2, -mp.e**(Y)*kp - 1j*s2*eY2*eps))          # D_B' = (e^{-Y/2}k^- + e^{Y/2}k^+)/s2 + i eps
    facs.append((2*kp, (a - 1j*eps)/(2*kp)))                            # D_a
    facs.append((2*kp, (b - 1j*eps)/(2*kp)))                            # D_b
    tot = 0
    for i, (ci, ri) in enumerate(facs):
        if mp.im(ri) > 0:                                               # close in the UHP
            val = 1/ci
            for j, (cj, rj) in enumerate(facs):
                if j != i:
                    val /= cj*(ri - rj)
            tot += val
    return 2j*mp.pi*tot

def J(a, b, Y, eps, kind):
    a, b, Y, eps = mp.mpf(a), mp.mpf(b), mp.mpf(Y), mp.mpf(eps)
    f = lambda kp: inner(kp, a, b, Y, eps, kind)
    sc = [mp.mpf(10)**k for k in range(-8, 5)]
    pts = sorted([-x for x in sc] + [mp.mpf(0)] + sc)
    pts = [-mp.inf] + pts + [mp.inf]
    val = mp.quad(f, pts)
    return (1j*1j)*mp.sinh(Y)*val                                       # i*i from the eikonal Feynman rules, measure

worst = 0
for (a, b, Y) in [(1.0, 2.5, 1.0), (0.7, 0.3, 3.0), (2.0, 0.1, 0.4)]:
    cb = 2*mp.pi/(a*b)*(mp.pi + 1j*Y); cc = -2*mp.pi/(a*b)*1j*Y
    rows = []
    for eps in [1e-3, 1e-4, 1e-5, 1e-6]:
        jb = J(a, b, Y, eps, 'box'); jc = J(a, b, Y, eps, 'cross')
        rows.append((eps, jb, jc))
        print(f"a={a} b={b} Y={Y} eps={eps:.0e}: J_box={mp.nstr(jb,10)}  J_cross={mp.nstr(jc,10)}")
    # Richardson-type check: deviation should shrink ~ eps*log(eps)
    eps, jb, jc = rows[-1]
    e = max(abs(jb - cb)/abs(cb), abs(jc - cc)/abs(cc))
    worst = max(worst, e)
    print(f"   closed form: J_box={mp.nstr(cb,10)}  J_cross={mp.nstr(cc,10)};  rel.dev at eps=1e-6: {mp.nstr(e,3)}")
print("worst relative deviation at eps=1e-6:", mp.nstr(worst, 3))

# ---------------- colour algebra with explicit SU(3) generators ----------------
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0,1]=lam[0][1,0]=1
lam[1][0,1]=-1j; lam[1][1,0]=1j
lam[2][0,0]=1; lam[2][1,1]=-1
lam[3][0,2]=lam[3][2,0]=1
lam[4][0,2]=-1j; lam[4][2,0]=1j
lam[5][1,2]=lam[5][2,1]=1
lam[6][1,2]=-1j; lam[6][2,1]=1j
lam[7]=np.diag([1,1,-2])/np.sqrt(3)
tF = lam/2
tAF = -np.conj(tF)                       # antifundamental generators -t^{a*}
# adjoint (T^a)_{bc} = -i f^{abc}
f = np.zeros((8,8,8))
for A_ in range(8):
    for B_ in range(8):
        comm = tF[A_]@tF[B_] - tF[B_]@tF[A_]
        for C_ in range(8):
            f[A_,B_,C_] = np.real(-2j*np.trace(comm@tF[C_]))
tAd = np.array([-1j*f[A_] for A_ in range(8)])
def check(TA, TB, name):
    dA = TA.shape[1]; dB = TB.shape[1]
    I_A = np.eye(dA); I_B = np.eye(dB)
    X = sum(np.kron(TA[c], TB[c]) for c in range(8))
    # path ordering: later attachment to the left; box: same order on both lines; cross: opposite
    cbox = sum(np.kron(TA[b_]@TA[a_], TB[b_]@TB[a_]) for a_ in range(8) for b_ in range(8))
    ccross = sum(np.kron(TA[b_]@TA[a_], TB[a_]@TB[b_]) for a_ in range(8) for b_ in range(8))
    CA = 3
    e1 = np.max(np.abs(cbox - X@X)); e2 = np.max(np.abs(ccross - (X@X + CA/2*X)))
    print(f"colour [{name}]: |c_box - X^2| = {e1:.1e},  |c_cross - (X^2 + C_A/2 X)| = {e2:.1e}")
check(tF, tF, "3 x 3"); check(tF, tAF, "3 x 3bar"); check(tAd, tF, "8 x 3"); check(tAd, tAd, "8 x 8")
