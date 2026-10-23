/* MS_SOC lookup (CLAUDE.md 5fd, 23 X 2026): one domain, IP, URL or wildcard checked in every threat-intel source we hold
   a key for (ti_sources.json), one section per source. Owner only: staticwebapp.config.json allows /api/* to the role
   "owner" (an invitation in the Static Web App, Role management), and this function checks the role again.
   Keys are application settings of the Static Web App (VT_API_KEY, ABUSECH_AUTH_KEY, GREYNOISE_API_KEY) - never in the
   repo, never sent to the browser. A missing key means that section says "no key", never an error. */

const T_OUT = 20000;     // per source; the Static Web Apps API answers within 45 s

function principal(req) {
  try {
    const h = req.headers["x-ms-client-principal"];
    return h ? JSON.parse(Buffer.from(h, "base64").toString("utf8")) : null;
  } catch (e) { return null; }
}

async function call(url, opt) {
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), T_OUT);
  try {
    const r = await fetch(url, Object.assign({ signal: ctl.signal }, opt || {}));
    const txt = await r.text();
    let j = null;
    try { j = JSON.parse(txt); } catch (e) { /* not JSON */ }
    return { status: r.status, json: j };
  } catch (e) {
    return { status: 0, error: e.name === "AbortError" ? "timeout after " + T_OUT / 1000 + " s" : String(e.message || e).slice(0, 120) };
  } finally { clearTimeout(t); }
}

function day(ts) { return ts ? new Date(ts * 1000).toISOString().slice(0, 10) : null; }

function classify(q) {
  let v = q.trim().toLowerCase().replace(/\[\.\]/g, ".").replace(/^hxxp/, "http");
  if (/^https?:\/\//.test(v)) { try { v = new URL(v).hostname; } catch (e) { return null; } }
  v = v.replace(/\.$/, "");
  if (!/^[a-z0-9.*%:_-]{2,253}$/.test(v)) return null;
  if (/^\d{1,3}(\.\d{1,3}){3}$/.test(v)) return { type: "ip", v };
  if (/^[0-9a-f:]+$/.test(v) && v.includes(":")) return { type: "ip", v };
  if (/[*%]/.test(v)) {
    const word = v.replace(/[*%]/g, " ").split(/[ .]/).filter(Boolean).sort((a, b) => b.length - a.length)[0] || "";
    if (word.length < 4) return null;          // %ab% would ask crt.sh for millions of names
    return { type: "wildcard", v, word, re: new RegExp("^" + v.replace(/[.]/g, "\\.").replace(/[*%]/g, ".*") + "$") };
  }
  if (/^[a-z0-9-]+(\.[a-z0-9-]+)+$/.test(v)) return { type: "domain", v };
  return null;
}

async function virustotal(k, x) {
  if (!process.env.VT_API_KEY) return { state: "no key", note: "application setting VT_API_KEY is not set" };
  const H = { headers: { "x-apikey": process.env.VT_API_KEY } };
  const base = "https://www.virustotal.com/api/v3/" + (x.type === "ip" ? "ip_addresses/" : "domains/") + encodeURIComponent(x.v);
  const [r, rr] = await Promise.all([call(base, H), call(base + "/resolutions?limit=10", H)]);
  if (r.status === 404) return { state: "ok", notFound: true, link: k.link };
  if (r.status === 429) return { state: "limited", note: "VirusTotal quota (public key: 4 a minute, 500 a day) - try again in a minute" };
  if (r.status !== 200) return { state: "error", note: r.error || "HTTP " + r.status };
  const a = (r.json.data || {}).attributes || {};
  const s = a.last_analysis_stats || {};
  const eng = Object.entries(a.last_analysis_results || {})
    .filter(([, v]) => v.category === "malicious" || v.category === "suspicious")
    .map(([e, v]) => ({ engine: e, category: v.category, result: v.result || "" }))
    .sort((p, q) => (p.category === q.category ? p.engine.localeCompare(q.engine) : p.category === "malicious" ? -1 : 1));
  const res = rr.status === 200 ? (rr.json.data || []).map(d => ({
    value: (d.attributes || {})[x.type === "ip" ? "host_name" : "ip_address"], date: day((d.attributes || {}).date)
  })) : [];
  return {
    state: "ok", link: k.link,
    stats: { malicious: s.malicious || 0, suspicious: s.suspicious || 0, harmless: s.harmless || 0, undetected: s.undetected || 0 },
    engines: eng, reputation: a.reputation, votes: a.total_votes || null,
    categories: Object.entries(a.categories || {}).map(([src, c]) => src + ": " + c),
    created: day(a.creation_date), lastAnalysis: day(a.last_analysis_date), lastDns: day(a.last_dns_records_date),
    registrar: a.registrar || null, owner: a.as_owner || null, asn: a.asn || null, country: a.country || null,
    tags: a.tags || [], resolutions: res
  };
}

async function urlhaus(k, x) {
  if (!process.env.ABUSECH_AUTH_KEY) return { state: "no key", note: "application setting ABUSECH_AUTH_KEY is not set" };
  const wild = x.type === "wildcard";
  const r = await call("https://urlhaus-api.abuse.ch/v1/" + (wild ? "tag/" : "host/"), {
    method: "POST", headers: { "Auth-Key": process.env.ABUSECH_AUTH_KEY, "Content-Type": "application/x-www-form-urlencoded" },
    body: wild ? "tag=" + encodeURIComponent(x.word) : "host=" + encodeURIComponent(x.v)
  });
  if (r.status !== 200 || !r.json) return { state: "error", note: r.error || "HTTP " + r.status };
  const j = r.json;
  if (j.query_status !== "ok") return { state: "ok", listed: false, status: j.query_status, link: k.link };
  const urls = (j.urls || []).slice(0, 15).map(u => ({ url: u.url, status: u.url_status, threat: u.threat, tags: u.tags || [], added: (u.date_added || "").slice(0, 10) }));
  return { state: "ok", listed: true, count: Number(j.url_count || urls.length), firstSeen: (j.firstseen || "").slice(0, 10) || null,
           blacklists: j.blacklists || null, urls, link: k.link, by: wild ? "tag “" + x.word + "”" : "host" };
}

async function threatfox(k, x) {
  if (!process.env.ABUSECH_AUTH_KEY) return { state: "no key", note: "application setting ABUSECH_AUTH_KEY is not set" };
  const wild = x.type === "wildcard";
  const r = await call("https://threatfox-api.abuse.ch/api/v1/", {
    method: "POST", headers: { "Auth-Key": process.env.ABUSECH_AUTH_KEY, "Content-Type": "application/json" },
    body: JSON.stringify(wild ? { query: "taginfo", tag: x.word, limit: 50 } : { query: "search_ioc", search_term: x.v, exact_match: false })
  });
  if (r.status !== 200 || !r.json) return { state: "error", note: r.error || "HTTP " + r.status };
  const d = Array.isArray(r.json.data) ? r.json.data : [];
  return { state: "ok", listed: d.length > 0, status: r.json.query_status, link: k.link, by: wild ? "tag “" + x.word + "”" : "indicator",
           items: d.slice(0, 15).map(i => ({ ioc: i.ioc, type: i.ioc_type, threat: i.threat_type, malware: i.malware_printable,
                                              confidence: i.confidence_level, first: (i.first_seen || "").slice(0, 10), last: (i.last_seen || "").slice(0, 10), tags: i.tags || [] })) };
}

async function greynoise(k, x) {
  if (x.type !== "ip") return { state: "n/a", note: "GreyNoise knows IP addresses only" };
  const h = process.env.GREYNOISE_API_KEY ? { key: process.env.GREYNOISE_API_KEY } : {};
  const r = await call("https://api.greynoise.io/v3/community/" + encodeURIComponent(x.v), { headers: h });
  if (r.status === 404) return { state: "ok", seen: false, note: "not seen scanning the internet", link: k.link };
  if (r.status === 429) return { state: "limited", note: "GreyNoise community quota reached" };
  if (r.status !== 200 || !r.json) return { state: "error", note: r.error || "HTTP " + r.status };
  const j = r.json;
  return { state: "ok", seen: !!j.noise, riot: !!j.riot, classification: j.classification || null, name: j.name || null,
           lastSeen: j.last_seen || null, link: k.link, keyed: !!process.env.GREYNOISE_API_KEY };
}

async function crtsh(k, x) {
  if (x.type === "ip") return { state: "n/a", note: "certificates are looked up by name" };
  const q = x.type === "wildcard" ? "%" + x.word + "%" : x.v;
  const u = "https://crt.sh/?identity=" + encodeURIComponent(q) + "&output=json" + (x.type === "wildcard" ? "&exclude=expired" : "");
  let r = await call(u);
  if (r.status === 502 || r.status === 503 || r.status === 0) { await new Promise(z => setTimeout(z, 3000)); r = await call(u); }   // crt.sh under load
  if (r.status !== 200 || !Array.isArray(r.json)) return { state: "error", note: r.error || "HTTP " + r.status + " (crt.sh is often slow - try again)" };
  const rows = r.json;
  const names = new Map();
  for (const row of rows) for (const n of String(row.name_value || "").split("\n")) {
    const h = n.trim().toLowerCase().replace(/^\*\./, "");
    if (!h || (x.type === "wildcard" && !x.re.test(h) && !x.re.test("*." + h))) continue;
    const nb = (row.not_before || "").slice(0, 10);
    const o = names.get(h) || { name: h, first: nb, last: nb, certs: 0 };
    o.certs++; if (nb < o.first) o.first = nb; if (nb > o.last) o.last = nb;
    names.set(h, o);
  }
  const L = [...names.values()].sort((a, b) => b.last.localeCompare(a.last));
  const dates = rows.map(r => (r.not_before || "").slice(0, 10)).filter(Boolean).sort();
  return { state: "ok", link: k.link, certificates: rows.length, firstCert: dates[0] || null, lastCert: dates[dates.length - 1] || null,
           issuers: [...new Set(rows.map(r => (String(r.issuer_name || "").match(/O=([^,]+)/) || [])[1]).filter(Boolean))].slice(0, 5),
           names: L.slice(0, 40), namesTotal: L.length,
           note: x.type === "wildcard" ? "crt.sh answers a part-of-name search with a partial, varying slice - a lower bound, not a count" : "" };
}

module.exports = async function (context, req) {
  const p = principal(req);
  if (!p || !(p.userRoles || []).includes("owner")) {
    context.res = { status: 403, headers: { "Content-Type": "application/json" }, body: { error: "owner only - sign in and accept the invitation" } };
    return;
  }
  const x = classify(String((req.query && req.query.q) || ""));
  if (!x) {
    context.res = { status: 400, headers: { "Content-Type": "application/json" },
                    body: { error: "give a domain (example.com), an IP, a URL or a wildcard with a word of 4+ letters (*copilot*.com, %passkey%)" } };
    return;
  }
  const e = encodeURIComponent;
  const links = {
    vt: { link: "https://www.virustotal.com/gui/" + (x.type === "ip" ? "ip-address/" : "domain/") + e(x.v) },
    uh: { link: x.type === "wildcard" ? "https://urlhaus.abuse.ch/browse.php?search=" + e(x.word) : "https://urlhaus.abuse.ch/host/" + e(x.v) + "/" },
    tf: { link: "https://threatfox.abuse.ch/browse.php?search=" + (x.type === "wildcard" ? "tag%3A" + e(x.word) : "ioc%3A" + e(x.v)) },
    gn: { link: "https://viz.greynoise.io/ip/" + e(x.v) },
    ct: { link: "https://crt.sh/?identity=" + e(x.type === "wildcard" ? "%" + x.word + "%" : x.v) }
  };
  const t0 = Date.now();
  const [vt, uh, tf, gn, ct] = await Promise.all([
    x.type === "wildcard" ? Promise.resolve({ state: "n/a", note: "VirusTotal searches by pattern only with a paid Intelligence licence" }) : virustotal(links.vt, x),
    urlhaus(links.uh, x), threatfox(links.tf, x), greynoise(links.gn, x), crtsh(links.ct, x)
  ]);
  context.res = {
    status: 200,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
    body: { query: x.v, type: x.type, word: x.word || null, ms: Date.now() - t0, at: new Date().toISOString(),
            sources: { VirusTotal: vt, URLhaus: uh, ThreatFox: tf, GreyNoise: gn, "crt.sh": ct },
            notes: { "Microsoft TI": "Microsoft's own host reputation needs the tenant app (ThreatIntelligence.Read.All) - it runs in the IOC watch workflow, not here" } }
  };
};
