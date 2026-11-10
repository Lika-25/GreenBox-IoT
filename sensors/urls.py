from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_list, name='sensor_list'),
    path('add/', views.add_sensor, name='add_sensor'),
]