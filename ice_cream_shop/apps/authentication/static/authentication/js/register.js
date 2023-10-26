// Ожидаем пока документ будет полностью загружен
$(document).ready(function () {
    var container = $(".container-fluid");
    var card = $(".card");

    // Функция для обновления классов контейнера в зависимости от высоты
    function updateClasses() {
        // Получаем высоту окна и высоту карточки
        var windowHeight = $(window).height();
        var cardHeight = card.outerHeight();

        if (cardHeight >= windowHeight - 20) {
            container.removeClass("mt-lg-0 mb-lg-0");
        } else {
            container.addClass("mt-lg-0 mb-lg-0");
        }
    }
    // Добавляем обработчик события изменения размера окна
    $(window).resize(updateClasses);
    // Вызываем функцию updateClasses при загрузке страницы
    updateClasses();
});