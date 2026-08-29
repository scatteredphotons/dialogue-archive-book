#!/usr/bin/env python3
"""Inventory document assets and flag exact or title-like duplicate candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


SUPPORTED_SUFFIXES = {".docx", ".pdf"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_title(path: Path) -> str:
    title = path.stem.casefold()
    title = re.sub(r"(?:copy|副本|最终版|final|修订版|v\d+)$", "", title)
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", title)


def groups(records: list[dict], key: str) -> list[list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for record in records:
        grouped[record[key]].append(record["path"])
    return [paths for paths in grouped.values() if len(paths) > 1]


def build_inventory(root: Path) -> dict:
    records = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in SUPPORTED_SUFFIXES:
            continue
        records.append(
            {
                "title": path.stem,
                "normalized_title": normalized_title(path),
                "path": str(path.resolve()),
                "relative_path": str(path.relative_to(root)),
                "suffix": path.suffix.casefold(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return {
        "root": str(root.resolve()),
        "asset_count": len(records),
        "assets": records,
        "exact_duplicate_groups": groups(records, "sha256"),
        "normalized_title_candidates": groups(records, "normalized_title"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Root directory to scan recursively")
    parser.add_argument("--output", type=Path, help="Write JSON to this path; stdout otherwise")
    args = parser.parse_args()

    if not args.root.is_dir():
        parser.error(f"not a directory: {args.root}")

    payload = json.dumps(build_inventory(args.root), ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
        print(f"Wrote inventory to {args.output}", file=sys.stderr)
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
