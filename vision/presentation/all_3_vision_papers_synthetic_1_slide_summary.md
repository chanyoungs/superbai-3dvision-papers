# All 3 Vision Papers - 1 Slide Summary

Scope: Depth Anything 3, MoGe-2, and VGGT

---

## Slide 1 - Synthetic view

### A three-level picture of modern 3D vision

**MoGe-2**
- single-image metric geometry
- strongest when scale + sharp detail matter

**Depth Anything 3**
- any-view geometry from 1 to many images
- depth + ray representation, posed or unposed inputs

**VGGT**
- multi-view transformer for cameras, depth, point maps, and tracks
- strongest as a fast general multi-view 3D backbone

Common pattern:
- big public 3D training mixtures
- transformer backbones with minimal manual geometry design
- geometry treated as a reusable foundation capability

Main takeaway:

**Read the three papers as complementary foundation models for different points on the single-view to multi-view 3D stack.**
