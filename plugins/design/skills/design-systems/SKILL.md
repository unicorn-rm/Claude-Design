---
name: design-systems
description: Senior methodology for design systems and design tokens — a token architecture (color, type, space, radius, shadow, motion), themeable primitives, component consistency, naming, and dark mode — built on real tools (shadcn, Radix, Tailwind config) so a product looks like one coherent thing. Use when building or auditing a design system, defining tokens, or making a product visually consistent.
when_to_use: Building or auditing a design system; defining design tokens (color/type/space/radius/shadow/motion); theming and dark mode; component consistency and naming; scaling a look across a product.
---

# Design systems (senior methodology)

A design system makes a product feel like **one intentional thing** and lets it
scale without drifting into inconsistency. It's the durable form of a distinctive
look (`distinctive-design`) — the taste, encoded. Ground tokens/components in real
tools via `design-grounding` (Tailwind config, shadcn/Radix, real values).

## Tokens are the foundation

Express every visual decision as a **semantic token**, not a raw value scattered in
components:
- **Color:** `surface`, `ink`, `accent`, `muted`, `border` (+ scales); light + dark.
- **Type:** families, scale steps, weights, leading.
- **Space:** one scale (e.g. 4/8-based) used everywhere → consistent rhythm.
- **Radius, shadow, border:** a small set of intentional values (not `rounded-2xl`
  everywhere by reflex).
- **Motion:** the one easing + durations.
Tokens make theming, dark mode, and consistency trivial — change once, propagate.
Map them to CSS custom properties and/or Tailwind theme config.

## Two-tier tokens

Separate **primitive** tokens (raw scale: `color-orange-500`, `space-4`) from
**semantic** tokens (`--accent`, `--surface`) that reference them. Components use
semantic tokens; rebrand or theme by remapping semantics to primitives.

## Components with consistency

- Build on real primitives you can restyle (**shadcn/Radix** — `ui-components`) so
  behavior/a11y are handled and visuals are yours.
- Consistent props, states (hover/focus/active/disabled/loading), and sizes across
  components. A button and an input should feel like siblings.
- **Name** things clearly and predictably; a system nobody can navigate gets
  bypassed and drifts.

## Dark mode as a first-class theme

Design the dark palette as a real second set of tokens (`color-systems`), not an
invert; every component reads from tokens so it themes automatically.

## Don't over-build

YAGNI: start with the tokens and the few components actually used; grow the system
from real needs, not a speculative library nobody uses. A giant unused system is
waste; a small consistent one is gold.

## Reading it back

Reviewing a system: are decisions tokenized (semantic, not scattered)? primitive vs
semantic tiers? components consistent in states/naming? dark mode via tokens? is it
right-sized (used, not speculative)? Name the biggest source of inconsistency.
Handoff of tokens → `dev-handoff`; component sourcing → `ui-components`.
