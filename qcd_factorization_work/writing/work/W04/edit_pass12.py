# -*- coding: utf-8 -*-
# Pass 12 (writer W04): citation location precision (claim E15 printable version: ELOP p. 48 "content with
# plausibility arguments", p. 50 "requires homology theory").
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))
fn = os.path.join(ROOT, 'ch04_p1_landau.tex')
s = open(fn, encoding='utf-8').read()
a = "ELOP 在推导前声明只满足于似然性论证，并称严格的处理需要同调论\\cite[第~2.1~节，第~48~页]{EdenEtAl1966}"
assert s.count(a) == 1, 'anchor'
s = s.replace(a, "ELOP 在推导前声明只满足于似然性论证，并称严格处理需用同调论\\cite[第~2.1~节，第~48、50~页]{EdenEtAl1966}")
open(fn, 'w', encoding='utf-8').write(s)
print('pass 12 done')
