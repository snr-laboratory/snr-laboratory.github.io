(function () {
  function updateToggleState(toggle, notes) {
    var anyOpen = notes.some(function (note) { return note.open; });
    toggle.dataset.state = anyOpen ? "open" : "closed";
    toggle.setAttribute("aria-pressed", anyOpen ? "true" : "false");
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
      });
    });

    updateToggleState(toggle, notes);

    toggle.addEventListener("click", function () {
      var shouldOpen = toggle.dataset.state !== "open";
      notes.forEach(function (note) {
        note.open = shouldOpen;
      });
      updateToggleState(toggle, notes);
    });
  });
})();
