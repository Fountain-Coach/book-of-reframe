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
