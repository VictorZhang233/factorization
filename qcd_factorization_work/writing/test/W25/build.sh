#!/bin/sh
# build the Ch22 test document (run from this directory)
cd "$(dirname "$0")" || exit 1
cp "../../../chapters/ch22_lamet.tex" .
cp "../../../spec_v2/refs_merged_v2.bib" .
cat "../../../chapters/ch22_lamet.bib-additions" >> refs_merged_v2.bib
xelatex -interaction=nonstopmode test_lamet.tex > /dev/null 2>&1
bibtex test_lamet > bibtex.out 2>&1
xelatex -interaction=nonstopmode test_lamet.tex > /dev/null 2>&1
xelatex -interaction=nonstopmode test_lamet.tex > /dev/null 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' test_lamet.log)"
grep -n "Overfull" test_lamet.log | head -40
grep "Citation .* undefined" test_lamet.log | sort -u | head
grep "multiply defined" test_lamet.log | head
grep "Missing character" test_lamet.log | sort -u | head
grep -i "warning" test_lamet.blg | head
grep "Output written" test_lamet.log
