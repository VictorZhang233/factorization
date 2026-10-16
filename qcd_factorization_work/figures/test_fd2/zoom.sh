#!/bin/sh
# usage: zoom.sh DOC PAGE X0 Y0 X1 Y1 [DPI]  (box measured on the 110-dpi page PNG)
cd "$(dirname "$0")" || exit 1
DOC=$1; P=$2; X0=$3; Y0=$4; X1=$5; Y1=$6; D=${7:-250}
S=$(echo "scale=6; $D/110" | bc)
X=$(echo "$X0*$S/1" | bc); Y=$(echo "$Y0*$S/1" | bc)
W=$(echo "($X1-$X0)*$S/1" | bc); H=$(echo "($Y1-$Y0)*$S/1" | bc)
pdftoppm -r "$D" -f "$P" -l "$P" -x "$X" -y "$Y" -W "$W" -H "$H" -png -singlefile $DOC.pdf "png/zoom-$DOC-$P"
echo "png/zoom-$DOC-$P.png"
