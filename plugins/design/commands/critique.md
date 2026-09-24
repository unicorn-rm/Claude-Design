---
name: critique
description: Critique a design, screenshot, or live site — name what works and what reads as generic/AI-templated, with specific, grounded fixes and real references. Honest and actionable, prioritized by impact.
argument-hint: [file, url, or description]
allowed-tools: Read, WebFetch, Grep, Glob
---

# Critique a design

Target: `$ARGUMENTS` (a file/screenshot, a URL, or a described design; fetch/read it).

Load `design-critique`; measure against `distinctive-design`; ground fixes in
`design-grounding`.

1. **Intent** — what is this trying to be, and what's its one idea? If none, say so
   first (it's why it reads generic).
2. **Tells** — walk `distinctive-design` → ai-design-tells; mark each present
   (blurple, one-weight Inter, centered-everything, three equal cards, stock
   skeleton, glassmorphism, over-rounding, meaningless motion).
3. **Fundamentals** — hierarchy, type (voice/contrast/scale), color + **contrast
   with real numbers**, layout/whitespace/asymmetry, spacing rhythm.
4. **Top 3 issues by impact** — each: what → why it hurts → specific fix → a real
   reference to steal from where useful. Then **what's working** (keep it), and the
   **single highest-leverage change**.
5. Offer to build the improved version (`/design:artifact`).

Specific and grounded only — never "make it more modern", never invent a hex/font/
ratio. For a full review incl. accessibility + responsive, use `/design:review`.
