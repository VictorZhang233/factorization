# -*- coding: utf-8 -*-
# Pass 9 (writer W04): tighten free text after the power-counting table (no statement, proof, \uses or box touched);
# reword one parenthesis of a status paragraph that read as a citation instruction (all its citations are kept,
# the attribution follows FINAL_OUTLINE_v2 Ch4: the off-shell Sudakov regions example is cited from
# BecherBroggioFerroglia2015 Sec. 2.2, massive exchange Sec. 2.3 and Jantzen2011 Sec. 6).
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))

def fix(fn, pairs):
    path = os.path.join(ROOT, fn)
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert s.count(a) == 1, (fn, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)

fix('ch04_p4_power.tex', [
    ("下面三个例子把上述一般陈述落实到最简单的图上。\n\n", ""),
])
fix('ch04_p6_cancel.tex', [
    ("物理截面必须使之相消，或把它们吸收进可测量的长程因子。下面依次讨论 QED 的 Bloch--Nordsieck 定理（对不可分辨的软光子求和）、KLN 定理（对简并态求和）、非阿贝尔理论中有色初态的反例，以及红外安全的概念。",
     "物理截面必须使之相消（对不可分辨的软光子或简并态求和），或把它们吸收进可测量的长程因子。"),
])
fix('ch04_p7_regions.tex', [
    ("前几节从钳夹面出发确定区域：先由 Landau 方程与 Coleman--Norton 图像找出可能的长程敏感性，再由幂次计数挑出领头的部分。",
     "前几节由钳夹分析与幂次计数确定领头区域。"),
    ("（第~5~章的\\cref{ex:sudakov-offshell}；该例应引用\\cite[第~2.2~节]{BecherBroggioFerroglia2015}，有质量交换的情形见其第~2.3~节与\\cite[第~6~节]{Jantzen2011}，而不是\\cite{BenekeSmirnov1998}——后者是为阈值展开引入该方法的）",
     "（第~5~章的\\cref{ex:sudakov-offshell}；其区域分析见\\cite[第~2.2~节]{BecherBroggioFerroglia2015}，有质量交换的情形见其第~2.3~节与\\cite[第~6~节]{Jantzen2011}）"),
])
print('pass 9 done')
