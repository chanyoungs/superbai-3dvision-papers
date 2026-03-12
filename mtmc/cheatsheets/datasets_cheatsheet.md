# Datasets — Cheat Sheet

Scope: datasets appearing across the five papers

---

## Why the datasets matter

The papers do **not** evaluate on the same benchmark family.

Some datasets test:
- single-view association
- multi-camera association
- long-video identity recovery
- 3D / ground-plane reasoning
- structural occlusions from scene geometry

So the dataset choice strongly shapes what each paper is proving.

---

## Single-View 2D MOT Datasets

| Dataset | What is in it | Main challenge | Used by |
|---|---|---|---|
| DanceTrack | 100 videos of group dances | uniform appearance + diverse motion + frequent occlusion | CAMELTrack, MOTIP |
| SportsMOT | 240 sports broadcast videos | similar uniforms, camera motion, re-entry, team sports dynamics | CAMELTrack, MOTIP |
| MOT17 | classic pedestrian benchmark | crowded street scenes, benchmark legacy, mixed detector settings | CAMELTrack, One Graph |
| MOT20 | dense-crowd pedestrian benchmark | extreme crowd density and identity ambiguity | One Graph |
| BFT | 106 clips from 22 bird species | highly dynamic motion, similar appearance, non-human tracking | MOTIP |
| PoseTrack21 | person / pose tracking benchmark | articulated motion and pose-aware identity tracking | CAMELTrack |
| BEE24 | bee tracking benchmark | long sequences, hard re-ID, tiny fast-moving objects | CAMELTrack |

---

## Multi-View / MTMC Datasets

| Dataset | What is in it | Main challenge | Used by |
|---|---|---|---|
| WildTrack | 7 synchronized cameras over a shared outdoor space | cross-view association, occlusion, ground-plane localization | ReST, MCBLT, One Graph |
| CAMPUS | multiple classic multi-camera sequences | varying overlap, sparse scenes, view-to-view matching | ReST |
| PETS-09 | classic surveillance MTMC sequence | lower video quality, legacy benchmark, cross-view tracking | ReST |

---

## Large-Scale 3D / Scene-Aware Datasets

| Dataset | What is in it | Main challenge | Used by |
|---|---|---|---|
| AICity’24 | 90 synthetic indoor scenes, 953 cameras total, 3D boxes, long sequences up to 24k frames | long-term MTMC, severe occlusion, 3D location tracking | MCBLT |
| SCOUT | 25 partially overlapping cameras, 564k frames, 3k IDs, scene mesh + calibration | structural occlusions from walls / columns, unified single+multi-view tracking | One Graph |

---

## What Each Dataset Really Tests

### Best for single-view association
- DanceTrack
- SportsMOT
- MOT17 / MOT20
- BFT

### Best for overlapping multi-camera tracking
- WildTrack
- CAMPUS
- PETS-09

### Best for long videos + geometry + scene priors
- AICity’24
- SCOUT

### Best for transfer beyond standard pedestrian MOT
- PoseTrack21
- BEE24
- BFT

---

## Practical Reading Guide

- **DanceTrack / SportsMOT** tell you whether the association head is strong.
- **WildTrack** tells you whether cross-view reasoning works.
- **AICity’24** tells you whether the method can survive long-term MTMC.
- **SCOUT** tells you whether the tracker can use actual scene structure.

---

## One-Sentence Takeaway

Across these papers, datasets evolve from **2D single-view association benchmarks** to **geometry-rich, long-horizon multi-camera benchmarks** that increasingly reward 3D and scene-aware reasoning.
