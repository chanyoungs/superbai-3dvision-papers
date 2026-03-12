# Results — 5 Slide Summary

Scope: cross-paper results view for CAMELTrack, MOTIP, ReST, MCBLT, and One Graph

---

## Slide 1 — How to Read the Results

These papers are not all solving the exact same benchmark problem.

So compare in this order:
1. same dataset
2. same metric family
3. same detection / training setting if possible

Best practice:
use raw numbers to compare **within benchmark**, and use method design to compare **across benchmarks**.

---

## Slide 2 — Single-View Benchmarks

### DanceTrack
- CAMELTrack + keypoints: **69.3 HOTA**
- MOTIP: **69.6 HOTA** without extra data
- MOTIP + extra data: **72.0 HOTA**

### SportsMOT
- CAMELTrack: **80.4 HOTA**
- MOTIP: **72.6 HOTA**

### Takeaway
- MOTIP is strongest on DanceTrack.
- CAMELTrack is strongest on SportsMOT.

---

## Slide 3 — Multi-Camera Benchmarks

### WildTrack
- ReST: **85.7 IDF1 / 81.6 MOTA**
- MCBLT: **93.4 IDF1 / 87.5 MOTA**
- MCBLT†: **95.6 IDF1 / 92.6 MOTA**
- One Graph: **96.3 IDF1 / 93.9 MOTA**

### AICity’24
- MCBLT: **81.22 HOTA**

### Takeaway
- ReST is an important earlier graph baseline.
- MCBLT and One Graph are the strongest later MTMC systems here.

---

## Slide 4 — Paper-Specific Strengths

- **CAMELTrack** → learned multi-cue association with modular off-the-shelf cues
- **MOTIP** → strongest conceptual reformulation of association as ID prediction
- **ReST** → clean spatial-then-temporal graph decomposition
- **MCBLT** → strongest 3D long-video MTMC story
- **One Graph** → strongest unified single-view + multi-view graph story

---

## Slide 5 — Practical Takeaways for Our Team

### If we care most about 3D MTMC
look first at:
- **MCBLT**
- **One Graph**
- then **ReST** as a lighter graph baseline

### If we care about association heads we can reuse
borrow ideas from:
- **CAMELTrack**
- **MOTIP**

### Final takeaway

The strongest results come from methods that combine:
- learned association,
- explicit geometry,
- and a mechanism for long-term recovery.
