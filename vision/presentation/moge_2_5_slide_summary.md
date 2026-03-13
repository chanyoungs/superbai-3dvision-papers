# MoGe-2 - 5 Slide Summary

Source paper: MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details

---

## Slide 1 - Problem and target

### Monocular metric geometry

Goal: predict a metric-scale 3D point map from one image.

The paper's target is not just depth quality.
It wants:
- accurate relative geometry
- correct metric scale
- sharp boundaries and local detail

---

## Slide 2 - Core design

### Decouple scale from geometry

Pipeline:
image -> DINOv2 ViT -> shared convolutional neck -> affine-invariant point map + mask

Parallel branch:
CLS token -> MLP -> global scale factor

Final metric output:
`metric point map = s_hat * P_hat`

Why this matters:
- direct metric point-map regression is unstable
- decoupling scale protects relative geometry accuracy

---

## Slide 3 - Datasets

### Evaluation coverage

Relative geometry:
- NYUv2, KITTI, ETH3D, iBims-1, GSO, Sintel, DDAD, DIODE, Spring, HAMMER

Training:
- 24 datasets total
- mix of synthetic, LiDAR, and SfM data

Main purpose:
- stress relative geometry, metric scale, and boundary sharpness from one image

---

## Slide 4 - Metrics

### How MoGe-2 is judged

Relative geometry:
- point-map `Rel_p`
- depth `Rel_d`
- `delta1` inlier ratios
- scale-invariant and affine-invariant settings

Metric geometry:
- metric point-map error and `delta1`
- metric depth error and `delta1`

Detail quality:
- boundary F1 score

---

## Slide 5 - Results and takeaway

### Headline results

- best average metric-geometry rank: **1.95**
- best sharpness rank: **1.75**
- preserves near-state-of-the-art relative geometry while adding metric scale
- refined real data is the key ingredient for keeping both accuracy and detail

Main takeaway:

**MoGe-2 is a strong single-image geometry model because it predicts metric scale separately and uses synthetic-guided filtering to clean real training labels.**
