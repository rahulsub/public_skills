# Review lenses

One lens per agent. Each gets: scope, the rules it enforces, a known-issue list
to confirm-or-retract, an evidence path, and the output contract. Running them
in parallel is the point — they find different classes and they disagree
usefully.

**Output contract for every lens** (keep it identical so reports compose):
`{evidence file, location (page/node/file:line), severity, 2-3 sentence
reviewer-ready comment: what the evidence shows + the judgment + suggested fix}`
plus a per-unit summary (verdict, load count, strongest and weakest beat).

## 1. Conformance (class 1)
Diff each artifact against its source-of-truth spec, element by element:
verdict CONFORMS / DIVERGES-generated / DIVERGES-superseded-by-ruling / MISSING
/ EXTRA. Commit the diff **before** any rebuild so the before-state is on
record. Rank output by "would the customer call this different from what they
gave us". See `conformance.md`.

## 2. Rendered experience / attention (class 4)
Walk every screen in the real product, in the user's default mode. Measure, do
not opine: element inventory by class (primary / support / navigation /
metadata / decor), primary's share of the viewport, squint test on a blurred
capture. See `attention-standard.md` and `instrumentation.md`.

## 3. Audience lens (class 3/4)
Walk as the actual user — for children, a specific age. Hunt: register, dead
ends, redundancy, demotivation, the wrong-answer experience, and **load**
(count every discrete answer moment; compare across units — the lightest unit is
usually also the best-taught, which makes cuts free).

## 4. Content quality (class 3)
Per item: is it answerable without the source? Does the key differ in style,
length, specificity, or register from the distractors? Does feedback teach
without revealing? Does anything reference material the user has not reached
yet? Automate what you can (`validate-semantic` pattern: an LLM judge with a
strict schema, temperature default, content-hash verdict cache).

## 5. Regression against the ledger (class 1–4)
Rebuild the master checklist from **every** feedback source ever received, then
re-verify each item against current state: HOLDS / REGRESSED / NEVER-APPLIED /
N-A. Merges are the classic regression vector. Expect 100+ items; most of the
value is in the handful that regressed silently.

## 6. Engine / code (class 2/4)
Skeptical senior-engineer read of the diff, hunting the classes that already bit
this project: polled-timing bugs, state lost on mode flips or reload, gates that
trap or can be skipped, double-fire on rapid input, shared-component changes
that reach other teams' content, stale test fixtures masking defects.

## 7. Validators and tooling integrity (meta)
Run the battery. Then audit the battery: did any check get weakened, scoped
down, or moved out of the gate? Did known-debt grow to make a run green on
**new** content? Does each checker actually measure what it claims — or only
that a seam string exists? *A green gate that passes a failing artifact is a
top-severity finding.*

## 8. Accessibility (class 4, and often a compliance obligation)
Keyboard-only traversal of every interactive element; visible focus; screen-reader
labels on icon-only controls; contrast against the real background; tap targets
against the platform floor (44px); motion and autoplay respecting reduced-motion;
captions on media; text scaling to 200% without loss. For products used by
children or in schools this is not a nice-to-have — it is frequently a legal
requirement and it is the lens most often missing entirely.

## 9. Safety and privacy (class 1/2, highest consequence)
What data leaves the device, and does it need to? PII in logs, analytics or URLs;
third-party embeds and their trackers; outbound links from a child-facing screen;
user-generated content paths (open-response answers) and where they are stored or
sent; account-less usage assumptions; content safety of anything generated at
runtime. Check against the regime that applies (children's-privacy law, school
district policy). One finding here outranks a page of UX findings.

## 10. Performance on real hardware
Cold load and time-to-interactive on the device class the audience actually uses
(school tablets and low-end Chromebooks, not your laptop); bundle and asset
weight; memory over a long session; unreferenced media shipping in the build.
Measure on throttled CPU and network, not on the dev machine.

## 11. Telemetry reality check (when data exists)
Review against what users actually do — where they drop off, which items they
retry, which screens they skip — rather than against assumptions. Cheapest way to
find the screens worth auditing, and it turns "I think this is confusing" into
"84% retry here".

## Lens hygiene

- Give each lens the **known issues** relevant to it and require an explicit
  confirm-or-retract. Confirming a known issue on screen is worth as much as a
  new find, and retracting one is worth more.
- Require a **"what is genuinely good"** section from every lens. It is not
  politeness: it tells the reader which parts of the system to copy.
- Where a lens contradicts a standing rule (e.g. "less text" vs an accessibility
  requirement), it must **surface the tension** with both sides, not pick.
