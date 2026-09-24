# design — plugin

Senior design companion for Claude Code. Distinctive by default (anti-AI-slop) and
grounded in real curated references. Ships real front-end and claude.ai artifacts.

- **Skills:** 24 (2 backbone + 22 domain) with 8 deep references.
- **Agents:** `art-director`, `ui-designer`, `design-critic`, `motion-3d-designer`,
  `brand-designer`, `design-researcher`.
- **Commands:** `/brief`, `/moodboard`, `/critique`, `/palette`, `/typeset`,
  `/artifact`, `/design-review`, `/handoff`.
- **Evals:** 5 behavior tests (rejects AI-slop, grounds color/type, real-reference
  moodboard, WCAG contrast, distinctive shippable artifact).

## Backbone contract
Every skill that produces or critiques design references `distinctive-design`
(anti-slop) AND `design-grounding` (real sources); knowledge/process skills
reference `design-grounding`. The structural validator (`tools/validate_plugin.py`
at the repo root) enforces this.

See the repository [README](../../README.md) for install and the full inventory.
