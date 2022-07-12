$(document).ready(function() {
    $('.select2').select2({
        theme: "bootstrap4",
        language: {
            noResults: function (params) {
                return "нет подходящих результатов";
            }
        },
    });
});