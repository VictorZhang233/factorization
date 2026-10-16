#!/bin/bash
# usage: ./build.sh test_method   (xelatex + bibtex + xelatex x2)
set -e
n=$1
xelatex -interaction=nonstopmode $n.tex > /dev/null 2>&1 || true
bibtex $n > /dev/null 2>&1 || true
xelatex -interaction=nonstopmode $n.tex > /dev/null 2>&1 || true
xelatex -interaction=nonstopmode $n.tex > /dev/null 2>&1 || true
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' $n.log)"
grep -n 'LaTeX Error\|Undefined control sequence\|Emergency stop' $n.log | head -20 || true
echo "missing chars: $(grep -c 'Missing character' $n.log)"
grep 'Overfull \\hbox' $n.log | awk '{print}' | head -30 || true
grep 'Citation .* undefined' $n.log | sort -u | head -20 || true
grep 'multiply defined' $n.log | head || true
grep -c 'Reference .* undefined' $n.log || true
pdfinfo $n.pdf 2>/dev/null | grep Pages || true
