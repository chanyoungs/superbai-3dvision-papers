# Depth Anything 3 - Paper Cheat Sheet

Source paper: Depth Anything 3: Recovering the Visual Space from Any Views

---

## Problem

Goal: recover consistent 3D geometry from an arbitrary number of images, with or without known camera poses.

Why this is hard:
- the number of input views can vary from 1 image to long image sets or videos
- some inputs are posed, others are not
- depth labels in real data are noisy, sparse, or incomplete
- prior systems usually specialize in one task, such as monocular depth, SfM, or MVS

---

## Core idea

Depth Anything 3 (DA3) argues that a surprisingly small design is enough:

1. one plain transformer backbone
2. one minimal geometric target: depth + per-pixel ray maps
3. one teacher-student training recipe to unify synthetic and real data

Instead of predicting many overlapping 3D targets, DA3 predicts:
- a dense depth map
- a dense ray map whose origin and direction implicitly encode camera pose

This lets the model recover both scene structure and camera motion while keeping the model simple.

---

## Architecture

### Backbone
- pretrained ViT backbone (DINO / DINOv2 style)
- input-adaptive cross-view self-attention
- same model handles single-view and multi-view inputs

### Representation
- depth map `D(u, v)`
- ray map `r = (t, d)` where `t` is ray origin and `d` is ray direction
- 3D point is recovered as `P = t + D(u, v) * d`

### Heads
- Dual-DPT head predicts depth and ray maps jointly
- lightweight camera head predicts translation, quaternion, and field of view
- optional camera tokens inject known pose when available

### Training recipe
- train a strong monocular teacher on synthetic data
- align teacher predictions to noisy real depth with robust scale-shift fitting
- train DA3 on mixed synthetic + real datasets with depth, ray, point, camera, and gradient losses

---

## Datasets

### Pose + geometry benchmark

| Dataset | Role | What it tests |
|---|---|---|
| HiRoom | synthetic indoor scenes | clean pose + reconstruction benchmark |
| ETH3D | real indoor / outdoor laser scans | multi-view geometry on real scenes |
| DTU | controlled object-centric MVS | precise reconstruction and Chamfer distance |
| 7Scenes | low-resolution RGB-D indoor videos | blur, handheld motion, short-baseline indoor geometry |
| ScanNet++ | high-fidelity indoor scenes | real high-resolution geometry and pose |

The benchmark spans 5 datasets and more than 89 scenes.

### Feed-forward NVS benchmark

| Dataset | Role |
|---|---|
| DL3DV | in-domain large-scale feed-forward NVS benchmark |
| Tanks and Temples | out-of-domain large-scale scene rendering |
| MegaDepth | internet-photo style out-of-domain rendering |

### Training data (representative)

DA3 is trained only on public academic data and mixes synthetic, LiDAR, COLMAP, and reconstruction sources.

Representative datasets include:
- AriaDigitalTwin / AriaSyntheticENV
- ARKitScenes
- BlendedMVS
- Co3Dv2
- DL3DV
- HyperSim
- MapFree
- MegaDepth / MegaSynth
- MvsSynth
- Objaverse / OmniObject / OmniWorld
- PointOdyssey
- ReplicaVMAP
- ScanNet++
- SceneNetRGBD
- TartanAir
- Trellis
- vKITTI2
- WildRGBD

---

## Metrics

### Pose estimation
- AUC@3 and AUC@30
- built from relative rotation accuracy (RRA) and relative translation accuracy (RTA)
- higher is better

### Reconstruction
- accuracy: distance from reconstruction to ground truth
- completeness: distance from ground truth to reconstruction
- Chamfer distance (DTU)
- precision, recall, and F1 at a dataset-specific threshold

### Monocular depth
- `delta1` on standard monocular benchmarks
- higher is better

### Metric depth
- `delta1` and `AbsRel`
- `AbsRel = mean(|z_hat - z| / z)`
- higher `delta1` and lower `AbsRel` are better

### Feed-forward novel view synthesis
- PSNR
- SSIM
- LPIPS

---

## Results

### Pose estimation highlights
- DA3-Giant is best on almost every reported setting
- examples:
  - ScanNet++ AUC@3: **85.0**
  - ETH3D AUC@3: **48.4**
  - DTU AUC@3: **94.1**
- the paper reports an average gain over VGGT of about **35.7% in pose accuracy** on its benchmark

### Reconstruction highlights
- HiRoom F1 (without GT pose): **85.1**
- ETH3D F1 (without GT pose): **79.0**
- DTU Chamfer distance (without GT pose): **1.85 mm**
- the paper reports an average gain over VGGT of about **23.6% in geometric accuracy** on its benchmark

### Monocular depth highlights
- KITTI `delta1`: **95.3**
- NYU `delta1`: **97.4**
- ETH3D `delta1`: **98.6**
- beats DA2 and VGGT on the reported monocular benchmark table

### Metric depth highlights
- ETH3D: **delta1 0.917 / AbsRel 0.104**
- SUN-RGBD: **AbsRel 0.105** (best reported)
- DIODE: **delta1 0.838 / AbsRel 0.128** (competitive second-best setting)

### Feed-forward NVS highlights
- DL3DV: **21.33 PSNR / 0.711 SSIM / 0.241 LPIPS**
- Tanks and Temples: **18.10 / 0.578 / 0.311**
- MegaDepth: **17.89 / 0.561 / 0.351**
- stronger than the compared VGGT backbone on all three NVS benchmarks

---

## Why it matters

- one backbone covers monocular depth, any-view geometry, pose estimation, and feed-forward NVS
- the depth + ray representation shows that a minimal target can outperform larger multi-head task bundles
- geometry quality transfers directly into stronger rendering quality

---

## Caveats

- training is expensive for the largest model
- the benchmark is still centered on mostly static scenes
- the method is strongest when accurate dense geometry is the main goal, not dynamic reasoning

---

## One-sentence takeaway

Depth Anything 3 shows that a single transformer trained to predict depth and ray maps can act as a general any-view geometry foundation model, outperforming prior multi-view geometry systems while still staying simple.
