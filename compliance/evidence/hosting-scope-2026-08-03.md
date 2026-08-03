# Hosting scope review — 2026-08-03

The selected host is `book.fountain.coach`, served from Hetzner Cloud through Caddy. The authoritative DNS record and
public HTTPS response were verified on 2026-08-03; the server serves the isolated Book root and a valid certificate.
This record intentionally contains no credentials, private host identifiers, or raw logs.

The publication declares no analytics, profiling, forms, accounts, payments, advertising, social embeds, or
non-essential storage. Operational request logging is limited by policy to three days and is not used for analytics.

The host-wide journald policy was then configured and verified as `MaxRetentionSec=3day` through the guarded secure-
publishing operation. Applying the policy reduced existing archived/active journal usage from 3.7 GB to 91.5 MB; no
separate vacuum command was run. Access-control review, backup/rollback evidence, incident-response ownership, and the
final controller/processor review for Hetzner remain open. The infrastructure observation is evidence for review, not
a legal or security certification.
