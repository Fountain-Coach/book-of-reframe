# Accessibility declaration

**Status / Stand: 3 August 2026**  
The current site is a free technical publication, not a paid e-book or e-commerce service. EAA applicability is
recorded as not applicable for this scope; this is a publisher classification, not legal advice or a conformity
certificate.

Die aktuelle Website ist eine kostenfreie technische Publikation, kein kostenpflichtiges E-Book und kein
E-Commerce-Dienst. Die Anwendbarkeit des EAA ist für diesen Umfang als nicht anwendbar dokumentiert; dies ist eine
Einordnung des Herausgebers und keine Rechtsberatung oder Konformitätsbescheinigung.

FCIS-AX is the semantic authority and FCIS-VRT is the visual authority for this web publication.

- **Surfaces:** home page, `/commands/commands/` command atlas, and `/scenarios/` public scenario reference.
- **Custom-drawn views:** none; the site uses semantic HTML, CSS, and ordinary browser controls.
- **AX identifiers:** stable `id`, `data-*`, and ARIA attributes on the skip link, navigation, menu button, headings,
  breadcrumbs, evidence image, and related records.
- **AX-driven verification:** `.codex/skills/book-of-reframe-site-acceptance/scripts/cdp_site_acceptance.py`, using
  the browser accessibility tree and semantic DOM actions.
- **VRT-Render evidence:** `site/evidence/vrt/local-cdp/`, with desktop, mobile, and mobile-menu-open baselines.
- **Interaction behavior:** keyboard skip navigation, named landmarks, labeled mobile menu state, visible focus,
  reduced-motion support, and a high-contrast override are required.
- **Maintainer/public split:** the public scenario reference explains the maintainer workflow without exposing the
  role-gated maintainer snapshot or private runtime procedures.
- **Known limits:** this declaration is an engineering record, not a legal conformity assessment; production hosting
  and any future paid/e-book service require a fresh scope review.
