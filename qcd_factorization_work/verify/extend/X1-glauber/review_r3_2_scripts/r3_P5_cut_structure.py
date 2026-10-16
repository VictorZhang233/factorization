# Round-3 reviewer 2 -- P5: which part of |A^lines|^2 do the three-particle cuts of the direct-line class C produce?
# A cut rung joins line A (one side of the cut) to line B (other side), so class C yields only the A-B interference.
# Eikonal currents J_X = v_X/(v_X.k); Feynman-gauge polarisation sum -g_{mu nu}; metric (+,-,-,-).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(5)
g = np.diag([1., -1., -1., -1.])
dot = lambda a, b: a @ g @ b
for Y, label in [(0.5, 'timelike, Y=0.5'), (3.0, 'timelike, Y=3'), (8.0, 'nearly lightlike, Y=8')]:
    vA = np.array([np.cosh(Y), 0, 0, np.sinh(Y)]); vB = np.array([np.cosh(Y), 0, 0, -np.sinh(Y)])
    rows = []
    for t in range(5):
        n = rng.normal(size=3); n /= np.linalg.norm(n); k = np.concatenate([[1.0], n]) * rng.uniform(0.1, 1)
        JA, JB = vA/dot(vA, k), vB/dot(vB, k)
        full = -dot(JA - JB, JA - JB)          # |A^lines|^2 kinematic factor (gauge invariant: k.(JA-JB)=0)
        cross = 2*dot(JA, JB)                   # class-C three-particle cuts (rung joins A and B): interference only
        selfs = -dot(JA, JA) - dot(JB, JB)      # graphs with the radiated gluon on ONE line (outside C)
        rows.append((full, cross, selfs))
    print(label)
    for full, cross, selfs in rows:
        print(f'   full={full:+.5e}  cross(class C)={cross:+.5e}  self(outside C)={selfs:+.5e}  cross/full={cross/full:.6f}')
