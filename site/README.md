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
./open-local-preview.sh
```

This starts `dev-server.py` if needed and opens the URL in the system browser automatically. Use
`./open-local-preview.sh 4174` for a second preview port. Test the wide layout, a narrow mobile viewport, keyboard
focus, the skip link, and the Menu/Close navigation. Edit HTML, CSS, JavaScript, JSON, or image files and the local
preview reloads itself within roughly one second. The existing `/commands/commands/` route must remain reachable.
The reload script is injected only by `dev-server.py`; it is not part of the published HTML.

## Publication target

The fitting production hostname is proposed as `book.fountain.coach`. It is recorded in `site-config.json` for design
and metadata work, but DNS, Caddy, and deployment are not configured by this content repository change. Those are
separate secure-publishing operations requiring explicit confirmation and post-change DNS/TLS verification.

The page states that it is development/template content and makes no released-App claim.

## FCIS interface verification

FCIS-AX and FCIS-VRT are both required for site acceptance. The browser accessibility tree is the machine-readable
layer: landmarks, headings, links, buttons, accessible names, `aria-expanded` state, and keyboard actions are driven
and asserted semantically. Screenshots are the independent human/visual layer and are not used to infer accessibility
state.

```text
FCIS-AX Declaration
- Surfaces: home page, responsive navigation, command atlas route
- Custom-drawn views: none; HTML/CSS controls and content are used
- AX identifiers: semantic HTML, ARIA labels/states, and stable hrefs/data attributes
- AX-driven verification: integration `.codex/skills/book-of-reframe-site-acceptance`
- Known gaps: browser-dependent drive pending when no supported browser is available

FCIS-VRT:
  modes: [VRT-Render]
  baselines: site/evidence/vrt/ (manual/opt-in; first browser capture pending)
  gate: manual
  legacy-aliases: none
```
