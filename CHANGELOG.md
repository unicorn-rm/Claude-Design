# Changelog

All notable changes to the Claude Design plugin are documented here.

## [0.2.0] — 2026-09-24
### Changed
- **Renamed the plugin `design` → `design-studio`** to resolve a namespace
  collision at the *plugin-name* level: the desktop app ships a built-in `design`
  plugin (Anthropic) that owns the `design:` namespace, which orphaned this plugin
  on install. Commands are now `/design-studio:*` and skills `design-studio:*`.
  The marketplace (`claude-design`) and repository are unchanged.
  (v0.1.1's skill renames removed name overlaps but could not free the namespace.)
### Added
- `distinctive-design`: flagged the *new* AI defaults — "cream + serif display +
  terracotta" and "near-black + a single acid-green/vermilion" — so warm-paper is
  no longer treated as automatically distinctive.
- `typography`: a variable-vs-static weight check (e.g. no `Plex Mono 450`) to stop
  citing weights a static family doesn't have.

## [0.1.1] — 2026-09-24
### Changed
- Renamed two skills to avoid a namespace collision with the built-in `design`
  department plugin (which also exposes `design:design-critique` and
  `design:design-handoff`): `design-critique` → **`visual-critique`**,
  `design-handoff` → **`dev-handoff`**. Namespace (`design:`) and command names
  are unchanged.

## [0.1.0] — 2026-09-24
### Added
- Initial full build of the `design` plugin (senior design companion).
- **Backbone (2):** `distinctive-design` (anti-AI-slop doctrine + ai-design-tells
  catalog) and `design-grounding` (real source registry + design-direction schema).
- **22 domain skills** across Foundations, Web/UI, Motion/3D, and Process, with 8
  deep references.
- **6 agents:** art-director, ui-designer, design-critic, motion-3d-designer,
  brand-designer, design-researcher.
- **8 commands:** /brief, /moodboard, /critique, /palette, /typeset, /artifact,
  /design-review, /handoff.
- 5-case eval suite; structural validator; marketplace manifest `claude-design`.
