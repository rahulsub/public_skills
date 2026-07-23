---
name: brainlift
description: Build, review, or render a BrainLift — a structured DOK-layered document that manufactures a defensible point of view on one narrow topic. Use when the user wants to create/draft a BrainLift, structure knowledge into DOK1–DOK4 layers, extract or sharpen spiky points of view, critique an existing BrainLift, curate sources for one, or render a BrainLift as a visual field manual. Triggers on "brainlift", "spiky POV", "DOK layers", "depth of knowledge document".
argument-hint: [build|review|render] [topic or path to draft]
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
| **DOK4** | Spiky Points of View | One-sentence domain **principles** experts would argue over, with the ladder beneath each visible. | *All five gates in "The SPOV bar" below.* |

## The SPOV bar (what earns DOK4)

**A SPOV is a one-sentence principle about a domain that is fundamentally important, that informed experts would genuinely argue over, and that its holder can defend better than anyone else because of evidence only they hold.**

Five gates. Missing any one disqualifies the claim from DOK4:

1. **One plain sentence.** A fundamental learning statement, not an explanation. The evidence and the argument are layers expanded *after* it lands. If it can't be said in a sentence, it isn't understood yet — send it back down the ladder.
2. **About the domain, not the author.** It must matter enough to change how people in the domain allocate capital, choose architectures, or place category bets. "Our X never worked" is a DOK1 about your org; "X never works" is a domain claim (if you can defend it).
3. **Contested.** Qualified experts asked to opine would argue *with each other* — real stakes, no strawmen. Unanimous agreement = DOK2 consensus in costume. The disagreement isn't a defect; it's the source of the value.
4. **An invariant, not a description.** It carries causal content: explains why, predicts cases not yet seen, and still guides action after any specific instance is fixed. A fact expires when you fix it; a principle keeps telling you what to do. Test: *would this sentence still guide a decision a year from now, in a situation the author hasn't encountered?* ("There are no agents, only sessions" — fact, rejected. "Trust the work, not the worker" — principle, accepted.)
5. **Defensible with private evidence.** The author's DOK1 receipts give them an edge in the argument over anything the other side can source publicly. This is what makes the SPOV worth *owning* rather than merely interesting.

**Operational corollary: spikiness cannot be graded off the prose — only by staging the argument.** To test gate 3, simulate (or convene) a panel of experts with genuinely opposed priors and commercial positions and see if they split. If nobody argues, there's no SPOV yet — just a statement nobody cared about.

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
5. **Commit the spike (DOK4).** Induce, don't select: a SPOV is a generalization *from* the layers below, not the best fact promoted. Run every candidate through the five gates in "The SPOV bar" — one sentence, domain-level, contested (stage the argument), invariant-not-description, defensible from your DOK1s. If it wouldn't make an expert argue, it is a DOK2 in costume; if it merely describes what happened, it is a DOK1 in costume — cut or sharpen either way.
6. **Hold disputes, don't resolve them.** Where two DOK4 views genuinely conflict, keep *both*, marked `status: disputed`. Flattening a real dispute into one bland answer destroys the tension that makes the document worth reading.
7. **Enforce the caps.** Trim every layer to its hard limit (see above). Report the counts, e.g. `DOK1 12/15 · DOK2 8/10 · DOK3 4/5 · DOK4 2/3`.

Output the BrainLift as clean Markdown by default: a scope line, a sources block (followed / rejected), then the four DOK sections top-down (DOK4 first so the payload leads), each item with its supporting layer referenced. Show the cap counts. Mark disputed pairs explicitly.

## Mode B — Review a BrainLift

Read the draft (from the argument path or pasted text). Grade it against `reference/rubric.md` and report:

1. **Layer census + caps.** Count items per layer; flag any layer over its hard cap.
2. **Layer placement.** For each item, is it on the correct stratum? The most common defect is right content on the wrong layer — opinion filed as fact, or an obvious restatement filed as insight.
3. **The spike test.** Run every DOK4 through the five gates in "The SPOV bar": one sentence? domain-level? would experts genuinely split (stage the argument if unsure)? invariant or just a description? defensible from the document's own DOK1s? A DOK4 that fails gate 4 is the subtlest and most common miss — a striking *fact* wearing a principle's clothes.
4. **Traceability.** Does every DOK4 opinion trace down through DOK3/DOK2 to a DOK1 fact? Flag floating opinions.
5. **Failure modes.** Name any that apply (see below).
6. **Verdict + fixes.** One-line verdict (*lifts* / *sinks* / *salvageable*) and the specific, ranked edits that would fix it.

### Failure modes to name on sight

- **The pancake** — all DOK1/DOK2, no ascent. Informative and completely inert.
- **The soapbox** — straight to DOK4 with no ladder beneath. Opinions no reader can trace to a fact.
- **Layer inversion** — opinion filed as fact, or restatement filed as insight. Right content, wrong stratum.
- **Consensus mush** — a "spiky" POV nobody would argue with. A DOK2 in costume.
- **The fact in costume** — a surprising, receipt-backed *observation* filed as DOK4. It describes, predicts nothing, and stops guiding the moment the instance is fixed. A DOK1 wearing the spike's clothes.
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
- **Never soften a cap to fit more in.** Cut instead, and say what you cut.
- **Preserve disputes.** `status: disputed` is a feature, not an unfinished state.
- **Curation implies rejection.** If you didn't reject anything, you didn't curate.
- **The payload is DOK4.** Everything below it is scaffolding that exists to make the spike defensible.
