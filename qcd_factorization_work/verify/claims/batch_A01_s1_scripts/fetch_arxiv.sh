#!/bin/sh
# Usage: sh fetch_arxiv.sh <dest_root> <arxiv_id> [<arxiv_id> ...]
# Downloads the latest arXiv e-print source of each id into <dest_root>/<id_sanitized>/ (own empty dir),
# extracts it (tar or gzip), and also fetches the abstract page metadata via the arXiv API.
root="$1"; shift
for id in "$@"; do
  d="$root/$(echo "$id" | tr '/' '_')"
  if [ -d "$d" ] && [ -n "$(ls -A "$d" 2>/dev/null)" ]; then echo "skip $id (exists)"; continue; fi
  mkdir -p "$d"
  curl -sL -m 120 -A "Mozilla/5.0 (verification script)" -o "$d/src.bin" "https://arxiv.org/e-print/$id"
  t=$(file -b "$d/src.bin")
  case "$t" in
    *gzip*) ( cd "$d" && (tar -xzf src.bin 2>/dev/null || (gunzip -c src.bin > main.tex)) ) ;;
    *PDF*) mv "$d/src.bin" "$d/paper.pdf"; pdftotext -layout "$d/paper.pdf" "$d/paper.txt" ;;
    *tar*) ( cd "$d" && tar -xf src.bin ) ;;
    *) echo "unknown type for $id: $t" ;;
  esac
  curl -sL -m 60 -o "$d/arxiv_api.xml" "https://export.arxiv.org/api/query?id_list=$id"
  echo "$id -> $t ; files: $(ls "$d" | tr '\n' ' ' | cut -c1-200)"
  sleep 3
done
