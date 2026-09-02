#!/usr/bin/env python3
"""
build-report.py — turn findings + screenshots into a shareable illustrated report.

The report IS the deliverable. A finding nobody can see is a finding nobody
fixes, so every screenshot travels inline with its comment.

  python3 build-report.py findings.json --out report.html \
      [--upload --account you@work.com] [--share teammate@x.com] [--width 700]

findings.json:
{
  "title": "Full Course Review",
  "subtitle": "date, scope, method, honest coverage caveats",
  "verdict": "one paragraph a reader can act on",
  "sections": [
    { "heading": "Blockers",
      "intro": "optional prose",
      "findings": [
        { "id": "F-1",
          "severity": "BLOCKER|HIGH|MED|LOW|CLEAN",
          "location": "G3-U1-L2 p21",
          "image": "/abs/or/rel/shot.png",
          "comment": "What the shot shows, the judgment, and why it matters.",
          "fix": "optional suggested fix",
          "verified": true,
          "status": "confirmed|retracted|open"
        } ] },
    { "heading": "Pacing", "table": { "columns": ["Unit","Asks"], "rows": [["L4","55"]] } }
  ],
  "owners": [ {"item": "...", "owner": "..."} ],
  "credit": ["what is genuinely good, specifically"]
}
"""
import argparse, base64, html, json, os, shutil, subprocess, sys, tempfile

SEV = {"BLOCKER": "#b3261e", "HIGH": "#b3261e", "MED": "#8a6100",
       "LOW": "#555", "CLEAN": "#1b6b3a"}

def resize(src, width, tmp):
    """Downscale so base64 inflation keeps the doc under host conversion caps."""
    dst = os.path.join(tmp, str(abs(hash(src))) + os.path.splitext(src)[1])
    for cmd in (["sips", "-Z", str(width), src, "--out", dst],
                ["magick", src, "-resize", f"{width}x", dst],
                ["convert", src, "-resize", f"{width}x", dst]):
        if shutil.which(cmd[0]):
            if subprocess.run(cmd, capture_output=True).returncode == 0 and os.path.exists(dst):
                return dst
    return src  # no resizer available: embed as-is

def img_tag(path, width, tmp, base):
    p = path if os.path.isabs(path) else os.path.join(base, path)
    if not os.path.exists(p):
        return f'<p><i>[missing screenshot: {html.escape(path)}]</i></p>'
    b = base64.b64encode(open(resize(p, width, tmp), "rb").read()).decode()
    return f'<p><img src="data:image/png;base64,{b}" width="{width}"/></p>'

def render(doc, width, tmp, base):
    o = ['<html><head><meta charset="utf-8"><title>%s</title></head><body>'
         % html.escape(doc.get("title", "Review"))]
    o.append(f'<h1>{html.escape(doc.get("title","Review"))}</h1>')
    if doc.get("subtitle"):
        o.append(f'<p><i>{html.escape(doc["subtitle"])}</i></p>')
    if doc.get("verdict"):
        o.append('<h2>Verdict</h2><p>%s</p>' % html.escape(doc["verdict"]))

    counts = {}
    for s in doc.get("sections", []):
        for f in s.get("findings", []):
            counts[f.get("severity", "LOW")] = counts.get(f.get("severity", "LOW"), 0) + 1
    if counts:
        o.append("<p><b>Findings:</b> " + " &middot; ".join(
            f'{k} {v}' for k, v in sorted(counts.items(),
            key=lambda kv: list(SEV).index(kv[0]) if kv[0] in SEV else 9)) + "</p>")

    for s in doc.get("sections", []):
        o.append(f'<h2>{html.escape(s.get("heading",""))}</h2>')
        if s.get("intro"):
            o.append(f'<p>{html.escape(s["intro"])}</p>')
        t = s.get("table")
        if t:
            o.append('<table border="1" cellpadding="5" cellspacing="0"><tr>'
                     + "".join(f"<th>{html.escape(str(c))}</th>" for c in t["columns"]) + "</tr>")
            for r in t["rows"]:
                o.append("<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in r) + "</tr>")
            o.append("</table>")
        for f in s.get("findings", []):
            sev = f.get("severity", "LOW")
            colour = SEV.get(sev, "#555")
            head = f'<b style="color:{colour}">{html.escape(sev)}</b>'
            if f.get("id"): head = f'{html.escape(f["id"])} &middot; ' + head
            if f.get("location"): head += f' &middot; {html.escape(f["location"])}'
            if f.get("status") == "retracted": head += ' &middot; <b>RETRACTED</b>'
            elif f.get("verified"): head += ' &middot; re-verified'
            o.append(f'<h3>{head}</h3>')
            if f.get("image"):
                o.append(img_tag(f["image"], width, tmp, base))
            if f.get("comment"):
                o.append(f'<p>{html.escape(f["comment"])}</p>')
            if f.get("fix"):
                o.append(f'<p><b>Suggested fix:</b> {html.escape(f["fix"])}</p>')

    if doc.get("credit"):
        o.append("<h2>What is genuinely good</h2><ul>")
        o += [f"<li>{html.escape(c)}</li>" for c in doc["credit"]]
        o.append("</ul>")
    if doc.get("owners"):
        o.append('<h2>Open decisions — needs a human</h2>'
                 '<table border="1" cellpadding="5" cellspacing="0"><tr><th>Item</th><th>Owner</th></tr>')
        for r in doc["owners"]:
            o.append(f'<tr><td>{html.escape(r["item"])}</td><td>{html.escape(r.get("owner","unassigned"))}</td></tr>')
        o.append("</table>")
    o.append("</body></html>")
    return "\n".join(o)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("findings"); ap.add_argument("--out", default="report.html")
    ap.add_argument("--width", type=int, default=700)
    ap.add_argument("--upload", action="store_true")
    ap.add_argument("--account"); ap.add_argument("--share", action="append", default=[])
    ap.add_argument("--name")
    a = ap.parse_args()

    doc = json.load(open(a.findings))
    base = os.path.dirname(os.path.abspath(a.findings))
    with tempfile.TemporaryDirectory() as tmp:
        open(a.out, "w").write(render(doc, a.width, tmp, base))
    mb = os.path.getsize(a.out) / 1e6
    print(f"wrote {a.out} ({mb:.1f} MB)")
    if mb > 9:
        print("WARNING: >9MB may be refused on conversion — lower --width or split into an appendix.")

    name = a.name or doc.get("title", "Review")
    if not a.upload:
        print(f'\nupload:\n  gog --account <you@work.com> drive upload "{a.out}" '
              f'--convert --convert-to doc --name "{name}"')
        return
    if not a.account:
        sys.exit("--upload needs --account")
    r = subprocess.run(["gog", "--account", a.account, "drive", "upload", a.out,
                        "--convert", "--convert-to", "doc", "--name", name],
                       capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    doc_id = next((l.split()[-1] for l in r.stdout.splitlines() if l.startswith("id")), None)
    if doc_id:
        for who in a.share:
            s = subprocess.run(["gog", "--account", a.account, "drive", "share", doc_id,
                                "--role", "writer", "--email", who], capture_output=True, text=True)
            print(f"shared with {who}: {'ok' if s.returncode == 0 else s.stderr.strip()}")
        print("\nShare explicitly — a doc owned by a work account is invisible to a personal one.")

if __name__ == "__main__":
    main()
