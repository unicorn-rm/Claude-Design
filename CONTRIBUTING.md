# Contributing

Thanks for your interest in Claude Design.

## Ground rules
- **Distinctive, not generic.** Content must push the anti-AI-slop doctrine
  (`distinctive-design`): a point of view, real type/color/layout, restraint. No
  templated tells.
- **Grounded, not guessed.** Any specific (hex, font, Tailwind class, component,
  contrast ratio) must be verifiable in a real source (`design-grounding`). Label
  anything unverified. Never fabricate an API or a number.
- **Senior + teaches the eye.** Skills read like a senior designer explaining *why*,
  with before/after, not a style dump.

## Structure
- Skills: `plugins/design/skills/<name>/SKILL.md` (+ optional `references/`).
  Keep `description + when_to_use` under 1536 characters.
- Agents: `plugins/design/agents/<name>.md`. Commands: `plugins/design/commands/<name>.md`.

## Before you open a PR
Run the structural validator from the repo root:

```
python3 tools/validate_plugin.py
```

It must print `OK: plugin structure valid`. It checks the backbone contract
(producing skills reference distinctive-design + design-grounding, others reference
grounding), required references, and the eval suite.
