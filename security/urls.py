from django.urls import path
from . import views

urlpatterns = [
    path('', views.security_list, name='security_list'),
    path('add/', views.add_security_measure, name='add_security'),
    path('toggle/<int:pk>/', views.toggle_security_status, name='toggle_security'),
    path('delete/<int:pk>/', views.delete_security_measure, name='delete_security'),
]