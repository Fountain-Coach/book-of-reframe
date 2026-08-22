#!/usr/bin/env python3
"""Apply the reviewed Fountain Coach estate shell to generated Book routes."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "site"
FALLBACK_IMAGE = "https://book.fountain.coach/assets/book-estate-social.png"


def text(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def page_label(source: str, path: Path) -> str:
    match = re.search(r'<li[^>]*aria-current="page"[^>]*>(.*?)</li>', source, re.S)
    if match:
        return text(match.group(1))
    match = re.search(r"<h1[^>]*>(.*?)</h1>", source, re.S)
    return text(match.group(1)) if match else path.parent.name.replace("-", " ").title()


def section_for(path: Path) -> tuple[str, str] | None:
    parts = path.parts[:-1]
    if not parts:
        return None
    section = parts[0]
    return {
        "commands": ("Verified behavior", "commands/commands/"),
        "scenarios": ("Scenarios", "scenarios/"),
        "governance": ("Governance", "governance/default-semantic-manuscript-projection/"),
        "scenario-driven-development": ("Development method", "scenario-driven-development/"),
        "legal": ("Publication policy", "legal/"),
        "privacy": ("Publication policy", "privacy/"),
        "accessibility": ("Publication policy", "accessibility/"),
        "copyright": ("Publication policy", "copyright/"),
        "compliance": ("Publication policy", "compliance/"),
    }.get(section)


def prefix(path: Path) -> str:
    depth = len(path.relative_to(ROOT).parent.parts)
    return "../" * depth


def breadcrumbs(source: str, path: Path) -> str:
    label = page_label(source, path)
    current = f'<li aria-current="page">{html.escape(label)}</li>'
    middle = ''
    section = section_for(path)
    if section and section[0] != label:
        middle = f'<li><a href="{prefix(path) + section[1]}">{section[0]}</a></li>'
    return (f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>'
            f'<li><a href="https://fountain.coach/">Fountain Coach</a></li>'
            f'<li><a href="{prefix(path) or "./"}">Book</a></li>{middle}{current}</ol></nav>')


def estate_nav(path: Path) -> str:
    current = "Book"
    links = [
        ("Estate", "https://fountain.coach/", False),
        ("Book", prefix(path) or "./", True),
        ("Governance", "https://governance.fountain.coach/", False),
        ("Instruments", "https://instruments.fountain.coach/", False),
        ("Status", "https://status.fountain.coach/", False),
    ]
    items = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if active else '') + f'>{label}</a>'
        for label, href, active in links
    )
    return f'<nav class="estate-nav" aria-label="Fountain Coach publication estate">{items}</nav><button class="theme-button" type="button" data-theme-button aria-pressed="false">Theme: system</button>'


def footer(path: Path) -> str:
    root = prefix(path)
    return '''<footer class="footer">
      <p><strong>The Book of Reframe</strong> · human reference and evidence interpretation · <a href="https://fountain.coach/">Fountain Coach estate</a></p>
      <nav class="footer-estate" aria-label="Fountain Coach publications"><a href="https://fountain.coach/">Estate · identity</a><a href="''' + (root or './') + '''">Book · human reference</a><a href="https://governance.fountain.coach/">Governance · rules and authority</a><a href="https://instruments.fountain.coach/">Instruments · MIDI2 catalog</a><a href="https://status.fountain.coach/">Status · company and legal context</a></nav>
      <nav class="footer-legal" aria-label="Publication policy"><a href="''' + root + '''legal/">Book legal notices</a><a href="''' + root + '''privacy/">Book privacy</a><a href="''' + root + '''accessibility/">Accessibility</a><a href="''' + root + '''copyright/">Copyright</a><a href="''' + root + '''compliance/">EU compliance scope</a><a href="https://status.fountain.coach/unternehmen/">Official company context</a></nav>
      <p>Published public projection · Reframe runtime remains private · acceptance is not release.</p>
    </footer>'''


def apply(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    source = source.replace('href="../../GOVERNANCE-79.md"', 'href="https://github.com/Fountain-Coach/book-of-reframe/blob/main/GOVERNANCE-79.md"')
    label = page_label(source, path)
    source = re.sub(r'<meta name="theme-color"[^>]*>\s*', '', source)
    additions = (
        '  <meta name="color-scheme" content="light dark">\n'
        '  <meta name="fountain:publication-role" content="Human reference and evidence interpretation">\n'
        '  <meta name="fountain:publication-state" content="Published public projection">\n'
    )
    if 'fountain:publication-role' not in source:
        source = re.sub(r'(<link[^>]+rel=["\']canonical["\'][^>]*>)', additions + r'\1', source, count=1)
    canonical_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', source)
    canonical_url = canonical_match.group(1) if canonical_match else 'https://book.fountain.coach/'
    description_match = re.search(r'<meta name=["\']description["\'] content=["\']([^"\']*)', source)
    description = description_match.group(1) if description_match else f'{label}: published Book of Reframe human reference and evidence projection.'
    metadata = (
        f'  <meta property="og:title" content="{html.escape(label)} — The Book of Reframe">\n'
        f'  <meta property="og:description" content="{html.escape(description)}">\n'
        f'  <meta property="og:url" content="{html.escape(canonical_url)}">\n'
        f'  <meta name="twitter:title" content="{html.escape(label)} — The Book of Reframe">\n'
        f'  <meta name="twitter:description" content="{html.escape(description)}">\n'
    )
    if 'property="og:title"' not in source:
        source = source.replace('</head>', metadata + '</head>', 1)
    if 'property="og:description"' not in source:
        source = source.replace('</head>', f'  <meta property="og:description" content="{html.escape(description)}">\n</head>', 1)
    if 'property="og:url"' not in source:
        source = source.replace('</head>', f'  <meta property="og:url" content="{html.escape(canonical_url)}">\n</head>', 1)
    if 'name="twitter:title"' not in source:
        source = source.replace('</head>', f'  <meta name="twitter:title" content="{html.escape(label)} — The Book of Reframe">\n</head>', 1)
    if 'name="twitter:description"' not in source:
        source = source.replace('</head>', f'  <meta name="twitter:description" content="{html.escape(description)}">\n</head>', 1)
    if 'property="og:image"' not in source:
        source = source.replace('</head>', f'''  <meta property="og:image" content="{FALLBACK_IMAGE}">
  <meta property="og:image:alt" content="Fountain Coach publication estate illustration for {html.escape(label)}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{FALLBACK_IMAGE}">
</head>''', 1)
    if 'property="og:image:width"' not in source:
        source = source.replace('</head>', '  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n</head>', 1)
    if 'name="twitter:image"' not in source:
        source = source.replace('</head>', f'  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:image" content="{FALLBACK_IMAGE}">\n</head>', 1)
    if 'application/ld+json' not in source:
        canonical = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', source)
        canonical_url = canonical.group(1) if canonical else 'https://book.fountain.coach/'
        structured = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage",'
                      f'"name":{__import__("json").dumps(label)},"url":{__import__("json").dumps(canonical_url)},'
                      '"publisher":{"@type":"Organization","name":"Fountain Coach","url":"https://fountain.coach/",'
                      '"logo":"https://book.fountain.coach/assets/fountain-coach-logo.png"}}</script>\n')
        source = source.replace('</head>', structured + '</head>', 1)
    if 'data-theme-toggle' not in source:
        source = source.replace('data-theme-button', 'data-theme-toggle')
    estate = estate_nav(path).replace('data-theme-button', 'data-theme-toggle')
    source = re.sub(
        r'(<div class="nav-shell">.*?)(</div>)<nav class="estate-nav"[^>]*>.*?</nav><button class="theme-button".*?</button></header>',
        lambda match: match.group(1) + estate + match.group(2) + '</header>',
        source, count=1, flags=re.S)
    source = re.sub(r'<nav class="estate-nav"[^>]*>.*?</nav><button class="theme-button".*?</button>', estate, source, count=1, flags=re.S)
    if 'data-theme-toggle' not in source:
        source = source.replace('</header>', f'{estate_nav(path).replace("data-theme-button", "data-theme-toggle")}</header>', 1)
    source = re.sub(r'<(?:nav|div) class="breadcrumbs"[^>]*>.*?</(?:nav|div)>', breadcrumbs(source, path), source, count=1, flags=re.S)
    if '<nav class="breadcrumbs"' not in source:
        source = re.sub(r'(<main\b[^>]*>)', r'\1\n    ' + breadcrumbs(source, path), source, count=1)
    source = re.sub(r'<footer\b.*?</footer>', footer(path), source, count=1, flags=re.S)
    path.write_text(source, encoding="utf-8")


def main() -> None:
    paths = [path for path in ROOT.rglob("*.html") if not path.name.startswith("._")]
    for path in sorted(paths):
        apply(path)
    print(f"updated {len(paths)} Book routes")


if __name__ == "__main__":
    main()
