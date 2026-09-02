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

## Assembling a shareable document

Embed the images inline with their comments rather than linking a folder — a
reviewer will not open 90 files. Downscale (≈700px wide) and expect the
base64-inflated document to be several MB; split into a main report plus an
appendix if the host refuses the size.

If you later retract findings, publish the correction **in a document the same
people read**, and re-title the original to point at it. Never leave a
superseded list circulating.
