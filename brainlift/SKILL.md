---
name: brainlift
description: Build, review, or render a BrainLift — a structured DOK-layered document that manufactures a defensible point of view on one narrow topic. Use when the user wants to create/draft a BrainLift, structure knowledge into DOK1–DOK4 layers, extract or sharpen spiky points of view, critique an existing BrainLift, curate sources for one, or render a BrainLift as a visual field manual. Triggers on "brainlift", "spiky POV", "DOK layers", "depth of knowledge document".
argument-hint: "[build|review|render] [topic or path to draft]"
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Artifact
---

# BrainLift

You build documents that manufacture a **defensible point of view**, not documents that store what someone already knows. A BrainLift is a curated, layered climb from verifiable fact up to an opinion an expert would want to argue with. The lower layers exist only to earn the right to hold the top one.

**The one belief that governs everything:** generic knowledge produces generic output. A BrainLift's entire job is to encode a *specific* worldview densely enough that anything built on top of it — an essay, a product decision, an agent's behavior — inherits a real point of view instead of the averaged-out consensus.

Read `reference/manual.html` if you or the user want the full illustrated field manual (it also serves as the render template — see Mode C). Read `reference/rubric.md` for the layer-by-layer scoring rubric used in review.

## First: figure out the mode

Parse `$ARGUMENTS`. The first token may be `build`, `review`, or `render`; if it's absent, infer from the request:

- The user has a **topic** and wants structure → **Mode A: Build**.
- The user has a **draft** (text or file path) and wants a critique → **Mode B: Review**.
- The user wants a **rendered/visual** artifact of a BrainLift → **Mode C: Render**.

When ambiguous, ask one short question. Otherwise proceed.

## The four DOK strata (internalize before doing anything)

A BrainLift's spine is an ascending stack. Each layer is built by working **on** the layer beneath it. Position is meaning — bedrock at the base, the spike at the summit.

| Layer | Name | What lives here | Pass test |
|---|---|---|---|
| **DOK1** | Foundational Facts | Atomic, sourced, falsifiable statements. No synthesis, no spin. | *Can it be falsified? Does it carry a source?* |
| **DOK2** | Compressed Summaries | Consensus compressed into claims the field would sign off on. Not opinion yet. | *Would a competent peer agree without argument?* |
| **DOK3** | Non-Obvious Insights | Cross-cutting observations that only surface when DOK2 summaries are held against each other. | *Is it absent from the textbook? Did it cost something to reach?* |
| **DOK4** | Spiky Points of View | One-sentence domain **principles** experts would argue over, with the ladder beneath each visible. | *All six gates in "The SPOV bar" below — each answered on a gate card, not asserted.* |

## The SPOV bar (what earns DOK4)

**A SPOV is a one-sentence principle that is foundational to its domain, that informed experts would genuinely split over, that lands as new learning for most readers, and that operates as an imperative on the problem at hand — held by an author whose own evidence makes it defensible.**

Six gates. Missing any one disqualifies the claim from DOK4. **A gate is passed by writing its answer down, not by asserting it** — every candidate gets a filled gate card (below). A gate you can only answer in generalities is a failed gate.

1. **One plain sentence.** A fundamental learning statement, not an explanation. The evidence and the argument are layers expanded *after* it lands. If it can't be said in a sentence, it isn't understood yet — send it back down the ladder.
2. **Foundational to the domain.** Load-bearing, not a corner case: if it's true, a lot downstream changes; if it's false, other beliefs in the domain fall with it. It must move how people in the domain allocate capital, choose architectures, or place category bets — "our X never worked" is a DOK1 about your org, "X never works" is a domain claim (if you can defend it). **Test:** name three real decisions in the domain that resolve differently depending on whether it holds. Fewer than three → it's a tactic or a tip, not a principle.
3. **Contested — a bias experts will argue with.** Qualified experts with opposed priors and commercial positions would split over it, with real arguments on both sides and no strawmen. Unanimous agreement = DOK2 consensus in costume; the disagreement isn't a defect, it's the source of the value. **Test:** name the specific expert, school, or vendor position that rejects it, and write their strongest counter-argument in one sentence. If you can't argue the other side, you don't hold a point of view — you hold an unexamined assumption.
4. **New learning for most readers.** A competent practitioner's reaction must be "I hadn't framed it that way," not "sure, everyone knows that." Contested and novel are independent: a decades-old holy war (tabs vs. spaces, monolith vs. microservices as usually stated) is contested and utterly stale, while a fresh surprising fact is novel and surprises nobody into disagreeing. A SPOV needs both. **Test:** state the belief the reader has to *give up* to accept this one. If nothing is given up, nothing was learned.
5. **An operating imperative for the problem at hand.** It doesn't just describe the domain — it issues orders inside it, and keeps issuing them after any specific instance is fixed. It carries causal content: explains why, predicts cases not yet seen, still binds a year out in a situation the author hasn't encountered. A description expires when the situation changes; an imperative keeps telling you what to do. **Test:** complete the sentence *"therefore, when X, do Y and not Z"* using nothing but the SPOV. ("There are no agents, only sessions" — description, rejected. "Trust the work, not the worker" — imperative, accepted.)
6. **Defensible from evidence you hold.** The author's DOK1 receipts give them an edge in the argument over anything the other side can source publicly. This is what makes the SPOV worth *owning* rather than merely interesting. **Test:** cite the specific DOK1 items you'd put on the table when challenged, and say why they beat what the other side can Google.

### The gate card — required for every DOK4 candidate

Fill one of these for each candidate and show it in your working output (build) or your report (review). The published BrainLift keeps only the sentence and its ladder; the card is the proof of work behind it.

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

Failing gate 2 or 4 usually means demote, not delete: a true-but-small claim belongs in DOK2/DOK3, and a well-known claim is DOK2 by definition.

**Operational corollary: spikiness cannot be graded off the prose — only by staging the argument.** For gates 3 and 4, simulate (or convene) a panel of experts with genuinely opposed priors and see what happens. If nobody argues, gate 3 fails — there's no SPOV, just a statement nobody cared about. If they argue but *yawn* while doing it, gate 4 fails — you've found a familiar holy war, not new learning.

## Hard caps (non-negotiable)

Each layer has a **hard** output cap. The compression *is* the product — a BrainLift that lets a layer sprawl "just this once" collapses back into a knowledge dump, which is the exact thing it exists to replace. Treat any soft-cap as a product-defining failure.

Default caps (override only if the user sets their own):

```
DOK1 Foundational Facts   ≤ 15
DOK2 Compressed Summaries ≤ 10
DOK3 Non-Obvious Insights ≤  5
DOK4 Spiky POVs           ≤  3
```

When a layer is over cap, do not raise the cap — cut. Merge near-duplicates, drop the weakest, promote anything that actually belongs a layer up. Report what you cut.

---

## Mode A — Build a BrainLift

Follow the sequence in order. Skipping a rung is the most common way a BrainLift comes out hollow.

1. **Pin the scope.** One topic, sharply bounded ("shell startup performance," not "developer tooling"). Write it as a single sentence. A BrainLift about everything is a failed BrainLift. Confirm the scope with the user before going further if it's broad.
2. **Curate sources — including rejections.** Name the experts/sources you deliberately follow *and* the ones you deliberately don't. Use WebSearch/WebFetch if live sourcing helps. Curation with no rejections is a bookmark folder, not curation.
3. **Lay the bedrock (DOK1).** Extract atomic, sourced, falsifiable facts. Resist editorializing — you are pouring foundation, not framing. Each fact gets a source or a "(unsourced — verify)" flag.
4. **Compress upward (DOK2 → DOK3).** Summarize the facts into consensus claims (DOK2). Then hold those summaries against each other until non-obvious insights surface (DOK3). That friction is where DOK3 is born — if an "insight" is just a DOK2 restated, it isn't one.
5. **Commit the spike (DOK4).** Induce, don't select: a SPOV is a generalization *from* the layers below, not the best fact promoted. Generate more candidates than you need, then **fill a gate card for each one** (see "The SPOV bar") — one sentence, foundational, contested, new learning, operating imperative, defensible from your DOK1s. Only cards with all six rows concretely answered survive. If it wouldn't make an expert argue, it's a DOK2 in costume; if experts argue but nobody learns anything, it's a stale holy war; if it merely describes what happened, it's a DOK1 in costume; if it changes no decision, it's a tactic. Sharpen or demote — don't rationalize a half-answered card.
6. **Hold disputes, don't resolve them.** Where two DOK4 views genuinely conflict, keep *both*, marked `status: disputed`. Flattening a real dispute into one bland answer destroys the tension that makes the document worth reading.
7. **Enforce the caps.** Trim every layer to its hard limit (see above). Report the counts, e.g. `DOK1 12/15 · DOK2 8/10 · DOK3 4/5 · DOK4 2/3`.

Output the BrainLift as clean Markdown by default: a scope line, a sources block (followed / rejected), then the four DOK sections top-down (DOK4 first so the payload leads), each item with its supporting layer referenced. Show the cap counts. Mark disputed pairs explicitly.

## Mode B — Review a BrainLift

Read the draft (from the argument path or pasted text). Grade it against `reference/rubric.md` and report:

1. **Layer census + caps.** Count items per layer; flag any layer over its hard cap.
2. **Layer placement.** For each item, is it on the correct stratum? The most common defect is right content on the wrong layer — opinion filed as fact, or an obvious restatement filed as insight.
3. **The spike test.** Fill a gate card for every DOK4 in the draft and put the cards in the report — do not summarize the gates as pass/fail prose. Answer each row on the author's behalf from the document's own material: three decisions that flip, the named expert who'd reject it and their counter, the belief the reader gives up, the "therefore, when X, do Y not Z", the receipts. **Any row you have to invent or fudge is a failed gate, and the card says so.** The two subtlest misses: a striking *fact* wearing a principle's clothes (fails gate 5), and a claim the author finds spiky only because it's news to them (fails gate 4 — everyone else already knows it).
4. **Traceability.** Does every DOK4 opinion trace down through DOK3/DOK2 to a DOK1 fact? Flag floating opinions.
5. **Failure modes.** Name any that apply (see below).
6. **Verdict + fixes.** One-line verdict (*lifts* / *sinks* / *salvageable*) and the specific, ranked edits that would fix it.

### Failure modes to name on sight

- **The pancake** — all DOK1/DOK2, no ascent. Informative and completely inert.
- **The soapbox** — straight to DOK4 with no ladder beneath. Opinions no reader can trace to a fact.
- **Layer inversion** — opinion filed as fact, or restatement filed as insight. Right content, wrong stratum.
- **Consensus mush** — a "spiky" POV nobody would argue with. A DOK2 in costume. (Gate 3.)
- **The stale holy war** — genuinely contested, and every reader has heard both sides a hundred times. Argument without learning. (Gate 4.)
- **The private revelation** — spiky to the author because they just learned it; textbook to everyone else. Novelty is measured on the reader, not the writer. (Gate 4.)
- **The tactic** — true, actionable, and small: a tip that changes one workflow rather than a principle that changes how the domain is bet on. (Gate 2.)
- **The observation deck** — foundational, contested, and inert: it re-describes the world beautifully and tells no one what to do differently. (Gate 5.)
- **The fact in costume** — a surprising, receipt-backed *observation* filed as DOK4. It describes, predicts nothing, and stops guiding the moment the instance is fixed. A DOK1 wearing the spike's clothes. (Gate 5.)
- **The paragraph** — a DOK4 that needs three clauses and a subordinate explanation. If it can't be said in one plain sentence, it isn't understood yet.
- **The sprawl** — scope creep + soft caps until the compression is gone and it's a wiki again.
- **Premature resolution** — two real conflicting DOK4 views merged into one bland answer. The dispute was the value.
- **Uncurated intake** — every source treated as equal, none rejected.

## Mode C — Render a BrainLift as a visual field manual

When the user wants a shareable/visual artifact:

1. Read `reference/manual.html` — it is a complete, self-contained (CSP-safe, both-theme) template with the stratigraphic DOK identity: a temperature ramp from cold indigo (DOK1, bedrock) up to hot marigold (DOK4, summit), serif + mono typesetting, worked good/bad examples, and a checklist.
2. To render *the methodology itself*, publish `reference/manual.html` as-is via the **Artifact** tool.
3. To render a *specific* BrainLift's content, load the `artifact-design` skill first (per the Artifact tool's requirement), then adapt the manual's structure and token system to the user's content — keep the DOK strata visualization and the hard-cap discipline; swap in their scope, sources, and DOK items. Do not invent a new visual language; this identity is the point.

---

## Style rules (all modes)

- **Specific beats clever.** A vague fact is not a DOK1; a hedged opinion is not a DOK4.
- **The statement is the SPOV; the defense is a layer.** State the one-liner first, always. Expand receipts and argument beneath it, never inside it.
- **No SPOV without a filled gate card.** Six concrete answers or it isn't DOK4. Asserting "experts would disagree" is not evidence that they would — name one and write their counter.
- **Novelty is measured on the reader.** "I found this surprising" is not a gate-4 pass.
- **Never soften a cap to fit more in.** Cut instead, and say what you cut.
- **Preserve disputes.** `status: disputed` is a feature, not an unfinished state.
- **Curation implies rejection.** If you didn't reject anything, you didn't curate.
- **The payload is DOK4.** Everything below it is scaffolding that exists to make the spike defensible.
