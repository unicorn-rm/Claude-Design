---
name: iconography
description: Senior methodology for iconography and simple logo/mark craft — choosing a consistent real icon set (Lucide, Phosphor, Heroicons, Tabler, Iconify), keeping icons consistent (grid, weight, optical size), custom SVG icons, and logotype/mark basics. Use when choosing or using icons, ensuring icon consistency, drawing simple SVG icons, or working on a wordmark/logo mark.
when_to_use: Choosing or using an icon set; keeping icons consistent (weight/grid/optical size); custom SVG icons; simple logotype/mark craft; replacing emoji or mismatched icons.
---

# Iconography (senior methodology)

Icons are small but they betray sloppiness fast — mismatched sets, inconsistent
weights, or emoji standing in for real iconography (an AI tell). Follow
`distinctive-design`; use a real, consistent set grounded via `design-grounding`
(real icon libraries — don't invent icon names).

## Choose one real set and commit

- **Lucide** (shadcn's default), **Phosphor** (multiple weights), **Heroicons**,
  **Tabler**, **Radix Icons**, and **Iconify** (aggregates most sets + API) are the
  standard real sources; **Simple Icons** for brand logos.
- Pick **one** family for the UI so weight, corner radius, and grid match. Mixing
  Heroicons + Font Awesome + emoji is the tell. Verify icon names exist in the set.
- Never use emoji as UI icons/section markers — replace with the chosen set.

## Keep them consistent

- **Grid & optical size:** icons drawn on the same grid (e.g. 24px), aligned
  optically to text (visual center, not metric). Size icons to the type they sit
  beside; don't mix 16px and 28px randomly in one row.
- **Weight:** match stroke weight to the type weight and to each other; Phosphor's
  weight variants help match a light or bold UI.
- **Color/state:** icons inherit token colors (`currentColor`), get the same
  hover/active treatment as their control.

## Custom SVG icons

- When the set lacks one, draw it on the **same grid and stroke weight** so it
  belongs. Optimize the SVG (SVGO), use `currentColor`, give it an accessible name
  if it carries meaning (`accessibility`).

## Logotype / mark basics

- A considered **logotype** (the brand name set in the right typeface, optically
  spaced) often beats a generic abstract mark. Keep marks simple, legible at small
  sizes, and monochrome-first (works in one color before you add any). Provide clear
  space and min sizes. Deep brand identity → `brand-identity`.

## Reading it back

Reviewing icons: one consistent real set? matched weight/grid/optical alignment?
`currentColor` + tokenized? no emoji-as-icons? custom ones on-grid? Name the
inconsistency and the fix. Brand marks → `brand-identity`; SVG systems →
`design-systems`.
