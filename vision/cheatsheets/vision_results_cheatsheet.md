# Vision Results - Cheat Sheet

Scope: main results across Depth Anything 3, MoGe-2, and VGGT where comparison is meaningful

---

## First rule - compare inside task families

These papers are not one shared leaderboard.

The cleanest reading is:
1. compare DA3 and VGGT on multi-view geometry where they overlap
2. read MoGe-2 as the strongest single-image metric geometry paper in this set
3. treat NVS and tracking results as downstream evidence for geometry quality

---

## Direct overlap - DA3 vs VGGT on multi-view geometry

| Benchmark | Metric | VGGT | DA3 | Readout |
|---|---|---:|---:|---|
| ETH3D pose | AUC@3 | 26.3 | **48.4** | DA3 is much stronger |
| ScanNet++ pose | AUC@3 | 62.6 | **85.0** | DA3 clearly wins |
| HiRoom reconstruction | F1 w/o GT pose | 56.7 | **85.1** | huge DA3 gain |
| ETH3D reconstruction | F1 w/o GT pose | 57.2 | **79.0** | DA3 clearly wins |
| DTU reconstruction | CD w/o GT pose | 2.05 | **1.85** | DA3 is better (lower is better) |
| DL3DV NVS backbone | PSNR | 20.96 | **21.33** | DA3 is the stronger NVS backbone |

The paper summary for DA3 reports average improvements over VGGT of about:
- **35.7%** in pose accuracy
- **23.6%** in geometric accuracy

---

## Single-image metric geometry - MoGe-2's position

MoGe-2 is the strongest single-image metric geometry paper in this three-paper set.

Headline evidence:
- best average rank on the 7-dataset metric geometry benchmark: **1.95**
- best sharpness rank: **1.75**
- preserves near-state-of-the-art relative geometry while adding metric scale

Representative reported numbers:
- metric point map: **Rel_p 8.19 / delta1 93.6**
- metric depth: **Rel_d 15.7 / delta1 76.8**
- with GT camera intrinsics: **13.6 / 87.4**

Important note:
- DA3 also has strong monocular and metric depth branches, but the exact evaluation protocol is not identical to MoGe-2's point-map setup, so read them as adjacent evidence, not a strict one-line leaderboard.

---

## DA3's monocular and metric depth evidence

DA3 is not only a multi-view model.
It also reports strong single-image depth variants.

Highlights:
- monocular depth `delta1`:
  - KITTI **95.3**
  - NYU **97.4**
  - ETH3D **98.6**
- metric depth:
  - ETH3D **delta1 0.917 / AbsRel 0.104**
  - SUN-RGBD **AbsRel 0.105**
  - DIODE **delta1 0.838 / AbsRel 0.128**

Readout:
- DA3 is the strongest evidence in this set that a general any-view backbone can still produce competitive monocular depth variants.

---

## VGGT's multi-task and downstream evidence

VGGT's value is breadth.

### Camera pose
- Re10K AUC@30: **85.3** feed-forward
- Co3Dv2 AUC@30: **88.2** feed-forward
- IMC with BA: **66.37 / 75.16 / 84.91** for AUC@3 / @5 / @10

### Reconstruction
- DTU overall: **0.382** without GT cameras
- ETH3D overall: **0.677** using depth + camera heads

### Matching / tracking / NVS
- ScanNet-1500 matching beats Roma in AUC
- CoTracker + VGGT features improves TAP-Vid tracking over vanilla CoTracker
- GSO NVS: **30.41 PSNR / 0.949 SSIM / 0.033 LPIPS** without known input cameras

Readout:
- VGGT is the most obviously reusable general multi-view 3D backbone in the set.

---

## Synthesis

### Best evidence by role
- **single-image metric geometry** -> MoGe-2
- **any-view pose + reconstruction** -> Depth Anything 3
- **fast multi-view cameras + points + tracks** -> VGGT

### Overall pattern
As the models get more general, performance no longer comes from one handcrafted geometry solver.
It comes from:
- large transformer backbones
- large mixed 3D datasets
- carefully chosen multi-task or decoupled outputs

---

## One-sentence takeaway

The results across these papers support a clean division of labor: MoGe-2 is strongest for single-image metric geometry, DA3 is strongest for any-view geometry, and VGGT is strongest as a broad feed-forward multi-view 3D backbone.
