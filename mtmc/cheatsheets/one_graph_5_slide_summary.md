# One Graph to Track Them All — 5 Slide Summary

Source paper: One Graph to Track Them All: Dynamic GNNs for Single- and Multi-View Tracking

---

## Slide 1 — Problem & Motivation

### Why one graph?

Most tracking methods are specialized:
- single-view trackers are not naturally multi-view
- multi-view trackers often ignore scene structure
- long scene-induced occlusions remain hard

Real-world challenge:
people disappear not only behind each other, but also behind **walls, columns, and architecture**.

**Core idea**
Use one online graph model that can handle both single-view and multi-view tracking.

---

## Slide 2 — Graph Design

Graph vertices:
- detections
- optional camera vertices

Graph edges:
- **temporal edges** across time
- **view edges** across cameras
- **context edges** between nearby detections
- **camera edges** for scene priors

The graph therefore mixes motion, cross-view, context, and visibility cues.

---

## Slide 3 — Online Pipeline

Pipeline:

detections  
→ build rolling graph  
→ **UMPN** message passing  
→ edge and vertex probabilities  
→ greedy trajectory extraction

Important detail:
training and inference both use a **dynamic rolling window**, not a fixed offline graph.

---

## Slide 4 — Scene Priors & Dataset

### Scene-aware tracking

Camera vertices and edges encode:
- camera position
- line of sight
- visibility to detections
- occlusion from scene mesh

### SCOUT dataset

New benchmark introduced in the paper:
- **25 cameras**
- **564k frames**
- **3k identities**
- scene mesh + calibration
- long, structural occlusions

---

## Slide 5 — Results & Insights

### Results

WildTrack  
MOTA: **93.9**  
IDF1: **96.3**

MOT17 test  
MOTA: **82.2**

MOT20 test  
MOTA: **77.7**

### Main insights

1. A unified graph can work for both single-view and multi-view setups.
2. Scene priors help when occlusions come from the environment.
3. Dynamic graph training avoids heuristic stitching between windows.
4. Graph reasoning is a strong alternative to specialized per-setting trackers.
