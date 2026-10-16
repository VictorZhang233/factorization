#!/bin/bash
# build the standalone test of Ch24 (xelatex + bibtex + xelatex x2)
cd "$(dirname "$0")"
xelatex -interaction=nonstopmode test_front.tex > /dev/null 2>&1
bibtex test_front > /dev/null 2>&1
xelatex -interaction=nonstopmode test_front.tex > /dev/null 2>&1
xelatex -interaction=nonstopmode test_front.tex > /dev/null 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' test_front.log)"
grep "Output written" test_front.log
grep -n "Overfull" test_front.log | head -20
grep "Citation .* undefined" test_front.log | head
grep "multiply defined" test_front.log | head
grep "Missing character" test_front.log | head
