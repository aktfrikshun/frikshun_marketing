const header = document.querySelector('[data-header]');
const nav = document.querySelector('#site-nav');
const toggle = document.querySelector('.nav-toggle');

const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 20);
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

toggle?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
  toggle.querySelector('.sr-only').textContent = open ? 'Close navigation' : 'Open navigation';
});

nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  toggle?.setAttribute('aria-expanded', 'false');
}));

const form = document.querySelector('#contact-form');
const submit = document.querySelector('#submit-btn');
form?.addEventListener('submit', () => {
  submit.disabled = true;
  submit.textContent = 'Sending…';
});
