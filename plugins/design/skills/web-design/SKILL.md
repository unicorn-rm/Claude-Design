---
name: web-design
description: Senior methodology for crafting modern websites that read as intentional, not AI-templated — section patterns (hero, nav, feature, social proof, footer) done with craft, page structure and narrative, and awwwards-level polish. Routes to a section-patterns deep reference. Use when designing or reviewing a website/landing page, a hero or section, or making a site feel distinctive and shippable.
when_to_use: Designing or reviewing a website/landing page or a specific section (hero/nav/features/footer); giving a site craft and narrative; making a generic site distinctive; producing shippable front-end.
---

# Web design (senior methodology)

A site is a sequence of decisions a visitor feels. The generic site is the
**stock skeleton** (centered hero → three cards → testimonial → pricing → CTA) in
default type and blurple. Senior web design has a narrative and a point of view,
and it ships as real front-end. Follow `distinctive-design` (kill the tells) and
`design-grounding` (steal structure from real awwwards/Mobbin/Refero work; real
Tailwind/components — see [section-patterns](references/section-patterns.md)).

## Start from story and idea, not sections

Decide the **one idea** and the **narrative** the page tells (problem → shift →
proof → action), then design sections to serve it. Let one section dominate; cut
sections that don't earn their place. Reordering/removing the stock skeleton is
itself an anti-slop move.

## Craft the key surfaces

- **Hero:** the whole first impression. Real type at real scale, a specific
  accent, an intentional composition (often asymmetric), and *one* clear action.
  Avoid the centered-headline-subtitle-two-buttons default unless you make it
  distinctly yours. See the reference for grounded, non-generic hero patterns.
- **Navigation:** simple, legible, honest; a considered logotype beats a generic
  wordmark. Sticky only if it earns it.
- **Feature/content sections:** vary structure (editorial rows, an intentful bento,
  alternating media) instead of three equal cards. Real hierarchy per section.
- **Social proof / footer:** treat as design, not afterthought; footers are a
  chance for character.

## Make it feel made

- Warmth/texture over flat gradients (grain, a real photo, a considered
  illustration or 3D — see `illustration-and-imagery`, `web-3d`).
- Motion that means something, one easing (`motion-and-interaction`).
- Responsive as craft, not just "it doesn't break" (`responsive-design`).
- Accessible by construction (`accessibility`).

## Ship it

Produce real front-end: semantic HTML + Tailwind (or CSS), real components from
`ui-components`, tokens from `color-systems`/`typography`. Deliver as a claude.ai
artifact via `design-to-artifact` or as handoff-ready code (`design-handoff`).

## Reading it back

Reviewing a site: does it tell a story or run the stock skeleton? is the hero
specific or default? sections varied or three-cards-repeated? does it commit to one
idea? Name the tells and the grounded fixes with real references. Whole-page
composition → `layout-and-composition`; conversion depth → `landing-pages`.
