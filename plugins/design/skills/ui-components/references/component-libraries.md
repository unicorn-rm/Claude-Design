# Component libraries — deep reference

Verify component names/props against the real docs/GitHub before using
(`design-grounding`). Never invent an API.

## Own-the-code (best for distinctive work)
- **shadcn/ui** (ui.shadcn.com, GH: shadcn-ui/ui) — copy components into your repo,
  built on Radix + Tailwind. You edit the source → fully restylable. Default choice
  when you want control and a non-templated look. CLI adds components on demand.
- **Radix UI** (radix-ui.com) — headless primitives (Dialog, DropdownMenu,
  Popover, Tabs…): behavior + a11y, zero styling. You bring the visuals.

## Tailwind ecosystems (speed)
- **Tailwind CSS** (tailwindcss.com) — utility substrate; verify class names.
- **Tailwind UI** — official pro components (paid).
- **HyperUI** (hyperui.dev), **Flowbite** (flowbite.com), **daisyUI** — free/OSS
  Tailwind component sets. Fast, but restyle or they look stock.
- **Preline**, **Park UI**, **Origin UI**, **Cult UI**, **Kokonut UI** — more sets.

## Animated / marketing (use sparingly)
- **Aceternity UI** (ui.aceternity.com), **Magic UI** (magicui.design) — animated
  hero/section effects (beams, spotlight, marquee, gradients). High recognition =
  high AI-slop risk; restyle and use one or two, not a page of them.
- **21st.dev** — community registry of shadcn-style animated components.
- **Motion** (motion.dev / framer-motion), **Headless UI** — animation + headless.

## Dashboards / data
- **Tremor** (tremor.so) — React charts/KPI components (see `data-visualization`).

## Icons (pair with components)
Lucide (shadcn's default), Heroicons, Phosphor, Tabler, Radix Icons, Iconify
(aggregator + API), Simple Icons (brands).

## Selection heuristic
- Need control + distinctive look → **shadcn + Radix + Tailwind**, restyled.
- Need speed on an internal tool → HyperUI/Flowbite/daisyUI.
- Marketing sizzle → one or two Aceternity/Magic UI pieces, restyled.
- Always: apply your own tokens, radius, shadow, motion. Ship your design, not the demo.
