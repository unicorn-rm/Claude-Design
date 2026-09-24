---
name: accessibility
description: Senior methodology for accessible design — WCAG contrast, keyboard and focus, semantic structure, ARIA where needed, forms, images/alt, reduced motion, and target sizes — as a craft integrated into design, not a bolt-on audit. Use when designing or reviewing for accessibility, checking contrast, ensuring keyboard/screen-reader support, or meeting WCAG.
when_to_use: Designing or reviewing for accessibility; checking WCAG contrast; keyboard/focus/screen-reader support; semantic HTML/ARIA; forms; reduced motion; target sizes; meeting AA/AAA.
---

# Accessibility (senior methodology)

Accessible design is better design — it forces real hierarchy, honest contrast, and
clear structure. Treat it as craft woven in, not an audit at the end. Ground
contrast and criteria in real specs via `design-grounding` (real WCAG numbers, real
ratios — don't guess). It also reinforces `distinctive-design`: many AI tells (low-
contrast greys, decorative-only cues) are accessibility failures too.

## Contrast (real numbers)

- **WCAG AA:** text ≥ **4.5:1** (normal), ≥ **3:1** (large ≥ 24px or 18.7px bold).
  UI components/graphics ≥ 3:1. AAA is 7:1 / 4.5:1.
- Verify with a real tool (WebAIM contrast, Leonardo) and **report the ratio** —
  never assert "passes" without the number. Low-contrast light-grey-on-white is
  both an a11y fail and an AI tell.
- Don't rely on color alone to convey meaning (add text/icon/pattern).

## Keyboard & focus

- Everything interactive must be reachable and operable by keyboard, in a logical
  order. **Visible focus states** (don't remove outlines — restyle them). Skip-link
  to main. Manage focus for modals/menus (Radix/shadcn handle this — `ui-components`).

## Semantics & screen readers

- Use real semantic elements (`nav`, `main`, `button`, `h1–h6` in order, `label`
  for inputs) before reaching for ARIA. ARIA only to fill gaps, correctly — wrong
  ARIA is worse than none.
- Images: meaningful `alt`; decorative images empty `alt`. Icons that carry meaning
  need accessible names.

## Forms

- Labels tied to inputs, clear error messages (not color-only), grouped fields,
  visible focus, adequate hit areas.

## Motion & targets

- Honor `prefers-reduced-motion` (reduce/disable non-essential motion —
  `motion-and-interaction`). Touch targets ≥ ~44px. Don't trap or auto-advance.

## Reading it back

Reviewing a11y: real contrast numbers reported and passing? keyboard-operable with
visible focus? semantic structure + correct labels? meaning not color-only? reduced
motion respected? Name failures with the exact fix and number. Part of a full
`/design-studio:review`; ties into `color-systems` (contrast) and `ux-principles`.
