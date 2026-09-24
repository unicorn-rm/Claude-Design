---
name: typeset
description: Choose and set up typography for a project — a grounded type pairing with a point of view (real families/weights), a modular scale and rhythm, and performant webfont loading. Verified against real font sources.
argument-hint: [project or mood]
allowed-tools: Read, Write, Edit, WebFetch
---

# Set the typography

Subject: `$ARGUMENTS`. Load `typography` (+ type-pairing reference); ground families
in real sources via `design-grounding`; give it a voice per `distinctive-design`.

1. Take the mood from `.design/direction.md` if present, else ask.
2. **Choose type with intent** — a display/body pairing (or one strong family) that
   *means* something for the brand, not default Inter. Ground it: real families and
   weights from Google/Adobe Fonts/Fontshare, feel validated against Typewolf/
   Fontpair. Confirm the weights/axes actually exist.
3. **Set a modular scale** (base + ratio via type-scale.com) with decisive
   hierarchy, real line-length and leading, and a spacing rhythm.
4. **Webfont loading**: `font-display: swap`, preload the critical face, subset,
   self-host via Fontsource if needed. Flag any performance cost.
5. Output the type tokens (families, scale steps, weights, leading) into the
   direction, with a small specimen. Note the source for each family.

Never cite a font or weight you haven't verified exists.
