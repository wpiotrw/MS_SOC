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
     is written to <out>/data/page/<page>-<id>.<hash>.json; the very same element (same id, same type, same text) is put
     back at the same place before any script that follows runs - so those scripts, written for an inline block, find
     it exactly where they always did (5dl read it synchronously; since 5ds asynchronously, points 4-5 below);
  3. the file name carries a hash of its content, so a cached copy can never pair a new page with old data.
If the request fails the loader says so on the page instead of leaving "Loading..." forever.

5ds (14 X 2026) - the data is read WITHOUT blocking the phone. Owner, 14 X: "on mobile browsers the page loads very slowly
or nothing can be clicked, reloading does not help, empty black fields". Cause: the synchronous read of 5dl. While a
phone downloads 1.2 MB (compressed) of data, a synchronous request holds the page's only thread: Safari still scrolls,
but paints nothing new (black or empty bands below what was painted), no tap is handled, and "Loading today's brief..."
stays until the data and all scripts are done. Now:
  4. a tiny script at the top of <head> starts the download of every data file at once (fetch, asynchronous; one retry
     after 1.5 s), so the download runs while the 2.6 MB page itself is still arriving and being painted;
  5. every script after the first data block keeps its text but gets type="text/x-s5ds", so the browser does not run
     it while parsing; at the end of <body> a runner waits for the data, puts the JSON elements back at their places,
     then runs the scripts in their original order, one per task (the phone paints and handles taps between them).
     While they run, document.readyState reads "loading" and DOMContentLoaded listeners are collected, then called
     one per task in the order they were added - the same order the browser would have used, so no script sees an
     earlier or later state than it was written for (52 scripts use readyState === "loading" -> DOMContentLoaded);
  6. the Google Fonts stylesheet no longer blocks the first paint (media=print, switched to all when it loads; the
     fonts already used display=swap);
  7. the data files carry a hash in their names, so the deployed staticwebapp.config.json gets one route that lets a
     browser keep them for a year ("immutable"): the second visit with unchanged data reads them from the phone. Only
     the copy in <out> is changed - site/staticwebapp.config.json stays as it is (CLAUDE.md "Czego nie robic" binds
     the routines; a route header overrides the global one, Microsoft Learn "Configure Azure Static Web Apps").
The repository copy is unchanged; only what goes to Azure Static Web Apps."""
import hashlib, json, os, re, shutil, sys

MIN = 200000
BLOCK = re.compile(r'<script type="application/json" id="([A-Za-z0-9_-]+)">(.*?)</script>', re.S)
DATA_TYPE = "text/x-s5ds-data"
LATE_TYPE = "text/x-s5ds"

# starts every download at once, before the page body arrives (5ds point 4)
STARTER = ('<script>(function(){var L=%s,D=window.__s5dsD={};'
           'function get(u){if(window.fetch)return fetch(u,{credentials:"same-origin"}).then(function(r){'
           'if(!r.ok)throw new Error("HTTP "+r.status);return r.text();});'
           'return new Promise(function(ok,no){var x=new XMLHttpRequest();x.open("GET",u,true);'
           'x.onload=function(){(x.status===200||x.status===0)?ok(x.responseText):no(new Error("HTTP "+x.status));};'
           'x.onerror=function(){no(new Error("network"));};x.send(null);});}'
           'function one(u){return get(u).catch(function(){return new Promise(function(r){setTimeout(r,1500);})'
           '.then(function(){return get(u);});});}'
           'for(var i=0;i<L.length;i++)D[L[i][0]]=one(L[i][1]);})();</script>')

# waits for the data, restores the JSON elements, runs the held scripts in order, one per task (5ds point 5)
RUNNER = r"""<script>(function(){
var D=window.__s5dsD||{},ids=[],ps=[],k;for(k in D){ids.push(k);ps.push(D[k]);}
function fail(e){if(window.console)console.error("[page data]",e);var p=document.createElement("p");p.className="s5dl-fail";
p.style.cssText="margin:16px;padding:12px;border:1px solid #d33;border-radius:8px";
p.appendChild(document.createTextNode("The data of this page did not load. "));var b=document.createElement("button");
b.type="button";b.textContent="Reload the page";b.onclick=function(){location.reload();};p.appendChild(b);
(document.body||document.documentElement).insertBefore(p,(document.body||document.documentElement).firstChild);}
function ev(){try{return new Event("DOMContentLoaded");}catch(e){var x=document.createEvent("Event");x.initEvent("DOMContentLoaded",false,false);return x;}}
function exec(old){var s=document.createElement("script"),a=old.attributes,i;for(i=0;i<a.length;i++)if(a[i].name!=="type")s.setAttribute(a[i].name,a[i].value);
s.text=old.text;old.parentNode.replaceChild(s,old);}
function run(){var dcl=[],t0=Date.now();
var late=[].slice.call(document.querySelectorAll('script[type="LATE_TYPE"]'));
try{Object.defineProperty(document,"readyState",{configurable:true,get:function(){return "loading";}});}catch(e){}
document.addEventListener=function(t,f){if(t==="DOMContentLoaded"){dcl.push([document,f]);return;}return Document.prototype.addEventListener.apply(this,arguments);};
window.addEventListener=function(t,f){if(t==="DOMContentLoaded"){dcl.push([window,f]);return;}return Window.prototype.addEventListener.apply(this,arguments);};
var T=window.__s5dsT=[];late.forEach(function(s,n){setTimeout(function(){var a=Date.now();try{exec(s);}catch(e){if(window.console)console.error("[s5ds]",e);}T.push(["script "+n,Date.now()-a]);},0);});
setTimeout(function(){try{delete document.addEventListener;delete window.addEventListener;delete document.readyState;}catch(e){}
var E=ev();dcl.forEach(function(p,n){setTimeout(function(){var a=Date.now();try{if(typeof p[1]==="function")p[1].call(p[0],E);else if(p[1]&&p[1].handleEvent)p[1].handleEvent(E);}
catch(e){if(window.console)console.error("[s5ds DOMContentLoaded]",e);}T.push(["ready "+n,Date.now()-a,String(p[1]).slice(0,60)]);},0);});
setTimeout(function(){window.__s5dsDone=Date.now()-t0;},0);},0);}
function go(){Promise.all(ps).then(function(txt){for(var i=0;i<ids.length;i++){var ph=document.querySelector('script[type="DATA_TYPE"][data-id="'+ids[i]+'"]');
var s=document.createElement("script");s.type="application/json";s.id=ids[i];s.textContent=txt[i];if(ph)ph.parentNode.replaceChild(s,ph);else document.body.appendChild(s);}
run();},fail);}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",go);else go();
})();</script>""".replace("DATA_TYPE", DATA_TYPE).replace("LATE_TYPE", LATE_TYPE).replace("\n", "")

SCRIPT_OPEN = re.compile(r'<script\b([^>]*)>', re.I)
CLASSIC = re.compile(r'^\s*(type\s*=\s*["\']?(text/javascript|application/javascript)["\']?\s*)?$', re.I)
FONTS = re.compile(r'<link href="(https://fonts\.googleapis\.com/[^"]+)" rel="stylesheet">')


def hold_scripts(h, start):
    """type="text/x-s5ds" on every classic inline script after `start`; comments and script bodies are skipped whole"""
    out, i, n = [], start, 0
    out.append(h[:start])
    while True:
        a = h.find("<script", i)
        c = h.find("<!--", i)
        if a < 0:
            out.append(h[i:])
            break
        if 0 <= c < a:
            e = h.find("-->", c + 4)
            e = len(h) if e < 0 else e + 3
            out.append(h[i:e])
            i = e
            continue
        m = SCRIPT_OPEN.match(h, a)
        if not m:
            out.append(h[i:a + 7])
            i = a + 7
            continue
        end = h.lower().find("</script", m.end())
        end = len(h) if end < 0 else end
        attrs = m.group(1)
        out.append(h[i:a])
        if CLASSIC.match(attrs) and "src=" not in attrs.lower():
            rest = re.sub(r'\s*type\s*=\s*["\']?[^"\'\s>]*["\']?', "", attrs, flags=re.I)
            out.append('<script type="%s"%s>' % (LATE_TYPE, rest))
            n += 1
        else:
            out.append(m.group(0))
        out.append(h[m.end():end])
        i = end
    return "".join(out), n


def split(html_path, root):
    h = open(html_path, encoding="utf-8").read()
    rel_dir = os.path.relpath(os.path.join(root, "data", "page"), os.path.dirname(html_path)).replace(os.sep, "/")
    stem = os.path.splitext(os.path.basename(html_path))[0]
    os.makedirs(os.path.join(root, "data", "page"), exist_ok=True)
    moved, urls = [], []

    def rep(m):
        bid, body = m.group(1), m.group(2)
        if len(body) < MIN:
            return m.group(0)
        hx = hashlib.sha256(body.encode("utf-8")).hexdigest()[:12]
        name = "%s-%s.%s.json" % (stem, bid, hx)
        open(os.path.join(root, "data", "page", name), "w", encoding="utf-8").write(body)
        moved.append((bid, len(body)))
        urls.append([bid, rel_dir + "/" + name])
        return '<script type="%s" data-id="%s"></script>' % (DATA_TYPE, bid)

    out = BLOCK.sub(rep, h)
    held = 0
    if moved:
        first = out.find('<script type="%s"' % DATA_TYPE)
        out, held = hold_scripts(out, first)
        hm = re.search(r'<meta charset[^>]*>', out[:4000], re.I) or re.search(r'<head[^>]*>', out, re.I)
        starter = STARTER % json.dumps(urls)
        out = out[:hm.end()] + starter + out[hm.end():] if hm else starter + out
        b = out.lower().rfind("</body>")
        out = out[:b] + RUNNER + out[b:] if b >= 0 else out + RUNNER
        out = FONTS.sub(lambda m: '<link href="%s" rel="stylesheet" media="print" onload="this.media=\'all\'">'
                        '<noscript><link href="%s" rel="stylesheet"></noscript>' % (m.group(1), m.group(1)), out, count=1)
        open(html_path, "w", encoding="utf-8").write(out)
    return moved, len(h), len(out), held


CACHE_ROUTE = {"route": "/data/page/*", "headers": {"cache-control": "public, max-age=31536000, immutable"}}


def cache_route(dst):
    p = os.path.join(dst, "staticwebapp.config.json")
    if not os.path.exists(p):
        return False
    cfg = json.load(open(p, encoding="utf-8"))
    routes = cfg.setdefault("routes", [])
    if any(r.get("route") == CACHE_ROUTE["route"] for r in routes):
        return False
    routes.insert(0, CACHE_ROUTE)
    json.dump(cfg, open(p, "w", encoding="utf-8"), indent=2)
    return True


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
        moved, a, b, held = split(p, dst)
        if moved:
            print("deploy_prep: %s %.1f MB -> %.1f MB, %s; %d scripts run after the data" % (os.path.relpath(p, dst), a / 1e6, b / 1e6,
                  ", ".join("%s %.1f MB" % (i, n / 1e6) for i, n in moved), held))
    if cache_route(dst):
        print("deploy_prep: staticwebapp.config.json (deployed copy) - data/page/* cached as immutable")


if __name__ == "__main__":
    main()
