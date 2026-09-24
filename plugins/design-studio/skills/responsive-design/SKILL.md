---
name: responsive-design
description: Senior methodology for responsive design — mobile-first, fluid type and spacing, sensible breakpoints, container queries, responsive images, and touch ergonomics — so a design is crafted at every width, not just unbroken. Use when making a design responsive, fixing mobile layout, choosing breakpoints, or setting fluid type/spacing.
when_to_use: Making a design responsive; fixing mobile/tablet layout; choosing breakpoints; fluid type/spacing (clamp); container queries; responsive images; touch ergonomics.
---

# Responsive design (senior methodology)

Responsive is craft, not "it doesn't break". A design should feel *composed* at
every width — phone, tablet, desktop, and the awkward sizes between. Ground CSS
features/support in real specs via `design-grounding` (real properties, real
behavior — don't invent).

## Mobile-first

Design the smallest screen first: it forces priority (what actually matters), then
enhance up. Retrofitting desktop down to mobile is where cramped, broken mobile
comes from.

## Fluid, not just steppy

- **Fluid type & space** with `clamp()` so sizes scale smoothly between breakpoints
  instead of jumping. Set a min, preferred (viewport-based), and max.
- **Breakpoints where the design needs them**, not at device names — add a
  breakpoint when the layout starts to hurt, not because "tablet is 768".
- **Container queries** for components that must adapt to their container, not the
  viewport — the modern tool for truly reusable responsive components.

## Layout that reflows with intent

- Multi-column → single column gracefully; decide the stacking order (source order
  matters for a11y and for the story). Don't just let flex wrap into mush — recompose.
- Keep a side gutter at every width; never let the page scroll horizontally (tables/
  code/diagrams get their own `overflow-x` container).

## Images & media

- `srcset`/`sizes` for responsive images; correct aspect-ratio boxes to prevent
  layout shift; lazy-load below the fold. Art-direct with `<picture>` when the crop
  should change by width.

## Touch ergonomics

- Targets ≥ ~44px, comfortable spacing, thumb-reachable primary actions on mobile;
  don't rely on hover (add a tap/focus path). Test the real phone width (~360–390px).

## Reading it back

Reviewing responsive: mobile-first with real priority? fluid type/space, not just
breakpoint jumps? recomposed (not squished) at each width? no horizontal scroll?
images responsive? touch-friendly? Name the width where it breaks and the fix.
Composition → `layout-and-composition`; a11y overlap → `accessibility`.
