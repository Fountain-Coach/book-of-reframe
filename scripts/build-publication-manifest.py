#!/usr/bin/env python3
"""Compile the scenario acceptance projection and the release boundary.

Scenario acceptance decides whether a command page is eligible for publication.
The named release surface is deliberately kept as a separate axis.
"""

import argparse
import hashlib
import json
from pathlib import Path


STATUSES = {"draft", "executable", "live-accepted", "blocked", "retired"}
KINDS = {"command", "capability", "system-boundary", "projection", "failure-recovery"}


def load(path):
    return json.loads(path.read_text())


def route_for(page):
    if not page:
        return None
    return "/" + page.removesuffix(".md").strip("/") + "/"


def validate_record(record, location, book_root):
    for key in ("scenario", "scenarioKind", "status"):
        if not record.get(key):
            raise ValueError(f"{location} missing {key}")
    if record["status"] not in STATUSES:
        raise ValueError(f"{location} has invalid status {record['status']}")
    if record["scenarioKind"] not in KINDS:
        raise ValueError(f"{location} has invalid scenarioKind {record['scenarioKind']}")
    page = record.get("page")
    if page and not (book_root / page).is_file():
        raise ValueError(f"{location} points to missing page {page}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-root", type=Path, default=Path("."))
    parser.add_argument("--coverage", type=Path, default=Path("scenarios/coverage.json"))
    parser.add_argument("--release", type=Path, default=Path("evidence/2026-08-15/reframe-release-surface.json"))
    parser.add_argument("--output", type=Path, default=Path("site/publication-manifest.json"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.book_root.resolve()
    coverage = load((root / args.coverage).resolve())
    release = load((root / args.release).resolve())

    routes = []
    for group in ("commands", "upcoming"):
        for index, record in enumerate(coverage.get(group, [])):
            location = f"{group}[{index}]"
            validate_record(record, location, root)
            page = record.get("page")
            accepted = record["status"] == "live-accepted"
            routes.append({
                "command": record.get("command"),
                "capability": record.get("capability"),
                "scenario": record["scenario"],
                "scenarioKind": record["scenarioKind"],
                "scenarioStatus": record["status"],
                "page": page,
                "route": route_for(page),
                "publicationStatus": (
                    "published-live-accepted" if accepted and page else
                    "accepted-no-page" if accepted else
                    "pending-scenario" if page else
                    "not-published"
                ),
                "coverage": record.get("coverage"),
                "evidence": record.get("evidence"),
                "currentEvidence": record.get("currentEvidence"),
                "legacyEvidence": record.get("legacyEvidence"),
            })

    system = []
    for index, record in enumerate(coverage.get("systemCapabilities", [])):
        validate_record(record, f"systemCapabilities[{index}]", root)
        system.append({
            "capability": record.get("capability"),
            "scenario": record["scenario"],
            "scenarioKind": record["scenarioKind"],
            "scenarioStatus": record["status"],
            "page": record.get("page"),
            "route": route_for(record.get("page")),
            "capabilityStatus": "live-accepted" if record["status"] == "live-accepted" else "not-live-accepted",
            "coverage": record.get("coverage"),
            "evidence": record.get("evidence"),
            "claimBoundary": record.get("claimBoundary"),
        })

    snapshot = release["developmentSnapshot"]
    result = {
        "schemaVersion": 1,
        "generatedFrom": [str(args.coverage), str(args.release)],
        "policy": {
            "commandInventoryIsNotPublicationTrigger": True,
            "commandPageRequiresLiveAcceptedScenario": True,
            "liveAcceptedDoesNotImplyReleased": True,
            "systemBoundaryNeverBecomesCommand": True,
        },
        "release": {
            "id": release["releaseId"],
            "status": release["status"],
            "sourceCommit": release["source"]["commit"],
            "capabilityAllowList": release.get("capabilityAllowList", []),
            "developmentSnapshot": snapshot,
        },
        "counts": {
            "scenarioRecords": len(routes) + len(system),
            "scenarioLiveAccepted": sum(r["scenarioStatus"] == "live-accepted" for r in routes + system),
            "commandPagesLiveAccepted": sum(r["publicationStatus"] == "published-live-accepted" for r in routes),
            "commandPagesPending": sum(r["publicationStatus"] == "pending-scenario" for r in routes),
            "acceptedCommandScenariosWithoutPage": sum(r["publicationStatus"] == "accepted-no-page" for r in routes),
            "systemCapabilitiesLiveAccepted": sum(r["capabilityStatus"] == "live-accepted" for r in system),
            "releaseLiveAccepted": snapshot["capabilitiesLiveAccepted"],
        },
        "routes": routes,
        "systemCapabilities": system,
    }
    rendered = json.dumps(result, indent=2) + "\n"
    output = (root / args.output).resolve()
    if args.check:
        if not output.is_file() or output.read_text() != rendered:
            raise SystemExit(f"stale publication manifest: {output}")
        print(f"publication manifest is current ({hashlib.sha256(rendered.encode()).hexdigest()[:12]})")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered)
    print(f"wrote {output} ({hashlib.sha256(rendered.encode()).hexdigest()[:12]})")


if __name__ == "__main__":
    main()
