#!/bin/sh
# zoom.sh PAGE [DPI] [Y0] [H]: render the upper part of a page of test_fc.pdf to zoom/pPAGE.png
cd "$(dirname "$0")" || exit 1
p=$1; r=${2:-220}; y0=${3:-0}; h=${4:-0}
mkdir -p zoom
W=$(python3 -c "print(int(21/2.54*$r))")
[ "$h" = 0 ] && h=$(python3 -c "print(int(16/2.54*$r))")
Y=$(python3 -c "print(int((1.6+$y0)/2.54*$r))")
pdftoppm -r "$r" -f "$p" -l "$p" -x 0 -y "$Y" -W "$W" -H "$h" -png test_fc.pdf zoom/p"$p"
ls zoom/p"$p"*
