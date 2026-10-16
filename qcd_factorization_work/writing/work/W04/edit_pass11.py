# -*- coding: utf-8 -*-
# Pass 11 (writer W04): restore the precision of the chapter summary ("not equivalent at the level of pinches";
# the two sets of equations are algebraically equivalent by lem:ir-envelope).
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))
fn = os.path.join(ROOT, 'ch04_p7_regions.tex')
s = open(fn, encoding='utf-8').read()
a = "二者都在微扰论中严格成立，但并不等价。"
assert s.count(a) == 1
s = s.replace(a, "二者都在微扰论中严格成立，但在钳夹层次上并不等价。")
open(fn, 'w', encoding='utf-8').write(s)
print('pass 11 done')
