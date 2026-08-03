# Canonical Book site

This static site is the canonical public destination for social sharing. GitHub remains the source and provenance
record; the site provides stable URLs and Facebook/Open Graph metadata.

Each command URL MUST have:

- a stable canonical URL;
- an absolute `og:image` pointing to that command's own live-drive snapshot;
- descriptive `og:title`, `og:description`, and image alt text;
- the same honest release status as `RELEASE-SURFACE.md`;
- a link back to the evidence-backed Markdown page.

The current home page is a responsive development/template specimen using lorem ipsum content so its reading rhythm
and navigation can be tested before real command stories are projected.

## Local rinse-and-wash

From this directory:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173/` and test the wide layout, a narrow mobile viewport, keyboard focus, the skip link, and
the Menu/Close navigation. The existing `/commands/commands/` route must remain reachable.

## Publication target

The fitting production hostname is proposed as `book.fountain.coach`. It is recorded in `site-config.json` for design
and metadata work, but DNS, Caddy, and deployment are not configured by this content repository change. Those are
separate secure-publishing operations requiring explicit confirmation and post-change DNS/TLS verification.

The page states that it is development/template content and makes no released-App claim.
