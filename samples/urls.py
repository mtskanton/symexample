from django.urls import path
from . import views

app_name = 'samples'

urlpatterns = [
    path('', views.samples_list, name='list'),
    path('create', views.samples_create, name='create'),
    path('<int:pk>', views.samples_view, name='view'),
    path('<int:pk>/update', views.samples_update, name='update'),
    path('<int:pk>/delete', views.samples_delete, name='delete'),

    path('on-testing', views.samples_list_on_testing, name='on-testing'),
    path('win', views.samples_list_win, name='win'),
    path('declined-by-properties', views.samples_list_declined_properties, name='declined-properties'),
    path('declined-by-price', views.samples_list_declined_price, name='declined-price'),
    path('send', views.samples_list_send, name='send'),
    path('send-directly', views.samples_list_send_directly, name='send-directly'),
    path('abandoned', views.samples_list_abandoned, name='abandoned'),
]
