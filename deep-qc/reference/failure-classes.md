# Four failure classes, five gates

## The four classes

**Class 1 — wrong requirements.** The artifact is built correctly to the wrong
spec, or to no spec. Every artifact test passes; the customer opens it and says
"this isn't what we gave you". Caught only by comparing against the source of
truth, and only if you know the source exists.

*Signature:* internal reviews are green and the customer is unhappy about
content, not bugs.

**Class 2 — mechanical.** Deterministic, enumerable, machine-checkable:
broken references, missing assets, schema violations, statistical skew in
answer positions, text/audio mismatch.

*Signature:* a script can decide it. If one can, one must — see the ratchet.

**Class 3 — semantic.** Needs judgment: an answer inferable without reading the
text, a distractor that gives itself away, feedback that spoils a later reveal,
register that is wrong for the audience.

*Signature:* a human notices in seconds; a regex cannot. LLM judges do well here
if you give them the right unit (see the collection-scope trap below).

**Class 4 — experience.** Only visible in motion, rendered: timing, attention,
layout collisions, state loss, dead affordances, gates that trap or leak.

*Signature:* the report describes a feeling ("cuts off", "feels cluttered",
"confusing"); instrumentation converts it into a number.

**The collection-scope trap** (a real class-3 miss): a semantic checker that
collects only question nodes cannot see narrated text nodes. It reported zero
failures twice while the rule it enforced was being broken in prose on the same
pages. *Whenever a checker reports clean, verify what it collected.*

## The five gates

| Gate | When | Catches | Fails how |
|---|---|---|---|
| 0 Source census | before authoring | class 1 | new/renamed/moved source not in the manifest |
| 1 Conformance | at authoring | class 1 | element diverges from spec without a ledgered ruling |
| 2 Deterministic battery | every commit | class 2 | any validator non-zero |
| 3 Judgment battery | every content change | class 3 | any judge FAIL |
| 4 Rendered + human | before release | class 4 | walk fails, or a human walk finds anything |

Prefer **more gates** (cheap, automated, early) over **more review rounds**
(expensive, human, late). Rounds are a queue; gates are a filter.

## Operating rules

1. **Transfer, don't generate** — content comes from its spec; generate only
   what no spec supplies, and mark it as generated.
2. **Every audit interrogates its own boundary** — one pass per round asks
   "what source or class are we not checking?"
3. **The ratchet** — any defect a human catches becomes a machine check within
   the same cycle, or you write down why it cannot be.
4. **Fixed once is not fixed** — re-verify the historical ledger on a cadence;
   merges are the classic regression vector.
5. **One owner per check; one named decider per tension.**
6. **Shared surfaces need shared sign-off**; prove other teams' content is
   byte-identical when you touch shared code.
7. **Verify in the medium the user gets** — schema-green is not done.
8. **Reviewers review one pinned build**, with a change-log answering their
   previous feedback item by item.
9. **Small targeted checkers beat one omniscient one** — one lens, one crisp bar.
10. **Benchmarks anchor taste** — compare against real products in the category,
    and name the pattern you are borrowing.

## Two ambitions worth adopting

**Superhuman fault-finding.** Machines play a different game than reviewers:
enumeration beats sampling, many narrow lenses beat one generalist, total recall
of every past complaint beats memory, instrumentation localizes what humans can
only describe. Acceptance test: *any fault the customer finds must be one you
already found and consciously deferred* — otherwise it triggers a root-cause on
why your lenses missed it, plus a new check.

**Justified by construction.** Passing QC proves defect-freedom, not value.
Require every element to carry a three-line case: its **source** (which spec put
it there), its **principle** (what mechanism it serves), and its **behavior**
(what the user observably does because of it, and what you would expect if it
were removed). An element with no case is decoration — cut it. This converts
taste arguments into evidence arguments.
