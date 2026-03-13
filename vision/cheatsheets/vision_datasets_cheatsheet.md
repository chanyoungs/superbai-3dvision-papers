# Vision Datasets - Cheat Sheet

Scope: datasets appearing across Depth Anything 3, MoGe-2, and VGGT

---

## Why datasets matter here

These three papers are not evaluated on one shared benchmark.

Instead, each paper chooses datasets that match a different claim:
- single-image metric geometry
- any-view pose and reconstruction
- multi-view reconstruction, matching, and tracking

So the first rule is:

**always compare results inside the same task family before comparing papers.**

---

## Benchmark families

| Family | Representative datasets | Used by | What it tests |
|---|---|---|---|
| single-image metric geometry | NYUv2, KITTI, ETH3D, iBims-1, GSO, Sintel, DDAD, DIODE, Spring, HAMMER | MoGe-2, DA3 metric / monocular variants | metric depth, relative geometry, sharpness |
| any-view pose + reconstruction | HiRoom, ETH3D, DTU, 7Scenes, ScanNet++ | Depth Anything 3 | posed and unposed multi-view geometry |
| camera pose generalization | RealEstate10K, Co3Dv2, IMC | VGGT | camera estimation on real scenes and phototourism |
| feed-forward novel view synthesis | DL3DV, Tanks and Temples, MegaDepth, GSO | Depth Anything 3, VGGT downstream | rendering quality from sparse views |
| matching / tracking | ScanNet-1500, TAP-Vid | VGGT | two-view matching and dense point tracking |

---

## Depth Anything 3 datasets

### Core evaluation benchmark
- HiRoom
- ETH3D
- DTU
- 7Scenes
- ScanNet++

### Rendering benchmark
- DL3DV
- Tanks and Temples
- MegaDepth

### Training mix
DA3 mixes public synthetic, LiDAR, and SfM / COLMAP datasets, such as:
- ARKitScenes
- Co3Dv2
- DL3DV
- MegaDepth
- ScanNet++
- HyperSim
- Objaverse
- TartanAir
- SceneNetRGBD
- WildRGBD

Its training story is about **coverage across view count and geometry source type**.

---

## MoGe-2 datasets

### Evaluation focus
MoGe-2 uses 10 datasets to stress three things:
- relative geometry
- metric scale
- detail sharpness

Key benchmarks:
- NYUv2, KITTI, ETH3D, DIODE for metric depth
- iBims-1 and HAMMER for dense real-world geometry
- Sintel and Spring for boundary sharpness
- GSO for object-centric generalization

### Training mix
24 datasets total:
- synthetic worlds: Hypersim, IRS, MatrixCity, MidAir, Structured3D, Synscapes, TartanAir, UnrealStereo4K, UrbanSyn, ObjaverseV1
- LiDAR / real: A2D2, Argoverse2, Waymo
- SfM / RGB-D: ARKitScenes, MegaDepth, BlendedMVS, ScanNet++, Taskonomy

Its dataset story is about **single-view generalization plus better supervision quality**.

---

## VGGT datasets

### Evaluation focus
VGGT evaluates across many downstream tasks instead of one benchmark family:
- camera pose: RealEstate10K, Co3Dv2, IMC
- dense MVS: DTU
- point maps: ETH3D
- matching: ScanNet-1500
- NVS: GSO
- dynamic point tracking: TAP-Vid

### Training mix
Representative sources:
- Co3Dv2, DL3DV, MegaDepth, BlendedMVS
- ScanNet, HyperSim, Habitat, Replica
- Kubric, PointOdyssey, Virtual KITTI
- Aria Synthetic Environments, Aria Digital Twin
- WildRGB and artist-created 3D assets

Its dataset story is about **breadth across multi-view, reconstruction, and tracking tasks**.

---

## Practical reading guide

- If the paper talks about **metric single-image geometry**, look first at the MoGe-2 benchmark family.
- If the paper talks about **unposed multi-view geometry**, look first at DA3's 5-dataset benchmark.
- If the paper talks about **feed-forward multi-view cameras + tracks**, look first at VGGT's cross-task evaluation.

---

## One-sentence takeaway

Across these three papers, dataset choice is not a detail - it is the clearest indicator of whether the model is meant for single-image metric geometry, any-view reconstruction, or general multi-view 3D understanding.
