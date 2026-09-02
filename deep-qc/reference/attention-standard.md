# The attention hierarchy standard

For any screen a user works on. Written for children's learning UI, but the
mechanism is general: **clutter is the emergent property of per-element
compliance.** Every element earned its place in some review; nobody owns the
screen's total attention budget. That is why the same "too cluttered" feedback
recurs after every fix round.

## The seven rules

1. **Name the ONE primary.** The single thing the user must attend to now. If
   you cannot name it, the screen is two screens.
2. **The primary wins the squint test.** Blur the capture (~12px): the first
   shape read must be the primary. Enforceable numerically — primary ≥25% of the
   viewport on presentation screens, ≥ the largest competitor on work screens.
3. **One ask, printed once.** A question or instruction appears in exactly one
   surface per viewport. A guide character may *frame* it, never restate it.
   (Lintable: ≥60% content-token overlap between adjacent text blocks.)
4. **Chrome is silent while the user works.** Anything not needed for the
   current act is absent, visually recessive, or summoned on demand — the
   video-player idiom.
5. **Feedback is anchored to the thing acted on**, adjacent to it, above the
   next action. Feedback hundreds of pixels from the tapped element reads as
   unrelated.
6. **Support is staged, not stacked.** Word banks, hints, sentence starters
   mount at the step that uses them, not on arrival.
7. **Metadata lives with adults.** Timers, version strings, counters, scripts,
   progress ledgers: reviewer/preview mode or the summary screen only.

## How to audit against it

Per screen archetype: inventory every visible element and classify it
**primary / support / navigation / metadata / decor**; measure the primary's
pixel share from bounding boxes; render a blurred copy and record what reads
first; count simultaneous text blocks and competing interactive targets.

Then disposition every element: **KEEP / DEMOTE / DEFER / RELOCATE / REMOVE**,
each with its blast radius (pure chrome / shared engine / content) and whose
sign-off it needs.

## Two traps

**The validator that gates the seam, not the size.** A checker that greps for
the source strings implementing a rule passes any refactor that preserves the
strings while breaking the behaviour — and a pixel floor delegated to a harness
that has no pixel measurement is enforced nowhere. Verify that a passing gate
corresponds to a passing screen.

**Two review modes, one product.** If a preview/reviewer mode exists, know which
one your reviewers are seeing. A large share of "your UI is cluttered" feedback
has turned out to be reviewers looking at preview chrome the end user never
sees — and if the mode toggle is reachable by the end user, that is a defect in
its own right (skippable gates, and progress written from preview navigation).
