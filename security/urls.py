from django.urls import path
from . import views

urlpatterns = [
    path('', views.security_list, name='security_list'),
    path('toggle/<str:threat_id>/', views.toggle_threat_status, name='toggle_threat'),
    path('delete/<str:threat_id>/', views.delete_threat, name='delete_threat'),
    path('add/', views.add_security, name='add_threat'),
]