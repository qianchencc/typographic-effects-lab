# A mechanical vocabulary for typography-as-image

Each effect starts with an accurate readable glyph mask and a typographic layout. Do not claim the following vector methods were executed in the five image-generation experiments.

| Mechanism | Engineering concept | Tunable controls | Failure mode |
| --- | --- | --- | --- |
| Nested route lettering | repeated equidistant signed-distance contours around glyph skeleton or outline | number of contours, pitch, corner radius, counters | touching lines, closed holes |
| Vertical pulse | intersect sampling columns with glyph mask and vary width/length of tapered strokes | pitch, stroke width, taper, pulse height | needles become unreadable noise |
| Dot-matrix lettering | regular grid with per-site radius determined by glyph coverage | pitch, dot radius, threshold, falloff | arbitrary spacing, illegible letter edge |
| Slice and fold | clip glyph mask to strip geometry; move strips and apply plane-specific affine transforms | slice pitch, displacement, fold angle, seam | random glitch strips instead of folding |
| Wave-modulated type | propagate continuous wave paths then use glyph mask to vary line width/spacing | wavelength, phase, amplitude, base pitch, decay | texture sits behind solid letters |
| Raster-to-vector rebuild | trace select structural lines only, rebuild small text as real type | path tolerance, stroke join, glyph fidelity | indiscriminate auto-trace yields a noisy pseudo-source |

Core order: secure text and hierarchy → define geometric mechanism → enforce negative space → place quiet information grid → inspect crossing zones → export and verify actual dimensions.
