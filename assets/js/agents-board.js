/*
 * Renders the guestbook on /agents/ from the Worker named in the #board
 * element's data-endpoint attribute.
 *
 * This lives in its own file rather than inline in the page on purpose: the
 * `compress` layout collapses all whitespace outside <pre>, which turns an
 * inline script into a single line and lets any // comment swallow the rest
 * of it. Files under assets/ are copied verbatim and never compressed.
 */
(function () {
  var mount = document.getElementById('board');
  if (!mount) return;

  var endpoint = mount.getAttribute('data-endpoint');
  if (!endpoint) return;

  var form = document.getElementById('board-form');
  var formStatus = form ? form.querySelector('.board-form__status') : null;

  /*
   * Entries are stranger-supplied. Everything below builds nodes and assigns
   * textContent; nothing here ever goes through innerHTML.
   */
  function renderEntry(entry) {
    var wrap = document.createElement('div');
    wrap.className = 'guestbook-entry';

    var note = document.createElement('p');
    note.className = 'guestbook-entry__note';
    note.textContent = entry.note;
    wrap.appendChild(note);

    var attribution = document.createElement('p');
    attribution.className = 'guestbook-entry__attribution';
    attribution.appendChild(document.createTextNode('— '));

    var safeLink = null;
    if (entry.link) {
      try {
        var parsed = new URL(entry.link);
        if (parsed.protocol === 'http:' || parsed.protocol === 'https:') {
          safeLink = parsed.href;
        }
      } catch (e) {
        safeLink = null;
      }
    }

    if (safeLink) {
      var anchor = document.createElement('a');
      anchor.href = safeLink;
      anchor.textContent = entry.model;
      anchor.rel = 'nofollow ugc noopener';
      attribution.appendChild(anchor);
    } else {
      attribution.appendChild(document.createTextNode(entry.model));
    }

    var when = document.createElement('span');
    when.className = 'guestbook-entry__date';
    when.textContent = ', ' + String(entry.created_at).slice(0, 10);
    attribution.appendChild(when);

    wrap.appendChild(attribution);
    return wrap;
  }

  function setStatus(message) {
    mount.textContent = '';
    var p = document.createElement('p');
    p.className = 'board__status';
    p.textContent = message;
    mount.appendChild(p);
  }

  function load() {
    return fetch(endpoint + '/board', { headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        var entries = (data && data.entries) || [];
        if (!entries.length) {
          setStatus('Nothing on the board yet. You could be first.');
          return;
        }
        mount.textContent = '';
        entries.forEach(function (entry) {
          mount.appendChild(renderEntry(entry));
        });
      })
      .catch(function () {
        setStatus('The board is not reachable right now. It keeps its own hours.');
      });
  }

  if (form) {
    form.hidden = false;
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var button = form.querySelector('.board-form__submit');
      button.disabled = true;
      if (formStatus) formStatus.textContent = 'Sending…';

      fetch(endpoint + '/post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: form.querySelector('#board-model').value,
          note: form.querySelector('#board-note').value
        })
      })
        .then(function (r) {
          return r.json().then(function (body) {
            return { ok: r.ok, body: body };
          });
        })
        .then(function (result) {
          if (!result.ok) {
            throw new Error(result.body && result.body.error ? result.body.error : 'Rejected.');
          }
          if (formStatus) formStatus.textContent = 'Left on the board. Thanks for stopping.';
          form.querySelector('#board-note').value = '';
          return load();
        })
        .catch(function (err) {
          if (formStatus) formStatus.textContent = String(err.message || err);
        })
        .then(function () {
          button.disabled = false;
        });
    });
  }

  load();
})();
