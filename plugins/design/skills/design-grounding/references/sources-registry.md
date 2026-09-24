# Design source registry

Ground truth for design decisions. Prefer reading real current work over reciting
"trends". Access model per row: **WF** = WebFetch/browser (public), **API** = has
an API, **GH** = GitHub code, **LG** = login-gated (use as named reference, ask
the user for screens).

## Color
| Source | Use | Access |
|---|---|---|
| Coolors (coolors.co) | palette generation, export | WF/API-ish (export URLs) |
| Colorhunt (colorhunt.co) | curated palettes | WF |
| Adobe Color (color.adobe.com) | harmony rules, extract from image | WF/LG |
| Happy Hues (happyhues.co) | palettes shown *in context* (great for UI roles) | WF |
| Khroma (khroma.co) | AI-trained personal palettes | LG |
| uicolors (uicolors.app) | Tailwind-style shade scales from one color | WF |
| Realtime Colors (realtimecolors.com) | preview a palette on a real UI live | WF |
| Radix Colors (radix-ui.com/colors) | accessible, dark-mode-ready scales | WF/GH |
| Open Color (yeun.github.io/open-color) | open UI color scheme | WF/GH |
| Tailwind palette (tailwindcss.com) | default scale reference | WF |
| Leonardo (leonardocolor.io) / WebAIM contrast | contrast + accessible ramps | WF |

## Type
| Source | Use | Access |
|---|---|---|
| Google Fonts (fonts.google.com) | free webfonts, real families/weights | WF/API |
| Adobe Fonts (fonts.adobe.com) | pro families | LG |
| Typewolf (typewolf.com) | real-world pairings, "fonts in use", lists | WF |
| Fontpair (fontpair.co) | Google Font pairings | WF |
| Fontshare (fontshare.com) | quality free fonts (Indian Type Foundry) | WF |
| Fontsource (fontsource.org) | self-host webfonts via npm | WF/GH |
| Modern Font Stacks (modernfontstacks.com) | system-font stacks, zero-load | WF |
| type-scale.com | modular type scale ratios | WF |
| Wakamai Fondue (wakamaifondue.com) | inspect a variable font's axes | WF |

## Inspiration / direction (real work to steal structure from)
| Source | Use | Access |
|---|---|---|
| Awwwards (awwwards.com) | top-tier web craft | WF |
| Land-book, Lapa Ninja, Landingfolio, SaaSLandingPage | landing galleries | WF |
| SiteInspire, Minimal.gallery, Httpster, Godly (godly.website) | curated web | WF |
| recent.design, Screenlane, Curated.design, CSSDA, The FWA | more galleries | WF |
| Mobbin (mobbin.com) | real app UI flows/screens (huge) | LG |
| Refero (refero.design) | web + app reference library | WF/LG |
| Page Flows (pageflows.com) | UX flows/onboarding | LG |
| Dribbble, Behance, Pinterest, ArtStation | visual direction (vet for AI-slop!) | WF/LG |

> Dribbble/Pinterest bias toward pretty-but-unbuildable; use for mood, verify
> against real shipping sites (Awwwards/Mobbin) before committing.

## Components (real code)
| Source | Use | Access |
|---|---|---|
| shadcn/ui (ui.shadcn.com) | Radix + Tailwind components you own | WF/GH |
| Radix UI (radix-ui.com) | headless accessible primitives | WF/GH |
| Tailwind CSS (tailwindcss.com) / Tailwind UI | utility CSS / pro components | WF |
| Aceternity UI (ui.aceternity.com), Magic UI (magicui.design) | animated sections | WF/GH |
| HyperUI (hyperui.dev), Flowbite (flowbite.com), daisyUI | Tailwind component sets | WF/GH |
| 21st.dev | community shadcn-style registry | WF |
| Park UI, Origin UI, Cult UI, Kokonut UI | more component libs | WF/GH |
| Tremor (tremor.so) | React dashboard/chart components | WF/GH |
| Motion (motion.dev / framer-motion), Headless UI | animation / headless | WF/GH |

## 3D / graphics
| Source | Use | Access |
|---|---|---|
| Three.js (threejs.org) + React Three Fiber / drei | web 3D engine + React | WF/GH |
| Three.js Journey (threejs-journey.com) | the canonical learning reference | WF |
| Spline (spline.design) | no-code 3D scenes → web embed | WF/LG |
| Sketchfab (sketchfab.com) | 3D model marketplace/library | WF/API/LG |
| poly.pizza | free low-poly models (glTF) | WF/API |
| Vectary (vectary.com) | browser 3D design | LG |
| Poly Haven (polyhaven.com) | free HDRIs, textures, models | WF/API |
| Quaternius (quaternius.com) | free stylized model packs | WF |
| Shadertoy (shadertoy.com) | GLSL shader reference | WF |
| Rive (rive.app), Lottie/LottieFiles | interactive/vector animation | WF/LG |
| Haikei (haikei.app), Hero Patterns, SVG Backgrounds | SVG backgrounds/blobs | WF |
| DrawKit, unDraw, Blush, Open Doodles, Humaaans | illustration | WF |

## Icons
Lucide (lucide.dev), Heroicons, Phosphor (phosphoricons.com), Tabler Icons,
Iconify (iconify.design — aggregates most sets), Radix Icons, Simple Icons
(brand logos). All WF/GH; Iconify has an API.

## GitHub — first-class source
Search GitHub for real, current component code and ready solutions before
inventing anything: component libraries (above), `awesome-design`, `awesome-web-
design`, `awesome-threejs`, template repos, and the actual source of any library
you cite. Read the real API from the repo; don't guess it.

## Rule
If a fetch/login blocks a source, say the specific is **unverified** and either
use an accessible equivalent or ask the user to pull the screen — never fabricate
what's behind the gate.
