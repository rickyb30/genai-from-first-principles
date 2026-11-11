/* Generative AI from First Principles: the site's only script.
 *
 * Quizzes, flashcards (Leitner boxes), progress, search, the depth filter and the theme switch.
 * Everything is stored in this browser's localStorage, under one key. Nothing is sent anywhere.
 * Catalog data (lessons, levels, paths, glossary cards, search index) comes from data.js.
 */
(function () {
  "use strict";

  var KEY = "genai-fp-progress";
  var INTERVALS = { 1: 1, 2: 2, 3: 4, 4: 8, 5: 16 }; // Leitner box -> days until next review
  var CATALOG = window.CATALOG || { lessons: [], levels: [], paths: {}, cards: [], search: [] };
  var ROOT = document.body.getAttribute("data-root") || "";

  // --- Storage ---------------------------------------------------------------------------

  function emptyState() {
    return { version: 1, completed: {}, quiz: {}, cards: {}, settings: { depth: "red", theme: "auto", path: null } };
  }

  function load() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return emptyState();
      var data = JSON.parse(raw);
      var base = emptyState();
      ["completed", "quiz", "cards", "settings"].forEach(function (k) {
        if (data[k] && typeof data[k] === "object") base[k] = Object.assign(base[k], data[k]);
      });
      return base;
    } catch (e) {
      return emptyState();
    }
  }

  var state = load();

  function save() {
    try {
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {
      /* storage may be disabled (private mode): the site still works, it just won't remember */
    }
  }

  function today(offsetDays) {
    var d = new Date();
    d.setDate(d.getDate() + (offsetDays || 0));
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + day;
  }

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function el(tag, attrs, text) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { node.setAttribute(k, attrs[k]); });
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function lessonById(id) {
    for (var i = 0; i < CATALOG.lessons.length; i++) if (CATALOG.lessons[i].id === id) return CATALOG.lessons[i];
    return null;
  }

  // --- Theme -----------------------------------------------------------------------------

  function applyTheme() {
    var t = state.settings.theme;
    if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
    else document.documentElement.removeAttribute("data-theme");
    var btn = $("#theme-toggle");
    if (btn) {
      var label = { auto: "Theme: follows your system", light: "Theme: light", dark: "Theme: dark" }[t] || "Theme";
      btn.setAttribute("aria-label", label + ". Click to change.");
      btn.title = label;
    }
  }

  function initTheme() {
    applyTheme();
    var btn = $("#theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var order = ["auto", "light", "dark"];
      state.settings.theme = order[(order.indexOf(state.settings.theme) + 1) % order.length];
      save();
      applyTheme();
    });
  }

  // --- Math ------------------------------------------------------------------------------

  function renderMath() {
    if (!window.katex) return;
    $all(".math").forEach(function (node) {
      try {
        window.katex.render(node.textContent, node, {
          displayMode: node.classList.contains("block"),
          throwOnError: false
        });
      } catch (e) { /* leave the source text visible */ }
    });
  }

  // --- Search ----------------------------------------------------------------------------

  function initSearch() {
    var input = $("#search-input");
    var list = $("#search-results");
    if (!input || !list) return;
    var active = -1;

    function close() {
      list.hidden = true;
      input.setAttribute("aria-expanded", "false");
      active = -1;
    }

    function run() {
      var q = input.value.trim().toLowerCase();
      list.innerHTML = "";
      if (q.length < 2) { close(); return; }
      var words = q.split(/\s+/);
      var hits = [];
      CATALOG.search.forEach(function (item) {
        var title = item.title.toLowerCase();
        var text = (item.title + " " + item.text).toLowerCase();
        if (!words.every(function (w) { return text.indexOf(w) !== -1; })) return;
        var score = words.reduce(function (s, w) { return s + (title.indexOf(w) !== -1 ? 3 : 1); }, 0);
        if (title.indexOf(q) === 0) score += 5;
        hits.push({ item: item, score: score });
      });
      hits.sort(function (a, b) { return b.score - a.score; });
      hits.slice(0, 8).forEach(function (h, i) {
        var li = el("li", { role: "option", id: "search-opt-" + i });
        var a = el("a", { href: ROOT + h.item.url });
        a.appendChild(el("span", { "class": "result-kind" }, h.item.kind));
        a.appendChild(document.createTextNode(" " + h.item.title));
        li.appendChild(a);
        list.appendChild(li);
      });
      if (!hits.length) list.appendChild(el("li", { "class": "no-results" }, "No matches"));
      list.hidden = false;
      input.setAttribute("aria-expanded", "true");
    }

    input.addEventListener("input", run);
    input.addEventListener("keydown", function (e) {
      var links = $all("a", list);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        if (!links.length) return;
        e.preventDefault();
        active = (active + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach(function (a, i) { a.classList.toggle("active", i === active); });
        input.setAttribute("aria-activedescendant", "search-opt-" + active);
      } else if (e.key === "Enter" && active >= 0 && links[active]) {
        e.preventDefault();
        window.location.href = links[active].href;
      } else if (e.key === "Escape") {
        close();
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search")) close();
    });
  }

  // --- Lessons ---------------------------------------------------------------------------

  function applyDepth() {
    var depth = state.settings.depth || "red";
    var rank = { green: 1, yellow: 2, red: 3 };
    $all(".lesson-section[data-depth]").forEach(function (sec) {
      sec.hidden = rank[sec.getAttribute("data-depth")] > rank[depth];
    });
    $all(".toc li.green, .toc li.yellow, .toc li.red").forEach(function (li) {
      var d = li.classList.contains("green") ? "green" : li.classList.contains("yellow") ? "yellow" : "red";
      li.hidden = rank[d] > rank[depth];
    });
    $all(".depth-filter button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-depth") === depth));
    });
  }

  function initDepth() {
    if (!$(".depth-filter")) return;
    $all(".depth-filter button").forEach(function (b) {
      b.addEventListener("click", function () {
        state.settings.depth = b.getAttribute("data-depth");
        save();
        applyDepth();
      });
    });
    applyDepth();
  }

  function sameSet(a, b) {
    if (a.length !== b.length) return false;
    var s = a.slice().sort().join(",");
    return s === b.slice().sort().join(",");
  }

  function updateScore(quiz) {
    var lesson = quiz.getAttribute("data-lesson");
    var questions = $all(".question", quiz);
    var answered = questions.filter(function (q) { return q.hasAttribute("data-result"); });
    var correct = questions.filter(function (q) { return q.getAttribute("data-result") === "correct"; });
    var out = $(".quiz-score", quiz);
    if (answered.length < questions.length) {
      out.textContent = answered.length + " of " + questions.length + " answered.";
      return;
    }
    var prev = state.quiz[lesson];
    var best = prev ? Math.max(prev.best, correct.length) : correct.length;
    state.quiz[lesson] = { best: best, of: questions.length, last: correct.length, date: today() };
    save();
    out.textContent = "You scored " + correct.length + " out of " + questions.length +
      (best > correct.length ? " (your best is " + best + ")." : ".") +
      (correct.length < questions.length ? " Reread the explanations, then try again in a few days." : " Well done.");
  }

  function initQuiz() {
    $all(".quiz").forEach(function (quiz) {
      $all(".question", quiz).forEach(function (q) {
        var kind = q.getAttribute("data-kind");
        var answer = (q.getAttribute("data-answer") || "").split(",").filter(Boolean);
        var feedback = $(".feedback", q);

        function reveal() { q.classList.add("revealed"); }

        if (kind === "open") {
          $(".reveal", q).addEventListener("click", function () {
            reveal();
            $(".self-mark", q).hidden = false;
          });
          $(".got-it", q).addEventListener("click", function () {
            q.setAttribute("data-result", "correct");
            feedback.textContent = "Marked as got it.";
            updateScore(quiz);
          });
          $(".not-yet", q).addEventListener("click", function () {
            q.setAttribute("data-result", "incorrect");
            feedback.textContent = "Marked as not yet. Come back to this one.";
            updateScore(quiz);
          });
          return;
        }

        $(".check", q).addEventListener("click", function () {
          var chosen = $all("input:checked", q).map(function (i) { return i.value; });
          if (!chosen.length) {
            feedback.textContent = "Choose an answer first.";
            return;
          }
          var ok = sameSet(chosen, answer);
          q.setAttribute("data-result", ok ? "correct" : "incorrect");
          q.classList.toggle("is-correct", ok);
          q.classList.toggle("is-incorrect", !ok);
          feedback.textContent = ok ? "✓ Correct." : "✗ Not quite. The answer is " + answer.join(", ") + ".";
          $all("label.option", q).forEach(function (label) {
            var v = $("input", label).value;
            label.classList.toggle("right", answer.indexOf(v) !== -1);
          });
          reveal();
          updateScore(quiz);
        });
      });
    });
  }

  function initComplete() {
    $all(".mark-complete").forEach(function (btn) {
      var id = btn.getAttribute("data-lesson");
      var status = $(".complete-status", btn.parentNode);
      function show() {
        var done = !!state.completed[id];
        btn.textContent = done ? "Completed ✓ (click to undo)" : "Mark lesson as complete";
        btn.classList.toggle("done", done);
        status.textContent = done ? "Completed on " + state.completed[id] + ". Its key terms are now in your flashcard deck." : "";
      }
      btn.addEventListener("click", function () {
        if (state.completed[id]) delete state.completed[id];
        else state.completed[id] = today();
        save();
        show();
      });
      show();
    });
  }

  function initCopyButtons() {
    $all(".lesson pre").forEach(function (pre) {
      if (!navigator.clipboard) return;
      var btn = el("button", { type: "button", "class": "copy-btn" }, "Copy");
      btn.addEventListener("click", function () {
        navigator.clipboard.writeText(pre.innerText).then(function () {
          btn.textContent = "Copied";
          setTimeout(function () { btn.textContent = "Copy"; }, 1500);
        });
      });
      pre.appendChild(btn);
    });
  }

  // --- Curriculum, home and paths --------------------------------------------------------

  function initDoneMarks() {
    $all("tr[data-lesson]").forEach(function (tr) {
      var done = !!state.completed[tr.getAttribute("data-lesson")];
      tr.classList.toggle("is-done", done);
      var mark = $(".done-mark", tr);
      if (mark) mark.textContent = done ? "✓" : "";
      if (done) tr.setAttribute("aria-label", "Completed");
    });
  }

  function levelStats(level) {
    var built = level.lessons.filter(function (id) { var l = lessonById(id); return l && l.built; });
    var done = level.lessons.filter(function (id) { return state.completed[id]; });
    return { total: level.lessons.length, built: built.length, done: done.length };
  }

  function nextLesson(ids) {
    for (var i = 0; i < ids.length; i++) {
      var l = lessonById(ids[i]);
      if (l && l.built && !state.completed[l.id]) return l;
    }
    return null;
  }

  function initHome() {
    $all(".level-bar[data-level]").forEach(function (bar) {
      var lv = CATALOG.levels[Number(bar.getAttribute("data-level"))];
      if (!lv) return;
      var s = levelStats(lv);
      $("span", bar).style.width = (s.total ? (100 * s.done / s.total) : 0) + "%";
      bar.title = s.done + " of " + s.total + " completed";
    });
    var link = $("#continue-link");
    if (!link) return;
    var path = state.settings.path && CATALOG.paths[state.settings.path];
    var ids = path ? path.lessons : CATALOG.lessons.map(function (l) { return l.id; });
    var any = Object.keys(state.completed).length > 0;
    var next = nextLesson(ids);
    if (any && next) {
      link.textContent = "Continue: " + next.id + " " + next.title;
      link.href = ROOT + next.url;
    }
  }

  function pathSummary(pid) {
    var path = CATALOG.paths[pid];
    var built = path.lessons.filter(function (id) { var l = lessonById(id); return l && l.built; });
    var done = path.lessons.filter(function (id) { return state.completed[id]; });
    return { path: path, total: path.lessons.length, built: built.length, done: done.length };
  }

  function initPaths() {
    $all(".path-progress[data-path]").forEach(function (box) {
      var s = pathSummary(box.getAttribute("data-path"));
      box.textContent = s.total + " lessons in this path · " + s.built + " available now · " + s.done + " completed";
    });
    $all(".follow-path").forEach(function (btn) {
      var pid = btn.getAttribute("data-path");
      function show() {
        var on = state.settings.path === pid;
        btn.textContent = on ? "Following this path ✓" : "Follow this path";
        btn.classList.toggle("primary", on);
        btn.setAttribute("aria-pressed", String(on));
      }
      btn.addEventListener("click", function () {
        state.settings.path = state.settings.path === pid ? null : pid;
        save();
        $all(".follow-path").forEach(function (b) { b.dispatchEvent(new Event("refresh")); });
      });
      btn.addEventListener("refresh", show);
      show();
    });
  }

  // --- Flashcards ------------------------------------------------------------------------

  function initFlashcards() {
    var box = $(".flashcards");
    if (!box) return;
    var deckSelect = $("#fc-deck");
    var current = null;

    function deck() {
      var mode = deckSelect.value;
      return CATALOG.cards.filter(function (c) { return mode === "all" || state.completed[c.lesson]; });
    }

    function due(cards) {
      var t = today();
      return cards.filter(function (c) {
        var s = state.cards[c.id];
        return !s || s.due <= t;
      }).sort(function (a, b) {
        var sa = state.cards[a.id], sb = state.cards[b.id];
        return ((sa ? sa.box : 0) - (sb ? sb.box : 0)) || a.term.localeCompare(b.term);
      });
    }

    function show() {
      var cards = deck();
      var queue = due(cards);
      $(".fc-due", box).textContent = queue.length + " due today, " + cards.length + " cards in this deck";
      $(".card-back", box).hidden = true;
      $(".fc-show", box).hidden = false;
      $(".fc-knew", box).hidden = true;
      $(".fc-missed", box).hidden = true;
      current = queue[0] || null;
      if (!current) {
        $(".card-term", box).textContent = cards.length
          ? "All caught up. Come back tomorrow for the next reviews."
          : "No cards yet. Complete a lesson, or switch to “All terms”.";
        $(".fc-show", box).hidden = true;
        return;
      }
      var s = state.cards[current.id];
      $(".card-side", box).textContent = "Term" + (s ? " · box " + s.box : " · new");
      $(".card-term", box).textContent = current.term;
      $(".card-def", box).textContent = current.definition.replace(/[*_`]/g, "");
    }

    function grade(knew) {
      if (!current) return;
      var s = state.cards[current.id] || { box: 1 };
      var newBox = knew ? Math.min((state.cards[current.id] ? s.box + 1 : 2), 5) : 1;
      state.cards[current.id] = { box: newBox, due: today(INTERVALS[newBox]) };
      save();
      show();
      $(".card", box).focus();
    }

    deckSelect.value = Object.keys(state.completed).length ? "completed" : "all";
    deckSelect.addEventListener("change", show);
    $(".fc-show", box).addEventListener("click", function () {
      $(".card-back", box).hidden = false;
      $(".fc-show", box).hidden = true;
      $(".fc-knew", box).hidden = false;
      $(".fc-missed", box).hidden = false;
      $(".fc-knew", box).focus();
    });
    $(".fc-knew", box).addEventListener("click", function () { grade(true); });
    $(".fc-missed", box).addEventListener("click", function () { grade(false); });
    show();
  }

  // --- Progress page ---------------------------------------------------------------------

  function bar(done, total) {
    var wrap = el("span", { "class": "progress-bar", role: "img", "aria-label": done + " of " + total });
    var fill = el("span");
    fill.style.width = (total ? 100 * done / total : 0) + "%";
    wrap.appendChild(fill);
    return wrap;
  }

  function initProgressPage() {
    var levelsBox = $("#level-progress");
    if (!levelsBox) return;

    var table = el("table", { "class": "simple" });
    table.innerHTML = "<thead><tr><th>Level</th><th>Completed</th><th></th></tr></thead>";
    var tbody = el("tbody");
    CATALOG.levels.forEach(function (lv) {
      var s = levelStats(lv);
      var tr = el("tr");
      tr.appendChild(el("td", {}, "Level " + lv.number + " — " + lv.title));
      tr.appendChild(el("td", { "class": "nowrap" }, s.done + " of " + s.total + (s.built < s.total ? " (" + s.built + " available)" : "")));
      var td = el("td");
      td.appendChild(bar(s.done, s.total));
      tr.appendChild(td);
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    levelsBox.appendChild(table);

    var pathBox = $("#path-progress");
    if (state.settings.path && CATALOG.paths[state.settings.path]) {
      var ps = pathSummary(state.settings.path);
      pathBox.appendChild(el("p", {}, ps.path.name + ": " + ps.done + " of " + ps.total + " lessons completed (" + ps.built + " available so far)."));
      pathBox.appendChild(bar(ps.done, ps.total));
      var next = nextLesson(ps.path.lessons);
      if (next) {
        var p = el("p");
        p.appendChild(document.createTextNode("Next: "));
        p.appendChild(el("a", { href: ROOT + next.url }, next.id + " " + next.title));
        pathBox.appendChild(p);
      }
    } else {
      var p2 = el("p");
      p2.appendChild(document.createTextNode("You aren't following a path yet. "));
      p2.appendChild(el("a", { href: ROOT + "paths.html" }, "Choose one"));
      p2.appendChild(document.createTextNode("."));
      pathBox.appendChild(p2);
    }

    var quizBox = $("#quiz-progress");
    var ids = Object.keys(state.quiz).sort();
    if (!ids.length) quizBox.appendChild(el("p", {}, "No quizzes taken yet."));
    else {
      var qt = el("table", { "class": "simple" });
      qt.innerHTML = "<thead><tr><th>Lesson</th><th>Best</th><th>Last</th><th>Date</th></tr></thead>";
      var qb = el("tbody");
      ids.forEach(function (id) {
        var r = state.quiz[id];
        var l = lessonById(id);
        var tr = el("tr");
        var td = el("td");
        td.appendChild(l ? el("a", { href: ROOT + l.url }, id + " " + l.title) : document.createTextNode(id));
        tr.appendChild(td);
        tr.appendChild(el("td", {}, r.best + " / " + r.of));
        tr.appendChild(el("td", {}, r.last + " / " + r.of));
        tr.appendChild(el("td", {}, r.date || ""));
        qb.appendChild(tr);
      });
      qt.appendChild(qb);
      quizBox.appendChild(qt);
    }

    var cardBox = $("#card-progress");
    var boxes = [0, 0, 0, 0, 0];
    var dueCount = 0, t = today();
    Object.keys(state.cards).forEach(function (id) {
      var s = state.cards[id];
      boxes[s.box - 1] += 1;
      if (s.due <= t) dueCount += 1;
    });
    var studied = boxes.reduce(function (a, b) { return a + b; }, 0);
    cardBox.appendChild(el("p", {}, studied
      ? studied + " cards studied, " + dueCount + " due today. Cards per box: " + boxes.map(function (n, i) { return "box " + (i + 1) + ": " + n; }).join(", ") + "."
      : "No flashcards studied yet."));
    var a = el("a", { href: ROOT + "glossary.html#fc-title" }, "Go to flashcards");
    cardBox.appendChild(a);

    var status = $("#data-status");
    $("#export-progress").addEventListener("click", function () {
      var blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
      var link = el("a", { href: URL.createObjectURL(blob), download: "genai-progress-" + today() + ".json" });
      document.body.appendChild(link);
      link.click();
      link.remove();
      status.textContent = "Progress exported.";
    });
    $("#import-progress").addEventListener("change", function (e) {
      var file = e.target.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var data = JSON.parse(reader.result);
          if (!data || data.version !== 1) throw new Error("not a progress file");
          localStorage.setItem(KEY, JSON.stringify(data));
          status.textContent = "Progress imported. Reloading…";
          setTimeout(function () { location.reload(); }, 600);
        } catch (err) {
          status.textContent = "That file isn't a valid progress export.";
        }
      };
      reader.readAsText(file);
    });
    $("#reset-progress").addEventListener("click", function () {
      if (!window.confirm("Delete all your progress on this device? This can't be undone.")) return;
      try { localStorage.removeItem(KEY); } catch (err) { /* ignore */ }
      status.textContent = "All progress deleted. Reloading…";
      setTimeout(function () { location.reload(); }, 600);
    });
  }

  // --- Start -----------------------------------------------------------------------------

  function start() {
    initTheme();
    renderMath();
    initSearch();
    initDepth();
    initQuiz();
    initComplete();
    initCopyButtons();
    initDoneMarks();
    initHome();
    initPaths();
    initFlashcards();
    initProgressPage();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
