(function () {
  var desktopQuery = window.matchMedia("(min-width: 961px)");

  function updateToggleState(toggle, notes) {
    var anyOpen = notes.some(function (note) { return note.open; });
    toggle.dataset.state = anyOpen ? "open" : "closed";
    toggle.setAttribute("aria-pressed", anyOpen ? "true" : "false");
  }

  function layoutNotes(notes) {
    var container = document.querySelector(".container");

    if (!container) {
      return;
    }

    if (!desktopQuery.matches) {
      container.style.minHeight = "";
      notes.forEach(function (note) {
        note.style.top = "";
      });
      return;
    }

    container.style.minHeight = "";

    var gap = 18;
    var bottom = 0;

    notes.forEach(function (note) {
      var anchor = note.previousElementSibling;
      var anchorTop = anchor && anchor.classList.contains("commentary-anchor")
        ? anchor.offsetTop
        : note.offsetTop;
      var top = Math.max(anchorTop, bottom + gap);

      note.style.top = top + "px";
      bottom = top + note.offsetHeight;
    });

    container.style.minHeight = Math.max(container.offsetHeight, bottom + 80) + "px";
  }

  function scheduleLayout(notes) {
    window.requestAnimationFrame(function () {
      layoutNotes(notes);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("commentary-toggle");
    var notes = Array.prototype.slice.call(document.querySelectorAll("details.commentary"));

    if (!toggle) {
      return;
    }

    if (notes.length === 0) {
      toggle.hidden = true;
      return;
    }

    notes.forEach(function (note) {
      note.open = false;
      note.addEventListener("toggle", function () {
        updateToggleState(toggle, notes);
        scheduleLayout(notes);
      });
    });

    updateToggleState(toggle, notes);
    layoutNotes(notes);

    toggle.addEventListener("click", function () {
      var shouldOpen = toggle.dataset.state !== "open";
      notes.forEach(function (note) {
        note.open = shouldOpen;
      });
      updateToggleState(toggle, notes);
      scheduleLayout(notes);
    });

    window.addEventListener("resize", function () {
      scheduleLayout(notes);
    });
  });
})();
