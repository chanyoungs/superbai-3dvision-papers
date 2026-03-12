# Datasets — 5 Slide Summary

Scope: datasets used across CAMELTrack, MOTIP, ReST, MCBLT, and One Graph

---

## Slide 1 — Why Dataset Choice Matters

These papers do not test exactly the same problem.

Different datasets emphasize different skills:
- single-view association
- cross-view association
- long-term occlusion recovery
- 3D localization
- scene-aware tracking

So the dataset is part of the method story.

---

## Slide 2 — Single-View MOT Datasets

Main datasets:
- **DanceTrack** → uniform appearance, diverse motion
- **SportsMOT** → sports players, camera motion, re-entry
- **MOT17 / MOT20** → classic pedestrian benchmarks
- **BFT** → highly dynamic bird tracking
- **PoseTrack21 / BEE24** → pose and non-human transfer cases

Used mostly by:
- CAMELTrack
- MOTIP
- One Graph

---

## Slide 3 — Classic Multi-Camera Datasets

Main datasets:
- **WildTrack** → 7 calibrated overlapping cameras
- **CAMPUS** → multiple classic multi-view scenes
- **PETS-09** → legacy surveillance MTMC benchmark

What they test:
- cross-view identity association
- calibration-aware tracking
- robustness to occlusion across cameras

Used mostly by:
- ReST
- MCBLT
- One Graph

---

## Slide 4 — Large-Scale 3D / Scene-Aware Datasets

### AICity’24
- synthetic indoor MTMC benchmark
- 90 scenes
- 953 cameras total
- sequences up to 24k frames
- 3D boxes and long occlusions

### SCOUT
- 25 cameras
- 564k frames
- 3k identities
- scene mesh + calibration
- structural occlusion focus

These datasets reward explicit geometry and long-term reasoning.

---

## Slide 5 — What Each Dataset Tells Us

### Best for association quality
- DanceTrack
- SportsMOT

### Best for cross-view MTMC
- WildTrack
- CAMPUS
- PETS-09

### Best for 3D / scene-aware long-term tracking
- AICity’24
- SCOUT

### Main takeaway

Dataset choice reveals whether a paper is mainly about:
- better matching in 2D,
- better cross-view reasoning,
- or better geometry-aware long-horizon tracking.
