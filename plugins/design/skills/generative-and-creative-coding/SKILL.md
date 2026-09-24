---
name: generative-and-creative-coding
description: Senior methodology for generative and creative coding on the web — Canvas/SVG generative art, noise and randomness with control, patterns and generative backgrounds, and creative typography/graphics — used as distinctive, on-brand craft rather than random noise. Use when creating generative backgrounds/art, algorithmic patterns, noise fields, or creative-coded graphics.
when_to_use: Creating generative art/backgrounds; algorithmic patterns; noise fields (Perlin/simplex); Canvas/SVG creative graphics; generative brand marks or textures.
---

# Generative & creative coding (senior methodology)

Generative graphics can give a brand a **signature, living texture** no template
has — or become meaningless noise. The craft is control and intent. Follow
`distinctive-design` (it must serve the idea and the palette) and ground library
APIs in real sources via `design-grounding`.

## Where it earns its place

- **Generative backgrounds/textures** — a subtle animated field, grain, or pattern
  that's on-brand and unique (a strong anti-slop move vs a stock gradient).
- **Generative brand marks / patterns** — systems that produce consistent-but-varied
  graphics (identity, cover art, tickets).
- **Data-driven visuals** — form from real data (ties to `data-visualization`).
Skip it when it's just noise with no relationship to the brand or content.

## Tools & techniques

- **Canvas 2D** — pixels, particles, flow fields; fast for many elements.
- **SVG** — crisp, stylable, animatable vector generative art; great for patterns
  and marks; inspectable and accessible.
- **WebGL/shaders** — GPU generative fields (see `3d-assets-and-shaders`).
- **Libraries:** p5.js (learning/sketching), Paper.js/Two.js (vector), and Canvas/
  SVG directly for production. Haikei/Hero Patterns for ready SVG backgrounds.
- **Noise & randomness with control:** Perlin/simplex noise for organic motion;
  **seed** randomness so results are reproducible; constrain the palette and ranges
  to the brand — unconstrained random looks like noise, constrained random looks
  designed.

## Make it on-brand, not generic

- Use the real **palette** (`color-systems`) and restraint — a generative field in
  two brand colors reads intentional; a rainbow reads like a screensaver.
- Tie the motion to one easing/rhythm; subtle, slow, ambient — background, not
  foreground.

## Performance & accessibility

- Cap particle counts and framerate; pause offscreen; prefer transform/opacity and
  GPU where possible. Provide a static fallback and honor `prefers-reduced-motion`
  (`accessibility`) — an always-moving background is hostile to some users.

## Reading it back

Reviewing generative work: does it serve the brand/idea or is it noise? constrained
palette + controlled randomness? subtle/ambient, not distracting? performant with a
reduced-motion fallback? Name whether it's a signature or a screensaver. Shaders/3D
→ `3d-assets-and-shaders`/`web-3d`; data-driven → `data-visualization`.
