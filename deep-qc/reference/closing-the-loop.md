# Closing the loop: dedup, triage, closure, calibration

Finding defects is the part everyone does. This file is the part that decides
whether the review changes anything.

## Deduplicate before you publish

Parallel lenses will find the same defect three times in three vocabularies —
the UX lens calls it "feedback far from the tapped element", the engine lens
calls it "the anchor prop is not threaded", the audience lens calls it
"confusing". Merge them into **one finding with the strongest evidence and the
root-cause framing**, listing the surfaces it appears on. Three reports of one
bug reads as noise and inflates your count dishonestly.

Conversely: when two lenses **contradict** each other, do not average them.
Re-test the specific claim, and if both survive, publish the disagreement —
usually it means the behaviour differs by mode, state, or viewport.

## Triage on consequence × blast radius, not severity alone

For each finding record: who it blocks, how many artifacts it touches, whose
sign-off the fix needs, and whether it is content, shared engine, or process.
A LOW finding in shared code that touches 26 units usually outranks a HIGH
finding in one screen. Order the fix list by that product, not by the severity
label.

## Closure means verified in the artifact

The single most corrosive habit is marking a finding closed because a fix was
*written*. A real round produced a "not reproducible — this string does not
occur" closure for a string that did occur, narrated, on the page.

Rules:
- A finding is closed only with **evidence from the current build** — the same
  capture or probe that found it, re-run.
- Closure links to that evidence. "Fixed in <commit>" is not closure.
- **Re-run the finder, not a different check.** A fix verified by a different
  method than the one that found it is a coincidence, not a verification.
- Track status explicitly: `open / fixed-unverified / closed-verified /
  retracted / deferred-with-owner`. Anything not `closed-verified` is open.

## The ratchet: turn findings into checks

Every human-caught defect becomes a machine check in the same cycle, or you
write down why it cannot be. Practical form:

1. Write the check so it **fires on the original defect** — reconstruct the
   pre-fix content and prove red before trusting green. (A check that has never
   been seen to fail is not a check.)
2. Narrow against current content until false positives are zero.
3. Decide severity: fail the build, or warn with a dated debt entry that names
   its retirement condition.
4. Never grandfather **new** content into a debt list — that is how a gate
   becomes decorative.

Watch for the two decoys: a check that greps for the *implementation seam*
rather than the *behaviour* (a refactor keeps the string, breaks the product),
and a check that delegates its real assertion to a harness that does not run in
the gate.

## Flaky findings

Concurrent runs on one server, races between agents, and animation timing
produce phantom failures. Before filing an intermittent: re-run it alone, and
say in the finding how many of N attempts reproduced. A finding that
reproduces 1-in-5 is still real — but the reader needs to know.

## Calibrate the review itself

Track, per round: findings filed, confirmed, retracted, and **novel findings
the customer found that you missed**. Two numbers matter:

- **Precision** (retraction rate) — the trust metric. Ours was 33% on a first
  uncalibrated sweep. Publish it.
- **Escape rate** (customer-found novel faults) — the coverage metric. The goal
  is zero; each escape triggers a root-cause on which lens should have caught it
  and a new check.

Both belong in the report. A review that reports its own error rate is trusted
further than one that implies perfection.

## Sampling when a full sweep is too expensive

Full sweeps do not scale linearly with corpus size. Prioritise: (1) anything
changed since the last sweep, (2) the newest artifact — least-walked, most
defects, (3) the oldest artifact — most drift from current standards, (4) one
artifact per generation or template family, (5) whatever the customer last
complained about. State the sample in the report so nobody reads it as full
coverage.
