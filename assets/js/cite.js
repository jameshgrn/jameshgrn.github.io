/*
 * Expand/collapse the citation block on each entry in the homepage
 * publications list, and copy the citation to the clipboard.
 *
 * This lives in its own file rather than inline in the page on purpose: the
 * `compress` layout collapses all whitespace outside <pre>, which turns an
 * inline script into a single line and lets any // comment swallow the rest
 * of it. Files under assets/ are copied verbatim and never compressed.
 */
(function () {
  var list = document.querySelector('.pubs-list');
  if (!list) return;

  /* Citations are authored with <i> for the venue; copy the rendered text. */
  function citationText(panel) {
    var el = panel.querySelector('.cite-text');
    return el ? el.textContent.replace(/\s+/g, ' ').trim() : '';
  }

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    /* file:// and plain http have no async clipboard. */
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.top = '-1000px';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      ok ? resolve() : reject();
    });
  }

  list.addEventListener('click', function (e) {
    var toggle = e.target.closest('.cite-toggle');
    if (toggle) {
      var panel = document.getElementById(toggle.getAttribute('aria-controls'));
      if (!panel) return;
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      panel.hidden = open;
      return;
    }

    var button = e.target.closest('.cite-copy');
    if (!button) return;
    var text = citationText(button.closest('.cite-panel'));
    if (!text) return;

    copy(text).then(function () {
      button.textContent = 'copied';
    }).catch(function () {
      button.textContent = 'press ⌘C';
    });
    window.setTimeout(function () { button.textContent = 'copy'; }, 2000);
  });
})();
