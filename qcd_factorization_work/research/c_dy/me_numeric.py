# -*- coding: utf-8 -*-
"""
me_numeric.py -- independent numerical check (D=4) of the real-emission matrix elements used in nlo_checks.py:
explicit Dirac matrices and spinors, PHYSICAL gluon polarisation vectors (no -g replacement),
photon index contracted with -g_{mu nu}; plus Ward identities q_mu M^mu = 0 and k_alpha M^alpha = 0.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

RES = []
def report(name, ok, extra=''):
    RES.append((name, bool(ok)))
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra))

g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
def gk(s):
    m = np.zeros((4, 4), dtype=complex); m[:2, 2:] = s; m[2:, :2] = -s; return m
GAM = [g0, gk(sx), gk(sy), gk(sz)]
MET = np.diag([1., -1., -1., -1.])
def slash(p): return sum(MET[m, m] * p[m] * GAM[m] for m in range(4))
def mdot(a, b): return a @ MET @ b
def u_sp(p):
    E = p[0]; S = p[1] * sx + p[2] * sy + p[3] * sz
    return [np.concatenate([np.sqrt(E) * c, S @ c / np.sqrt(E)]) for c in (np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex))]
def v_sp(p):
    E = p[0]; S = p[1] * sx + p[2] * sy + p[3] * sz
    return [np.concatenate([S @ c / np.sqrt(E), np.sqrt(E) * c]) for c in (np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex))]
bar = lambda w: w.conj() @ g0
def pols(k):
    """two physical (transverse) polarisation 4-vectors for massless k (contravariant components)."""
    n = k[1:] / np.linalg.norm(k[1:])
    a = np.array([1.0, 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(n, a); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    return [np.array([0, *e1]), np.array([0, *e2])]
def rotate(p, R): return np.array([p[0], *(R @ p[1:])])

rng = np.random.default_rng(11)
def random_rotation():
    A = rng.normal(size=(3, 3)); Qm, _ = np.linalg.qr(A); return Qm * np.sign(np.linalg.det(Qm))

def kin(shat, Q2, cth):
    """partonic cm frame: p1 along +z, p2 along -z; massless final parton k at angle theta, gamma* recoils."""
    E = np.sqrt(shat) / 2
    p1 = np.array([E, 0, 0, E]); p2 = np.array([E, 0, 0, -E])
    kk = (shat - Q2) / (2 * np.sqrt(shat)); sth = np.sqrt(1 - cth**2)
    k = np.array([kk, kk * sth * np.cos(0.7), kk * sth * np.sin(0.7), kk * cth])
    return p1, p2, k

worst = 0; worst_qg = 0; ward = 0
for trial in range(6):
    shat = rng.uniform(5, 50); z = rng.uniform(0.05, 0.95); Q2 = z * shat; cth = rng.uniform(-0.95, 0.95)
    p1, p2, k = kin(shat, Q2, cth)
    R = random_rotation(); p1, p2, k = rotate(p1, R), rotate(p2, R), rotate(k, R)
    q = p1 + p2 - k
    # ---- q(p1) qbar(p2) -> gamma*(q) g(k)
    t = mdot(p1 - k, p1 - k); u = mdot(p2 - k, p2 - k)
    tot = 0
    for up in u_sp(p1):
        for vb in v_sp(p2):
            for eps_ in pols(k):
                es = slash(eps_.conj())
                Mmu = np.array([bar(vb) @ (GAM[m] @ slash(p1 - k) @ es / t + es @ slash(k - p2) @ GAM[m] / u) @ up for m in range(4)])
                tot += -mdot(Mmu, Mmu.conj()).real
                ward = max(ward, abs(mdot(q, Mmu)))
            # gluon Ward identity: replace eps by k
            ks = slash(k)
            for m in range(4):
                val = bar(vb) @ (GAM[m] @ slash(p1 - k) @ ks / t + ks @ slash(k - p2) @ GAM[m] / u) @ up
                ward = max(ward, abs(val))
    Tan = 8 * ((u / t + t / u) + 2 * shat * Q2 / (t * u))
    worst = max(worst, abs(tot / Tan - 1))
    # ---- q(p1) g(p2) -> gamma*(q) q(k): reuse kinematics with p2 = gluon
    s_ = shat; tq = mdot(p2 - k, p2 - k); uq = mdot(p1 - k, p1 - k)
    tot2 = 0
    for up in u_sp(p1):
        for uk in u_sp(k):
            for eps_ in pols(p2):
                es = slash(eps_)
                Mmu = np.array([bar(uk) @ (GAM[m] @ slash(p1 + p2) @ es / s_ + es @ slash(k - p2) @ GAM[m] / tq) @ up for m in range(4)])
                tot2 += -mdot(Mmu, Mmu.conj()).real
                ward = max(ward, abs(mdot(q, Mmu)))
    Tan2 = -8 * ((s_ / tq + tq / s_) + 2 * uq * Q2 / (s_ * tq))
    worst_qg = max(worst_qg, abs(tot2 / Tan2 - 1))
report('q qbar -> gamma* g: explicit spinors + physical gluon polarisations = 8[(u/t+t/u)+2sQ^2/(tu)]  (6 random points)', worst < 1e-10, '(max rel. dev. %.1e)' % worst)
report('q g -> gamma* q:    explicit spinors + physical gluon polarisations = -8[(s/t+t/s)+2uQ^2/(st)]  (6 random points)', worst_qg < 1e-10, '(max rel. dev. %.1e)' % worst_qg)
report('Ward identities q_mu M^mu = 0 (both channels) and k_alpha M^{mu alpha} = 0 (q qbar channel)', ward < 1e-9, '(max |.| = %.1e)' % ward)
print()
print('SUMMARY me_numeric: %d/%d PASS' % (sum(ok for _, ok in RES), len(RES)))
