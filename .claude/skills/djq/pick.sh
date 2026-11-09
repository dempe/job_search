#!/usr/bin/env bash
# Print one question, chosen uniformly at random, from the interview notes
# (Applications/{title}/Interviews/{n}/{n}.md) under root (default: the vault).
# Application notes are never practiced. A question is a `### {question}`
# heading inside a note's `## Questions` section. Its answers are the plain
# text directly under the heading (application notes), up to the next heading,
# and the value of every `- answer::` line under it: the interview answer and
# each `#### Practice` session's answer.
#
# Output: the note's name on the first line ("{title} - Interview {n}"),
# its vault path without `.md` on the second, then the question as a `> ` line.
#
# With `--all {note}`, it reads only that interview note and prints every
# question in it, in order, after the same two lines, one blank line between
# questions. It exits non-zero for any other note.
#
# With `--next-run {note}`, it prints the number for a new practice run in that
# interview note: one more than the highest `- run::` in its practice sessions,
# or 1. With `--run {k} {note}`, it prints that run's practice answers in note
# order: `### {question}`, a blank line, then the session's `answer::` value,
# one blank line between them, and nothing if the run has none. Both exit
# non-zero for anything but an interview note.
#
# With `--answers [root]`, it reads every application and interview note under root
# and prints each answer, in order: `## {note path without .md}`,
# `### {question}`, a blank line, then the answer verbatim, one blank line
# between them. A question with several answers is printed once per answer.
set -euo pipefail
shopt -s nullglob

all=0
answers=0
nextrun=0
run=""
notes=()
root="$(cd "$(dirname "$0")/../../.." && pwd)"

interview_note() {
  notes=("$(cd "$(dirname "$1")" && pwd)/$(basename "$1")")
  [[ "${notes[0]}" =~ /Applications/[^/]+/Interviews/([0-9]+)/([0-9]+)\.md$ ]] \
    && [[ "${BASH_REMATCH[1]}" == "${BASH_REMATCH[2]}" ]] && [[ -f "${notes[0]}" ]] || exit 1
}

if [[ "${1:-}" == "--all" ]]; then
  all=1
  interview_note "$2"
elif [[ "${1:-}" == "--next-run" ]]; then
  all=1 nextrun=1
  interview_note "$2"
elif [[ "${1:-}" == "--run" ]]; then
  [[ "${2:-}" =~ ^[0-9]+$ ]] || exit 1
  all=1 run="$2"
  interview_note "$3"
elif [[ "${1:-}" == "--answers" ]]; then
  answers=1
  root="$(cd "${2:-$root}" && pwd)"
elif [[ -n "${1:-}" ]]; then
  root="$(cd "$1" && pwd)"
fi

cd "$root"

if (( ! all )); then
  for dir in Applications/*/; do
    if (( answers )); then
      title=$(basename "$dir")
      [[ -f "$dir$title.md" ]] && notes+=("$dir$title.md")
    fi
    for interview in "$dir"Interviews/*/; do
      n=$(basename "$interview")
      [[ -f "$interview$n.md" ]] && notes+=("$interview$n.md")
    done
  done
fi

(( ${#notes[@]} )) || exit 1

awk -v all="$all" -v answers="$answers" -v nextrun="$nextrun" -v run="$run" '
  function trim(s) { sub(/^\n+/, "", s); sub(/\n+$/, "", s); return s }
  FNR == 1 { inqs = 0; cur = 0 }
  /^#{1,2} / { inqs = ($0 == "## Questions"); cur = 0; next }
  inqs && /^### / {
    n++; cur = n; file[n] = FILENAME; q[n] = substr($0, 5); sect = "direct"; insess = 0
    direct[n] = ""; na[n] = 0; infield = 0
    next
  }
  cur && /^##### / { sect = "other"; s++; sq[s] = cur; srun[s] = ""; sans[s] = ""; insess = 1; next }
  cur && /^####+ / { sect = "other"; insess = 0; next }
  cur && insess && /^- run:: / { srun[s] = substr($0, 9); if (srun[s] + 0 > maxrun) maxrun = srun[s] + 0 }
  cur && insess && /^- answer:: / { sans[s] = substr($0, 12) }
  cur && /^- answer:: / { na[cur]++; ans[cur, na[cur]] = substr($0, 12) }
  cur && /^- [a-z_]+::( |$)/ { infield = 1; next }
  cur && infield && /^[ \t]+/ { next }
  cur { infield = 0 }
  cur && sect == "direct" { direct[cur] = direct[cur] $0 "\n" }
  END {
    if (nextrun) { print maxrun + 1; exit }
    if (run != "") {
      m = 0
      for (j = 1; j <= s; j++)
        if (srun[j] == run && sans[j] ~ /[^ \t]/) printf "%s### %s\n\n%s\n", (m++ ? "\n" : ""), q[sq[j]], sans[j]
      exit
    }
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
