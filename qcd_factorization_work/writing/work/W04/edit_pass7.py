# -*- coding: utf-8 -*-
# Pass 7 (writer W04): remove two repetitions in free text (no statement, proof, \uses, status paragraph or box touched).
#  - Sec. 4.2: the Coleman--Norton gap sentence repeats the status paragraph of rem:ir-landau-status.
#  - Sec. 4.3: the description of the three reduced diagrams repeats their captions.
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))

def fix(fn, pairs):
    path = os.path.join(ROOT, fn)
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert s.count(a) == 1, (fn, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)

fix('ch04_p2_cn.tex', [
    ("（\\cref{rem:ir-landau-status}），只有全阶论证的地位：Coleman 与 Norton 原文的证明有缺口，但按 Collins 的分析缺口在证明而不在结论\\cite[第~IV~节]{Collins:2020euz}（预印本）。",
     "（\\cref{rem:ir-landau-status}），只有全阶论证的地位。"),
])
fix('ch04_p3_pinch.tex', [
    ("\\cref{fig:reduced-ee,fig:reduced-dis,fig:reduced-dy}画出三类过程的典型约化图：$e^+e^-$ 的两个末态喷注穿过割线；DIS 的靶共线子图 $A$ 跨越割线，一个物理部分子进入 $H$ 与 $H^\\dagger$，旁观者直接穿过割线；DY 中两个强子的共线子图各分为振幅与共轭振幅两部分，$H$ 由来自 $A$ 的夸克与来自 $B$ 的反夸克湮灭而成。这些图只是钳夹面的骨架；",
     "\\cref{fig:reduced-ee,fig:reduced-dis,fig:reduced-dy}画出三类过程的典型约化图。它们只是钳夹面的骨架；"),
])
print('pass 7 done')
