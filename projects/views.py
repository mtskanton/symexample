from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from symcrm.access_filter import access_filter
from symcrm.choice_filter import choice_filter
from django.contrib import messages


@login_required(login_url='login')
def projects_list(request):
    access = access_filter(request)
    projects = choice_filter(access.projects(), request)

    projects.choice('archive', 'False')
    projects.choice('organisation', request.user.organisation.id)
    projects.choice('user')

    context = {
        'page_header': 'Проекты',
        'projects': projects.list,
        'dropdown': access,
        'filter_choice': projects.filter_choice
    }
    return render(request, 'customers/projects/list.html', context)


@login_required(login_url='login')
def projects_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm()
        # значения по умолчанию при создании из карточки какой-либо сущности
        default_customer = request.GET.get('customer', '')
        form.fields['customer'].initial = default_customer

        # фильтрация списков выбора
        form.fields['customer'].queryset = access_filter(request).customers()
        form.fields['contact'].queryset = access_filter(request).contacts(customer=0, actual=True)

    context = {
        'page_header': 'Добавить проект',
        'form': form
    }
    return render(request, 'customers/projects/form.html', context)


@login_required(login_url='login')
def projects_view(request, pk):
    project = access_filter(request).project(pk=pk)
    tasks = project.task_set.all()
    samples = project.sample_set.all()

    context = {
        'project': project,
        'tasks': tasks,
        'samples': samples,
        'subform_settings': '_project_subform',
    }
    return render(request, 'customers/projects/view.html', context)


@login_required(login_url='login')
def projects_update(request, pk):
    project = access_filter(request).project(pk=pk)
    form = ProjectForm(instance=project)
    form.fields['customer'].queryset = access_filter(request).customers()
    form.fields['contact'].queryset = access_filter(request).contacts(customer=project.customer if project.customer else 0, actual=True, chosen=project.contact)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            context = {'project': project}
            return render(request, 'customers/projects/view.html', context)
        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('contacts:view', pk=pk)

    context = {
        'page_header': 'Обновить проект',
        'form': form
    }
    return render(request, 'customers/projects/form.html', context)


@login_required(login_url='login')
def projects_delete(request, pk):
    project = access_filter(request).project(pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')

    return render(request, 'delete-confirm.html', {'obj': project})
