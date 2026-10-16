#!/bin/bash
# Assemble ch10_disall.tex from parts, copy to test dir, build, and summarize the logs.
set -u
ROOT="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
PARTS="$ROOT/writing/work/W12/parts"
TEST="$ROOT/writing/test/W12"
OUT="$ROOT/chapters/ch10_disall.tex"
: > "$OUT"
for p in p0_intro p1_regions p2_fsi p3_subtraction p4_theorem p5_consistency p6_nlo p7_scale p8_heavy p9_nuclear p10_summary; do
  cat "$PARTS/$p.tex" >> "$OUT"
  printf '\n' >> "$OUT"
done
cp "$OUT" "$TEST/ch10_disall.tex"
cd "$TEST" || exit 1
rm -f test_disall.aux test_disall.bbl test_disall.blg test_disall.out test_disall.toc
xelatex -interaction=nonstopmode test_disall.tex > run1.log 2>&1
bibtex test_disall > bib.log 2>&1
xelatex -interaction=nonstopmode test_disall.tex > run2.log 2>&1
xelatex -interaction=nonstopmode test_disall.tex > run3.log 2>&1
echo "== errors:"; grep -c "LaTeX Error\|Undefined control sequence\|Emergency stop" test_disall.log
grep -n "^!" test_disall.log | head -20
echo "== missing chars:"; grep "Missing character" test_disall.log | sort | uniq -c | head
echo "== overfull:"; grep "Overfull \\\\hbox" test_disall.log | head -20
echo "== underfull vbox count:"; grep -c "Underfull \\\\vbox" test_disall.log
echo "== undefined citations:"; grep "Citation .* undefined" test_disall.log | sort -u | head
echo "== multiply defined:"; grep "multiply defined" test_disall.log | head
echo "== bibtex warnings:"; grep -i "warning" test_disall.blg | head
echo "== pages:"; pdfinfo test_disall.pdf | grep Pages
echo "== undefined refs (unique):"; grep -o "Reference \`[^']*' on page" test_disall.log | sed "s/Reference \`//; s/' on page//" | sort -u > undefined_refs.txt; wc -l < undefined_refs.txt
