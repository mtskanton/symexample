from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks_list, name='list'),
    path('create', views.tasks_create, name='create'),
    path('<int:pk>', views.tasks_view, name='view'),
    path('<int:pk>/update', views.tasks_update, name='update'),
    path('<int:pk>/delete', views.tasks_delete, name='delete'),

    path('for-today', views.tasks_list_for_today, name='for-today'),
    path('expired', views.tasks_list_expired, name='expired'),
    path('i-creator', views.tasks_list_i_creator, name='i-creator'),
]
