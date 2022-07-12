from django.shortcuts import render, redirect
from users.forms import UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User
from django.contrib import messages


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def users_list(request):
    users = User.objects.all()

    context = {
        'page_header': 'Пользователи',
        'users': users,
    }
    return render(request, 'users/list.html', context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def users_create(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.password = make_password(instance.password)
            instance.save()
            return redirect('summary')
    else:
        form = UserForm()

    context = {
        'form': form,
        'page_header': 'Регистрация пользователя'
    }
    return render(request, 'users/form.html', context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def users_update(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    form.initial['password'] = '*****'

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        current_password = user.password
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.password != '*****':
                instance.password = make_password(instance.password)
            else:
                instance.password = current_password
            instance.save()
            messages.success(request, 'Информация обновлена')
            return redirect('users:update', pk=pk)
        else:
            messages.error(request, 'Ошибка при обновлении')
            return redirect('users:update', pk=pk)

    context = {
        'page_header': 'Обновить пользователя',
        'form': form
    }
    return render(request, 'users/form.html', context)

