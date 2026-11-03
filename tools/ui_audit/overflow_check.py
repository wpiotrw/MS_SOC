# MS_SOC - CLAUDE.md 5gg: horizontal overflow of every tab. python3 tools/ui_audit/overflow_check.py <chromium|webkit> <width> [url]
import asyncio, sys
from playwright.async_api import async_playwright
ENG=sys.argv[1]; W=int(sys.argv[2]); BASE=sys.argv[3] if len(sys.argv)>3 else "http://localhost:8767/"
async def main():
    async with async_playwright() as p:
        b = await getattr(p,ENG).launch(); pg = await b.new_page(viewport={"width": W, "height": 900}, color_scheme="dark")
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(BASE, wait_until="load"); await pg.wait_for_timeout(12000)
        tabs = await pg.evaluate("[...document.querySelectorAll('[id^=tabbtn-tab-]')].map(b=>b.id.replace('tabbtn-tab-',''))")
        bad=[]
        for t in tabs:
            await pg.evaluate("(t)=>document.getElementById('tabbtn-tab-'+t).click()", t); await pg.wait_for_timeout(1800)
            x = await pg.evaluate("""(t)=>{const vw=document.documentElement.clientWidth; const hs=document.documentElement.scrollWidth-vw; const o=[];
              const r=document.getElementById('tab-'+t); if(r) r.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect(); if(b.width&&b.right>vw+2&&!e.closest('.tw,.s5gf-tw,pre,table,[style*=overflow],.s5dv-hb,svg,.mcb-svcs,nav')&&getComputedStyle(e).position!=='fixed') o.push((e.className||e.tagName)+'');});
              return {hs, over:o.length, ex:[...new Set(o)].slice(0,4)};}""", t)
            if x['hs']>0 or x['over']: bad.append((t,x))
        print(ENG, W, "tabs", len(tabs), "with overflow:", bad[:10]); print("errors", errs[:3]); await b.close()
asyncio.run(main())
