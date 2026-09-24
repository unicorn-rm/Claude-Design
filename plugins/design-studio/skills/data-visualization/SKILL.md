---
name: data-visualization
description: Senior methodology for data visualization and dashboards in a design context — choosing the right chart, honest and legible encodings, accessible chart color, dashboard layout and hierarchy, and real tools (Tremor, D3, Recharts). Use when designing charts, dashboards, KPIs, or data-heavy UI, or fixing misleading or cluttered visualizations.
when_to_use: Designing charts/graphs/dashboards/KPIs; choosing a chart type; chart color and legibility; dashboard layout; making a visualization honest and accessible; data-heavy UI.
---

# Data visualization (senior methodology)

Good data viz is honest, legible, and quietly beautiful — bad data viz misleads or
overwhelms. Treat it as design with a truth constraint. Follow `distinctive-design`
(clarity over chart-junk) and ground chart types/tools/color in real sources via
`design-grounding`. If a dedicated dataviz skill exists in the environment, use it
for depth.

## Choose the right chart for the question

Match the encoding to the question: **trend over time → line**; **compare
categories → bar** (usually beats pie); **part-to-whole → stacked/100% bar** (pie
only for a couple of slices); **distribution → histogram/box**; **relationship →
scatter**; **single KPI → a big number + sparkline**. The wrong chart is a design
bug, not a style choice.

## Honesty first

- **Bar charts start at zero** (truncating exaggerates). Consistent, linear scales
  unless clearly labeled. Don't distort area/3D. One idea per chart.
- Label directly where possible (beats a legend hunt); units and context always.

## Legibility & restraint

- Remove chart-junk: heavy gridlines, 3D, redundant legends, decorative fills.
  Maximize data-ink. The data is the hero.
- Type and spacing still apply (`typography`, `layout-and-composition`); a chart is
  a small composition.

## Accessible chart color

- Don't encode by color alone (add labels/patterns/shape); ensure series colors are
  distinguishable for color-blindness and pass contrast against the background
  (`accessibility`). Use a real categorical/sequential palette, not random hues.

## Dashboards

- Hierarchy: the most important metric is biggest/top-left; group related metrics;
  don't dump every chart on one screen. Consistent card/KPI treatment
  (`design-systems`).
- **Tools:** Tremor (React KPI/chart components), Recharts, or D3 for custom. Verify
  the real API; restyle to the tokens so it's on-brand, not the library default.

## Reading it back

Reviewing a viz: right chart for the question? honest scales (zero baseline)? chart-
junk removed? color accessible and not the only encoding? dashboard hierarchy clear?
Name the misleading or cluttered part and the fix. Color → `color-systems`;
components → `ui-components`.
