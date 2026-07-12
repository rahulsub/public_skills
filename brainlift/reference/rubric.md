# BrainLift review rubric

Score each layer, then the document as a whole. Use this in Mode B (review).

## Per-layer scoring

### DOK1 — Foundational Facts
- [ ] Every item is a single atomic statement (not a paragraph, not a bundle).
- [ ] Every item is falsifiable — you could imagine an observation that proves it wrong.
- [ ] Every item carries a source, or is explicitly flagged `(unsourced — verify)`.
- [ ] No synthesis, framing, or opinion has leaked down to this layer.
- **Fail signals:** vibes ("X can feel slow"), bundled claims, unsourced assertions treated as ground truth.

### DOK2 — Compressed Summaries
- [ ] Each item synthesizes multiple DOK1 facts rather than restating one.
- [ ] The field would sign off without argument (it is consensus, not opinion).
- [ ] It genuinely compresses — less text, more claim.
- **Fail signals:** a DOK1 fact copied up a layer; an opinion masquerading as "everyone knows."

### DOK3 — Non-Obvious Insights
- [ ] The insight only appears when several DOK2 summaries are compared.
- [ ] It is absent from the introductory/textbook treatment of the topic.
- [ ] It cost something to reach — a smart newcomer would not land on it in five minutes.
- **Fail signals:** an obvious corollary; a DOK2 summary with the word "interestingly" bolted on.

### DOK4 — Spiky Points of View
- [ ] At least one POV a knowledgeable peer would actively contest.
- [ ] Each opinion has a visible ladder down through DOK3/DOK2 to DOK1.
- [ ] Genuine conflicts are held as `status: disputed` pairs, not averaged away.
- **Fail signals:** consensus mush ("fast is good"); floating opinions with no support; a single resolved "answer" where a live dispute belongs.

## Whole-document checks

- **Caps.** DOK1 ≤ 15 · DOK2 ≤ 10 · DOK3 ≤ 5 · DOK4 ≤ 3 (unless the author set their own). Over cap = cut, never raise.
- **Ascent.** All four layers present and each built from the one below. A missing middle layer means the spike is floating.
- **Scope.** One narrow named topic; no creep since the last pass.
- **Curation.** Sources are chosen *and* rejected; DOK1 claims are sourced.
- **Reads as a POV, not a wiki.** If a neutral reader couldn't tell what the author *believes*, it failed its one job.

## Verdict

- **Lifts** — has a real, traceable spike within caps. Ship it.
- **Salvageable** — sound bedrock, weak or missing spike. Name the 1–3 edits that would give it one.
- **Sinks** — pancake, soapbox, or consensus mush throughout. Say which failure mode and what to rebuild.
