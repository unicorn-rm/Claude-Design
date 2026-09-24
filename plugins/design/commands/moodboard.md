---
name: moodboard
description: Build a distinctive visual direction from real references — gather and vet real sites/apps/brands, extract a point of view, palette, type, and composition cues, and write the design direction. Grounded in real sources, not generic trends.
argument-hint: [project or vibe]
allowed-tools: Read, Write, Edit, WebFetch, Grep, Glob
---

# Build a visual direction (moodboard)

Subject: `$ARGUMENTS`. Load `design-research` and `design-grounding`; hold the line
with `distinctive-design`.

1. **Gather real references** (not "trends"): pull from the source registry —
   awwwards, Land-book, SiteInspire, Mobbin, Refero, Dribbble/Behance (vetted for
   AI-slop), Typewolf for type, Godly for web. Use WebFetch/browser for public
   pages; for login-gated (Mobbin/Dribbble) ask the user for specific screens.
   Prefer real shipping sites over pretty-but-unbuildable shots.
2. **Vet each** against `distinctive-design`: keep the ones with a point of view;
   drop generic ones. For each keeper, name *what specifically* to steal (masthead,
   rhythm, type feel, color move) — not "the vibe".
3. **Synthesize a direction:** the single idea (one sentence), 3 personality
   adjectives, must-avoid guardrails, a grounded palette (real hexes + a tool), a
   real type pairing (real families), and the structural move for layout.
4. **Write it** to `${CLAUDE_PROJECT_DIR}/.design/direction.md` (design-direction
   schema in `design-grounding`), with the reference links.
5. Summarize the direction and the one idea; offer to build a palette
   (`/design:palette`), type (`/design:typeset`), or the artifact (`/design:artifact`).

Real, linked references only. If a source is blocked, say so and ask for screens —
don't fabricate what's behind the login.
