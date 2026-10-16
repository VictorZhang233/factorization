# -*- coding: utf-8 -*-
# Third (small) trimming pass on Ch08 parts: prose only.
import os, glob
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')
files = sorted(glob.glob(os.path.join(here, 'ch08_p*.tex')))
texts = {f: open(f, encoding='utf-8').read() for f in files}

def rep(old, new):
    hits = [f for f in files if old in texts[f]]
    if len(hits) != 1 or texts[hits[0]].count(old) != 1:
        raise SystemExit('match problem for: %s' % old[:70])
    texts[hits[0]] = texts[hits[0]].replace(old, new)

# free-field example: keep plane-wave values, antiquark sign, moments in one line
rep(r"""各自由分布的矩为 $1$、$(-1)^n$、$1+(-1)^n$；定域算符在同样的态中给出 $\langle p|\bar\psi\gamma^+(\ii\partial^+)^{n-1}\psi|p\rangle=2(p^+)^n$，反夸克 $-\bar v\gamma^+v(-p^+)^{n-1}=(-1)^n2(p^+)^n$，胶子 $\sum_j\langle k|G^{+j}(\ii\partial^+)^{n-2}G^{+j}|k\rangle=[1+(-1)^n](k^+)^n$——除以 $2(p^+)^n$ 后与矩逐一相等，这是\cref{thm:pdf-moments-local}在自由场上的特例；""",
r"""各自由分布的矩 $1$、$(-1)^n$、$1+(-1)^n$ 与定域算符 $\bar\psi\gamma^+(\ii\partial^+)^{n-1}\psi$、$\sum_jG^{+j}(\ii\partial^+)^{n-2}G^{+j}$ 在同样态中的值除以 $2(p^+)^n$ 逐一相等（\cref{thm:pdf-moments-local}的自由场特例）；""")

# misconception box: merge the two positivity items (C13 kept explicitly)
rep(r"""\item 「PDF 是概率密度，故 $\MSbar$ PDF 为正。」——数密度只对裸的截断量成立（\cref{rem:pdf-number-density}）；$\MSbar$ 正定性是猜想，在所有标度上非负是错的（\cref{conj:pdf-positivity}）。
\item 「领头阶演化保持正定性，故 $\MSbar$ PDF 为正。」——循环论证：初始条件的正定性正是问题所在。""",
r"""\item 「PDF 是概率密度，故 $\MSbar$ PDF 为正」或「领头阶演化保持正定性，故 $\MSbar$ PDF 为正」。——数密度只对裸的截断量成立（\cref{rem:pdf-number-density}）；后一说法是循环论证，初始条件的正定性正是问题所在；$\MSbar$ 正定性是猜想，在所有标度上非负是错的（\cref{conj:pdf-positivity}）。""")

# transversity paragraph
rep(r"""横度分布是手征奇的，单举 DIS 中不出现，测量它需要另一个手征奇的对象，例如横向极化 Drell--Yan 中另一个强子的横度分布\cite{RalstonSoper1979,JaffeJi1991,JaffeJi1992}；对自旋 $\frac12$ 的靶不存在胶子横度分布（胶子的螺旋度翻转改变两个单位）。极化分布的过程、演化（次领头阶核见\cite{MertigVanNeerven1996,Vogelsang1996}）与因子化定理见第~11~章。""",
r"""横度分布是手征奇的，单举 DIS 中不出现，需要另一个手征奇的对象才能测量（如横向极化 Drell--Yan\cite{RalstonSoper1979,JaffeJi1991,JaffeJi1992}）；自旋 $\frac12$ 的靶没有胶子横度分布。极化分布的演化（次领头阶核见\cite{MertigVanNeerven1996,Vogelsang1996}）与因子化见第~11~章。""")

# chapter summary
rep(r"""PDF 与碎裂函数在任何因子化定理之前就有了精确的算符定义。PDF 的矩是扭度 2 定域算符的矩阵元，其重整化核的矩恰为定域算符的重整化常数（\cref{app:appL}）；DGLAP 由算符重整化得出，Feynman 规范中带 Wilson 线的单圈计算与定域算符的单圈计算逐图对应；求和规则来自守恒流；DIS 扭度 2 部分的 $x$ 空间因子化以 OPE 为前提而严格。碎裂函数的全阶演化需要独立的乘法可重整性输入，$\MSbar$ PDF 的正定性只是猜想。第~9~章起，这些分布将作为因子化定理中的长距离因子出现。""",
r"""PDF 与碎裂函数在任何因子化定理之前就有了精确的算符定义：PDF 的矩是扭度 2 定域算符的矩阵元（\cref{app:appL}），DGLAP 由算符重整化得出，求和规则来自守恒流，DIS 扭度 2 部分的 $x$ 空间因子化以 OPE 为前提而严格；碎裂函数的全阶演化需要独立的乘法可重整性输入，$\MSbar$ PDF 的正定性只是猜想。第~9~章起，这些分布作为因子化定理中的长距离因子出现。""")

for f in files:
    open(f, 'w', encoding='utf-8').write(texts[f])
print('trim3 ok')
