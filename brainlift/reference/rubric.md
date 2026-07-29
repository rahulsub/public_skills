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
A SPOV is a one-sentence principle that is **foundational to its domain**, that informed experts would **genuinely split over**, that lands as **new learning for most readers**, and that works as an **operating imperative on the problem at hand** — defensible because of evidence its author holds.

Six gates, all required. **Score each gate by filling its row on the card below, not by judging the prose.** A row you can only answer in generalities is a failed gate.

- [ ] **G1 — One plain sentence.** The statement stands alone; receipts and argument are expanded beneath it, never inside it.
- [ ] **G2 — Foundational to the domain.** Load-bearing: name three real decisions in the domain that resolve differently depending on whether it holds. It moves capital allocation, architecture choices, or category bets — not just the author's org, not one workflow. Fewer than three decisions → a tactic, not a principle.
- [ ] **G3 — Contested.** Name the expert, school, or vendor position that rejects it and write their strongest counter in one sentence. If the opposition can't be voiced, it's an unexamined assumption. Unanimity = DOK2 in costume.
- [ ] **G4 — New learning for most readers.** State the belief the informed reader must give up to accept it. Contested and novel are independent — a decades-old holy war is contested and stale; a fresh fact is novel and uncontested. Both required. Novelty is judged on the reader, never the author.
- [ ] **G5 — Operating imperative.** Complete *"therefore, when X, do Y and not Z"* using nothing but the SPOV. It must still bind after the specific instance is fixed. ("There are no agents, only sessions" — description. "Trust the work, not the worker" — imperative.)
- [ ] **G6 — Defensible from this document's DOK1s.** Cite which receipts go on the table under challenge, and why they beat what the other side can source publicly.
- [ ] Each opinion has a visible ladder down through DOK3/DOK2 to DOK1.
- [ ] Genuine conflicts are held as `status: disputed` pairs, not averaged away.

**Gate card (fill one per DOK4 item and include it in the report):**

```
SPOV: <the one sentence>
G1 one sentence      : ✅ / ❌
G2 foundational      : decisions that flip — 1) … 2) … 3) …
G3 contested         : who rejects it — <expert / school / position>
                       their best counter — "…"
G4 new learning      : belief the reader must give up — "…"
G5 imperative        : therefore, when <X>, do <Y> and not <Z>
G6 defensible        : DOK1 #… , #… — edge over public sourcing: …
verdict              : DOK4 / demote to DOK3 / demote to DOK1 / cut
```

- **Fail signals by gate:** *G2* — the tactic (true, actionable, small). *G3* — consensus mush ("fast is good"). *G4* — the stale holy war (argument everyone has heard) or the private revelation (news to the author, textbook to the reader). *G5* — the observation deck (re-describes the world, orders no one) or a surprising *fact* filed as the spike. *G1* — a paragraph where a sentence belongs. *G6* — floating opinion with no receipts. Plus: a single resolved "answer" where a live dispute belongs.
- **Demote, don't delete.** G2 or G4 failures usually belong a layer down: true-but-small → DOK2/DOK3; well-known → DOK2 by definition.

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
