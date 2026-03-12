# Source evidence notes

This file records the source-paper locations used for the presentation report.

## Depth Anything 3

- **Abstract (p. 1):** DA3 predicts spatially consistent geometry from an arbitrary number of visual inputs, with or without known camera poses.
- **Abstract (p. 1):** The paper argues that a single plain transformer backbone plus a single depth-ray target is sufficient, rather than a large bespoke multi-task stack.
- **Abstract (p. 1):** DA3 reports average gains of **35.7% in camera pose accuracy** and **23.6% in geometric accuracy** over VGGT on the benchmark defined in the paper.
- **Sec. 1 and Fig. 2 (pp. 3–5):** The model uses a pretrained ViT / DINO-style backbone, input-adaptive cross-view self-attention, an optional camera encoder, and a dual-DPT head for depth and ray prediction.
- **Sec. 4.2 (p. 10):** Teacher depth is aligned to sparse metric depth with a robust scale-shift procedure for real-world data.

## MoGe-2

- **Abstract (p. 1):** MoGe-2 predicts a metric-scale 3D point map from a single image and explicitly aims to combine relative geometry accuracy, metric prediction, and fine detail.
- **Sec. 1 (pp. 1–2):** The model builds on MoGe and explores two routes to metric geometry, concluding that a **decoupled affine-invariant representation plus a separate global scale prediction** works best.
- **Fig. 2 / Sec. 3 (p. 4):** The architecture uses a DINOv2 ViT, an affine-invariant point-map path, and a CLS-token MLP scale head.
- **Table 4 (p. 9):** The decoupled CLS-MLP design improves metric geometry over entangled variants and reaches **F1 = 12.5** for the refined-real-data training setup.
- **Table 4 (p. 9):** The ablation shows a **10.3 → 12.5** F1 improvement from raw real data to refined real data, supporting the presentation's emphasis on data refinement.

## VGGT

- **Abstract (p. 1):** VGGT directly predicts camera parameters, point maps, depth maps, and 3D point-track features from one, a few, or hundreds of views in a single forward pass.
- **Sec. 1 (pp. 1–2):** The paper frames VGGT as a feed-forward alternative to iterative geometry pipelines and emphasizes multi-task 3D prediction from a shared transformer.
- **Fig. 2 / Sec. 3.2 (p. 3):** The architecture patchifies inputs with DINO, adds camera tokens, alternates frame-wise and global attention, and uses a camera head plus DPT heads.
- **Sec. 1 (pp. 1–2):** The paper also positions VGGT features as a reusable backbone for downstream point tracking and novel-view synthesis style tasks.

## Stability note

The original PowerPoint deck contained a rough status / citation-count slide. Those fields are time-sensitive and were **not** carried into the cleaned report. The literal extraction in `report/slide_text_dump.md` keeps them only as an exact record of the deck text.
