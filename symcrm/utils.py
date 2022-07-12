from contacts.models import Contact
from projects.models import Project
from django.http import JsonResponse


# функция составления списка выбора зависимых форм
def dependent_select_options(request):

    select_value = request.GET.get('select_value', '')
    # делаем невозможным выбор контактов и проектов, если нет клиента
    select_value = select_value if select_value != '' else 0

    dependent_select = request.GET.get('dependent_select')
    ajax_response = {}
    elements_set = ''

    if dependent_select == 'contact':
        elements_set = Contact.objects.filter(customer=select_value).filter(actual=True)

    if dependent_select == 'project':
        elements_set = Project.objects.filter(customer=select_value).filter(archive=False)

    for e in elements_set:
        ajax_response[e.pk] = e.display

    response = {
        'ajax_response': ajax_response
    }
    return JsonResponse(response)

