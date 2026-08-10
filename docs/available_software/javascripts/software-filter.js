/*
 * Javascript for search box in software overview page (see docs/available_software/index.md)
 */
document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("software-search");
  const cards = document.querySelectorAll(".software-card");

  input.addEventListener("input", () => {
    const q = input.value.toLowerCase();

    cards.forEach(card => {
      const li = card.closest("li");
      const text = card.dataset.search.toLowerCase();
      li.style.display = text.includes(q) ? "" : "none";
    });

    const url = new URL(window.location);
    if (input.value) {
      url.searchParams.set("search", input.value);
    } else {
      url.searchParams.delete("search");
    }
    history.replaceState(null, "", url);
  });

  const search = new URLSearchParams(window.location.search).get("search");
  if (search) {
    input.value = search;
    input.dispatchEvent(new Event("input"));
  }
});
