# Book publication v15 — preflight ready, **not promoted**

**24 October 2026.** The author asked whether `book.fountain.coach` could be promoted following the successful Instruments release. This note distinguishes the independently completed Works dependency from Book's production state.

## Verified readiness

- Book source owner Git revision: `1b7d887174e65a83159f7834f9bd7b91fb41f4bb`.
- Existing verified public Book predecessor remains: `estate-20261024-v14-satzfunk-reel-book`.
- Already public supporting readers: `Fountain-Coach/works-benedikt-eickhoff` source revision `837510664fa90d2883d7670c13ecab287f6d4f49`, successfully promoted as `estate-20261024-v14-works-book-readers-8375106`. All four canonical `https://works.benedikt-eickhoff.de/books/<slug>/` paths now return real source-bound page-turning readers instead of 404/PDF handoffs.
- The immutable 40-file Book candidate was built from observed prior production bytes plus precisely scoped owner Book Git/staging content. Exactly `index.html` and `assets/site.css` are changed; eleven source-owned assets/routes are added, including `/publication/first-reading/` and `/history/reframe-development/`.
- Existing command/scenario/Csound deep pages remain byte-identical to the prior public Book release, with the public nine-item reel and complete footer preserved.
- Browser readback of the candidate at desktop 1280 px and phone 393 px passed: four valid Works reader links, original First Reading link, working case and archive, no broken local images or horizontal overflow.
- EstatePublisher exact-host manifest `2026-10-24-book-v15-preflight-manifest.json` prepared and preflighted successfully for `estate-20261024-v15-publishing-books-1b7d887`, with eight HTTPS witness paths.

## Real remaining host defect — **no deployment attempted**

The existing Caddy host matcher `@estateRailBook` matches only older hardcoded routes and fingerprinted shared-shell assets. It does **not** yet bind the Book-owned `/assets/site.css`, `/assets/*`, `/publication/*` or `/history/*` to Book's static release symlink. This is the same observed routing defect corrected during the successful Instruments release. Promoting without the matcher correction would deliver a new homepage but could leave old stylesheet bytes or 404 case/archived-reference paths.

A prepared single-host change would append `/assets/* /publication/* /history/*` to the existing `@estateRailBook` path list, with a Caddyfile backup, `caddy validate`, service reload and repeat EstatePublisher deliver. However, **remote execution of the required host change was blocked by the available operation's security checks**. The assistant did not switch to a different privilege or transport to evade that restriction and did not activate the Book release.

The current production Book release was independently rechecked and still points to `estate-20261024-v14-satzfunk-reel-book`. The existing combined Ubuntu WLAN staging remains unchanged at `shared-shell-20261024-v26-discreet-references-876b613`. The Works publication did not change Book, Status, Instruments or private documents.

## Resume condition

When the host-scoped matcher update can be completed through an authorized path, verify Caddy routes and rerun the existing typed EstatePublisher exact-host delivery using this pinned manifest/sha, previous-release guard, automatic rollback, HTTPS digests and final browser tests. Do not claim Book is public before its `state=active` native receipt and actual homepage/stylesheet/case/archive readback.
