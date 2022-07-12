from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_list, name='list'),
    path('create', views.users_create, name='create'),
    path('<int:pk>/update', views.users_update, name='update'),
]
