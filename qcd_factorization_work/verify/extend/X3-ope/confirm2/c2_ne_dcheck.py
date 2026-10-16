#!/usr/bin/env python3
"""
Diagnostic for c2_ne_exact_rank.py: repeat the rank test in dimension D=2k (metric diag(1^k,(-1)^k)),
with a rational null z built from a rational orthogonal matrix (Cayley transform).
If a deficiency found at D=4 persists for large D, it is not a D=4-only relation.
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from fractions import Fraction
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c2_ne_lib.py')).read())

for (n, S, rp) in [(4, 5, 1), (5, 6, 1), (6, 7, 1), (6, 7, 3), (7, 8, 3), (5, 6, 3)]:
    for D in [4, 6, 8, 10, 12, 16]:
        ns, rk = test_D(n, S, rp, D)
        print(f"n={n} S={S} r'={rp} D={D}: #struct={ns} rank={rk} {'FULL' if rk==ns else 'deficiency '+str(ns-rk)}", flush=True)
    print()
