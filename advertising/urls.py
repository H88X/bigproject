from django.urls import path
from . import views

app_name = 'advertising'

urlpatterns = [
    path('', views.my_view, name='my-view'),
    path('<int:client_id>/', views.client_advertising_list, name='client_advertising_list'),
]