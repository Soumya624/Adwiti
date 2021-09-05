(function () {
  const options = document.querySelectorAll(".options li");
  const hideTargets = function () {
    document.querySelectorAll(".expansions > *").forEach((element) => {
      element.classList.remove("view");
    });
  };
  options.forEach(function (option) {
    const target = option.dataset.target;
    const targetElement = document.getElementById(target);
    option.addEventListener("click", function () {
      hideTargets();
      targetElement.classList.add("view");
    });
  });
})();
