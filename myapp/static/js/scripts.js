(function () {
  const navigationButton = document.querySelector(
    ".mobile-nav > nav > #nav-btn"
  );
  const mobileNavigation = document.querySelector(".mobile-nav");
  const htmlElement = document.querySelector("html");
  navigationButton.addEventListener("click", function () {
    const navigationButtonImage = this.querySelector("img");
    const navigationButtonImageSource =
      navigationButtonImage.getAttribute("src");
    const sourceToSet =
      navigationButtonImageSource === "/static/images/icon-hamburger.svg"
        ? "/static/images/icon-close.svg"
        : "/static/images/icon-hamburger.svg";
    mobileNavigation.classList.toggle("view");
    htmlElement.classList.toggle("no-scroll");
    navigationButtonImage.setAttribute("src", sourceToSet);
  });
  const mobileAnchors = mobileNavigation.querySelectorAll("a");
  mobileAnchors.forEach((mobileAnchor) => {
    mobileAnchor.addEventListener("click", function () {
      navigationButton.click();
    });
  });
})();
