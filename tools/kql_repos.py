#!/usr/bin/env python3
"""kql_repos.py - Kusto (KQL) hunting queries from public community repositories (CLAUDE.md 5eu, 21 X 2026).

    python3 tools/kql_repos.py [--force]       # once a day (cache/kql-repos.json remembers the last run)

Owner, 21 X 2026: "the KQL tab - make sure it is updated and the queries are written to JSON; collect KQL from the
community too; store the full text and the link". The repositories are listed in kql_sources.json (Kind "git"):
each is cloned shallow; every Markdown fence ```kql / ```kusto, every .kql/.txt file and every YAML `query: |` that
is Kusto (tools/kql_extract.py) becomes one entry: the full query, its title (the file's heading, the section above
the fence), description, MITRE techniques, the file's link on GitHub, the repository's licence as written in its
LICENSE file. A repository with `RecentDays` (Azure-Sentinel: thousands of rules) contributes only the files its
commits of the last N days touched.

Writes cache/kql-repos.json (all entries, firstSeen kept between runs); tools/kql_archive.py files them in site/kql/.
Exit 0 always - a repository that fails is named in the output.
"""
import datetime as dt, json, os, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kql_extract

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "kql_sources.json")
OUT = os.path.join(ROOT, "cache", "kql-repos.json")
EXT = (".md", ".kql", ".txt", ".yaml", ".yml", ".csl")


def run(args, cwd=None, timeout=600):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout, errors="replace")


def licence(d):
    for n in ("LICENSE", "LICENSE.md", "LICENSE.txt", "license", "LICENCE"):
        p = os.path.join(d, n)
        if os.path.exists(p):
            t = open(p, encoding="utf-8", errors="replace").read(400)
            for rx, name in [(r"MIT License|Permission is hereby granted, free of charge", "MIT"), (r"BSD 3-Clause", "BSD-3-Clause"),
                             (r"BSD 2-Clause", "BSD-2-Clause"), (r"Apache License", "Apache-2.0"), (r"GNU GENERAL PUBLIC LICENSE", "GPL"),
                             (r"Creative Commons", "Creative Commons"), (r"Unlicense", "Unlicense")]:
                if re.search(rx, t, re.I):
                    return name
            return "see LICENSE"
    return ""


def md_entries(text):
    """one entry per Kusto fence of a Markdown file: the file title, the section above the fence, description, MITRE"""
    title = (re.search(r"^#\s+(.+)$", text, re.M) or [None, ""])[1].strip()
    desc = re.search(r"(?is)#+\s*Description\s*\n+(.+?)(?:\n#|\Z)", text)
    desc = re.sub(r"\s+", " ", desc.group(1)).strip()[:400] if desc else ""
    mitre = sorted(set(re.findall(r"\bT\d{4}(?:\.\d{3})?\b", text)))[:8]
    out = []
    for m in re.finditer(r"(?s)```[ \t]*(?:kql|kusto|KQL|Kusto)?[ \t]*\n(.*?)```", text):
        code = m.group(1).strip()
        if not kql_extract.is_kusto(code):
            continue
        heads = re.findall(r"^#{2,4}\s+(.+)$", text[:m.start()], re.M)
        sub = heads[-1].strip() if heads else ""
        t = title + (" · " + sub if sub and sub.lower() not in title.lower() else "")
        out.append({"title": (t or sub or "Hunting query")[:160], "query": code, "description": desc, "mitre": mitre})
    return out


def yaml_entry(text):
    m = re.search(r"(?ms)^query:\s*[|>][-+]?\s*\n(.*?)(?=^\S|\Z)", text)
    if not m:
        return []
    lines = m.group(1).splitlines()
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    code = "\n".join(l[ind:] for l in lines).strip()
    if not kql_extract.is_kusto(code):
        return []
    name = (re.search(r"(?m)^name:\s*['\"]?(.+?)['\"]?\s*$", text) or [None, ""])[1]
    desc = re.search(r"(?ms)^description:\s*[|>]?[-+]?\s*\n?(.*?)(?=^\S)", text)
    desc = re.sub(r"\s+", " ", (desc.group(1) if desc else "")).strip().strip("'\"")[:400]
    mitre = sorted(set(re.findall(r"\bT\d{4}(?:\.\d{3})?\b", text)))[:8]
    return [{"title": name[:160] or "Hunting query", "query": code, "description": desc, "mitre": mitre}]


def scan_file(path, rel):
    t = open(path, encoding="utf-8", errors="replace").read()
    if len(t) > 400000:
        return []
    if rel.lower().endswith(".md"):
        return md_entries(t)
    if rel.lower().endswith((".yaml", ".yml")):
        return yaml_entry(t)
    out = []
    for b in kql_extract.from_text(t):
        fname = os.path.splitext(os.path.basename(rel))[0].replace("_", " ").replace("-", " ").strip()
        # a comment is a title only when it reads as prose (commented-out code "//| where ..." is not)
        com = [l.strip()[2:].strip() for l in b["query"].splitlines() if l.strip().startswith("//")]
        com = [c for c in com if re.match(r"^[A-Za-z][A-Za-z0-9 ,'()/:&.-]{12,120}$", c) and not re.search(r"==|\||http", c)]
        out.append({"title": (fname if len(fname) >= 8 or not com else com[0])[:160],
                    "query": b["query"], "description": "", "mitre": sorted(set(re.findall(r"\bT\d{4}(?:\.\d{3})?\b", b["query"])))[:8]})
    return out


def one(src, tmp, today):
    url, name = src["SourceURL"].rstrip("/"), src["SourceName"]
    dest = os.path.join(tmp, re.sub(r"\W+", "-", name))
    days = src.get("RecentDays")
    if days:
        since = (dt.date.fromisoformat(today) - dt.timedelta(days=int(days))).isoformat()
        r = run(["git", "clone", "-q", "--shallow-since=" + since, "--filter=blob:none", "--no-checkout", url + ".git", dest], timeout=900)
        if r.returncode != 0:
            raise RuntimeError("clone: " + r.stderr[-200:])
        paths = src.get("Paths") or []
        lg = run(["git", "log", "--since=" + since, "--name-only", "--format=", "HEAD", "--"] + (paths or ["."]), cwd=dest, timeout=600)
        files = sorted({l.strip() for l in lg.stdout.splitlines() if l.strip().lower().endswith(EXT)})[:int(src.get("MaxFiles") or 400)]
        lic = ""
        try:
            lt = run(["git", "show", "HEAD:LICENSE"], cwd=dest).stdout[:400]
            lic = "MIT" if re.search(r"MIT License|Permission is hereby granted", lt) else ("see LICENSE" if lt else "")
        except Exception:
            pass
        sha = run(["git", "rev-parse", "HEAD"], cwd=dest).stdout.strip()
        out = []
        for rel in files:
            show = run(["git", "show", "HEAD:" + rel], cwd=dest, timeout=120)
            if show.returncode != 0:
                continue      # deleted since
            p = os.path.join(tmp, "f.tmp")
            open(p, "w", encoding="utf-8").write(show.stdout)
            for e in scan_file(p, rel):
                out.append(dict(e, path=rel))
        return out, lic, sha
    r = run(["git", "clone", "-q", "--depth", "1", url + ".git", dest], timeout=900)
    if r.returncode != 0:
        raise RuntimeError("clone: " + r.stderr[-200:])
    sha = run(["git", "rev-parse", "HEAD"], cwd=dest).stdout.strip()
    out = []
    for d, _, fs in os.walk(dest):
        if "/.git" in d:
            continue
        for f in fs:
            if not f.lower().endswith(EXT):
                continue
            p = os.path.join(d, f)
            rel = os.path.relpath(p, dest)
            for e in scan_file(p, rel):
                out.append(dict(e, path=rel))
    return out, licence(dest), sha


def main(argv):
    now = dt.datetime.now(dt.timezone.utc)
    today, stamp = now.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        prev = json.load(open(OUT, encoding="utf-8"))
    except Exception:
        prev = {}
    if (prev.get("run") or "")[:10] == today and "--force" not in argv:
        print("kql_repos: already read today (%d queries)" % len(prev.get("queries") or []))
        return 0
    srcs = [s for s in json.load(open(SRC, encoding="utf-8")) if s.get("Kind") == "git"]
    old = {q["key"]: q for q in prev.get("queries") or []}
    keep, rep = {}, []
    tmp = tempfile.mkdtemp(prefix="kqlrepos-")
    try:
        for s in srcs:
            r = {"name": s["SourceName"], "url": s["SourceURL"], "state": "ok", "queries": 0, "new": 0}
            try:
                found, lic, sha = one(s, tmp, today)
                initial = not any(q.get("repo") == s["SourceName"] for q in old.values())
                branch = s.get("Branch") or "HEAD"
                for e in found:
                    k = kql_extract.key(e["query"])
                    if k in keep:
                        continue
                    o = old.get(k) or {}
                    tb = kql_extract.tables(e["query"])
                    keep[k] = {"key": k, "title": e["title"], "query": e["query"], "description": e.get("description") or "",
                               "mitre": e.get("mitre") or [], "tables": tb, "product": kql_extract.product(tb),
                               "repo": s["SourceName"], "author": s.get("Author") or "", "license": lic or "not stated",
                               "path": e["path"], "link": s["SourceURL"].rstrip("/") + "/blob/" + (sha or branch) + "/" + e["path"].replace(" ", "%20"),
                               "firstSeen": o.get("firstSeen") or stamp,
                               # the first read of a repository files what it already had: archive, not "new today"
                               "initial": o.get("initial", True) if o else initial}
                    r["queries"] += 1
                    if not o:
                        r["new"] += 1
                r["license"], r["sha"] = lic or "not stated", sha[:10]
            except Exception as ex:
                r["state"], r["error"] = "failed", str(ex)[:200]
                for k, q in old.items():      # a failed read keeps what we had from that repository
                    if q.get("repo") == s["SourceName"]:
                        keep.setdefault(k, q)
            rep.append(r)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    qs = sorted(keep.values(), key=lambda q: (q["firstSeen"], q["repo"], q["title"]), reverse=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump({"run": stamp, "source": "tools/kql_repos.py (CLAUDE.md 5eu)", "repos": rep, "queries": qs},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("kql_repos: %d queries from %d repositories (%s)" % (len(qs), len(rep),
          "; ".join("%s %s %d (+%d)" % (r["name"], r["state"], r["queries"], r["new"]) for r in rep)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:
        print("kql_repos: skipped - %s" % e)
        sys.exit(0)
