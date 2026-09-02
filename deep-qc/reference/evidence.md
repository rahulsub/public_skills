# Evidence and reporting

## Capture discipline

- Capture **at the moment of failure**, not after. A screenshot of the resting
  state proves nothing about an interaction.
- Full viewport, fixed width (1280×800 is a good default), plus a second at the
  smallest supported width. Add a blurred copy for attention findings.
- Name files so the finding is readable from the filename:
  `p21-step3-DEADEND-correct-sentence-tap-does-nothing.png`.
- Also capture **one representative shot per major beat even where clean** — the
  report should show the whole arc, not only the wounds. It is what makes the
  document usable by someone who was not there.
- Note dev-only artifacts (debug badges, overlays) so nobody files them.

## The report

Order: **verdict → blockers → cross-cutting defects → per-unit sections →
conformance → what is genuinely good → open decisions with owners → action plan
by dependency.**

- Lead with the one-paragraph verdict. Reviewers read the first paragraph and
  the headings.
- Each finding: evidence image, location, severity, and 2–3 sentences that say
  what the shot shows, the judgment, and the suggested fix.
- **Severity means consequence.** Blocks the user / misleads the user / teaches
  something false / annoys. Not "how much it bothered me".
- **Quantify the vague.** "Feels cluttered" → primary holds 6% of the viewport
  while the passage holds 28%. "Too many questions" → 55 discrete answer moments
  versus 31 in the best-paced unit. Numbers survive arguments.
- **Credit what is good, specifically.** Name the beat other units should copy.
- **Open decisions get a table with named owners**, not verdicts — design
  intent, spec conflicts, and domain calls are not yours to close.
- **State your own uncertainty**: mark findings that were re-verified
  adversarially, and publish your correction rate when any were disputed.

## Timeline framing

Plan by **dependency order**, not calendar: what can start now with no
blockers, what depends on it, and what is genuinely human-gated (customer
replies, sign-offs, hands-on sessions). Calendar time belongs only in that last
group.

## The findings file (machine-readable)

Every lens emits findings into one `findings.json` so the report builds itself,
findings dedupe across lenses, and status carries between rounds:

```json
{ "title": "...", "subtitle": "date, scope, method, coverage caveats",
  "verdict": "one paragraph",
  "sections": [ { "heading": "Blockers", "findings": [
    { "id": "F-1", "severity": "BLOCKER|HIGH|MED|LOW|CLEAN",
      "location": "unit / page / file:line", "image": "shot.png",
      "comment": "what the shot shows + judgment + why it matters",
      "fix": "suggested fix", "verified": true,
      "status": "confirmed|retracted|open|closed-verified" } ] },
    { "heading": "Pacing", "table": {"columns": [], "rows": [[]]} } ],
  "credit": ["what is genuinely good"],
  "owners": [ {"item": "decision", "owner": "name"} ] }
```

## Assembling a shareable document

**Use `scripts/build-report.py`** — it renders `findings.json` into HTML with
every screenshot embedded beside its comment, resizes to keep the file under
host conversion caps, and optionally uploads and shares:

```bash
python3 scripts/build-report.py findings.json --out report.html \
    --upload --account you@work.com --share teammate@x.com
```

Embed images inline with their comments rather than linking a folder — a
reviewer will not open 90 files. ≈700px wide and ~45 images lands near 5MB,
which converts fine; split into report + appendix if the host refuses it.

If you later retract findings, publish the correction **in a document the same
people read**, and re-title the original to point at it. Never leave a
superseded list circulating.
