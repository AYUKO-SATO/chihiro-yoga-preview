(function () {
  'use strict';

  /* menu drawer */
  var drawer = document.getElementById('drawer');
  var openBtn = document.querySelector('.menu-btn');
  function setMenu(open) {
    if (!drawer) return;
    drawer.hidden = !open;
    openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (openBtn) {
    openBtn.addEventListener('click', function () { setMenu(true); });
    drawer.querySelector('.drawer-close').addEventListener('click', function () { setMenu(false); });
    drawer.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* accordions */
  document.addEventListener('click', function (e) {
    var head = e.target.closest('.acc-head');
    if (!head) return;
    var acc = head.parentElement;
    var open = !acc.classList.contains('is-open');
    acc.classList.toggle('is-open', open);
    head.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* hero slider (auto 4s, dissolve, swipe) */
  var hero = document.querySelector('.hero');
  if (hero) {
    var slides = [].slice.call(hero.querySelectorAll('.hero-slide'));
    var dots = [].slice.call(hero.querySelectorAll('.dot'));
    var cur = 0, timer = null;
    var go = function (i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('is-active', k === cur); });
      dots.forEach(function (d, k) { d.classList.toggle('is-active', k === cur); });
      // lazy images
      var img = slides[cur].querySelector('img');
      if (img) img.loading = 'eager';
    };
    var start = function () {
      stop();
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      timer = setInterval(function () { go(cur + 1); }, 4000);
    };
    var stop = function () { if (timer) clearInterval(timer); timer = null; };
    dots.forEach(function (d) {
      d.addEventListener('click', function () { go(+d.dataset.go); start(); });
    });
    var x0 = null;
    hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; stop(); }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (x0 !== null) {
        var dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1));
      }
      x0 = null; start();
    }, { passive: true });
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    start();
  }

  /* news / blog carousels */
  [].forEach.call(document.querySelectorAll('.carousel'), function (c) {
    var row = c.querySelector('.car-row');
    var step = function () { var card = row.querySelector('.card'); return card ? card.offsetWidth + 12 : 170; };
    c.querySelector('.car-prev').addEventListener('click', function () { row.scrollBy({ left: -step(), behavior: 'smooth' }); });
    c.querySelector('.car-next').addEventListener('click', function () { row.scrollBy({ left: step(), behavior: 'smooth' }); });
  });

  /* voice slider: swipe + pagination dots */
  var vt = document.querySelector('.voice-track');
  if (vt) {
    var vdots = [].slice.call(document.querySelectorAll('.vdot'));
    var mark = function () {
      var i = Math.round(vt.scrollLeft / (vt.firstElementChild.offsetWidth + 12));
      vdots.forEach(function (d, k) { d.classList.toggle('is-active', k === i); });
    };
    vt.addEventListener('scroll', function () { window.requestAnimationFrame(mark); }, { passive: true });
    vdots.forEach(function (d) {
      d.addEventListener('click', function () {
        vt.scrollTo({ left: (+d.dataset.go) * (vt.firstElementChild.offsetWidth + 12), behavior: 'smooth' });
      });
    });
  }

  /* concept video: swap the thumbnail for the YouTube player on click */
  var video = document.querySelector('.video');
  if (video) {
    video.addEventListener('click', function () {
      var id = video.dataset.yt;
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&playsinline=1';
      f.title = 'コンセプト動画';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      video.appendChild(f);
      video.classList.add('is-playing');
    }, { once: true });
  }
})();
