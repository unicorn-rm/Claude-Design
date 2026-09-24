# Canonical design-direction schema

The artifact that captures a grounded, distinctive direction before production.
It's what `distinctive-design` and every producing skill build from, and what
`/brief` + `/moodboard` fill in. Save to `${CLAUDE_PROJECT_DIR}/.design/direction.md`.

```markdown
# Design direction: <project>
Date: <date>

## Brief
- What it is / who it's for / the one job of the design.
- Brand personality in 3 adjectives (e.g. warm, precise, editorial).
- The single idea this design commits to (one sentence). If blank, keep working.

## Must-avoid (anti-slop guardrails)
- <e.g. no blurple gradient, no glassmorphism, no centered-everything, no Inter-only>

## References (real, linked — the things we steal structure from)
- <site/app + link + what specifically we take (masthead / rhythm / type feel)>
- <2–5 real references from awwwards / Mobbin / Refero / Typewolf>

## Palette (grounded + contrast-checked)
- surface: <hex>  ink: <hex>  accent: <hex>  (+ scale if needed)
- contrast: body on surface = <ratio> (AA/AAA), source: <tool>

## Type (real families + scale)
- display: <family, weight>   body: <family, weight>   (source: Google/Adobe)
- scale: base <px> · ratio <e.g. 1.25> · leading <values>

## Layout system
- grid: <columns/asymmetry>  spacing rhythm: <scale>  breakpoints: <...>
- the structural move (what breaks the template).

## Motion
- one easing: <curve>   what actually animates and why: <...>
- reduced-motion behavior.

## Deliverable
- artifact (claude.ai) | shippable HTML/React | tokens/handoff | mockup
```

## Rules
- Every specific (hex, font, class, component, contrast) is grounded — see
  `sources-registry.md`; unverified specifics are labelled, not faked.
- The "single idea" line is mandatory. No idea → the design will read generic.
- References are real and linked; "make it like Stripe" without the specific move
  is not a reference.
