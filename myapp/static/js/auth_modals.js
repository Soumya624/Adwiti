(function () {
  const loginLinks = document.querySelectorAll(".invoke-login");
  const registerLinks = document.querySelectorAll(".invoke-register");
  const loginModal = document.querySelector(".modal-container.login-modal");
  const registerModal = document.querySelector(
    ".modal-container.register-modal"
  );
  const loginModalClose = document.querySelector(
    ".modal-container .login-modal-close"
  );
  const registerModalClose = document.querySelector(
    ".modal-container .register-modal-close"
  );
  loginLinks.forEach(function (loginLink) {
    loginLink.addEventListener("click", function (e) {
      e.preventDefault();
      registerModal.classList.remove("view");
      loginModal.classList.add("view");
    });
  });
  registerLinks.forEach(function (registerLink) {
    registerLink.addEventListener("click", function (e) {
      e.preventDefault();
      loginModal.classList.remove("view");
      registerModal.classList.add("view");
    });
  });
  loginModalClose.addEventListener("click", function () {
    loginModal.classList.remove("view");
  });
  registerModalClose.addEventListener("click", function () {
    registerModal.classList.remove("view");
  });
})();
