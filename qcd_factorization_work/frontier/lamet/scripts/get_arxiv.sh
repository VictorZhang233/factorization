#!/bin/sh
# Download arXiv source (e-print) for each id given as argument into papers/<id>/ (untrusted data),
# extract it there, and also produce a plain-text dump of all .tex files (papers/<id>/ALL.tex.txt).
# Falls back to the PDF (papers/<id>/paper.pdf -> paper.txt via pdftotext) if no TeX source exists.
# Usage: sh scripts/get_arxiv.sh <id> [<id> ...]   (run from the lamet directory)
BASE="$(pwd)/papers"
for id in "$@"; do
  d="$BASE/$(echo "$id" | tr '/' '_')"
  if [ -f "$d/ALL.tex.txt" ] || [ -f "$d/paper.txt" ]; then echo "have $id"; continue; fi
  mkdir -p "$d/src"
  curl -s -L -m 120 -A "Mozilla/5.0 (research script)" "https://arxiv.org/e-print/$id" -o "$d/eprint.bin"
  t=$(file -b "$d/eprint.bin")
  case "$t" in
    *gzip*)
      # could be tar.gz or a single gzipped tex file
      if tar -tzf "$d/eprint.bin" >/dev/null 2>&1; then
        (cd "$d/src" && tar -xzf "$d/eprint.bin" 2>/dev/null)
      else
        gunzip -c "$d/eprint.bin" > "$d/src/main.tex"
      fi ;;
    *tar*)
      (cd "$d/src" && tar -xf "$d/eprint.bin" 2>/dev/null) ;;
    *PDF*)
      cp "$d/eprint.bin" "$d/paper.pdf" ;;
    *)
      echo "?? $id: $t" ;;
  esac
  # collect tex
  find "$d/src" -name '*.tex' -type f 2>/dev/null | sort > "$d/texfiles.lst"
  if [ -s "$d/texfiles.lst" ]; then
    : > "$d/ALL.tex.txt"
    while IFS= read -r f; do
      printf '\n%%%%%%%%%%%% FILE: %s\n' "${f#$d/src/}" >> "$d/ALL.tex.txt"
      cat "$f" >> "$d/ALL.tex.txt"
    done < "$d/texfiles.lst"
    echo "ok  $id  ($(wc -l < "$d/ALL.tex.txt") lines tex)"
  else
    if [ ! -f "$d/paper.pdf" ]; then
      curl -s -L -m 120 -A "Mozilla/5.0 (research script)" "https://arxiv.org/pdf/$id" -o "$d/paper.pdf"
    fi
    pdftotext -layout "$d/paper.pdf" "$d/paper.txt" 2>/dev/null && echo "pdf $id ($(wc -l < "$d/paper.txt") lines)" || echo "FAIL $id"
  fi
  sleep 1
done
