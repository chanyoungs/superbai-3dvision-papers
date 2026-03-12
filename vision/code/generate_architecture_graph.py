from __future__ import annotations

import argparse
from pathlib import Path

from diagram_utils import DA3, EDGE, MOGE, VGGT, add_arrow, add_box, add_outline, save_figure, setup_figure


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the architecture overview diagram.")
    parser.add_argument("--outdir", type=Path, default=Path("../assets"))
    args = parser.parse_args()

    fig, ax = setup_figure(16, 9)

    # Lane outlines
    add_outline(ax, 1, 40, 98, 18, "Depth Anything 3  |  any-view geometry", DA3)
    add_outline(ax, 1, 20, 98, 16, "VGGT  |  feed-forward multi-task 3D", VGGT)
    add_outline(ax, 1, 1, 98, 16, "MoGe-2  |  single-image metric geometry", MOGE)

    # DA3 lane
    add_box(ax, 2, 46, 14, 6, "any number of images\n(+ optional poses)", fontsize=12)
    add_box(ax, 20, 46, 14, 6, "plain ViT / DINO backbone", facecolor="#F9E5DE", edgecolor=DA3, textcolor="#4A2A16", fontsize=12)
    add_box(ax, 41, 46, 15, 6, "within-view + cross-view\nself-attention", fontsize=12)
    add_box(ax, 65, 46, 9, 6, "optional\ncamera head", fontsize=12)
    add_box(ax, 65, 40, 11, 6, "dual-DPT\ndepth + ray heads", fontsize=12)
    add_box(ax, 83, 40, 16, 6, "consistent depth + ray maps\n→ fused 3D / NVS", facecolor="#F7E7E0", edgecolor=DA3, textcolor="#4A2A16", fontsize=12)
    add_arrow(ax, (16, 49), (20, 49))
    add_arrow(ax, (34, 49), (41, 49))
    add_arrow(ax, (56, 49), (65, 49))
    add_arrow(ax, (56, 49), (65, 43))
    add_arrow(ax, (76, 43), (83, 43))

    # VGGT lane
    add_box(ax, 2, 24, 13, 5, "1 to 100s of images", fontsize=12)
    add_box(ax, 19, 24, 16, 5, "DINO patchify\n+ camera / register tokens", facecolor="#E5E4FB", edgecolor=VGGT, textcolor="#232483", fontsize=12)
    add_box(ax, 40, 23.5, 16, 6, "alternating\nframe/global self-attention", fontsize=12)
    add_box(ax, 67, 27, 10, 4.5, "DPT heads", fontsize=12)
    add_box(ax, 67, 20.5, 10, 4.5, "camera head", fontsize=12)
    add_box(ax, 84, 27, 15, 4.5, "depth / point / track feats", facecolor="#E5E4FB", edgecolor=VGGT, textcolor="#232483", fontsize=12)
    add_box(ax, 86, 20.5, 9, 4.5, "cameras", facecolor="#E5E4FB", edgecolor=VGGT, textcolor="#232483", fontsize=12)
    add_arrow(ax, (15, 26.5), (19, 26.5))
    add_arrow(ax, (35, 26.5), (40, 26.5))
    add_arrow(ax, (56, 27), (67, 29.25))
    add_arrow(ax, (56, 24), (67, 22.75))
    add_arrow(ax, (77, 29.25), (84, 29.25))
    add_arrow(ax, (77, 22.75), (86, 22.75))

    # MoGe-2 lane
    add_box(ax, 5, 8.5, 8, 4.5, "RGB image", fontsize=12)
    add_box(ax, 18, 8.5, 8, 4.5, "DINOv2 ViT", facecolor="#DFF7F6", edgecolor=MOGE, textcolor="#0F7774", fontsize=12)
    add_box(ax, 43, 11.5, 12, 4.5, "CLS token → MLP\nmetric scale", fontsize=12)
    add_box(ax, 44, 5.5, 7, 3.8, "conv neck", fontsize=12)
    add_box(ax, 64, 9.5, 13, 4.5, "affine-invariant\npoint map head", fontsize=12)
    add_box(ax, 84, 9.5, 15, 4.5, "metric points + depth\nsharp boundaries", facecolor="#DFF7F6", edgecolor=MOGE, textcolor="#0F7774", fontsize=12)
    add_arrow(ax, (13, 10.75), (18, 10.75))
    add_arrow(ax, (26, 10.75), (43, 13.75))
    add_arrow(ax, (26, 10.75), (44, 7.4))
    add_arrow(ax, (55, 13.75), (84, 13.75))
    add_arrow(ax, (51, 7.4), (64, 11.75))
    add_arrow(ax, (77, 11.75), (84, 11.75))

    outpath = args.outdir / "architecture_graph.png"
    save_figure(fig, outpath)


if __name__ == "__main__":
    main()
