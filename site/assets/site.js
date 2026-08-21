(() => {
  const root = document.documentElement;
  const button = document.querySelector('[data-theme-toggle]');
  if (!button) return;
  const stored = window.localStorage.getItem('fountain-coach-theme');
  root.dataset.theme = stored || 'system';
  const sync = () => {
    const mode = root.dataset.theme;
    button.textContent = `Theme: ${mode}`;
    button.setAttribute('aria-pressed', String(mode === 'dark'));
    button.setAttribute('aria-label', `Switch to ${mode === 'dark' ? 'light' : 'dark'} theme`);
  };
  sync();
  button.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    window.localStorage.setItem('fountain-coach-theme', next);
    sync();
  });
})();

(() => {
  const brand = document.querySelector('.brand');
  const nav = document.querySelector('[data-site-nav]');
  const main = document.querySelector('main');
  if (brand && nav && main) {
    const root = new URL(brand.getAttribute('href'), window.location.href);
    root.hash = '';
    root.pathname = root.pathname.replace(/[^/]*$/, '');
    const links = [
      ['Start here', new URL('./', root).href],
      ['Verified behavior', new URL('commands/commands/', root).href],
      ['Scenarios', new URL('scenarios/', root).href],
      ['Governance', new URL('governance/default-semantic-manuscript-projection/', root).href],
    ];
    const currentPath = window.location.pathname;
    nav.replaceChildren(...links.map(([label, href]) => {
      const a = document.createElement('a');
      a.href = href;
      a.textContent = label;
      if ((label === 'Start here' && currentPath === new URL(href).pathname) ||
          (label === 'Verified behavior' && currentPath.startsWith(new URL('commands/', root).pathname)) ||
          (label === 'Scenarios' && currentPath.startsWith(new URL('scenarios/', root).pathname)) ||
          (label === 'Governance' && currentPath.startsWith(new URL('governance/', root).pathname))) {
        a.setAttribute('aria-current', 'page');
      }
      return a;
    }));

    let breadcrumb = main.querySelector('.breadcrumbs');
    if (!breadcrumb) {
      breadcrumb = document.createElement('nav');
      breadcrumb.className = 'breadcrumbs';
      breadcrumb.setAttribute('aria-label', 'Breadcrumb');
      main.prepend(breadcrumb);
    }
    const list = document.createElement('ol');
    const add = (label, href, current = false) => {
      const li = document.createElement('li');
      if (current) {
        li.textContent = label;
        li.setAttribute('aria-current', 'page');
      } else {
        const a = document.createElement('a');
        a.href = href;
        a.textContent = label;
        li.append(a);
      }
      list.append(li);
    };
    add('Fountain Coach', 'https://fountain.coach/', false);
    const relative = currentPath.slice(new URL(root).pathname.length).replace(/^\/+|\/+$/g, '');
    if (!relative) {
      add('The Book of Reframe', null, true);
    } else {
      add('The Book of Reframe', root.href);
      const section = relative.split('/')[0];
      const sectionMap = {
        commands: ['Verified behavior', new URL('commands/commands/', root).href],
        scenarios: ['Scenarios', new URL('scenarios/', root).href],
        'scenario-driven-development': ['Development method', new URL('scenario-driven-development/', root).href],
        governance: ['Governance', new URL('governance/default-semantic-manuscript-projection/', root).href],
      };
      const mapped = sectionMap[section];
      if (mapped) add(mapped[0], mapped[1], false);
      const current = document.querySelector('h1');
      add(current ? current.textContent.trim() : section, null, true);
    }
    breadcrumb.replaceChildren(list);
  }
})();

(() => {
  const button = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-site-nav]');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    const open = nav.dataset.open === 'true';
    nav.dataset.open = String(!open);
    button.setAttribute('aria-expanded', String(!open));
    button.textContent = open ? 'Menu' : 'Close';
  });
  nav.addEventListener('click', (event) => {
    if (event.target.matches('a')) {
      nav.dataset.open = 'false';
      button.setAttribute('aria-expanded', 'false');
      button.textContent = 'Menu';
    }
  });
})();

(() => {
  const applyData = (data) => {
    document.querySelectorAll('[data-site-value]').forEach((node) => {
      const value = data[node.dataset.siteValue];
      if (value !== undefined) node.textContent = value;
    });
    document.querySelectorAll('[data-site-date]').forEach((node) => { node.textContent = data.snapshotDate; });
    document.querySelectorAll('[data-site-status]').forEach((node) => { node.textContent = data.releaseStatus; });
  };
  const dataUrl = document.body.dataset.siteData || 'site-data.json';
  fetch(dataUrl, { cache: 'no-store' }).then((response) => response.json()).then(applyData).catch(() => {});
})();
