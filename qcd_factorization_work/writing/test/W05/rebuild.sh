#!/bin/sh
# reassemble unit files from parts and rebuild both test drivers (writer W05)
W="../../work/W05/parts"
cat $W/p0_intro.tex $W/p1_oneloop.tex $W/p2_regions.tex $W/p3_factorization.tex $W/p4_evolution.tex $W/p5_multileg.tex $W/p6_collinear.tex > ../../../chapters/ch05_sudakov.tex
cat $W/b1_rules.tex $W/b2_eikonal.tex $W/b3_cusp.tex > ../../../chapters/appB_wilson.tex
cp ../../../chapters/ch05_sudakov.tex ../../../chapters/appB_wilson.tex .
cp ../../../chapters/ch05_sudakov.bib-additions ch05_additions.bib
for t in test_sudakov test_appB; do
  xelatex -interaction=nonstopmode $t.tex > $t.run1 2>&1
  bibtex $t > $t.bibrun 2>&1
  xelatex -interaction=nonstopmode $t.tex > $t.run2 2>&1
  xelatex -interaction=nonstopmode $t.tex > $t.run3 2>&1
  echo "== $t: errors=$(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' $t.log) $(grep 'Output written' $t.log)"
done
