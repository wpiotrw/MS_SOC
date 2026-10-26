# MS SOC BRIEF — poranny (build + publish) — one run, two parts

Since 26 Oct 2026 this ONE routine does what used to be two separate jobs: the scheduled task
"Microsoft SOC Brief — Morning" (builds today's `Microsoft SOC Brief <date>` artifact) and the routine
"MS SOC BRIEF - raport poranny v2" (mirrors that artifact to the site). The scheduled task stopped
working on 26 Oct 2026: its session classed the scripts of this repository as external code and refused
to run them. This routine runs with the owner's own repository `wpiotrw/MS_SOC` as its source.

The full instructions are versioned in that repository:

- PART A — `routines/poranny-A-build.md` (research, state, build and publish today's brief artifact)
- PART B — `routines/poranny-B-publish.md` (mirror the artifact to `site/`, publish, prove it on `main`)

How to run:

1. Run `date -u '+%Y-%m-%d %H:%M UTC'` and `TZ=Europe/Warsaw date '+%A %d %B %Y %H:%M %Z'`. The Warsaw date is the run date.
2. Read the two files from the CURRENT `origin/main` (`git fetch origin` in the checked-out repository, then
   `git show origin/main:routines/poranny-A-build.md`; if there is no checkout,
   `git clone --depth 1 https://github.com/wpiotrw/MS_SOC /tmp/rt`). Never use an older copy.
3. Read PART A and carry it out completely. It ends when today's artifact is published, or when PART A's own
   rules stop it — then say why.
4. Only after that, read PART B and carry it out completely. Where PART B speaks of the artifact "the scheduled
   task" or "another run" built, that is PART A of THIS run. If PART A did not publish today's artifact, PART B
   follows its own rule for a missing artifact.
5. After a context compaction, check what is already done before doing anything: does
   `Microsoft SOC Brief <today>` exist in `Artifact action:"list"` (PART A done)? Is `site/data/<today>.json`
   on `origin/main` (PART B done)? Continue from the first part that is not done; never redo PART A when
   today's artifact exists.
6. Reply: PART A's reply, then PART B's reply, each as its own instructions ask.

Where the two files and this prompt disagree, the files win — except points 3–5 here (the order of the parts).
