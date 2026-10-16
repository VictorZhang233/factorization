#!/bin/sh
# usage: zoom.sh PAGE X0 Y0 X1 Y1 [DPI]   (box measured on the 110-dpi page PNG)
# writes png/zoom-PAGE.png rendered at DPI (default 250)
cd "$(dirname "$0")" || exit 1
P=$1; X0=$2; Y0=$3; X1=$4; Y1=$5; D=${6:-250}
S=$(echo "scale=6; $D/110" | bc)
X=$(echo "$X0*$S/1" | bc); Y=$(echo "$Y0*$S/1" | bc)
W=$(echo "($X1-$X0)*$S/1" | bc); H=$(echo "($Y1-$Y0)*$S/1" | bc)
pdftoppm -r "$D" -f "$P" -l "$P" -x "$X" -y "$Y" -W "$W" -H "$H" -png -singlefile test_figset_F.pdf "png/zoom-$P"
echo "png/zoom-$P.png"
