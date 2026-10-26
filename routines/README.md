# Routines — MS SOC Brief

Since 26 Oct 2026 the portal is built by **two routines** (claude.ai → Code → Routines), each with this
repository as its source:

| Routine | When (Europe/Warsaw) | Prompt to paste | Part A | Part B |
|---|---|---|---|---|
| MS SOC BRIEF - poranny | 06:00 | `poranny.prompt.md` | `poranny-A-build.md` — sources, state, brief artifact | `poranny-B-publish.md` — mirror to `site/`, publish |
| MS SOC BRIEF - wieczorny | 21:00 | `wieczorny.prompt.md` | `wieczorny-A-delta.md` — afternoon delta | `wieczorny-B-diff.md` — `/diff/` page |

The pasted prompt is short; the full instructions are the part files here, read from `origin/main` at every
run — a change to a part file is a commit, nobody pastes 90 kB into a settings box again.

Why: on 26 Oct 2026 the two scheduled tasks (Morning 06:00, Afternoon delta 21:00) stopped at their first
script — the session classed the scripts cut from `CLAUDE.md` as "Code from External" and refused to run them.
Routines run with the repository as their own source and were not affected (the 22:15 routine ran
`make_diff.py` from the same repository the evening before).

The four old jobs are DISABLED, not deleted: scheduled tasks "Microsoft SOC Brief — Morning" and
"— Afternoon delta", routines "MS SOC BRIEF - raport poranny v2" and "MS SOC BRIEF - zmiany v2". Their prompts
as stored on 26 Oct 2026 are the part files (owner's address removed — this repository is public).
