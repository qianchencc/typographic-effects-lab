# Typographic Effects Lab

A reproducible archive of generative typography and poster-effect reconstruction.

从参考图拆解「字形即画面」的设计机制：脉冲、嵌套轮廓、切片折面、点阵与波纹。保留参考素材、实际图像创建提示词、位图输出、对照试验和质量检查记录。

- Source study: [Xiaohongshu post](https://www.xiaohongshu.com/explore/6af2c6c1000000001b01f805)
- Study date: 2026-11-10
- Scope: 4 reference-guided recreations + 1 text-only comparison
- Fidelity: visual reconstruction, **not** the author's editable source or original prompts
- Output resolution: 941 × 1672 px (RGB PNG)

## Archive

| Study | Reference | Generated | Prompt |
| --- | --- | --- | --- |
| Rhythm Loop / 节奏循环 | [Reference](assets/references/01-rhythm-loop.webp) | [Result](assets/outputs/01-rhythm-loop.png) | [Prompt](prompts/01-rhythm-loop.txt) |
| Spectral Fold / 光谱褶皱 | [Reference](assets/references/02-spectral-fold.webp) | [Result](assets/outputs/02-spectral-fold.png) | [Prompt](prompts/02-spectral-fold.txt) |
| Urban Echo / 都市回声 | [Reference](assets/references/03-urban-echo.webp) | [Result](assets/outputs/03-urban-echo.png) | [Prompt](prompts/03-urban-echo.txt) |
| Wave Memory / 波浪记忆 | [Reference](assets/references/04-wave-memory.webp) | [Result](assets/outputs/04-wave-memory.png) | [Prompt](prompts/04-wave-memory.txt) |
| Urban Echo (text only) | — | [Result](assets/outputs/05-urban-echo-text-only.png) | [Prompt](prompts/05-urban-echo-text-only.txt) |

## How to use

1. Read [skill/SKILL.md](skill/SKILL.md) for the repeatable workflow.
2. Inspect the original and generated images side by side in [comparison.html](comparison.html).
3. Reuse the actual submitted prompts in [prompts/](prompts/), replacing the event content and typography map.
4. Validate exports with `python scripts/check_assets.py`.
5. Review the observed successes, deviations and limits in [docs/experiment-notes.md](docs/experiment-notes.md).

**Note:** Original reference images belong to their respective creator(s) and are archived only for attribution and reconstruction research. Do not present them as newly authored work. Poster event copy is artwork content, not verified event data. The generated PNGs are raster images, not SVG/AI files.


## GitHub Pages

Website: https://qianchencc.github.io/typographic-effects-lab/

The site entrypoint is [index.html](index.html), an exact copy of [comparison.html](comparison.html).
Images remain as separate files under `assets/`; the site does not need a build step.

For the first deployment, open [Settings → Pages](https://github.com/qianchencc/typographic-effects-lab/settings/pages) and select **GitHub Actions** under **Build and deployment → Source**. Then rerun the [Deploy Typographic Effects Lab to GitHub Pages](https://github.com/qianchencc/typographic-effects-lab/actions/workflows/pages.yml) workflow. Later changes to the site and images on `main` deploy automatically.
