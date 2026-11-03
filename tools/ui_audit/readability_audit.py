# MS_SOC - CLAUDE.md 5gg (3 XI 2026): per tab, text under 13.5px and contrast under 4.5:1 / 7:1. Author: Piotr Wisniewski.
# python3 tools/ui_audit/readability_audit.py <site url>
"""readability audit: per tab, visible text elements with font-size < 13.5px or contrast < 4.5 (WCAG AA) / < 7 (AAA)"""
import asyncio, json, sys
from playwright.async_api import async_playwright
BASE = sys.argv[1] if len(sys.argv) > 1 else "https://orange-ground-019f30603.7.azurestaticapps.net/"
JS = r"""(tab)=>{
 function rgb(s){const m=/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/.exec(s||'');return m?[+m[1],+m[2],+m[3],m[4]===undefined?1:+m[4]]:null;}
 function lum(c){const a=c.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2];}
 function bg(e){let cs=[];while(e){const c=rgb(getComputedStyle(e).backgroundColor);if(c&&c[3]>0){cs.push(c);if(c[3]>=.99)break;}e=e.parentElement;}
   let r=[18,20,26];for(let i=cs.length-1;i>=0;i--){const c=cs[i];r=[0,1,2].map(k=>c[k]*c[3]+r[k]*(1-c[3]));}return r;}
 const root=document.getElementById('tab-'+tab); if(!root) return null;
 const out={n:0,small:0,low:0,lowAAA:0,cls:{}};
 const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let t;
 while((t=w.nextNode())){const s=t.textContent.trim(); if(s.length<3) continue; const e=t.parentElement; if(!e) continue;
   const r=e.getBoundingClientRect(); if(!r.width||!r.height) continue; const cs=getComputedStyle(e); if(cs.visibility==='hidden'||+cs.opacity===0) continue;
   const fs=parseFloat(cs.fontSize), fg=rgb(cs.color); if(!fg) continue; const b=bg(e); const f=[0,1,2].map(k=>fg[k]*fg[3]+b[k]*(1-fg[3]));
   const L1=lum(f),L2=lum(b),cr=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
   out.n++; const small=fs<13.5, low=cr<4.5, lowA=cr<7;
   if(small) out.small++; if(low) out.low++; if(lowA) out.lowAAA++;
   if(small||lowA){const k=(e.className&&typeof e.className==='string'?e.className.split(' ')[0]:e.tagName.toLowerCase())||e.tagName.toLowerCase();
     const o=out.cls[k]||(out.cls[k]={n:0,fs:fs,cr:Math.round(cr*10)/10,ex:s.slice(0,60)}); o.n++;}
 }
 out.top=Object.entries(out.cls).sort((a,b)=>b[1].n-a[1].n).slice(0,14).map(([k,v])=>k+' x'+v.n+' '+v.fs+'px c'+v.cr+' «'+v.ex+'»'); delete out.cls; return out;}"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1400, "height": 1000}, color_scheme="dark")
        await pg.goto(BASE, wait_until="load"); await pg.wait_for_timeout(12000)
        tabs = await pg.evaluate("[...document.querySelectorAll('[id^=tabbtn-tab-]')].map(b=>b.id.replace('tabbtn-tab-',''))")
        res = {}
        for t in tabs:
            await pg.evaluate("(t)=>document.getElementById('tabbtn-tab-'+t).click()", t); await pg.wait_for_timeout(2500)
            await pg.evaluate("(t)=>{const r=document.getElementById('tab-'+t); if(r) r.querySelectorAll('details').forEach((d,i)=>{if(i<6) d.open=true;});}", t); await pg.wait_for_timeout(600)
            r = await pg.evaluate(JS, t)
            if r: res[t] = r; print("%-12s text %4d  <13.5px %4d (%2d%%)  contrast<4.5 %4d  <7 %4d" % (t, r["n"], r["small"], 100*r["small"]//max(1,r["n"]), r["low"], r["lowAAA"]))
        json.dump(res, open("readability_audit.json", "w"), indent=1)
        await b.close()
asyncio.run(main())
