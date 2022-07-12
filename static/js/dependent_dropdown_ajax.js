function linkedListUpload(e) {
    let select_id = e.id
    let select_value = e.value

    /* находим все элементы, которые зависят от измененного select. Для каждого запускаем функцию dependentSelectUpdateByAjax */
    let selectsSet = document.getElementsByTagName('select')
    for (i = 0; i < selectsSet.length; i++) {
        if (selectsSet[i].dataset['depend'] === select_id.slice(3)) {
            let dependent_select_id = selectsSet[i].id
            dependentSelectUpdateByAjax(select_value, dependent_select_id)
        }
    }
}

/* функция обновления зависимого выпадающего списка через ajax */
function dependentSelectUpdateByAjax(select_value, dependent_select_id){
    let dependentSelect = $('#'+dependent_select_id);
    let optionList = '<option value="">---------</option>';

    $.ajax({
        type: 'GET',
        url: '/dependent_select',
        data: {
            'select_value': select_value,
            'dependent_select': dependent_select_id.slice(3)
        },
        success: function(response) {
            $.each(response['ajax_response'], function(k ,v){
                optionList += '<option value=' + k + '>' + v + '</option>';
            });
            dependentSelect.html(optionList)
        }
    });
}