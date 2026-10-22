(() => {
  'use strict';
  const event = window.UNLOCKED;
  if (!event) return;
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const safeUrl = value => {
    if (!value) return '';
    try { const url = new URL(value, location.href); return /^https?:$/.test(url.protocol) ? url.href : ''; } catch { return ''; }
  };
  // Renders into an element only if it exists, so removing markup never stops the rest of the page.
  const fill = (selector, html) => { const el = $(selector); if (el) el.innerHTML = html; return el; };
  const external = 'target="_blank" rel="noopener noreferrer"';
  // An SVG, not the ↗ character, which iOS draws as a colour emoji.
  const ARROW = '<svg class="ext-arrow" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 9 9 3M4 3h5v5"/></svg>';
  const iconPaths = {
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21v-2a8 8 0 0 1 16 0v2"/>',
    plus: '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6Z"/>',
    flask: '<path d="M9 3h6m-5 0v6L4 19a1.3 1.3 0 0 0 1 2h14a1.3 1.3 0 0 0 1-2L14 9V3M7 14h10"/>',
    home: '<path d="m3 10 9-7 9 7M5 9v12h14V9M10 21v-7h4v7"/>',
    eye: '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    play: '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="m10 8 6 4-6 4Z"/>',
    box: '<path d="m12 3 9 5v9l-9 5-9-5V8l9-5Zm0 10v9M3 8l9 5 9-5M7.5 5.5l9 5"/>',
    file: '<path d="M14 2H5v20h14V7l-5-5Zm0 0v5h5M8 12h8m-8 4h6"/>',
    check: '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="m7 12 3 3 7-7"/>',
    star: '<path d="m12 3 2.8 5.8 6.4 1-4.6 4.4 1.1 6.3-5.7-3-5.7 3 1.1-6.3L2.8 9.8l6.4-1Z"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c5 5 5 13 0 18-5-5-5-13 0-18Z"/>',
    diamond: '<path d="m7 3-5 6 10 13L22 9l-5-6H7Zm-5 6h20M7 3l5 19 5-19"/>',
    ballot: '<path d="M8 11V2h8v9M6 9H4l-2 5v8h20v-8l-2-5h-2M2 14h20M7 11h10m-7-5 1.5 1.5L14 5"/>'
  };
  const icon = name => `<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">${iconPaths[name] || iconPaths.user}</svg>`;
  const tags = values => `<div class="tags">${values.map(t => `<span class="tag">${esc(t)}</span>`).join('')}</div>`;

  $$('[data-year]').forEach(el => { el.textContent = event.year; });
  document.title = `${event.title} | ${event.challengeLabel} of the ${event.eventName} | Tide`;

  // One Discord URL for every help link. Without one, links fall back to the Help section.
  const discord = safeUrl(event.discordUrl);
  $$('[data-discord]').forEach(el => {
    if (discord) { el.href = discord; return; }
    el.href = '#help'; el.removeAttribute('target'); el.removeAttribute('rel');
    el.querySelector('.ext-arrow')?.remove();
  });

  // Videos play in an overlay. YouTube and Vimeo are embedded; direct .mp4/.webm files use the native player.
  function embedUrl(url) {
    const parsed = new URL(url), host = parsed.hostname.replace(/^www\./, '');
    if (host === 'youtu.be') return `https://www.youtube-nocookie.com/embed/${encodeURIComponent(parsed.pathname.slice(1))}?autoplay=1&rel=0&vq=hd1080`;
    if (/(^|\.)youtube\.com$/.test(host)) {
      const id = parsed.searchParams.get('v') || (parsed.pathname.match(/\/(?:embed|shorts|live)\/([\w-]+)/) || [])[1];
      return id ? `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&vq=hd1080` : '';
    }
    if (host === 'vimeo.com') { const id = (parsed.pathname.match(/\/(\d+)/) || [])[1]; return id ? `https://player.vimeo.com/video/${id}?autoplay=1` : ''; }
    if (host === 'player.vimeo.com') return url;
    return '';
  }
  const videoDialog = $('#video-dialog'), videoFrame = $('#video-frame');
  let videoTrigger;
  $$('[data-video]').forEach(button => {
    const video = event[button.dataset.video] || {};
    const url = safeUrl(video.url);
    if (!url) {
      // Not published yet: hero buttons stay visible but inactive; other video buttons are hidden.
      const note = $('[data-video-note]', button);
      if (!note) { button.hidden = true; return; }
      button.disabled = true;
      button.classList.add('is-pending');
      note.textContent = 'Coming soon';
      return;
    }
    button.addEventListener('click', () => {
      const embed = embedUrl(url);
      if (!embed && !/\.(mp4|webm)$/i.test(new URL(url).pathname)) { window.open(url, '_blank', 'noopener'); return; }
      if (!videoDialog) return;
      videoTrigger = button;
      const title = esc(video.title || 'Video');
      videoFrame.innerHTML = embed
        ? `<iframe src="${esc(embed)}" title="${title}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>`
        : `<video controls autoplay src="${esc(url)}" aria-label="${title}"></video>`;
      videoDialog.setAttribute('aria-label', video.title || 'Video');
      videoDialog.showModal();
      $('.video-close', videoDialog).focus({ preventScroll: true });
    });
  });
  if (videoDialog) {
    $('.video-close', videoDialog).addEventListener('click', () => videoDialog.close());
    videoDialog.addEventListener('click', e => { if (e.target === videoDialog) videoDialog.close(); });
    // Emptying the frame stops playback when the overlay closes.
    videoDialog.addEventListener('close', () => { videoFrame.innerHTML = ''; if (videoTrigger) videoTrigger.focus({ preventScroll: true }); });
  }

  // Submission deadlines differ by city. The countdown follows the viewer's own city (by time zone), else the first one.
  const submission = event.submission || {};
  const cities = (submission.deadlineCities || []).map(c => ({ ...c, due: new Date(c.deadlineIso) })).filter(c => !isNaN(c.due));
  if (cities.length) {
    const viewerZone = (() => { try { return Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch { return ''; } })();
    const mine = cities.find(c => (c.zones || [c.timeZone]).some(z => viewerZone.startsWith(z))) || cities[0];
    const list = $('#deadline-cities');
    const renderCities = () => fill('#deadline-cities', cities.map(c => {
      let time = '';
      try { time = new Intl.DateTimeFormat('en-AU', { timeZone: c.timeZone, weekday: 'short', day: 'numeric', month: 'short', hour: 'numeric', minute: '2-digit', timeZoneName: c.showZone ? 'short' : undefined }).format(c.due); } catch { return ''; }
      return `<div${c === mine ? ' class="is-mine"' : ''}><dt>${esc(c.name)}</dt><dd>${c.due <= Date.now() ? 'Closed' : esc(time)}</dd></div>`;
    }).join(''));
    if (list) renderCities();
    const countdown = $('#countdown'), closed = $('#deadline-closed'), label = $('#deadline-label');
    if (label) label.textContent = `${mine.name} closes in`;
    const parts = Object.fromEntries($$('[data-cd]', countdown || document).map(el => [el.dataset.cd, el]));
    const tick = () => {
      const left = mine.due - Date.now();
      if (left <= 0) {
        if (countdown) countdown.hidden = true;
        if (closed) { closed.hidden = false; closed.textContent = `${mine.name} submissions have closed.`; }
        if (label) label.hidden = true;
        renderCities();
        return false;
      }
      const s = Math.floor(left / 1000);
      const values = { days: Math.floor(s / 86400), hours: Math.floor(s / 3600) % 24, minutes: Math.floor(s / 60) % 60, seconds: s % 60 };
      Object.entries(values).forEach(([k, v]) => { if (parts[k]) parts[k].textContent = k === 'days' ? v : String(v).padStart(2, '0'); });
      if (countdown) { countdown.hidden = false; countdown.setAttribute('aria-label', `${values.days} days, ${values.hours} hours and ${values.minutes} minutes left for ${mine.name}`); }
      if (s % 60 === 0) renderCities();
      return true;
    };
    if (tick()) { const timer = setInterval(() => { if (!tick()) clearInterval(timer); }, 1000); }
  }
  const form = safeUrl(submission.formUrl);
  fill('#submit-cta', form
    ? `<a class="button dark-button" href="${esc(form)}" ${external}>Submit via Google Form${ARROW}</a>`
    : `<p class="info-note" role="note"><strong>Submission link coming.</strong> The submission form link will be added here once it’s live.</p>`);

  // README project overview: one prompt per judging criterion, plus a copyable Markdown template.
  const prompted = (event.criteria || []).filter(c => c.readmePrompt);
  fill('#readme-prompts', prompted.map(c => `<li><h4>${esc(c.title)}</h4><p>${esc(c.readmePrompt)}</p></li>`).join(''));
  const copyButton = $('#copy-readme'), copyStatus = $('#copy-status');
  if (copyButton && prompted.length) {
    const link = safeUrl(event.readmeLink), badge = safeUrl(event.readmeBadge);
    const template = [
      ...(badge && link ? [`[![Built with TideCloak](${badge})](${link})`, ''] : []),
      '## Project overview', '', '_One-sentence description of your project._', '',
      ...(link ? [`Built with [TideCloak](${link}).`, ''] : []),
      ...prompted.flatMap((c, i) => [`### ${i + 1}. ${c.title}`, '', `<!-- ${c.readmePrompt} -->`, '']),
      '## Setup', '', '<!-- How to install and run the prototype. -->', ''].join('\n');
    copyButton.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(template); copyStatus.textContent = 'Copied. Paste it at the top of your README.'; }
      catch {
        // Clipboard unavailable: show the template for manual copying.
        copyStatus.innerHTML = `<textarea class="template-fallback" readonly rows="10" aria-label="README template">${esc(template)}</textarea>`;
        $('.template-fallback', copyStatus).select();
      }
    });
  } else if (copyButton) copyButton.hidden = true;

  fill('#criteria-list', (event.criteria || []).map(c => `<article class="criterion"><span class="criterion-weight">${esc(c.weight)}<span class="pct">%</span></span><div><h3>${esc(c.title)}</h3><p>${esc(c.description)}</p></div></article>`).join(''));

  // Resources in two groups: the TideCloak links you build with, then reading shown as story cards with a thumbnail.
  const resources = group => (event.resources || []).filter(r => r.group === group);
  fill('#resource-build', resources('build').map(r =>
    `<a class="resource-link build-link" href="${esc(safeUrl(r.url))}" ${external}><span class="resource-name">${esc(r.name)}${ARROW}</span>${r.text ? `<span class="resource-text">${esc(r.text)}</span>` : ''}</a>`).join(''));
  fill('#resource-think', resources('think').map(r =>
    `<a class="resource-story" href="${esc(safeUrl(r.url))}" ${external}>${r.image ? `<img class="story-thumb" src="${esc(r.image)}" alt="" width="480" height="300" loading="lazy" decoding="async">` : ''}<span class="story-copy">${r.source ? `<span class="story-source">${esc(r.source)}</span>` : ''}<span class="resource-name">${esc(r.name)}</span>${r.text ? `<span class="resource-text">${esc(r.text)}</span>` : ''}</span></a>`).join(''));

  const sessions = (event.supportSessions || []).filter(s => s && s.text);
  const sessionList = fill('#support-sessions', sessions.map(s => {
    const url = safeUrl(s.url);
    return `<li>${url ? `<a href="${esc(url)}" ${external}>${esc(s.text)}${ARROW}</a>` : esc(s.text)}</li>`;
  }).join(''));
  if (sessionList && sessions.length) sessionList.hidden = false;

  fill('#faq-list', (event.faqs || []).map(f => {
    let extra = '';
    if (f.discord && discord) extra = `<a href="${esc(discord)}" ${external}>Get help on Discord${ARROW}</a> <button type="button" class="faq-chat" data-open-chat>Ask Hackbot</button>`;
    else if (f.link && /^#[\w-]+$/.test(f.link.href)) extra = `<a href="${esc(f.link.href)}">${esc(f.link.label)}</a>`;
    return `<details><summary>${esc(f.question)}</summary><p>${esc(f.answer)}${extra ? `<span class="faq-links">${extra}</span>` : ''}</p></details>`;
  }).join(''));

  // Ideas: a short first selection, with the rest one click away.
  const ideas = event.inspirationIdeas || [];
  const initialIdeas = 4;
  const ideaGrid = fill('#idea-grid', ideas.map((idea,index) => `<button class="idea-card" type="button" data-idea="${index}" aria-haspopup="dialog" aria-labelledby="idea-name-${index}" aria-describedby="idea-description-${index}"${index >= initialIdeas ? ' hidden' : ''}><span class="idea-symbol">${icon(idea.icon)}</span><span class="idea-copy"><span class="idea-name" id="idea-name-${index}">${esc(idea.name)}</span><span class="idea-description" id="idea-description-${index}">${esc(idea.summary)}</span><span class="domain">${esc(idea.tags[0])}</span></span><span class="idea-arrow" aria-hidden="true">${ARROW}</span></button>`).join(''));
  const ideasToggle = $('#ideas-toggle');
  if (ideaGrid && ideasToggle && ideas.length > initialIdeas) {
    const label = open => open ? 'Show fewer ideas' : `Show all ${ideas.length} ideas`;
    ideasToggle.textContent = label(false);
    ideasToggle.hidden = false;
    ideasToggle.addEventListener('click', () => {
      const open = ideasToggle.getAttribute('aria-expanded') !== 'true';
      $$('[data-idea]', ideaGrid).forEach((card, i) => { if (i >= initialIdeas) card.hidden = !open; });
      ideasToggle.setAttribute('aria-expanded', String(open));
      ideasToggle.textContent = label(open);
      if (open) $$('[data-idea]', ideaGrid)[initialIdeas].focus();
    });
  }

  const menuButton = $('.menu-toggle'), menu = $('#mobile-nav');
  if (menuButton && menu) {
    const closeMenu = () => { menu.hidden = true; menuButton.setAttribute('aria-expanded','false'); menuButton.setAttribute('aria-label','Open navigation'); };
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') !== 'true';
      menu.hidden = !open; menuButton.setAttribute('aria-expanded',String(open));
      menuButton.setAttribute('aria-label',open ? 'Close navigation' : 'Open navigation');
    });
    $$('a',menu).forEach(a => a.addEventListener('click',closeMenu));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { closeMenu(); menuButton.focus(); } });
    window.matchMedia('(min-width:1051px)').addEventListener('change', e => { if (e.matches) closeMenu(); });
  }

  const dialog = $('#idea-dialog');
  if (dialog) {
    let dialogTrigger;
    const closeDialog = () => dialog.close();
    const showDialog = (content, trigger) => {
      dialogTrigger = trigger || document.activeElement;
      $('#dialog-content').innerHTML = content;
      if (!dialog.open) dialog.showModal();
      dialog.scrollTop = 0;
      $('.dialog-close').focus({preventScroll:true});
    };
    $('.dialog-close').addEventListener('click',closeDialog);
    dialog.addEventListener('click',e => {
      if (e.target !== dialog) return;
      const r = dialog.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) closeDialog();
    });
    dialog.addEventListener('close',() => { if (dialogTrigger && document.contains(dialogTrigger)) dialogTrigger.focus({preventScroll:true}); });
    const showIdea = (index, trigger) => {
      const idea = ideas[index];
      if (!idea) return;
      showDialog(`<p class="dialog-topline">Example idea · inspiration only</p><h2 id="dialog-title">${esc(idea.name)}</h2><p class="dialog-summary">${esc(idea.summary)}</p>${tags(idea.tags)}${[['The idea',idea.idea],['What trust blocks today',idea.barrier],['Why Tide changes it',idea.tide],['The demo moment',idea.demo]].map(([label,text],i) => `<div class="dialog-section ${i === 3 ? 'demo-moment' : ''}"><h3>${label}</h3><p>${esc(text)}</p></div>`).join('')}<p class="dialog-footnote">Use synthetic data. Any revocation stops future authorised access; it cannot recall material a recipient has already viewed or copied.</p><div class="dialog-actions"><button type="button" id="idea-back">Back to ideas</button><button type="button" id="next-idea">Next idea →</button></div>`,trigger);
      $('#next-idea').addEventListener('click',() => showIdea((index+1)%ideas.length,dialogTrigger));
      $('#idea-back').addEventListener('click',closeDialog);
    };
    $$('[data-idea]').forEach(button => button.addEventListener('click',() => showIdea(Number(button.dataset.idea),button)));
  }

  initHackbot(event.chat || {});

  // Hackbot, the UNLOCKED assistant. Uses the whitepaper chatbot's backend in its "unlocked" mode.
  function initHackbot(chat) {
    const root = $('#hackbot'), panel = $('#hackbot-panel'), launcher = $('#hackbot-launcher');
    const log = $('#hackbot-log'), empty = $('#hackbot-empty'), form = $('#hackbot-form'), input = $('#hackbot-input');
    const apiUrl = safeUrl(chat.apiUrl);
    if (!root || !panel || !launcher || !apiUrl) {
      // No backend configured: hide everything that would open the chat.
      $$('[data-open-chat]').forEach(el => { el.hidden = true; });
      $$('.hackbot-callout, .help-way-hackbot').forEach(el => { el.hidden = true; });
      return;
    }
    root.hidden = false;
    const messages = [];
    let busy = false, returnFocus = null;

    const inline = text => esc(text)
      .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, (m, label, url) => { const safe = safeUrl(url.replace(/&amp;/g, '&')); return safe ? `<a href="${esc(safe)}" ${external}>${label}</a>` : label; })
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^*])\*([^*\s][^*]*?)\*/g, '$1<em>$2</em>');
    // Groups consecutive lines into paragraphs, bullet lists, numbered lists and fenced code.
    const markdown = text => {
      const html = []; let para = [], list = null, code = null;
      const flushPara = () => { if (para.length) html.push(`<p>${para.map(inline).join('<br>')}</p>`); para = []; };
      const flushList = () => { if (list) html.push(`<${list.tag}>${list.items.map(i => `<li>${inline(i)}</li>`).join('')}</${list.tag}>`); list = null; };
      for (const line of String(text).split('\n')) {
        if (code) { if (/^\s*```/.test(line)) { html.push(`<pre><code>${esc(code.join('\n'))}</code></pre>`); code = null; } else code.push(line); continue; }
        if (/^\s*```/.test(line)) { flushPara(); flushList(); code = []; continue; }
        const bullet = line.match(/^\s*[-*] (.*)/), numbered = line.match(/^\s*\d+[.)] (.*)/);
        const item = bullet || numbered;
        if (item) {
          const tag = bullet ? 'ul' : 'ol';
          flushPara();
          if (list && list.tag !== tag) flushList();
          if (!list) list = { tag, items: [] };
          list.items.push(item[1]);
        } else if (!line.trim()) { flushPara(); flushList(); }
        else { flushList(); para.push(line.replace(/^#{1,6}\s+/, '')); }
      }
      if (code) html.push(`<pre><code>${esc(code.join('\n'))}</code></pre>`);
      flushPara(); flushList();
      return html.join('');
    };

    const addBubble = (role, html) => {
      const bubble = document.createElement('div');
      bubble.className = `hackbot-msg ${role}`;
      bubble.innerHTML = html;
      log.append(bubble);
      log.scrollTop = log.scrollHeight;
      return bubble;
    };

    const setOpen = open => {
      panel.hidden = !open;
      launcher.setAttribute('aria-expanded', String(open));
      root.classList.toggle('is-open', open);
      if (open) { input.focus(); }
      else if (returnFocus && document.contains(returnFocus)) { returnFocus.focus({preventScroll:true}); }
    };

    async function send(text) {
      const content = text.trim();
      if (!content || busy) return;
      busy = true;
      empty.hidden = true;
      messages.push({ role: 'user', content });
      addBubble('user', `<p>${esc(content)}</p>`);
      input.value = ''; resize();
      if (hint) hint.hidden = true;
      const typing = addBubble('assistant typing', '<span></span><span></span><span></span><span class="sr-only">Hackbot is typing</span>');
      let reply;
      try {
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ messages, context: chat.context || undefined })
        });
        if (response.status === 429) reply = 'I’m getting a lot of questions right now. Give me a minute and try again.';
        else if (!response.ok) throw new Error(`Chat request failed: ${response.status}`);
        else reply = (await response.json()).message;
        if (!reply) throw new Error('Empty reply');
        if (response.ok) messages.push({ role: 'assistant', content: reply });
      } catch (err) {
        console.warn('[Hackbot]', err);
        reply = discord
          ? `I lost my train of thought there. Try again in a moment, or ask on the [Tide Discord](${discord}).`
          : 'I lost my train of thought there. Try again in a moment.';
      } finally {
        typing.remove();
        // A failed turn is dropped so the next request starts from a clean conversation.
        if (messages.length && messages[messages.length - 1].role === 'user') messages.pop();
        addBubble('assistant', markdown(reply));
        busy = false;
      }
    }

    const resize = () => { input.style.height = 'auto'; input.style.height = `${Math.min(input.scrollHeight, 120)}px`; };
    // Fills the message box so the student can add their own details before sending.
    const hint = $('#hackbot-hint');
    const prefill = text => {
      input.value = text; resize(); input.focus();
      input.setSelectionRange(input.value.length, input.value.length);
      input.scrollTop = input.scrollHeight;
      if (hint) hint.hidden = false;
    };
    const suggestions = (chat.suggestions || []).filter(q => q && q.label && (q.send || q.prefill));
    fill('#hackbot-chips', suggestions.map((q, i) => `<button type="button" class="hackbot-chip${q.prefill ? ' is-prefill' : ''}" data-chip="${i}">${esc(q.label)}${q.prefill ? '<span class="chip-note">Add your details</span>' : ''}</button>`).join(''));
    $$('.hackbot-chip', panel).forEach(chip => chip.addEventListener('click', () => {
      const q = suggestions[Number(chip.dataset.chip)];
      if (q.prefill) prefill(q.prefill);
      else { input.focus(); send(q.send); }
    }));
    form.addEventListener('submit', e => { e.preventDefault(); send(input.value); });
    input.addEventListener('input', resize);
    input.addEventListener('keydown', e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(input.value); } });
    launcher.addEventListener('click', () => { returnFocus = launcher; setOpen(panel.hidden); });
    $('.hackbot-close', panel).addEventListener('click', () => setOpen(false));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden && !document.querySelector('dialog[open]')) setOpen(false); });
    // Delegated so buttons rendered later (e.g. in the FAQ) also open the panel.
    document.addEventListener('click', e => {
      const opener = e.target.closest('[data-open-chat]');
      if (!opener) return;
      returnFocus = opener;
      setOpen(true);
      if (opener.dataset.prefill) prefill(opener.dataset.prefill);
      else if (opener.dataset.openChat) send(opener.dataset.openChat);
    });
  }
})();
