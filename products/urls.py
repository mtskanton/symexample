from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list, name='list'),
    path('create', views.products_create, name='create'),
    path('<int:pk>', views.products_view, name='view'),
    path('<int:pk>/update', views.products_update, name='update'),
    path('<int:pk>/delete', views.products_delete, name='delete'),
]
