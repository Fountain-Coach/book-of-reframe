#!/usr/bin/env python3
"""Validate the release-surface boundary without inferring a release."""

import json
from pathlib import Path
import sys


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "releases/reframe-release-surface.json")
    doc = json.loads(path.read_text(encoding="utf-8"))
    required = {"schemaVersion", "product", "releaseId", "status", "source", "acceptedAt", "capabilityAllowList"}
    missing = required - doc.keys()
    if missing:
        raise SystemExit(f"release manifest missing: {sorted(missing)}")
    if doc["status"] not in {"released", "development-snapshot", "no-released-build"}:
        raise SystemExit(f"invalid release status: {doc['status']}")
    if doc["status"] != "released" and doc["capabilityAllowList"]:
        raise SystemExit("non-released manifest must have an empty capability allow-list")
    if doc["status"] == "released":
        source = doc["source"]
        if not doc["acceptedAt"] or not source.get("commit") or not source.get("build"):
            raise SystemExit("released manifest requires acceptedAt, source.commit, and source.build")
        if not doc["capabilityAllowList"]:
            raise SystemExit("released manifest requires a non-empty capability allow-list")
    print(f"validated {doc['status']} release surface: {doc['releaseId']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
