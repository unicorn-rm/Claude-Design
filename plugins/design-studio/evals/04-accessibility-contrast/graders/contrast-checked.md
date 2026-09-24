---
type: llm
focus: last_message
weight: 3
---
The user proposed #B0B0B0 body text on white (#FFFFFF) — a low-contrast choice that
fails WCAG.

Score PASS if the response evaluates the actual contrast against WCAG (notes it
fails AA for normal text — the real ratio of #B0B0B0 on white is ~2.5:1, well under
4.5:1), explains why low-contrast grey-on-white is both an accessibility failure and
a generic "AI" tell, and gives a grounded fix (a darker ink, a real ratio target).
Reporting a concrete ratio and the 4.5:1 threshold is a strong PASS.

Score FAIL if it approves the low-contrast text, ignores accessibility, or gives no
real contrast reasoning/numbers.
