// Функция для установки выбранных фильтров
function setSelectedFilters(filterName, selectedValues) {
    selectedValues.forEach(function (value) {
        $("#" + filterName + value).prop("checked", true);
    });
}

function setupFilterRange(filterName, max, selectedMin, selectedMax) {
    var filterRange = $("#" + filterName + "-range");
    var minInput = $("#min-" + filterName);
    var maxInput = $("#max-" + filterName);

    filterRange.slider({
        range: true,
        min: 0,
        max: max,
        values: [selectedMin, selectedMax],
        slide: function (event, ui) {
            minInput.val(ui.values[0]);
            maxInput.val(ui.values[1]);
        }
    });

    // Установка начальных значений полей ввода
    minInput.val(filterRange.slider("values", 0));
    maxInput.val(filterRange.slider("values", 1));

    // Обработчики событий для полей ввода
    minInput.on("change", function () {
        var newMin = minInput.val();
        var currentMax = filterRange.slider("values", 1);
        if (newMin >= 0 && newMin < currentMax) {
            filterRange.slider("values", 0, newMin);
        }
    });

    maxInput.on("change", function () {
        var currentMin = filterRange.slider("values", 0);
        var newMax = maxInput.val();
        if (newMax > currentMin && newMax <= max) {
            filterRange.slider("values", 1, newMax);
        }
    });
}