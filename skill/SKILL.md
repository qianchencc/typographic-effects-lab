---
name: typographic-effects-lab
description: Analyze and reproduce typography-as-image posters using pulse lines, contour routing, sliced folds, dot matrices, and wave-modulated letterforms. Preserve visual evidence, exact prompts and QA observations.
---

# 字体构图海报复刻 / Typographic Effects Lab

Use this skill when asked to reconstruct a typographic visual, design a poster in the same structural language, or document an image-generation experiment. This is a procedure for visual reconstruction, **not** an original font, an editable Illustrator document, or a claim about the source author's workflow.

## 0. Choose the task mode

- **Reference-guided reconstruction**: favor composition fidelity, word positions, scale, whitespace and palette, while tracking any regenerated details.
- **Style/mechanism transfer**: keep the dot/line/slice mechanisms, change words and layout as needed.
- **Text-only exploration**: allow geometric variation and document departures from the source; do not promise pixel-aligned reproduction.
- **Engineering rebuild**: construct actual vector geometry separately. Do not mislabel an image-generated PNG as an SVG or AI source.

## 1. Inspect before generating

Read the source image from top to bottom. Build a table: exact word, reading order, width/height/position, construction mechanism, stroke spacing, counter/negative-space constraints, line continuity, color, and information-area text. Distinguish the structure letters from small editorial text. Note image provenance and access date.

## 2. Describe observable operations

Avoid relying only on words like "experimental", "premium", "retro" or "sound wave." Express how each glyph becomes the graphic:

- **Pulse**: a regular array of vertical tapered strokes; thicken within glyphs; decay toward dot trains.
- **Nested routes**: repeated even-spaced letter contours, readable holes and smooth turning radii.
- **Slice/fold**: bands clipped across letters, selected lateral offsets, different affine transforms on adjacent planes, consistent fold seam.
- **Dot-matrix**: ordered dot grid; dot radius modulated by glyph coverage while grid pitch stays constant.
- **Wave-letter**: establish continuous aligned wave paths; modulate stroke weight by a glyph mask; create dots and dashes only at decay zones.

See [mechanisms](../docs/mechanisms.md) and the [source study](../docs/experiment-notes.md).

## 3. Prompt order

1. Output: one full poster, aspect ratio, full bleed, flat print, not mockup.
2. Composition lock: exact word order, hierarchy, relative bands and footer.
3. Palette and explicit no-go decoration.
4. For each main word: concrete mechanism, counts/spacing/line joins and required counters.
5. Exact metadata and editorial copy, separately from distorted display typography.
6. Negative constraints: no unrelated images, glow, chrome, random noise or extra words.

For close reconstruction attach the matching image as reference; never claim an image was attached when it was not. The five prompts in `../prompts/` are **actual submitted prompts** from this study, not perfected prompts inferred later.

## 4. Generate and inspect

Produce each poster separately. Inspect the whole composition, then small text, then zoom into: internal counters, turn corners, fold seams, pulse-to-dot transitions, dense wave troughs, and footer grid. Compare original and output side by side, and sample colors only in matching uniform regions. Every correction should name one concrete visible defect and explicitly freeze unaffected areas.

## 5. Keep evidence and limits

Record source URL/date, mode, actual input prompt, reference inputs, parameters that were actually set, output artifact, actual dimensions/file format, observed successes, observed deviations and untested hypotheses. Never invent a seed, model version, similarity score or vector editing provenance. Report true pixel size; increasing DPI metadata alone does not add detail. Seek explicit rights clearance before redistributing reference artwork beyond research.

## Reference set

- Rhythm Loop: `../assets/references/01-rhythm-loop.webp`
- Spectral Fold: `../assets/references/02-spectral-fold.webp`
- Urban Echo: `../assets/references/03-urban-echo.webp`
- Wave Memory: `../assets/references/04-wave-memory.webp`

The matching generated results are under `../assets/outputs/` (Wave Memory has a chunked archival copy recoverable via `scripts/restore_full_outputs.py` if the full PNG is not present yet). Use the complete original prompt text in `../prompts/`.
