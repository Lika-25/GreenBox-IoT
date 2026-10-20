from django.views import generic
from django.urls import reverse_lazy
from .models import GreenhouseInfo
from .forms import GreenhouseInfoForm

# Страница просмотра параметров (твоя главная страница)
class DashboardView(generic.ListView):
    model = GreenhouseInfo
    context_object_name = 'greenhouses'
    template_name = 'dashboard.html'

# Страница добавления новых параметров (POST-форма)
class AddInfoView(generic.CreateView):
    form_class = GreenhouseInfoForm
    template_name = 'add_info.html'
    success_url = reverse_lazy('dashboard')