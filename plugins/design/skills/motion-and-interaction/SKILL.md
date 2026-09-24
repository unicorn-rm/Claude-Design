---
name: motion-and-interaction
description: Senior methodology for web motion and micro-interactions — meaningful animation, one considered easing, scroll-driven effects (GSAP/ScrollTrigger), Framer Motion, micro-interactions and state transitions, performance, and respecting reduced motion. Leans on real libraries, doesn't reinvent them. Use when adding animation/interaction, scroll effects, micro-interactions, or fixing janky/meaningless motion.
when_to_use: Adding animation or micro-interactions; scroll-driven effects (GSAP/ScrollTrigger); page/element transitions (Framer Motion); easing choices; motion performance; respecting prefers-reduced-motion.
---

# Motion & interaction (senior methodology)

Motion should **mean something** — reveal structure, guide the eye, give feedback —
not decorate. The AI tell is "everything fades-up-on-scroll with the same 300ms
ease-in-out". Senior motion is restrained, characterful, and performant. Follow
`distinctive-design`; ground library APIs in real docs via `design-grounding`
(GSAP/Framer Motion/Motion — verify, don't invent).

## Principles

1. **Meaning over decoration.** Animate to communicate: reveal hierarchy, show
   cause→effect, confirm an action, orient during navigation. If a motion says
   nothing, cut it. Most elements shouldn't animate.
2. **One considered easing.** Pick a single characterful curve (a custom
   cubic-bezier, not the default ease) and reuse it — that consistency reads as a
   designed system. Duration short for UI (~150–250ms), longer for large reveals.
3. **Micro-interactions matter most.** Button/press feedback, hover intent, input
   focus, toggle transitions, optimistic states — small, fast, honest. These carry
   more perceived quality than a flashy hero.
4. **Natural physics where it fits.** Spring/inertia (Framer Motion springs) for
   things that should feel physical; but restraint — not everything bounces.

## The tools (lean on real libraries)

- **CSS transitions/animations** — the default for simple state/hover/enter; cheapest.
- **Framer Motion / Motion** — React declarative animation, layout animations,
  gestures, springs. Great for component and page transitions.
- **GSAP + ScrollTrigger** — the standard for complex, timeline-based and
  scroll-driven sequences (pinning, scrubbing, parallax). Use for real
  choreography; verify the API. (If a GSAP/ScrollTrigger skill exists in the
  environment, use it.)
- **Lottie/Rive** — designed vector/interactive animation from real files.
Don't hand-roll what these solve; do restyle so it's not the library's demo.

## Scroll effects without the slop

Scroll-triggered reveals are fine — once, with intent, one easing. Avoid every
section fading up identically. Parallax and pinning must serve the story; gratuitous
scroll-jacking hurts usability. Keep it subtle.

## Performance

- Animate **transform** and **opacity** (GPU-friendly); avoid animating layout
  properties (width/top/left) that thrash. Use `will-change` sparingly. Watch for
  jank on mobile; test on a real device.

## Accessibility (non-negotiable)

- Honor **`prefers-reduced-motion`**: reduce or remove non-essential motion, kill
  parallax/auto-play. Never trap or force motion. (See `accessibility`.)

## Reading it back

Reviewing motion: does each animation mean something, or is it decoration? one
consistent easing, or defaults everywhere? micro-interactions present? transform/
opacity only? reduced-motion respected? Name the meaningless motion and cut/fix it.
3D scenes → `web-3d`; generative backgrounds → `generative-and-creative-coding`.
