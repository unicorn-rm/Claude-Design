---
name: ux-principles
description: Senior UX methodology — usability heuristics, information architecture, user flows, affordances and feedback, forms and error states, and UX writing/microcopy — so a design is usable, not just pretty. Use when structuring flows or IA, improving usability, designing forms/empty/error states, or writing interface copy.
when_to_use: Structuring user flows or information architecture; improving usability; affordances/feedback/states; designing forms, empty, loading, and error states; UX writing and microcopy.
---

# UX principles (senior methodology)

A beautiful design that's hard to use has failed. UX is the substrate under the
visuals: structure, clarity, and honest feedback. Ground patterns in how real
products solve them (`design-grounding` → Mobbin/Refero/Page Flows), and keep the
craft distinctive, not just conventional (`distinctive-design`).

## Heuristics that catch most problems

Nielsen's heuristics, applied: **visibility of system status** (feedback for every
action), **match to the real world** (plain language, familiar concepts),
**user control** (undo, escape, no dead ends), **consistency**, **error
prevention** over error messages, **recognition over recall** (show options, don't
make people remember), **flexibility**, **minimalist** (every element earns its
place), **good error recovery**, and **help** where needed.

## Information architecture & flows

- Organize by the user's mental model, not the org chart. Clear labels (real words,
  not clever ones). A findable structure beats a pretty menu.
- Map the **flow** for key tasks: the steps, the decision points, the shortest
  honest path. Remove steps; don't add clever ones. Study real flows on Page
  Flows/Mobbin.

## States are the design

- Design the **empty, loading, error, and success** states, not just the happy
  full state. Empty states onboard; error states recover (say what happened + how
  to fix, never blame the user); loading sets expectations. These states are where
  most designs quietly fail.

## Affordances & feedback

- Interactive things should look interactive (affordance); every action gets
  immediate, honest feedback. Don't disguise buttons or fake progress.

## UX writing / microcopy

- Interface copy is design. Be clear, concise, human; label buttons with the action
  ("Create project", not "Submit"); write errors that help. Copy carries more of the
  experience than most effects — and generic "Lorem/placeholder" copy is its own AI
  tell.

## Reading it back

Reviewing UX: is the flow the shortest honest path? are states (empty/loading/error)
designed? is feedback present and honest? is the copy clear and human? Name the
biggest usability gap and the fix. Accessibility → `accessibility`; visual layer →
`web-design`/`layout-and-composition`.
