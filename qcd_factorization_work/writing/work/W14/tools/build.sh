#!/bin/zsh
# Full build of the W14 test driver: xelatex + bibtex + xelatex x2, then log checks.
T="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W14"
cd "$T" || exit 1
xelatex -interaction=nonstopmode test_dy.tex > xe1.out 2>&1
bibtex test_dy > bib.out 2>&1
xelatex -interaction=nonstopmode test_dy.tex > xe2.out 2>&1
xelatex -interaction=nonstopmode test_dy.tex > xe3.out 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop\|^! ' test_dy.log)"
echo "missing chars: $(grep -c 'Missing character' test_dy.log)"
echo "overfull hbox:"; grep 'Overfull \\hbox' test_dy.log | head -20
echo "undefined citations:"; grep 'Citation .* undefined' test_dy.log | sort -u | head
echo "multiply defined:"; grep 'multiply defined' test_dy.log | head
echo "undefined refs (unique):"; grep -o "Reference \`[^']*' on page" test_dy.log | sed "s/Reference \`//; s/' on page//" | sort -u | tr '\n' ' '; echo
echo "blg warnings:"; grep -i "warning" test_dy.blg | head
echo "pages: $(grep -o 'Output written on test_dy.pdf ([0-9]* pages' test_dy.log)"
