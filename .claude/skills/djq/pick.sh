#!/usr/bin/env bash
# Print one question, chosen uniformly at random, from the application notes
# (Applications/{title}/{title}.md) and interview notes
# (Applications/{title}/Interviews/{n}/{n}.md). A question is a run of consecutive `>` lines followed by
# one blank line and then an answer: a ``` fence or an ![[embed]] of its Answers section. Blockquotes
# that aren't followed by an answer (quoted emails, notes) are not questions.
# Inside an interview note's `## Questions` section, a question is instead a
# `### {question}` heading followed (after any `- field::` grade bullets and a
# `#### Canonical Answer` heading) by an
# answer; it is printed as a `> ` line so the output looks the same.
#
# Output: the note's name on the first line ("{title}" or "{title} - Interview {n}"),
# its vault path without `.md` on the second, then the question's `>` lines verbatim.
#
# With `--all {note}`, it reads only that note and prints every question in it,
# in order, after the same two lines, one blank line between questions.
set -euo pipefail
shopt -s nullglob

all=0
notes=()
if [[ "${1:-}" == "--all" ]]; then
  all=1
  notes=("$(cd "$(dirname "$2")" && pwd)/$(basename "$2")")
fi

cd "$(dirname "$0")/../../.."

if (( ! all )); then
  for dir in Applications/*/; do
    title=$(basename "$dir")
    [[ -f "$dir$title.md" ]] && notes+=("$dir$title.md")
    for interview in "$dir"Interviews/*/; do
      n=$(basename "$interview")
      [[ -f "$interview$n.md" ]] && notes+=("$interview$n.md")
    done
  done
fi

awk -v all="$all" '
  function flush() { if (blk != "") { n++; file[n] = FILENAME; q[n] = blk } }
  FNR == 1 { inq = 0; state = 0; blk = ""; inqs = 0; hstate = 0 }
  state == 2 { if ($0 ~ /^```/ || $0 ~ /^!?\[\[/) flush(); state = 0; blk = "" }
  /^## / { inqs = ($0 == "## Questions") }
  inqs && /^### / { hq = "> " substr($0, 5) "\n"; hstate = 1; next }
  hstate {
    if ($0 ~ /^```/ || $0 ~ /^!?\[\[/) { blk = hq; flush(); blk = ""; hstate = 0 }
    else if ($0 != "" && $0 != "#### Canonical Answer" && $0 !~ /^- [a-z_]+::( |$)/ && $0 !~ /^[ \t]+- /) hstate = 0
    next
  }
  /^>/ { if (!inq) blk = ""; blk = blk $0 "\n"; inq = 1; next }
  inq { inq = 0; state = ($0 == "") ? 2 : 0; if (state == 0) blk = ""; next }
  END {
    if (n == 0) exit 1
    srand()
    i = all ? 1 : int(rand() * n) + 1
    path = file[i]; sub(/\.md$/, "", path); sub(/^.*Applications\//, "Applications/", path)
    name = file[i]; sub(/^.*Applications\//, "", name)
    if (match(name, /\/Interviews\/[0-9]+\/[0-9]+\.md$/)) {
      num = substr(name, RSTART + 12); sub(/\/.*/, "", num)
      name = substr(name, 1, RSTART - 1) " - Interview " num
    } else sub(/\/.*/, "", name)
    printf "%s\n%s\n", name, path
    if (!all) { printf "%s", q[i]; exit }
    for (j = 1; j <= n; j++) printf "%s%s", (j > 1 ? "\n" : ""), q[j]
  }
' "${notes[@]}"
