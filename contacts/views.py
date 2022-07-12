from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ContactForm
from symcrm.access_filter import access_filter
from symcrm.choice_filter import choice_filter
from django.contrib import messages


@login_required(login_url='login')
def contacts_list(request):
    access = access_filter(request)
    contacts = choice_filter(access.contacts(), request)

    contacts.choice('actual', 'True')
    contacts.choice('emailing')
    contacts.choice('organisation', request.user.organisation.id)
    contacts.choice('user')

    context = {
        'page_header': 'Контакты',
        'contacts': contacts.list,
        'dropdown': access,
        'filter_choice': contacts.filter_choice
    }
    return render(request, 'customers/contacts/list.html', context)


@login_required(login_url='login')
def contacts_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:list')
    else:
        form = ContactForm()
        # значения по умолчанию при создании из карточки какой-либо сущности
        default_customer = request.GET.get('customer', '')
        form.fields['customer'].initial = default_customer

        # фильтрация списков выбора
        form.fields['customer'].queryset = access_filter(request).customers()

    context = {
        'page_header': 'Добавить контакт',
        'form': form
    }
    return render(request, 'customers/contacts/form.html', context)


@login_required(login_url='login')
def contacts_view(request, pk):
    contact = access_filter(request).contact(pk=pk)
    context = {'contact': contact}
    return render(request, 'customers/contacts/view.html', context)


@login_required(login_url='login')
def contacts_update(request, pk):
    contact = access_filter(request).contact(pk=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            context = {'contact': contact}
            return render(request, 'customers/contacts/view.html', context)
        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('contacts:view', pk=pk)
    else:
        context = {
            'page_header': 'Обновить контакт',
            'form': form
        }
    return render(request, 'customers/contacts/form.html', context)


@login_required(login_url='login')
@permission_required('contacts.delete_contact', raise_exception=True)
def contacts_delete(request, pk):
    contact = access_filter(request).contact(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:list')

    return render(request, 'delete-confirm.html', {'obj': contact})
