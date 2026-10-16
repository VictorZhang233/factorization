# -*- coding: utf-8 -*-
# Pass 5 (writer W04): remove printed internal planning labels (critic items C/O, misconception numbers M#);
# keep them as % comments for traceability.
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parts'))

def fix(fn, pairs):
    path = os.path.join(ROOT, fn)
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (fn, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)

fix('ch04_p1_landau.tex', [
    ("于是有两个不同的问题（critic O12）：", "于是有两个不同的问题：%\n% (critic O12)\n"),
    ("“欧氏区没有 Landau 解，所以欧氏 Green 函数红外有限”的前半句是错的（误解 M29）。",
     "“欧氏区没有 Landau 解，所以欧氏 Green 函数红外有限”的前半句是错的。%\n% (misconception M29)\n"),
])
fix('ch04_p2_cn.tex', [
    ("那里的论据是谱支撑与因果性（critic C15；第~7~章）。", "那里的论据是谱支撑与因果性（第~7~章）。%\n% (critic C15)\n"),
])
fix('ch04_p5_glauber.tex', [
    ("并未离开 Glauber 区（误解 M31）；", "并未离开 Glauber 区；%\n% (misconception M31)\n"),
])
fix('ch04_p6_cancel.tex', [
    ("更重要的是物理上的限制（误解 M8）：", "更重要的是物理上的限制：%\n% (misconception M8)\n"),
    ("红外安全只处理末态奇异性（误解 M9）：", "红外安全只处理末态奇异性：%\n% (misconception M9, first statement)\n"),
])
fix('ch04_p7_regions.tex', [
    ("在 Minkowski 运动学中是循环论证（critic C5）。", "在 Minkowski 运动学中是循环论证。%\n% (critic C5)\n"),
    ("所以欧氏 Green 函数红外有限。”}（M29）", "所以欧氏 Green 函数红外有限。”}"),
    ("\\textbf{“Landau 方程给出奇异性。”}（M20，O12）", "\\textbf{“Landau 方程给出奇异性。”}"),
    ("\\textbf{“Coleman--Norton 图像说明这里没有奇异性。”}（C15）", "\\textbf{“Coleman--Norton 图像说明这里没有奇异性。”}"),
    ("\\textbf{“KLN 定理解释了强子对撞截面为何有限。”}（M8）", "\\textbf{“KLN 定理解释了强子对撞截面为何有限。”}"),
    ("\\textbf{“红外安全保证了因子化。”}（M9）", "\\textbf{“红外安全保证了因子化。”}"),
    ("\\textbf{“区域方法是定理”“可以用它确定领头区域。”}（M19，O11，C5）", "\\textbf{“区域方法是定理”“可以用它确定领头区域。”}"),
    ("\\begin{tcolorbox}[enhanced,breakable,title=常见误解,", "% misconception box: M29; M20 + critic O12; critic C15; M8; M9 (first statement); M19 + critic O11 + critic C5\n\\begin{tcolorbox}[enhanced,breakable,title=常见误解,"),
])
print('pass 5 done')
