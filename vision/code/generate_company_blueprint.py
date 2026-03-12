from __future__ import annotations

import argparse
from pathlib import Path

from diagram_utils import ACCENT, DA3, EDGE, MOGE, VGGT, add_arrow, add_box, add_outline, save_figure, setup_figure


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the company blueprint diagram.")
    parser.add_argument("--outdir", type=Path, default=Path("../assets"))
    args = parser.parse_args()

    fig, ax = setup_figure(16, 6)

    add_outline(ax, 1, 1.5, 13, 34, "TRAINING MIX", EDGE, dashed=True)

    add_box(ax, 2.5, 23, 9, 6, "synthetic 3D\n(rendered scenes)", fontsize=12)
    add_box(ax, 2.5, 13, 9, 6, "refined real RGB-D / SfM\n(filtered + completed)", fontsize=12)
    add_box(ax, 2.5, 3.5, 10.5, 6, "company unlabeled video\n(for distillation / adaptation)", fontsize=12)
    add_box(ax, 17, 14, 14, 6, "teachers + label refinement", facecolor="#F6EADA", edgecolor=ACCENT, textcolor="#9C5D00", lw=2.0, fontsize=12)

    add_arrow(ax, (11.5, 26), (17, 17), color=EDGE, lw=2.0)
    add_arrow(ax, (11.5, 16), (17, 17), color=EDGE, lw=2.0)
    add_arrow(ax, (13, 6.5), (17, 17), color=EDGE, lw=2.0)

    add_box(ax, 41, 25, 17, 6, "shared geometry backbone\nplain pretrained ViT / DINO", fontsize=13)
    add_arrow(ax, (31, 17), (41, 28), color=EDGE, lw=2.2)
    ax.text(35.5, 22.4, "clean supervision", color=EDGE, fontsize=12, family="DejaVu Serif")

    add_box(ax, 61, 31, 13, 6, "monocular metric\naffine point + scale", facecolor="#DFF7F6", edgecolor=MOGE, textcolor="#0F7774", lw=2.0, fontsize=12)
    add_box(ax, 61, 21, 13, 6, "any-view geometry\ndepth + ray + pose", facecolor="#F9E5DE", edgecolor=DA3, textcolor="#C9460B", lw=2.0, fontsize=12)
    add_box(ax, 61, 11, 12, 6, "tracking / matching\nfeature adapter", facecolor="#E5E4FB", edgecolor=VGGT, textcolor="#3F40D8", lw=2.0, fontsize=12)
    add_box(ax, 62.5, 1.5, 10, 6, "NVS / 3DGS\nadapter", fontsize=12)

    add_arrow(ax, (58, 28), (61, 34), color=EDGE, lw=2.0)
    add_arrow(ax, (58, 28), (61, 24), color=EDGE, lw=2.0)
    add_arrow(ax, (58, 28), (61, 14), color=EDGE, lw=2.0)
    add_arrow(ax, (58, 28), (62.5, 4.5), color=EDGE, lw=2.0)

    add_box(ax, 80, 11, 19, 8, "internal benchmark suite:\nmetric depth + sharpness | pose + reconstruction | tracking/NVS | latency/memory", fontsize=12)
    add_arrow(ax, (74, 34), (80, 15), color=EDGE, lw=1.8, linestyle=(0, (3, 3)))
    add_arrow(ax, (74, 24), (80, 15), color=EDGE, lw=1.8, linestyle=(0, (3, 3)))
    add_arrow(ax, (73, 14), (80, 15), color=EDGE, lw=1.8, linestyle=(0, (3, 3)))
    add_arrow(ax, (72.5, 4.5), (80, 15), color=EDGE, lw=1.8, linestyle=(0, (3, 3)))
    add_arrow(ax, (31, 17), (80, 15), color=EDGE, lw=1.8, linestyle=(0, (3, 3)))

    outpath = args.outdir / "company_blueprint_simple.png"
    save_figure(fig, outpath)


if __name__ == "__main__":
    main()
