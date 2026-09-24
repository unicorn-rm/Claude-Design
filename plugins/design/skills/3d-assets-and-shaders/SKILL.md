---
name: 3d-assets-and-shaders
description: Senior methodology for sourcing and optimizing 3D assets (Sketchfab, poly.pizza, Poly Haven, Quaternius, Vectary), the glTF pipeline and compression, and shader basics for the web — gradient meshes, custom materials, and Shadertoy-style effects — done with meaning and performance. Use when sourcing 3D models/HDRIs/textures, optimizing glTF, or adding shader effects.
when_to_use: Sourcing 3D models/HDRIs/textures; optimizing/compressing glTF (Draco/meshopt/KTX2); licensing of assets; writing or adapting shaders/gradient meshes; custom materials.
---

# 3D assets & shaders (senior methodology)

Great web 3D is mostly **the right asset, optimized** — plus restrained shader
craft. Follow `web-3d` for the scene; here it's sourcing, the glTF pipeline, and
shaders. Ground every asset/API in real sources via `design-grounding` (real
libraries, real licenses — don't invent), and keep effects meaningful per
`distinctive-design`.

## Sourcing models & maps (real libraries)

| Source | What | Notes |
|---|---|---|
| **poly.pizza** | free low-poly models (glTF) | has an API; CC0-ish, check per-model |
| **Sketchfab** | huge model marketplace/library | licenses vary — **check each**; downloadable + API |
| **Poly Haven** | HDRIs, textures, models | CC0, great for environment lighting |
| **Quaternius** | stylized model packs | CC0 |
| **Vectary** | browser 3D design/export | login-gated |

Always confirm the **license** before shipping an asset — never assume free. For
login-gated, ask the user to export/download.

## The glTF pipeline (this is where perf is won)

- Ship **glTF/glb**, not raw formats. Compress geometry with **Draco** or
  **meshopt**; compress textures with **KTX2/Basis**. Run assets through
  **gltf-transform** or gltfpack to prune, dedupe, and compress.
- Right-size: reduce poly count for web (retopo/decimate), cap texture resolution
  (2K rarely needed for web), bake lighting where static.
- Reuse via **instancing** for repeated objects; merge static meshes to cut draw
  calls. See the perf checklist in `web-3d`.

## Shaders (restrained craft)

- **When:** custom materials, gradient meshes/animated backgrounds, dissolve/
  displacement effects, things standard materials can't do. **When not:** if a
  standard PBR material + good lighting does it, don't write a shader.
- **How:** GLSL vertex/fragment; in R3F use a `shaderMaterial` (drei) or a library.
  Study **Shadertoy** for technique, but adapt — don't ship someone's demo. Keep
  effects meaningful (they should serve the idea, not be noise), and cheap
  (fragment cost scales with pixels).
- **Gradient meshes** (animated color fields) are a tasteful, performant signature
  when restrained — one, on-brand, subtle; not a rainbow.

## Accessibility & fallback

Provide a static fallback for reduced-motion/low-power/no-WebGL; don't gate content
behind a shader that some users can't run.

## Reading it back

Reviewing assets/shaders: licensed correctly? glTF compressed (Draco/KTX2) and
right-sized? draw calls controlled? shader meaningful and cheap, not a copied demo?
fallback present? Name the biggest perf or licensing risk. Scene setup → `web-3d`.
