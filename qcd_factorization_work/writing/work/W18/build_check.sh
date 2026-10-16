#!/bin/sh
# Assemble Ch15 from the parts, run the full test build (xelatex + bibtex + xelatex x2) and the QA greps,
# then run check_unit_v2.py.  Usage: sh build_check.sh
ROOT="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
cd "$ROOT" || exit 1
python3 -I writing/work/W18/assemble.py "$ROOT" || exit 1
cp chapters/ch15_scet.tex writing/test/W18/
cd writing/test/W18 || exit 1
xelatex -interaction=nonstopmode test_scet.tex > /dev/null 2>&1
bibtex test_scet > bibtex.out 2>&1
xelatex -interaction=nonstopmode test_scet.tex > /dev/null 2>&1
xelatex -interaction=nonstopmode test_scet.tex > /dev/null 2>&1
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' test_scet.log)"
echo "missing chars: $(grep -c 'Missing character' test_scet.log)"
echo "overfull boxes:"; grep 'Overfull' test_scet.log
echo "undefined citations: $(grep -c 'Citation .* undefined' test_scet.log)"
echo "multiply defined: $(grep -c 'multiply defined' test_scet.log)"
echo "bibtex warnings: $(grep -c '^Warning--' test_scet.blg)"
echo "pages: $(pdfinfo test_scet.pdf | awk '/Pages/{print $2}')"
for p in $(seq 1 40); do t=$(pdftotext -f $p -l $p test_scet.pdf - 2>/dev/null | head -c 60); case "$t" in *参考文献*) echo "bibliography starts on page $p"; break;; esac; done
echo "undefined refs (other units):"; grep 'Reference .* undefined' test_scet.log | sed "s/.*Reference \`\([^']*\)'.*/\1/" | sort -u | tr '\n' ' '; echo
python3 -I check_unit_v2.py ch15_scet.tex Ch15 FINAL_OUTLINE_v2.md
