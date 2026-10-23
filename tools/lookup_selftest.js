/* Runs api/lookup/index.js with the repository secrets as a signed-in owner and prints, per source, only the state and
   counts - never a key. CLAUDE.md 5fd. Used by .github/workflows/lookup-selftest.yml. */
const f = require("../api/lookup/index.js");
const who = Buffer.from(JSON.stringify({ userRoles: ["anonymous", "authenticated", "owner"] })).toString("base64");
const Q = process.argv.slice(2).length ? process.argv.slice(2) : ["copilot-cloud-microsoft.com", "144.172.64.128", "*connectwise*", "example.com"];
(async () => {
  let bad = 0;
  for (const q of Q) {
    const c = {};
    await f(c, { query: { q }, headers: { "x-ms-client-principal": who } });
    const b = c.res.body;
    if (c.res.status !== 200) { console.log(q, "HTTP", c.res.status, b.error); bad++; continue; }
    console.log("\n" + q + "  (" + b.type + ", " + b.ms + " ms)");
    for (const [k, v] of Object.entries(b.sources)) {
      const bits = [v.state];
      if (v.stats) bits.push("VT " + JSON.stringify(v.stats) + " engines " + v.engines.length + " resolutions " + v.resolutions.length);
      if (v.notFound) bits.push("not in VirusTotal");
      if (v.listed != null) bits.push("listed " + v.listed + (v.count != null ? " count " + v.count : "") + (v.items ? " items " + v.items.length : ""));
      if (v.seen != null) bits.push("seen " + v.seen + " class " + v.classification + " keyed " + v.keyed);
      if (v.certificates != null) bits.push("certificates " + v.certificates + " names " + v.namesTotal);
      if (v.note) bits.push("(" + v.note + ")");
      if (v.state === "error") bad++;
      console.log("  " + k.padEnd(11) + bits.join(" | "));
    }
  }
  process.exitCode = bad ? 1 : 0;
})();
