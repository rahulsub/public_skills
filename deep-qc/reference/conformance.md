# Conformance: diffing artifacts against their source of truth

The mechanism for class 1 — the failure no artifact test can catch.

## Establish the authority chain first

Write down, in order, what decides what. A real example (three tiers):

1. **Curriculum sheet** — WHICH procedure each unit runs.
2. **Procedure design docs** — HOW that procedure's steps are taught.
3. **Per-lesson design docs + knowledge-base rows** — WHAT content the lesson
   contains: the designated vocabulary, the key idea, canonical media and its
   embedded checks, off-limits lists, transfer activities.

Tier 3 was invisible for months: internal audits verified tiers 1–2 and were
green while the customer's own per-lesson specs sat unread in a shared drive.
**Every project has a tier-3 equivalent.** Find it before reviewing anything.

Record the chain where builders will see it, with the tie-break rule
("on routing the sheet wins; on step mechanics the design doc wins").

## The diff

Per artifact × its spec, element by element:

| Verdict | Meaning |
|---|---|
| CONFORMS | transferred as specified |
| DIVERGES-generated | we invented content the spec supplies |
| DIVERGES-superseded | differs, but a dated ruling covers it — name the ruling |
| MISSING | the spec supplies it; we ship nothing |
| EXTRA | we ship it; no spec basis (may be fine — mark it) |

Commit the diff **before** any rebuild. The before-state is the evidence that
the rebuild was needed and the baseline for the next round.

## The deviations ledger

Every difference that ships gets one line: element / what the spec says / what
we ship / the covering ruling / needs-sign-off flag. The test of a good ledger:
**the customer can read it alone and see every difference with its
justification.** Nothing diverges silently — an undocumented divergence is a
build error regardless of who requested it verbally.

Also record the third category honestly: **elements with no canon at all**. If
the spec is silent (morphology, per-item feedback wording, page furniture),
say so — that is not divergence, and pretending otherwise inflates the count.

## The convention-parity gap (tier 2.5)

A new artifact built in an evolved codebase inherits the ENGINE but not the
AUTHORING WIRING that invokes it. Staging idioms (frames that reveal on the
narration clock, questions that mount after their teach completes, banks that
arm per blank) live as per-page JSON wiring that accumulated through fix
waves on OLD artifacts — no spec ever names them, so a conformance diff
against the design doc comes back clean while the new artifact ships as a
static dump. This is how a lesson with a perfect content-transfer scorecard
shipped four staging defects on day one.

Fix: maintain a living **engine-conventions checklist** (the current staging
/ interaction idioms, each with its reference implementation) as explicit
tier-2.5 canon, walked per page type on every new build — and back it with a
mechanical check: any page combining a narrated teach node with a work node
must carry staging wiring, or fail loud.

## Signals that you have a class-1 problem

- Internal reviews green, customer unhappy about *content* rather than bugs
- "Most of it isn't even an extrapolation — it's a direct transfer" in feedback
- One artifact conforms far better than its siblings (proves the platform can;
  removes every "the renderer can't do it" defence)
- A spec folder was renamed or re-parented and nobody noticed (run the census)
