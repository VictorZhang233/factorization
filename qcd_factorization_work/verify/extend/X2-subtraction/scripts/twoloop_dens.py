"""X2 / twoloop_dens.py -- fibered densities (k1^-, k2^- integrated by residues) of the two-loop planar vertex and of any
zeroing pattern (approximated integrand).  Normalisation: each loop int d^4k/(i pi^2); propagators 1/(-q^2 - i0).
Base point: k1p, k2p (plus components), k1T, k2T (2-vectors given as |k1T|, |k2T|, relative angle phi).
rho(base) = (1/(i pi^2))^2 * int dk1^- dk2^-  prod_lines 1/D_line   ->   I = int dk1p dk2p d^2k1T d^2k2T rho.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lcpt import Factor, iterated_residue

LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
# line momentum = c0 + c1*k1 + c2*k2 ; c0 in {0, p1, p2}
LINE_DEF = {'g1': (None, 1, 0), 'g2': (None, 0, 1), 'a1': ('p1', 0, -1), 'a2': ('p1', -1, -1),
            'b1': ('p2', 0, 1), 'b2': ('p2', 1, 1)}
WEIGHTS = {'g1': 0.913, 'g2': 1.071, 'a1': 1.237, 'a2': 0.811, 'b1': 1.153, 'b2': 0.977}

class Kin:
    def __init__(self, P, Pp, m2):
        self.P, self.Pp, self.m2 = P, Pp, m2
        self.p1m = -m2/(2*P); self.p2p = m2/(2*Pp)

def line_factor(line, Zset, kin, k1p, k2p, k1T, k2T, cosphi):
    """factor -V^2 with V = c0 + c1 k1 + c2 k2 after zeroing coordinates in Zset.
    -V^2 = -2 V^+ V^- + |V_T|^2 ; V^- linear in k1^-, k2^-."""
    c0, c1, c2 = LINE_DEF[line]
    zM = 'M' in Zset
    k1p_e = 0.0 if 'k1+' in Zset else k1p
    k2p_e = 0.0 if 'k2+' in Zset else k2p
    d1 = 0.0 if 'k1-' in Zset else 1.0
    d2 = 0.0 if 'k2-' in Zset else 1.0
    t1 = 0.0 if 'k1T' in Zset else 1.0
    t2 = 0.0 if 'k2T' in Zset else 1.0
    if c0 == 'p1':
        c0p, c0m = kin.P, (0.0 if zM else kin.p1m)
    elif c0 == 'p2':
        c0p, c0m = (0.0 if zM else kin.p2p), -kin.Pp
    else:
        c0p, c0m = 0.0, 0.0
    Vp = c0p + c1*k1p_e + c2*k2p_e
    # |V_T|^2 with V_T = c1 t1 k1T + c2 t2 k2T
    VT2 = (c1*t1*k1T)**2 + (c2*t2*k2T)**2 + 2*c1*c2*t1*t2*k1T*k2T*cosphi
    a = -2*Vp*c0m + VT2
    b1 = -2*Vp*c1*d1 + 0*k1p
    b2 = -2*Vp*c2*d2 + 0*k1p
    return Factor(a + 0*k1p, [b1, b2], WEIGHTS[line])

def density(pattern, kin, k1p, k2p, k1T, k2T, cosphi):
    """pattern: dict line -> set of zeroed coordinates.  Returns rho (real array)."""
    facs = [line_factor(l, set(pattern.get(l, ())), kin, k1p, k2p, k1T, k2T, cosphi) for l in LINES]
    val = iterated_residue(facs, 2, order=[0, 1])
    return np.real(val / (1j*np.pi**2)**2)
