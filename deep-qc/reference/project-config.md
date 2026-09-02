# Portability: what travels, what you must supply

Read this first. The method is portable; several of the *inputs* are not, and
the ones that are hardest to replace are also the ones that catch the most
expensive failures. Be honest with users about that instead of letting them
believe a green run means the same thing everywhere.

## Fully portable (no setup)

The model (four classes, five gates), the filing gate, the lens taxonomy, the
attention standard, the instrumentation recipes, the reporting discipline,
`scripts/probe-null-claim.mjs`, `scripts/build-report.py` (findings.json → an
illustrated shareable report, with optional Drive upload/share), the
closing-the-loop practice, and — for learning products — the distilled reviewer
principles in `learning-product-principles.md`. Any project, any domain.

## Needs configuring per project (cheap)

| Input | What to supply |
|---|---|
| Artifact locations | where content/data lives; how to enumerate units |
| Rendered target | a URL or dev-server command; how to reach a given screen deterministically (deep links, seeded state) |
| Validator battery | the project's own checks; if none exist, gate 2 is empty — say so |
| Walk harness | scripted end-to-end traversal; without one, gate 4 is manual |
| Standing rules | the register/format/pedagogy rules your reviewers enforce |
| Severity vocabulary | what "blocks the user" means in this product |

## Requires access others may not have (the honest limits)

1. **The source-of-truth specs.** Gate 0/1 needs the customer's own design
   documents and data. Usually in a shared drive behind an account the reviewer
   may not hold, and often *not linked from the repo at all*. Without them the
   skill cannot catch class 1 — the most expensive class — and it should say so
   in the report rather than implying full coverage.
2. **A drive/API client for those sources** (here: a Google Drive CLI with a
   specific work account). Substitute your own; the census must be able to list
   folders and detect renames or re-parenting.
3. **An LLM-judge budget.** Gate 3 calls a model per item. Cache verdicts by
   content hash; expect real spend on a large corpus, and a workspace spend cap
   will silently degrade a run.
4. **The historical feedback ledger.** The regression lens re-verifies every
   complaint ever received. A new project has none — the skill can teach you to
   build one, but cannot supply it. Its value compounds; ours reached 200+ items.
5. **Institutional rulings.** Which deviations were approved, by whom, when.
   Without a deviations ledger every divergence looks like a defect — which is
   exactly how a review produces false findings.
6. **A real browser, and permissions.** Headless automation cannot answer a
   permission prompt; several capability checks (microphone, camera, autoplay)
   need a human-driven browser or they produce false dead-ends.
7. **Domain expertise for gate 4's human half.** Two named humans who know the
   subject. The skill makes their time count; it does not replace them.

## What the skill deliberately does not do

- **Decide design intent.** Conflicts between a finding and a deliberate choice
  go to a named owner.
- **Change code.** Reviews are read-only; fixing is a separate, explicit task,
  and mixing them corrupts the evidence.
- **Judge pedagogy or domain correctness on its own authority.** It checks
  conformance to the domain experts' spec and surfaces tensions.
- **Replace the customer.** Zero novel findings in a customer round is the goal;
  it is not proof that none exist.

## Calibration

On its home project the full sweep is ~4–7 parallel lenses over ~26 units,
producing 100+ findings with several hundred screenshots. First runs on a new
project will over-file: the filing gate and the known-issue confirm-or-retract
loop are what bring the correction rate down. **Publish that rate.** Ours was
67% on the first uncalibrated sweep of a mature codebase — knowing that number
is what made the second sweep trustworthy.
