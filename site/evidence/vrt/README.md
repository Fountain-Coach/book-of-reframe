# Book site VRT-Render baselines

This directory is reserved for reviewed FCIS-VRT-Render screenshots captured from the local site preview.

Required baseline states:

- `home-desktop-light-1440x1000.png`
- `home-mobile-light-390x844.png`
- `home-mobile-menu-open-light-390x844.png`

The first local browser-backed capture is recorded under `local-cdp/`, using Google Chrome via the repository's
isolated Chrome DevTools Protocol runner. The ChatGPT Browser connector is optional for this evidence. Do not
fabricate or promote a baseline from source inspection. Each image must be accompanied by the
source commit, browser/runtime, viewport, route, theme, and interaction state in the integration `PLANS.md` record.
