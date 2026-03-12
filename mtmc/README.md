# MTMC papers review — source bundle

This bundle packages the source materials behind the MTMC papers review presentation.

## What is included

- `presentation_report.md` — a Markdown version of the slide deck.
- `code/generate_diagrams.py` — Python code used to generate the custom diagrams and charts.
- `data/*.csv` — source tables used by the plotting code.
- `diagrams/*.png` — regenerated diagram assets.
- `slide_sources.md` — slide-by-slide page-level source mapping from the deck speaker notes.
- `references.md` and `references.bib` — paper citations in readable and BibTeX formats.
- `presentation/mtmc_papers_review.pptx` — the delivered PowerPoint deck.
- `slides_png/*.png` — rendered slide previews.
- `papers/*.pdf` — the five uploaded source papers.

## Regenerating the diagrams

From the extracted bundle root:

```bash
python code/generate_diagrams.py
```

Optional arguments:

```bash
python code/generate_diagrams.py --datadir data --outdir diagrams
```

## Notes on trustworthiness and comparability

- The benchmark charts are based on paper-reported values copied from the uploaded PDFs.
- The executive synthesis scatter is **qualitative** and was created for the presentation to show relative design tendencies, not exact paper metrics.
- The architecture / pipeline figures are **synthesized diagrams** drawn from the cited method sections; they are not paper-native figures.
- Cross-paper benchmark values are **not apples-to-apples** because detectors, training data, and evaluation settings differ.

See `visuals_manifest.md` for a figure-by-figure provenance note.
