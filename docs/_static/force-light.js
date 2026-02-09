localStorage.setItem("theme", "light");

if (document.body) {
  document.body.dataset.theme = "light";
} else {
  document.addEventListener("DOMContentLoaded", () => {
    document.body.dataset.theme = "light";
  });
}
