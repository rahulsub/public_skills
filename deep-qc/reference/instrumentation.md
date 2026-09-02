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

## Adversarial passes (cheap, high yield)

Rapid double-taps on every control; wrong-then-right on every item; back and
forward mid-interaction; reload mid-task (is in-flight work preserved?); mode
flips mid-page; deep-linking into the middle of a flow (does arriving mark
earlier work complete?); a fresh profile with no stored state.

## Cross-surface consistency

Run the same probe on an older artifact and a newer one. Engine migrations land
unevenly, and "this behaves differently from the lesson next to it" is a finding
the owning team usually does not know about.
