$(document).ready(function() {

    $('#customers_list').DataTable({
        order: [[2, 'asc']],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#contacts_list').DataTable({
        order: [[6, 'asc'],[1, 'asc']],
        columnDefs : [{ 'visible': false, 'targets': [6] }],
        dom: 'lBfrtip',
        buttons: {
            dom: {
                button: {className: 'btn btn-light btn-sm ml-1'}
            },
            buttons: ['excel', 'print'],
        },
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#contacts_list_customer_subform').DataTable({
        lengthChange: false,
        order: [[6, 'asc'],[1, 'asc']],
        columnDefs : [{ 'visible': false, 'targets': [2] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#tasks_list').DataTable({
        order: [[2, 'asc'],[1, 'asc']],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#tasks_list_customer_subform').DataTable({
        lengthChange: false,
        order: [[6, 'asc'], [2, 'asc']],
        columnDefs : [{ 'visible': false, 'targets': [5] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#tasks_list_project_subform').DataTable({
        lengthChange: false,
        order: [[6, 'asc'], [2, 'asc']],
        columnDefs : [{ 'visible': false, 'targets': [5] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#tasks_list_product_subform').DataTable({
        lengthChange: false,
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#projects_list').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#projects_list_customer_subform').DataTable({
        lengthChange: false,
        order: [[4, 'asc']],
        columnDefs : [{ 'visible': false, 'targets': [3] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#samples_list').DataTable({
        dom: 'lBfrtip',
        buttons: {
            dom: {
                button: {className: 'btn btn-light btn-sm ml-1'}
            },
            buttons: ['excel', 'print'],
        },
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#samples_list_customer_subform').DataTable({
        lengthChange: false,
        columnDefs : [{ 'visible': false, 'targets': [2] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#samples_list_project_subform').DataTable({
        lengthChange: false,
        columnDefs : [{ 'visible': false, 'targets': [2, 3] }],
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#samples_list_product_subform').DataTable({
        lengthChange: false,
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#products_list').DataTable({
        order: [[1, 'asc']],
        dom: 'lBfrtip',
        buttons: {
            dom: {
                button: {className: 'btn btn-light btn-sm ml-1'}
            },
            buttons: ['excel', 'print'],
        },
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });

    $('#users_list').DataTable({
        language: {url: "//cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json"},
    });
} );