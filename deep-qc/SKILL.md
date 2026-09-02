---
name: deep-qc
description: Run a deep, evidence-backed quality review of a learning product (or any content-heavy app) across four failure classes and five lifecycle gates — requirements conformance, mechanical validators, semantic judgment, rendered experience, and human review. Produces ranked findings with screenshot evidence and a shareable report. Use when asked to review lessons/courses/content for quality, audit a merge wave, check conformance to source-of-truth specs, hunt UX/attention problems, or design a QC process. Triggers on "deep QC", "full review", "quality audit", "review all lessons", "conformance diff", "attention audit".
argument-hint: "[audit|conform|render|process] [scope: lesson ids, PR, or 'all']"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Agent, WebFetch
---

# Deep QC

A review method built and corrected over ~30 review rounds on a K-8 reading
course. Its central claim: **quality failures fall into four classes, each
needing a different mechanism — so "review it harder" cannot work.** Its
second claim, learned the expensive way: **a false finding costs more than a
missed one**, so the method includes a filing gate, not just detection.

Read `reference/project-config.md` FIRST. It marks what is portable method
versus what is bound to a specific project, and lists what you need access to.

## Pick the mode

- **audit** — review existing artifacts. The default. → §Running an audit
- **conform** — diff artifacts against their source-of-truth specs. → `reference/conformance.md`
- **render** — rendered-experience verification only (UI/UX, interaction, a11y). → `reference/instrumentation.md`
- **process** — design or repair the QC system itself. → `reference/failure-classes.md`

## The model (internalize before reviewing anything)

**Four failure classes.** Name the class before choosing a tool:

| Class | Example | Only caught by |
|---|---|---|
| 1. Wrong requirements | content generated where a spec supplies it verbatim | source census + conformance diff |
| 2. Mechanical | broken refs, missing assets, key-position skew | deterministic validators |
| 3. Semantic | answer inferable without reading; spoiler in feedback | LLM-judge + adversarial lenses |
| 4. Experience | audio cut 0.3s late; the passage outweighs the task 4:1 | instrumented rendered walk |

Class 1 is invisible to every artifact test — the artifact matches everything
you know. It is the most expensive class and the one teams skip.

**Five gates, in lifecycle order.** A defect caught one gate later costs ~10×
more; at the customer gate it costs trust.

0. **Source census** (before authoring) — enumerate every requirements source; diff against a manifest. New/renamed/moved sources fail loudly.
1. **Conformance** (at authoring) — transfer from spec; commit a diff before building; every deviation ledgered with its covering ruling.
2. **Deterministic battery** (every commit) — the repo's own validators; exit 0 or no merge.
3. **Judgment battery** (every content change) — semantic judges + standing adversarial lenses.
4. **Rendered + human** (before any release) — instrumented walk, then two named humans, then the link goes out.

## Running an audit

1. **Scope and census.** List what you are reviewing and what governs it. If a
   source exists that you have not ingested, stop and ingest it — that is class 1.
2. **Pick lenses** (`reference/review-lenses.md`). Standard set: conformance,
   rendered UX/attention, child-or-user lens, content quality, regression
   against the historical ledger, engine/code, validators. One lens per agent.
3. **Fan out.** Run lenses in parallel as subagents, each with: scope, the
   standing rules it enforces, known-issue list to confirm-or-retract, evidence
   path, and the output contract (finding = {evidence file, location, severity,
   2-3 sentence reviewer-ready comment}).
4. **Apply the filing gate to every finding** (`reference/filing-gate.md`).
   This is not optional. It is where a 67%-correction-rate review became a
   trustworthy one.
5. **Assemble** (`reference/evidence.md`) — ranked report, evidence embedded at
   the moment of failure, credit where the work is good, open decisions with
   named owners.

## The filing gate (short form — full version in reference/)

Before any finding ships, answer:

1. **Was it requested?** Check the feedback ledger. If the customer asked for
   it, the finding is "confirm with X", never "defect".
2. **If you claim nothing happened — did you watch the whole page?** Feedback
   often renders on a different surface than the one you are driving.
   Document-level instrumentation and full-viewport capture, or no null claim.
3. **Did you wait out the designed timer?** Compute expected dwell from the
   content before calling a gate broken.
4. **Is it the product or your environment?** Hung permission prompts, missing
   APIs, and headless quirks masquerade as dead-ends.
5. **Do you know the canon?** A specified step is not a defect. Keep "the step
   is wrong" separate from "this instance of it is weak".

Retract loudly and fast when wrong. Report your own correction rate.

## Non-negotiables

- **Evidence or it did not happen.** Every finding carries a capture at the
  moment of failure, plus the location (file/line, page/node path).
- **Severity means consequence**, not annoyance: does it block, mislead, or
  teach something false?
- **Credit the good.** A review that only lists faults gets read as hostile and
  acted on less.
- **Separate what you decide from what a human decides.** Design intent,
  spec conflicts, and pedagogy calls get a named owner, not a verdict.
- **Never weaken a check to make a run green.** Park it as documented debt with
  a retirement condition.
