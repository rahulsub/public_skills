# The filing gate

Detection is the easy half. This gate exists because a review that filed six
"child cannot proceed" blockers had **four of them retracted** on adversarial
re-verification. The author had to defend working code; the reviewer's whole
list lost credibility, including the two findings that were real.

Run every candidate finding through all five. A finding that cannot pass is
downgraded to a question, not published as a defect.

## 1. Was it requested?

Search the feedback ledger (every channel: docs, chat exports, meeting notes,
issue trackers) for the element before calling it wrong.

*What went wrong:* we recommended splitting a morpheme display into two tiles.
The team had moved to the highlighter treatment **because the customer sent a
reference showing it**. We were telling them to undo what they were asked to do.

If a reviewer asked for it: the finding is "this may not be working as you
intended — confirm with X", or nothing at all.

## 2. If you claim nothing happened — did you watch the whole page?

A null claim ("no response", "does nothing", "no feedback") is the highest-risk
finding type and needs the strongest evidence.

*What went wrong:* three separate "the tap does nothing" claims were false. The
feedback rendered — persistently, with an avatar, anchored to the tapped element
— **in a different column** from the one the reviewer was driving and watching.
The counter they were watching correctly does not move on a wrong answer.

Required before a null claim:
- MutationObserver on `document.body` armed **before** the action, logging added
  and removed nodes plus attribute changes for ≥5s
- Full-viewport captures at +150ms, +400ms, +1000ms (not one shot at rest)
- Check `aria-live` regions, `[role=status]`, `[role=tooltip]`, portals mounted
  outside the component, and CSS-transitioned overlays
- State the *positive* observation: "an element with text X appeared at (x,y)"
  or "zero mutations in 5s"

`scripts/probe-null-claim.mjs` does this. Use it.

## 3. Did you wait out the designed timer?

*What went wrong:* we reported that a "read it myself" gate never unlocks. It
unlocks at words ÷ 150 wpm — ~152s on that page. We also claimed the audio mode
"unlocks instantly"; it was still locked at 59s. Both halves wrong, from a
sampling window shorter than the design.

Compute the expected wait from the content (word counts, clip durations,
authored dwell) and exceed it before filing.

## 4. Is it the product or your environment?

*What went wrong:* a "silent mic dead-end, lesson cannot be completed" was
`getUserMedia` **hanging** — never resolving — in an automation context where
the permission prompt is never answered. The component's error path never got
to run. A real browser prompts, or rejects into the authored error state.

Environment suspects: permissions that never resolve, missing browser APIs,
autoplay policy, headless font/layout differences, network mocking, a stale
service worker, a dev-only overlay (dev-tools badges are not shipped UI).

If you cannot rule the environment out, file it as "unverified — needs a real
browser", not as a defect.

## 5. Do you know the canon?

*What went wrong:* we filed a step as a "stem echo" defect. Reading the question
**is** the specified first step of that procedure. The real defect — that this
instance's distractors discriminate nothing — is a different finding, and only
that one should have shipped.

Read the spec for the mechanism before judging an instance of it. Then keep the
two claims apart:
- "This step should not exist" → a conformance/design claim, needs the spec
- "This instance of the step is weak" → a content-quality claim, needs an example

## Reporting discipline

- Publish your **correction rate** when findings are disputed and re-verified.
  It is the number that tells a reader how much to trust the list.
- When you retract, retract in a document the same people read, and say what
  method gap caused it. Do not bury it in a thread.
- Rank retraction risk in the report itself: findings that survived adversarial
  re-verification should be marked as such.
