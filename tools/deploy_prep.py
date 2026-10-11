#!/usr/bin/env python3
"""deploy_prep.py - the copy of site/ that goes to Azure Static Web Apps, with the big data blocks as files.

  python3 tools/deploy_prep.py site _deploy

Why (CLAUDE.md 5dl, 11 X 2026): the published page carries its data inline - two <script type="application/json">
blocks of 8.9 MB and 5.3 MB. Measured that day, same page, same machine: Chromium tokenizes them in 0.36 s, WebKit -
the engine of every browser on an iPhone - in 4.7 s, before a single script can run; on a phone it is several times
that, and Safari ran out of time or memory ("loads or it does not", empty sections, a bar left in the middle of an
unpainted screen). Read as a file instead, the same page reached DOMContentLoaded in 1.6 s in WebKit instead of 6.9 s,
with the same 127 249 elements.

What it does, and nothing more:
  1. copies <site> to <out> (the repository keeps the full page: the gate, code_refresh.py, make_diff --morning and
     every routine read site/index.html as before);
  2. in <out>/index.html and in every uncompressed page under <out>/history/, each JSON block over 200 000 characters
     is written to <out>/data/page/<page>-<id>.<hash>.json and replaced by a short script that reads that file
     SYNCHRONOUSLY and puts back the very same element (same id, same type, same text) at the same place - so the
     scripts that follow, written for an inline block, find it exactly where they always did;
  3. the file name carries a hash of its content, so a cached copy can never pair a new page with old data.
If the request fails the loader says so on the page instead of leaving "Loading..." forever.
"""
import hashlib, os, re, shutil, sys

MIN = 200000
BLOCK = re.compile(r'<script type="application/json" id="([A-Za-z0-9_-]+)">(.*?)</script>', re.S)


def loader(bid, url):
    return ('<script>(function(){var id=%s,u=%s;try{var x=new XMLHttpRequest();x.open("GET",u,false);x.send(null);'
            'if(x.status!==200&&x.status!==0)throw new Error("HTTP "+x.status);'
            'var s=document.createElement("script");s.type="application/json";s.id=id;s.textContent=x.responseText;'
            'var c=document.currentScript;c.parentNode.insertBefore(s,c);}catch(e){'
            'if(window.console)console.error("[page data] "+u,e);'
            'var p=document.createElement("p");p.className="s5dl-fail";p.style.cssText="margin:16px;padding:12px;border:1px solid #d33;border-radius:8px";'
            'p.textContent="The data of this page did not load ("+u+"). Reload the page.";'
            '(document.body||document.documentElement).appendChild(p);}})();</script>') % (repr(bid).replace("'", '"'), repr(url).replace("'", '"'))


def split(html_path, root):
    h = open(html_path, encoding="utf-8").read()
    rel_dir = os.path.relpath(os.path.join(root, "data", "page"), os.path.dirname(html_path)).replace(os.sep, "/")
    stem = os.path.splitext(os.path.basename(html_path))[0]
    os.makedirs(os.path.join(root, "data", "page"), exist_ok=True)
    moved = []

    def rep(m):
        bid, body = m.group(1), m.group(2)
        if len(body) < MIN:
            return m.group(0)
        hx = hashlib.sha256(body.encode("utf-8")).hexdigest()[:12]
        name = "%s-%s.%s.json" % (stem, bid, hx)
        open(os.path.join(root, "data", "page", name), "w", encoding="utf-8").write(body)
        moved.append((bid, len(body)))
        return loader(bid, rel_dir + "/" + name)

    out = BLOCK.sub(rep, h)
    if moved:
        open(html_path, "w", encoding="utf-8").write(out)
    return moved, len(h), len(out)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst, symlinks=False)
    pages = [os.path.join(dst, "index.html")]
    hist = os.path.join(dst, "history")
    if os.path.isdir(hist):
        pages += [os.path.join(hist, f) for f in sorted(os.listdir(hist)) if f.endswith(".html")]
    for p in pages:
        if not os.path.exists(p):
            continue
        moved, a, b = split(p, dst)
        if moved:
            print("deploy_prep: %s %.1f MB -> %.1f MB, %s" % (os.path.relpath(p, dst), a / 1e6, b / 1e6,
                  ", ".join("%s %.1f MB" % (i, n / 1e6) for i, n in moved)))


if __name__ == "__main__":
    main()
