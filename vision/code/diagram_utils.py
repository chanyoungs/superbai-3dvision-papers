from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

DARK_BG = "#000000"
LIGHT_BOX = "#EAEAEA"
EDGE = "#B9C6D8"
TEXT = "#222222"

DA3 = "#FF6A45"
VGGT = "#4C46F5"
MOGE = "#17D4D1"
ACCENT = "#F0A500"


def setup_figure(width: float, height: float):
    fig, ax = plt.subplots(figsize=(width, height), dpi=150)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis("off")
    return fig, ax


def save_figure(fig, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def add_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    facecolor: str = LIGHT_BOX,
    edgecolor: str = EDGE,
    textcolor: str = TEXT,
    lw: float = 1.8,
    dashed: bool = False,
    fontsize: int = 12,
    alpha: float = 1.0,
    zorder: int = 2,
):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=1.8",
        linewidth=lw,
        edgecolor=edgecolor,
        facecolor=facecolor,
        linestyle=(0, (3, 3)) if dashed else "solid",
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        color=textcolor,
        ha="center",
        va="center",
        fontsize=fontsize,
        family="DejaVu Sans",
        zorder=zorder + 1,
        wrap=True,
    )
    return box


def add_outline(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    label: str,
    color: str,
    fontsize: int = 12,
    dashed: bool = False,
):
    outline = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=2.0",
        linewidth=2.2,
        edgecolor=color,
        facecolor="none",
        linestyle=(0, (4, 3)) if dashed else "solid",
        zorder=1,
    )
    ax.add_patch(outline)
    ax.text(
        x + w / 2,
        y + h - 1.2,
        label,
        color=color,
        ha="center",
        va="center",
        fontsize=fontsize,
        weight="bold",
        family="DejaVu Serif",
        zorder=2,
    )
    return outline


def add_arrow(
    ax,
    start: Tuple[float, float],
    end: Tuple[float, float],
    color: str = EDGE,
    lw: float = 1.8,
    rad: float = 0.0,
    linestyle: str = "solid",
    zorder: int = 3,
):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=11,
        linewidth=lw,
        color=color,
        linestyle=linestyle,
        connectionstyle=f"arc3,rad={rad}",
        zorder=zorder,
    )
    ax.add_patch(arrow)
    return arrow
