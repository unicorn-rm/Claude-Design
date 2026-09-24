# Type pairing — deep reference

Ground every family/weight in a real source (Google/Adobe Fonts); validate the
*feel* against Typewolf/Fontpair. Pairings below are real, common starting points
— confirm availability, then make it specific to the brief.

## Principles
- **Contrast in structure, harmony in mood.** Pair an expressive display with a
  neutral body, not two similar sans. Or use ONE family with a wide weight range.
- **Limit to two families** (plus maybe a mono for code/labels). Three+ fights.
- **Assign roles:** display (headlines), body (text), optional mono (labels/code).

## Real starting pairs (verify on Google Fonts / Fontshare)
| Display | Body | Feel |
|---|---|---|
| Fraunces (opsz) | Inter / Söhne-like sans | editorial, warm, modern |
| Instrument Serif | Geist / Inter | elegant, restrained |
| Clash Display (Fontshare) | Satoshi (Fontshare) | contemporary, confident |
| Space Grotesk | IBM Plex Sans | technical, characterful |
| Libre Franklin (bold) | Libre Franklin (regular) | one-family, editorial |
| GT-style grotesque / Archivo | Newsreader | magazine, contrast |
| Playfair Display | Source Sans 3 | classic, high-contrast |

> These are anchors, not answers. The point of view comes from choosing a family
> that *means* something for this brand, then confirming it's real.

## Anti-tells
- Inter (or Roboto/Open Sans) for both display and body, one weight → no voice.
- Two similar geometric sans → muddy, no contrast.
- Random Google Font "because it looked cool" with no relation to the brief.
- Display used at body sizes (its optical design breaks) or body used huge.
- Citing a weight a **static** family doesn't have (e.g. `Plex Mono 450`,
  `Instrument Serif 700`) — verify variable-vs-static and the real weights first.

## Scale (type-scale.com)
- base 16–18px; ratio 1.2 (subtle) → 1.333 (dramatic).
- Example (1.25, base 16): 16 · 20 · 25 · 31 · 39 · 49 · 61px.
- Tighten leading as size grows; tighten tracking on large display only.

## Loading
- Variable font, `font-display: swap`, `<link rel="preload">` the critical face,
  subset to used weights/glyphs. Self-host via Fontsource for control.
