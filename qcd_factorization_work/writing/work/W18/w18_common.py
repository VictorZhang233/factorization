# -*- coding: utf-8 -*-
"""
w18_common.py -- helpers for the W18 (Ch15, SCET) re-derivation scripts.

Binding conventions (WRITER_SPEC_v2 Sec. 3, CONTEXT.md):
  metric (+,-,-,-); D_mu = d_mu - i g A_mu^a t^a; vertex i g gamma^mu t^a; Tr(t^a t^b) = delta^{ab}/2;
  SCET vectors (Ch15 only): n = (1,0,0,1), nbar = (1,0,0,-1), n.nbar = 2,
  p = nbar.p n/2 + n.p nbar/2 + p_perp,  nbar.p = sqrt2 p^+,  n.p = sqrt2 p^-.
Written independently of research/c_scet (own implementation; same conventions).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np


class Check:
    def __init__(self, title):
        self.title, self.np, self.nf = title, 0, 0
        print('=' * 96); print(title); print('=' * 96)

    def __call__(self, name, ok, detail=''):
        ok = bool(ok)
        if ok:
            self.np += 1
        else:
            self.nf += 1
        print(('[PASS] ' if ok else '[FAIL] ') + name + (('   :: ' + str(detail)) if detail != '' else ''))
        sys.stdout.flush()
        return ok

    def summary(self):
        print('-' * 96); print(f'{self.title}: {self.np} PASS, {self.nf} FAIL'); print('-' * 96)
        return self.nf == 0


# ---------------------------------------------------------------- Dirac algebra (Dirac representation)
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
PAULI = [np.array([[0, 1], [1, 0]], dtype=complex),
         np.array([[0, -1j], [1j, 0]], dtype=complex),
         np.array([[1, 0], [0, -1]], dtype=complex)]
GAM = [np.block([[I2, Z2], [Z2, -I2]])] + [np.block([[Z2, s], [-s, Z2]]) for s in PAULI]
ID4 = np.eye(4, dtype=complex)
METRIC = np.diag([1.0, -1.0, -1.0, -1.0])

NV = np.array([1.0, 0.0, 0.0, 1.0])     # n
NBV = np.array([1.0, 0.0, 0.0, -1.0])   # nbar


def dot(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def slash(v):
    v = np.asarray(v)
    return v[0] * GAM[0] - v[1] * GAM[1] - v[2] * GAM[2] - v[3] * GAM[3]


def bar(u):
    return np.conj(u) @ GAM[0]


NSL, NBSL = slash(NV), slash(NBV)
PN = NSL @ NBSL / 4.0          # P_n  = nslash nbarslash / 4  (xi_n = P_n psi)
PNB = NBSL @ NSL / 4.0         # P_nbar


def perp_part(p):
    """p_perp^mu (only components 1,2)."""
    q = np.zeros(4, dtype=complex); q[1] = p[1]; q[2] = p[2]
    return q


def lc_vec(nbp, np_, pt):
    """p^mu = nbar.p n/2 + n.p nbar/2 + p_perp, pt = (px, py)."""
    return nbp * NV / 2 + np_ * NBV / 2 + np.array([0, pt[0], pt[1], 0])


def massless_spinor(p, chi):
    """an (unnormalized) solution of pslash u = 0 for massless p: u = pslash chi."""
    return slash(p) @ chi


# ---------------------------------------------------------------- SU(3)
def gell_mann():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return l / 2.0


TGEN = gell_mann()


def rand_su3_alg(rng, scale=1.0):
    c = rng.normal(size=8) * scale
    return np.einsum('a,aij->ij', c, TGEN)


def path_ordered(afun, s0, s1, nstep=4000):
    """Solve dW/ds = i a(s) W, W(s0)=1, with a(s) hermitian 3x3 (a = g v.A); later s to the LEFT.
    4th-order Runge-Kutta on the matrix ODE."""
    h = (s1 - s0) / nstep
    W = np.eye(3, dtype=complex)
    s = s0
    for _ in range(nstep):
        k1 = 1j * afun(s) @ W
        k2 = 1j * afun(s + h / 2) @ (W + h / 2 * k1)
        k3 = 1j * afun(s + h / 2) @ (W + h / 2 * k2)
        k4 = 1j * afun(s + h) @ (W + h * k3)
        W = W + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        s += h
    return W
