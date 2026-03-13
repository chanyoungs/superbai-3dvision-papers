# VGGT - 5 Slide Summary

Source paper: VGGT: Visual Geometry Grounded Transformer

---

## Slide 1 - Problem and promise

### One feed-forward network for many 3D tasks

Goal: reconstruct a scene from one to hundreds of images and output:
- camera poses
- depth maps
- point maps
- point tracks

Key claim:
VGGT often beats methods that still depend on costly post-processing.

---

## Slide 2 - Architecture

### Alternating-attention transformer

Pipeline:
images -> DINO patch tokens + camera tokens -> alternating frame-wise and global self-attention ->
- camera head
- DPT head for depth and point maps
- tracking head

Key design choice:
- minimal explicit 3D bias
- let scale come from large data and multi-task supervision

---

## Slide 3 - Datasets

### Broad multi-task evaluation

Training data spans many public 3D datasets such as:
- Co3Dv2
- DL3DV
- MegaDepth
- ScanNet
- HyperSim
- Habitat / Replica
- Kubric
- PointOdyssey
- Aria datasets

Evaluation covers:
- RealEstate10K, Co3Dv2, IMC
- DTU, ETH3D
- ScanNet-1500
- GSO
- TAP-Vid

---

## Slide 4 - Metrics

### What is measured

Camera pose:
- AUC@30 or AUC@3/5/10

Geometry:
- Accuracy
- Completeness
- Overall / Chamfer-style score

Rendering:
- PSNR, SSIM, LPIPS

Tracking:
- AJ, `delta_vis_avg`, OA

---

## Slide 5 - Results and takeaway

### Headline results

- Re10K AUC@30: **85.3** feed-forward, **93.5** with BA
- Co3Dv2 AUC@30: **88.2** feed-forward
- DTU overall: **0.382** without GT cameras
- ETH3D overall: **0.677**
- ScanNet-1500 matching outperforms Roma
- VGGT features improve CoTracker on TAP-Vid

Main takeaway:

**VGGT turns multi-view 3D reconstruction into a large multi-task transformer backbone that can also seed downstream tracking and rendering models.**
