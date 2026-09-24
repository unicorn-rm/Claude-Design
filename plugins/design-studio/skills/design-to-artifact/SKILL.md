---
name: design-to-artifact
description: Senior methodology for turning a design into a real, shippable deliverable — primarily a self-contained claude.ai Artifact (HTML/CSS/JS or React), plus standalone HTML for handoff. Covers structure, embedding fonts/assets, responsiveness, theming, and honoring the anti-slop doctrine in real code. Use when producing a design as an artifact or shippable page, or turning a mockup/direction into working front-end.
when_to_use: Producing a design as a claude.ai artifact or shippable HTML/React page; turning a direction/mockup into real front-end; making a distinctive, responsive, theme-aware deliverable.
---

# Design to artifact (senior methodology)

The plugin ships design as **real front-end**, most often a self-contained
claude.ai Artifact. The output must honor `distinctive-design` in actual code (no
templated tells) and be grounded in real libraries/specs (`design-grounding`).

## Before writing the artifact

If the Artifact tooling/skills are available in the environment, load the
artifact-design guidance first (design calibration) and, when the page needs
runtime behavior (state, live data, saving), the artifact-capabilities guidance.
Use the design direction (`.design/direction.md`) as the source of truth for
palette/type/layout.

## Build it distinctive, in code

- **Real type** (self-hosted/Google via `<link>`), real scale, weight contrast —
  not one-weight Inter. **Warm neutrals + one specific accent** as CSS custom
  properties (tokens), not blurple, not pure `#fff`.
- **Composition with hierarchy and intentional asymmetry** (`layout-and-composition`),
  not centered-everything. Depth from borders/warmth, not `backdrop-filter` on
  everything.
- **Real components** (`ui-components`) restyled to the tokens; accessible markup
  (semantic elements, focus states, contrast — `accessibility`).
- **One easing**, motion that means something, `prefers-reduced-motion` respected
  (`motion-and-interaction`).
- **Responsive** as craft down to ~360px (`responsive-design`); a side gutter and
  fluid type.

## Self-contained & theme-aware

- Inline CSS/JS or a single file; embed or link real fonts; assets as needed.
- Define a complete light palette on `:root` and a dark variant; give the body an
  explicit token background so it doesn't borrow the host theme.
- Keep it under size limits; images optimized.

## Deliver

Produce the artifact, then hand back the link and a one-line note on the single
idea and the key choices. For dev handoff instead of an artifact, emit clean
tokens + components (`dev-handoff`).

## Reading it back

Before shipping: run the anti-slop check (`distinctive-design` → ai-design-tells)
against the actual rendered result, verify contrast with real numbers, and confirm
it's responsive and theme-aware. Fix tells in the code, not just in intent.
