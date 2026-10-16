#!/bin/sh
# Assemble chapters/ch20_heavy.tex from parts, copy into the test directory and build it (xelatex, bibtex, xelatex x2).
# Usage: sh build.sh   (run from anywhere; paths are absolute and quoted because the project path contains a space)
R="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
W="$R/writing/work/W23"
T="$R/writing/test/W23"
python3 -I "$W/assemble.py" || exit 1
cp "$R/chapters/ch20_heavy.tex" "$T/ch20_heavy.tex"
cat "$R/spec_v2/refs_merged_v2.bib" "$R/chapters/ch20_heavy.bib-additions" > "$T/refs_merged_v2.bib"
cd "$T" || exit 1
xelatex -interaction=nonstopmode test_heavy.tex > run1.out 2>&1
bibtex test_heavy > bib.out 2>&1
xelatex -interaction=nonstopmode test_heavy.tex > run2.out 2>&1
xelatex -interaction=nonstopmode test_heavy.tex > run3.out 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' test_heavy.log)"
grep "Overfull" test_heavy.log
grep "Citation .* undefined" test_heavy.log | sort -u
grep "multiply defined" test_heavy.log | sort -u
grep "Missing character" test_heavy.log | sort -u | head
grep -i "warning" test_heavy.blg | head
echo "pages: $(pdfinfo test_heavy.pdf | grep Pages)"
grep "参考文献" test_heavy.aux | sed 's/.*{参考文献}{\([0-9]*\)}.*/bibliography starts on page \1/'
grep -o "\\\\@writefile{toc}{\\\\contentsline {section}{\\\\numberline {[0-9.]*}[^}]*}{[0-9]*}" test_heavy.aux | sed 's/.*numberline {\([0-9.]*\)}\(.*\)}{\([0-9]*\)}/section \1 starts p.\3/'
