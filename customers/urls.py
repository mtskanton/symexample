from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customers_list, name='list'),
    path('create', views.customers_create, name='create'),
    path('<int:pk>', views.customers_view, name='view'),
    path('<int:pk>/update', views.customers_update, name='update'),
    path('<int:pk>/delete', views.customers_delete, name='delete'),
]
