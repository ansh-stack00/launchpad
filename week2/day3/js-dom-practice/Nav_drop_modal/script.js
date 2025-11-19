
const toggleBtn = document.querySelector(".toggle-btn");
const navLinks = document.querySelector(".nav-links");

toggleBtn.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

const dropdown = document.querySelector(".dropdown");
const dropBtn = document.querySelector(".drop-btn");

dropBtn.addEventListener("click", (e) => {
  e.preventDefault(); 
  dropdown.classList.toggle("active");
});


window.addEventListener("click", (e) => {
  if (!dropdown.contains(e.target) && !dropBtn.contains(e.target)) {
    dropdown.classList.remove("active");
  }
});


const modal = document.querySelector("#modal");
const openModalBtn = document.querySelector("#openModal");
const closeModalBtn = document.querySelector("#closeModal");
const closeModalBtn2 = document.querySelector("#closeModalBtn");

openModalBtn.addEventListener("click", (e) => {
  e.preventDefault();
  modal.style.display = "flex";
});

closeModalBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

closeModalBtn2.addEventListener("click", () => {
  modal.style.display = "none";
});


window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});
