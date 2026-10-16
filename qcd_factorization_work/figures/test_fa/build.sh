#!/bin/sh
# Build the test document twice and render every page at 110 dpi into png/
cd "$(dirname "$0")" || exit 1
xelatex -interaction=nonstopmode -halt-on-error test_fa.tex > build_stdout.log 2>&1
xelatex -interaction=nonstopmode -halt-on-error test_fa.tex > build_stdout.log 2>&1
status=$?
echo "exit status: $status"
grep -n -E "^!|LaTeX Error|Undefined control|Overfull|Underfull|Missing character|multiply defined" test_fa.log | head -40
grep -c "Reference .* undefined" test_fa.log
[ $status -ne 0 ] && { echo "BUILD FAILED"; tail -40 test_fa.log; exit 1; }
rm -rf png; mkdir -p png
pdftoppm -r 110 -png test_fa.pdf png/p
ls png
pdfinfo test_fa.pdf | grep Pages
