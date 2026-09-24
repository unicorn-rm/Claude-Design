---
name: design-grounding
description: The grounding layer for design work. Use whenever a design decision depends on something real — a color/hex, a font family, a Tailwind class or shadcn component name, a WCAG contrast ratio, a library API, a 3D asset, or "what's the current pattern for X". Enforces basing decisions on real curated references (awwwards, Typewolf, Mobbin, Refero, shadcn, Three.js, GitHub) and real specs, and never fabricating hex values, font names, class names, or component APIs.
when_to_use: Choosing colors/fonts/components/icons/3D assets; citing a Tailwind class, shadcn/Radix component, or library API; checking WCAG contrast; researching current design patterns; before asserting any design fact.
---

# Design grounding

Distinctive design comes from **real, specific references** — not from the model's
average and not from invented facts. This layer keeps every design decision
traceable to a real source, and stops the two failure modes: hallucinated
specifics (a hex/font/class that doesn't exist) and generic vibes (see
`distinctive-design`).

## Non-fabrication rules (hard)

- Never invent: hex values presented as a brand's real color, font family names,
  Tailwind class names, shadcn/Radix/other component names or props, library APIs,
  WCAG contrast ratios, or "current trends". If unsure, look it up.
- Verify against the real source before asserting: Google Fonts for a family,
  the Tailwind/shadcn/Radix docs for a class/component, a contrast tool/math for a
  ratio, the library's GitHub for an API.
- Distinguish **pulled from a real reference** (cite it) from **my suggestion**
  (label it). "Borrow the masthead from <real site>" beats "make it modern".

## The source registry

Use the curated platforms in [sources-registry](references/sources-registry.md),
categorized (color · type · inspiration · components · 3D/graphics · icons ·
GitHub) with how to access each. The rule of thumb:

- **Public pages** → WebFetch or the browser tools to read real current work.
- **Has an API** (Google Fonts, poly.pizza, Sketchfab) → use it.
- **Real code** → GitHub is a first-class source: component libraries, awesome-
  lists, and ready solutions. Read the actual repo, don't guess the API.
- **Login-gated** (Mobbin, Dribbble at scale, Adobe Fonts, Pinterest, ArtStation)
  → treat as named references; ask the user to pull specific screens/boards when
  you need them, rather than fabricating what's behind the login.

## Grounding a decision (method)

1. **Color** → build/verify in a real tool (Coolors, Adobe Color, Radix Colors,
   uicolors, Realtime Colors); check contrast (WebAIM/Leonardo) with real numbers.
2. **Type** → real families from Google/Adobe Fonts; pairings validated against
   Typewolf/Fontpair; confirm weights/variable axes exist.
3. **Components** → real shadcn/Radix/Aceternity/Magic UI/Flowbite/HyperUI names
   and props (check docs/GitHub); real Tailwind classes.
4. **3D** → real assets (Sketchfab/poly.pizza/Poly Haven), real glTF, real
   Three.js/R3F/drei APIs.
5. **Patterns** → how do good, current, *real* sites/apps do this (awwwards,
   Mobbin, Refero, Land-book)? Steal structure from real work.

Record the chosen direction in the canonical
[design-direction schema](references/design-direction-schema.md): brief, references
(with links), palette, type, layout system, motion, and the do/don't list.

## When you can't verify

Say the specific is **unverified** and offer to confirm (fetch the source, check
the docs) rather than presenting a remembered hex/font/class as fact.

Reply in the user's language.
