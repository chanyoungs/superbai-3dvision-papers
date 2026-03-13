# Vision Datasets - 5 Slide Summary

Scope: datasets across Depth Anything 3, MoGe-2, and VGGT

---

## Slide 1 - Why dataset choice matters

These papers do not share one benchmark.

Instead, each paper uses datasets to support a different claim:
- MoGe-2: single-image metric geometry
- DA3: any-view pose + reconstruction
- VGGT: general multi-view 3D + tracking

---

## Slide 2 - Depth Anything 3 datasets

Evaluation:
- HiRoom
- ETH3D
- DTU
- 7Scenes
- ScanNet++

Rendering benchmark:
- DL3DV
- Tanks and Temples
- MegaDepth

Training mix:
- public synthetic + LiDAR + SfM / COLMAP datasets

---

## Slide 3 - MoGe-2 datasets

Evaluation:
- NYUv2, KITTI, ETH3D, iBims-1, GSO, Sintel, DDAD, DIODE, Spring, HAMMER

Training:
- 24 datasets total
- synthetic + LiDAR + SfM

Main purpose:
- stress relative geometry, metric scale, and boundary sharpness from one image

---

## Slide 4 - VGGT datasets

Evaluation:
- RealEstate10K, Co3Dv2, IMC
- DTU, ETH3D
- ScanNet-1500
- GSO
- TAP-Vid

Training:
- broad 3D-annotated public data for reconstruction and tracking

Main purpose:
- show one feed-forward backbone can support many 3D tasks

---

## Slide 5 - Takeaway

How to read the datasets:
- MoGe-2 = single-view metric geometry
- DA3 = any-view geometry and rendering
- VGGT = multi-view scene reconstruction, matching, and tracks

Main takeaway:

**Dataset choice is the easiest way to understand what each paper is actually trying to prove.**
