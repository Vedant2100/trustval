"""Export a small, complete Overleaf project from the tracked AGENT manuscript.

Usage:
    python paper/agent2027/export_overleaf.py
    python paper/agent2027/export_overleaf.py --output /tmp/trustval-overleaf.zip

This script includes only files used by LaTeX, not raw run outputs or repo code.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
FILES = (
    "main.tex",
    "references.bib",
    "tables/v3-primary.tex",
    "tables/revisions.tex",
    "tables/trace-comparison.tex",
)


def export(output: Path) -> Path:
    missing = [name for name in FILES if not (HERE / name).is_file()]
    if missing:
        raise FileNotFoundError("Overleaf export missing: " + ", ".join(missing))
    for name in FILES:
        if not (HERE / name).resolve().is_relative_to(HERE):
            raise ValueError("Unsafe relative path: " + name)

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name in FILES:
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, (HERE / name).read_bytes())
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "trustval-overleaf.zip")
    args = parser.parse_args()
    print(export(args.output))
