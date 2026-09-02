# public_skills

Reusable [Claude](https://claude.com/claude-code) skills.

Each top-level directory is a self-contained skill: a `SKILL.md` (name + description frontmatter, then instructions) plus any bundled reference assets.

## Skills

| Skill | What it does |
|---|---|
| [`deep-qc`](./deep-qc) | Run a deep, evidence-backed **quality review** of a content-heavy product across four failure classes (wrong requirements, mechanical, semantic, experience) and five lifecycle gates. Fans out parallel review lenses — conformance against source-of-truth specs, rendered UX/attention with instrumented probes, audience lens, content quality, regression against the full feedback ledger, engine, and validator integrity — then puts every candidate finding through a **filing gate** that exists because an uncalibrated sweep had a 67% correction rate. Ships a working null-claim probe and a portability guide naming exactly what it cannot do without your project's access. |
| [`brainlift`](./brainlift) | Build, review, or render a **BrainLift** — a DOK-layered document (foundational facts → compressed summaries → non-obvious insights → spiky POVs) engineered to manufacture a defensible point of view on one narrow topic. Enforces hard per-layer caps, and gates every spiky POV on six tests answered in writing: one sentence, foundational to the domain, contested by named opposition, new learning for the reader, an operating imperative, and defensible from your own receipts. Ships with an illustrated field manual and a review rubric. |

## Installing a skill

Clone anywhere, then symlink the skill you want into your Claude skills directory:

```bash
git clone https://github.com/rahulsub/public_skills.git
ln -s "$PWD/public_skills/deep-qc" ~/.claude/skills/deep-qc
```

Claude Code (and other clients that read `~/.claude/skills`) will pick it up on the next session. To update, `git pull` in the clone — the symlink follows.

## Using `deep-qc`

```
/deep-qc audit all            # full sweep across every unit
/deep-qc conform <unit>       # diff one artifact against its source-of-truth spec
/deep-qc render <unit>        # rendered-experience verification only
/deep-qc process              # design or repair the QC system itself
```

Read [`deep-qc/reference/project-config.md`](./deep-qc/reference/project-config.md)
before the first run: it separates portable method from the inputs you must
supply, and is explicit about what the skill **cannot** catch without access to
your source-of-truth specs and feedback history.

The one file to read even if you never run the skill:
[`deep-qc/reference/filing-gate.md`](./deep-qc/reference/filing-gate.md) — five
rules that stop false findings, each written against the real failure that
produced it.
