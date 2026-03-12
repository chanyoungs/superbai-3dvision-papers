
# MCBLT — Paper Cheat Sheet

Source paper: MCBLT: Multi-Camera Multi-Object 3D Tracking in Long Videos

---

## Problem

Multi-Camera Multi-Object Tracking (MTMC)

Goal: Track identities across cameras and long videos.

Key difficulties:
- occlusion across cameras
- viewpoint changes
- long sequences (10k–20k frames)
- unreliable cross-camera ReID

Traditional pipeline:

per-camera detection  
→ single-camera tracking  
→ cross-camera association

Weakness: association errors accumulate.

---

## Core Idea

Fuse cameras early and track in **3D space**.

Pipeline:

multi-view images  
→ BEV fusion  
→ 3D detection  
→ graph tracking

Benefits:
- consistent geometry
- simpler association
- better occlusion handling

---

## Pipeline

Multi-view images  
→ BEVFormer fusion  
→ 3D detection  
→ 2D–3D detection association  
→ multi-view ReID features  
→ hierarchical GNN tracking  
→ global association

---

## Key Components

### 1. BEV Multi-View Detection

Project camera features into BEV grid and detect objects in 3D.

Output:
3D bounding boxes.

---

### 2. 2D–3D ReID Association

3D detection projected to cameras  
→ matched with 2D detections  
→ clean object crops used for ReID.

Improves appearance features.

---

### 3. Graph Tracking

Nodes: detections  
Edges: identity relationships

Features:
- 3D geometry distance
- appearance similarity

GNN learns associations across frames.

---

### 4. Global Tracking Layer

Standard trackers use sliding windows.

MCBLT adds global association to:
- reconnect tracks
- recover long occlusions (~2000 frames).

---

## Key Insight

For multi-camera tracking:

**3D geometry + multi-view appearance are stronger cues than motion models.**

---

## Results

AICity’24

HOTA: 81.22  
DetA: 86.94  
AssA: 76.19

WildTrack

IDF1: 95.6

Major improvement in **identity consistency**.

---

## One-Sentence Takeaway

MCBLT solves multi-camera tracking by fusing cameras into a unified BEV 3D representation and associating identities using hierarchical graph neural networks.
