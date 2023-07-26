// script.js
document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener("change", function () {
        if (this.checked) {
          const popup = document.getElementById("popup");
          popup.classList.add("show");
  
          const duration = 3000; // 3 segundos
  
          setTimeout(function () {
            popup.classList.remove("show");
          }, duration);
        }
      });
    });
  });
  