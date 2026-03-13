# VGGT - Paper Cheat Sheet

Source paper: VGGT: Visual Geometry Grounded Transformer

---

## Problem

Goal: given one, a few, or even hundreds of images of the same scene, predict all key 3D scene attributes in one feed-forward pass.

Outputs:
- camera intrinsics and extrinsics
- depth maps
- point maps
- dense tracking features for point tracking

Why this matters:
- classic SfM / MVS pipelines are accurate but slow and optimization-heavy
- many learned methods still work only on image pairs and need expensive post-alignment
- a general 3D backbone should be usable across reconstruction, matching, tracking, and rendering

---

## Core idea

VGGT asks: can a large transformer replace most of the geometry pipeline?

Key answer:
- yes, if trained on enough public 3D-annotated data and asked to predict multiple related 3D targets at once

Main design principles:
- minimal explicit 3D inductive bias
- one shared transformer backbone
- alternating frame-wise and global self-attention
- separate camera head and DPT heads for dense outputs
- tracking head on top of learned dense features

---

## Architecture

Pipeline:
input images -> DINO patch tokens + camera tokens -> alternating-attention transformer ->
- camera head for extrinsics + intrinsics
- DPT head for depth maps, point maps, and dense tracking features
- CoTracker-style tracking head for query-point correspondences

Important details:
- the first frame defines the world coordinate system
- the model is permutation-equivariant for all non-reference frames
- multi-task training supervises cameras, depth, point maps, and tracks jointly

---

## Datasets

### Training data (representative)
- Co3Dv2
- BlendedMVS
- DL3DV
- MegaDepth
- Kubric
- WildRGB
- ScanNet
- HyperSim
- Mapillary
- Habitat
- Replica
- MVS-Synth
- PointOdyssey
- Virtual KITTI
- Aria Synthetic Environments
- Aria Digital Twin
- artist-created synthetic 3D asset dataset

### Evaluation benchmarks

| Task | Datasets |
|---|---|
| camera pose | RealEstate10K, Co3Dv2, IMC |
| dense MVS | DTU |
| point-map estimation | ETH3D |
| image matching | ScanNet-1500 |
| novel view synthesis | GSO |
| dynamic point tracking | TAP-Vid (Kinetics, RGB-S, DAVIS) |

---

## Metrics

### Camera pose
- AUC@30 on RealEstate10K and Co3Dv2
- AUC@3 / AUC@5 / AUC@10 on IMC
- higher is better

### Dense reconstruction
- Accuracy
- Completeness
- Overall = mean / Chamfer-style summary
- lower is better

### Image matching
- relative pose accuracy AUC@5 / AUC@10 / AUC@20
- higher is better

### Novel view synthesis
- PSNR
- SSIM
- LPIPS

### Dynamic point tracking
- AJ (average Jaccard)
- `delta_vis_avg`
- OA (occlusion accuracy)

---

## Results

### Camera pose
- feed-forward only:
  - RealEstate10K AUC@30: **85.3**
  - Co3Dv2 AUC@30: **88.2**
- with bundle adjustment:
  - RealEstate10K: **93.5**
  - Co3Dv2: **91.8**
- on IMC with BA: **66.37 / 75.16 / 84.91** for AUC@3 / @5 / @10, beating VGGSfM v2

### Dense MVS / point maps
- DTU overall score without ground-truth cameras: **0.382**
- ETH3D overall score using depth + camera heads: **0.677**
- both clearly better than DUSt3R / MASt3R in the reported tables

### Matching and tracking
- ScanNet-1500 matching: **33.9 / 55.2 / 73.4** for AUC@5 / @10 / @20
- TAP-Vid finetuned tracker (CoTracker + Ours) improves over vanilla CoTracker across Kinetics, RGB-S, and DAVIS

### Novel view synthesis
- GSO: **30.41 PSNR / 0.949 SSIM / 0.033 LPIPS**
- competitive even without known input camera parameters

### Key ablations
- alternating-attention is better than global-only or cross-attention variants
- multi-task learning improves point-map accuracy compared with training without camera, depth, or tracking losses

---

## Why it matters

- a single feed-forward model can now cover cameras, geometry, matching, and tracking
- predictions are directly usable before optimization, which is the real practical shift
- the learned features transfer well to downstream NVS and dynamic tracking

---

## Limitations

The paper explicitly notes:
- no support for fisheye or panoramic imagery yet
- performance drops for extreme input rotations
- large non-rigid deformations remain difficult

---

## One-sentence takeaway

VGGT is a general-purpose multi-view transformer that predicts cameras, depth, point maps, and tracking features in one fast feed-forward pass, reducing the need for classical test-time geometry optimization.
