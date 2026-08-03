#!/usr/bin/env python3
"""Generate the site's numeric/status projection from the checked release evidence."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=Path("../evidence/2026-08-03/reframe-release-surface.json"))
    parser.add_argument("--output", type=Path, default=Path("site-data.json"))
    args = parser.parse_args()
    source = json.loads(args.evidence.read_text())
    snapshot = source["developmentSnapshot"]
    result = {
        "snapshotDate": source["releaseId"].removeprefix("main-development-"),
        "releaseId": source["releaseId"],
        "releaseStatus": source["status"],
        "releaseSourceCommit": source["source"]["commit"],
        "commandEntries": snapshot["commandEntries"],
        "commandEntriesAvailable": snapshot["commandEntriesAvailable"],
        "commandEntriesUnavailable": snapshot["commandEntriesUnavailable"],
        "capabilityIdentities": snapshot["capabilityIdentities"],
        "capabilitiesExecutable": snapshot["capabilitiesExecutable"],
        "capabilitiesLiveAccepted": snapshot["capabilitiesLiveAccepted"],
        "capabilitiesUnavailable": snapshot["capabilitiesUnavailable"],
        "liveAcceptedCapabilityIds": snapshot["liveAcceptedCapabilityIds"],
        "sourceEvidence": "../evidence/2026-08-03/reframe-release-surface.json",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {args.output} from {args.evidence}")


if __name__ == "__main__":
    main()
