# European publication compliance

The Book of Reframe is a static, evidence-backed technical publication. This file defines the release boundary for
the current publication and points to the machine-readable decision register in [`compliance/register.yaml`](compliance/register.yaml).

The register is a practical release control, not a legal opinion or a certification of every European or national law.
Every row records an applicability decision, official source, evidence, owner, review date, and remaining limits. A
`requires_review` row blocks publication. A `not_applicable` row requires a written rationale.

The live infrastructure audit verified DNS, HTTPS, Caddy, and the dedicated Book root. A guarded host operation now
enforces `MaxRetentionSec=3day` for journald. Access-control, backup/rollback, incident ownership, and the
controller/processor review remain operational/legal review items.

## Publisher facts recorded 3 August 2026

- Publisher: Benedikt Eickhoff, Einzelunternehmer, Wühlischstraße 8, 10245 Berlin, Deutschland.
- Contact: [mail@benedikt-eickhoff.de](mailto:mail@benedikt-eickhoff.de).
- Scope: free, development-only technical publication; not commercial, paid, e-commerce, or an e-book product.
- Processing surface: no accounts, forms, payments, advertising, analytics, cookies, social embeds, or non-essential
  browser storage.
- Hosting: Hetzner Cloud and Caddy; declared technical-log retention is three days for security and operations only.
- Editorial provenance: extensive AI assistance, reviewed and approved by Benedikt Eickhoff.
- Rights assertion: publication text, design, screenshots, and original assets are owned by Benedikt Eickhoff; no
  third-party material is intentionally included in the current scope.

## Current scope

The current projection has no accounts, forms, payments, user uploads, analytics, advertising, or embedded social/media
widgets. The production host, server logs, DNS/CDN configuration, manuscript excerpts, screenshots, AI-related claims,
and any future paid lane remain part of the review surface.

The publication must be rescanned when any of those facts change or when its audience, hosting, or Member State scope
changes. EU directives and national implementing laws must be checked for the jurisdictions in which Fountain Coach
operates or offers the publication.

## Release meaning

`GO` means the documented scope is internally consistent, evidence-backed, and ready for the recorded human/legal
review decision. It does not mean that automated checks replace qualified EU legal advice, a DPO decision, or national
regulatory interpretation.

Official reference starting points include the [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), [European Accessibility Act](https://eur-lex.europa.eu/eli/dir/2019/882/oj), [Digital Services Act guidance](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act), and [Digital Single Market copyright directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0790).
