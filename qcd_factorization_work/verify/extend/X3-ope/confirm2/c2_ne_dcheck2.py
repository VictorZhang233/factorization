#!/usr/bin/env python3
"""Diagnostic 2: same as c2_ne_dcheck.py but with npts = #structures + 10 points (each point gives at least one
independent functional per 'Dirac-carrier family'), to remove the sampling artefact of the first run."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c2_ne_lib.py')).read())
for (n, S, rp) in [(4, 5, 1), (5, 6, 1), (6, 7, 1), (7, 8, 1), (5, 6, 3), (6, 7, 3), (7, 8, 3)]:
    for D in [4, 6, 8, 12]:
        st = structures(n, S, rp); ns = len(st)
        rows = eval_rows(st, n, S, rp, D, ns + 10)
        rk = rank_mod_p(rows)
        print(f"n={n} S={S} r'={rp} D={D}: #struct={ns} rank={rk} {'FULL' if rk==ns else 'deficiency '+str(ns-rk)}", flush=True)
    print()
