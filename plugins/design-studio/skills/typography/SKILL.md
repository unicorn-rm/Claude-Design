---
name: typography
description: Senior methodology for typography — type pairing, modular scale and vertical rhythm, weight/size contrast, variable fonts and optical sizing, and webfont loading/performance — grounded in real families (Google Fonts, Adobe Fonts) and real pairings (Typewolf, Fontpair). Routes to a type-pairing deep reference. Use when choosing or pairing fonts, setting a type scale, fixing generic one-weight-Inter type, or loading webfonts.
when_to_use: Choosing/pairing typefaces; setting a modular type scale and rhythm; weight/size contrast; variable fonts; webfont loading/performance; replacing generic single-weight sans type.
---

# Typography (senior methodology)

Type does more of the design work than any effect. The generic look is **one
geometric sans (Inter/Roboto), one weight, weak hierarchy**. Senior type has a
point of view and real contrast. Follow `distinctive-design` and ground families/
pairings in real sources via `design-grounding` (confirm the family and its
weights actually exist — see [type-pairing](references/type-pairing.md)).

## Choosing type with intent

1. **Pick for voice, not default.** A display serif, a grotesque, a mono accent —
   the typeface *is* the personality. Browse **Typewolf** (real-world "fonts in
   use") and **Fontpair** for grounded pairings; **Fontshare** for quality free
   families beyond the Google defaults.
2. **Pair with contrast, not similarity.** The classic move: an expressive display
   (serif or characterful sans) for headlines + a clean, legible sans for body.
   Contrast in structure, harmony in mood. One family with a strong weight range
   can also carry the whole design.
3. **Confirm it's real.** Verify the family and weights on Google/Adobe Fonts
   before using — don't cite a font that doesn't exist or a weight it lacks.

## Scale & rhythm

- **Modular scale:** base ~16–18px body, a ratio (1.2 minor third → 1.333 perfect
  fourth for more drama). Use type-scale.com to generate real steps.
- **Decisive hierarchy:** headings should clearly out-size body; the "AI tell" is
  an h1 barely larger than a paragraph. Big jumps read intentional.
- **Line length** ~60–75 characters for body; **leading** tighter on large display
  (~1.05–1.15), looser on body (~1.5).
- **Measure & rhythm:** align to a spacing scale so vertical rhythm is consistent.

## Variable fonts & optical detail

- Prefer variable fonts for weight range + performance (one file). Inspect real
  axes with Wakamai Fondue before assuming an axis exists.
- **Variable vs static — verify the weight exists.** A static family ships only
  fixed weights (e.g. IBM Plex Mono has 100/200/300/400/500/600/700 — there is no
  `450`); only a *variable* family has a continuous range. Asking for a weight a
  static family lacks silently falls back to the nearest — a common way to "invent"
  a weight. Confirm the family is variable (and the axis range) via the real
  registry / Wakamai Fondue before citing a non-standard weight.
- **Optical sizing** (`opsz`) where available; tighten letter-spacing on large
  display, leave body alone. Hanging punctuation and optical alignment (`text-
  wrap: balance/pretty`) are the small senior corrections.

## Webfont loading (performance is craft)

- Self-host via **Fontsource** or serve from Google; use `font-display: swap`,
  preload the critical face, and subset to needed characters/weights. A slow font
  flash is a design defect. **Modern Font Stacks** gives zero-load system stacks
  when appropriate.

## Reading it back

Reviewing type: is there a real voice or default Inter? real weight/size contrast
or flat? scale intentional? families/weights verified? webfonts loaded well? Name
the biggest tell and the grounded fix (a real pairing from Typewolf). Color →
`color-systems`; system → `design-systems`.
