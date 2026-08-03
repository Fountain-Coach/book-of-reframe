#!/usr/bin/env python3
"""Build a reviewable Facebook post package from one evidence-backed command page."""

import argparse
import json
from pathlib import Path
import re
import shutil


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("book_root", type=Path)
    parser.add_argument("command_page", type=Path)
    parser.add_argument("--teaser", required=True)
    parser.add_argument("--book-url", required=True)
    parser.add_argument("--output", type=Path, default=Path("facebook-post"))
    args = parser.parse_args()

    page = args.command_page if args.command_page.is_absolute() else args.book_root / args.command_page
    text = page.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("!["):
        raise SystemExit("command page must begin with its GUI snapshot image")
    image_match = re.search(r"\]\(([^)]+)\)", lines[0])
    if not image_match:
        raise SystemExit("snapshot image link is missing")
    image = (page.parent / image_match.group(1)).resolve()
    if not image.is_file():
        raise SystemExit(f"snapshot image missing: {image}")
    if "Live drive:" not in text:
        raise SystemExit("command page has no live-drive proof reference")
    command_match = re.search(r"`(/[^`]+)`", text)
    if not command_match:
        raise SystemExit("command page has no slash command identity")
    command = command_match.group(1)
    evidence = args.book_root / "evidence/2026-08-03/command-evidence.json"
    evidence_doc = json.loads(evidence.read_text(encoding="utf-8"))
    command_evidence = evidence_doc.get("commands", {}).get(command)
    if not command_evidence or command_evidence.get("status") != "live-accepted":
        raise SystemExit(f"command is not live-accepted in evidence manifest: {command}")
    release_doc = json.loads((args.book_root / "evidence/2026-08-03/reframe-release-surface.json").read_text(encoding="utf-8"))
    release_status = release_doc.get("status", "unknown")
    status_line = "Development/evidence preview — no released App surface is recorded." if release_status != "released" else "From a named Reframe release."
    caption = f"{args.teaser.strip()}\n\n{command} — {status_line}\nRead the evidence-backed story in The Book of Reframe: {args.book_url}"
    args.output.mkdir(parents=True, exist_ok=True)
    output_image = args.output / image.name
    shutil.copy2(image, output_image)
    package = {
        "command": command,
        "image": output_image.name,
        "caption": caption,
        "evidence": command_evidence,
        "releaseStatus": release_status,
        "externalPublish": False,
    }
    (args.output / "facebook-post.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    (args.output / "README.md").write_text(
        "# Facebook post package\n\n"
        f"Command: `{command}`\n\n"
        "The image is the command page's own live-drive GUI snapshot. This package has not been posted externally.\n",
        encoding="utf-8",
    )
    print(f"built Facebook package for {command}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
