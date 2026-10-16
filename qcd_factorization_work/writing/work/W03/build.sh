#!/bin/bash
# W03 build: concatenate Ch3 parts, copy units into the test dir, build all three drivers, summarize logs
set -u
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
cd "$W/writing/work/W03/parts" && cat ch03_p1.tex ch03_p2.tex ch03_p3.tex ch03_p4.tex ch03_p5.tex ch03_p6.tex > "$W/chapters/ch03_prelim.tex"
T="$W/writing/test/W03"
cp "$W/chapters/ch03_prelim.tex" "$W/chapters/appA_lightfront.tex" "$W/chapters/appI_gamma5.tex" "$T/"
cd "$T"
# bibliography for the standalone tests: merged bib + this writer's additions
cat refs_merged_v2.bib "$W/chapters/appI_gamma5.bib-additions" > refs_W03.bib
for d in test_prelim test_appA test_appI; do
  sed -i '' 's/\\bibliography{refs_merged_v2}/\\bibliography{refs_W03}/' $d.tex
  xelatex -interaction=nonstopmode $d.tex > /dev/null 2>&1
  bibtex $d > $d.bibtex.out 2>&1
  xelatex -interaction=nonstopmode $d.tex > /dev/null 2>&1
  xelatex -interaction=nonstopmode $d.tex > /dev/null 2>&1
  echo "=== $d: errors=$(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' $d.log)  $(grep -o 'Output written on .*' $d.log)"
  grep "Overfull" $d.log | head -5
  grep "Citation .* undefined" $d.log | head -5
  grep "multiply defined" $d.log | head -3
  grep "Missing character" $d.log | head -3
  grep -i "warning" $d.blg | head -5
done
