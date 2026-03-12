from __future__ import annotations

import argparse
from pathlib import Path

from diagram_utils import DA3, EDGE, MOGE, VGGT, add_arrow, add_box, save_figure, setup_figure


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the capability graph for the vision review.")
    parser.add_argument("--outdir", type=Path, default=Path("../assets"))
    args = parser.parse_args()

    fig, ax = setup_figure(16, 9)

    # Left inputs
    add_box(ax, 1, 44, 8, 8, "single\nimage", fontsize=14)
    add_box(ax, 1, 24, 12, 8, "many views\n/ video", fontsize=14)
    add_box(ax, 1, 10, 12, 8, "known poses\n(optional)", fontsize=14)
    add_box(ax, 1, -4, 12, 8, "few\nviews", fontsize=14)

    # Shared thesis
    add_box(ax, 18, 22, 24, 8, "shared thesis:\nplain pretrained ViT backbone", fontsize=14)

    # Paper nodes
    add_box(ax, 47, 48, 26, 8, "MoGe-2\nsingle-view metric geometry", facecolor="#DFF7F6", edgecolor=MOGE, textcolor="#0F7774", lw=2.2, fontsize=14)
    add_box(ax, 48, 26, 23, 8, "VGGT\nfeed-forward multi-task 3D", facecolor="#E5E4FB", edgecolor=VGGT, textcolor="#3F40D8", lw=2.2, fontsize=14)
    add_box(ax, 51, 13, 20, 8, "Depth Anything 3\nany-view geometry", facecolor="#F9E5DE", edgecolor=DA3, textcolor="#C9460B", lw=2.2, fontsize=14)

    # Right outputs
    add_box(ax, 78, 48, 18, 7, "metric point / depth\n+ sharp details", fontsize=14)
    add_box(ax, 78, 34, 18, 7, "point tracks\n/ matching features", fontsize=14)
    add_box(ax, 78, 22, 18, 7, "camera pose\n+ dense geometry", fontsize=14)
    add_box(ax, 78, 10, 18, 7, "NVS / 3DGS\nadapters", fontsize=14)
    add_box(ax, 78, -2, 18, 8, "depth + ray maps\nfor consistent 3D", fontsize=14)

    # Arrows into thesis
    add_arrow(ax, (9, 48), (47, 52), color=MOGE, lw=2.0, rad=-0.18)
    add_arrow(ax, (13, 28), (48, 30), color=VGGT, lw=2.0, rad=-0.10)
    add_arrow(ax, (13, 14), (51, 17), color=DA3, lw=2.0, rad=0.12)
    add_arrow(ax, (13, 0), (18, 26), color=EDGE, lw=2.0)

    # Thesis to papers
    add_arrow(ax, (42, 26), (47, 52), color=MOGE, lw=2.0)
    add_arrow(ax, (42, 26), (48, 30), color=VGGT, lw=2.0)
    add_arrow(ax, (42, 26), (51, 17), color=DA3, lw=2.0)

    # Direct input-to-paper curves
    add_arrow(ax, (9, 48), (48, 30), color=VGGT, lw=1.8, rad=-0.05)
    add_arrow(ax, (9, 48), (51, 17), color=DA3, lw=1.8, rad=0.23)
    add_arrow(ax, (13, 28), (48, 30), color=VGGT, lw=1.8, rad=-0.05)
    add_arrow(ax, (13, 28), (51, 17), color=DA3, lw=1.8)
    add_arrow(ax, (13, 14), (51, 17), color=DA3, lw=1.8, linestyle=(0,(3,3)))
    add_arrow(ax, (13, 14), (48, 30), color=EDGE, lw=1.8, linestyle=(0,(3,3)))
    add_arrow(ax, (13, 0), (48, 30), color=VGGT, lw=1.8, rad=0.18)
    add_arrow(ax, (13, 0), (51, 17), color=DA3, lw=1.8, rad=0.22)

    # Paper outputs
    add_arrow(ax, (73, 52), (78, 51.5), color=MOGE, lw=2.0)
    add_arrow(ax, (71, 30), (78, 37.5), color=VGGT, lw=2.0)
    add_arrow(ax, (71, 30), (78, 25.5), color=VGGT, lw=2.0)
    add_arrow(ax, (71, 30), (78, 13.5), color=VGGT, lw=2.0)
    add_arrow(ax, (71, 17), (78, 25.5), color=DA3, lw=2.0)
    add_arrow(ax, (71, 17), (78, 13.5), color=DA3, lw=2.0)
    add_arrow(ax, (71, 17), (78, 2), color=DA3, lw=2.0)

    outpath = args.outdir / "capability_graph.png"
    save_figure(fig, outpath)


if __name__ == "__main__":
    main()
