#!/usr/bin/env python3
"""code_refresh.py - put TODAY's code from CLAUDE.md into the published page, data untouched.

  python3 tools/code_refresh.py CLAUDE.md site/index.html [<work dir, default .refresh>]

Why (28 IX 2026): code reached the site only when the next morning run rebuilt the page, so a
fix pushed at 11:00 was invisible until 07:00 the next day - and on 26-27 IX, when the mirror
routine failed, for three days. The owner chose a "code refresh" path: after a push that changes
CLAUDE.md, the workflow .github/workflows/code-refresh.yml runs this script.

What it does, and nothing more:
  1. cuts the scripts and appended.css out of CLAUDE.md with extract_code.py (bootstrapped from
     CLAUDE.md itself, the same one-liner as .claude/rules/ms-soc-spec.md);
  2. in the page, replaces the BODY of each <script> whose header names "SCRIPT N" (4-17) with
     the fresh SCRIPT N, and the appended stylesheet (from its fixed first rule to </style>)
     with the fresh appended.css;
  3. never touches the two JSON state blocks, the shell, the text or the data files.
Exit 0 with "no change" when the page already carries this code; exit 2 when a block it must
replace is not found (the page shape changed: better no refresh than a half-refreshed page).
"""
import os, re, subprocess, sys

def bootstrap(doc, work):
    os.makedirs(work, exist_ok=True)
    s = open(doc, encoding="utf-8").read()
    i = s.index('"""extract_code.py')
    a = s.rindex("```python\n", 0, i) + 10
    b = s.index("\n```", i)
    open(os.path.join(work, "extract_code.py"), "w", encoding="utf-8").write(s[a:b])
    r = subprocess.run([sys.executable, "extract_code.py", os.path.abspath(doc), "."], cwd=work,
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("extract_code.py failed:\n" + r.stdout + r.stderr)

CSS_HEAD = "@media (max-width:760px){\n  header.top{position:static}"   # first rule of appended.css since 5ae

def main():
    doc, page = sys.argv[1], sys.argv[2]
    work = sys.argv[3] if len(sys.argv) > 3 else ".refresh"
    bootstrap(doc, work)
    h = open(page, encoding="utf-8").read()
    orig = h
    changed, missing = [], []
    for n in range(4, 18):
        f = os.path.join(work, "script%d.js" % n)
        if not os.path.exists(f):
            missing.append("script%d.js not extracted" % n); continue
        new = open(f, encoding="utf-8").read().strip()
        # the LAST executable <script> whose first 1 500 characters name "SCRIPT n" and that is
        # under 1 MB (the data scripts at the top of the page mention script numbers in prose)
        best = None
        for m in re.finditer(r"<script(?![^>]*application/json)[^>]*>", h):
            end = h.find("</script>", m.end())
            if end < 0: continue
            body = h[m.end():end]
            if len(body) > 1_000_000: continue
            mm = re.search(r"SCRIPT (\d+)\b", body[:1500])
            if mm and int(mm.group(1)) == n: best = (m.end(), end)
        if not best:
            missing.append("SCRIPT %d block" % n); continue
        a, b = best
        if h[a:b].strip() != new:
            h = h[:a] + "\n" + new + "\n" + h[b:]; changed.append("SCRIPT %d" % n)
    css = open(os.path.join(work, "appended.css"), encoding="utf-8").read().strip()
    # 5co (5 X 2026): a relational selector in this page's stylesheet froze Safari for 11 s at a
    # time (124 000 nodes, tens of thousands of insertions, every one re-checked against it).
    # Measured: boot callbacks 21.3 s with four such rules, 4.6 s without. Use a class set by script.
    if ":has(" in css:
        print("NOT REFRESHED - appended.css uses a relational selector (:has), forbidden since 5co")
        sys.exit(2)
    a = h.rfind(CSS_HEAD)
    if a < 0:
        missing.append("appended.css block")
    else:
        b = h.find("</style>", a)
        if h[a:b].strip() != css:
            h = h[:a] + css + "\n\n" + h[b:]; changed.append("appended.css")
    if missing:
        print("NOT REFRESHED - not found: " + ", ".join(missing)); sys.exit(2)
    if h == orig:
        print("no change - the page already carries the code of this CLAUDE.md"); return
    open(page, "w", encoding="utf-8").write(h)
    print("refreshed: " + ", ".join(changed))

if __name__ == "__main__":
    main()
