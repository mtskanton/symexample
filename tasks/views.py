from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from symcrm.access_filter import access_filter, products_filter
from .forms import TaskForm
from django.contrib import messages
import datetime
from symcrm.choice_filter import choice_filter


@login_required(login_url='login')
def tasks_list(request):
    access = access_filter(request)
    tasks_initial = access.tasks().filter(responsible=request.user)
    tasks = choice_filter(tasks_initial, request)

    tasks.choice('done', 'False')
    tasks.choice('reminder_from')
    tasks.choice('reminder_till')

    context = {
        'page_header': 'Задачи',
        'tasks': tasks.list,
        'dropdown': access,
        'filter_choice': tasks.filter_choice
    }
    return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def tasks_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            # указываем создателя по умолчанию
            instance.creator = request.user
            # если задача отмечена выполненной проставляем дату выполнения
            if form.cleaned_data['done'] is True:
                instance.done_date = datetime.datetime.now()
            instance.save()
            return redirect('tasks:list')
    else:
        form = TaskForm()
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
        form.fields['responsible'].queryset = access_filter(request).users()
        form.fields['responsible'].initial = request.user
        form.fields['customer'].queryset = access_filter(request).customers()
        form.fields['contact'].queryset = access_filter(request).contacts(customer=0, actual=True)
        form.fields['project'].queryset = access_filter(request).projects(customer=0, archive=False)
        form.fields['product'].queryset = products_filter(actual=True)

    context = {
        'page_header': 'Добавить задачу',
        'form': form
    }
    return render(request, 'tasks/form.html', context)


@login_required(login_url='login')
def tasks_view(request, pk):
    task = access_filter(request).task(pk=pk)
    context = {'task': task}
    return render(request, 'tasks/view.html', context)


@login_required(login_url='login')
def tasks_update(request, pk):
    task = access_filter(request).task(pk=pk)
    done_initial = task.done

    # не возможны корректировки, если задача отмечена выполненной и вы не создатель задачи
    if task.done is True and task.creator != request.user:
        messages.warning(request, 'Задача выполнена. Для корректировок обратитесь к постановщику задачи')
        return redirect('tasks:view', task.id)

    form = TaskForm(instance=task)
    form.fields['responsible'].queryset = access_filter(request).users()
    form.fields['customer'].queryset = access_filter(request).customers()
    form.fields['contact'].queryset = access_filter(request).contacts(customer=task.customer if task.customer else 0, actual=True, chosen=task.contact)
    form.fields['project'].queryset = access_filter(request).projects(customer=task.customer if task.customer else 0, archive=False, chosen=task.project)
    form.fields['product'].queryset = products_filter(actual=True, chosen=task.product)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=False)
            # если задача не была выполнена, то обновляем дату выполнения
            if done_initial is False and form.instance.done is True:
                form.instance.done_date = datetime.datetime.now()
            form.save()
            context = {'task': task}
            return render(request, 'tasks/view.html', context)

        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('tasks:view', pk=pk)

    context = {
        'page_header': 'Обновить задачу',
        'form': form
    }
    return render(request, 'tasks/form.html', context)


@login_required(login_url='login')
def tasks_delete(request, pk):
    task = access_filter(request).task(pk=pk)

    # удалить задачу может только постановщик
    if task.creator != request.user:
        messages.warning(request, 'Удалить задачу может только постановщик')
        return redirect('tasks:view', task.id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:list')

    return render(request, 'delete-confirm.html', {'obj': task})


@login_required(login_url='login')
def tasks_list_for_today(request):
    access = access_filter(request)
    tasks_initial = access.tasks().filter(responsible=request.user).filter(done=False).filter(reminder=datetime.date.today())
    tasks = choice_filter(tasks_initial, request)

    context = {
        'page_header': 'Задачи на сегодня',
        'tasks': tasks.list,
        'dropdown': access,
        'filter_choice': tasks.filter_choice
    }
    return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def tasks_list_expired(request):
    access = access_filter(request)
    tasks_initial = access.tasks().filter(responsible=request.user).filter(done=False).filter(reminder__lt=datetime.date.today())
    tasks = choice_filter(tasks_initial, request)

    context = {
        'page_header': 'Задачи просроченные',
        'tasks': tasks.list,
        'dropdown': access,
        'filter_choice': tasks.filter_choice
    }
    return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def tasks_list_i_creator(request):
    access = access_filter(request)
    tasks_initial = access.tasks().filter(creator=request.user).exclude(responsible=request.user)
    tasks = choice_filter(tasks_initial, request)

    tasks.choice('done', 'False')
    tasks.choice('reminder_from')
    tasks.choice('reminder_till')

    context = {
        'page_header': 'Задачи поставленные мной',
        'tasks': tasks.list,
        'dropdown': access,
        'filter_choice': tasks.filter_choice
    }
    return render(request, 'tasks/list.html', context)
