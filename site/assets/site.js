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
