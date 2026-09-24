---
name: palette
description: Build an intentional, grounded color palette and tokens for a project — a specific accent (not default blurple), warm neutrals, shade scales, dark mode, and real WCAG contrast numbers, verified in real color tools.
argument-hint: [project or mood]
allowed-tools: Read, Write, Edit, WebFetch
---

# Build a color palette

Subject: `$ARGUMENTS`. Load `color-systems`; ground in real tools via
`design-grounding`; avoid default schemes per `distinctive-design`.

1. Take the mood from `.design/direction.md` if present, else ask for the idea.
2. **Pick a specific accent** (not blurple by reflex) and **warm neutrals**
   (off-white surface, near-black ink), assigned to roles (surface/ink/accent/
   border). Ground the choice in a real tool (Coolors/Adobe Color/Radix/Happy Hues)
   and give real hex values.
3. **Generate shade scales** (uicolors.app for Tailwind-style, or Radix Colors for
   accessible light+dark). Design **dark mode** as a real second palette, not an
   invert.
4. **Check contrast with real numbers** (WebAIM/Leonardo): report body-on-surface
   and accent-on-surface ratios and whether they pass WCAG AA/AAA. Fix failures.
5. Output as semantic **tokens** (CSS custom properties / Tailwind config) and, if
   useful, a preview. Save into the direction. Note the source tool for each choice.

Real hexes and real contrast ratios only — never fabricate a number; verify it.
