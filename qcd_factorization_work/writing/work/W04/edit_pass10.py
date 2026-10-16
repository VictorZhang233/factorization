# -*- coding: utf-8 -*-
# Pass 10 (writer W04): tighten the closing free text so that Ch4 does not spill four lines onto an extra page
# (no statement, proof, \uses, status paragraph or box touched; the summary keeps every claim and every tag).
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))

def fix(fn, pairs):
    path = os.path.join(ROOT, fn)
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert s.count(a) == 1, (fn, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)

fix('ch04_p6_cancel.tex', [
    ("最后给出可以在微扰论中逐阶计算的末态可观测量的精确定义。\n\n", ""),
])
fix('ch04_p7_regions.tex', [
    ("参数形式的 Landau 条件控制外部不变量的解析性与红外有限性，二者都在重整化微扰论中严格成立，但在钳夹的层次上并不等价。Coleman--Norton 图像把钳夹面翻译为经典过程，给出硬--喷注--软的约化图（\\tagA）；幂次计数给出其超表观度（严格的标度陈述），在 Feynman 规范中挑出",
     "参数形式的 Landau 条件控制外部不变量的解析性与红外有限性；二者都在微扰论中严格成立，但并不等价。Coleman--Norton 图像给出硬--喷注--软的约化图（\\tagA）；幂次计数（严格的标度陈述）在 Feynman 规范中挑出"),
    ("建立在\\cref{rem:ir-euclid-corners}与红外幂次计数之上；", "建立在\\cref{rem:ir-euclid-corners}之上；"),
])
print('pass 10 done')
