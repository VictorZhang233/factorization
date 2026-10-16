#!/bin/bash
# Figure checker build: fresh relative copies of all nine figure files, dummy targets, two xelatex runs,
# log summary, label->page map.  Run from this directory:  ./build.sh   (add "render" to render PNGs at 80 dpi)
set -u
cd "$(dirname "$0")"
W="../.."
cp "$W/common/preamble_fact.tex" preamble_fact.tex
cp "$W/research/tikz1/figures1.tex" "$W/research/tikz2/figures2.tex" "$W/research/tikz3/figures3.tex" src/
cp "$W/figures/figset_A.tex" "$W/figures/figset_B.tex" "$W/figures/figset_C.tex" \
   "$W/figures/figset_D.tex" "$W/figures/figset_E.tex" "$W/figures/figset_F.tex" src/
SRCS="src/figures1.tex src/figures2.tex src/figures3.tex src/figset_A.tex src/figset_B.tex src/figset_C.tex src/figset_D.tex src/figset_E.tex src/figset_F.tex"
python3 -I mkdummy.py "$W/spec_v2/FINAL_OUTLINE_v2.md" dummy_labels.tex $SRCS || exit 1
rm -f check_all.aux
for i in 1 2; do
  xelatex -interaction=nonstopmode -halt-on-error=n check_all.tex > xelatex_run$i.stdout 2>&1
done
python3 -I logcheck.py check_all.log $SRCS
# label -> page map from the aux file
grep -o '\\newlabel{fig:[^}]*}{{[^}]*}{[0-9]*}' check_all.aux | sed 's/\\newlabel{\(fig:[^}]*\)}{{\([^}]*\)}{\([0-9]*\)}/\3\t\2\t\1/' | sort -n > labelpages.tsv
echo "pages: $(grep -c . labelpages.tsv) figure labels mapped; PDF pages: $(pdfinfo check_all.pdf 2>/dev/null | awk '/^Pages/{print $2}')"
if [ "${1:-}" = "render" ]; then
  rm -f png/*.png
  pdftoppm -r 80 -png check_all.pdf png/p
  echo "rendered $(ls png | wc -l) pages"
fi
