
const headers = document.querySelectorAll('.accordion-header');

headers.forEach(header => {
  header.addEventListener('click', () => {
    console.log(header.parentElement);
    header.parentElement.classList.toggle('active');
  });
});