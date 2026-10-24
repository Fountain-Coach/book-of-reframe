# Book v15 — public publication and acceptance

**24 October 2026 — ACTIVE.** Author request: "fix it and promote!" for `https://book.fountain.coach/`. This record follows the previously preflighted and held Book v15 static publication candidate. Book was published only after the demonstrably missing Book-only Caddy route was repaired and the Works-owned readers had been independently released.

## Authorities and bounded scope

- **Book source owner:** Fountain-Coach/book-of-reframe; content revision **`1b7d887174e65a83159f7834f9bd7b91fb41f4bb`**. Subsequent documentation commits do not change published bytes.
- **Previously published production:** `estate-20261024-v14-satzfunk-reel-book`, observed by public HTTPS and original immutable release inventory; retained as rollback.
- **New typed public release:** **`estate-20261024-v15-publishing-books-1b7d887`**, 40 complete static files.
- **Native publication authority:** existing EstatePublisherSSHDelivery CLI (SSH, rsync, digest-bound immutable release, atomic symlink, HTTPS readback). Native receipt: [Book v15 active public receipt](2026-10-24-book-v15-public-receipt.json), `state=active`, `activated=true`, eight independently matched HTTPS witnesses.
- **Supporting source-owned readers:** Works, release `estate-20261024-v14-works-book-readers-8375106`; original Works source commit `837510664fa90d2883d7670c13ecab287f6d4f49`. The four `https://works.benedikt-eickhoff.de/books/<slug>/` addresses were independently verified publicly before Book's promotion, with live desktop two-page and mobile single-page page-turning acceptance. Works remains off the estate reel and owns source PDFs, credits and facsimile reader content.

## One host-specific Caddy fix — independent of deployment

The production Caddy `@estateRailBook` matcher previously lacked Book's release-owned assets and new editorial routes. Its prior bytes were pinned to SHA-256 `bc2e60820fe9d77ee875a688e3c7a46a573bd2619be28c2e4db1292f4c5126cc`.

Using the existing authorized SSH transport, the accepted one-line delta adds exactly `/assets/* /publication/* /history/*` to the existing `@estateRailBook` path list restricted by `host book.fountain.coach`. All other Caddy matcher lines are byte-identical. The independently read and constructed Caddy candidate was transferred as a Caddyfile artifact, `caddy validate` passed, the original was copied to `/etc/caddy/Caddyfile.before-book-reading-routes-20261024`, the validated file was moved into place, and `systemctl reload caddy` succeeded. Active configuration SHA-256 is `277203a076bda8a3a1ff518d2efeb754c2dfec2554b647919e1c394fa018f110`. The backup remains available.

No new DNS, SSH account, helper, daemon, GitHub CI or security ceremony was created. Other host matchers were untouched.

## Public release, eight independent byte witnesses

The candidate was composed from the independently observed Book production release with only `index.html` and `assets/site.css` changed, and eleven new source-owned static case/history/social/book assets added. Existing technical deep pages, shared nine-item reel and footer were preserved. The pinned exact-host `EstatePublisher` manifest passed preflight both before and after the Caddy correction. The publisher then activated Book v15 with a typed active receipt and eight exact public HTTPS SHA-256 matches:

| Published path | SHA-256 |
| --- | --- |
| `/index.html` | `85330584e7cf19457a736f50416aeb1a3169a4c053a30f0e059b790bd24373f5` |
| `/assets/site.css` | `8af1b527ff56cf2f6da9b60e699f64495ba3e40c917a525d70f0d4c7353f06e0` |
| `/assets/book-publishing-social.png` | `63967dd2ed58318efe7535a2c65d229d9baa8af271b0234156fce85845d83c15` |
| `/assets/book-open.svg` | `3e3379d4470415ee6a159c9c3a266a18922a722b4dfac9b9e7240d4a8628d86c` |
| `/publication/first-reading/index.html` | `3aaaa023ae8f8e9e991e52738725d0cd58f97f8aa5e9b923d74af5ebdd60ceae` |
| `/history/reframe-development/index.html` | `98663c8e3a6c9d363ecc051cef00d627e6b56cc3f66b3efec9a68fc6aacae913` |
| `/commands/commands/index.html` | `a2b790b2b5a13414b1fabce4e465c464a4de8d3abd73ff2904ea04a9bf02deab` |
| `/csound-teatro/index.html` | `07b7595c3061ac2e96a0eb27874d524e3e86aaf2f4d47d03f38` |

A separate `curl` and local candidate SHA-256 comparison, using a cache-busting query, matched all eight. The exact public release symlink and retained v14 directory were independently inspected. Caddy remained active.

## Actual browser observation and no-broad-estate delta

Chromium headless browser accessed **the actual public HTTPS** site at desktop 1280×900 and mobile 393×852, cache disabled. The homepage title "A book, published." appeared with four correctly resolving Works book-reader links, an intact nine-item editorial reel including Instruments/Satzfunk, legal-footer Status link, no image loading failures, no JavaScript page errors and no horizontal overflow. `/publication/first-reading/` and `/history/reframe-development/` both opened and retained the shared footer at both widths.

Works v14 and Instruments v16 current symlinks were separately verified unchanged, as was the owner-WLAN canonical combined staging v26; public Status and Instruments roots continued serving HTTPS 200. No private Jobcenter/legal documents were included. A published facsimile reader is not a semantic, reflowable Fountain Press manuscript reader or a new private Reframe Bookshelf admission. Native Safari/iPad-specific acceptance was **not** carried out; Chrome desktop and mobile viewport checks are recorded as such.

**Result:** Book's editorial/publishing entrance and four actual public book-reader links are operational on production; previous Book v14 release is preserved as rollback.
