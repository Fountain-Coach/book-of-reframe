#!/usr/bin/env python3
"""Generate the site's numeric/status projection from the checked release evidence."""

import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=Path("../evidence/2026-08-15/reframe-release-surface.json"))
    parser.add_argument("--output", type=Path, default=Path("site-data.json"))
    args = parser.parse_args()
    evidence_path = args.evidence.resolve()
    source = json.loads(evidence_path.read_text())
    snapshot = source["developmentSnapshot"]
    manifest_path = Path(__file__).resolve().parent / "publication-manifest.json"
    manifest = json.loads(manifest_path.read_text())
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
        "scenarioRecords": manifest["counts"]["scenarioRecords"],
        "scenarioLiveAccepted": manifest["counts"]["scenarioLiveAccepted"],
        "commandPagesLiveAccepted": manifest["counts"]["commandPagesLiveAccepted"],
        "commandPagesPending": manifest["counts"]["commandPagesPending"],
        "acceptedCommandScenariosWithoutPage": manifest["counts"]["acceptedCommandScenariosWithoutPage"],
        "systemCapabilitiesLiveAccepted": manifest["counts"]["systemCapabilitiesLiveAccepted"],
        "releaseLiveAccepted": manifest["counts"]["releaseLiveAccepted"],
        "publicationManifest": "publication-manifest.json",
        "publicationManifestDigest": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "sourceEvidence": f"../evidence/{source['releaseId'].removeprefix('main-development-')}/reframe-release-surface.json",
    }
    output_path = args.output.resolve()
    output_path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {output_path} from {evidence_path}")


if __name__ == "__main__":
    main()
