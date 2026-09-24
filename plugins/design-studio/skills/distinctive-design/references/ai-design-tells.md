# AI-design tells — catalog + fixes

A working checklist. For each tell: what it is, why it reads as generic, and the
specific fix. Ground fixes in real references (`design-grounding`).

## Color
- **Blurple gradient accent** (blue → purple/violet). → Pick a specific, often
  warm or unexpected accent tied to the brand; ground it in a real palette
  (Coolors/Adobe Color/Radix). One accent, used with intent.
- **Pure `#ffffff` / `#000000`** everywhere. → Warm or cool off-white
  (`#f7f5ef`, `#faf9f6`) and a near-black ink (`#1a1a1a`) read as considered.
- **Rainbow of accents.** → 2–3 colors max; assign roles (surface, ink, accent).

## Type
- **Inter/Roboto/generic geometric sans for everything, one weight.** → A display
  or serif for headlines with real weight/size contrast; keep body clean. Pair
  from Typewolf/Fontpair, not by reflex.
- **No hierarchy** (h1 barely bigger than body). → Real scale (e.g. 1.25–1.333
  ratio), decisive jumps, tight display leading.
- **Emoji headings/bullets.** → Real type, real list markers, or an icon set
  (Lucide/Phosphor) used consistently.

## Layout
- **Everything centered & symmetric.** → Break the axis: asymmetric masthead,
  uneven columns, an editorial grid, deliberate overlap.
- **Three equal cards in a row.** → Vary weight/size (a hero feature + supporting),
  or a different structure entirely (list, editorial rows, a bento with intent).
- **The stock skeleton** hero→3 features→testimonial→pricing→CTA in that order. →
  Reorder around the actual story; let one section dominate; cut a section.
- **Uniform generous padding everywhere.** → Deliberate rhythm: tight where things
  relate, generous where they separate.

## Depth & effects
- **Glassmorphism / `backdrop-filter: blur` on every card.** → Depth from a warm
  ground + hairline borders (ink at low alpha, e.g. `rgba(26,26,26,.1)`) +
  restraint. (Anthropic's site: zero backdrop-filter.)
- **Soft grey drop-shadow on white** as the only depth. → Real light logic, or
  flat with borders, or a single considered shadow.
- **Over-rounded (`rounded-2xl`) everything.** → Choose a radius with intent;
  sharp edges are allowed and often stronger.
- **Glow + gradient + shadow + blur stacked.** → Remove until it hurts. Usually
  one is enough.

## Motion
- **Everything fades-up-on-scroll, same 300ms ease-in-out.** → One characterful
  easing, applied to motion that *means* something (reveals structure, directs
  the eye). Most elements shouldn't animate at all.
- **Autoplay everything.** → Respect `prefers-reduced-motion`; motion earns its place.

## Imagery
- **Generic 3D blobs / abstract gradient meshes with no meaning.** → A real
  photograph, a crafted illustration (DrawKit/unDraw styled), a purposeful 3D
  object (`web-3d`), or honest flat graphics. Meaning over decoration.
- **Obvious AI stock illustration** (melty hands, uncanny gradients). → Curated
  real illustration or commissioned-looking sets; consistent style.

## The meta-tell
- **No point of view.** The design offends no one and moves no one. → Decide on a
  stance and push one idea. If you can't name the idea in a sentence, there isn't
  one yet.

## The new defaults (yesterday's escape is today's cliché)
The moves that once read as "designed" have been absorbed into the average:
- **Cream/warm off-white + high-contrast serif display + terracotta accent** — the
  "editorial warm" cluster. Now a default, including in this plugin's own early
  work. Use it only if it's genuinely right for *this* brand, not by reflex.
- **Near-black + a single acid-green / electric-lime / vermilion accent** — the
  "dark technical" cluster. Same story.
- **Bento grids, oversized single-weight display, one big number per card** — were
  fresh, now templated.
→ Fix: the escape from a default is never another default. Decide from the brief
and real references (`design-grounding`); if you can't say *why this palette for
this brand*, it's a reflex, not a choice.

## How to use this
1. Generate/receive a design. 2. Walk the list; mark every tell present. 3. For
each, apply the fix with a **real reference** to steal from (not "make it modern").
4. Re-check: can you name the single idea the design commits to?
