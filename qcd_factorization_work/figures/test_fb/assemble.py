#!/usr/bin/env python3
"""Assemble ../figset_B.tex from the parts (in book order) and write the full test driver."""
import os

here = os.path.dirname(os.path.abspath(__file__))
order = [
    # Ch4 ir
    '01_ir-mode-exponents', '20_ir-landau-simplex',
    # Ch6 ee
    '02_ee-cutsum-disc',
    # Ch7 dis
    '03_dis-euclid-segment',  # '19_dis-twist-graphical' dropped: duplicate of the figset_F version (figure checker, FIGCHECK.md)
    # Ch9 method
    '04_method-flowchart', '05_method-hasse', '06_method-nesting', '07_method-neighbourhoods',
    '08_method-kg', '09_method-sudakov-plane', '10_method-coeff-minus-coll', '11_method-glauber-direction',
    # Ch10 disall
    '12_disall-seed', '14_disall-ladder-regions', '13_disall-heavy',
    # Ch11 coll
    '15_coll-sia', '16_coll-sidis', '17_coll-photoproduction', '18_coll-transversity',
]

header = r"""% =====================================================================
%  figset_B.tex  --  TikZ figure set B of the QCD factorization monograph
%  (agent figB, local style prefix "fb").
%  Scope (FIGURES_INDEX_v2):
%    Sec. 2 -- Ch9 method, Ch10 disall, Ch11 coll (required + optional);
%    Sec. 3 -- Ch4 ir, Ch6 ee, Ch7 dis, Ch9 method, Ch10 disall
%              (required + optional).
%  Figures, in book order (owner chapter in brackets; "opt" = optional):
%    [Ch4]  fig:ir-mode-exponents
%           fig:ir-landau-simplex          (opt; Sec. 2 optional table, Ch4
%                                           owner -- drawn because no other
%                                           set covers Ch4; may be dropped)
%    [Ch6]  fig:ee-cutsum-disc
%    [Ch7]  fig:dis-euclid-segment
%           (the optional fig:dis-twist-graphical lives in figset_F.tex; the
%           duplicate drawn here was removed by the figure checker)
%    [Ch9]  fig:method-flowchart, fig:method-hasse, fig:method-nesting,
%           fig:method-neighbourhoods, fig:method-kg, fig:method-sudakov-plane,
%           fig:method-coeff-minus-coll, fig:method-glauber-direction
%    [Ch10] fig:disall-seed, fig:disall-ladder-regions, fig:disall-heavy
%    [Ch11] fig:coll-sia, fig:coll-sidis, fig:coll-photoproduction,
%           fig:coll-transversity (opt)
%
%  Requirements: common/preamble_fact.tex (ctexbook, XeLaTeX).  It loads
%  tikz with the libraries decorations.pathmorphing, decorations.markings,
%  arrows.meta, calc, positioning, shapes.geometric, patterns, backgrounds,
%  fit, and pgfplots (compat=1.17), and contains the style blocks STYLES and
%  STYLES-EXT (quark, gluon, gluon loop, photon, ghost, mom, mom', vertex,
%  blob, wilson, wilson plain, cut, hard blob, jet blob, jetB blob, soft blob,
%  hadron blob, glauber, opvertex, scalar, longit + \longitmark, lcaxis,
%  region), the macros \ii \dd \MSbar \as \order \Real \Imag \Disc, the
%  xcolor option dvipsnames (OliveGreen, RoyalBlue, Plum) and cleveref.
%  No package or TikZ library is loaded here.  Every extra style is declared
%  in the options of its tikzpicture (local to that picture) and carries the
%  prefix "fb"; the few helper macros (\fbEEladder, \fbEEred, \fbref,
%  \fbstep, \fbKGframe, \fbCMCphot, \fbCMCapprox, \fbGwedge, \fbTWframe)
%  are defined inside their figure environment, hence local to it.
%
%  Conventions used throughout (WRITER_SPEC_v2 Sec. 3):
%    * solid line with arrow = quark; the arrow is the fermion-number flow
%      (for an antiquark it points against the momentum); thick solid line
%      with arrow = heavy quark (fig:disall-heavy);
%    * separate thin labelled arrows (mom/mom') = momentum flow;
%    * double line with arrow = Wilson line, the arrow is the path
%      orientation of W[b,a] (from a to b); future pointing = away from the
%      operator vertex towards infinity;
%    * red dashed line = final-state cut (for a vertical cut the amplitude
%      is on the left, the complex-conjugate amplitude on the right);
%      zig-zag = branch cut;
%    * blob colours as in STYLES-EXT: grey = hard, blue = collinear to A
%      (target), orange = collinear to B / current jet, green = soft,
%      light grey = hadron; dark-red coil = Glauber gluon; blue coil with a
%      dot = scalar-polarized (K) gluon, the dot marking its k^mu end;
%    * n_A, n_B = light-like directions of the two beams/jets (row 2),
%      e_G = n_B - n_A (row 38); light-cone and exponent axes are labelled.
%  Each figure is delimited by  %%% BEGIN <label>  /  %%% END <label>.
% =====================================================================
"""

parts = []
for name in order:
    with open(os.path.join(here, 'parts', name + '.tex'), encoding='utf-8') as fh:
        parts.append(fh.read().rstrip('\n') + '\n')
with open(os.path.join(here, '..', 'figset_B.tex'), 'w', encoding='utf-8') as fh:
    fh.write(header + '\n\n' + '\n\n'.join(parts))

driver = r"""\input{preamble_fact.tex}
\AfterEndEnvironment{figure}{\clearpage}
\begin{document}
\setcounter{chapter}{4}\addtocounter{chapter}{-1}
\chapter{图集 B 测试}
\input{../figset_B.tex}
\input{dummy_labels.tex}
\end{document}
"""
with open(os.path.join(here, 'figset_B_test.tex'), 'w', encoding='utf-8') as fh:
    fh.write(driver)
print('figures:', len(order))
