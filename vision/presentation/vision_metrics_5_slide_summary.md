# Vision Metrics - 5 Slide Summary

Scope: metrics across Depth Anything 3, MoGe-2, and VGGT

---

## Slide 1 - First check the alignment

Before comparing any result, ask:
- scale-invariant or affine-invariant?
- metric or not?
- point map or depth map?
- are camera intrinsics known?

This matters especially for MoGe-2 versus DA3-style depth metrics.

---

## Slide 2 - Geometry metrics

Point maps:
- `Rel_p`
- `delta1^p`

Depth maps:
- `Rel_d`
- `delta1^d`

MoGe-2 also reports boundary F1 for detail sharpness.

---

## Slide 3 - Pose and reconstruction metrics

Pose:
- AUC@3, AUC@30, AUC@5, AUC@10, AUC@20

Reconstruction:
- Accuracy
- Completeness
- Chamfer / Overall
- precision / recall / F1

---

## Slide 4 - Rendering and tracking metrics

Rendering:
- PSNR
- SSIM
- LPIPS

Tracking / matching:
- AJ
- `delta_vis_avg`
- OA
- pose AUC for image matching

---

## Slide 5 - Takeaway

Main reading rule:

**Do not compare numbers across papers until you know whether they are measuring aligned geometry, metric geometry, pose, rendering, or tracking.**
