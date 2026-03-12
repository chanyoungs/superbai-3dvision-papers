from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(script: Path, outdir: Path) -> None:
    subprocess.run([sys.executable, str(script), "--outdir", str(outdir)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate all diagrams for the vision review.")
    parser.add_argument("--outdir", type=Path, default=Path("../assets"))
    args = parser.parse_args()

    code_dir = Path(__file__).resolve().parent
    outdir = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    run(code_dir / "generate_capability_graph.py", outdir)
    run(code_dir / "generate_architecture_graph.py", outdir)
    run(code_dir / "generate_company_blueprint.py", outdir)

    print(f"Generated diagrams in: {outdir.resolve()}")


if __name__ == "__main__":
    main()
