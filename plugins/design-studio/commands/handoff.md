---
name: handoff
description: Prepare a design-to-development handoff — clean semantic design tokens, documented components and all states, responsive and accessibility specs (with real contrast ratios), and exported assets — so developers build the design accurately.
argument-hint: [design, component, or file]
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Prepare a design handoff

Target: `$ARGUMENTS`. Load `dev-handoff`; ground token/component formats via
`design-grounding`.

1. **Tokens** — emit the design as semantic tokens (color/type/space/radius/shadow/
   motion) as CSS custom properties and/or a Tailwind theme config and/or tokens
   JSON. Semantic names, light + dark. This is the source of truth (`design-systems`).
2. **Components & states** — document each component's states (default/hover/focus/
   active/disabled/loading/**empty/error**), sizes, spacing, and behavior; map to
   real component source (shadcn/Radix) where possible (`ui-components`).
3. **Responsive** — intended behavior per breakpoint (stack/reflow, fluid ranges),
   not just desktop (`responsive-design`).
4. **Accessibility** — contrast pairs with **real ratios** (AA/AAA), focus order,
   labels, reduced-motion (`accessibility`).
5. **Assets** — export SVG (optimized, `currentColor`), raster (WebP/AVIF + srcset),
   glTF (compressed) with predictable names.
6. Output a clean handoff doc/tokens a developer can build from without guessing.

Real values and real ratios only — never invent a token or a contrast number. If
shipping code directly, the handoff is the code (`/design-studio:artifact`).
