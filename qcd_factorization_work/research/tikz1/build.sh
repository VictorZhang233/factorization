#!/bin/sh
# Rebuild figures1.tex from blocks/, check delimiters, compile the test document twice, render pages.
cd "$(dirname "$0")"
{ cat blocks/00_header.tex; for f in blocks/[0-9][0-9]_fig_*.tex; do printf '\n\n'; cat "$f"; done; } > figures1.tex
python3 -I split_figures.py | grep -E "PROBLEM|blocks"
xelatex -interaction=nonstopmode -halt-on-error test_figures1.tex > build1.log 2>&1 || { echo "LaTeX ERROR"; grep -n -A5 "^!" test_figures1.log | head -30; exit 1; }
xelatex -interaction=nonstopmode -halt-on-error test_figures1.tex > build1.log 2>&1 || { echo "LaTeX ERROR (2nd)"; exit 1; }
grep -n -E "Overfull|Underfull|undefined|multiply" test_figures1.log | head -20
rm -f png/p-*.png; pdftoppm -r 110 -png test_figures1.pdf png/p
echo "pages: $(ls png/p-*.png | wc -l)"
