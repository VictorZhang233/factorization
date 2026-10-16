#!/bin/zsh
# assemble + full build + log checks (W19, Ch16)
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
zsh "$W/writing/work/W19/assemble.sh"
cd "$W/writing/test/W19" || exit 1
rm -f test_jets.aux test_jets.bbl test_jets.blg test_jets.out
xelatex -interaction=nonstopmode test_jets.tex > build1.log 2>&1
bibtex test_jets > bib.log 2>&1
xelatex -interaction=nonstopmode test_jets.tex > build2.log 2>&1
xelatex -interaction=nonstopmode test_jets.tex > build3.log 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' test_jets.log)"
echo "missing chars:"; grep "Missing character" test_jets.log | sort | uniq -c | head
echo "overfull:"; grep "Overfull \\\\hbox" test_jets.log
echo "underfull vbox/hbox count: $(grep -c 'Underfull' test_jets.log)"
echo "undefined citations:"; grep "Citation .* undefined" test_jets.log | sort -u
echo "multiply defined:"; grep "multiply defined" test_jets.log
echo "bibtex warnings:"; grep -i "warning" test_jets.blg
echo "pages: $(pdfinfo test_jets.pdf | grep Pages)"
python3 -I check_unit_v2.py ch16_jets.tex Ch16 FINAL_OUTLINE_v2.md
