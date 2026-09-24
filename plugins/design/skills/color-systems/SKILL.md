---
name: color-systems
description: Senior methodology for color in design — building intentional palettes, color theory and harmony, semantic tokens and shade scales, dark mode, and WCAG contrast — grounded in real color tools (Coolors, Adobe Color, Radix Colors, uicolors, Realtime Colors, Happy Hues). Use when choosing a palette, building color tokens, fixing a generic/AI color scheme, or checking contrast.
when_to_use: Choosing or fixing a color palette; building color tokens/shade scales; dark mode; WCAG contrast; replacing a default blurple/pure-white scheme with something intentional.
---

# Color systems (senior methodology)

Color is where "AI design" is most obvious — default blue→purple gradients and
pure `#ffffff`. A senior palette is **intentional, restrained, and grounded** in a
real tool, with real contrast numbers. Follow `distinctive-design` (avoid the
default accent) and `design-grounding` (verify hex/contrast, don't invent).

## Build an intentional palette (method)

1. **Start from the idea, not a hue wheel.** Warm/analog, cool/technical,
   high-contrast/editorial — the mood picks the direction. (See the direction
   brief in `design-grounding`.)
2. **Pick a real, specific accent** — not blurple by reflex. Ground it in a real
   tool: Coolors (coolors.co) to generate, Adobe Color for harmony, Khroma/Happy
   Hues for context. Happy Hues is especially good: it shows colors *in a real UI*
   so you assign roles, not just admire swatches.
3. **Restrain to roles, not a rainbow.** Typically: `surface`, `ink` (text),
   `accent`, plus muted/border derived from ink at low alpha. 2–3 real colors used
   with intent beats ten.
4. **Warm the neutrals.** A warm off-white (`#f7f5ef`/`#faf9f6`) and a near-black
   ink (`#1a1a1a`) read considered; pure `#fff`/`#000` read default. Borders as
   `ink` at ~8–12% alpha, not grey.
5. **Generate shade scales** with a real tool (uicolors.app for Tailwind-style
   ramps, Radix Colors for accessible, dark-mode-ready pairs) rather than
   eyeballing tints.

## Contrast & accessibility (real numbers)

- Check body text against its surface for **WCAG**: AA needs ≥ 4.5:1 (normal),
  ≥ 3:1 (large). Verify with a real tool (WebAIM contrast, Leonardo) — report the
  ratio, don't guess "looks fine". See `accessibility`.
- Don't carry meaning by color alone; accent must still pass contrast where it
  holds text.

## Dark mode

Not "invert". Design a second real palette: raised surfaces get *lighter*, not
just darker text on black; reduce accent saturation so it doesn't vibrate on dark;
re-check every contrast pair. Radix Colors gives matched light/dark scales.

## Tokens

Express the palette as semantic tokens (`--surface`, `--ink`, `--accent`,
`--border`) so it's themeable and consistent — the basis of `design-systems`.

## Reading it back

Reviewing a palette: is the accent specific or default blurple? neutrals warm or
pure? restrained to real roles? contrast checked with real numbers? dark mode
designed, not inverted? Name the biggest "AI tell" and the grounded fix (with the
tool + a real hex). Type pairing → `typography`; system tokens → `design-systems`.
