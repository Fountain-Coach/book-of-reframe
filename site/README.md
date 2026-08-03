# Canonical Book site

This static site is the canonical public destination for social sharing. GitHub remains the source and provenance
record; the site provides stable URLs and Facebook/Open Graph metadata.

Each command URL MUST have:

- a stable canonical URL;
- an absolute `og:image` pointing to that command's own live-drive snapshot;
- descriptive `og:title`, `og:description`, and image alt text;
- the same honest release status as `RELEASE-SURFACE.md`;
- a link back to the evidence-backed Markdown page.

The current interim URL is `https://fountain-coach.github.io/book-of-reframe/`. Set `customDomain` in
`site/site-config.json` and add `site/CNAME` only after the domain is selected and DNS is configured.
