from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomerForm
from symcrm.access_filter import access_filter
from symcrm.choice_filter import choice_filter
from django.contrib import messages


@login_required(login_url='login')
def customers_list(request):
    access = access_filter(request)
    customers = choice_filter(access.customers(), request)

    customers.choice('priority')
    customers.choice('organisation_customer', request.user.organisation.id)
    customers.choice('user_customer')

    context = {
        'page_header': 'Клиенты',
        'customers': customers.list,
        'dropdown': access,
        'filter_choice': customers.filter_choice
    }
    return render(request, 'customers/list.html', context)


@login_required(login_url='login')
@permission_required('customers.add_customer', raise_exception=True)
def customers_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # урезаем начало адреса сайта
            if instance.website:
                instance.website = instance.website.replace('http://', '').replace('https://', '')
            instance.save()
            return redirect('customers:list')
    else:
        form = CustomerForm()
        form.fields['responsible'].queryset = access_filter(request).users()

    context = {
        'page_header': 'Добавить клиента',
        'form': form
    }
    return render(request, 'customers/form.html', context)


@login_required(login_url='login')
def customers_view(request, pk):
    customer = access_filter(request).customer(pk)
    tasks = customer.task_set.all()
    contacts = customer.contact_set.all()
    projects = customer.project_set.all()
    samples = customer.sample_set.all()

    context = {
        'customer': customer,
        'tasks': tasks,
        'contacts': contacts,
        'projects': projects,
        'samples': samples,
        'subform_settings': '_customer_subform',
    }
    return render(request, 'customers/view.html', context)


@login_required(login_url='login')
def customers_update(request, pk):
    customer = access_filter(request).customer(pk)
    form = CustomerForm(instance=customer)
    form.fields['responsible'].queryset = access_filter(request).users()

    if not request.user.has_perm('customers.manage_customer'):
        form.fields['title'].disabled = 'True'

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            instance = form.save(commit=False)
            # урезаем начало адреса сайта
            if instance.website:
                instance.website = instance.website.replace('http://', '').replace('https://', '')
            form.save()
            context = {'customer': customer}
            return render(request, 'customers/view.html', context)
        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('customers:view', pk=pk)
    else:
        context = {
            'page_header': 'Обновить клиента',
            'form': form
        }
    return render(request, 'customers/form.html', context)


@login_required(login_url='login')
@permission_required('customers.delete_customer', raise_exception=True)
def customers_delete(request, pk):
    customer = access_filter(request).customer(pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customers:list')

    return render(request, 'delete-confirm.html', {'obj': customer})
