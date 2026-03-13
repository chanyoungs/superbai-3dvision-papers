# MoGe-2 - Paper Cheat Sheet

Source paper: MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details

---

## Problem

Goal: recover a metric-scale 3D point map from a single image.

The paper argues that a useful monocular geometry model must do three things at once:
- preserve **relative geometry accuracy**
- predict **metric scale**
- keep **sharp local details**

Why this is hard:
- direct metric point-map prediction is unstable because scene scales vary hugely across images
- real RGB-depth data contains misalignment artifacts, missing regions, and noisy boundaries
- synthetic-only supervision is sharp but usually hurts open-domain realism and accuracy

---

## Core idea

MoGe-2 extends MoGe with two main ideas:

### 1. Decouple geometry from scale
- keep MoGe's affine-invariant point-map prediction branch
- predict one global metric scale separately from the CLS token
- final metric point map is `s_hat * P_hat`

### 2. Refine real training data instead of discarding it
- train a synthetic-only teacher `G_syn`
- use local alignment to filter mismatched depth in real data
- fill removed regions with edge-preserving depth completion
- preserve real metric structure while recovering sharper local detail

---

## Architecture

Pipeline:
input image -> DINOv2 ViT -> shared convolutional neck ->
- affine-invariant point-map head
- mask head
- CLS-token MLP head for global scale

Then:
- metric point map = predicted scale x affine-invariant point map
- metric depth is read from the z-channel of the point map
- camera field of view can be recovered using the MoGe geometry solver

Key design choice from the paper:
- a **decoupled CLS-token MLP** works better than entangled metric point maps or a convolutional scale head

---

## Datasets

### Evaluation datasets

| Dataset | What it tests |
|---|---|
| NYUv2 | indoor metric depth |
| KITTI | outdoor driving geometry |
| ETH3D | real-world metric geometry |
| iBims-1 | indoor geometry + sharp boundaries |
| GSO | object-centric generalization |
| Sintel | synthetic scenes with fine detail |
| DDAD | driving depth |
| DIODE | indoor / outdoor metric depth |
| Spring | high-detail synthetic motion scenes |
| HAMMER | dense geometry quality |

### Which subsets are used for which evaluations?
- relative geometry: all 10 datasets
- metric geometry: 7 datasets with metric scale annotations
- boundary sharpness: iBims-1, HAMMER, Sintel, Spring

### Training data

MoGe-2 uses 24 datasets in total:
- 16 synthetic datasets
- 3 LiDAR datasets
- 5 SfM datasets

Representative training sources:
- A2D2, Argoverse2, Waymo
- ARKitScenes, ScanNet++, Taskonomy
- BlendedMVS, MegaDepth
- ApolloSynthetic, Hypersim, IRS, MatrixCity, MidAir, Structured3D, Synscapes, TartanAir, UnrealStereo4K, UrbanSyn
- ObjaverseV1

---

## Metrics

### Relative geometry
The paper evaluates point maps and depth under several alignment settings.

Common point-map error:
- `Rel_p = ||p_hat - p||_2 / ||p||_2`
- `delta1^p`: percent of pixels with point error below threshold

Common depth error:
- `Rel_d = |z_hat - z| / z`
- `delta1^d`: percent of pixels where `max(z_hat / z, z / z_hat) < 1.25`

Alignment variants:
- scale-invariant
- affine-invariant
- local point-map alignment
- affine-invariant disparity

### Metric geometry
- metric point-map `Rel_p` and `delta1^p`
- metric depth `Rel_d` and `delta1^d`
- also reported with ground-truth camera intrinsics for methods that can use them

### Boundary sharpness
- boundary F1 score on high-quality dense geometry datasets
- higher is better

---

## Results

### Relative geometry
- average rank across the 10-dataset benchmark: **2.05**
- better average ranking than UniDepth V2 (**2.88**) and Depth Pro (**4.52**)
- very close to MoGe while adding metric-scale prediction
- strongest reported local point-map setting: **Rel_p 5.33 / delta1 95.9**

### Metric geometry
- best average rank across the 7-dataset metric benchmark: **1.95**
- metric point map: **Rel_p 8.19 / delta1 93.6**
- metric depth: **Rel_d 15.7 / delta1 76.8**
- metric depth with GT camera intrinsics: **Rel_p 13.6 / delta1 87.4**

### Boundary sharpness
- average sharpness rank: **1.75**
- iBims-1 F1: **17.9**
- HAMMER F1: **5.42**
- competitive with Depth Pro on sharpness while clearly stronger in geometry accuracy

### Key ablations
- decoupled CLS-token scale prediction is best overall
- synthetic-only training is sharper but much less accurate
- refined real data keeps almost all metric accuracy of raw real data while recovering much more detail

---

## Why it matters

- preserves MoGe's strong relative geometry while adding useful metric scale
- shows that **real data refinement** is better than simply dropping noisy real labels
- useful for robotics, AR/VR, 3D editing, and scene understanding where both scale and detail matter

---

## Limitations

The paper notes three main weaknesses:
- extremely fine structures such as thin lines and hair remain difficult
- large foreground/background scale differences can bend or misalign straight structures
- metric scale can drift on out-of-distribution scenes with weak real-world priors

---

## One-sentence takeaway

MoGe-2 turns monocular geometry into a practical metric 3D point-map problem by decoupling global scale from affine-invariant geometry and by cleaning real depth supervision instead of throwing it away.
