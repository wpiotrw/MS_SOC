#!/usr/bin/env python3
"""mobile_check.py - phone regression check of the portal (CLAUDE.md 5eb, 16 X 2026).

  python3 tools/mobile_check.py <url> [--cpu 4] [--json out.json]
  e.g. python3 tools/deploy_prep.py site _deploy && (cd _deploy && python3 -m http.server 8766 &) &&
       python3 tools/mobile_check.py http://localhost:8766/

Why: the owner reviews the portal on an iPhone and reported the same two faults several times - slow loading and
sections cut off - each time after a new feature. This script is the check every UI change runs BEFORE commit:
Chromium with Playwright's "iPhone 13" profile (390 px, touch, DPR 3) and CPU throttled 4x (a conservative phone).
It prints: time to the data, to the Overview sentences, main-thread long tasks; and for EVERY tab: page-level
sideways scroll, elements running past the right edge outside a scroll box, JS errors.
Exit 1 when a tab scrolls sideways, an element runs off screen, a JS error is thrown, or the sentences take more than
--max-sentences seconds (default 25). --engine webkit runs the Safari engine (the one every iPhone browser uses);
it is installed on the owner's Windows PC in his user profile (16 X 2026: pip install --user playwright;
python -m playwright install webkit), runs at full CPU speed (no throttling) and reports no long tasks.
"""
import json, sys, time
from playwright.sync_api import sync_playwright


def arg(name, default):
    return type(default)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def main():
    url = sys.argv[1]
    cpu, maxs, engine = arg("--cpu", 4), arg("--max-sentences", 25.0), arg("--engine", "chromium")
    bad, rep = [], {"url": url}
    with sync_playwright() as p:
        bt = getattr(p, engine)
        b = bt.launch()
        dev = dict(p.devices["iPhone 13"]); dev.pop("default_browser_type", None)
        if engine != "chromium":
            dev.pop("is_mobile", None) if engine == "firefox" else None
        ctx = b.new_context(**dev)
        ctx.add_init_script("window.__lt=[];try{new PerformanceObserver(function(l){l.getEntries().forEach(function(e){window.__lt.push(e.duration)})}).observe({type:'longtask',buffered:true})}catch(e){}")
        pg = ctx.new_page()
        if engine == "chromium":
            cdp = ctx.new_cdp_session(pg); cdp.send("Emulation.setCPUThrottlingRate", {"rate": cpu})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
        t0 = time.time()
        pg.goto(url, wait_until="load", timeout=300000)
        rep["load_s"] = round(time.time() - t0, 1)
        sent = None
        for _ in range(int(maxs * 4) + 40):
            if pg.evaluate("document.querySelectorAll('#tab-overview .s5ci-ten .s5bk-3 > li').length"):
                sent = round(time.time() - t0, 1); break
            pg.wait_for_timeout(250)
        rep["sentences_s"] = sent
        if sent is None or sent > maxs:
            bad.append("Overview sentences: %s (limit %ss)" % (sent, maxs))
        pg.wait_for_timeout(3000)
        lt = pg.evaluate("window.__lt||[]")
        rep["long_tasks"] = len(lt); rep["long_tasks_ms"] = int(sum(lt))
        tabs = pg.eval_on_selector_all("[id^=tabbtn-tab-]", "e=>e.map(x=>x.id.replace('tabbtn-',''))")
        rep["tabs"] = {}
        for t in tabs:
            pg.evaluate("id=>{var b=document.getElementById('tabbtn-'+id); if(b) b.click();}", t)
            pg.wait_for_timeout(1200)
            r = pg.evaluate("""(id)=>{var p=document.getElementById(id); if(!p) return {missing:1};
              var W=document.documentElement.clientWidth, off=[];
              p.querySelectorAll('*').forEach(function(e){ if(!e.offsetParent) return; var r=e.getBoundingClientRect(); if(r.width<2||r.right<=W+2) return;
                var a=e.parentElement, scroller=false; while(a&&a!==p){var cs=getComputedStyle(a); if(/(auto|scroll)/.test(cs.overflowX)){scroller=true;break;} a=a.parentElement;}
                if(!scroller) off.push(String(e.className||e.tagName).slice(0,40)+' R'+Math.round(r.right)+' in '+String((e.parentElement||{}).className||'').slice(0,30)+' < '+String(((e.parentElement||{}).parentElement||{}).className||'').slice(0,30)); });
              var hid=[]; p.querySelectorAll('*').forEach(function(e){ if(!e.offsetParent) return; var cs=getComputedStyle(e);
                if(/(auto|scroll)/.test(cs.overflowX) && e.scrollWidth>e.clientWidth+4 && !e.querySelector('table,pre,code') && e.tagName!=='TABLE' && e.tagName!=='PRE')
                  hid.push(String(e.className||e.tagName).slice(0,40)+' '+e.scrollWidth+'>'+e.clientWidth); });
              /* a tap target covered by another element (16 X 2026: the source chip lay on the title) - checked in the viewport */
              var cov=[], n=0; window.scrollTo({top:p.getBoundingClientRect().top+scrollY,behavior:'instant'});
              [0, 500, 1000, 1500, 2000, 2500].forEach(function(y){ window.scrollTo({top:p.getBoundingClientRect().top+scrollY+y-100,behavior:'instant'});
                p.querySelectorAll('a,button').forEach(function(e){ if(n>600||!e.offsetParent) return; var r=e.getBoundingClientRect();
                  if(r.width<8||r.height<8||r.top<90||r.bottom>innerHeight-10||r.left<0||r.right>W) return; n++;
                  [0.2,0.5,0.8].forEach(function(f){ var h=document.elementFromPoint(r.left+r.width*f, r.top+Math.min(r.height/2,10));
                  /* only a cover inside the same row (li / tr / card): sticky bars that pass over content while scrolling are by design */
                  var row=e.closest('li,tr,article,.ab-head,.jtile'), sticky=false, a2=h; while(a2&&a2!==document.body){var ps=getComputedStyle(a2).position; if(ps==='sticky'||ps==='fixed'){sticky=true;break;} a2=a2.parentElement;}
                  if(h&&h!==e&&!e.contains(h)&&!h.contains(e)&&!sticky&&row&&row.contains(h)&&getComputedStyle(h).pointerEvents!=='none'&&h.closest('a,button'))
                    cov.push(String(e.className||e.tagName).slice(0,30)+' under '+String(h.className||h.tagName).slice(0,30)); }); }); });
              return {covered: Array.from(new Set(cov)).slice(0,6), sideways: document.documentElement.scrollWidth-W, offscreen: Array.from(new Set(off)).slice(0,6), hiddenScroll: Array.from(new Set(hid)).slice(0,6)}}""", t)
            rep["tabs"][t] = r
            if r.get("sideways", 0) > 1:
                bad.append("%s: page scrolls sideways by %dpx" % (t, r["sideways"]))
            if r.get("covered"):
                bad.append("%s: tap target covered by another element %s" % (t, "; ".join(r["covered"])))
            if r.get("hiddenScroll"):
                bad.append("%s: content scrolls sideways inside a box (looks cut off) %s" % (t, "; ".join(r["hiddenScroll"])))
            if r.get("offscreen"):
                bad.append("%s: off screen %s" % (t, "; ".join(r["offscreen"])))
        # 5ed (18 X 2026): the Message Center tab grew from 25 038 to 46 010 elements on a day without new posts (Section A fell
        # back to the whole index) - size is checked too: a tab over --max-tab elements, or the page over --max-dom, fails
        maxtab, maxdom = arg("--max-tab", 25000), arg("--max-dom", 120000)
        sizes = pg.evaluate("()=>{var o={};document.querySelectorAll('.tabpanel').forEach(function(p){o[p.id]=p.getElementsByTagName('*').length});o.__all=document.getElementsByTagName('*').length;return o}")
        rep["dom"] = sizes
        if sizes.get("__all", 0) > maxdom:
            bad.append("page has %d elements (limit %d)" % (sizes["__all"], maxdom))
        for k, v in sizes.items():
            if k != "__all" and v > maxtab:
                bad.append("%s has %d elements (limit %d)" % (k, v, maxtab))
        rep["errors"] = errs
        if errs:
            bad.append("JS errors: %s" % " | ".join(errs[:3]))
        b.close()
    rep["problems"] = bad
    if "--json" in sys.argv:
        json.dump(rep, open(arg("--json", "mobile.json"), "w"), indent=1)
    how = ("%dx CPU" % cpu) if engine == "chromium" else ("%s, no CPU throttling, no long-task API" % engine)
    print("mobile_check: load %ss, Overview sentences %ss, long tasks %d (%d ms) [%s], %d elements after every tab was opened" % (rep["load_s"], rep["sentences_s"], rep["long_tasks"], rep["long_tasks_ms"], how, rep.get("dom", {}).get("__all", 0)))
    for x in bad:
        print("  PROBLEM " + x)
    print("mobile_check: %s" % ("FAIL" if bad else "OK"))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
