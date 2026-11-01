#!/usr/bin/env python3
"""mirror_redact.py - CLAUDE.md 5gc (1 XI 2026): take Microsoft's sample credentials out of our Learn copy before it is
committed.

Why: Microsoft Purview documents every sensitive information type (SIT) on its own page (mirror/learn/purview/Purview/
sit-defn-*.md) and most credential SITs carry a "Credential example" - a fake key in the real format. GitHub push
protection cannot tell a sample from a secret: on 30 and 31 X 2026 it rejected three mirror commits over
sit-defn-azure-iot-connection-string.md line 77 ("Azure IoT Hub Connection String"), so no Learn page change reached
the repository for two days. Allowing the "secret" by hand would only move the problem to the next sample.

What it does (only on the files git reports as new or changed under mirror/, unless --all):
  1. in a "## Credential example" section, every `inline code` value and every fenced block becomes
     `<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>`;
  2. anywhere in mirror/, values in the formats GitHub's push protection scans for (Azure connection strings and
     account keys, AWS, GitHub, Slack, Google, Stripe, Twilio, SendGrid, npm, PyPI tokens, private key blocks) are
     replaced by the same marker.
The live page is the reference; the mirror is for "what changed on the page", and a sample key never changes the
meaning of a page. Prints one line per file it changed; exit 0 always (it never blocks the mirror).

  python3 tools/mirror_redact.py [repo] [--all]
"""
import os, re, subprocess, sys

MARK = "<sample credential removed by the MS_SOC mirror (GitHub push protection) - see the live Learn page>"
PATTERNS = [
    r"HostName\s*=\s*[^\s`;]{1,200}azure-devices\.net[^`\n]{0,200}?SharedAccessKey\s*=\s*[A-Za-z0-9/+]{20,}=*",
    r"Endpoint\s*=\s*sb://[^\s`;]+;\s*SharedAccessKeyName\s*=\s*[^;`\s]+;\s*SharedAccessKey\s*=\s*[A-Za-z0-9/+]{20,}=*",
    r"DefaultEndpointsProtocol\s*=\s*https?;\s*AccountName\s*=\s*[^;`\s]+;\s*AccountKey\s*=\s*[A-Za-z0-9/+]{40,}=*[^`\s]*",
    r"AccountKey\s*=\s*[A-Za-z0-9/+]{80,}={0,2}",
    r"SharedAccessSignature\s*=\s*[^`\s]{20,}",
    r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",
    r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    r"\bgithub_pat_[A-Za-z0-9_]{60,}\b",
    r"\bxox[abposr]-[A-Za-z0-9-]{10,}\b",
    r"\bAIza[0-9A-Za-z_\-]{35}\b",
    r"\b(?:sk|rk)_live_[0-9A-Za-z]{20,}\b",
    r"\bSK[0-9a-fA-F]{32}\b",
    r"\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}\b",
    r"\bnpm_[A-Za-z0-9]{36}\b",
    r"\bpypi-AgEIcHlwaS5vcmc[A-Za-z0-9_\-]{50,}",
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----",
]
RX = [re.compile(p) for p in PATTERNS]
SECTION = re.compile(r"(^#{2,4}\s*Credential examples?\s*\n)(.*?)(?=^#{1,4}\s|\Z)", re.M | re.S | re.I)


def redact(text):
    n = 0

    def sect(m):
        nonlocal n
        body = m.group(2)
        b2, k1 = re.subn(r"```[\s\S]*?```", "```\n" + MARK + "\n```", body)
        b2, k2 = re.subn(r"`[^`\n]+`", "`" + MARK + "`", b2)
        n += k1 + k2
        return m.group(1) + b2
    text = SECTION.sub(sect, text)
    for rx in RX:
        text, k = rx.subn(MARK, text)
        n += k
    return text, n


def changed_files(repo):
    out = subprocess.run(["git", "-C", repo, "status", "--porcelain", "-uall", "--", "mirror"], capture_output=True, text=True).stdout
    files = []
    for line in out.splitlines():
        p = line[3:].strip().strip('"')
        if " -> " in p:
            p = p.split(" -> ", 1)[1]
        if line[:2].strip() != "D":
            files.append(p)
    return files


def main(argv):
    repo = next((a for a in argv if not a.startswith("--")), os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if "--all" in argv:
        files = [os.path.relpath(os.path.join(d, f), repo) for d, _, fs in os.walk(os.path.join(repo, "mirror")) for f in fs]
    else:
        files = changed_files(repo)
    total = 0
    for rel in files:
        p = os.path.join(repo, rel)
        if not os.path.isfile(p) or not re.search(r"\.(md|yml|yaml|json|txt|html)$", p, re.I):
            continue
        try:
            with open(p, encoding="utf-8") as f:
                t = f.read()
        except Exception:
            continue
        t2, n = redact(t)
        if n:
            with open(p, "w", encoding="utf-8") as f:
                f.write(t2)
            total += n
            print("redacted %d sample credential(s): %s" % (n, rel))
    print("mirror_redact: %d file(s) checked, %d sample credential(s) removed" % (len(files), total))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
