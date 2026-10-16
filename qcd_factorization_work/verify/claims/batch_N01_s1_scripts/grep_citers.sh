#!/bin/bash
# usage: grep_citers.sh DIR id1 id2 ...   (downloads arXiv e-print into DIR/<id>/src, extracts into DIR/<id>/z, greps)
D="$1"; shift
for id in "$@"; do
  sub="$D/$(echo $id | tr '/' '_')"
  mkdir -p "$sub"
  if [ ! -s "$sub/src" ]; then curl -sL -m 90 -A "Mozilla/5.0 (verification script)" -o "$sub/src" "https://arxiv.org/e-print/$id"; sleep 2; fi
  rm -rf "$sub/z"; mkdir -p "$sub/z"
  ft=$(file -b "$sub/src")
  case "$ft" in
    *gzip*)
      inner=$(gunzip -c "$sub/src" 2>/dev/null | file -b -)
      case "$inner" in
        *tar*) tar -xzf "$sub/src" -C "$sub/z" 2>/dev/null ;;
        *) gunzip -c "$sub/src" > "$sub/z/main.tex" ;;
      esac ;;
    *PDF*) pdftotext "$sub/src" "$sub/z/main.txt" ;;
    *tar*) tar -xf "$sub/src" -C "$sub/z" ;;
    *) cp "$sub/src" "$sub/z/main.tex" ;;
  esac
  hits=$(grep -rIil "gordan\|farkas\|theorem of the alternative\|theorems of the alternative\|stiemke\|motzkin" "$sub/z" 2>/dev/null | head -5)
  echo "$id :: ${hits:-none}"
done
