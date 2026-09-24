---
name: brief
description: Capture the design brief and direction for this project (brand, audience, mood, the one idea, must-avoid guardrails, real references) so distinctive-design and design-grounding have real context to work from.
argument-hint: [project name]
allowed-tools: Read, Write, Edit, WebFetch
---

# Capture the design brief & direction

You are setting up the design direction this project works from. `distinctive-design`
and `design-grounding` read it before producing anything.

1. Collect from the user (ask for anything missing, one concise batch):
   - **What & who:** what is it, who's the audience, the one job of the design.
   - **Personality:** 3 adjectives (e.g. warm, precise, editorial).
   - **The one idea:** the single stance this design commits to. If the user is
     unsure, help derive it — a design without an idea reads generic.
   - **Must-avoid:** anti-slop guardrails (e.g. no blurple gradient, no
     glassmorphism, not Inter-only, not centered-everything) and any brand rules.
   - **References:** real sites/apps/brands they like and *what specifically*
     about each. If they have none, offer to pull some via `design-research`.
   - **Constraints:** existing brand assets/tokens, tech (React/Tailwind?),
     deliverable (artifact / shippable HTML / handoff).

2. Ground anything checkable via `design-grounding` (real fonts, real palette,
   real reference links). Don't invent brand colors or "trends".

3. Write the direction to `${CLAUDE_PROJECT_DIR}/.design/direction.md` using the
   design-direction schema (see `design-grounding` → design-direction-schema).

4. Confirm back the captured direction and the single idea, and remind the user
   that design work will now be checked against it by `distinctive-design`
   (anti-slop) and grounded by `design-grounding`.

Do not fabricate a brand or references the user didn't give. If the "one idea" is
still blank, say so — that's the first thing to solve.
