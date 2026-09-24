# Three.js / R3F / Spline — deep reference

Verify APIs against real docs (threejs.org, R3F/drei GitHub, Spline docs) via
`design-grounding`. If environment Three.js skills exist, prefer them for depth.

## Three.js core (mental model)
Scene graph: **Scene** contains **Mesh** = **Geometry** + **Material**, lit by
**Lights**, viewed by a **Camera**, drawn by the **WebGLRenderer** each frame
(render loop). Add **OrbitControls** for interaction, an **environment/IBL** for
realistic lighting, and a **loader** (GLTFLoader) for models.

## React Three Fiber (best for React sites)
- `<Canvas>` sets up renderer/scene/camera; JSX elements map to Three objects
  (`<mesh><boxGeometry/><meshStandardMaterial/></mesh>`).
- **drei** helpers: `OrbitControls`, `Environment`, `useGLTF`, `Float`, `Html`,
  `PresentationControls`, `ContactShadows`, `Bounds`. Huge time-savers.
- Loading: `useGLTF('/model.glb')` + `<Suspense fallback={...}>`; preload with
  `useGLTF.preload`.
- Frame loop: `useFrame((state, delta) => ...)` for animation.

## Materials & light (why scenes look cheap or good)
- Prefer **MeshStandardMaterial/MeshPhysicalMaterial** (PBR) with an **environment
  map** (HDRI from Poly Haven) for believable lighting — flat default lighting is
  the "cheap 3D" tell.
- Match the scene's light mood to the page palette; subtle, not blown-out.

## Spline (no-code → embed)
- Design the scene in spline.design, export a web embed or use the react-spline
  runtime. Fastest branded 3D for non-coders. Cost: runtime JS weight — lazy-load,
  show a poster, and check mobile perf.

## Performance checklist
- glTF/glb with **Draco** or **meshopt** compression; **KTX2** compressed textures.
- Limit draw calls (merge/instance), cap `dpr` (`[1, 2]`), dispose unused, pause
  when offscreen (IntersectionObserver / drei `useInView`).
- Lazy-load the whole 3D bundle; static fallback for reduced-motion/no-WebGL.

## Where to get models/HDRIs
poly.pizza (free low-poly, API), Sketchfab (huge, licenses vary), Poly Haven
(HDRIs/textures/models, CC0), Quaternius (CC0 packs). See `3d-assets-and-shaders`.
