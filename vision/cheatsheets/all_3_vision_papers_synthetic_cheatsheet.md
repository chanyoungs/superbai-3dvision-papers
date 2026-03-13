# All 3 Vision Papers - Synthetic Cheat Sheet

Scope: Depth Anything 3, MoGe-2, and VGGT

---

## The big picture

These three papers attack different slices of the same 3D-vision stack.

- **MoGe-2**: single-image metric geometry with sharp details
- **Depth Anything 3**: any-view geometry from one to many images, posed or unposed
- **VGGT**: multi-view scene understanding with cameras, depth, point maps, and tracks

Together they show a clear trend:

**3D vision is moving toward large transformer backbones trained on heterogeneous public 3D data, with geometry treated as a reusable foundation capability.**

---

## Comparison table

| Paper | Input regime | Core representation | Main outputs | Best fit |
|---|---|---|---|---|
| MoGe-2 | 1 image | affine-invariant point map + global scale | metric point map, depth, mask | single-image metric geometry |
| Depth Anything 3 | 1 to many images, posed or unposed | depth + ray maps | pose, depth, geometry, NVS backbone | any-view geometry |
| VGGT | 1 to hundreds of images | alternating-attention transformer with multi-task heads | cameras, depth, point maps, tracks | fast multi-view reconstruction and tracking |

---

## Shared design themes

### 1. Minimal inductive bias
All three papers rely on strong pretrained vision transformers instead of highly handcrafted 3D pipelines.

### 2. Geometry as a reusable representation
- MoGe-2: metric point map
- DA3: depth + ray map
- VGGT: joint cameras + depth + point maps + tracks

### 3. Large heterogeneous training corpora
All three papers mix synthetic and real 3D supervision rather than staying inside one benchmark family.

### 4. Multi-task or decoupled prediction heads
- MoGe-2 decouples global scale from geometry
- DA3 predicts depth and rays jointly, plus an optional camera head
- VGGT predicts cameras, depth, points, and tracks jointly

---

## What each paper is really best at

### MoGe-2
Use when the input is a single image and metric scale plus detail matter.

### Depth Anything 3
Use when the number of views is variable and you want one backbone for monocular depth, pose-free geometry, and downstream NVS.

### VGGT
Use when you need one fast multi-view model that predicts cameras and geometry directly and also transfers to tracking.

---

## How they fit together for a 3D team

A practical way to present them is as a ladder:

1. **single-view geometry** -> MoGe-2
2. **any-view geometry** -> Depth Anything 3
3. **multi-view geometry + tracks** -> VGGT

This also reflects increasing input richness and increasing scene-level reasoning.

---

## One-sentence takeaway

MoGe-2, Depth Anything 3, and VGGT are best read as complementary foundation-style models for single-view, any-view, and multi-view 3D perception rather than as one direct leaderboard race.
