from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import dependent_select_options
from users.forms import LoginForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "users/login.html"


@login_required(login_url='login')
def summary(request):
    context = {}
    return render(request, 'summary.html', context)


@login_required(login_url='login')
#контроллер для связанных списков
def dependent_select(request):
    return dependent_select_options(request)
