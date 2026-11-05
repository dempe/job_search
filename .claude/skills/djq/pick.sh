#!/usr/bin/env bash
# Print one question, chosen uniformly at random, from the application notes
# (Applications/{title}/{title}.md) and interview notes
# (Applications/{title}/Interviews/{n}/{n}.md). A question is a run of consecutive `>` lines followed by
# one blank line and then an answer: a ``` fence or a [[link]] line. Blockquotes
# that aren't followed by an answer (quoted emails, notes) are not questions.
#
# Output: the note's name on the first line ("{title}" or "{title} - Interview {n}"),
# then the question's `>` lines verbatim.
set -euo pipefail
shopt -s nullglob

cd "$(dirname "$0")/../../.."

notes=()
for dir in Applications/*/; do
  title=$(basename "$dir")
  [[ -f "$dir$title.md" ]] && notes+=("$dir$title.md")
  for interview in "$dir"Interviews/*/; do
    n=$(basename "$interview")
    [[ -f "$interview$n.md" ]] && notes+=("$interview$n.md")
  done
done

awk '
  function flush() { if (blk != "") { n++; file[n] = FILENAME; q[n] = blk } }
  FNR == 1 { inq = 0; state = 0; blk = "" }
  state == 2 { if ($0 ~ /^```/ || $0 ~ /^\[\[/) flush(); state = 0; blk = "" }
  /^>/ { if (!inq) blk = ""; blk = blk $0 "\n"; inq = 1; next }
  inq { inq = 0; state = ($0 == "") ? 2 : 0; if (state == 0) blk = ""; next }
  END {
    if (n == 0) exit 1
    srand()
    i = int(rand() * n) + 1
    name = file[i]; sub(/^Applications\//, "", name)
    if (match(name, /\/Interviews\/[0-9]+\/[0-9]+\.md$/)) {
      n = substr(name, RSTART + 12); sub(/\/.*/, "", n)
      name = substr(name, 1, RSTART - 1) " - Interview " n
    } else sub(/\/.*/, "", name)
    printf "%s\n%s", name, q[i]
  }
' "${notes[@]}"
