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
A SPOV is a one-sentence principle about the domain that is fundamentally important, that informed experts would genuinely argue over, and that the author can defend better than anyone else because of evidence only they hold. Five gates, all required:
- [ ] **One plain sentence.** The statement stands alone; receipts and argument are expanded beneath it, never inside it.
- [ ] **Domain-level.** It changes capital allocation, architecture choices, or category bets in the domain — not just the author's org.
- [ ] **Contested.** Qualified experts with opposed priors would split over it, with real arguments on both sides. Unanimity = DOK2 in costume.
- [ ] **Invariant, not description.** Causal content; predicts unseen cases; still guides action after the specific instance is fixed. A fact expires when fixed; a principle keeps guiding. ("There are no agents, only sessions" — fact. "Trust the work, not the worker" — principle.)
- [ ] **Defensible from this document's DOK1s.** The private receipts give the author an edge over anything publicly arguable.
- [ ] Each opinion has a visible ladder down through DOK3/DOK2 to DOK1.
- [ ] Genuine conflicts are held as `status: disputed` pairs, not averaged away.
- **Fail signals:** consensus mush ("fast is good"); a surprising *fact* filed as the spike (describes, doesn't guide); a paragraph where a sentence belongs; floating opinions with no support; a single resolved "answer" where a live dispute belongs.

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
