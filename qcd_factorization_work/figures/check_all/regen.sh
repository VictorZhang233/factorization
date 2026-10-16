#!/bin/bash
# Figure checker: re-assemble figset_B..F from their per-figure sources exactly as the owners' build
# scripts do (without running the owners' test builds).  Usage: ./regen.sh B C D E F
set -eu
cd "$(dirname "$0")/.."
for X in "$@"; do
  case $X in
    B) (cd test_fb && python3 -I assemble.py) ;;
    C|E|F)
      case $X in C) D=test_fc ;; E) D=test_fe ;; F) D=test_ff ;; esac
      { cat $D/blocks/00_header.tex; for f in $D/blocks/[0-9][0-9]_fig_*.tex; do printf '\n'; cat "$f"; done; } > figset_$X.tex ;;
    D) python3 -I - <<'EOF'
import glob
blocks = sorted(glob.glob('test_fd2/blocks/[0-9][0-9]_*.tex'))
with open('figset_D.tex', 'w', encoding='utf-8') as f:
    for i, b in enumerate(blocks):
        txt = open(b, encoding='utf-8').read().rstrip('\n') + '\n'
        if i:
            f.write('\n')
        f.write(txt)
EOF
    ;;
  esac
  echo "re-assembled figset_$X.tex: $(grep -c '^%%% BEGIN' figset_$X.tex) blocks"
done
