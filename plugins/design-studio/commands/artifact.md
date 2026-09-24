---
name: artifact
description: Turn a design or direction into a real, shippable claude.ai Artifact (or standalone HTML) — distinctive in actual code, grounded in real libraries, responsive, theme-aware, and checked against the anti-slop tells.
argument-hint: [what to build]
allowed-tools: Read, Write, Edit, WebFetch, Grep, Glob
---

# Build a design artifact

Target: `$ARGUMENTS`. Load `design-to-artifact`; hold `distinctive-design` and
`design-grounding` throughout.

1. **Source of truth:** use `.design/direction.md` (palette/type/layout/one idea)
   if present; else derive a quick direction first (`/design-studio:brief` or `/design-studio:moodboard`).
2. If Artifact design/capabilities skills exist in the environment, load them first
   (design calibration; runtime capabilities only if the page needs state/data).
3. **Build it distinctive in real code:** real type (linked/self-hosted) at real
   scale; warm neutrals + one specific accent as CSS tokens; intentional, often
   asymmetric composition (`layout-and-composition`); real restyled components
   (`ui-components`); depth from borders/warmth, not blur-everything; one easing,
   meaningful motion; semantic, accessible markup; responsive to ~360px; light +
   dark palettes on `:root` with an explicit body background.
4. **Anti-slop pass on the rendered result:** walk the tells
   (`distinctive-design` → ai-design-tells), verify contrast with real numbers,
   confirm responsiveness. Fix issues in the code.
5. **Deliver** the artifact and hand back the link + the one idea + the key
   choices. For dev handoff instead, emit tokens + components (`/design-studio:handoff`).

Ground every font/component/class in a real source; never invent an API or a hex.
