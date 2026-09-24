---
name: web-3d
description: Senior methodology for 3D on the web — Three.js and React Three Fiber (drei), Spline for no-code scenes, when 3D actually earns its place, integration into a page, and performance/loading. Orchestrates the real libraries rather than reinventing them. Routes to a Three.js + Spline deep reference. Use when adding 3D to a site, evaluating whether 3D fits, integrating a Three.js/R3F/Spline scene, or fixing 3D performance.
when_to_use: Adding web 3D (Three.js/R3F/Spline); deciding whether 3D earns its place; integrating a 3D scene into a page; 3D loading/performance; hero or product 3D.
---

# Web 3D (senior methodology)

3D can make a site unforgettable — or a slow, meaningless gimmick (the generic
"floating gradient blob"). The senior questions are **should this be 3D at all**,
and **does it serve the idea**. Follow `distinctive-design` (meaning over
decoration) and ground APIs/assets in real sources via `design-grounding`
(Three.js/R3F/drei docs, real models — see [threejs-and-spline](references/threejs-and-spline.md)).

## Does 3D earn its place? (ask first)

Use 3D when it **communicates** — a product you rotate, a spatial concept, a
signature brand moment, real interactivity. Skip it when a photo, illustration, or
flat graphic says it better, when the audience is on low-end mobile, or when it's
just "a 3D blob because everyone has one". A meaningless 3D scene is an AI tell with
a performance cost.

## The tools (orchestrate, don't reinvent)

- **Three.js** — the WebGL engine. Powerful, verbose. (If Three.js skills exist in
  the environment — fundamentals, materials, lighting, loaders, postprocessing —
  use them.)
- **React Three Fiber (R3F) + drei** — Three.js as declarative React components +
  ready helpers (controls, loaders, environments). The best path for React sites.
- **Spline** (spline.design) — design 3D scenes no-code and embed; fastest route to
  a branded hero for designers who don't want to write shaders. Watch the runtime
  weight.
Verify component/hook/loader names against real docs; don't invent an API.

## Integrate into the page (not a separate world)

- Match the 3D to the design system: same palette/light mood, real materials, so it
  belongs. A garish default-lit scene clashes with a warm editorial page.
- Composition still applies — the 3D is an element in a `layout-and-composition`,
  not the whole canvas by default. Often best as a contained hero or product moment.

## Performance & loading (this makes or breaks it)

- **Budget:** poly count, texture sizes, draw calls. Use **glTF** (compressed:
  Draco/meshopt), power-of-two/compressed textures (KTX2), instancing for repeats.
  See `3d-assets-and-shaders` for sourcing/optimizing models.
- **Load gracefully:** lazy-load the 3D, show a fallback/poster, suspend on
  React (`Suspense`), and don't block first paint. Cap pixel ratio; pause when
  offscreen.
- **Fallbacks:** a static image/video for reduced-motion, low-power, or no-WebGL.
  Respect `prefers-reduced-motion` for auto-rotation (`accessibility`).

## Reading it back

Reviewing 3D: does it earn its place / serve the idea? does it match the design
system's light and palette? is it within a performance budget with graceful load +
fallbacks? reduced-motion respected? Name whether the 3D is meaningful or a gimmick,
and fix. Assets/shaders → `3d-assets-and-shaders`; motion → `motion-and-interaction`.
