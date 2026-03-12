# MOTIP — 5 Slide Summary

Source paper: Multiple Object Tracking as ID Prediction

---

## Slide 1 — Problem & Motivation

### Why rethink association?

Traditional MOT usually does:
- detection
- hand-crafted trajectory matching

Problems:
- motion heuristics fail on irregular motion
- ReID matching struggles with similar appearance
- tuning many rules is hard

At the same time, joint detection+tracking models can create conflicts between detection and association.

**MOTIP idea**
Keep detection and association decoupled, but make association fully learnable.

---

## Slide 2 — Core Reformulation

### MOT as in-context ID prediction

For each historical trajectory:
- attach a temporary learnable ID token

For each current detection:
- predict which historical ID token it should match

Why this matters:
- avoids fixed global identity classes
- generalizes to unseen trajectories
- turns association into a standard prediction problem

---

## Slide 3 — Architecture

Pipeline:

image  
→ **Deformable DETR**  
→ object embeddings  
→ historical tracklets + learnable ID dictionary  
→ **ID Decoder**  
→ ID label prediction

Components:
- detector
- learnable ID dictionary
- transformer-based ID decoder
- newborn token for new objects

---

## Slide 4 — Training & Inference

Training loss:
- detection loss
- ID prediction loss

Robustness tricks:
- random trajectory occlusion
- random token switch between trajectories

Inference:
- filter detections by confidence
- predict highest-confidence ID
- if no valid old ID, create a newborn trajectory
- recycle IDs from finished tracks when needed

---

## Slide 5 — Results & Insights

### Results

DanceTrack  
HOTA: **69.6** without extra data  
HOTA: **72.0** with extra data

SportsMOT  
HOTA: **72.6**

BFT  
HOTA: **70.5**

### Main insights

1. The formulation itself matters: ID prediction is stronger than heuristic matching.
2. Very simple architectures can work if the task is framed well.
3. Historical trajectory context is enough to drive strong association decisions.
4. MOT labels behave more like prompts than fixed semantic classes.
