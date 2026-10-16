# -*- coding: utf-8 -*-
# Pass 3 (writer W04): move verbatim figure blocks earlier in their sections so that floats share pages with text;
# a few further compressions of running text.  Figure blocks themselves are not modified.
def load(fn):
    return open('parts/' + fn, encoding='utf-8').read()

def save(fn, s):
    open('parts/' + fn, 'w', encoding='utf-8').write(s)

def extract(s, label):
    b = '%%%% BEGIN %s\n' % label
    e = '%%%% END %s\n' % label
    i = s.index(b)
    j = s.index(e, i) + len(e)
    return s[:i] + s[j:], s[i:j]

# ------------------------------------------------------------------ sec:ir-pinch: reduced diagrams right after the first paragraph
s = load('ch04_p3_pinch.tex')
s, fee = extract(s, 'fig:reduced-ee')
s, fdis = extract(s, 'fig:reduced-dis')
s, fdy = extract(s, 'fig:reduced-dy')
anchor = '对一般的图，Coleman--Norton 图像给出同样简单的结构。'
i = s.index(anchor)
s = s[:i] + fee + '\n' + fdis + '\n' + fdy + '\n' + s[i:]
save('ch04_p3_pinch.tex', s)

# ------------------------------------------------------------------ sec:ir-power: mode-exponent figure after the units paragraph
s = load('ch04_p4_power.tex')
s, fmode = extract(s, 'fig:ir-mode-exponents')
anchor = '\\begin{proposition}[超表观红外发散度 \\tagR]'
i = s.index(anchor)
s = s[:i] + fmode + '\n' + s[i:]
save('ch04_p4_power.tex', s)

# ------------------------------------------------------------------ sec:ir-landau: principle paragraph compressed
s = load('ch04_p1_landau.tex')
a = s.index('由此得到原则：')
b = s.index('\\paragraph{Feynman 参数表示。}')
s = s[:a] + ('由此得到原则：这类积分作为外部参数的函数，只有在围道被奇点从两侧夹住（钳夹，pinch）或被奇点逼到不能移动的端点时'
             '才可能奇异。圈动量积分遍及 $\\mathbb R^{4L}$，没有有限端点；端点只在部分积分之后出现（Feynman 参数单形的面，光锥动量分数的 '
             '$0$ 与 $1$），“无穷远处”对应紫外行为与第二类奇异性（$\\mathcal U=0$）。于是有两个不同的问题（critic O12）：积分作为外部不变量'
             '的函数在何处非解析——Landau 原本的问题\\cite{Landau1959}（另见\\cite{Nakanishi:1959jzx}），由参数形式的'
             '\\cref{thm:ir-landau-alpha}回答；在固定外动量下圈动量空间中哪些点被钳住——因子化需要的问题，它决定长程敏感性来自哪些区域'
             '\\cite{Sterman1978a}，由动量形式的\\cref{thm:ir-landau-momentum}回答。两者由\\cref{lem:ir-envelope}在方程层次上联系，但并不等价。\n\n') + s[b:]
save('ch04_p1_landau.tex', s)
print('pass 3 done')
