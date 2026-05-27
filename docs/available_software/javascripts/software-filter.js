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
  });
});

