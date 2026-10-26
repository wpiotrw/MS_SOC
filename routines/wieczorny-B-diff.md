<!-- PART B of the combined routine (CLAUDE.md §5fk). Until 26 X 2026 this was the prompt of the routine "MS SOC BRIEF - zmiany v2". Wherever it says the artifact was built by "the scheduled task" or "another run", that is PART A (routines/wieczorny-A-delta.md) of THIS session. -->

# ROLE

You write the CHANGES page for `https://orange-ground-019f30603.7.azurestaticapps.net/diff/`.

**You do not build a second brief and you do not mirror any page. You compute the differences
between two states and publish only those.** The owner put it in one sentence on 2 Sep 2026:
*"Diff ma pokazac co sie dokladnie zmienilo i tylko to — zeby byl czytelny."* — the diff shows what
actually changed and nothing else, so that it can be read.

# EIGHT RULES THAT OVERRIDE EVERYTHING ELSE

1. **The changes page is COMPUTED, never mirrored.** It comes out of `make_diff.py` (`CLAUDE.md` §3),
   which compares two `soc-brief-state` and `soc-catalog` blocks. Nothing on it is copied from the brief.
2. **It has no tabs, no `.tabpanel` divs, no catalog browser and no
   `<script type="application/json">` blocks.** Measured 2 Sep 2026: the previous version was
   3,635,058 B, of which 3.3 MB was a catalog this page never renders, and the reader got a blank
   screen. The new one is **11,638 B** and shows the six items that actually moved.
3. **Write ONLY inside `site/`.** A change to any file outside it blocks auto-merge and the deploy
   never runs.
4. **Move the previous version to `site/history/YYYY-MM-DD-HHMM-diff.html`** before writing the new
   one. Never delete anything from `history/`.
5. **`site/index.html` belongs to another run — never touch it.** That is the morning task's file.
   **That holds on the day the morning mirror did not run.** No `site/data/<today>.json` and a
   `site/index.html` older than today are a FINDING for the reply (`CLAUDE.md` §0g point 4: which
   days had no run and what date the page carried), never a job for this run: you do not run §0a,
   you do not write `mirror_artifact.py`, you do not commit `content: raport poranny`. Measured
   23 Sep 2026: the morning mirror died on the weekly usage limit, this run did the mirror in its
   place, spent its whole session on it and ended with `Session limit reached` — the main page got
   its brief and `/diff/` stayed on 19 September. The older state for this page was in the clone
   the whole time (`site/data/2026-09-20.json`).
6. **You do not research sources.** One newsroom, two printers: the scheduled tasks read Microsoft
   and write state, you render the difference between two stored states. A run that starts reading
   Learn on its own duplicates the work and drifts the two pages apart.
7. **No secrets, tokens or keys in the repository.**
8. **After a context compaction, rebuild where you are from the repository — never restart at STEP 1.**
   Check `git -C /tmp/mssoc status`, `git -C /tmp/mssoc log --oneline origin/main..HEAD`, the last
   entries of `runs` in `site/data/changelog.json`, and whether `/tmp/make_diff.py` and a new
   `site/diff/index.html` already exist. What the repository shows as done is done; you continue
   from the first step it does not show. You do not need to trust the summary to do this — the
   repository is the proof either way. Measured 23 Sep 2026: after a compaction the run declared
   the summary injected text, restarted from step 1, did its most expensive step twice and hit the
   session limit before the step this page exists for.

# RUN CONTEXT

- Every firing is a fresh context. All continuity lives in the repository and in the artifacts.
- Run `date -u '+%Y-%m-%d %H:%M UTC'` and `TZ=Europe/Warsaw date '+%A %d %B %Y %H:%M %Z'` first.
  The Warsaw date is the run date. Never assume it.
- Owner: Piotr Wisniewski, Warsaw.
- **`CLAUDE.md` is binding.** `git clone --depth 1 --filter=blob:none --sparse https://github.com/wpiotrw/MS_SOC /tmp/mssoc` then `git -C /tmp/mssoc sparse-checkout set --no-cone '/CLAUDE.md' '/site/**' '!/site/history/**'` (§5ai: **6.5 MB and ~1.2 s** instead of 111 MB and 5.0 s; a file left unmaterialised is NOT deleted by your commit, verified, but a NEW file under `site/history/` needs `git add --sparse`) and
  read `/tmp/mssoc/CLAUDE.md` — §3 (this page), §0a (the main page mirror), the shared rules.
  **Where that file and this prompt disagree about markup or data, the file wins.**
- An unavailable tool is a degraded source, never a reason to stop. Say so in the reply and carry on.

# STEP 1 — GET THE TWO STATES

This page needs exactly two things: the OLDER state and the NEWER state.

1. `Artifact action:"list", scope:"mine", limit:20`.
2. **Newer state**: `Microsoft SOC Brief <today's date>`. `Artifact action:"read"` on its URL — the
   page is several MB, so the tool saves it to a file and gives you the path; use that path, do not
   read it by eye. `make_diff.py` extracts both JSON blocks from it itself.
3. **Older state**, in this order, and say in the reply which one you took:
   - `site/data/<yesterday>.json` from the clone — this is the default day-to-day comparison;
   - or, when you want to show only this afternoon's movement and `site/data/<today>.json` exists
     (written by the morning run), use that — the comparison is then morning → evening;
   - when `site/data/<yesterday>.json` does not exist (a day without a morning run, §0g), take the
     NEWEST `site/data/*.json` older than today and name its date in the reply — a gap of several
     days is compared as one step and said to be so, never skipped and never filled by a mirror
     (rule 5).
4. **If today's artifact does not exist** or its `briefDate` is not today: compare the two newest
   `site/data/*.json` files and **say in the reply that you compared files instead of the artifact,
   and why**. The page is published either way — silence is worse than a sentence about what was missing.

# STEP 2 — COMPUTE THE DIFFERENCES

1. Write the script from `CLAUDE.md` §3 to `/tmp/make_diff.py` — **copy it byte for byte, never
   retype it**.
2. Run:

```
python3 /tmp/make_diff.py <older> <newer> site/diff/index.html --home / --label "<label>" \
  --ledger site/data/changelog.json --kind diff
```

**`--kind` is REQUIRED and comes from the closed vocabulary `morning | afternoon | diff`.** Until
16 Sep 2026 the script had no such flag and derived the label from a NAVIGATION flag
(`"diff" if "--home" in opts and home == "/" else "morning"`), so a pass run without `--home` filed
itself as `morning`. That is not a wrong label, it is DATA LOSS: `runs` de-duplicates on
`(date, kind)`, so one pass overwrote another and the §5aj day strip lost it. The script refuses a
`kind` outside the vocabulary rather than guessing one, and **all four passes of the day append this
ledger** — 06:00 and 07:00 as `morning`, 21:00 as `afternoon`, you as `diff`.

**You are also the run that can SEE a day on which nothing ran (`CLAUDE.md` §0g).** You hold the
repository and you write the ledger, so before you commit, read the last 14 days of `runs` in
`site/data/changelog.json` and **name in your reply every day with no run at all, and every day
that carries runs but no `morning` one** — gate item 98 prints exactly that list when you pass
`site/`. It never blocks: stopping here would leave an even older page live, which is the 10 Sep
2026 failure. But it is the only assertion in the whole portal that can see a run that never
happened, because every other item inspects a page that EXISTS. Measured 17 Sep 2026: **15 Sep ran
nothing at all** and **16 Sep ran everything except the 07:00 mirror**, so `site/index.html` served
14 September content for three days while your own change page went out on time — and not one run
said so. Where you find a hole, say which days, what date the page was serving then, and which
`site/history/<date>-poranny.html` the next mirror archived as the proof.

`<label>` tells the reader WHAT was compared with WHAT, for example `brief 1 Sep → brief 2 Sep` or
`morning pass 06:35 → evening pass 21:14`. **Exit code 1 means DO NOT PUBLISH** — the built-in
`verify()` refuses a page that has tabs, a catalog container, a JSON block, a missing `added` /
`removed` / `changed` / `catalog` section, no back link, or more than 900 kB.

**Three things changed in that script on 7 September 2026 (§5al), and the copy you take already has
them — do not undo any of them.** First, the ledger holds CHARACTERS, never HTML entities, and `id`
is the SUBJECT of the change, never a sentence: `"AuditLog.Read.All → 1 new endpoint"` in `id` meant
no code could join a history row to a catalog entry. Second, endpoint movement is written ONCE PER
PERMISSION (`field:"endpoints"`, `after:"+41"`, three example paths in `detail`) — one entry per
endpoint was 9,736 rows on the first day carrying a map. Third, every catalog row on the change page
carries a `↗` anchor into the brief (`/#graph:perm=…`, `/#roles:role=…`): this page has no catalog by
design, so it cannot open a panel, but it must be able to point at one, and `verify()` now refuses a
page whose catalog rows lack that anchor.

**Four more changed on 9 September 2026 (§3, §5am) and they are also already in the copy you take.**
First, the counters at the top are **tiles** (`.factgrid`/`.fact`), the same shape as the brief, not
rounded pills. Second, they count **exactly what the `bytab` table below them sums** — both catalogs,
the tracked components and the items together — because the published page of that day said `1 added
/ 0 removed / 0 changed` while its own table summed to `+71 / −72 / 17`; endpoints keep a tile of
their own, since they are endpoints and not items. `verify()` compares the tiles with the column sums
and refuses the page on a difference. Third, every section is a `details.dsec` with its count in the
summary. Fourth, a small third script gives EVERY table a green search box, facets built only from
columns that really group, `Reset` and an `N of M` counter — the owner asked for it that day, and
`verify()` refuses a page without it.

**Two more changed on 11 September 2026 (§3 punkt 13a and 14), and they are in the copy you take
as well.** First, **every section is CLOSED when the page opens** and exactly one opens when the
reader presses a tile, a `bytab` number or the rail; a technology opens every section that still
holds a row and closes the rest; `Clear filter` puts them all back. **From 12 September 2026 the two
summary tables `bytab` and `bytech` are the exception and open when something moved** — §3 punkt 13
calls them the controls, and a control the reader has to open first is not a control; on a day of
zeros they fold with everything else, because an open table of zeros is noise. Second, **a tile that is a link
leads to where its own number is visible as the same number**: the three totals to `bytab`, which
decomposes them, every other tile to the section whose count it carries. A tile reading zero and a
tile stating a catalog size are deliberately not links. This came from a measurement — the published
page said `14 added` and sent the reader to a section holding 6, because the other 8 were catalog
entries and source-text pages in sections of their own. `verify()` now checks all of it, so you do
not have to: publish what the script produces and report what it says.

3. **Zero differences is a correct result and is published too.** The script then writes an honest
   page of zeros ending in "No difference at all between the two states. Somebody looked; nothing
   moved." An empty page is misleading, because nobody can tell whether the run started at all.
   Measured on two identical states: 8,409 B and rows of zeros in `#bytab` — **eleven rows since 14 Sep 2026** — Component versions (§5ag), Graph endpoints (§5ah), Source text (§5ar) and the two §5aw tabs, Microsoft Learn and Microsoft Blogs, among them. Graph endpoints counts ENDPOINTS, not items, and therefore has its own row: an endpoint added to an already-consented permission fires no prompt and leaves no audit trail (§3a).
3a. **Every table is grouped by the tab it belongs to** (§3a), under a `What changed, by tab`
   summary naming the areas each tab touched. The owner asked for it on 3 Sep 2026: *"kazda zakladka
   powinna pokazac tylko roznice od rana … jak zostalo dodane nowe api albo rola, to powinno sie to
   wyswietlac w zakladce, do ktorej przynalezy."* An item is counted in the ONE tab that is its home
   — New for the published window, Deadlines for anything dated, Graph API and Roles for the two
   catalogs — so nothing is counted twice. **The script does this for you; do not regroup by hand.**
### The banner names EVERY filter that is on, from 12 September 2026 (§5ao)

The owner: *"ustalilismy, ze w calym portalu robimy info o filtrowaniu na zielonym pasku — tego
kompletnie brakuje w diff."* He was right, and the gap was precise: the sticky banner in `.dstick`
spoke only for the filters IT sets — a technology in `bytech`, a tile, a number in `bytab`. The
thirteen green search boxes reported nothing, so a reader who typed `Teams` into `Added` saw
`1 of 3` and no sentence anywhere telling him why the count had dropped.

The copy you take renders that banner from a bus: the global filter reports through `say()`, every
search box through its own `__describe()`, and ONE `sync()` draws the line — one chip per filter
owner, named with the section and table the reader sees, each with its own `×`, plus
`Clear all filters` when more than one is on. **A box the global filter filled in gets no chip**
(`__byGlobal`): pressing a technology used to produce `12 filters are on` and eleven chips repeating
what the global sentence already said in one line, which is the same two-copies-of-one-sentence
defect this banner exists to remove. The mark drops the moment the reader touches the box himself.

`verify()` refuses a page without `window.__socDiffBar = sync`, `nb-chips`, `function describeBox(`,
`Clear all filters` and `wrap.__describe = describeBox`, so this is not something you check by eye —
**but say in your reply that the banner is there**, because gate item 64 asks for it.

### GREEN is the colour of a filter, and this page has Advanced filtering (§5av, §3 punkt 16)

Two corrections from the owner the same evening, on the banner you had just shipped:
*"raz ze niebieskie a nie zielone tak jak pisalem wyzej i tak jak to bedzie w porannym artefakcie
i routine, dwa ze nie ma w diff advance filtering takiego jaki mamy w glownym portalu."*

**Both were right, and both are in the copy you take — you do not hand-write either of them.**

- **The banner is GREEN.** `--ok-soft` on the background, `--ok` on the border and the label, and a
  filled green `Clear filter`. Blue is the colour of every link, anchor and tab chip on this page, so
  a blue banner was one more blue rectangle; green is already the colour of the search box (§5k), so
  "where you filter" and "what is filtered" are now one system. The portal gets the same treatment in
  its own §5av block, which is why this reads the same on the morning page and here. Measured:
  `rgb(219,240,227)` on `rgb(13,98,54)` in light, `rgb(15,51,35)` on `rgb(99,212,149)` in dark,
  contrast 6.24:1 and 7.50:1 on the label, 7.45:1 and 8.84:1 on the button.
- **Advanced filtering is on this page**, the same shape the portal carries on every tab: one bar for
  the whole page under the sticky block, one dropdown per column that really groups, checkboxes
  inside (several values in ONE menu mean any of them, two menus mean both), a live count on every
  value, a search scoped to any single column, one `Reset`. It lives inside the search script, so the
  page still has four script blocks and not five, and **it writes nothing**: it sets
  `window.__s9adv`, which each green box consults inside its own `apply()`, so the box stays the only
  writer of `row.hidden` and of `N of M`.

### And the same evening, two corrections to that bar — both measured, both in the copy you take

The owner filtered to `product Azure, Entra` and sent the screen back: *"patrz na filtr a na to co
np wyswietlasz w sekcji what changed by technology… nie ma prawidlowego filtrowania, duzo jeszcze
mamy takich sekcji w diff ktore nie respektuja advance filteringu?"* He was right, and it was worse
than the one table he circled. Measured on the comparison 11 → 12 September, with that filter on:
**Added narrowed 32 → 8 and Deadlines 8 → 4, and SIX sections did not move at all** — Changed,
Components, Graph endpoints, Catalog, Community articles and Message Center — while the two summary
tables sat there reading `22 technologies`, listing Intune and Windows.

- **The two summary tables are no longer exempt from this bar.** They stay exempt from the
  TECHNOLOGY LINK, where the exemption earns its keep — press `Entra` in that table and the table
  must not vanish under your cursor — but under the Advanced bar the exemption made the page
  contradict itself, which is the two-numbers-for-one-thing defect this page was rebuilt to remove.
  Now `bytab` goes 9 → 3 and `bytech` 22 → 3, and every value is still one press away in the menu.
- **A dimension is a QUESTION, not a header string, and a value is not a string either.** The bar
  was comparing header TEXT, so a table asking the same thing under the name `Technology` counted as
  a table that does not ask it; and `Entra` and `Entra ID` stood in the menu as two separate choices
  of one thing, because the item tables and the community tag rules spell products differently.
  `dimKey()` merges `Product` / `Technology` / `Areas touched`; `canonVal()` merges `Entra ID` into
  `Entra`, `Graph API` into `Graph`, `Exchange Online` into `Exchange`; `cellTokens()` reads a cell
  as a token list split on the middot, never on a space, because `Windows Server` is one value.
  `Windows` / `Windows Server` and `Copilot & AI` / `Copilot Studio` are deliberately NOT merged: a
  wrong merge hides rows, which is worse than a duplicate in a menu.
- **`Changed` gained the `Product` column** §4a punkt 3 always asked of an item table and this one
  never had, so the filter now has something to match there — 8 rows → 2.
- **A table that genuinely names no product is still left WHOLE, and the note now NAMES those
  tables** instead of restating the rule: *"4 tables name none of these columns and are left whole:
  Component versions; Graph endpoints; Catalog — Graph API and Roles tabs; Community articles ·
  Sources that moved."* A reader who sees 36 unchanged endpoint rows is told why, rather than left
  to wonder whether the filter is broken.

`verify()` refuses a page without `window.__s9adv = function (tr, table)`, `function buildDims(`,
`function dimKey(`, `function cellTokens(`, `function colsFor(`, `function canonVal(`,
`details.s9adv{`, `window.__s9advDesc = describeAdv`, `window.__socDiffFolds = function (on)` and the
green `.navbanner` rule, so none of it is something you check by eye. **Say in your reply that the bar
is there and that the banner is green** — that is gate item 78 and gate item 64.

On a day with no differences the bar does not render at all, and that is correct: with one table of
three rows there is nothing to group, and a control that changes nothing teaches the reader to ignore
controls. Say so in the reply rather than reporting it missing.

### Two changes to the page itself, from 12 September 2026

- **Every source link NAMES its source** (§4a punkt 4). `a_src()` in `make_diff.py` used to print the
  bare word `Source`, which says nothing about where it goes and, on the brief, broke the `Source`
  facet because that facet is built from link labels. The script now derives `Message Center`,
  `Microsoft Learn`, `TechCommunity blog`, `MSRC`, `Azure updates`, `DeltaPulse` and the rest from the
  host. Copy the script byte for byte and this comes with it.
- **The row under the cursor is highlighted whole** — `tbody tr:hover td{background:var(--accent-soft)}`
  in the page's own CSS, so the changes page behaves like the brief the reader just came from (§5au
  item 75). This page does not stripe rows inline, so it needs no `!important`.

### Source text — what Microsoft changed INSIDE the page (§5ar)

`make_diff.py` compares the `docText` block of the two states and the page gains
`<section id="srctext">`. **A page is compared by the commit it was read at, not by how many lines
moved** — the same `+21 / −15` on a different edit is still a difference. A page that joined the
watch list today is `added`, not `changed`, so the first run carrying `docText` does not announce all
42 watched pages as edited. Removed text is `<del>`, added text is `<ins>`: **this is the only place
on either page where a REMOVAL of prose is visible**, and a detection quietly dropped from
Microsoft's own list leaves no other trace. `verify()` requires the section, and the ledger files
each edited page as ONE entry under the tab `Source text` — per page, never per line, for the same
reason endpoints are filed per permission. Say in the reply how many pages were compared, how many
moved, and by which method (`git` or `snapshot`).

4. Do not hand-write anything onto this page. If something is missing, add it to `make_diff.py` in
   `CLAUDE.md` and say so in the reply — the page is a deterministic function of two states.

# STEP 3 — CHECK THE FINISHED FILE

Before you commit anything, run python3 over `site/diff/index.html`:

- size in tens of kilobytes, never megabytes (item 34 of the §0 checklist);
- `class="tabpanel"` = 0, `data-catalog` = 0, `<script type="application/json"` = 0;
- **the evidence sits under its own row** (§3 punkt 15, new 12 Sep 2026): every item that points at
  a watched page whose text moved carries a `+` in the first column of `added` / `removed` / `changed`,
  and under it a `<tr class="det" hidden>` holding a `.s12file` block — the SAME shape SCRIPT 12 draws
  in the brief. Check three things in the reply: `button.xb[data-diff]` equals `tr class="det"`, no
  detail row is empty, and the `srctext` section no longer renders a row per line. A page an item
  carries is NOT repeated in `srctext`; what is left there are orphans — pages that moved with no item
  to their name, which is itself a finding;
- **every change block names the section that asked for it** (§5bb, new 16 Sep 2026): `file_block()`
  stamps `data-ntowner` on each `.s12file` — the item's own id under a row, `srctext` for an orphan,
  `docsdiff` for a Learn page — so a block standing outside its section can be found instead of
  guessed at. `verify()` checks the attribute is there; it is the same rule the brief obeys, and it
  exists because the owner photographed orphan `.s12file` cards in the Microsoft Learn tab with no
  date, no heading and no row to point at. **One renderer, everywhere**: `lineBox()` in SCRIPT 15 v2
  is deleted and `window.__socFileBlock` is the only one left;
- **`bytab` and `bytech` are OPEN when anything moved, and only those two** — they are controls, not
  content (§3 punkt 13). `verify()` rejects any other section that ships open, and on a day with no
  change all twelve fold;
- **the Message Center section is a VIEW over both sources** (§3 punkt 11): the index AND any item on
  this page citing an MC/RM identifier in `reference`. Until 12 Sep 2026 it counted the index alone, so
  a row could read „Teams · Message Center · published today" while the section said `0`. It is left out
  of the top totals for the same reason endpoints are — the item is already counted in its own tab;
- **AND IT HAS THREE KINDS, NOT TWO — new on 16 Sep 2026, and it is the same defect a third time.**
  An identifier that was in both states was compared BY PRESENCE only, and `mc_view()` walked `added`
  and `removed` and never `changed`, so an entry Microsoft REVISED fell through both gaps. Measured
  that evening: MC1426371 gained a second retirement date on 15 Sep and an item on this page gained
  the reference `MC1426371` where it had said "no MC/RM post — Learn only", MC1413308 was cancelled,
  the run's own summary named all of it — and the section printed `0`, `+0 / −0` and "No Message
  Center or Roadmap identifier moved". Two true sentences that together are nonsense, which is the
  thing §3 punkt 11 exists to stop. The script you copy now does three things: `diff_community()`
  compares the index **field by field** through `MC_FIELDS`, with `Action required by` first because
  a deadline that moved is the only reason anyone opens this section at 22:00; `mc_view()` also walks
  `changed`, both for an item whose `reference` moved and for an item that GAINED one — `origin`
  `gained` says so in words, because "until this run that row said there was no MC or RM post" is the
  finding; and the row carries a **`What moved`** column showing `<del>` → `<ins>` per field, since
  a row reading `revised` with no difference beside it is a sentence about a change rather than the
  change, which §4 forbids. One identifier is still ONE row: the two paths merge and `origin`
  becomes `both` or `gained`, never two rows for one number;
- **AND IT READS THE POPULATION THE STATE CARRIES, NOT THE ONE IT USED TO CARRY — the fourth cause,
  found the same evening.** The brief has built `mc.entries[]` since §5az (239 entries on 16 Sep), while
  this script was still reading `community.messageCenter[]` (201) — and MC1426371 exists in the first
  and not the second, so the comparison was looking at the wrong table, not running the wrong
  algorithm. `mc_pop()` now reads `mc.entries` when the state carries it and falls back to the index
  for a state written before §5az, `mc_src()` says which was read, and `mc_norm()` gives both shapes
  ONE set of field names (`date` ← `published`, `revisedOn` ← `updated`) so `MC_FIELDS` compares like
  with like. **`MC_FIELDS` carries `revisedOn` from this run on** — a revision moves that field and
  nothing else, and the state has been carrying it as `updated` on 201 of 201 index entries, 81 of them
  differing from `date`, for as long as the section has printed zero;
- **WHEN THE TWO STATES READ DIFFERENT POPULATIONS THE INDEX SIDE IS A BASELINE FOR ONE RUN.**
  Yesterday's state read the index and today's reads `mc.entries`: the same entries carry different
  fields on the two sides, so comparing them field by field reports ALL of them as revised. Measured
  16 Sep 2026 on the real 14 → 16 September states: **201 of 201 came out as `changed` and the section
  grew from 20 rows to 259** — the same false alarm an endpoint map without a predecessor would raise
  (§3) and the same reason §5ag writes `state:"baseline"`. So on a population shift `mcAdd`, `mcRem`
  and `mcChg` announce NOTHING and the section says so in a sentence naming both tables and both
  counts; the ITEM side still reports, because it does not depend on which table was read — and that
  is the side that caught MC1426371. After the fix the same two states give **27 rows, MC1426371 present
  as `changed` / `origin=gained`, and `verify()` clean**;
- **what this page still cannot show, and it is not an algorithm problem.** MC1413308 is absent because
  the brief never held it: the index is read page one only (`Showing 200 of 2458`), so an entry
  published in July and revised in September never enters the state at all. That is fixed on the
  BUILDING side — §5az's revision sweep and gate item 92 — and until a brief carries
  `mc.revisionSweep`, say so in the reply rather than reporting a quiet Message Center;
- **`verify()` refuses a page that loses a cited identifier.** Every `MC…`/`RM…` printed in a
  `<span class="ref">` by a moved item must have a row in `mcenter`. It cannot fire on a quiet day —
  no moved item cites one, so the set is empty and the check passes — which is the whole point of
  writing it that way (§0b: an assertion that fires on a correct page is as useless as one that never
  fires);
- **AND THE PAGE MUST NOT SAY `0 added` OVER A MESSAGE CENTER SECTION SAYING `+9` — new on
  17 Sep 2026 (§3 punkty 17-20, items 99-102).** The evening Delta carried nine new Message Center
  entries, an empty `Added since` section and three tiles reading zero. Nothing was wrong with the
  data: the §3a exclusion of Message Center from the three totals is UNCONDITIONAL while its
  justification — "the item is already counted in its own tab" — is CONDITIONAL, and that evening
  all nine entries had `origin: index`, so they were cited by no item and counted nowhere at all.
  `bytech` did not apply the exclusion in the first place. Four things change, and each has its own
  gate item that `verify()` owns:
  - **99 (class A)** — the Message Center tile carries `+A / −R / C` from `mc_view()` and equals the
    `bytab` row, the section chip and the table caption; a tile stating a movement the page does not
    list, or listing one the tile does not state, exits 1;
  - **100 (class A)** — the exclusion is NAMED with numbers wherever a total is printed. The tile
    note and the empty `Added since` both say how many Message Center entries arrived in the same
    window and where they are; a zero with no sentence is the defect, not the zero;
  - **101 (class B)** — the Message Center table opens `What | ID | Published | Revised | …`.
    `Published` used to be the eighth of eight columns, off the right edge of a scrolling table, and
    `Revised` did not exist at all — the date lived in prose. Merill prints both on every message
    page, and a missing one prints `not printed at source` / `not stated at source`, never a blank;
  - **102 (class B)** — `nav.dsubnav` is TWO labelled rows in the sticky block (`What moved`, six;
    `Where from`, eight), the shape §5ae variant B gave the brief, and the rail highlights the
    destination after a programmatic jump. `mark()` keys `aria-current` off scroll position and runs
    on `scroll` only, so `goto_()` and `focusSection()` — which change every `offsetTop` after the
    handler last ran — left the reader in a section the rail did not mark. `markOne()` is called by
    both, and it scrolls the rail's own horizontal overflow so the marked row is visible;
- **FOURTEEN sections present, each of them a `<details class="dsec">`**, exactly one `<!DOCTYPE`:
  `bytab`, `bytech`, `deadlines`, `added`, `removed`, `changed`, `components`, `endpoints`,
  `catalog`, `community`, `mcenter`, `srctext`, **`docsdiff`** and **`blogsdiff`** (§5aw).
  `verify()` counts both the names and the fourteen folds; read the list from its own `for need in (...)` rather than from this line, which named ten
  until 12 September 2026 and would have let a page through missing `bytech` and `deadlines`;
- the three tiles equal the sums of the `Added` / `Removed` / `Changed` columns of `bytab`, and the
  endpoint tile equals the `Graph endpoints` row — `verify()` checks this, and so do you, in the reply;
- `s9find` and the search script are in the file, so every table can be searched and filtered;
- **`#bytab` holds ELEVEN rows — New, Deadlines, Graph API, Graph endpoints, Roles, Component versions,
  Community articles, Message Center, Source text, Microsoft Learn, Microsoft Blogs — even when every
  one of them is a zero** (§3a).
  A row of three zeros means "checked, nothing moved"; a missing row means "not known", and those
  are different answers. The list is `SUMMARY_TABS` in `make_diff.py`: count it there rather than
  from this sentence, because a number written into a prompt goes stale the day a row is added, and
  `Source text` was added on 11 September 2026 and the two §5aw tabs on 14 September;
- **the two new tabs are NAMED, never counted** (§5aw). `docsdiff` lists every `what's new` change
  that arrived or went away, matched by its area and its title because Microsoft gives it no id,
  every area whose read method or status moved, and every watched documentation page whose TEXT
  moved — **compared by the commit it was read at, not by how many lines moved**, in the same
  `.s12file` shape §5ar uses. `blogsdiff` names every article added and removed **with its title
  and its link**, and every blog whose `status`, read method or channel id moved; **a blog that
  went from `ok` to `failed` is the first row**. A first run whose previous state carries no `nt`
  key says so in one sentence and announces nothing as added — no reference point is not a change;
- **every catalog entry written to the ledger carries `surface`** (§5al, new 10 Sep 2026). The
  `graph` array is not Microsoft Graph — §5f puts every inventoried API surface in it — so without
  that field the brief's Graph API tab lists `vso.*` Azure DevOps names as Graph changes. `ledger()`
  fills it from the catalog; check it in the reply with a count per surface for today's entries;
- **the `community` section NAMES what changed, it does not count it** (§5an, gate item 62): every added
  and removed article appears with its title AND its link, sources added, removed or **renamed** sit in
  their own table — a rename keeps its URL and is ONE row, never an add plus a removal — and a source that
  went from `ok` to `failed` is the FIRST row of the third table, because that is the change worth acting
  on. A source added to or dropped from the list is a change to the LIST, not to an article: it has its
  own tile and is not mixed into the article counters. **First run with `community` in the state announces
  a baseline, not 187 additions** — no previous block means no comparison, exactly like `graphMap` on its
  first day. The `mcenter` section lists Message Center and Roadmap entries by identifier, technology and
  `actionRequiredBy`, with the dated ones first;
- **every tab with a non-zero counter in `#bytab` has a table below carrying its name in a
  `<caption class="tabcap">`** — `verify()` asserts this, because a summary nothing covers is worse
  than no summary. Measured 3 Sep 2026: New +7 (Entra · M365 admin · Dynamics 365), Deadlines 0/0/0,
  Graph API +35, Roles 0/0/0, page 15,562 B;
- **every row of the `changed` section carries a `<del>` or an `<ins>`** — do NOT compare the two
  counts with each other: a field that did not exist before has only `<ins>` and the words "not set"
  on the left (measured: 250 rows, 225 with `<ins>` alone, zero with neither);
- an anchor to `/` is present (shared rule 3: the changes page links to `/`, never to itself) — and
  **the one in the FOOTER goes there too.** Measured 12 Sep 2026 on the published page: it pointed at
  `srctext`, i.e. `/diff/srctext`, a 404, because a loop variable shadowed `build()`'s `home` parameter.
  The old assertion passed because it asked whether ANY link on the page went to `/`, and the dateline's
  does — an assertion that passes for the wrong reason is worse than none;
- **the theme switch survived**: `id="themebtn"` and the `soc-diff-theme` key are both in the file.
  The stylesheet carries both themes, so a page without the button locks the reader into whatever
  the system chose — the owner reported exactly that on 3 Sep 2026. `verify()` blocks it too.

If Playwright is available, render 1400x1000 in light and dark and 390x844: **no console or page
errors**, `document.documentElement.scrollWidth === clientWidth` at both widths, `del` and `ins`
have non-transparent backgrounds in both themes, and **clicking `#themebtn` flips `body`'s computed
background and sets `data-theme`, a second click flips it back, and the choice survives a reload**. Skip it and say so when Playwright is missing —
that is not a reason to stop the run.

# STEP 4 — HISTORY, COMMIT, PROOF

1. Move the previous version: `git mv site/diff/index.html site/history/YYYY-MM-DD-HHMM-diff.html`
   **before** writing the new one (rule 4). Never delete anything from `history/`.
2. `BEFORE=$(git rev-parse origin/main)`.
3. `git pull --rebase origin main` — two runs write to the same repository and can collide.
4. Commit: `content: routine zmian <YYYY-MM-DD HH:MM>`. Push **by ONE of two routes, both normal**:
   a. `git push origin HEAD:main` — the direct route. Use it when it is accepted.
   b. When the session may push only its own `claude/…` branch, push that branch and nothing else.
      `.github/workflows/publish.yml` fires on `claude/**`, takes `site/` from the branch, commits it
      to `main` as `content: publikacja z <branch>` and deploys the site. **This is the publication,
      not a missing merge**: nobody has to merge anything by hand. Never push by both routes — the
      page would ship twice.
5. **PROVE IT ON `main`, whichever route you used.** `git fetch origin`,
   `AFTER=$(git rev-parse origin/main)`.
   **Since 21 Oct 2026 (`CLAUDE.md` §5eq) your page does NOT stay at `site/diff/index.html` on `main`.**
   That address now serves the "What changed" app (about 37 kB), and every publication moves the page
   you wrote to **`site/diff/full.html`** — the "Full comparison (all fields)" link on `/diff/` — byte for
   byte (`tools/changes_page.py`, run by `publish.yml` and by `code-refresh.yml`). A 37 kB
   `site/diff/index.html` on `main` is therefore the app, NOT a lost page — never report it as an overwrite
   and never push again to "fix" it. Measured 23 Oct 2026: the routine's 340,449 B page was identical,
   byte for byte, to `site/diff/full.html` on `main`, while the reply said the workflow had overwritten it.
   - Route a: `AFTER` must differ from `BEFORE` and equal your `HEAD`. (Within minutes `Code refresh`
     moves your page to `site/diff/full.html` the same way — that is expected.)
   - Route b: `publish.yml` needs about a minute. Poll every 20 seconds, for at most 4 minutes:
     `git fetch origin && git diff --quiet HEAD:site/diff/index.html origin/main:site/diff/full.html`.
     The run is proven when that command exits 0 and `AFTER` differs from `BEFORE` — `AFTER` is then the
     workflow's commit, not your `HEAD`, and that is correct.
   - `AFTER` equal to `BEFORE` after the wait (route b) or straight away (route a) means the run
     FAILED, and you say so plainly, with the branch name and the last commit of `origin/main`.
6. **The run is finished when today's page is on `origin/main` — as `site/diff/full.html` after
   `publish.yml` (route b), or as `site/diff/index.html` right after your direct push (route a) —
   not when a push succeeded.** If what you pushed is anything else — a leftover commit from an earlier
   session, an archive, a ledger line — the run is NOT done: go on to STEP 2. Measured 23 Sep 2026: a
   resumed session pushed a leftover mirror commit, called the turn done, and `make_diff.py` never ran.

# STEP 5 — REPLY

Under ten lines:

- the `/diff/` URL and **what was compared with what** (the label and both dates);
- the numbers from the pills: added / removed / changed / deadlines moved / ± permissions / ± roles;
- **the `What changed, by tab` table copied as four short lines** — that is the answer to "where did
  it move", and it is why the page exists;
- **every added and every removed item as one bullet with its link** — that is the substance of this reply;
- deadline moves as `before → after`, because those are what rearrange the week;
- the file size in kB — the proof that this is a diff and not a copy of the brief;
- `BEFORE` and `AFTER` and **the route** (`direct to main` or `branch <name> → publish.yml → main`),
  and when they are equal, the sentence saying the run failed. **Never report a 37 kB
  `site/diff/index.html` on `main` as an overwrite — it is the "What changed" app; your page is
  `site/diff/full.html` (STEP 4 point 5).** **Never write "pushed to a branch, not
  main, needs merging" for route b once STEP 4 point 5 proved the page on `origin/main`** — measured 30 Sep
  and 1 Oct 2026: the reply said "NOT origin/main — it needs merging" while `publish.yml` had already
  published the page a minute after the push, and the owner was told to do work that was done.

**Below that, print the `CLAUDE.md` §0 checklist.** Most items are `n/d` for this page because they
describe the main page — **print them with that reason, never skip them in silence**.
**Item 79 is never `n/d`:** read the §0f register out of `CLAUDE.md` and print every entry whose
state is not `ZBUDOWANE`, by name, with its state and what is missing. This page runs no `gate.py`,
so nothing prints it for you — and an agreed item nobody names is an agreed item nobody builds,
which is exactly how two agreed tabs went missing for two days (§0f, 13 Sep 2026). **And the other
half of that rule, new on 16 Sep 2026: THE RUN THAT BUILDS A REGISTERED ITEM PROMOTES IT TO
`ZBUDOWANE` IN THAT SAME RUN**, on two conditions — the thing is on the page this run published, and
the §0 item that guards it came back `OK`. For this page that means items 34, 62, 78 and 99-102,
the seven `verify()` owns. A thing nobody guards is never `ZBUDOWANE`: promote its gate item first. Sixteen
entries sat at `ZASPECYFIKOWANE` on 16 Sep while their gate items were green all day, so the register
said the opposite of the checklist printed beside it. Binding for
this run is **item 34** (computed not mirrored, no tabs, no catalog, no JSON, under 900 kB),
**item 62** (community and Message Center named, not counted), **item 78** (Advanced filtering on
this page) and **items 99-102** (the Message Center tile matches the section; the exclusion is named
with numbers; the MC table opens `What | ID | Published | Revised`; the rail is two labelled rows and
marks the destination after a jump) — the seven the main-page gate never sees, all enforced by
`verify()` in `make_diff.py`,
whose exit code 1 means DO NOT PUBLISH — plus the items this page really carries: 16 (`linkStatus` —
zero `a.lnk-dead` anchors), 21 (Sources — if you report anything about sources at all) and 64 (the
filter banner is there, names every filter and is green).

## Component versions in the diff (added 6 September 2026)

`make_diff.py` now compares the `components` array of the two states as well, and the page gains a `<section id="components">`. Three things to check in the reply:

- the by-tab summary carries a `Component versions` row, zeros included — it is one of the nine
  rows of `SUMMARY_TABS` (this line said "five rows" until 12 September 2026, which was true on
  the day it was written and wrong from the day `Graph endpoints` was added);
- comparison is **per platform** — Authenticator moving on iOS but not on Android is ONE row, not two;
- `verify()` requires the `components` section, so a page without it exits 1 and must not be published;
- **where a version moved, the page prints what the new release contains** in a `div.relnew` block under
  the table &mdash; group headings and the vendor's bullets, capped at 20 with an `and N more in this release`
  line. Check it is there: a version row without its release block answers "it moved" and not "what it
  brings", and the second question is the one an administrator acts on. A component whose version did NOT
  move has no block, and that is correct.

Measured 6 September 2026 on four inputs: GSA `2.32.294 -> 2.33.101` with three new bullets renders one
table row plus one `relnew` block, 12,071 B; a release of 26 bullets renders 20 plus `and 6 more in this
release`; a newly tracked component renders a `not tracked -> ...` row plus its current release; two
identical states render zero blocks and the sentence `No tracked component moved.`. Zero console or page
errors and no horizontal scrolling in light and dark at 1400 and 390 px.