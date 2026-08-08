// Md Safayet Ullah — Portfolio
// Shared behaviour: mobile nav, theme toggle (persisted), scroll reveal, active nav link.

(function () {
  "use strict";

  var root = document.documentElement;
  var STORAGE_KEY = "msu-portfolio-theme";

  /* ---------- Theme (dark / light) ---------- */
  function applyTheme(theme) {
    if (theme === "light") {
      root.setAttribute("data-theme", "light");
    } else {
      root.setAttribute("data-theme", "dark");
    }
    var toggles = document.querySelectorAll(".theme-toggle");
    toggles.forEach(function (btn) {
      btn.setAttribute("aria-pressed", theme === "light" ? "true" : "false");
    });
  }

  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) { /* storage unavailable */ }
    if (!saved) {
      saved = window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches
        ? "light" : "dark";
    }
    applyTheme(saved);

    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var current = root.getAttribute("data-theme") === "light" ? "light" : "dark";
        var next = current === "light" ? "dark" : "light";
        applyTheme(next);
        try { localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* ignore */ }
      });
    });
  }

  /* ---------- Mobile nav ---------- */
  function initNav() {
    var toggle = document.querySelector(".nav-toggle");
    var links = document.querySelector(".nav-links");
    if (!toggle || !links) return;
    toggle.addEventListener("click", function () {
      var isOpen = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { links.classList.remove("open"); });
    });
  }

  /* ---------- Active nav link ---------- */
  function markActive() {
    var path = window.location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      var href = a.getAttribute("href");
      if (href === path || (path === "" && href === "index.html")) {
        a.classList.add("active");
      }
    });
  }

  /* ---------- Scroll reveal ---------- */
  function initReveal() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });

    // Safety net: if something goes wrong (e.g. an element never intersects),
    // never leave content permanently invisible.
    setTimeout(function () {
      items.forEach(function (el) { el.classList.add("in"); });
    }, 2500);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initNav();
    markActive();
    initReveal();
    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  });
})();
