# Vision Results - 5 Slide Summary

Scope: results across Depth Anything 3, MoGe-2, and VGGT

---

## Slide 1 - How to compare them fairly

These papers solve related but different tasks.

Fair comparison rule:
- DA3 vs VGGT on multi-view geometry
- MoGe-2 on single-image metric geometry
- treat NVS and tracking as downstream evidence

---

## Slide 2 - DA3 vs VGGT

Representative overlap:
- ETH3D pose AUC@3: 48.4 vs 26.3
- ScanNet++ pose AUC@3: 85.0 vs 62.6
- HiRoom F1 w/o pose: 85.1 vs 56.7
- ETH3D F1 w/o pose: 79.0 vs 57.2
- DL3DV PSNR: 21.33 vs 20.96

Readout:
- DA3 is stronger on any-view geometry and NVS backbone quality.

---

## Slide 3 - Where MoGe-2 leads

MoGe-2 is the best single-image metric geometry paper in this set.

Headline evidence:
- metric geometry average rank: 1.95
- sharpness rank: 1.75
- keeps strong relative geometry while adding metric scale

---

## Slide 4 - Where VGGT leads

VGGT is the broadest feed-forward multi-view backbone.

Highlights:
- Re10K AUC@30: 85.3
- Co3Dv2 AUC@30: 88.2
- IMC with BA: 84.91 at AUC@10
- DTU overall: 0.382 without GT cameras
- improves matching, tracking, and NVS downstream tasks

---

## Slide 5 - Takeaway

Best role for each paper:
- MoGe-2 -> single-image metric geometry
- DA3 -> any-view geometry
- VGGT -> multi-view geometry + tracking backbone

Main takeaway:

**These papers are complementary foundation models for different stages of the 3D-vision stack, not just direct competitors.**
