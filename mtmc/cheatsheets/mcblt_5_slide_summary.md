
# MCBLT — 5 Slide Summary

Source paper: MCBLT: Multi-Camera Multi-Object 3D Tracking in Long Videos

---

## Slide 1 — Problem & Idea

### Multi-Camera Multi-Object Tracking (MTMC)

Goal: Track identities across many cameras and long videos.

**Challenges**
- Cross-camera identity matching
- Severe occlusion
- Appearance changes across views
- Long sequences (10k–20k frames)

**Traditional pipeline**
2D detection → single-camera tracking → cross-camera ReID

**Weakness**
Association errors accumulate across cameras.

**MCBLT idea**
Fuse cameras early and track directly in **3D world space**.

---

## Slide 2 — Core Pipeline

Multi-view images  
→ BEVFormer fusion (multi-view feature aggregation)  
→ 3D object detection  
→ 2D–3D detection association  
→ Multi-view ReID features  
→ Hierarchical GNN tracking  
→ Global long-term association

Key philosophy:

**Track objects in unified 3D coordinates instead of per-camera images.**

---

## Slide 3 — Multi‑View 3D Detection

Uses **BEVFormer**.

Mechanism:
1. Extract image features per camera
2. Project features into BEV grid
3. Aggregate via spatial attention
4. Add temporal attention
5. Predict **3D bounding boxes**

Benefits:
- unified coordinate system
- camera‑invariant detection
- easier cross‑view association

---

## Slide 4 — Graph Tracking

Tracking formulated as a **graph problem**.

Nodes: detections  
Edges: identity hypotheses

Features used:
- 3D geometry distance
- multi-view appearance similarity

Graph Neural Network performs **message passing** to determine which detections belong to the same trajectory.

Hierarchy:
detections → tracklets → long trajectories

---

## Slide 5 — Results & Insights

### Results

AICity’24  
HOTA: **81.22** (state-of-the-art)

WildTrack  
IDF1: **95.6**

### Key insights

1. Track in **3D space**
2. Multi-view appearance improves identity matching
3. Long videos require **global association**
4. Geometry + appearance outperform motion models
