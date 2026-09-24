---
name: visual-critique
description: Senior design critique — reviewing a design, screenshot, or live site and naming exactly why it works or reads as generic/AI-templated, with specific, grounded fixes and real references to steal from. Use to review or critique a design, get feedback on a mockup or site, or diagnose why something feels off or "AI-made".
when_to_use: Reviewing/critiquing a design, screenshot, mockup, or live site; diagnosing why something looks generic/AI-made or "off"; getting actionable, specific design feedback.
---

# Design critique (senior methodology)

A good critique is **specific and actionable**, never "make it more modern". You
name what's there, why it helps or hurts, and the concrete fix — grounded in real
references (`design-grounding`) and measured against the anti-slop doctrine
(`distinctive-design`). This skill is honest and useful, not flattering.

## The critique method

1. **State the intent.** What is this trying to be/do (the one idea)? If you can't
   find one, that's finding #1 — it reads generic because it commits to nothing.
2. **Walk the anti-slop tells** (`distinctive-design` → ai-design-tells): blurple/
   default color, one-weight Inter, centered-everything, three equal cards, stock
   skeleton, glassmorphism, over-rounding, meaningless motion. Mark each present.
3. **Walk the fundamentals:** hierarchy (does the eye go where it should?), type
   (voice + contrast + scale), color (intentional + contrast/WCAG), layout
   (grid/asymmetry/whitespace), spacing rhythm, accessibility.
4. **Name the top 3 issues by impact**, each with: what it is → why it hurts → the
   specific fix → (where useful) a real reference to steal the better solution from.
5. **Say what's working** and should be kept — a critique that only tears down
   isn't senior.

## Rules of a useful critique

- **Specific, not vague.** "The h1 is 20px and the same weight as body, so there's
  no hierarchy — take it to a 40px display cut with tighter leading, like <real
  reference>" beats "needs more contrast".
- **Grounded.** Cite real fixes (a real font, a real palette move, a real site's
  structure), and real numbers for contrast — don't invent.
- **Prioritized.** Impact order; don't drown the user in 30 nits. Fix the tells and
  the hierarchy first.
- **Kind and honest.** Critique the design, not the person; be direct about what's
  generic.

## Reading it back / output

Deliver: intent, tells present, top issues (with grounded fixes + references),
what's working, and the single highest-leverage change. Drive via `/design:critique`
or a full `/design:review` (adds a11y + responsive). Turning fixes into a new
version → `web-design` + `design-to-artifact`.
