#!/bin/sh
# zoom.sh <name> <x0_cm> <y0_cm> <w_cm> <h_cm> [dpi]  -- crop of page 1 (cm from the top-left corner)
cd "$(dirname "$0")" || exit 1
n="$1"; d="${6:-300}"
x=$(python3 -c "print(int($2/2.54*$d))"); y=$(python3 -c "print(int($3/2.54*$d))")
w=$(python3 -c "print(int($4/2.54*$d))"); h=$(python3 -c "print(int($5/2.54*$d))")
pdftoppm -r "$d" -png -f 1 -l 1 -x "$x" -y "$y" -W "$w" -H "$h" "one/$n.pdf" "png/$n-crop"
ls png | grep "$n-crop"
