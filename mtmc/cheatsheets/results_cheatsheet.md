# Results — Cheat Sheet Across the Five Papers

Scope: datasets, models, and metric results across CAMELTrack, MOTIP, ReST, MCBLT, and One Graph where overlap exists

---

## First Rule: Compare Within the Same Benchmark

These papers do **not** all evaluate on the same datasets.

Also, some results differ in:
- detector choice
- extra training data
- 2D vs ground-plane vs 3D evaluation space

So the fairest reading is:
1. compare within a dataset first,
2. then compare design choices across datasets.

---

## Direct Overlap 1 — DanceTrack

| Model | HOTA | AssA | IDF1 | MOTA | Notes |
|---|---:|---:|---:|---:|---|
| CAMELTrack | 66.1 | 54.0 | 71.1 | 91.4 | default model |
| CAMELTrack + keypoints | 69.3 | 58.9 | 74.9 | 91.4 | best CAMELTrack variant |
| MOTIP | 69.6 | 60.4 | 74.7 | 90.6 | no extra data |
| MOTIP + extra data | 72.0 | 63.5 | 76.8 | 91.9 | not apples-to-apples |

### Readout
- CAMELTrack and MOTIP are both very strong on hard association.
- MOTIP has the stronger DanceTrack result overall.

---

## Direct Overlap 2 — SportsMOT

| Model | HOTA | AssA | IDF1 | MOTA | Notes |
|---|---:|---:|---:|---:|---|
| CAMELTrack | 80.4 | 72.8 | 84.8 | 96.3 | best HOTA |
| CAMELTrack + keypoints | 80.3 | 72.6 | 84.8 | 96.4 | keypoints do not help here |
| MOTIP | 72.6 | 63.2 | 77.1 | 92.4 | no extra data |

### Readout
- CAMELTrack is much stronger than MOTIP on SportsMOT.
- This suggests CAMELTrack benefits more from strong modular cues in sports scenes.

---

## Direct Overlap 3 — MOT17 / MOT20

| Model | Dataset | HOTA | IDF1 | MOTA | Notes |
|---|---|---:|---:|---:|---|
| CAMELTrack | MOT17 test | 62.4 | 76.5 | 78.5 | online learned association |
| One Graph | MOT17 test | 62.5 | 75.1 | 82.2 | graph without explicit appearance cues |
| One Graph | MOT20 test | 62.0 | 75.2 | 77.7 | dense crowd benchmark |

### Readout
- CAMELTrack and One Graph are very close in HOTA on MOT17.
- One Graph has higher MOTA; CAMELTrack has slightly higher IDF1.

---

## Direct Overlap 4 — WildTrack

| Model | IDF1 | MOTA | MOTP | Notes |
|---|---:|---:|---:|---|
| ReST | 85.7 | 81.6 | 81.8 | 2-stage spatial/temporal graph |
| MCBLT | 93.4 | 87.5 | 94.3 | own BEVFormer detections |
| MCBLT† | 95.6 | 92.6 | 93.7 | uses shared detections |
| One Graph | 96.3 | 93.9 | 86.9 | unified dynamic graph |

### Readout
- ReST is clearly improved upon by later models.
- MCBLT and One Graph are the strongest WildTrack performers.
- One Graph has the top WildTrack MOTA/IDF1 in this set, while MCBLT is also extremely strong and more explicitly 3D-first.

---

## Unique Benchmark Highlights

### CAMELTrack
- PoseTrack21: HOTA **66.0**, IDF1 **76.0**
- BEE24: HOTA **50.3**, IDF1 **63.8**

### MOTIP
- BFT: HOTA **70.5**, AssA **71.8**, IDF1 **82.1**

### ReST
- CAMPUS: MOTA **77.6 / 86.0 / 77.7 / 81.2** across sequences
- PETS-09 S2.L1: MOTA **92.3**, MOTP **99.7**

### MCBLT
- AICity’24: HOTA **81.22**, DetA **86.94**, AssA **76.19**, LocA **95.67**

### One Graph
- SCOUT single-view: MOTA **69.8**, IDF1 **62.1**, HOTA **63.3**
- SCOUT single-view + scene priors: MOTA **73.6**, IDF1 **63.3**, HOTA **64.8**

---

## What the Results Say

### CAMELTrack
Best when strong modular cues are available and association is the bottleneck.

### MOTIP
Best illustration that a new **association formulation** alone can beat heuristic matching on hard 2D MOT.

### ReST
Important step for multi-camera graph association, but now outperformed by stronger geometry / graph designs.

### MCBLT
Best blueprint for **3D MTMC with long videos** and calibrated static camera rigs.

### One Graph
Best demonstration of a **unified graph** that covers both single-view and multi-view tracking, especially when scene priors are available.

---

## One-Sentence Takeaway

The results support a clear pattern: **as methods move from heuristic matching toward learned association with stronger geometry and better long-term memory, identity tracking becomes substantially more reliable.**
