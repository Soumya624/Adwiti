(function () {
  const navButton = document.querySelector(".mobile-only-nav-btn button");
  const mobileNav = document.querySelector(".mobile-only-nav");
  navButton.addEventListener("click", function () {
    mobileNav.classList.toggle("view");
  });
  const notesNav = document.querySelector(".notes-nav");
  const modalRight = document.querySelector(".modal-right");
  notesNav.addEventListener("click", function () {
    modalRight.classList.toggle("view");
  });
})();
