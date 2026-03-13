# Vision Metrics - Cheat Sheet

Scope: metrics used across Depth Anything 3, MoGe-2, and VGGT

---

## First rule - check the alignment protocol

These papers do not all use the same evaluation convention.

Important variants:
- **scale-invariant**: predictions are aligned by one global scale
- **affine-invariant**: predictions are aligned by scale + shift
- **metric**: no scale rescue at test time; the model must predict the right scale
- **point-map vs depth-map**: same scene, different representation

So before comparing two numbers, always ask:
- is it point error or depth error?
- is it scale-invariant, affine-invariant, or metric?
- are camera intrinsics given or predicted?

---

## Relative and metric geometry metrics

### Point-map relative error
`Rel_p = ||p_hat - p||_2 / ||p||_2`

High-level meaning:
- how close the predicted 3D point is to the ground truth point

### Depth relative error
`Rel_d = |z_hat - z| / z`

High-level meaning:
- average relative depth error per pixel

### Inlier metric: `delta1`
For depth, a common form is:
`max(z_hat / z, z / z_hat) < 1.25`

High-level meaning:
- what fraction of predictions are close enough to the target

### Boundary sharpness (MoGe-2)
- boundary F1 score
- higher means crisper geometric edges and less boundary blur

---

## Pose and reconstruction metrics

### Pose AUC
DA3 and VGGT use pose AUC metrics.

DA3:
- AUC@3 and AUC@30
- built from relative rotation accuracy (RRA) and relative translation accuracy (RTA)

VGGT:
- AUC@30 on Re10K / Co3Dv2
- AUC@3 / @5 / @10 on IMC

High-level meaning:
- how often relative camera poses are accurate within different angular thresholds

### Reconstruction metrics
- Accuracy: distance from prediction to ground truth
- Completeness: distance from ground truth to prediction
- Overall / Chamfer summary: combined reconstruction quality

DA3 also reports:
- precision
- recall
- `F1 = 2 * precision * recall / (precision + recall)`

High-level meaning:
- accuracy says whether your reconstruction is correct
- completeness says whether you recovered all surfaces
- F1 balances both

---

## Rendering metrics

Used for feed-forward novel view synthesis.

### PSNR
- pixel fidelity metric
- higher is better

### SSIM
- structural similarity metric
- higher is better

### LPIPS
- perceptual similarity metric based on deep features
- lower is better

High-level reading rule:
- PSNR / SSIM favor exact image agreement
- LPIPS favors perceptual realism

---

## Matching and tracking metrics

### Image matching AUC
Used by VGGT on ScanNet-1500.

- AUC@5 / @10 / @20
- derived from recovered relative pose accuracy
- higher is better

### TAP-Vid metrics
Used by VGGT downstream tracking experiments.

- AJ: average Jaccard over tracked points and occlusions
- `delta_vis_avg`: fraction of visible points tracked within a pixel threshold
- OA: occlusion accuracy

High-level meaning:
- AJ is the strongest single summary metric
- `delta_vis_avg` measures localization of visible points
- OA measures whether the model knows when a point disappears

---

## Practical reading guide

- use **Rel / delta1** to understand geometry quality
- use **AUC** to understand camera recovery or relative-pose quality
- use **Accuracy / Completeness / F1 / Chamfer** to judge multi-view reconstruction
- use **PSNR / SSIM / LPIPS** for rendering quality
- use **AJ / delta_vis_avg / OA** for dynamic point tracking

---

## One-sentence takeaway

The most important metric lesson across these papers is that a number is only meaningful once you know its alignment setting and whether it measures geometry, pose, rendering, or tracking.
