# THE REPLY IS AN E-MAIL — format of the final reply of both routines (§5ho, 24 Nov 2026)

The owner does not read the run in a session. He reads **the completion e-mail**, and its body is the
final reply of the run, word for word. Until 24 Nov 2026 that e-mail was a wall of pipes, file names and
a 96-row checklist, and **no change in it carried a source** — the owner could not open what Microsoft
had published. This file sets the form of that reply. It binds both routines (`poranny`, `wieczorny`)
and overrides every "Reply in under N lines" / "print the checklist" sentence in the four part files on
FORM; the part files still decide WHAT has to be reported, and every item they ask for goes into one of
the sections below.

## Rules of form

1. **One reply for the whole run**, written after PART B — not "PART A's reply, then PART B's reply".
   Everything PART A would have said goes into the same sections.
2. **English** (the portal is in English), **with one Polish summary of 2–3 sentences** right under the
   status line (`W skrócie:`). Polish with diacritics; product names stay in English.
3. **Every URL is bare and complete**, on its own line or after `Source:` / `Portal:` / `Page:`:
   `https://…`. Never markdown link syntax `[text](url)`, never `<url>`, never a full stop or a closing
   bracket right after a URL — mail clients turn a bare `https://` into a link, and anything glued to it
   breaks the link. Never a relative path (`site/data/…`) where the reader needs a link.
4. **Every change has a source the reader can open**: the Message Center post, the Microsoft Learn page,
   the Microsoft blog post, the Microsoft Graph DevX commit
   (`https://github.com/microsoftgraph/microsoft-graph-devx-content/commit/<sha>`), the role page on
   Microsoft Learn — the `url`/`reference` the state block or catalog already holds. A change seen only in
   our tenant's own read says so: `Source: our tenant's Microsoft Graph service principal, read <UTC time>`.
   A change with no public source yet says `Source: not published by Microsoft yet` — never invent a URL.
5. **Plain text that survives any mail client**: no tables, no pipes as columns, no HTML, no emoji, no
   headings made of `#`. Section names in CAPITALS on their own line, items as `- ` bullets or `1.` numbers,
   at most two levels. Dates `24 Nov 2026`, times `07:34 Warsaw` or `06:34 UTC`.
6. **Short**: the whole e-mail fits on two screens. The detail lives on the page; the e-mail says what
   changed, why it matters, and where to read it.
7. **Nothing private**: no tenant ID, no account, no e-mail address, no secret (the repository is public
   and so is everything the run writes).

## Layout (in this order; a section with nothing to say is ONE line saying so, never left out)

```
MS SOC Brief — <Weekday DD Mon YYYY> — <morning build | evening delta> — <OK | PARTIAL | FAILED>
W skrócie: <2–3 zdania po polsku: co najważniejszego się zmieniło i czy coś wymaga działania>

TOP CHANGES
1. <what changed, in plain words> — <product>
   Why it matters: <one sentence, the SOC or admin consequence>
   Source: https://<Microsoft's page>
   Portal: https://guardzilla.azureme.pl/#<tab or anchor>
2. …  (the brief's Top N in the morning, at most 10; in the evening every added or changed item, at most 10,
       then "and N more: https://guardzilla.azureme.pl/diff/")

GRAPH PERMISSIONS AND ENTRA ROLES
- Microsoft changed: <N permissions, M roles> (catalog's own edits: K — not Microsoft's)
- <name> — <what changed> — <date of Microsoft's change>
  Source: https://<commit, Learn page or "our tenant's read …">
- Seen in our tenant since the last brief: <N> (from data/graph-sp-history.json), each as above

MESSAGE CENTER
- MC<number> — <title> — <action needed / by date, or "informational">
  Source: https://<the post's url from the state block>

DEADLINES IN THE NEXT 14 DAYS
- <DD Mon> — <what> — Source: https://…

LINKS
- Today's brief: https://<artifact URL>   (evening: "the SAME brief as this morning, now with today's changes")
- Portal: https://guardzilla.azureme.pl/
- What changed since the last brief: https://guardzilla.azureme.pl/diff/   (evening: and the delta artifact URL)

RUN NOTES
- every finding the part files tell you to "say in the reply": unreachable or stale sources (named),
  publish proof (BEFORE → AFTER SHAs and the route), class B items published as BRAK, compared-with
  dates, sizes — one line each
- §0f register entries not ZBUDOWANE (by name, state, what is missing) — only if there are any

CHECKLIST
- <n> OK, <m> BRAK, <k> n/d of <total> (§0, counted from CLAUDE.md §0)
- BRAK <item> — <reason>   (every BRAK, one line each; never "see file")
- Full checklist: https://github.com/wpiotrw/MS_SOC/blob/main/runlog/<YYYY-MM-DD>-<morning|evening>.md
```

The first line carries the status the part files ask for: `FAILED` when they say "say FAILED in the
first line", `PARTIAL` when the run published with BRAK items or skipped a step, otherwise `OK`.

## The full checklist goes to a file, not into the e-mail

The part files still require the WHOLE §0 checklist, every item `OK`, `BRAK <reason>` or `n/d <why>`,
never shortened — that rule stands, only the place changes. Write it to
`runlog/<YYYY-MM-DD>-<morning|evening>.md` in the repository root (NOT under `site/`): a heading with the
date, time and run, then PART A's checklist and PART B's checklist, one item per line, exactly as the
part files describe them. Add the file to PART B's last commit before its push; if PART B already
pushed, make one more commit `runlog: <date> <morning|evening>` by the same route PART B used and check
it reached `origin/main`. If it did not, say so in RUN NOTES and paste the BRAK lines anyway — the
e-mail must never claim a file that is not on `main`.
