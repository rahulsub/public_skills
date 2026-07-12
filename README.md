# public_skills

Reusable [Claude](https://claude.com/claude-code) skills.

Each top-level directory is a self-contained skill: a `SKILL.md` (name + description frontmatter, then instructions) plus any bundled reference assets.

## Skills

| Skill | What it does |
|---|---|
| [`brainlift`](./brainlift) | Build, review, or render a **BrainLift** — a DOK-layered document (foundational facts → compressed summaries → non-obvious insights → spiky POVs) engineered to manufacture a defensible point of view on one narrow topic. Enforces hard per-layer caps. Ships with an illustrated field manual and a review rubric. |

## Installing a skill

Clone anywhere, then symlink the skill you want into your Claude skills directory:

```bash
git clone https://github.com/rahulsub/public_skills.git
ln -s "$PWD/public_skills/brainlift" ~/.claude/skills/brainlift
```

Claude Code (and other clients that read `~/.claude/skills`) will pick it up on the next session. To update, `git pull` in the clone — the symlink follows.
