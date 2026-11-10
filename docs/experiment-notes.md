# 2026-11-10 typography-as-image reconstruction experiment

## Evidence and conditions

Source: [Blue's Xiaohongshu post](https://www.xiaohongshu.com/explore/6af2c6c1000000001b01f805). Four references were inspected. Four image-conditioned runs and one text-only run were created with ChatGPT's built-in image creation. The author’s source project, fonts, original prompts and model logs were not available. No stable random seed, model version, statistical similarity score, print proof or editable vector source was obtained.

All five actual output files were RGB PNG, **941 × 1672 pixels**. Each run produced one result; no subsequent local retouching or interpolation was done in this experiment. See `data/generation-record.json` and `data/asset-manifest.json`.

## Observed outcomes

| Study | Structure retained | Visible departures | Zoom-in focus |
| --- | --- | --- | --- |
| Rhythm Loop | pulse RHYTHM, nested LOOP, dotted BEAT, routed RETURN; O counters; footer | warmer brighter ivory, red more vivid, blue darker, sharpened endpoints | two Os, P extension, RETURN corners |
| Spectral Fold | diagonal slice, horizontal strips, central fold; four-level words | warmer pink, stronger ink contrast and sharper fine lines | FOLD plane change, O/D counters, joins |
| Urban Echo | dot-grid URBAN, nested ECHO, vertical PUBLIC, wave SPACE; left footer margin | green slightly darker, light ink brighter, wave paths smoother, slight background tonal variation | ECHO and vertical drops, PUBLIC-to-wave connection |
| Wave Memory | continuous wave field, delicate TRACE contours, MEMORY and dissolving ARCHIVE; diagonal flow | terracotta more saturated, light ink brighter, grain more conspicuous | TRACE R/A, MEMORY troughs, ARCHIVE tail |

No obvious new misspelling or missing footer copy was seen in the five outputs by visual inspection, but this was not a typographic proofing process. The original upper label for Spectral Fold reads *SPECTRUM* while the large word reads *SPECTRAL*: preserve that difference rather than "correcting" it.

A few dense line crossings and narrow gaps still touch or vary in spacing. No destructive new large-area fusion was seen, but local print safety is unverified.

## Controlled comparison: Urban Echo without a source image

The fifth run reused the verbal specification with references to the attached image removed; no image was attached. Dot-radius URBAN, contour ECHO, pulsed PUBLIC, wavy SPACE and the forest-green/cream palette persisted. However, ECHO grew larger, the four sections became more regular, upper text enlarged, and the left footer blank column disappeared. This one run demonstrates mechanism transfer **not** reproducible exact composition. It is not a multi-seed ablation study.

## Palette sampling

Median RGB in a matching empty footer rectangle (x=420..519, y=1560..1584):

| Study | Reference | Generated |
| --- | --- | --- |
| Rhythm Loop | `#F3EDDA` | `#F8EFD8` |
| Spectral Fold | `#DBA2A3` | `#DFA2A0` |
| Urban Echo | `#033A2A` | `#013824` |
| Wave Memory | `#943D1C` | `#923611` |

These are selected-screen-pixel values, not calibrated print colors or perceptual distance scores. Raw records are in `data/background-samples.json`.

## Generalizable procedures, not proven causal claims

- Give each displayed word an explicit mechanism: pulse width, contour count, fold direction, dot pitch or wave phase. This made outputs inspectable; there was **no** style-words-only baseline to quantify improvement.
- Separate display typography from informational text and list all footer copy verbatim.
- Use a reference image for close layout matching, but expect subtle redraws in colors, counters, endpoints and paper texture.
- Use text-only prompts to transfer visual mechanics; add numeric layout constraints or references for precision.
- Revise one measured/visible deviation at a time while freezing other areas. Suggested revisions here were **not yet executed**.
- Treat raster outputs as raster. Vector/print-ready engineering needs a separate reproducible construction process.

## Next-test template

For each new trial record the source and rights, task mode, full actual prompt, reference assets, actual tool parameters, output SHA256 and pixel size, exact words and reading order, preserved invariants, visible defects, repair instruction, and what remains untested.
