# -*- coding: utf-8 -*-
# Pass 6 (writer W04): float placement only.
# fig:momentum-regions (about 0.6 page) was deferred to a float page of its own (about 0.4 page white space).
# Move its (verbatim, unchanged) block after the paragraph that cites it, so that it is met at the top of a
# text page and can be placed there as a top float.
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))
fn = os.path.join(ROOT, 'ch04_p4_power.tex')
s = open(fn, encoding='utf-8').read()
b0 = s.index('%%% BEGIN fig:momentum-regions')
b1 = s.index('%%% END fig:momentum-regions') + len('%%% END fig:momentum-regions')
block = s[b0:b1]
# remove the block together with one following newline
rest = s[:b0] + s[b1:].lstrip('\n')
anchor = '\\paragraph{两种单位。}'
i = rest.index(anchor)
new = rest[:i] + block + '\n\n' + rest[i:]
assert new.count('%%% BEGIN fig:momentum-regions') == 1
open(fn, 'w', encoding='utf-8').write(new)
print('pass 6 done')
