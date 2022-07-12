from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from symcrm.access_filter import access_filter, products_filter
from .forms import SampleForm
from django.contrib import messages
import datetime
from symcrm.choice_filter import choice_filter
from .models import Sample


@login_required(login_url='login')
def samples_list(request):
    access = access_filter(request)
    dropdown_statuses = Sample.STATUSES
    samples = choice_filter(access.samples(), request)
    status_date_from_default = str(datetime.date.today() - datetime.timedelta(days=30))
    status_date_till_default = str(datetime.date.today())

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')
    samples.choice('status')
    samples.choice('status_date_from', status_date_from_default)
    samples.choice('status_date_till', status_date_till_default)

    context = {
        'page_header': 'Образцы все',
        'samples': samples.list,
        'dropdown': access,
        'dropdown_statuses': dropdown_statuses,
        'filter_choice': samples.filter_choice
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_create(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status_date = datetime.datetime.now()
            instance.save()
            return redirect('samples:list')
    else:
        form = SampleForm()
        # значения по умолчанию при создании из карточки какой-либо сущности
        default_customer = request.GET.get('customer', '')
        default_product = request.GET.get('product', '')
        default_project = request.GET.get('project', '')
        default_contact = ''

        if default_project != '':
            project = access_filter(request).project(pk=default_project)
            default_customer = project.customer
            default_contact = project.customer

        form.fields['customer'].initial = default_customer
        form.fields['contact'].initial = default_contact
        form.fields['product'].initial = default_product
        form.fields['project'].initial = default_project

        # фильтрация списков выбора
        form.fields['product'].queryset = products_filter(actual=True)
        form.fields['customer'].queryset = access_filter(request).customers()
        form.fields['contact'].queryset = access_filter(request).contacts(customer=0, actual=True)
        form.fields['project'].queryset = access_filter(request).projects(customer=0, archive=False)

    context = {
        'page_header': 'Добавить образец',
        'form': form
    }
    return render(request, 'customers/samples/form.html', context)


@login_required(login_url='login')
def samples_view(request, pk):
    sample = access_filter(request).sample(pk=pk)
    context = {'sample': sample}
    return render(request, 'customers/samples/view.html', context)


@login_required(login_url='login')
def samples_update(request, pk):
    sample = access_filter(request).sample(pk=pk)
    status_initial = sample.status

    # не возможны корректировки, если статус образца win и нет прав на manage_samples
    if sample.status == 'win' and not request.user.has_perm('samples.manage_sample'):
        messages.warning(request, 'Статус образца - win. Для корректировок обратитесь к представителю Symrise')
        return redirect('samples:view', sample.id)

    form = SampleForm(instance=sample)
    form.fields['product'].queryset = products_filter(actual=True, chosen=sample.product)
    form.fields['customer'].queryset = access_filter(request).customers()
    form.fields['contact'].queryset = access_filter(request).contacts(customer=sample.customer if sample.customer else 0, actual=True, chosen=sample.contact)
    form.fields['project'].queryset = access_filter(request).projects(customer=sample.customer if sample.customer else 0, archive=False, chosen=sample.project)

    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save(commit=False)
            # если изменился статус - меняем дату статуса
            if status_initial != form.instance.status:
                form.instance.status_date = datetime.datetime.now()
            form.save()

            context = {'sample': sample}
            return render(request, 'customers/samples/view.html', context)
        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('samples:view', pk=pk)

    context = {
        'page_header': 'Обновить образец',
        'form': form
    }
    return render(request, 'customers/samples/form.html', context)


@login_required(login_url='login')
def samples_delete(request, pk):
    sample = access_filter(request).sample(pk=pk)
    # не возможны корректировки, если статус образца win и нет прав на manage_samples
    if not request.user.has_perm('samples.manage_sample'):
        messages.warning(request, 'Для корректировок обратитесь к представителю Symrise')
        return redirect('samples:view', sample.id)

    if request.method == 'POST':
        sample.delete()
        return redirect('samples:list')

    return render(request, 'delete-confirm.html', {'obj': sample})


@login_required(login_url='login')
def samples_list_on_testing(request):
    access = access_filter(request)
    samples_initial = access.samples().filter(status='on_testing')
    samples = choice_filter(samples_initial, request)

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')

    context = {
        'page_header': 'Образцы на тестировании',
        'samples': samples.list,
        'dropdown': access,
        'filter_choice': samples.filter_choice
    }

    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_win(request):
    access = access_filter(request)
    samples_initial = access.samples().filter(status='win')
    status_date_from_default = str(datetime.date.today() - datetime.timedelta(days=30))
    status_date_till_default = str(datetime.date.today())

    samples = choice_filter(samples_initial, request)

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')
    samples.choice('status_date_from', status_date_from_default)
    samples.choice('status_date_till', status_date_till_default)

    context = {
        'page_header': 'Образцы в статусе win',
        'samples': samples.list,
        'dropdown': access,
        'filter_choice': samples.filter_choice
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_declined_properties(request):
    access = access_filter(request)
    samples_initial = access.samples().filter(status='declined_by_properties')
    status_date_from_default = str(datetime.date.today() - datetime.timedelta(days=30))
    status_date_till_default = str(datetime.date.today())

    samples = choice_filter(samples_initial, request)

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')
    samples.choice('status_date_from', status_date_from_default)
    samples.choice('status_date_till', status_date_till_default)

    context = {
        'page_header': 'Образцы отклоненные по свойствам',
        'samples': samples.list,
        'dropdown': access,
        'filter_choice': samples.filter_choice
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_declined_price(request):
    access = access_filter(request)
    samples_initial = access.samples().filter(status='declined_by_price')
    status_date_from_default = str(datetime.date.today() - datetime.timedelta(days=30))
    status_date_till_default = str(datetime.date.today())

    samples = choice_filter(samples_initial, request)

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')
    samples.choice('status_date_from', status_date_from_default)
    samples.choice('status_date_till', status_date_till_default)

    context = {
        'page_header': 'Образцы отклоненные по цене',
        'samples': samples.list,
        'dropdown': access,
        'filter_choice': samples.filter_choice
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_send(request):
    samples = access_filter(request).samples()
    status_to_send = Q(status='to_send')
    status_to_get = Q(status='to_get')
    own_customers = Q(customer__responsible__organisation=request.user.organisation)
    send_indirectly = Q(direct=False)

    # если пользователь из Symrise
    if request.user.organisation.manager is None:
        q1 = Q(status_to_send & own_customers)  # у своих клиентов статус to send
        q2 = Q(status_to_get & ~own_customers)  # у прочих клиентов статус to get
        samples = samples.filter(q1 | q2)
    else:
        q1 = Q(status_to_send & send_indirectly)  # у прочих клиентов статус to send и отправка напрямую
        samples = samples.filter(q1)

    context = {
        'page_header': 'Образцы на отправку',
        'samples': samples
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_send_directly(request):
    status_to_send = Q(status='to_send')
    send_directly = Q(direct=True)
    samples = access_filter(request).samples().filter(status_to_send & send_directly)

    context = {
        'page_header': 'Образцы на прямую отправку',
        'samples': samples
    }
    return render(request, 'customers/samples/list.html', context)


@login_required(login_url='login')
def samples_list_abandoned(request):
    access = access_filter(request)
    status_date_default = str(datetime.date.today() - datetime.timedelta(days=90))
    samples_initial = access.samples().filter(status='on_testing').filter(status_date__lt=status_date_default)

    samples = choice_filter(samples_initial, request)

    samples.choice('organisation')
    samples.choice('user')
    samples.choice('important')

    context = {
        'page_header': 'Образцы заброшены: статус не обновлялся более 90 дней',
        'samples': samples.list,
        'dropdown': access,
        'filter_choice': samples.filter_choice
    }
    return render(request, 'customers/samples/list.html', context)