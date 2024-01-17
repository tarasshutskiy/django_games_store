 // Відслідковуємо подію завантаження сторінки
  document.addEventListener('DOMContentLoaded', function() {
    // Отримуємо елементи кнопки та блоку контенту
    var responsiveButton = document.getElementById('responsiveButton');
    var collapseExample = document.getElementById('collapseExample');

    // Визначаємо ширину екрану та встановлюємо/видаляємо клас 'show'
    function checkWidth() {
      if (window.innerWidth >= 768) {
        collapseExample.classList.add('show');
      } else {
        collapseExample.classList.remove('show');
      }
    }

    // Викликаємо перевірку ширини екрану при завантаженні та ресайзі
    checkWidth();
    window.addEventListener('resize', checkWidth);
  });