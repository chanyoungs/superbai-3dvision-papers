# All 5 Papers — 1 Slide Synthetic Summary

---

## Core Synthesis

**Tracking performance improves when identity association is learned and geometry is moved earlier into the pipeline.**

### 3 design buckets

**1. Learned association on 2D detections**
- CAMELTrack → learn multi-cue fusion inside tracking-by-detection
- MOTIP → treat association as trajectory-conditioned ID prediction

**2. Multi-camera graph reasoning after detection**
- ReST → spatial graph first, temporal graph second
- One Graph → one dynamic graph over time, views, context, and scene priors

**3. Early-fusion 3D tracking**
- MCBLT → BEV fusion, 3D detection, hierarchical GNN, global long-term association

### Design axes to remember

- **Fusion point:** late vs unified vs early
- **Association object:** embedding distance vs ID tokens vs graph edges
- **Geometry prior:** none / ground plane / BEV 3D / scene mesh
- **Long-term handling:** cue history, ID prompts, reconfiguration, global block, scene priors

### Practical takeaway for a 3D team

**Use the richest geometry you can afford, but keep the association module learned and modular.**
