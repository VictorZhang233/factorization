# -*- coding: utf-8 -*-
# Pass 8 (writer W04): float placement only (after pass 7 shifted the text).
# Move the verbatim fig:momentum-regions block back in front of def:ir-scalings, so that it is met near the top
# of the page that starts with the end of the eq:ir-pgeneric paragraph.
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))
fn = os.path.join(ROOT, 'ch04_p4_power.tex')
s = open(fn, encoding='utf-8').read()
b0 = s.index('%%% BEGIN fig:momentum-regions')
b1 = s.index('%%% END fig:momentum-regions') + len('%%% END fig:momentum-regions')
block = s[b0:b1]
rest = s[:b0].rstrip('\n') + '\n\n' + s[b1:].lstrip('\n')
anchor = '\\begin{definition}[区域标度]\\label{def:ir-scalings}'
i = rest.index(anchor)
new = rest[:i] + block + '\n\n' + rest[i:]
assert new.count('%%% BEGIN fig:momentum-regions') == 1
open(fn, 'w', encoding='utf-8').write(new)
print('pass 8 done')
