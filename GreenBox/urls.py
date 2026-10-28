from django.contrib import admin
from django.urls import path, include
from monitoring.views import DashboardView, AddInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('create/', AddInfoView.as_view(), name='add_info'),
    path('sensors/', include('sensors.urls')),
    path('security/', include('security.urls')),
    path('analytics/', include('analytics.urls')),
]
