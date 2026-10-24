#!/usr/bin/env python3
"""Source-owned semantic first page for The Book of Reframe.

Composition at authoring time only; preserves actual technical record sections,
does not mint a manuscript, a Bookshelf edition or a released App.
"""
from pathlib import Path
import argparse, re

def extract(source: str, identifier: str) -> str:
    m = re.search(r'<section\s+id="' + re.escape(identifier) + r'"\b[^>]*>.*?</section>', source, re.S)
    if not m:
        # Attribute order differs between published and authoring source.
        m = re.search(r'<section\b(?=[^>]*\bid="' + re.escape(identifier) +
                      r'")[^>]*>.*?</section>', source, re.S)
    if not m:
        raise ValueError("Missing approved record: " + identifier)
    return m.group(0)

def render_main(source: str) -> str:
    # Owner Git carries the reviewed exact history and quantitative facts.
    appendix = "\n".join(extract(source, key) for key in ("scope", "evidence", "governance"))
    return '''<main class="layout book-semantic" id="main">
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="https://fountain.coach/">Fountain Coach</a></li><li aria-current="page">The Book of Reframe</li></ol></nav>
<article aria-labelledby="page-title">
<section class="book-frontispiece" aria-labelledby="page-title">
  <div class="book-identity"><img src="assets/book-open.svg" width="48" height="48" alt="" aria-hidden="true"/><span>The Book of Reframe</span></div>
  <div class="book-opening">
    <div class="book-opening-copy">
      <div class="eyebrow">An account of how Reframe is made</div>
      <h1 id="page-title">The Book<br>of Reframe</h1>
      <p class="book-deck">How a source becomes a reading, a governed action, an observed result—and, when admitted, a publication.</p>
      <p class="book-explanation">This is a book <em>about</em> Reframe. It is not the Reframe Bookshelf, a substitute for a manuscript, or a promise that development features have shipped.</p>
      <p class="book-begin"><a href="scenario-driven-development/">Begin reading: the method <span aria-hidden="true">→</span></a></p>
    </div>
    <aside class="book-marginalia" aria-label="Publication context">
      <span class="eyebrow">Public documentation</span>
      <strong>A witnessed development account</strong>
      <p>The Book describes work and its evidence. The app, its Bookshelf, individual manuscripts and composed editions each retain their own authority.</p>
      <p class="book-snapshot-note">The quantitative records below refer to the <time datetime="2026-08-15">15 August 2026</time> reviewed snapshot—not today's Reframe release state.</p>
    </aside>
  </div>
</section>
<section class="book-toc section" id="contents" aria-labelledby="contents-title">
  <div class="eyebrow">Contents</div>
  <h2 id="contents-title">Four ways into the work.</h2>
  <p class="book-section-intro">Read in sequence, or enter at the evidence that interests you. These are existing public pages, not invented Bookshelf volumes.</p>
  <ol class="book-toc-list">
    <li><a href="scenario-driven-development/"><span class="book-ordinal">I</span><span><strong>The method</strong><small>From a source to a governed scenario and its criteria</small></span><span aria-hidden="true" class="book-chevron">↗</span></a></li>
    <li><a href="scenarios/"><span class="book-ordinal">II</span><span><strong>The journeys</strong><small>Which scenarios have evidence, and what it does not yet establish</small></span><span aria-hidden="true" class="book-chevron">↗</span></a></li>
    <li><a href="commands/commands/"><span class="book-ordinal">III</span><span><strong>The observable behavior</strong><small>A dated command inventory, not a list of shipped product features</small></span><span aria-hidden="true" class="book-chevron">↗</span></a></li>
    <li><a href="csound-teatro/"><span class="book-ordinal">IV</span><span><strong>Sound in space</strong><small>Csound, Teatro, Ear and the boundary between score and hearing</small></span><span aria-hidden="true" class="book-chevron">↗</span></a></li>
  </ol>
</section>
<section class="book-terms section" id="distinctions" aria-labelledby="distinctions-title">
  <div class="eyebrow">Terms that must remain distinct</div>
  <h2 id="distinctions-title">Book is not Bookshelf.</h2>
  <div class="book-term-grid">
    <div><h3>This Book</h3><p>A reviewed, public narrative about Reframe's development. Its claims remain tied to dated records and checked evidence.</p></div>
    <div><h3>A manuscript</h3><p>An authored source with its own identity and custody. Having a file, a PDF or a cover does not make it an admitted reading edition.</p></div>
    <div><h3>The Reframe Bookshelf</h3><p>The writer's collection of explicitly admitted works and editions. Fountain Press composes their measured reading pages; this website does not grant admission.</p></div>
  </div>
  <p class="book-sidenote">A separately published reading, such as <a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">First Reading</a>, is another kind of object—not a chapter of this Book.</p>
</section>
<section class="book-method section" id="method" aria-labelledby="method-title">
  <div class="eyebrow">The underlying method</div>
  <h2 id="method-title">Five acts, five different claims.</h2>
  <ol class="book-act-list">
    <li><strong>Source</strong><span>Identify the material and its provenance.</span></li>
    <li><strong>Scenario</strong><span>Name what must happen and what would count as evidence.</span></li>
    <li><strong>Implement</strong><span>Build bounded behavior against that contract.</span></li>
    <li><strong>Accept</strong><span>Witness actual results, interfaces and persistence.</span></li>
    <li><strong>Publish</strong><span>Release only the separately reviewed public projection.</span></li>
  </ol>
</section>
<section class="book-reference section" id="reference" aria-labelledby="reference-title">
  <div class="eyebrow">Reference / historical edition</div>
  <h2 id="reference-title">What the records establish.</h2>
  <p>These are the retained, checked technical records from the 15 August 2026 Book snapshot. They are useful evidence, not a measure of current product availability.</p>
  <details class="book-appendix">
    <summary>Open the quantitative records and evidence notes <span aria-hidden="true">⌄</span></summary>
    <div class="book-appendix-content">
''' + appendix + '''
    </div>
  </details>
  <p class="book-colophon">A Fountain Coach publication projection. The current Reframe runtime and the author's Bookshelf remain independent of this static Book.</p>
</section>
</article>
</main>'''

def apply(page: Path, main: str) -> None:
    s = page.read_text()
    m = re.search(r'<main\b[^>]*>.*?</main>', s, re.S)
    if not m:
        raise ValueError("No unique editable main in " + str(page))
    assert len(re.findall(r'<main\b', s)) == 1
    s = s[:m.start()] + main + s[m.end():]
    s = s.replace('href="#start"', 'href="#contents"')
    s = s.replace('https://book.fountain.coach/assets/commands-live-fullcatalog-20260803.png',
                  'https://book.fountain.coach/assets/book-reframe-social.png')
    s = s.replace('Reframe showing the live command catalog',
                  'The Book of Reframe: standard open-book symbol and publication title')
    s = s.replace('content="1672"', 'content="1200"').replace('content="941"', 'content="630"')
    s = re.sub(r'<title>[^<]*</title>', '<title>The Book of Reframe — an account of reading and evidence</title>', s, count=1)
    s = s.replace('The public development story and method of Reframe: source, scenario contract, implementation, acceptance, and publication.',
                  'A public account of Reframe: source, reading, governed action, witnessed evidence and publication.')
    s = s.replace('A clear starting point for understanding Reframe, its verified behavior, scenario evidence, and release boundary.',
                  'A public account of Reframe: source, reading, governed action, witnessed evidence and publication.')
    page.write_text(s)

def main():
    a = argparse.ArgumentParser()
    a.add_argument('--source', type=Path, required=True)
    a.add_argument('--target', type=Path, required=True)
    args = a.parse_args()
    source = args.source.read_text()
    rendered = render_main(source)
    apply(args.target, rendered)
    print('SEMANTIC_BOOK_MAIN_READY', args.target)

if __name__ == "__main__":
    main()
