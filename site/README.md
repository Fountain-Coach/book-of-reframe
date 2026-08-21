# Canonical Book site

This static site is the canonical public destination for social sharing. GitHub remains the source and provenance
record; the site provides stable URLs and Facebook/Open Graph metadata. The public/private boundary is defined in
[`../PUBLICATION-POLICY.md`](../PUBLICATION-POLICY.md) and governance Chapter 44.

Each command URL MUST have:

- a stable canonical URL;
- an absolute `og:image` pointing to that command's own live-drive snapshot;
- descriptive `og:title`, `og:description`, and image alt text;
- the same honest release status as `RELEASE-SURFACE.md`;
- a link back to the evidence-backed Markdown page.

Facebook/Twitter preview contract:

- `og:url`, `og:title`, `og:description`, `og:site_name`, and `og:image` are absolute HTTPS values;
- `og:image:width` and `og:image:height` match the published PNG;
- the Fountain Coach organization logo is available as the local favicon, Apple touch icon, and structured publisher
  logo;
- command previews use the command's own evidence snapshot, never the generic homepage brand image.

The current home page is a responsive repository-derived projection of the publication README, command atlas,
capability atlas, release surface, provenance, and legal publication boundary. It keeps the development snapshot
visible without presenting it as a released App.

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

Before publication, compile scenario acceptance first, then regenerate the numeric/status projection:

```sh
python3 scripts/build-publication-manifest.py
python3 scripts/build-publication-manifest.py --check
```

The manifest is the route gate: a command page is eligible only for a named `live-accepted` scenario. An accepted
scenario without a page is retained as `accepted-no-page`; the named release surface remains independent.

```sh
python3 build-site-data.py
```

This writes `site-data.json`, which supplies the command, capability, live-acceptance, snapshot-date, and release-status
values used by the overview and command pages. The HTML keeps reviewed fallback values so the page remains legible if
JavaScript is unavailable.

## Publication target

The production hostname is `book.fountain.coach`. DNS, Caddy, and HTTPS have been verified by the secure-publishing
workflow. Legal publication remains separately gated by `compliance/register.yaml`; infrastructure verification does
not by itself constitute legal clearance.

The page states that it is a development snapshot and makes no released-App claim.

## FCIS interface verification

FCIS-AX and FCIS-VRT are both required for site acceptance. The browser accessibility tree is the machine-readable
layer: landmarks, headings, links, buttons, accessible names, `aria-expanded` state, and keyboard actions are driven
and asserted semantically. Screenshots are the independent human/visual layer and are not used to infer accessibility
state.

When the ChatGPT Browser connector is not exposed, acceptance uses the repository's deterministic Chrome CDP runner
instead. It launches an isolated Chrome profile, reads `Accessibility.getFullAXTree`, performs semantic DOM actions,
and captures fixed-viewport PNGs; it does not require a ChatGPT extension or a signed-in browser session:

```sh
python3 /path/to/midi2-gpu-fabric/.codex/skills/book-of-reframe-site-acceptance/scripts/cdp_site_acceptance.py \
  --site-root "$PWD"
```

```text
FCIS-AX Declaration
- Surfaces: home page, responsive navigation, command atlas route
- Custom-drawn views: none; HTML/CSS controls and content are used
- AX identifiers: semantic HTML, ARIA labels/states, and stable hrefs/data attributes
- AX-driven verification: integration `.codex/skills/book-of-reframe-site-acceptance`
- Known gaps: requires a locally installed Chromium-family browser; the ChatGPT Browser connector is optional

FCIS-VRT:
  modes: [VRT-Render]
  baselines: site/evidence/vrt/ (manual/opt-in; CDP captures under local-cdp/)
  gate: manual
  legacy-aliases: none
```
