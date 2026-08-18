---
name: book-of-reframe-social-publish
description: Prepare and, only with explicit confirmation, publish a verified Book of Reframe command as a Facebook post using its own GUI snapshot as the image and an honest story-teasing caption. Use for social promotion of command pages or live command evidence.
---

# Book of Reframe Social Publish

 Package one verified Book of Reframe command page for Facebook. The page's leading GUI snapshot is the only image
 source; the caption is a short writer-facing teaser grounded in the page and its evidence. The Facebook URL is always
 the full Book page; the snapshot is its `og:image`, never the image asset itself. This skill publishes an
external post only after a separate explicit confirmation naming the Facebook destination.

## Authority and safety

- Read the Book maintenance skill, release manifest, command page, and evidence manifest first.
- The command page must pass `verify_command_pages.py`; its evidence must be `live-accepted` with AX, window-ID, and
  FountainStore proof. Do not package a catalog screenshot for a different command.
- If the release manifest says `no-released-build` or `development-snapshot`, the caption MUST say this is a
  development/evidence preview. Never imply that the command is shipped.
- Do not copy prompts, manuscript text, private store data, local paths, access tokens, or internal execution IDs into
  the caption. Use the public Book URL and sanitized evidence links only.
- Creating a package is local and reversible. Posting is an external side effect and requires explicit confirmation,
  a named Facebook Page, and credentials supplied through the environment or an approved connector; never ask for or
  print a token.

## Workflow

1. Resolve the command page and its evidence manifest. Confirm the first non-empty page line is the command's own
   alt-texted image and that the referenced file exists.
2. Run `scripts/build_facebook_post.py <book-root> <command-page> --teaser "..." --book-url "..."`.
   `--book-url` must be the full HTTPS Book page URL, not `/assets/`, `/social/`, a raw image URL, or a GitHub file URL.
   Use the canonical site URL from `site/site-config.json` (the interim GitHub Pages URL until a custom domain is
   selected), not a raw GitHub file URL.
3. Inspect the generated `facebook-post.json` and the image visually. The package must contain `image`, `caption`,
   `publicUrl` naming the full Book page,
   `command`, `evidence`, `releaseStatus`, and `externalPublish: false`.
4. Edit the teaser only from verified facts. A good caption has: a hook about the writer's problem, the command's
   visible act/result, an honest evidence or development-status line, and the public Book link.
5. For explicit publishing, recheck the destination Page, caption, image, release status, and consent. Use the approved
   Facebook/Meta connector or Graph API; upload the image as the post image and retain the returned post ID in a
   private operator record, never in the public Book.
6. Record only sanitized publication provenance in the Book or integration `PLANS.md`: command, snapshot, public URL,
   destination Page name, date, and post URL/ID if the user authorizes it.

## Output contract

The package is a directory containing:

- `facebook-post.json` — deterministic post metadata and caption;
- the copied GUI snapshot image;
- `README.md` — review note stating the evidence and whether external publishing occurred.

The package is not proof of posting. Only the external platform's returned post record proves publication.
