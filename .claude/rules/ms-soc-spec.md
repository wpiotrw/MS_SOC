# MS_SOC: how to use CLAUDE.md (read this first)

`CLAUDE.md` in the repository root is the binding specification AND the only source of the
page code (scripts, CSS, gate, make_diff, mirror, collectors). It is about 1.9 MB, roughly
600 000 tokens — more than a session's context window. It is therefore excluded from automatic
loading (`.claude/settings.json`, `claudeMdExcludes`). Measured 28 IX 2026: the morning routine
stopped after 14 seconds with "Context window was full" while the file was auto-loaded.

Rules for every run, overriding any prompt sentence that says "read CLAUDE.md in full":

1. NEVER read `CLAUDE.md` whole — not with Read, not with `cat`. Read only the sections your
   prompt names, by line range:
   `grep -n '^## 0a\.' CLAUDE.md` gives the start; the next `^## ` or `^# ` line gives the end;
   then `sed -n '<start>,<end>p' CLAUDE.md`, or Read with offset/limit.
   List all section headings with `grep -n '^## [0-9]\+[a-z]*\. \|^# [0-9]\+\. ' CLAUDE.md`.
2. The §0 checklist is lines from `# 0.` to `## 0a.`; read it whole (it is short) when your
   prompt asks for the checklist.
3. Code is never read by eye: cut it with `extract_code.py` (§0c). Bootstrap it with this one line
   (tested 28 IX 2026, writes 28 files):
   `python3 -c "s=open('CLAUDE.md',encoding='utf-8').read();i=s.index('\"\"\"extract_code.py');a=s.rindex('\`\`\`python\n',0,i)+10;b=s.index('\n\`\`\`',i);open('extract_code.py','w').write(s[a:b])"`
   then `python3 extract_code.py CLAUDE.md <dir>`.
   The gate (`python3 gate.py <page> <site> --doc CLAUDE.md`) reads the file itself; you do not.
4. When a prompt tells you to read `/tmp/spec/CLAUDE.md` or `/tmp/mssoc/CLAUDE.md`, the same rules
   apply to that copy.
