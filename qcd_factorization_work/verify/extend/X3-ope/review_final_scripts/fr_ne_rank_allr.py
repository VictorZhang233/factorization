"""Variant of fr_ne_rank.py: quark sectors with all Dirac ranks r = 0..4 (chirality not assumed)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import fr_ne_rank as F
ok = True
for minus in (False, True):
    for n in (2, 3, 4, 5):
        for (nm_, nA) in [("qq", 0), ("qqA", 1), ("qqAA", 2)]:
            if n == 5 and nA >= 1: continue
            d = n + 2; K = d - 3 - nA
            if K < 0: continue
            base = {'z': n}
            if minus: base['w1'] = 1; base['w2'] = 1
            for i in range(nA): base['e%d' % i] = 1
            tot = 0; defic = 0; nmult = 0
            for comp in F.compositions(K, 2 + nA):
                deg = dict(base)
                for i, c in enumerate(comp): deg['p%d' % i] = c
                monos = F.monomials(deg, (0, 1, 2, 3, 4))
                if not monos: continue
                ns = F.nsamples(monos, True)
                r4, _ = F.rank(F.evaluate(monos, deg, 4, ns, True))
                r10, _ = F.rank(F.evaluate(monos, deg, 10, ns, True))
                if r10 != len(monos): print("  proxy deficient", nm_, n, comp, len(monos), r10)
                tot += len(monos); defic += len(monos) - r4; nmult += 1
            ok &= defic == 0
            print("  B^%s_%d %-5s all ranks 0..4: multidegrees=%2d monomials=%4d D=4 deficiency=%d" % ('-' if minus else '+', n, nm_, nmult, tot, defic))
print("RESULT:", "PASS" if ok else "FAIL")
