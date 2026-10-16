#!/bin/sh
# Build the test document and render every page at 110 dpi into render/
cd "$(dirname "$0")" || exit 1
xelatex -interaction=nonstopmode -halt-on-error test_figures2.tex > build_stdout.log 2>&1
status=$?
grep -n -E "^!|Overfull|Underfull|Warning: Reference|undefined" test_figures2.log | head -40
[ $status -ne 0 ] && { echo "BUILD FAILED"; tail -30 test_figures2.log; exit 1; }
rm -rf render; mkdir -p render
pdftoppm -r 110 -png test_figures2.pdf render/page
ls render
pdfinfo test_figures2.pdf | grep Pages
