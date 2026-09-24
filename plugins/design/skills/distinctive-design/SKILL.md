---
name: distinctive-design
description: The anti-AI-slop doctrine and the core of this plugin. Use whenever design is being produced, chosen, or reviewed — a website, landing page, UI, layout, hero, color, type, brand, or artifact. Checks every design decision against one question: is this intentional and distinctive, or default/templated "AI-looking" design? Names the generic tells and drives the choices that defeat them.
when_to_use: Any time you generate, choose, or review visual design — a site/UI/landing/hero/layout/palette/type/brand/artifact; before shipping a design; when a design feels generic or "AI-made".
---

# Distinctive design (anti-AI-slop doctrine)

This is the plugin's spine. Most generated design fails the same way: it is
**competent and completely forgettable** — the visual equivalent of the average
of everything. Your job is the opposite: design with a **point of view**,
grounded in real references (`design-grounding`), that looks made by a person who
decided things.

## The rule of precedence

Before shipping or approving any design, run the AI-slop check: does it read as
**intentional and distinctive**, or as **default/templated**? If it's the latter,
that's the finding — say so and fix it. This overrides "it looks fine / it's
clean." Clean-but-generic is the failure mode, not the goal. See the full catalog
in [ai-design-tells](references/ai-design-tells.md).

## The tells (what "AI design" looks like — avoid these)

- **Everything centered**, everything symmetric, everything equal weight.
- **Purple/indigo/violet gradients** and blue→purple as the default accent.
- **Glassmorphism everywhere** — `backdrop-filter: blur` on every card. (Anthropic's
  own site uses *zero* `backdrop-filter`; depth comes from warm paper, hairline
  borders, and restraint, not blur.)
- **Inter (or a generic geometric sans) for everything**, one weight, no contrast.
- **Emoji as section bullets/headings** (🚀 ✨ 💡) doing the work real type should.
- **Three equal feature cards** in a row, soft shadow, rounded-2xl, on pure white.
- **The predictable skeleton:** big centered hero → 3 features → testimonial →
  pricing → CTA, in that exact order, every time.
- **Fake depth:** soft grey drop-shadows on white, no real light logic.
- **Over-rounding** everything to `rounded-2xl`; no sharp intentional edges.
- **Meaningless motion:** everything fades-up-on-scroll with the same easing.
- **No point of view:** nothing is exaggerated, nothing is restrained, nothing
  is a choice. Safe. Forgettable.

## The moves that defeat them

1. **A point of view.** Pick a stance — editorial, brutalist, warm/analog,
   technical, playful — and commit. One idea, pushed. Contrast against the default.
2. **Real type as the design.** A considered typeface (often a display or serif
   for headlines) with real size/weight contrast carries more than any effect.
   See `typography`. Avoid one-weight Inter walls.
3. **Intentional color, not default.** A warm off-white beats `#ffffff`; a
   specific accent beats blurple. Ground it in real palettes (`color-systems`).
   Restrain the palette — 2–3 real colors, used with intent.
4. **Editorial / asymmetric layout.** Break the center. Use a real grid, uneven
   columns, overlap, generous *and* tight space deliberately. Whitespace is a
   material, not a leftover. See `layout-and-composition`.
5. **Optical adjustments.** Optical alignment and trim (not mathematical),
   balanced letter-spacing on display type, hanging punctuation — the small
   corrections a person makes and a template doesn't.
6. **Texture & warmth.** Grain, paper, a subtle noise, a real photograph, a hand
   element — anything that isn't a flat gradient. Depth from light and material,
   not blur.
7. **One considered easing.** Pick a single, characterful easing curve and reuse
   it; motion should mean something (reveal structure, guide the eye), not
   decorate. See `motion-and-interaction`.
8. **Restraint.** Remove effects until it hurts, then stop. The generic look is
   usually *too much* (blur + gradient + shadow + glow), not too little.

## Grounding, not vibes

Distinctiveness comes from **stealing from real, specific work**, not from the
model's average. Always pair this doctrine with `design-grounding`: pull real
references (awwwards, Typewolf, Mobbin, Refero, Dribbble, GitHub) and real specs.
"Make it pop" is not a decision; "borrow the asymmetric masthead from <this real
site> and set it in <this real typeface>" is.

## Reviewing a design

When critiquing, name the specific tells present, then give the specific fix and,
where useful, a real reference to steal from. Vague ("make it more modern") is
banned. See `design-critique`.

## Teaching mode

When the user is learning, explain *why* a choice reads as generic vs intentional
with a concrete before/after, so they build the eye — not just the output.

Reply in the user's language.
