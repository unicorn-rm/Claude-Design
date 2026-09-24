---
name: ui-components
description: Senior methodology for building UIs with real component libraries — shadcn/ui, Radix, Tailwind, Aceternity, Magic UI, HyperUI, Flowbite, 21st.dev — choosing the right one, composing accessible components, and using animated collections without the AI-templated look. Routes to a component-libraries deep reference. Use when building UI from components, choosing a library, or assembling a design system from primitives.
when_to_use: Building UI from components; choosing between shadcn/Radix/Aceternity/Magic UI/HyperUI/Flowbite/Tailwind; composing accessible primitives; using animated component collections; assembling from a real library.
---

# UI components (senior methodology)

Don't hand-roll what a good library already solves accessibly — but don't ship the
library's demo either. The skill is **choosing the right real library and making
it yours** so it doesn't read as a template. Follow `distinctive-design`; ground
every component name/prop in the real library via `design-grounding` (docs/GitHub —
see [component-libraries](references/component-libraries.md)). Never invent a
component or prop.

## Choose the right library

- **shadcn/ui** — Radix + Tailwind components you copy into your repo and *own*
  and restyle. Best default when you want control and a distinctive look (you edit
  the code, not fight a theme).
- **Radix UI** — headless, accessible primitives (dialog, popover, menu). Use when
  you want full visual control with accessibility handled.
- **Tailwind CSS** — the utility layer under most of these; the styling substrate.
- **Aceternity UI / Magic UI** — animated, flashy marketing sections. Powerful for
  landings, but the highest AI-slop risk: everyone uses the same beam/spotlight/
  marquee. Use sparingly and restyle, or the site looks like every other one.
- **HyperUI / Flowbite / daisyUI** — ready Tailwind component sets for speed.
- **21st.dev / Park UI / Origin/Cult/Kokonut UI** — more registries to source from.
- **Tremor** — React dashboard/chart components (`data-visualization`).

## Make it yours (avoid the demo look)

The tell is shipping the library's default theme untouched (default radius,
default shadow, default blurple). Restyle to the brief: your tokens
(`color-systems`/`typography`), your radius/spacing, your motion. shadcn is ideal
because you own the source. A restyled shadcn button reads bespoke; an unmodified
Aceternity hero reads "template".

## Compose accessibly

Prefer primitives that handle focus, keyboard, and ARIA (Radix/shadcn) over
hand-rolled `div` buttons. Verify accessibility survives your restyling (focus
rings, contrast — `accessibility`).

## Reading it back

Reviewing component work: is the library right for the need? is it restyled to the
brand or shipped as the demo? are names/props real (not invented)? accessible after
restyle? Name where it reads as a template and the grounded fix. Tokens/system →
`design-systems`; motion → `motion-and-interaction`.
