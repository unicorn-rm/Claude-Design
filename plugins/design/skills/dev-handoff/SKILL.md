---
name: dev-handoff
description: Senior methodology for design-to-development handoff — clean design tokens, documented components and states, specs and redlines, responsive and accessibility notes, and asset export — so developers build the design accurately. Use when preparing a handoff, exporting tokens/specs, documenting components, or translating a design (or Figma) into implementable specs and code.
when_to_use: Preparing a design-to-dev handoff; exporting design tokens; documenting components/states/specs; responsive + a11y notes; asset export; Figma-to-code or design-to-code specs.
---

# Design handoff (senior methodology)

Handoff is where good design gets built accurately — or lost in translation. The
goal is a developer builds the intended design without guessing. Ground token
formats/component APIs in real specs via `design-grounding`.

## Tokens as the contract

- Deliver the design as **tokens** (`design-systems`), not screenshots: color,
  type, space, radius, shadow, motion — as CSS custom properties, a Tailwind theme
  config, or a tokens JSON. Semantic names (`--accent`, not `#e2542b` scattered).
  This is the single source of truth that keeps design and code in sync.

## Document components & states

- For each component: the states (default/hover/focus/active/disabled/loading/
  error), sizes, spacing, and behavior. **Include the states that get forgotten**
  (empty/error/loading — `ux-principles`), not just the happy path.
- Map to the real component source where possible (shadcn/Radix — `ui-components`)
  so devs extend real code, not reinterpret a picture.

## Specs, redlines, responsive & a11y

- Spacing, sizes, and alignment specified from the spacing scale (not arbitrary
  px). Optical adjustments called out.
- **Responsive:** the intended behavior at each breakpoint (what stacks/reflows,
  fluid ranges), not just desktop (`responsive-design`).
- **Accessibility:** contrast pairs with **real ratios**, focus order, labels,
  reduced-motion behavior (`accessibility`) — so a11y survives implementation.

## Assets

- Export at the right formats/resolutions: SVG for icons/logos (optimized,
  `currentColor`), optimized raster (WebP/AVIF) with `srcset`, glTF (compressed) for
  3D (`3d-assets-and-shaders`). Name assets predictably.

## Design-to-code

- When you produce the code directly (this plugin ships real front-end), the
  handoff *is* the code: clean tokens, real restyled components, semantic accessible
  markup, responsive — see `design-to-artifact`. Figma → code: translate the file's
  intent into this same grounded system, don't blindly export div soup.

## Reading it back

Reviewing a handoff: are tokens the source of truth (semantic)? components + all
states documented? responsive + a11y (real ratios) specified? assets exported right?
could a dev build it without guessing? Name the biggest ambiguity. System →
`design-systems`; shipping code → `design-to-artifact`.
