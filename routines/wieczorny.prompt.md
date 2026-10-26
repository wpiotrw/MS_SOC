# MS SOC BRIEF — wieczorny (delta + changes page) — one run, two parts

Since 26 Oct 2026 this ONE routine does what used to be two separate jobs: the scheduled task
"Microsoft SOC Brief — Afternoon delta" (reads the sources again, adds `#pmdelta` to today's brief artifact and
publishes the `Microsoft SOC Delta <date>` artifact) and the routine "MS SOC BRIEF - zmiany v2" (computes the
`/diff/` page). The scheduled task stopped working on 26 Oct 2026: its session classed the scripts of this
repository as external code and refused to run them. This routine runs with the owner's own repository
`wpiotrw/MS_SOC` as its source.

The full instructions are versioned in that repository:

- PART A — `routines/wieczorny-A-delta.md` (afternoon delta of today's brief)
- PART B — `routines/wieczorny-B-diff.md` (the changes page `/diff/`)

How to run:

1. Run `date -u '+%Y-%m-%d %H:%M UTC'` and `TZ=Europe/Warsaw date '+%A %d %B %Y %H:%M %Z'`. The Warsaw date is the run date.
2. Read the two files from the CURRENT `origin/main` (`git fetch origin` in the checked-out repository, then
   `git show origin/main:routines/wieczorny-A-delta.md`; if there is no checkout,
   `git clone --depth 1 https://github.com/wpiotrw/MS_SOC /tmp/rt`). Never use an older copy.
3. Read PART A and carry it out completely. If today's brief does not exist, PART A follows its own rule for that.
4. Only after that, read PART B and carry it out completely. Where PART B speaks of what "the scheduled tasks"
   wrote, that includes PART A of THIS run. PART B's rule 6 ("you do not research sources") applies to PART B.
5. After a context compaction, check what is already done: does today's brief carry `#pmdelta` /
   `Microsoft SOC Delta <today>` exist (PART A done)? Is today's `/diff/` page on `origin/main`
   (`site/diff/full.html` dated today — PART B done)? Continue from the first part that is not done.
6. Reply: PART A's reply, then PART B's reply, each as its own instructions ask.

Where the two files and this prompt disagree, the files win — except points 3–5 here (the order of the parts).
