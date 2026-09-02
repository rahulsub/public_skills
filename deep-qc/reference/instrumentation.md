# Rendered verification: how to prove what you claim

Class-4 defects are invisible to schema checks and most of them are invisible to
screenshots at rest. This file is the difference between "it feels broken" and a
finding an engineer can act on in one read.

## Prove a null claim (the highest-risk finding type)

Never write "nothing happened" from a screenshot. Use
`scripts/probe-null-claim.mjs`, or replicate it:

1. Arm `MutationObserver(document.body, {subtree, childList, attributes,
   characterData})` **before** the action.
2. Perform the action; log every mutation for ≥5s with timestamps.
3. Capture the **full viewport** at +150ms, +400ms, +1000ms — feedback often
   renders outside the component you are driving.
4. Enumerate `[aria-live]`, `[role=status]`, `[role=alert]`, `[role=tooltip]`,
   and any node whose computed opacity/transform changed.
5. Report the positive: "an element containing X appeared at (x,y), persisted
   Ns" or "0 mutations in 5s, 0 aria-live updates".

The real-world failure this prevents: three "the tap does nothing" claims where
a persistent popover was rendering in a different column from the one being
watched.

## Timing and gates

- Compute the **designed** wait before calling a gate broken (word count ÷
  reading speed, clip duration, authored dwell). Exceed it, then file.
- For audio-coupled UI, attach listeners on the media element (`play`, `pause`,
  `seeked`, `ended`, `timeupdate`) with `currentTime`, and compare against the
  content's own boundaries. A poll-driven pause lands late by
  `pollInterval × playbackRate` — that arithmetic has explained real "audio cuts
  off abruptly" reports to the millisecond.
- Distinguish **gate traps** (cannot proceed) from **gate leaks** (can proceed
  without doing the work). Both are severe; leaks are easier to miss — test by
  clicking forward with an empty answer and checking whether progress or reward
  is recorded.

## Environment vs product

Rule out before filing: permissions that hang rather than reject; APIs absent in
headless (speech, media devices); autoplay policy; a dev-only overlay; a stale
service worker; fonts/layout differing from a real browser. If you cannot rule
them out, file as "unverified — needs a real browser".

## Temporal capture: staging defects are invisible at rest

A page screenshotted after it settles looks finished — that is exactly the
problem. Staging defects (a question visible while its teach content is still
being narrated; a steps frame dumped whole instead of revealing on the
narration clock) exist only DURING the narration and vanish from every
at-rest capture. Four such defects shipped through an audit whose screenshots
were all settled pages.

Required for every teach-then-work page:
- Capture **at arrival (t=0)** and **mid-narration** (~1-2s in), not only at
  rest, and assert: work nodes (questions, clozes, composers) are absent or
  visibly dormant while the teach clip is playing.
- Mechanical form: while the page's autoplay clip is before its final mark,
  query for mounted work-node selectors — presence is a failure. Wire this
  into the walk harness, not just eyeballs.

## Content-extremes stress test

Every fitting component (word cards, chips, pills, banks, headers) was sized
against the content that existed when it was built. New content breaks the
assumption silently: the first 14-letter vocabulary word wrapped a card head
mid-word, collided the morph-wash with the line above, and split "reproduce"
before its final "e" on the review chips — three surfaces, one cause.

- Compute the corpus extremes (longest word, longest option, longest
  sentence, max option count) and render each fitting component with them at
  the widest AND narrowest supported viewports.
- Mechanical overlap check: a standalone word's DOM Range yielding >1 client
  rect means it wrapped — fail for word-display surfaces; bounding-box
  intersection between decorative rects (washes, highlights) and any other
  text line is a fail everywhere.
- Re-run whenever content arrives that extends an extreme.

## Adversarial passes (cheap, high yield)

Rapid double-taps on every control; wrong-then-right on every item; back and
forward mid-interaction; reload mid-task (is in-flight work preserved?); mode
flips mid-page; deep-linking into the middle of a flow (does arriving mark
earlier work complete?); a fresh profile with no stored state.

## Cross-surface consistency

Run the same probe on an older artifact and a newer one. Engine migrations land
unevenly, and "this behaves differently from the lesson next to it" is a finding
the owning team usually does not know about.
