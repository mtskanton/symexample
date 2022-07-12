from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contacts_list, name='list'),
    path('create', views.contacts_create, name='create'),
    path('<int:pk>', views.contacts_view, name='view'),
    path('<int:pk>/update', views.contacts_update, name='update'),
    path('<int:pk>/delete', views.contacts_delete, name='delete'),
]
