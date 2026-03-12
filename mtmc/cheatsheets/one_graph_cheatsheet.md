# One Graph to Track Them All — Paper Cheat Sheet

Source: One Graph to Track Them All: Dynamic GNNs for Single- and Multi-View Tracking

---

## Problem

Tracking systems are usually specialized:
- single-view trackers ignore cross-view constraints
- multi-view trackers often cannot transfer back to single-view
- most methods do not model scene structure explicitly

Hard real-world challenge:
long occlusions caused not only by people, but also by **walls, columns, and scene layout**.

---

## Core Idea

Use **one dynamic spatio-temporal graph** for both single-view and multi-view tracking.

The graph connects detections through:
- time
- camera views
- local context
- optional scene priors

A learned message passing network then predicts which vertices and edges belong to the same trajectory.

---

## Pipeline

detections  
→ build rolling spatio-temporal graph  
→ temporal / view / contextual edges  
→ optional camera vertices + camera edges  
→ UMPN message passing  
→ edge and vertex probabilities  
→ online trajectory extraction

---

## Key Components

### 1. Dynamic Graph Construction

The graph is updated online in a rolling temporal window.

It supports:
- single-view tracking
- multi-view tracking
- long-term streaming inference

---

### 2. UMPN

**Unified Message Passing Network**

Updates both edge and vertex features and predicts:
- whether an edge is active
- whether a detection is valid

---

### 3. Scene Priors

Optional camera vertices and camera edges encode:
- camera geometry
- visibility / line of sight
- occlusion from scene structure

This is especially helpful for structural occlusions.

---

### 4. Online Trajectory Extraction

A fast greedy extraction step turns graph probabilities into trajectories while enforcing temporal and spatial consistency.

---

## Key Insight

A single graph can jointly reason over:
- temporal continuity
- cross-view consistency
- local context
- scene structure

This makes the same model useful for both **single-view** and **multi-view** tracking.

---

## Results

WildTrack
MOTA: **93.9**
IDF1: **96.3**

MOT17 test
MOTA: **82.2**
HOTA: **62.5**

MOT20 test
MOTA: **77.7**
HOTA: **62.0**

The paper also introduces **SCOUT**, a new 25-camera dataset with scene mesh information and long structural occlusions.

---

## One-Sentence Takeaway

One Graph to Track Them All unifies single-view, multi-view, and scene-aware tracking by expressing all association cues inside one dynamic graph.
