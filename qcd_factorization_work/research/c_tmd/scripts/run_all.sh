#!/bin/zsh
# Re-run every verification script of the c_tmd agent and write logs/<name>.log ; prints the last line of each.
# Usage:  zsh "scripts/run_all.sh"   (from the c_tmd directory; paths are quoted because of the space in "theorem proof")
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$DIR/../logs"
mkdir -p "$LOG"
for s in real_graphs rapidity_checks ft_check virtual_vertex soft_factor one_loop_tmd collins_tmd quark_in_gluon \
         delta_regulator form_factor hard_and_scheme css_expansion dy_matrix_elements dy_qt_check dy_qt_check2 \
         sivers_spectator sivers_symmetry; do
  ( cd "$DIR" && python3 -u -I "$s.py" > "$LOG/$s.log" 2>&1 )
  printf '%-20s %s\n' "$s" "$(grep -v 'Warning\|warnings.warn\|v, _ = quad\|tolerance\|underestimated' "$LOG/$s.log" | tail -1)"
done
if grep -l "FAIL" "$LOG"/*.log >/dev/null 2>&1; then echo "SOME LOG CONTAINS FAIL:"; grep -l "FAIL" "$LOG"/*.log; else echo "no FAIL in any log"; fi
