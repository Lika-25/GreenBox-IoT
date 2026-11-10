from django.views import generic
from django.urls import reverse_lazy
from .models import GreenhouseInfo
from .forms import GreenhouseInfoForm
import pymongo
from django.shortcuts import render

# Сторінка перегляду параметрів головна
class DashboardView(generic.ListView):
    model = GreenhouseInfo
    context_object_name = 'greenhouses'
    template_name = 'dashboard.html'

# Сторінка додавання нових параметрів (POST-форма)
class AddInfoView(generic.CreateView):
    form_class = GreenhouseInfoForm
    template_name = 'add_info.html'
    success_url = reverse_lazy('dashboard')



def user_list_view(request):
    # Підключення до MongoDB
    client = pymongo.MongoClient('localhost', 27017)
    db = client['GreenBox_Users_DB']
    users = list(db['users'].find()) 
    
    return render(request, 'user_list.html', {'users': users})