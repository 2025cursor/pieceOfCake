(function () {
  'use strict';

  var STORAGE_KEY = 'piece-of-cake-consent-v1';
  var saved = null;
  try { saved = window.localStorage.getItem(STORAGE_KEY); } catch (error) { saved = null; }

  function setConsent(allowed) {
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: allowed ? 'granted' : 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied'
      });
    }
    try { window.localStorage.setItem(STORAGE_KEY, allowed ? 'granted' : 'denied'); } catch (error) { /* privacy choice still applies for this view */ }
  }

  if (saved === 'granted') setConsent(true);
  if (saved === 'denied') setConsent(false);

  document.addEventListener('click', function (event) {
    var trigger = event.target.closest('[data-open-consent]');
    if (!trigger) return;
    try { window.localStorage.removeItem(STORAGE_KEY); } catch (error) {}
    saved = null;
    var existing = document.querySelector('.consent-banner');
    if (existing) existing.remove();
    render();
  });

  function render() {
    if (typeof window.gtag !== 'function') return;
    if (saved === 'granted' || saved === 'denied' || document.querySelector('.consent-banner')) return;
    var banner = document.createElement('aside');
    banner.className = 'consent-banner';
    var language = (document.documentElement.lang || 'en').slice(0, 2);
    var copy = {
      zh: { label: '隐私选择', text: '本站使用 Google Analytics 统计汇总访问信息，目前不投放广告。', deny: '仅必要功能', allow: '允许分析' },
      es: { label: 'Preferencia de privacidad', text: 'Este sitio usa Google Analytics para datos agregados; actualmente no muestra anuncios.', deny: 'Solo necesario', allow: 'Permitir analítica' },
      en: { label: 'Privacy choice', text: 'This site uses Google Analytics for aggregate visit information. No advertising is served on this site currently.', deny: 'Use necessary only', allow: 'Allow analytics' }
    }[language] || { label: 'Privacy choice', text: 'This site uses Google Analytics for aggregate visit information. No advertising is served on this site currently.', deny: 'Use necessary only', allow: 'Allow analytics' };
    banner.setAttribute('aria-label', copy.label);
    banner.innerHTML = '<div><strong>' + copy.label + '</strong><p>' + copy.text + '</p></div><div class="consent-actions"><button type="button" data-consent="deny">' + copy.deny + '</button><button type="button" class="consent-accept" data-consent="allow">' + copy.allow + '</button></div>';
    document.body.appendChild(banner);
    banner.addEventListener('click', function (event) {
      var button = event.target.closest('[data-consent]');
      if (!button) return;
      var allowed = button.getAttribute('data-consent') === 'allow';
      setConsent(allowed);
      banner.remove();
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
  else render();
})();
