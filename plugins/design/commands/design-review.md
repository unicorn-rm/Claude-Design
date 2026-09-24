---
name: design-review
description: Full design review of a page or screen — anti-slop craft, visual fundamentals, accessibility (real WCAG contrast, keyboard, semantics), responsive behavior, and UX states — with specific grounded fixes prioritized by impact.
argument-hint: [file, url, or component]
allowed-tools: Read, WebFetch, Grep, Glob
---

# Full design review

Target: `$ARGUMENTS`. A superset of `/design:critique` that also covers
accessibility, responsive, and UX. Ground everything via `design-grounding`.

1. **Craft & anti-slop** (`visual-critique`, `distinctive-design`): intent/one
   idea, the tells present, hierarchy, type, color, layout, spacing.
2. **Accessibility** (`accessibility`): real WCAG **contrast ratios** (report the
   numbers), keyboard operability + visible focus, semantic structure + labels,
   alt text, reduced motion, target sizes. Mark AA/AAA pass/fail per check.
3. **Responsive** (`responsive-design`): mobile-first priority, fluid type/space,
   recomposition (not squish) at each width, no horizontal scroll, responsive images.
4. **UX** (`ux-principles`): flow clarity, empty/loading/error states, honest
   feedback, microcopy.
5. **Report**: findings grouped by area, each with severity and a specific grounded
   fix; then the top 3 highest-impact changes overall. Note what's working.

Offer to produce the fixed version (`/design:artifact`). Real numbers and real
references only.
