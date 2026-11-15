#!/usr/bin/env python3
"""mc_related.py - related Message Center posts for every post the portal knows (CLAUDE.md 5gs, 15 XI 2026).
Author: Piotr Wisniewski.

The owner (15 XI 2026): "can we list every MC that belongs to a campaign or rollout, like mc.ai-news.cz shows
'Similar posts'? And on our Message Center list - new, old, updated AND removed posts - do we link the related
ones?" This file answers the second half with our own code, from data already in the repository:

  site/data/<newest brief>.json   Message Center entries (title, service, published, storyKey, summaries)
  site/data/mc-tenant.json        the tenant's posts (summary, "when", "prepare", dated sentences) and the
                                  change log with REMOVED posts (a removed post keeps its title here)
  site/data/campaigns.json        campaigns and their member posts (tools/campaigns.py)

For each post it writes the related posts, each with ONE reason, strongest first:
  camp     same campaign (the campaign's name is in "camps")
  cites    this post names the other by number in its text
  citedby  the other post names this one by number
  story    the same story key in the brief (one change seen in several sources)
  similar  the same service and close wording (TF-IDF cosine of title + summary >= MIN_SIM; at most TOP_SIM)

Output site/data/mc-related.json:
  {"generated", "rule", "counts", "posts": {id: [title, service, published, state, removedOn]},
   "camps": {campaignId: [name, type]}, "inCamp": {id: [campaignId, ...]}, "rel": {id: [[otherId, reason], ...]}}
state: "" for a post Microsoft still lists, "removed" for a post that left the tenant's Message Center.
Exit code 0 always when the inputs were read; a missing campaigns file only drops the "camp" reason.
"""
import glob
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "site", "data")
MIN_SIM = 0.30
TOP_SIM = 5
MAX_CAMP = 40
IDRE = re.compile(r"\bMC\d{5,8}\b")
STOP = set("""a an and are as at be been but by can for from has have in into is it its may more new not now of on or our
that the their there these this to updated update updates use used users user using via was we were what when which
who will with you your microsoft general availability available preview public plan change changes coming retirement
""".split())


def jload(p, d=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def newest_state():
    files = sorted(f for f in glob.glob(os.path.join(DATA, "20[0-9][0-9]-[01][0-9]-[0-3][0-9].json")))
    for f in reversed(files):
        d = jload(f)
        if d:
            return d.get("soc-brief-state", d), os.path.basename(f)
    return {}, None


def clean(t):
    t = re.sub(r"^\s*\((?:updated|retirement|deferred|reminder|update)\)\s*", "", t or "", flags=re.I)
    return re.sub(r"\s+", " ", t).strip()


def toks(text):
    return [w for w in re.findall(r"[a-z][a-z0-9+#.-]{2,}", (text or "").lower()) if w not in STOP]


def main(out):
    st, sname = newest_state()
    ten = jload(os.path.join(DATA, "mc-tenant.json"), {}) or {}
    camp = jload(os.path.join(DATA, "campaigns.json"), {}) or {}
    tmsg = {m["id"]: m for m in ten.get("messages") or [] if m.get("id")}
    removed = {}
    for c in ten.get("changes") or []:
        if c.get("type") == "removed" and c.get("id") and c["id"] not in tmsg:
            removed[c["id"]] = {"title": c.get("title"), "on": c.get("date")}

    posts, text, svc, story = {}, {}, {}, {}
    for e in (st.get("mc") or {}).get("entries") or []:
        i = e.get("id") or ""
        if not IDRE.fullmatch(i):
            continue
        tm = tmsg.get(i, {})
        services = tm.get("services") or e.get("tech") or []
        posts[i] = [clean(e.get("title") or tm.get("title")), ", ".join(services), e.get("published") or tm.get("start") or "",
                    "removed" if i in removed else "", (removed.get(i) or {}).get("on") or ""]
        text[i] = " ".join(str(x or "") for x in (e.get("dpSummary"), e.get("feedSummary"), tm.get("summary"), tm.get("when"),
                                                    tm.get("prepare"), " ".join(tm.get("dates") or [])))
        svc[i] = {s.lower() for s in services}
        if e.get("storyKey"):
            story[i] = e["storyKey"]
    for i, tm in tmsg.items():
        if i in posts:
            continue
        posts[i] = [clean(tm.get("title")), ", ".join(tm.get("services") or []), tm.get("start") or "", "", ""]
        text[i] = " ".join(str(x or "") for x in (tm.get("summary"), tm.get("when"), tm.get("prepare"), " ".join(tm.get("dates") or [])))
        svc[i] = {s.lower() for s in tm.get("services") or []}
    for i, r in removed.items():
        if i in posts:
            continue
        posts[i] = [clean(r["title"]), "", "", "removed", r["on"] or ""]
        text[i] = ""
        svc[i] = set()

    rel = defaultdict(dict)   # id -> {other: reason}; the first (strongest) reason wins
    RANK = {"camp": 0, "cites": 1, "citedby": 2, "story": 3, "similar": 4}

    def add(a, b, why):
        if a == b or b not in posts:
            return
        old = rel[a].get(b)
        if old is None or RANK[why] < RANK[old]:
            rel[a][b] = why

    # campaigns
    camps, in_camp = {}, defaultdict(list)
    for c in camp.get("campaigns") or []:
        mem = [m for m in c.get("members") or [] if IDRE.fullmatch(m)]
        if len(mem) < 1:
            continue
        camps[c["id"]] = [c.get("name") or c["id"], c.get("type") or ""]
        for m in mem:
            if m in posts:
                in_camp[m].append(c["id"])
        if len(mem) <= MAX_CAMP:
            for a in mem:
                for b in mem:
                    add(a, b, "camp")
    # numbers named in the text
    for a, t in text.items():
        named = set(IDRE.findall(t)) - {a}
        if len(named) > 6:      # a round-up post names everything; it is not a relation
            continue
        for b in named:
            add(a, b, "cites")
            add(b, a, "citedby")
    # story keys
    groups = defaultdict(list)
    for i, k in story.items():
        groups[k].append(i)
    for k, ids in groups.items():
        if 1 < len(ids) <= 12:
            for a in ids:
                for b in ids:
                    add(a, b, "story")
    # similar wording within the same service
    docs = {i: Counter(toks(posts[i][0] + " " + posts[i][0] + " " + text.get(i, "")[:600])) for i in posts}
    df = Counter(t for c in docs.values() for t in c)
    n = max(1, len(docs))
    vec = {}
    for i, c in docs.items():
        v = {t: (1 + math.log(f)) * math.log(n / (1 + df[t])) for t, f in c.items() if df[t] > 1}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vec[i] = {t: x / norm for t, x in v.items()}
    by_svc = defaultdict(list)
    for i, s in svc.items():
        for x in s or {""}:
            by_svc[x].append(i)
    for a in posts:
        cand = set()
        if svc[a]:
            for x in svc[a]:
                cand.update(by_svc[x])
        else:   # a removed post keeps only its title: compare it with every post
            cand = set(posts)
        cand.discard(a)
        va = vec[a]
        sims = []
        for b in cand:
            vb = vec[b]
            s = sum(w * vb.get(t, 0.0) for t, w in va.items())
            if s >= MIN_SIM:
                sims.append((s, b))
        for s, b in sorted(sims, reverse=True)[:TOP_SIM]:
            add(a, b, "similar")

    def key(a, b, why):
        return (RANK[why], -(posts[b][2] > "" and int(re.sub(r"\D", "", posts[b][2] or "0") or 0)))
    out_rel = {}
    for a, d in rel.items():
        if d:
            out_rel[a] = [[b, w] for b, w in sorted(d.items(), key=lambda kv: key(a, kv[0], kv[1]))]
    cnt = Counter(w for d in rel.values() for w in d.values())
    res = {"generated": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "state": sname,
           "rule": "Related posts, strongest reason first: same campaign; names the other by number; named by the other; "
                   "same story in the brief; same service and close wording (TF-IDF cosine >= %.2f, at most %d)." % (MIN_SIM, TOP_SIM),
           "counts": {"posts": len(posts), "withRelated": len(out_rel), "removed": sum(1 for p in posts.values() if p[3]),
                      "links": dict(cnt)},
           "posts": posts, "camps": camps, "inCamp": dict(in_camp), "rel": out_rel}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, separators=(",", ":"))
    print("mc_related: %d posts, %d with related, %d removed, links %s -> %s (%d B)"
          % (len(posts), len(out_rel), res["counts"]["removed"], dict(cnt), out, os.path.getsize(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(DATA, "mc-related.json"))
