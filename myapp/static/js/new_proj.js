const newProjButton = document.getElementById("new-project");
const newProjModal = document.querySelector(".new-project-modal");
const newProjModalClose = document.querySelector(".new-project-modal-close");
const newProjForm = document.getElementById("new-project-form");
const newProjFormButton = document.getElementById("new-project-form-button");
const deleteProjButtons = document.querySelectorAll(".delete-project-btn");
const tip = document.querySelector(".tip");
const url = newProjForm.action;
const csrfToken = document.querySelector(
  "input[name='csrfmiddlewaretoken']"
).value;
let found = false;
newProjButton.addEventListener("click", function () {
  newProjModal.classList.add("view");
  found = true;
});
newProjModalClose.addEventListener("click", function () {
  newProjModal.classList.remove("view");
});
newProjForm.addEventListener("submit", function (e) {
  e.preventDefault();
  yes();
});
function yes() {
  const formData = new FormData();
  const projName = document.getElementById("project-name").value;
  if (projName.trim().split(" ").length != 1) {
    tip.textContent = "Project Name should not contain spaces";
    tip.style.color = "pink";
  } else {
    formData.append("name", projName.trim());
    fetch(url, {
      method: "POST",
      cache: "no-cache",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrfToken,
      },
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.exist) {
          tip.textContent = "Project with this name already Exists";
        } else {
          window.location = "/adwiti/" + data.user + "/" + data.p_name;
        }
      });
  }
}
deleteProjButtons.forEach((deleteProjButton) => {
  deleteProjButton.addEventListener("click", function () {
    const formData = new FormData();
    formData.append("id", this.dataset.projectId);
    this.setAttribute("disabled", "disabled");
    fetch("/deleteProj/", {
      method: "POST",
      cache: "no-cache",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": this.dataset.csrfToken,
      },
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.message == "success") {
          window.location = "/dashboard/";
        } else {
          window.location = "/dashboard/";
        }
      });
  });
});
