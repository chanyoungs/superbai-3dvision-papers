
from __future__ import annotations

import argparse
from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

BG = "#F5F7FB"
NAVY = "#13213D"
TEXT = "#1D2740"
MUTED = "#6A7895"
LIGHT = "#D3D9E6"
TEAL = "#1CA395"
ORANGE = "#F28E2B"
BLUE = "#3867E8"
PURPLE = "#8A5CF6"
RED = "#E45756"
SLATE = "#4F5968"
SOFT_GRAY = "#E9EEF6"

PAPER_COLORS = {
    "ReST": TEAL,
    "MCBLT": ORANGE,
    "UMPN": BLUE,
    "CAMELTrack": RED,
    "MOTIP": PURPLE,
}


def wrap(s: str, width: int) -> str:
    return "\n".join(textwrap.wrap(s, width=width))


def set_style() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": BG,
            "axes.facecolor": BG,
            "savefig.facecolor": BG,
            "font.family": "DejaVu Sans",
            "axes.edgecolor": LIGHT,
            "axes.labelcolor": MUTED,
            "text.color": TEXT,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "axes.titleweight": "bold",
            "axes.titlesize": 20,
        }
    )


def save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def rounded_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    fc: str = SOFT_GRAY,
    ec: str = LIGHT,
    lw: float = 1.2,
    radius: float = 0.02,
    fontsize: float = 11,
    weight: str = "normal",
    color: str = TEXT,
    ha: str = "center",
    va: str = "center",
):
    box = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=patches.BoxStyle("Round", pad=0.01, rounding_size=radius),
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h / 2,
        text
        ha=ha,
        va=va,
        fontsize=fontsize,
        fontweight=weight,
        color=color,
    )
    return box


def badge(ax, x: float, y: float, text: str, fc: str, width: float | None = None):
    width = width or max(0.1, 0.010 * len(text) + 0.12)
    return rounded_box(ax, x, y, width, 0.08, text, fc=fc, ec=fc, color="white", fontsize=11, radius=0.025)


def arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = MUTED,
    lw: float = 1.4,
    ls: str = "-",
    rad: float = 0.0,
    mutation_scale: float = 12,
):
    patch = patches.FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=lw,
        color=color,
        linestyle=ls,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(patch)
    return patch


def circle_label(ax, x: float, y: float, r: float, text: str, fc: str):
    circ = patches.Circle((x, y), r, facecolor=fc, edgecolor=fc, lw=1.0)
    ax.add_patch(circ)
    ax.text(x, y, text, ha="center", va="center", fontsize=12, color="white", fontweight="bold")
    return circ


def style_axis_for_chart(ax, title: str, xlabel: str = "", ylabel: str = ""):
    ax.set_title(title, loc="left")
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", linewidth=1.0, color="#CBD3E1")


def fig_title_concept(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(5.1, 6.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ys = [0.82, 0.66, 0.50, 0.34, 0.18]
    labels = ["ReST", "MCBLT", "UMPN", "MOTIP", "CAMELTrack"]
    for y, label in zip(ys, labels):
        rounded_box(ax, 0.08, y - 0.035, 0.18, 0.07, label, fc=PAPER_COLORS[label], ec=PAPER_COLORS[label], fontsize=10, color="white", radius=0.04)

    geometry = circle_label(ax, 0.79, 0.82, 0.12, "Geometry", BLUE)
    memory = circle_label(ax, 0.79, 0.52, 0.12, "Memory", ORANGE)
    assoc = circle_label(ax, 0.79, 0.22, 0.12, "Association", RED)

    edges = {
        "ReST": ["Geometry", "Memory"],
        "MCBLT": ["Geometry", "Memory"],
        "UMPN": ["Geometry", "Memory", "Association"],
        "MOTIP": ["Association"],
        "CAMELTrack": ["Association"],
    }
    targets = {"Geometry": (0.67, 0.82), "Memory": (0.67, 0.52), "Association": (0.67, 0.22)}
    for y, label in zip(ys, labels):
        x0 = 0.26
        for idx, concept in enumerate(edges[label]):
            xt, yt = targets[concept]
            arrow(ax, (x0, y), (xt, yt), color="#8AA0BF", lw=1.25, rad=0.05 * (idx - 1))
    save(fig, out_dir / "01_title_concept.png")


def fig_exec_synthesis(data_dir: Path, out_dir: Path) -> None:
    df = pd.read_csv(data_dir / "executive_synthesis_positions.csv")
    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    style_axis_for_chart(
        ax,
        "Executive synthesis",
        xlabel="later fusion \u2192 early BEV fusion",
        ylabel="more learned / longer memory",
    )
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.grid(True, linestyle="--", linewidth=0.8, color="#E1E7F0")
    ax.plot([2.2, 8.4], [4.8, 8.9], linestyle="--", linewidth=1.2, color="#9AA7BF")
    ax.text(8.55, 9.2, "direction of stronger\ngeometry + memory", fontsize=9, color=MUTED, ha="left")

    markers = {"MTMC": "o", "Association lesson": "D"}
    for _, row in df.iterrows():
        ax.scatter(row["x"], row["y"], s=140, color=PAPER_COLORS[row["paper"]], marker=markers[row["category"]], edgecolor=BG, linewidth=1.5, zorder=3)
        ax.text(row["x"] + 0.15, row["y"] + 0.12, row["paper"], fontsize=9.5, weight="bold", color=TEXT)

    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=BLUE, markersize=8, label="MTMC"),
        Line2D([0], [0], marker="D", color="w", markerfacecolor=RED, markersize=8, label="single-view lesson"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=True, facecolor=BG, edgecolor=LIGHT)
    ax.text(0.02, -0.18, "Qualitative synthesis for the deck; coordinates are directional rather than paper-reported metrics.", transform=ax.transAxes, fontsize=9, color=MUTED)
    save(fig, out_dir / "02_exec_synthesis_scatter.png")


def fig_comparison_table(data_dir: Path, out_dir: Path) -> None:
    df = pd.read_csv(data_dir / "comparison_summary.csv")
    fig, ax = plt.subplots(figsize=(12.2, 4.6))
    ax.axis("off")

    columns = ["paper", "role", "fusion_point", "association_core", "key_reported_result", "main_takeaway"]
    display_cols = ["Paper", "Role", "Fusion point", "Association core", "Key reported result", "Main takeaway"]
    cell_text = []
    for _, row in df.iterrows():
        cell_text.append([row[c] for c in columns])

    table = ax.table(
        cellText=cell_text,
        colLabels=display_cols,
        cellLoc="left",
        colLoc="center",
        loc="upper center",
        bbox=[0.0, 0.1, 1.0, 0.84],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)

    # header
    for c in range(len(display_cols)):
        cell = table[(0, c)]
        cell.set_facecolor(NAVY)
        cell.set_edgecolor(BG)
        cell.get_text().set_color("white")
        cell.get_text().set_weight("bold")
        cell.PAD = 0.02

    row_fill = {
        "ReST": "#E8F6F3",
        "MCBLT": "#FBEFDA",
        "UMPN": "#E8EFFF",
        "CAMELTrack": "#FBE9E8",
        "MOTIP": "#F2ECFF",
    }
    for r in range(1, len(df) + 1):
        paper = df.iloc[r - 1]["paper"]
        for c in range(len(display_cols)):
            cell = table[(r, c)]
            cell.set_facecolor(row_fill[paper])
            cell.set_edgecolor(LIGHT)
            cell.PAD = 0.02
            if c == 0:
                cell.get_text().set_weight("bold")
                cell.get_text().set_color(PAPER_COLORS[paper])

    table.scale(1, 1.65)
    ax.text(0.995, 0.03, "\u2020 MCBLT WildTrack best number uses the same detections as EarlyBird; compare directionally.", ha="right", va="bottom", fontsize=10, color=MUTED)
    save(fig, out_dir / "03_comparison_table.png")


def fig_wildtrack_bar(data_dir: Path, out_dir: Path) -> None:
    df = pd.read_csv(data_dir / "wildtrack_comparison.csv")
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    style_axis_for_chart(ax, "WildTrack IDF1\n(as reported in each paper)")
    x = np.arange(len(df))
    colors = [TEAL, ORANGE, BLUE]
    bars = ax.bar(x, df["idf1"], color=colors, width=0.58)
    ax.set_xticks(x, df["model"], fontsize=12, color=TEXT)
    ax.set_ylim(75, 100)
    ax.set_yticks(np.arange(75, 101, 5))
    for i, b in enumerate(bars):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.8, f"{df.iloc[i]['idf1']:.1f}", ha="center", fontsize=11, fontweight="bold", color=TEXT)
        ax.text(b.get_x() + b.get_width() / 2, 76.0, f"MOTA {df.iloc[i]['mota']:.1f}", ha="center", va="bottom", fontsize=10, color=MUTED)
    ax.text(0.99, -0.18, "\u2020 same detections as EarlyBird", transform=ax.transAxes, ha="right", fontsize=9, color=MUTED)
    save(fig, out_dir / "04_wildtrack_bar.png")


def fig_taxonomy_arch(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(12.2, 6.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Top: association heads
    rounded_box(ax, 0.04, 0.66, 0.92, 0.28, "", fc="#F3F6FB")
    ax.text(0.5, 0.93, "Association heads that can be plugged into MTMC", ha="center", va="center", fontsize=15)
    rounded_box(ax, 0.06, 0.77, 0.12, 0.08, "Track history\n+ cue bank")
    rounded_box(ax, 0.22, 0.77, 0.18, 0.08, "Learned association\nrepresentation", fc="#FFF2F1", ec=RED)
    rounded_box(ax, 0.44, 0.77, 0.10, 0.08, "CAMEL\nmulti-cue fusion", fc=RED, ec=RED, color="white")
    rounded_box(ax, 0.46, 0.67, 0.14, 0.08, "Matched IDs /\nembeddings")
    badge(ax, 0.44, 0.88, "MOTIP\nID prediction", PURPLE, width=0.13)
    arrow(ax, (0.18, 0.81), (0.22, 0.81))
    arrow(ax, (0.40, 0.81), (0.46, 0.71))
    arrow(ax, (0.40, 0.81), (0.44, 0.81), color=RED, ls="--")
    arrow(ax, (0.33, 0.85), (0.50, 0.88), color=PURPLE, ls=(0, (3, 3)))

    # Middle: early BEV / 3D
    rounded_box(ax, 0.02, 0.41, 0.96, 0.18, "", fc="#F3F6FB")
    ax.text(0.5, 0.58, "Early BEV / 3D pipelines", ha="center", va="center", fontsize=16)
    xs = [0.03, 0.21, 0.40, 0.64, 0.84]
    widths = [0.13, 0.16, 0.14, 0.14, 0.12]
    labels = [
        "Synced camera\nstreams + calibration",
        "Multi-view encoder\n\u2192 BEV features",
        "3D detections in BEV",
        "Hierarchical GNN\n+ global block",
        "Long-term MTMC\ntracks",
    ]
    for x, w, label in zip(xs, widths, labels):
        rounded_box(ax, x, 0.44, w, 0.08, label, fc="#F2F2EE" if x in (0.03, 0.84) else "#F8F1E8", ec=ORANGE if x in (0.40, 0.64) else LIGHT, radius=0.02)
    for a, b in zip([0.16, 0.37, 0.54, 0.78], [0.21, 0.40, 0.64, 0.84]):
        arrow(ax, (a, 0.48), (b, 0.48))
    badge(ax, 0.88, 0.53, "MCBLT", ORANGE, width=0.08)
    arrow(ax, (0.92, 0.53), (0.76, 0.52), color=ORANGE, ls=(0, (3, 3)))

    # Bottom: late 2D graph
    rounded_box(ax, 0.04, 0.05, 0.78, 0.30, "", fc="#F3F6FB")
    ax.text(0.43, 0.33, "Late 2D graph pipelines", ha="center", va="center", fontsize=16)
    rounded_box(ax, 0.05, 0.15, 0.12, 0.08, "Synced camera\nstreams")
    rounded_box(ax, 0.23, 0.15, 0.14, 0.08, "Per-view detection\n+ world projection")
    rounded_box(ax, 0.41, 0.15, 0.18, 0.08, "Cross-view + temporal\nassociation graph", fc="#ECFAF7", ec=TEAL)
    rounded_box(ax, 0.63, 0.05, 0.14, 0.06, "Online track IDs")
    badge(ax, 0.62, 0.25, "UMPN\ndynamic graph + scene priors", BLUE, width=0.16)
    badge(ax, 0.65, 0.15, "ReST\nsplit spatial\u2192temporal", TEAL, width=0.15)
    arrow(ax, (0.17, 0.19), (0.23, 0.19))
    arrow(ax, (0.37, 0.19), (0.41, 0.19))
    arrow(ax, (0.50, 0.19), (0.63, 0.08))
    arrow(ax, (0.58, 0.20), (0.62, 0.20), color=BLUE, ls=(0, (3, 3)))
    arrow(ax, (0.58, 0.19), (0.65, 0.19), color=TEAL, ls=(0, (3, 3)))
    save(fig, out_dir / "05_taxonomy_arch.png")


def fig_rest_pipeline(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(10.2, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rounded_box(ax, 0.03, 0.18, 0.26, 0.54, "", fc="#F3F6FB")
    rounded_box(ax, 0.37, 0.29, 0.10, 0.28, "2  Reconfiguration", fc="#EDF5FA")
    rounded_box(ax, 0.53, 0.18, 0.28, 0.54, "", fc="#F3F6FB")

    ax.text(0.05, 0.68, "1  Cross-view graph @ t", fontsize=13, fontweight="bold")
    ax.text(0.55, 0.68, "3  Temporal graph\n    t \u2192 t+1", fontsize=13, fontweight="bold")

    # left panel nodes
    cams = ["c1", "c2", "c3"]
    ys = [0.52, 0.40, 0.28]
    for cam, y in zip(cams, ys):
        ax.text(0.04, y, cam, fontsize=10, color=MUTED, va="center")
        ax.plot([0.08, 0.23], [y, y], color="#D4DCE8", lw=1.2)
    node_positions = [(0.10, 0.52), (0.16, 0.52), (0.10, 0.40), (0.16, 0.40), (0.10, 0.28), (0.16, 0.28)]
    node_colors = [BLUE, ORANGE, TEAL, BLUE, TEAL, ORANGE]
    for (x, y), c in zip(node_positions, node_colors):
        ax.add_patch(patches.Circle((x, y), 0.012, facecolor=c, edgecolor=c))
    # spatial edges
    spatial_pairs = [((0.10, 0.52), (0.10, 0.40)), ((0.16, 0.52), (0.16, 0.40)), ((0.10, 0.40), (0.10, 0.28))]
    for a, b in spatial_pairs:
        arrow(ax, a, b, color=BLUE, lw=1.3, mutation_scale=8)
    # temporal-ish within frame match edges
    temporal_pairs = [((0.10, 0.52), (0.16, 0.52)), ((0.10, 0.40), (0.16, 0.40)), ((0.10, 0.28), (0.16, 0.28))]
    for a, b in temporal_pairs:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=ORANGE, lw=1.4)

    # reconfiguration arrows
    for y0, y1 in [(0.52, 0.52), (0.40, 0.48), (0.28, 0.44)]:
        arrow(ax, (0.23, y0), (0.37, y1), color="#97A7BF", lw=1.2)
    ax.add_patch(patches.Circle((0.42, 0.47), 0.014, facecolor=TEAL, edgecolor=TEAL))
    ax.add_patch(patches.Circle((0.42, 0.37), 0.014, facecolor=ORANGE, edgecolor=ORANGE))

    # right panel nodes
    positions = {
        "a0": (0.58, 0.52),
        "a1": (0.68, 0.52),
        "b0": (0.58, 0.36),
        "b1": (0.68, 0.36),
    }
    for key, pos in positions.items():
        c = TEAL if key.startswith("a") else ORANGE
        ax.add_patch(patches.Circle(pos, 0.014, facecolor=c, edgecolor=c))
    ax.text(0.58, 0.59, "t", fontsize=10, color=MUTED)
    ax.text(0.68, 0.59, "t+1", fontsize=10, color=MUTED)
    arrow(ax, positions["a0"], positions["a1"], color=ORANGE, lw=1.4)
    arrow(ax, positions["b0"], positions["b1"], color=ORANGE, lw=1.4)
    ax.plot([positions["a0"][0], positions["b0"][0]], [positions["a0"][1], positions["b0"][1]], color=BLUE, lw=1.4)
    ax.plot([positions["a1"][0], positions["b1"][0]], [positions["a1"][1], positions["b1"][1]], color=BLUE, lw=1.4)

    ax.text(0.75, 0.22, "Blue = spatial edge\norange = temporal edge", fontsize=9, color=MUTED)
    save(fig, out_dir / "06_rest_pipeline.png")


def fig_mcblt_pipeline(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(12.0, 3.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    nodes = [
        (0.03, 0.42, 0.08, "Multi-view\ncameras", "#F2F2EE", LIGHT),
        (0.16, 0.42, 0.10, "BEVFormer\nbackbone", "#F8F1E8", ORANGE),
        (0.30, 0.42, 0.09, "3D boxes\n+ ID feats", "#F8F1E8", ORANGE),
        (0.42, 0.42, 0.10, "2D detector\n+ ReID", "#F2F2EE", LIGHT),
        (0.56, 0.42, 0.12, "2D\u20133D\nassociation", "#F2F2EE", LIGHT),
        (0.72, 0.42, 0.12, "Hierarchical\nGNN", "#F8F1E8", ORANGE),
        (0.87, 0.42, 0.08, "Global block", ORANGE, ORANGE),
    ]
    for x, y, w, text, fc, ec in nodes:
        rounded_box(ax, x, y, w, 0.16, text, fc=fc, ec=ec, fontsize=11, color="white" if fc == ORANGE else TEXT, radius=0.02)
    rounded_box(ax, 0.96, 0.42, 0.07, 0.16, "Long-term\ntracks", fc="#F2F2EE", ec=LIGHT, fontsize=10)
    for idx in range(len(nodes)):
        x0 = nodes[idx][0] + nodes[idx][2]
        if idx < len(nodes) - 1:
            x1 = nodes[idx + 1][0]
        else:
            x1 = 0.96
        arrow(ax, (x0, 0.50), (x1, 0.50))
    save(fig, out_dir / "07_mcblt_pipeline.png")


def fig_aicity_ablation(data_dir: Path, out_dir: Path) -> None:
    df = pd.read_csv(data_dir / "aicity_long_term_ablation.csv")
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    style_axis_for_chart(ax, "Long-term association ablation (AICity)")
    x = np.arange(len(df))
    ax.plot(x, df["hota"], color=ORANGE, linewidth=3.0, marker="o", markersize=7, label="HOTA")
    ax.plot(x, df["assa"], color=SLATE, linewidth=3.0, marker="o", markersize=7, label="AssA")
    ax.fill_between(x, df["assa"], df["hota"], color=ORANGE, alpha=0.06)
    ax.set_xticks(x, df["setting"], color=TEXT)
    ax.set_ylim(20, 85)
    ax.legend(loc="lower right", frameon=True, edgecolor=LIGHT)
    ax.text(x[-1], df["hota"].iloc[-1] + 1.5, f"{df['hota'].iloc[-1]:.2f}", color=ORANGE, fontsize=11, fontweight="bold", ha="center")
    ax.text(0.99, -0.16, "heuristics \u2192 global block", transform=ax.transAxes, ha="right", fontsize=10, color=MUTED)
    save(fig, out_dir / "08_aicity_ablation.png")


def fig_umpn_graph(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(10.0, 4.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rounded_box(ax, 0.05, 0.18, 0.90, 0.62, "", fc="#F3F6FB")
    ax.text(0.07, 0.76, "Dynamic spatio-temporal graph", fontsize=15, fontweight="bold")
    ax.text(0.07, 0.70, "View + temporal + contextual + optional camera edges", fontsize=10.5, color=MUTED)

    # left time slice
    t0_left = [(0.18, 0.50), (0.18, 0.34)]
    t0_right = [(0.30, 0.48), (0.30, 0.36)]
    t1_left = [(0.42, 0.52), (0.42, 0.34)]
    t1_right = [(0.54, 0.54), (0.54, 0.36)]

    for x, y in t0_left + t1_left:
        ax.add_patch(patches.Circle((x, y), 0.012, facecolor=BLUE, edgecolor=BLUE))
    for x, y in t0_right + t1_right:
        ax.add_patch(patches.Circle((x, y), 0.012, facecolor=TEAL, edgecolor=TEAL))

    ax.text(0.15, 0.58, "cam 1", fontsize=9, color=MUTED)
    ax.text(0.15, 0.42, "cam 2", fontsize=9, color=MUTED)
    ax.text(0.29, 0.58, "t", fontsize=9, color=MUTED)
    ax.text(0.53, 0.58, "t+1", fontsize=9, color=MUTED)

    # view edges
    for a, b in [(t0_left[0], t0_left[1]), (t1_left[0], t1_left[1])]:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=BLUE, lw=1.4)
    # temporal edges
    for a, b in [(t0_left[0], t1_left[0]), (t0_left[1], t1_left[1]), (t0_right[0], t1_right[0]), (t0_right[1], t1_right[1])]:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=ORANGE, lw=1.4)
    # context edges
    for a, b in [(t0_left[0], t0_right[0]), (t0_left[1], t0_right[1]), (t1_left[0], t1_right[0]), (t1_left[1], t1_right[1])]:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=TEAL, lw=1.4, linestyle="--")
    # camera vertex + scene prior
    ax.add_patch(patches.Circle((0.78, 0.26), 0.014, facecolor="#9AA7B7", edgecolor="#9AA7B7"))
    ax.text(0.74, 0.21, "camera vertex", fontsize=8.5, color=MUTED)
    ax.text(0.72, 0.46, "occluder /\nscene prior", fontsize=8.5, color=MUTED)
    for p in t1_right + t0_right:
        ax.plot([p[0], 0.78], [p[1], 0.26], color="#B3BFCE", lw=1.0)

    # legend
    legend_x = 0.83
    y0 = 0.52
    ax.plot([legend_x, legend_x + 0.05], [y0, y0], color="#B3BFCE", lw=1.2)
    ax.text(legend_x + 0.055, y0, "camera edge", fontsize=8.5, color=MUTED, va="center")
    y0 -= 0.08
    ax.plot([legend_x, legend_x + 0.05], [y0, y0], color=TEAL, lw=1.4, linestyle="--")
    ax.text(legend_x + 0.055, y0, "context edge", fontsize=8.5, color=MUTED, va="center")
    y0 -= 0.08
    ax.plot([legend_x, legend_x + 0.05], [y0, y0], color=ORANGE, lw=1.4)
    ax.text(legend_x + 0.055, y0, "temporal edge", fontsize=8.5, color=MUTED, va="center")
    y0 -= 0.08
    ax.plot([legend_x, legend_x + 0.05], [y0, y0], color=BLUE, lw=1.4)
    ax.text(legend_x + 0.055, y0, "view edge", fontsize=8.5, color=MUTED, va="center")
    save(fig, out_dir / "09_umpn_dynamic_graph.png")


def fig_scene_priors(data_dir: Path, out_dir: Path) -> None:
    df = pd.read_csv(data_dir / "scout_scene_priors.csv")
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    style_axis_for_chart(ax, "Scene priors help hardest SCOUT splits")
    x = np.arange(len(df))
    width = 0.36
    ax.bar(x - width / 2, df["without_scene_prior"], width=width, color="#9AA7B7", label="without scene prior")
    ax.bar(x + width / 2, df["with_scene_prior"], width=width, color=BLUE, label="with scene prior")
    ax.set_xticks(x, [wrap(m, 10) for m in df["metric"]], color=TEXT)
    ax.set_ylim(0, 80)
    ax.legend(loc="upper right", frameon=True, edgecolor=LIGHT)
    for i in range(len(df)):
        ax.text(i - width / 2, df.iloc[i]["without_scene_prior"] + 1.0, f"{df.iloc[i]['without_scene_prior']:.1f}", ha="center", va="bottom", fontsize=10, color=TEXT)
        ax.text(i + width / 2, df.iloc[i]["with_scene_prior"] + 1.0, f"{df.iloc[i]['with_scene_prior']:.1f}", ha="center", va="bottom", fontsize=10, color=TEXT)
    save(fig, out_dir / "10_scout_scene_priors.png")


def fig_association_heads(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(10.0, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # MOTIP band
    rounded_box(ax, 0.03, 0.58, 0.92, 0.32, "", fc="#F3F6FB")
    ax.text(0.50, 0.86, "MOTIP lesson: learn ID decoding", ha="center", fontsize=13)
    rounded_box(ax, 0.07, 0.70, 0.18, 0.10, "Track history\n+ ID prompts")
    rounded_box(ax, 0.33, 0.70, 0.16, 0.10, "Transformer\nID decoder", fc=PURPLE, ec=PURPLE, color="white")
    rounded_box(ax, 0.57, 0.70, 0.16, 0.10, "ID labels /\nassignment")
    rounded_box(ax, 0.08, 0.60, 0.20, 0.06, "ID dictionary", fc="#F2ECFF", ec=PURPLE, fontsize=10)
    arrow(ax, (0.25, 0.75), (0.33, 0.75))
    arrow(ax, (0.49, 0.75), (0.57, 0.75))

    # CAMEL band
    rounded_box(ax, 0.03, 0.08, 0.92, 0.38, "", fc="#F3F6FB")
    ax.text(0.50, 0.42, "CAMELTrack lesson: learn cue fusion", ha="center", fontsize=13)
    rounded_box(ax, 0.06, 0.19, 0.18, 0.10, "Tracklet history\n+ cues")
    rounded_box(ax, 0.30, 0.19, 0.20, 0.10, "Temporal encoders\n(per cue)", fc="#FFF2F1", ec=RED)
    rounded_box(ax, 0.58, 0.19, 0.20, 0.10, "GAFFE\n(group-aware fusion)", fc=RED, ec=RED, color="white")
    rounded_box(ax, 0.84, 0.19, 0.10, 0.10, "Disentangled\nembeddings")
    arrow(ax, (0.24, 0.24), (0.30, 0.24))
    arrow(ax, (0.50, 0.24), (0.58, 0.24))
    arrow(ax, (0.78, 0.24), (0.84, 0.24))
    save(fig, out_dir / "11_association_heads.png")


def fig_company_blueprint(data_dir: Path, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(12.0, 3.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rounded_box(ax, 0.02, 0.36, 0.10, 0.22, "Synced\ncameras", fc="#F2F2EE")
    rounded_box(ax, 0.15, 0.50, 0.10, 0.12, "2D detector +\nReID / pose", fc="#FFF2F1", ec=RED, fontsize=9.5)
    rounded_box(ax, 0.15, 0.34, 0.10, 0.12, "Early BEV props\n(MCBLT)", fc="#F8F1E8", ec=ORANGE, fontsize=9.5)
    rounded_box(ax, 0.29, 0.42, 0.12, 0.12, "2D\u20133D association\n+ feature bank", fc="#F2F2EE", fontsize=10)
    rounded_box(ax, 0.45, 0.36, 0.15, 0.22, "Stage 1: same-time\ncross-view merge\n(ReST)", fc="#ECFAF7", ec=TEAL, fontsize=10)
    rounded_box(ax, 0.63, 0.36, 0.16, 0.22, "Stage 2: temporal graph\n(UMPN + CAMEL/MOTIP)", fc="#E8EFFF", ec=BLUE, fontsize=10)
    rounded_box(ax, 0.82, 0.36, 0.10, 0.22, "Global memory\nblock\n(MCBLT)", fc="#FBEFDA", ec=ORANGE, fontsize=10)
    rounded_box(ax, 0.94, 0.36, 0.06, 0.22, "Online MTMC\ntracks", fc="#F2F2EE", fontsize=9.5)

    rounded_box(ax, 0.03, 0.20, 0.09, 0.08, "Calibration +\nvisibility map", fc="#F3F6FB", fontsize=8.5)

    arrow(ax, (0.12, 0.47), (0.15, 0.56))
    arrow(ax, (0.12, 0.47), (0.15, 0.40))
    arrow(ax, (0.25, 0.56), (0.29, 0.48))
    arrow(ax, (0.25, 0.40), (0.29, 0.48))
    arrow(ax, (0.41, 0.48), (0.45, 0.47))
    arrow(ax, (0.60, 0.47), (0.63, 0.47))
    arrow(ax, (0.79, 0.47), (0.82, 0.47))
    arrow(ax, (0.92, 0.47), (0.94, 0.47))

    ax.text(0.50, 0.13, "Recommended synthesis: MCBLT front-end + ReST stage separation + UMPN scene priors + CAMEL/MOTIP learned association.", ha="center", fontsize=10.5, color=MUTED)
    save(fig, out_dir / "12_company_blueprint.png")


def build_all(data_dir: Path, out_dir: Path) -> None:
    set_style()
    fig_title_concept(data_dir, out_dir)
    fig_exec_synthesis(data_dir, out_dir)
    fig_comparison_table(data_dir, out_dir)
    fig_wildtrack_bar(data_dir, out_dir)
    fig_taxonomy_arch(data_dir, out_dir)
    fig_rest_pipeline(data_dir, out_dir)
    fig_mcblt_pipeline(data_dir, out_dir)
    fig_aicity_ablation(data_dir, out_dir)
    fig_umpn_graph(data_dir, out_dir)
    fig_scene_priors(data_dir, out_dir)
    fig_association_heads(data_dir, out_dir)
    fig_company_blueprint(data_dir, out_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate diagrams for the MTMC papers review package.")
    parser.add_argument("--outdir", type=Path, default=None, help="Output directory for generated diagrams.")
    parser.add_argument("--datadir", type=Path, default=None, help="Data directory containing CSV source files.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    data_dir = args.datadir or (repo_root / "data")
    out_dir = args.outdir or (repo_root / "diagrams")
    build_all(data_dir, out_dir)


if __name__ == "__main__":
    main()
