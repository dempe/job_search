#!/usr/bin/env bash
# Print one question, chosen uniformly at random, from the application notes
# (Applications/{title}/{title}.md) and interview notes
# (Applications/{title}/Interviews/{n}/{n}.md). A question is a `### {question}`
# heading inside a note's `## Questions` section. Its answers are the plain
# text directly under the heading (application notes), up to the next heading,
# and the value of every `- answer::` line under it: the interview answer and
# each `#### Practice` session's answer.
#
# Output: the note's name on the first line ("{title}" or "{title} - Interview {n}"),
# its vault path without `.md` on the second, then the question as a `> ` line.
#
# With `--all {note}`, it reads only that note and prints every question in it,
# in order, after the same two lines, one blank line between questions.
#
# With `--answers [root]`, it reads every note under root (default: the vault)
# and prints each answer, in order: `## {note path without .md}`,
# `### {question}`, a blank line, then the answer verbatim, one blank line
# between them. A question with several answers is printed once per answer.
set -euo pipefail
shopt -s nullglob

all=0
answers=0
notes=()
if [[ "${1:-}" == "--all" ]]; then
  all=1
  notes=("$(cd "$(dirname "$2")" && pwd)/$(basename "$2")")
fi
root="$(cd "$(dirname "$0")/../../.." && pwd)"
if [[ "${1:-}" == "--answers" ]]; then
  answers=1
  root="$(cd "${2:-$root}" && pwd)"
fi

cd "$root"

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

awk -v all="$all" -v answers="$answers" '
  function trim(s) { sub(/^\n+/, "", s); sub(/\n+$/, "", s); return s }
  FNR == 1 { inqs = 0; cur = 0 }
  /^#{1,2} / { inqs = ($0 == "## Questions"); cur = 0; next }
  inqs && /^### / {
    n++; cur = n; file[n] = FILENAME; q[n] = substr($0, 5); sect = "direct"
    direct[n] = ""; na[n] = 0; infield = 0
    next
  }
  cur && /^####+ / { sect = "other"; next }
  cur && /^- answer:: / { na[cur]++; ans[cur, na[cur]] = substr($0, 12) }
  cur && /^- [a-z_]+::( |$)/ { infield = 1; next }
  cur && infield && /^[ \t]+/ { next }
  cur { infield = 0 }
  cur && sect == "direct" { direct[cur] = direct[cur] $0 "\n" }
  END {
    if (answers) {
      m = 0
      for (j = 1; j <= n; j++) {
        path = file[j]; sub(/\.md$/, "", path)
        a = trim(direct[j])
        if (a ~ /[^ \t\n]/) printf "%s## %s\n### %s\n\n%s\n", (m++ ? "\n" : ""), path, q[j], a
        for (k = 1; k <= na[j]; k++)
          if (ans[j, k] ~ /[^ \t]/) printf "%s## %s\n### %s\n\n%s\n", (m++ ? "\n" : ""), path, q[j], ans[j, k]
      }
      exit (m == 0)
    }
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
    if (!all) { printf "> %s\n", q[i]; exit }
    for (j = 1; j <= n; j++) printf "%s> %s\n", (j > 1 ? "\n" : ""), q[j]
  }
' "${notes[@]}"
