from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_list, name='list'),
    path('create', views.projects_create, name='create'),
    path('<int:pk>', views.projects_view, name='view'),
    path('<int:pk>/update', views.projects_update, name='update'),
    path('<int:pk>/delete', views.projects_delete, name='delete'),
]
