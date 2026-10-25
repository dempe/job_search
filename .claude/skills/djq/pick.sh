#!/usr/bin/env bash
# Print one question, chosen uniformly at random, from the notes in
# "Job Applications/". A question is a run of consecutive `>` lines followed by
# one blank line and then an answer: a ``` fence or a [[link]] line. Blockquotes
# that aren't followed by an answer (quoted emails, notes) are not questions.
#
# Output: the note's name on the first line, then the question's `>` lines verbatim.
set -euo pipefail

cd "$(dirname "$0")/../../.."

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
    name = file[i]; sub(/^Job Applications\//, "", name); sub(/\.md$/, "", name)
    printf "%s\n%s", name, q[i]
  }
' "Job Applications"/*.md
