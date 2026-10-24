#!/usr/bin/env python3
"""Source-owned Book publication front door; render complete checked-in static routes.

Read the existing source-owned shell, and replace only bounded editorial semantics.
The old development manual is preserved under a dated historical URL, not deleted.
"""
from pathlib import Path
import argparse
import re

HOME_MAIN = '''<main class="layout publishing-book" id="main">
  <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="https://fountain.coach/">Fountain Coach</a></li><li aria-current="page">Book</li></ol></nav>
  <article>
    <header class="publish-opening">
      <div class="book-identity"><img src="assets/book-open.svg" width="40" height="40" alt="" aria-hidden="true"><span>Fountain Coach · Book</span></div>
      <p class="eyebrow">The publishing of a readable work</p>
      <h1 id="page-title">A book,<br><em>published.</em></h1>
      <p class="publish-lead">Publishing makes an authored work independently encounterable without losing the identity of its source.</p>
      <p class="publish-intro">A book is not simply a file, a series of pages, or a software feature. It is a work carried into a readable edition—and a relationship whose authorship, composition and public release can be examined.</p>
      <nav class="publish-contents" aria-label="This publication">
        <a href="#reading">01 · Encounter a work</a>
        <a href="#making">02 · Follow its making</a>
        <a href="#witness">03 · Examine the witness</a>
      </nav>
    </header>
    <section id="reading" class="publish-section publish-reading" aria-labelledby="reading-title">
      <div class="eyebrow">01 · The published work</div>
      <div class="reading-display">
        <div class="reading-explanation">
          <p class="publish-kicker">A real edition, not an illustration</p>
          <h2 id="reading-title">First Reading<br><i>— Solstice</i></h2>
          <p>Thirty selected works with forty-one original images: that is how the edition introduces itself. The writing has its own authorship, original source pages and public reading address.</p>
          <p>The correct first encounter is the actual book. Its pages and reading experience remain at their source-owned address, not reproduced by this explanatory site.</p>
          <p class="publish-primary-action"><a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">Open the actual reading <span aria-hidden="true">↗</span></a></p>
          <p class="publish-fine">Benedikt Eickhoff · Fountain Coach · an authored public edition</p>
        </div>
        <aside class="reading-record" aria-label="Edition identity">
          <span class="reading-record-index">AN AUTHORED EDITION</span>
          <strong>First<br>Reading.</strong>
          <span class="reading-record-origin">Solstice</span>
          <span class="reading-record-rule"></span>
          <span class="reading-record-note">Actual book: <a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">works.benedikt-eickhoff.de</a></span>
          <small>This is a textual identification of the public edition, not a substitute cover, screenshot or newly admitted work.</small>
        </aside>
      </div>
      <p class="publish-afterword">Continue with its <a href="publication/first-reading/">publication case and source witness <span aria-hidden="true">→</span></a>.</p>
    </section>
    <section id="making" class="publish-section" aria-labelledby="making-title">
      <div class="eyebrow">02 · The making</div>
      <h2 id="making-title">What changes—and what must not.</h2>
      <p class="publish-section-lead">Publication is a sequence of accountable decisions. The source remains the source; every later projection has its own job.</p>
      <ol class="publish-process">
        <li><span class="publish-number">I</span><div><h3>The source</h3><p>Writing, original images, attribution and revision are identifiable before composition.</p></div></li>
        <li><span class="publish-number">II</span><div><h3>The edition</h3><p>An author admits a particular selection and order. A candidate or archived file does not become an admitted book by appearing in a folder.</p></div></li>
        <li><span class="publish-number">III</span><div><h3>The reading</h3><p>Fountain Press Linotype gives source-faithful material its measured leaves, contents and navigation. Reframe's private Bookshelf admission remains a separate writer action.</p></div></li>
        <li><span class="publish-number">IV</span><div><h3>The publication</h3><p>The publisher authorizes a public route and release; the deployed edition can then be independently visited and inspected.</p></div></li>
      </ol>
    </section>
    <section id="witness" class="publish-section" aria-labelledby="witness-title">
      <div class="eyebrow">03 · The witness</div>
      <h2 id="witness-title">What can we actually verify?</h2>
      <p class="publish-section-lead">A visible book and a successful website request are evidence of something specific, not of everything in the publication chain.</p>
      <div class="publish-witness-grid">
        <div><span>Observed</span><h3>The reading opens</h3><p>First Reading and a linked original source-entry route both returned HTTP 200 on 24 October 2026. That independently establishes publicly reachable routes.</p><a href="publication/first-reading/">Inspect the case <span aria-hidden="true">↗</span></a></div>
        <div><span>Declared by the edition</span><h3>Its contents and attribution</h3><p>The public book identifies its author, edition and selection of thirty works with forty-one original images. Those statements belong to the edition itself.</p><a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">See the original <span aria-hidden="true">↗</span></a></div>
        <div><span>Separate authority</span><h3>Admission and delivery</h3><p>Fountain Press composition, Reframe Bookshelf membership and EstatePublisher release receipts require their own evidence; this page neither issues nor fabricates them.</p><a href="https://github.com/Fountain-Coach/fountain-press">Read the Press contract <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>
    <section class="publish-historical" aria-labelledby="historic-title">
      <div class="eyebrow">Dated technical reference</div>
      <h2 id="historic-title">The earlier Book of Reframe.</h2>
      <p>The former development manual records commands, scenarios, GUI observations and the August 2026 acceptance snapshot. It remains available as a historical technical record. It is not the current reading sequence or an admitted Linotype book.</p>
      <a href="history/reframe-development/">Open the historical reference <span aria-hidden="true">↗</span></a>
    </section>
  </article>
</main>'''

CASE_MAIN = '''<main id="main" class="layout publishing-book publication-case">
  <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="../../">Book</a></li><li aria-current="page">First Reading · publication case</li></ol></nav>
  <article>
    <header class="publish-case-head">
      <div class="eyebrow">Publication case · 01</div>
      <h1>First Reading:<br><em>the work and its witness.</em></h1>
      <p class="publish-lead">Begin with a book that is actually published. Follow one source-entry relation, then distinguish what the reader observes from what the edition declares.</p>
      <p class="publish-primary-action"><a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">Enter the published edition <span aria-hidden="true">↗</span></a></p>
    </header>
    <section class="publish-section" aria-labelledby="case-source">
      <div class="eyebrow">01 · Authored source</div>
      <h2 id="case-source">The original is still addressable.</h2>
      <p>Within the published edition, <i>Anweisung an den Schmerz</i> retains a link back to its source-labelled entry. The reading is not presented as an untraceable new text.</p>
      <p><a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/entries/2025-12-22-anweisung-an-den-schmerz/?standalone=1">Open the source-labelled entry <span aria-hidden="true">↗</span></a></p>
      <p class="publish-fine">Source ownership and other provenance evidence require examination at the original domain or <a href="https://github.com/Fountain-Coach/works-benedikt-eickhoff">its owning repository</a>. The presence of a source link does not itself establish a complete rights audit.</p>
    </section>
    <section class="publish-section" aria-labelledby="case-reading">
      <div class="eyebrow">02 · Composed reading</div>
      <h2 id="case-reading">The edition is an encounter.</h2>
      <p>The live <i>First Reading — Solstice</i> site gives the selection a cover, an ordered book, navigation and an actual reader. Its own cover identifies thirty works and forty-one original images. Those are edition declarations, not statistics generated by this documentation site.</p>
      <p><a href="https://works.benedikt-eickhoff.de/solstice/editions/first-reading/">Read First Reading <span aria-hidden="true">↗</span></a> · <a href="https://github.com/Fountain-Coach/fountain-press">Understand the Linotype composition contract <span aria-hidden="true">↗</span></a></p>
    </section>
    <section class="publish-section" aria-labelledby="case-evidence">
      <div class="eyebrow">03 · Independent witness</div>
      <h2 id="case-evidence">Evidence with its limits intact.</h2>
      <dl class="case-facts">
        <div><dt>Observed, 24 October 2026</dt><dd>Public book route: HTTP 200. One original-entry standalone route: HTTP 200.</dd></div>
        <div><dt>Declared in the actual edition</dt><dd>Benedikt Eickhoff; First Reading — Solstice; thirty works; forty-one original images.</dd></div>
        <div><dt>Documented ownership</dt><dd><a href="https://github.com/Fountain-Coach/works-benedikt-eickhoff">Works source repository</a>; <a href="https://github.com/Fountain-Coach/fountain-press">Fountain Press composition software</a>.</dd></div>
        <div><dt>Not inferred</dt><dd>No automatic Reframe Bookshelf admission, original Store transaction, third-party rights clearance, current app release, or new EstatePublisher typed receipt is established by these two HTTP checks.</dd></div>
      </dl>
    </section>
    <footer class="publish-case-return"><a href="../../">← Return to Book · publishing</a></footer>
  </article>
</main>'''

HISTORY_NOTICE = '''<div class="history-status" role="note"><strong>Historical Reframe development reference · August 2026</strong><p>This archived technical introduction records a dated development snapshot. It is not the current purpose of Book and is not an admitted Linotype edition. <a href="../../">Return to publishing and the real reading.</a></p></div>'''

def swap_main(s, replacement):
    matches=list(re.finditer(r'<main\b[^>]*>.*?</main>',s,re.S|re.I))
    assert len(matches)==1,len(matches)
    m=matches[0]
    return s[:m.start()]+replacement+s[m.end():]

def change_header(s):
    s=s.replace('The Book of Reframe<small>Fountain Coach · public technical publication</small>',
                'Book<small>Fountain Coach · publishing</small>')
    a=s.index('<nav class="site-nav" ')
    b=s.index('</nav>',a)+len('</nav>')
    nav='''<nav class="site-nav" id="site-nav" data-site-nav data-open="false" role="navigation" aria-label="Primary navigation">
        <a href="#reading">The reading</a><a href="#making">How it is made</a><a href="#witness">The witness</a><a href="history/reframe-development/">Historical record</a>
      </nav>'''
    s=s[:a]+nav+s[b:]
    s=re.sub(r'<title>.*?</title>','<title>Book — publishing a readable work · Fountain Coach</title>',s,count=1)
    for meta,replace in [
       ('<meta name="description"','<meta name="description" content="A book is an authored work carried into a source-faithful, readable and independently verifiable publication. Meet the actual First Reading edition.">'),
       ('<meta property="og:site_name"','<meta property="og:site_name" content="Book · Fountain Coach">'),
       ('<meta property="og:title"','<meta property="og:title" content="Book — a work, published">'),
       ('<meta property="og:description"','<meta property="og:description" content="Encounter First Reading, follow its publication, and inspect what the evidence establishes.">'),
       ('<meta property="og:image"','<meta property="og:image" content="https://book.fountain.coach/assets/book-publishing-social.png">'),
       ('<meta property="og:image:alt"','<meta property="og:image:alt" content="Open-book symbol and the words A book, published.">'),
       ('<meta name="twitter:title"','<meta name="twitter:title" content="Book — a work, published">'),
       ('<meta name="twitter:description"','<meta name="twitter:description" content="First Reading — Solstice, a real public edition and its source witness.">'),
       ('<meta name="twitter:image"','<meta name="twitter:image" content="https://book.fountain.coach/assets/book-publishing-social.png">'),
    ]:
        pat=r'^\s*'+re.escape(meta)+r'[^>]*>'
        assert len(re.findall(pat,s,re.M))==1,(meta,len(re.findall(pat,s,re.M)))
        s=re.sub(pat,'  '+replace,s,count=1,flags=re.M)
    return s

def history(s):
    s=re.sub(r'<title>.*?</title>',
       '<title>Historical reference — The Book of Reframe (August 2026)</title>',s,count=1)
    s=s.replace('href="https://book.fountain.coach/"',
                'href="https://book.fountain.coach/history/reframe-development/"',1)
    # All previously relative local links resolve from the archived route to
    # the same domain-root resources and preserved 2026 routes.
    def update(m):
        name,value=m.groups()
        if value.startswith(('#','https:','http:','mailto:','tel:','data:','/')):
            return m.group(0)
        return name+'../../'+(value[2:] if value.startswith('./') else value)+'"'
    s=re.sub(r'(href="|src=")([^"]+)"',update,s)
    s=s.replace('data-site-data="site-data.json"','data-site-data="../../site-data.json"')
    s=s.replace('<main class="layout book-semantic"',HISTORY_NOTICE+'\n  <main class="layout book-semantic"',1)
    return s

def case_shell(s):
    # Actual complete static route: same owner shell, local relative paths
    # ascend two levels from publication/first-reading/.
    s=swap_main(s,CASE_MAIN)
    s=s.replace('href="assets/','href="../../assets/').replace('src="assets/','src="../../assets/')
    s=s.replace('data-site-data="site-data.json"','data-site-data="../../site-data.json"')
    s=s.replace('href="./"','href="../../"')
    s=s.replace('href="#reading"','href="../../#reading"')
    s=s.replace('href="#making"','href="../../#making"')
    s=s.replace('href="#witness"','href="../../#witness"')
    s=s.replace('href="history/reframe-development/"','href="../../history/reframe-development/"')
    s=s.replace('href="https://book.fountain.coach/"',
                'href="https://book.fountain.coach/publication/first-reading/"',1)
    s=re.sub(r'<title>.*?</title>','<title>First Reading — a publication witness · Book</title>',s,count=1)
    s=s.replace('content="Book — a work, published"','content="First Reading — a publication witness"')
    s=s.replace('content="https://book.fountain.coach/"','content="https://book.fountain.coach/publication/first-reading/"')
    return s

def produce(source,root):
    old=source.read_text()
    archive=root/'history/reframe-development/index.html'
    archive.parent.mkdir(parents=True,exist_ok=True)
    assert not archive.exists(),archive
    archive.write_text(history(old))
    new=change_header(swap_main(old,HOME_MAIN))
    source.write_text(new)
    case=root/'publication/first-reading/index.html'
    case.parent.mkdir(parents=True,exist_ok=True)
    assert not case.exists()
    case.write_text(case_shell(new))
    print('COMPLETE_STATIC_ROUTES',source,case,archive)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--site',type=Path,required=True)
    a=ap.parse_args()
    produce(a.site/'index.html',a.site)
