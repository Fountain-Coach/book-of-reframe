#!/usr/bin/env python3
"""Fail closed when published command pages lack their own visual proof."""

from pathlib import Path
import re
import sys


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    pages = sorted(page for page in (root / "commands").glob("*.md") if page.name != "README.md")
    if not pages:
        print("no command pages found", file=sys.stderr)
        return 1
    failures = []
    for page in pages:
        lines = [line.strip() for line in page.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not lines or not lines[0].startswith("!["):
            failures.append(f"{page}: first non-empty line is not an image")
            continue
        match = re.search(r"\]\(([^)]+)\)", lines[0])
        if not match:
            failures.append(f"{page}: snapshot image has no link")
            continue
        image = (page.parent / match.group(1)).resolve()
        if not image.is_file():
            failures.append(f"{page}: missing snapshot {match.group(1)}")
        if "Live drive:" not in page.read_text(encoding="utf-8"):
            failures.append(f"{page}: missing live-drive proof reference")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"verified {len(pages)} command page(s) with leading GUI snapshots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
